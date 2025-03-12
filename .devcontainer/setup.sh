#!/bin/bash

# Actualizar paquetes e instalar Chrome
sudo apt-get update
sudo apt-get install -y google-chrome-stable

# Instalar ChromeDriver
CHROME_VERSION=$(google-chrome --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
wget -N https://chromedriver.storage.googleapis.com/$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION})/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Instalar dependencias de Python con python3 (3.11)
python3 -m pip install --upgrade pip
python3 -m pip install selenium