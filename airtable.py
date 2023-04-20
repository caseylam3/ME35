import time
import requests
import json 

URL = 'https://api.airtable.com/v0/appxFSx1vodDWljqe/TaskOrder?api_key=keyKf7fEzdNw4S7qi'


response = requests.get(url = URL, params = {})
datatask = response.json()

def getReady():
    # retrieves value for transport task for picking up the cup at the start
    Rcup = dataTask['records'][1]['fields']['Ready for Robot']
 
    Rice = dataTask['records'][2]['fields']['Ready for Robot']
    
    Rsmall = dataTask['records'][3]['fields']['Ready for Robot']

    Rprocessed = dataTask['records'][4]['fields']['Ready for Robot']

    Rblender1 = dataTask['records'][5]['fields']['Ready for Robot']

    Rblender2 = dataTask['records'][6]['fields']['Ready for Robot']

    Rpickup1 = dataTask['records'][7]['fields']['Ready for Robot']

    Rpickup2 = dataTask['records'][8]['fields']['Ready for Robot']

    
    return Rcup, Rice, Rsmall, Rprocessed, Rblender1, Rblender2, Rpickup1, Rpickup2

def getDocked():
    # retrieves value for transport task for picking up the cup at the start
    # retrieves value for transport task for picking up the cup at the start
    Dcup = dataTask['records'][1]['fields']['Robot Docked']
 
    # retrieves value for ice station open status
    Dice = dataTask['records'][2]['fields']['Robot Docked']

    # retrieves value for small foods and liquids station open status
    Dsmall = dataTask['records'][3]['fields']['Robot Docked']

    # retrieves value for transport task to pick up portioned items
    Dprocessed = dataTask['records'][4]['fields']['Robot Docked']

    # retrieves value for transport task to go to processing
    Dblender1 = dataTask['records'][5]['fields']['Robot Docked']

    # value for processing task to process food
    Dblender2 = dataTask['records'][6]['fields']['Robot Docked']

    # value for transport task to pick up processed 
    Dpickup1 = dataTask['records'][7]['fields']['Robot Docked']

    # value for transport to bring to blending
    Dpickup2 = dataTask['records'][8]['fields']['Robot Docked']

    
    return Dcup, Dice, Dsmall, Dprocessed, Dblender1, Dblender2, Dpickup1, Dpickup2

def getFinish():
    # retrieves value for transport task for picking up the cup at the start
    # retrieves value for transport task for picking up the cup at the start
    Fcup = dataTask['records'][1]['fields']['Tasked Finished']
 
    # retrieves value for ice station open status
    Fice = dataTask['records'][2]['fields']['Tasked Finished']

    # retrieves value for small foods and liquids station open status
    Fsmall = dataTask['records'][3]['fields']['Tasked Finished']

    # retrieves value for transport task to pick up portioned items
    Fprocessed = dataTask['records'][4]['fields']['Tasked Finished']

    # retrieves value for transport task to go to processing
    Fblender1 = dataTask['records'][5]['fields']['Tasked Finished']

    # value for processing task to process food
    Fblender2 = dataTask['records'][6]['fields']['Tasked Finished']

    # value for transport task to pick up processed 
    Fpickup1 = dataTask['records'][7]['fields']['Tasked Finished']

    # value for transport to bring to blending
    Fpickup2 = dataTask['records'][8]['fields']['Tasked Finished']

    
    return Fcup, Fice, Fsmall, Fprocessed, Fblender1, Fblender2, Fpickup1, Fpickup2
  
def main(args=None):
    startProcess = True
    #initialize process by setting all fields to ready for robot/ not sure if needed
    dataTask['records'][1]['fields']['Ready for Robot'] = 1
    dataTask['records'][2]['fields']['Ready for Robot'] = 1
    dataTask['records'][3]['fields']['Ready for Robot'] = 1
    dataTask['records'][4]['fields']['Ready for Robot'] = 1
    dataTask['records'][5]['fields']['Ready for Robot'] = 1
    dataTask['records'][6]['fields']['Ready for Robot'] = 1
    dataTask['records'][7]['fields']['Ready for Robot'] = 1
    dataTask['records'][8]['fields']['Ready for Robot'] = 1
    
    while startProcess:
        #retrieve updated values of each field from other robots
        Rcup, Rice, Rsmall, Rprocessed, Rblender1, Rblender2, Rpickup1, Rpickup2 = getReady()
        
        Dcup, Dice, Dsmall, Dprocessed, Dblender1, Dblender2, Dpickup1, Dpickup2 = getDocked()
        
        Fcup, Fice, Fsmall, Fprocessed, Fblender1, Fblender2, Fpickup1, Fpickup2 = getFinish()
        
        #conditions for getting cup:
        if Rcup == 1:
            Fcup = Dcup = 0 #not sure if i should use this variable or use whole json definition
        if Dcup == 1:
            Rcup = Fcup = 0
        if Fcup == 1:
            Dcup = Rcup = 0
        
        #conditions for getting ice:
        if Rice == 1:
            Fice = Dice = 0 
        if Dcup == 1:
            Rice = Fice = 0
        if Fcup == 1:
            Dice = Rice = 0
            
        #conditions for getting small foods and liquids:
        if Rsmall == 1:
            Fsmall = Dsmall = 0 
        if Dcup == 1:
            Rsmall = Fsmall = 0
        if Fcup == 1:
            Dsmall = Rsmall = 0
            
        #conditions for getting processed foods:
        if Rprocessed == 1:
            Fprocessed = Dprocessed = 0 
        if Dprocessed == 1:
            Rprocessed = Fprocessed = 0
        if Fprocessed == 1:
            Dprocessed = Rprocessed = 0
            
        #conditions for getting blended in blender 1:
        if Rblender1 == 1:
            Fblender1 = Dblender1 = 0 
        if Dblender1 == 1:
            Rblender1 = Fblender1 = 0
        if Fblender1 == 1:
            Dblender1 = Rblender1 = 0
            
            
        #conditions for getting blended in blender 2:
        if Rblender2 == 1:
            Fblender2 = Dblender2 = 0 
        if Dblender2 == 1:
            Rblender2 = Fblender2 = 0
        if Fblender2 == 1:
            Dblender1 = Rblender1 = 0
            
        #conditions for getting picked up at 1:
        if Rpickup1 == 1:
            Fpickup1 = Dpickup1 = 0 
        if Dpickup1 == 1:
            Rpickup1 = Fpickup1 = 0
        if Fpickup1 == 1:
            Dpickup1 = Rpickup1 = 0
            
        #conditions for getting picked up at 2:
        if Rpickup2 == 1:
            Fpickup2 = Dpickup2 = 0 
        if Dpickup2 == 1:
            Rpickup2 = Fpickup2 = 0
        if Fpickup2 == 1:
            Dpickup2 = Rpickup2 = 0
            
            
      
    
        
