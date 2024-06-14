from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
import os
from datetime import datetime
import schedule
import time
import imaplib

# Set up environment variables
os.environ['OPENAI_API_KEY'] = 'sk-proj-KK7x97999u4UE66vIQdNT3BlbkFJkvbR1vXPbxSuBmle0LXA'

# Email credentials
#EMAIL = 'your_email@gmail.com'
#PASSWORD = 'your_password'

def check_for_new_email():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("smverappan@gmail.com", "ifwg xeml wxvz kzut")
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    if result == 'OK' and data[0]:
        return True
    return False

def run_email_agent():
    if check_for_new_email():
        toolkit = GmailToolkit()
        current_date = datetime.now().strftime("%B %d, %Y")
        llm = ChatOpenAI(temperature=0.0)
        agent = initialize_agent(tools=toolkit.get_tools(), llm=llm, verbose=True, max_iterations=1000, max_execution_time=1600, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
        email_content = f"Use the current date: {current_date}, draft an email to sair62995@gmail.com by writing the content present in the latest email received in inbox and transforming the data in a manner that is stated below: first display Date of 'From Date', then display Date of 'To Date', then display date of 'Current Date', provide actual dates by using the content in the latest email from inbox, if necessary do calculations needed to find the dates if not specified"

        print(agent.run(email_content))

# Schedule the email check and agent run every 10 seconds
schedule.every(10).seconds.do(run_email_agent)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)