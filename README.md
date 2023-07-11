# git-ai

## Diagram

```
User (on Discord) <--> Discord API <--> Chatbot (Discord Bot)
                                       |
                                       --> OpenAI API (for generating responses and learning from conversations)
                                       |
                                       --> GitHub Token (for scanning Github repository information)
```
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
### Add Text data in the `data` folder

## Start
```
python bot.py
```
