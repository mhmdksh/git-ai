# Import necessary libraries
import os
import time
import subprocess
import threading
from dotenv import load_dotenv

# ... (rest of your imports)
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

# Load environment variables from .env file
load_dotenv()

# Get environment variables
access_token = os.getenv('GITHUB_ACCESS_TOKEN')
output_file = os.getenv('OUTPUT_FILE')
repo_name = os.getenv('REPO_NAME')

# Set the GitHub access token and OpenAI API key as environment variables
os.environ['GITHUB_ACCESS_TOKEN'] = access_token
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

def sync_repo():
    while True:
        subprocess.run(['gh2md', repo_name, output_file])
        time.sleep(60)  # Wait for 60 seconds before updating again

# Create a new thread for the synchronization process
sync_thread = threading.Thread(target=sync_repo)

# Start the new thread
sync_thread.start()

#loader = DirectoryLoader('data/', glob="**/*.md", loader_cls=TextLoader)
#print(f"Loader created with file: {output_file}")
#index = VectorstoreIndexCreator().from_loaders([loader])
## Create a ConversationalRetrievalChain object
#chain = ConversationalRetrievalChain.from_llm(
#  llm=ChatOpenAI(model="gpt-3.5-turbo"),
#  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
#)

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = DirectoryLoader('data/', glob="**/*.md", loader_cls=TextLoader)
  print(f"Loader created with file: {output_file}")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

# Create a ConversationalRetrievalChain object
chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Initialize an empty list to store the chat history
chat_history = []

# Define a function to ask a question
def ask_question(query):
  # Use the ConversationalRetrievalChain to generate an answer
  result = chain({"question": query, "chat_history": chat_history})
  answer = result['answer']

  # Append the question and answer to the chat history
  chat_history.append((query, result['answer']))

  # Return the answer
  return answer