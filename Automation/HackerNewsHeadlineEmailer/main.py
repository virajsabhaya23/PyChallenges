import requests
from bs4 import BeautifulSoup

#SENDS THE MAIL
import smtplib

#EMAIL BODY
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

content = ''

#EXTRACTING NEWS STORIES
def extract_news(url):
    print("\nEXTRACTING HACKER NEWS STORIES ...")
    cnt = ''
    cnt += ('<b>HN TOP STORIES:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(response,'html.parser')

    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1) + ' :: '))