import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.chat_models import AzureChatOpenAI
from tools import get_tools

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_KEY"),
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
    temperature=0.7
)

agent_executor = initialize_agent(
    tools=get_tools(),
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def ask_agent(question: str) -> str:
    return agent_executor.run(question)
