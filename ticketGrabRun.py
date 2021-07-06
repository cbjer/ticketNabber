"""
Main file for running the ticket grab
"""
from ticketDetails import TICKETS
from ticketGrabUtils import getAvailableTickets, parseTicketDictionary
from ticketAlerts import startTicketAlerts
import time

LOOP_PAUSE_TIME = 4
BETWEEN_EVENT_PAUSE_TIME = 2

print("Running for:", list(TICKETS.keys()))

def startTicketSearchLoop():
    loopCount = 0
    playAlert = True

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
                    
                    if playAlert:
                        startTicketAlerts()
                        playAlert = False

            except Exception as err:
                print("Check Page, Error found with", eventName)
                print(str(err))

            time.sleep(BETWEEN_EVENT_PAUSE_TIME)

        time.sleep(LOOP_PAUSE_TIME)

        if loopCount % 10 == 0:
            playAlert = True

startTicketSearchLoop()





