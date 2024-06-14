from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
import os
from datetime import datetime
import schedule
import time
import imaplib
import email
os.environ['OPENAI_API_KEY'] = 'sk-proj-KK7x97999u4UE66vIQdNT3BlbkFJkvbR1vXPbxSuBmle0LXA'

def check_for_new_email():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("shahishnu379@gmail.com", "uczm hshi wwsv potn")
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    if result == 'OK' and data[0]:
        return data[0].split()
    return []

"""def mark_email_as_seen():
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
"""
def run_final():
    new_emails = check_for_new_email()
    for emailid in new_emails:
        run_email_agent(emailid)


def run_email_agent(email_id):
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("shahishnu379@gmail.com", "uczm hshi wwsv potn")
    mail.select('inbox')
    result, data = mail.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    sender_email = email_message['From']
    email_content = email_message.get_payload()


    toolkit = GmailToolkit()
    current_date = datetime.now().strftime("%B %d, %Y")
    llm = ChatOpenAI(temperature=0.4)
    agent = initialize_agent(tools=toolkit.get_tools(), llm=llm, verbose=True, max_iterations=1000, max_execution_time=1600, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
    email_content = f"Use the current date: {current_date},now create a draft to ramyajaysha@gmail.com by using the content :{email_content} and transforming the data in the manner that is stated below: first display Date of 'From Date', then display Date of 'To Date', then display date of 'Current Date',then only display the 'reason' if specified ,then display the {sender_email}, provide actual dates , if necessary do calculations needed to find the dates if not specified using calendar"

    print(agent.run(email_content))
    mail.store(email_id, '+FLAGS', '\\Seen')

# Schedule the email check and agent run every 10 seconds
schedule.every(10).seconds.do(run_final)


# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)