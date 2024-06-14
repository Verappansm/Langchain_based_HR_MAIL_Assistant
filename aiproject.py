from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
import os
from datetime import datetime
import schedule
import time
import imaplib

os.environ['OPENAI_API_KEY'] = 'sk-proj-KK7x97999u4UE66vIQdNT3BlbkFJkvbR1vXPbxSuBmle0LXA'

def check_for_new_email():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("shahishnu379@gmail.com", "uczm hshi wwsv potn")
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    if result == 'OK' and data[0]:
        return True
    return False

def mark_email_as_seen():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("shahishnu379@gmail.com", "uczm hshi wwsv potn")
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    if result == 'OK' and data[0]:
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Seen')
        print("Email marked as seen.")
    else:
        print("No unseen emails found.")


def run_email_agent():
    if check_for_new_email():
        toolkit = GmailToolkit()
        current_date = datetime.now().strftime("%B %d, %Y")
        llm = ChatOpenAI(temperature=0.4)
        agent = initialize_agent(tools=toolkit.get_tools(), llm=llm, verbose=True, max_iterations=1000, max_execution_time=1600, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
        email_content = f"Use the current date: {current_date},now draft an email to ramyajaysha@gmail.com by using the content present in the latest email received in inbox and transforming the data in the manner that is stated below: first display Date of 'From Date', then display Date of 'To Date', then display date of 'Current Date',then only display the 'reason' if specified ,then display the 'sender's email address', provide actual dates by using the content in the latest email from inbox, if necessary do calculations needed to find the dates if not specified"

        print(agent.run(email_content))

# Schedule the email check and agent run every 10 seconds
schedule.every(10).seconds.do(run_email_agent)
schedule.every(10).seconds.do(mark_email_as_seen)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)