# git-ai
A personal git helper discord bot for your github repository
## Problem?
Back and forth github links about issues and pull requests between team memebers. Results in too many links in discord, things can get lost easily, and a lot of time can be wasted
## Solution
A build in discord bot that guides the chat participants on specific issues, pull requests and comments on the specific git repositories that they are working on
## Diagram

```
User (on Discord) <--> Discord API <--> Chatbot (Discord Bot)
                                       |
                                       --> OpenAI API (for generating responses and learning from conversations)
                                       |
                                       --> GitHub Token (for scanning Github repository information)
```
## Prerequisites
1. Discord Bot Setup and a Discord Token
2. Access token for your Github Account
3. OpenAI API Key for OpenAI integration
4. Python ~ `3.9.7`
## Configure
Configure the .env using the `.env.template` file
```
cp .env.template .env
```
Example:
```
OPENAI_API_KEY=your-openai-api-key
DISCORD_TOKEN=your-bot-token
GITHUB_ACCESS_TOKEN=your-github-access-token
OUTPUT_FILE=data/git_output_file.txt
REPO_NAME=repo-owner/repo-name
```
## Install & Configure
### Install dependencies using this command
```
pip install -r requirements.txt
```
### (Optional) Add Your own Text data in the `data` folder

## Start
```
python bot.py
```
Or just use docker-compose
```
docker-compose up -d
```
