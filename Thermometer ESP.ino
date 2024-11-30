#include <WiFi.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const char* ssid = "";          // Замініть на ваш SSID
const char* password = "";    // Замініть на ваш пароль
// Дані для сервера
const char* host = "";     // IP вашого сервера
const uint16_t port = 1235;            // Порт сервера

WiFiClient client;

// Налаштування DS18B20
#define ONE_WIRE_BUS 4 // Пін, до якого підключено DS18B20
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void connectToServer() {
  while (!client.connect(host, port)) {
    Serial.println("Не вдалося підключитися до сервера. Спроба через 5 секунд...");
    delay(5000);
  }
  Serial.println("Успішне підключення до сервера!");
}

void setup() {
  Serial.begin(115200);

  // Підключення до Wi-Fi
  Serial.println("Підключення до Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi підключено!");
  Serial.print("IP-адреса ESP32: ");
  Serial.println(WiFi.localIP());

  // Ініціалізація датчика
  sensors.begin();
  
  // Спроба підключення до сервера
  connectToServer();
}

void loop() {
  if (!client.connected()) {
    Serial.println("З'єднання з сервером втрачено. Спроба повторного підключення...");
    connectToServer();
  }

  // Читання температури
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0); // Отримати температуру першого датчика

  // Перевірка, чи температура коректна
  if (temperature != DEVICE_DISCONNECTED_C) {
    Serial.printf("Температура: %.2f °C\n", temperature);

    // Відправка даних на сервер
    client.printf("Температура: %.2f °C\n", temperature);
  } else {
    Serial.println("Помилка читання температури!");
  }

  delay(5000); // Затримка між читаннями
}
