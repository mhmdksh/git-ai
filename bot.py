# bot.py

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from explore import ask_question

# Load environment variables from .env file
load_dotenv()

# Get the Discord token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize the bot with all intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ask(ctx, *, question):
    # Call the ask_question function from explore.py
    answer = ask_question(question)

    # Send the answer to the Discord channel
    await ctx.send(answer)

# Run the bot
bot.run(DISCORD_TOKEN)

