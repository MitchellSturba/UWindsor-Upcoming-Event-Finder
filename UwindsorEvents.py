import requests
from bs4 import BeautifulSoup

def GetEventInformation(event):
    #Displays date, event description, time, and location of event
    print(event.text)

#Get the html from uWindsor
req = requests.get('http://www.uwindsor.ca')
r_html = req.text

#convert it into soup
soup = BeautifulSoup(r_html, 'html.parser')
# title = soup.find('span', 'event-col-title').string

print('This weeks events: ')
for event in soup.find_all(class_='frontpage-event-slide'):
    GetEventInformation(event)

dateEvent = input('What day of the month would you like to see the events for? ')
dateNum = int(dateEvent)

req2 = requests.get('http://www.uwindsor.ca/event-calendar/month')
r2_html = req2.text

soup2 = BeautifulSoup(r2_html, 'html.parser')

#Finds the day on the calander and prints the events
for v in soup2.find_all(class_='single-day future'):
    if int(v['data-day-of-month']) == dateNum:
        GetEventInformation(v)

