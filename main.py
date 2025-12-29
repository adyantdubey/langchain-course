from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query:str) -> str:
    """
    Tool to search the web for current information.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Searching for {query}...")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Get me 4 job openings for a person with business experience in tech field near Thane, maharashtra and link their details")]})
    print(result)
    

if __name__ == "__main__":
    main()
