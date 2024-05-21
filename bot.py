# message_logger.py

import discord
import logging
import aiohttp
import os
from logging.handlers import TimedRotatingFileHandler
from discord.ext import commands

# Set up logging to a file with daily rotation
handler = TimedRotatingFileHandler('discord.log', when="midnight", interval=1)
handler.suffix = "%Y-%m-%d"
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
                    handlers=[handler])

# Create an instance of a bot
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Ensure the directory exists for storing images
if not os.path.exists('images'):
    os.makedirs('images')

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} - {bot.user.id}')
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.event
async def on_message(message):
    logging.info(f'Message from {message.author}: {message.content}')
    # Download and log attachments
    if message.attachments:
        for attachment in message.attachments:
            await download_attachment(attachment)
    await bot.process_commands(message)  # Ensure other commands still work

@bot.event
async def on_message_delete(message):
    logging.info(f'Message deleted from {message.author}: {message.content}')
    # Log deleted attachments
    if message.attachments:
        for attachment in message.attachments:
            logging.info(f'Deleted attachment from {message.author}: {attachment.url}')

@bot.event
async def on_message_edit(before, after):
    logging.info(f'Message edited from {before.author}: {before.content} -> {after.content}')
    # Log edited attachments
    if before.attachments or after.attachments:
        before_attachments = [attachment.url for attachment in before.attachments]
        after_attachments = [attachment.url for attachment in after.attachments]
        logging.info(f'Attachments edited from {before_attachments} to {after_attachments}')

async def download_attachment(attachment):
    async with aiohttp.ClientSession() as session:
        async with session.get(attachment.url) as response:
            if response.status == 200:
                file_path = os.path.join('images', attachment.filename)
                with open(file_path, 'wb') as f:
                    f.write(await response.read())
                logging.info(f'Downloaded attachment: {attachment.url} to {file_path}')
            else:
                logging.error(f'Failed to download attachment: {attachment.url}')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN_HERE')
