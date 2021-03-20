"""
Ticket details
"""

TICKETS = {
        'MaidenVoyage' : {
            'url' : 'https://ra.co/events/1342426' ,
            'ignoreTickets' : ['After party only (anytime entry)', 'After party only (2nd release anytime entry)'] ,
            'expectedNumberTickets' : 8
            } ,

        'GalaSunday' : {
            'url' : 'https://ra.co/events/1336874',
            'ignoreTickets' : [],
            'expectedNumberTickets' : 3
            } ,

        'TheCause' : {
            'url' : 'https://ra.co/events/1438483' ,
            'ignoreTickets' : ['Super early bird (entry before midday)', 'Entry after 11pm (2nd release)', 'Entry before 1pm', 
                'Entry after 11pm (final release)'] ,
            'expectedNumberTickets' : 11
            } ,
        }

