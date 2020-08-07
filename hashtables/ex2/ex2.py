#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = []
    ticket_map = {}
    
    ## find the first case
    for ticket in tickets:
        #print(ticket.source)
        #print(ticket.destination)
        ticket_map[ticket.source] = ticket.destination

    # if 'NONE' in ticket_map :
    #      route = ['NONE', ticket_map['NONE']]

    first_destination = ticket_map['NONE']
    #print(first_destination)

    route.append(first_destination)
    

    #print(ticket_map[next_destination])

    next_destination = ticket_map[first_destination]
    #print(next_destination)

    route.append(next_destination)
    print(route)

    print(ticket_map[next_destination])

    while ticket_map[next_destination] is not 'NONE':
        
         next_destination = ticket_map[next_destination]
         route.append(next_destination)
         print(route)
    route.append("NONE")
    

    #print(ticket_map)

    
    




    return route
