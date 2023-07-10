import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sys
sys.path.insert(1, './chatgpt.py')
import chatgpt  # This is the script from the chatgpt-retrieval repository

# Load environment variables from .env file
load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ask(ctx, *, question):
    response = chatgpt.main(question)  # Assuming the main function in chatgpt.py takes a question as argument and returns the answer
    await ctx.send(response)

# Get the Discord token from the environment variables
token = os.getenv('DISCORD_TOKEN')

bot.run(token)

