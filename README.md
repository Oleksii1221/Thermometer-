# Thermometer
  
  This project monitors temperature data from an ESP32 with a DS18B20 sensor and sends critical temperature alerts to a Telegram bot. The bot also allows users to request the current temperature and configure a critical temperature threshold.
  
  ## Features
  - **Temperature Alerts**: Sends a notification to Telegram when the temperature exceeds the critical threshold.
  - **Manual Temperature Requests**: Users can request the current temperature via the bot.
  - **Critical Temperature Configuration**: Users can set a new critical temperature threshold directly from the bot.
  - **Intuitive Interface**: Utilizes a Telegram bot with a bottom navigation menu for easy interaction.
  
  ## Requirements
  - **Hardware**:
    - ESP32 microcontroller
    - DS18B20 temperature sensor
    - Wi-Fi network
  - **Software**:
    - Python 3.8+
    - Libraries: `aiogram`
  
  ## Installation
  
  ## Step 1: Hardware Setup
  1. Connect the DS18B20 sensor to the ESP32:
     - **VCC**: Connect to 3.3V.
     - **GND**: Connect to GND.
     - **Data**: Connect to a GPIO pin (e.g., GPIO4) with a 4.7kΩ pull-up resistor between VCC and Data.
     
  ## Step 2: ESP32 Code
  1. Upload the ESP32 firmware to read temperature data from DS18B20 and send it to the server.
  
  ## Step 3: Server Setup
  1. Clone this repository:
     ```bash
     git clone https://github.com/your-repo/esp32-temperature-monitor.git
     cd esp32-temperature-monitor
2 Install dependencies:
```pip install aiogram```
3 Configure the bot by replacing the following placeholders in main.py:

4 BOT_TOKEN: Your Telegram bot token from BotFather.
CHAT_ID: The Telegram chat ID where alerts will be sent.
Run the server:

README.md
markdown
Копіювати код
## ESP32 Temperature Monitoring with Telegram Bot

This project monitors temperature data from an ESP32 with a DS18B20 sensor and sends critical temperature alerts to a Telegram bot. The bot also allows users to request the current temperature and configure a critical temperature threshold.

## Features
- **Temperature Alerts**: Sends a notification to Telegram when the temperature exceeds the critical threshold.
- **Manual Temperature Requests**: Users can request the current temperature via the bot.
- **Critical Temperature Configuration**: Users can set a new critical temperature threshold directly from the bot.
- **Intuitive Interface**: Utilizes a Telegram bot with a bottom navigation menu for easy interaction.

## Requirements
- **Hardware**:
  - ESP32 microcontroller
  - DS18B20 temperature sensor
  - Wi-Fi network
- **Software**:
  - Python 3.8+
  - Libraries: `aiogram`

## Installation

### Step 1: Hardware Setup
1. Connect the DS18B20 sensor to the ESP32:
   - **VCC**: Connect to 3.3V.
   - **GND**: Connect to GND.
   - **Data**: Connect to a GPIO pin (e.g., GPIO4) with a 4.7kΩ pull-up resistor between VCC and Data.
   
## Step 2: ESP32 Code
1. Upload the ESP32 firmware to read temperature data from DS18B20 and send it to the server.

## Step 3: Server Setup
1. Clone this repository:
     ```bash
     git clone https://github.com/your-repo/esp32-temperature-monitor.git
     cd esp32-temperature-monitor
  Install dependencies:
  

 
  ```pip install aiogram```
  Configure the bot by replacing the following placeholders in main.py:
  
  BOT_TOKEN: Your Telegram bot token from BotFather.
  CHAT_ID: The Telegram chat ID where alerts will be sent.
  Run the server:
    ```python main.py```


## Step 4: Telegram Bot Setup
  Start your bot in Telegram by typing /start.
  Use the provided buttons:
  "Get Temperature": Fetch the current temperature.
  "Set Critical Temperature": Configure a new critical temperature threshold.
## Usage
  The ESP32 sends temperature readings to the server.
  The server monitors the temperature and:
  Sends critical alerts to the Telegram bot if the temperature exceeds the configured threshold.
  Responds to user commands like "Get Temperature" and "Set Critical Temperature."
## Bot Commands
  /start: Starts the bot and displays the menu.
  Get Temperature: Fetches the latest temperature reading.
  Set Critical Temperature: Allows you to set a new critical threshold.
## Example Workflow
  Start the bot by typing /start.
  Set a critical temperature (e.g., 30°C).
  View the current temperature by pressing "Get Temperature".
  If the temperature exceeds 30°C, the bot will send periodic alerts.
## Project Structure
  ```
  ├── main.py                 # Main Python script for the server
  ├── requirements.txt        # Dependencies
  └── README.md               # Documentation
  ```

## Known Issues
Ensure that the ESP32 and server are connected to the same network for seamless communication.
Configure a valid Telegram bot token and chat ID for proper operation.
## Contributions
Contributions are welcome! Please fork this repository and submit a pull request.
