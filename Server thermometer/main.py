import socket
import threading
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Telegram Bot налаштування
BOT_TOKEN = ""
CHAT_ID = ""  # ID користувача чи групи, де працює бот
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Налаштування сервера
HOST = '0.0.0.0'
PORT = 1235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = []
current_temperature = 0.0  # Поточна температура
critical_temperature = 30.0  # Початкова критична температура
spam_flag = False  # Флаг для спаму


async def broadcast_to_telegram(message):
    """Асинхронне відправлення повідомлень у Telegram."""
    try:
        await bot.send_message(CHAT_ID, message)
        print(f"[Telegram] Відправлено: {message}")
    except Exception as e:
        print(f"[Telegram Помилка] {e}")


def handle_client(client_socket, client_address, loop):
    """Обробка підключеного клієнта."""
    global current_temperature, spam_flag

    print(f"[НОВЕ З'ЄДНАННЯ] {client_address} підключився.")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")

            # Обробка повідомлення від ESP32
            if "Температура" in message:
                try:
                    current_temperature = float(message.split(":")[1].strip().replace("°C", ""))
                    print(f"Оновлено температуру: {current_temperature} °C")

                    # Автоспам при перевищенні критичної температури
                    if current_temperature > critical_temperature and not spam_flag:
                        spam_flag = True
                        asyncio.run_coroutine_threadsafe(spam_temperature_alert(), loop)
                    elif current_temperature <= critical_temperature:
                        spam_flag = False
                except ValueError:
                    print("Помилка обробки температури!")
    except Exception as e:
        print(f"[ПОМИЛКА] {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()
        print(f"[ВІДКЛЮЧЕННЯ] {client_address} відключився.")


def accept_connections(loop):
    """Прийом нових клієнтів."""
    print("[ЗАПУСК СЕРВЕРА] Очікування підключень...")
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, loop))
        thread.start()


async def spam_temperature_alert():
    """Автоспам при перевищенні критичної температури."""
    global spam_flag
    while spam_flag:
        await broadcast_to_telegram(f"⚠️ Температура перевищила критичну! Поточна: {current_temperature} °C")
        await asyncio.sleep(10)  # Інтервал між спамом


# Telegram: обробка команд
@dp.message_handler(commands=["start", "help"])
async def start_command(message: types.Message):
    """Обробка /start і /help."""
    # Нижнє меню
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Отримати температуру"))
    keyboard.add(KeyboardButton("Встановити критичну температуру"))
    await message.answer("Виберіть дію:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Отримати температуру")
async def get_temperature(message: types.Message):
    """Обробка запиту температури."""
    global current_temperature
    await message.answer(f"Поточна температура: {current_temperature} °C")


@dp.message_handler(lambda message: message.text == "Встановити критичну температуру")
async def set_critical_temp_prompt(message: types.Message):
    """Запит на встановлення критичної температури."""
    await message.answer("Введіть нове значення критичної температури (у °C):")


@dp.message_handler()
async def handle_text_message(message: types.Message):
    """Обробка текстових повідомлень (наприклад, зміна критичної температури)."""
    global critical_temperature
    try:
        new_temp = float(message.text.strip())
        critical_temperature = new_temp
        await message.answer(f"Критичну температуру змінено на: {critical_temperature} °C")
    except ValueError:
        await message.answer("Будь ласка, введіть коректне число для температури.")


# Основна функція для запуску
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server_thread = threading.Thread(target=accept_connections, args=(loop,), daemon=True)
    server_thread.start()

    print("[Telegram Bot] Запуск бота...")
    executor.start_polling(dp, skip_updates=True)
