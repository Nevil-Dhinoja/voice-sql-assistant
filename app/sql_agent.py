from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import \
    create_sql_agent
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_agent(db_path="data/school.db"):
    engine = create_engine(f"sqlite:///{db_path}")
    db = SQLDatabase(engine)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # free tier
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )
    agent = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        agent_type="zero-shot-react-description"
    )
    return agent

def query(agent, question: str) -> str:
    try:
        result = agent.invoke({"input": question})
        return result["output"]
    except Exception as e:
        return f"Error: {e}"