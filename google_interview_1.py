"""
Google mock interview question from: https://www.youtube.com/watch?v=qz9tKlF431k

Goal is to find minimum number of routes that must be added to get from
a specified starting airport to all other airports.
"""


airports = ['BGI', 'CDG', 'DEL', 'DOH', 'DSM', 'EWR', 'EYW', 'HND', 'ICN',
            'JFK',  'LGA', 'LHR', 'ORD', 'SAN', 'SFO', 'SIN', 'TLV', 'BUD']


routes = [
    ['DSM', 'ORD'],
    ['ORD', 'BGI'],
    ['BGI', 'LGA'],
    ['SIN', 'CDG'],
    ['CDG', 'BUD'],
    ['DEL', 'DOH'],
    ['DEL', 'CDG'],
    ['TLV', 'DEL'],
    ['EWR', 'HND'],
    ['HND', 'ICN'],
    ['HND', 'JFK'],
    ['ICN', 'JFK'],
    ['JFK', 'LGA'],
    ['EYW', 'LHR'],
    ['LHR', 'SFO'],
    ['SFO', 'DSM'],
    ['SAN', 'EYW'],
]

starting_airport = "LGA"

def minExtraRoutesNeeded(airports, routes, starting_airport):
    # Make directed graphs
    # If all routes make up a single directed graph, than all one need
    # is a route from startingAirport to the root of the graph
    # In case of multiple directed graphs, one needs a route from startingAirport
    # to each of the roots

    directed_graphs = []
    directed_graphs.append(routes[0]) # "Initializing" first graph
    for route in routes[1:]:
        src, dest = route[0], route[1]
        for graph in directed_graphs:
            idx = graph.index(src)
            if idx == len(graph) - 1:
                graph.append(dest)


    return -1;

