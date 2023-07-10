# bridge-ai

## Diagram

```
User (on Discord) <--> Discord API <--> Chatbot (Rasa or Botpress)
                                       |
                                       --> OpenAI API (for generating responses and learning from conversations)
                                       |
                                       --> GitHub API (for scanning code and learning about DevOps tools)
```
## Configure
Configure the .env using the `.env.template` file
```
cp .env.template .env
```
Example:
```
OPENAI_KEY=your-openai-api-key
DISCORD_BOT_TOKEN=your-discord-bot-token
```
## Install
Install using this command
```
npm install dotenv
```
