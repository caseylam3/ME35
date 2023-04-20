import time
import requests
import json 

URL = ''


response = requests.get(url = URL, params = {})
data = response.json()

def getReady():
    # retrieves value for transport task for picking up the cup at the start
# retrieves value for transport task for picking up the cup at the start
    cup_pick_up = dataTask['records'][1]['fields']['Ready for Robot']

    # retrieves value for transport task for going to portioning
    ice_pick_up = dataTask['records'][2]['fields']['Deployed?']

    # retrieves value for portioning task to begin portioning
    portioning = dataTask['records'][3]['fields']['Deployed?']

    # retrieves value for transport task to pick up portioned items
    transport3 = dataTask['records'][4]['fields']['Deployed?']

    # retrieves value for transport task to go to processing
    transport4 = dataTask['records'][5]['fields']['Deployed?']

    # value for processing task to process food
    processing = dataTask['records'][6]['fields']['Deployed?']

    # value for transport task to pick up processed 
    transport5 = dataTask['records'][7]['fields']['Deployed?']

    # value for transport to bring to blending
    transport6 = dataTask['records'][8]['fields']['Deployed?']

    # value for blending to start blending process
    blending = dataTask['records'][9]['fields']['Deployed?']

    # value for blending to clean - can happen asynchronously from chronological process
    blendingC = dataTask['records'][10]['fields']['Deployed?']

    transport7 = dataTask['records'][11]['fields']['Deployed?']

    return transport1, transport2, transport3, transport4, transport5, transport6, transport7, portioning, processing, blending, blendingC

  
