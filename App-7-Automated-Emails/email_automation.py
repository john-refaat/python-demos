import os
import smtplib
import time
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas
import schedule
from dotenv import load_dotenv
from pandas import Series

from news import NewsFeed

load_dotenv()

email_user = os.getenv('email.address')
email_password = os.getenv('email.app.password')


def schedule_email():
    schedule.every().day.at("02:33").do(start_email_automation)

    while True:
        schedule.run_pending()
        time.sleep(60)


def start_email_automation():
    print(f"Starting email automation at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    df = pandas.read_excel('people.xlsx')
    print(df)
    for index, row in df.iterrows():
        feed = NewsFeed(row['name'], row['interest'], from_date=yesterday, to_date=today)
        body = feed.create_email_body()
        print(f'Sending email to {row["name"]}...')
        msg = compose_email(body, row)
        send_email(msg, row)


def compose_email(body: str, row: Series) -> MIMEMultipart:
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = row['email']
    msg['Subject'] = f"Your {row['interest']} News For Today!"
    msg.attach(MIMEText(body, 'plain'))
    return msg


def send_email(msg: MIMEMultipart, row: Series):
    # Retry sending the email up to 4 times
    for attempt in range(1, 5):
        try:
            # Connect to Gmail using standard SMTP port 587 (TLS)
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(email_user, email_password)
                server.send_message(msg)
            print(f'Email sent to {row["name"]}.')
            break
        except Exception as send_err:
            if attempt == 4:
                print(f"Failed to send email to {row['name']} after 4 attempts.")
            else:
                print(f"Attempt {attempt} failed: {send_err}. Retrying...")
            time.sleep(5)


if __name__ == '__main__':
    schedule_email()
