import discord
import openai
import requests

# Initialize Discord client
client = discord.Client()

# Initialize OpenAI client
openai.api_key = 'your-openai-api-key'

@client.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == client.user:
        return

    # Generate a response using OpenAI
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=message.content,
      max_tokens=100
    )

    # Send the response back on Discord
    await message.channel.send(response.choices[0].text.strip())

# Start the Discord client
client.run('your-discord-bot-token')

