# bridge-ai

## Diagram

```
User (on Discord) <--> Discord API <--> Chatbot (Rasa or Botpress)
                                       |
                                       --> OpenAI API (for generating responses)
                                       |
                                       --> GitHub API (for scanning code)

```
