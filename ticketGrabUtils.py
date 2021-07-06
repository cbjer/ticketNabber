from bs4 import BeautifulSoup
import bs4
import requests

EVENT_CODE_LENGTH = 7
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def getAvailableTickets(url, ignoreTickets, expectedNumberTickets):
    soup = getTicketWidgetSoup(url)
    ticketTags = getTicketTags(soup)
    checkCorrectTicketsReturned(ticketTags, expectedNumberTickets)
    ticketNamesStatus = getTicketNamesAndStatus(ticketTags)
    goodTickets = filterAvailableTickets(ticketNamesStatus, ignoreTickets)

    return goodTickets

def getTicketWidgetSoup(url):
    eventCode = getEventCode(url)
    widgetLink = getTicketWidgetUrl(eventCode)
    return getSoup(widgetLink)

def getTicketNameFromTag(tag):
    CLASS_TYPES = ['pr8', 'type-title']
    names = []
    for classType in CLASS_TYPES:
        names += tag.find_all('div', attrs={'class' : classType})

    if len(names) != 1:
        raise AssertionError("More than 1 name found in tag")

    uniqueName = names[0]

    if len(uniqueName.contents) != 1:
        raise AssertionError("More than 1 ticket name found in tag")

    return uniqueName.contents[0]

def isTicketNotClosed(tag):
    return tag['class'][0] != 'closed' 

def getTicketTags(soup):
    divs = soup.find_all("ul", attrs={"data-ticket-info-selector-id" : "tickets-info"})[0]
    ticketTags = []
    for d in divs:
        if type(d) is bs4.element.Tag:
            ticketTags.append(d)

    return ticketTags

def getEventCode(eventUrlString):
    s = eventUrlString.split('/')
    s = [i for i in s if i != '']
    eventCode = s[-1]

    if len(eventCode) != EVENT_CODE_LENGTH:
        raise AssertionError("Event code not expected length", eventCode)
    
    return eventCode

def getTicketWidgetUrl(eventCode):
    PREFIX = "https://ra.co/widget/event/"
    SUFFIX = "/embedtickets"
    return PREFIX + eventCode + SUFFIX

def getSoup(webUrl):
    req = requests.get(webUrl, headers=HEADERS)
    soup = BeautifulSoup(req.content, 'lxml')
    return soup

def getTicketNamesAndStatus(ticketTags):
    ticketTuples = []
    for tag in ticketTags:
        name = getTicketNameFromTag(tag)
        isNotClosed = isTicketNotClosed(tag)
        ticketTuples.append((name, isNotClosed))
    return ticketTuples

def filterAvailableTickets(ticketNamesStatus, ignoreTickets):
    goodTickets = []
    for name, isNotClosed in ticketNamesStatus:
        if isNotClosed and name not in ignoreTickets:
            goodTickets.append(name)

    return goodTickets

def checkCorrectTicketsReturned(ticketTags, expectedNumberTickets):
    if len(ticketTags) != expectedNumberTickets:
        raise AssertionError("Error with number of tickets returned. Expected: ", expectedNumberTickets, " Number Returned: ", len(ticketTags))

def parseTicketDictionary(ticketDetailDict):
    url = ticketDetailDict['url']
    ignoreTickets = ticketDetailDict['ignoreTickets']
    expectedNumberTickets = ticketDetailDict['expectedNumberTickets']
    return url, ignoreTickets, expectedNumberTickets

