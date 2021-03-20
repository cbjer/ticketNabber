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
    assert(len(names) == 1)
    uniqueName = names[0]

    assert(len(uniqueName.contents) == 1)
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
    assert(len(eventCode) == EVENT_CODE_LENGTH)

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
    assert(len(ticketTags) == expectedNumberTickets)

