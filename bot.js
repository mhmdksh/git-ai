require('dotenv').config();
const Discord = require('discord.js');
const axios = require('axios');
const openai = require('openai');

// Initialize Discord client
const client = new Discord.Client();

// Initialize OpenAI client
openai.apiKey = process.env.OPENAI_KEY;

client.on('message', async message => {
    // Don't respond to ourselves
    if (message.author.bot) return;

    // Generate a response using OpenAI
    const response = await openai.Completion.create({
        engine: 'text-davinci-002',
        prompt: message.content,
        max_tokens: 100
    });

    // Send the response back on Discord
    message.channel.send(response.choices[0].text.strip());
});

// Start the Discord client
client.login(process.env.DISCORD_BOT_TOKEN);

