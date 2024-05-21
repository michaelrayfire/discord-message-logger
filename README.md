Discord Logging Bot
Overview
This bot is designed to provide comprehensive logging capabilities for your Discord server. It is both open-source and private, giving users full control over its functionalities.

Features
Message Logging: Logs all messages, including deleted and edited ones.
Image Saving: Automatically downloads and saves images shared in the server.
IPv4 Logging (Coming Soon): A feature for the private bot to log IPv4 addresses, controlled by the user through an open interface.
Open Source
The core functionalities of the bot are open-source, allowing for community contributions and transparency in how the bot operates.

Usage
Clone the Repository:


git clone https://github.com/yourusername/discord-logging-bot.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up the Bot:

Create a new application on the Discord Developer Portal.
Enable the required intents in the "Bot" settings.
Copy your bot token and add it to a .env file:
makefile
Copy code
DISCORD_BOT_TOKEN=your_bot_token_here
Run the Bot:


python message_logger.py
Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
