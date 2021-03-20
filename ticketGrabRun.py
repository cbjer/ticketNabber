"""
Main file for running the ticket grab
"""
from ticketDetails import TICKETS
from ticketGrabUtils import getAvailableTickets
from ticketAlerts import startTicketAlerts
import time

LOOP_PAUSE_TIME = 4
BETWEEN_EVENT_PAUSE_TIME = 2

print("Running for:", list(TICKETS.keys()))

def parseTicketDictionary(ticketDetailDict):
    url = ticketDetailDict['url']
    ignoreTickets = ticketDetailDict['ignoreTickets']
    expectedNumberTickets = ticketDetailDict['expectedNumberTickets']
    return url, ignoreTickets, expectedNumberTickets

def startTicketSearchLoop():
    loopCount = 0
    while True:
        loopCount += 1
        print("Starting loop number:", loopCount)
        for eventName in TICKETS:
            url, ignoreTickets, expectedNumberTickets = parseTicketDictionary(TICKETS[eventName])
            try:
                goodTickets = getAvailableTickets(url, ignoreTickets, expectedNumberTickets)

                if len(goodTickets) != 0:
                    print("!!! Ticket Found for", eventName)
                    print(goodTickets)
                    startTicketAlerts()
                    #TODO add found ticket to logger

            except Exception as e:
                print("Check Page, Error found with", eventName)
                print(e)
                startTicketAlerts()
                #TODO add error to a logger

            time.sleep(BETWEEN_EVENT_PAUSE_TIME)

        time.sleep(LOOP_PAUSE_TIME)

startTicketSearchLoop()





