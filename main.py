from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# llm = ChatOllama(temperature=0, model="gemma3:270m")

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Get me 4 job openings for a person with business experience in tech field near Thane, maharashtra and link their details")]})
    print(result)
    

if __name__ == "__main__":
    main()
