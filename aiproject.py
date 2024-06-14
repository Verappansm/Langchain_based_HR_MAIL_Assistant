from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType,initialize_agent
import os
import datetime
os.environ['OPENAI_API_KEY'] = 'sk-proj-KK7x97999u4UE66vIQdNT3BlbkFJkvbR1vXPbxSuBmle0LXA'
toolkit = GmailToolkit()
llm = ChatOpenAI(temperature=0.6)
agent=initialize_agent(tools = toolkit.get_tools(),llm=llm,verbose=True,max_iterations=1000,max_execution_time=1600,agent =AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
prompt = f"draft an email to aiproj@gmail.com by writing the current date: {current_date} and also calculate what will be the next monday by checking current day and write it in the email"
print(agent.run(prompt))