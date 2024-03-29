# bot.py

# Import necessary libraries
import discord
import markdown
from discord.ext import commands
from dotenv import load_dotenv
import os
# Import the ask_question function from explore.py
from explore import ask_question

# Load environment variables from .env file
load_dotenv()

# Get the Discord token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize the bot with all intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command called 'ask'
@bot.command()
async def ask(ctx, *, question):
    # Call the ask_question function from explore.py
    answer = ask_question(question)

    # Send the answer to the Discord channel
    await ctx.send(answer)

# Run the bot
bot.run(DISCORD_TOKEN)
