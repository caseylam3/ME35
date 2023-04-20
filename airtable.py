import time
import requests
import json 

URL = 'https://api.airtable.com/v0/appxFSx1vodDWljqe/TaskOrder?api_key=keyKf7fEzdNw4S7qi'


response = requests.get(url = URL, params = {})
datatask = response.json()

def getReady():
    # retrieves boolean for if station is ready or not
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
    # retrieves boolean for if robot is docked or not
    Dcup = dataTask['records'][1]['fields']['Robot Docked']
 
    Dice = dataTask['records'][2]['fields']['Robot Docked']

    Dsmall = dataTask['records'][3]['fields']['Robot Docked']

    Dprocessed = dataTask['records'][4]['fields']['Robot Docked']

    Dblender1 = dataTask['records'][5]['fields']['Robot Docked']

    Dblender2 = dataTask['records'][6]['fields']['Robot Docked']

    Dpickup1 = dataTask['records'][7]['fields']['Robot Docked']

    Dpickup2 = dataTask['records'][8]['fields']['Robot Docked']
    
    return Dcup, Dice, Dsmall, Dprocessed, Dblender1, Dblender2, Dpickup1, Dpickup2

def getFinish():
    # retrieves boolean for if robot is finished with task
    Fcup = dataTask['records'][1]['fields']['Tasked Finished']
 
    Fice = dataTask['records'][2]['fields']['Tasked Finished']

    Fsmall = dataTask['records'][3]['fields']['Tasked Finished']

    Fprocessed = dataTask['records'][4]['fields']['Tasked Finished']

    Fblender1 = dataTask['records'][5]['fields']['Tasked Finished']

    Fblender2 = dataTask['records'][6]['fields']['Tasked Finished']

    Fpickup1 = dataTask['records'][7]['fields']['Tasked Finished']

    Fpickup2 = dataTask['records'][8]['fields']['Tasked Finished']
    
    return Fcup, Fice, Fsmall, Fprocessed, Fblender1, Fblender2, Fpickup1, Fpickup2

def getCoordinates(): #retrieves coordiates for every task
    Cupx = datatask['records'][1]['fields']['X Coordinate']
    Cupy = datatask['records'][1]['fields']['Y Coordinate']  
    Cupz = datatask['records'][1]['fields']['Z Coordinate'] 
    Cupw = datatask['records'][1]['fields']['W Coordinate'] 
    
    Icex = datatask['records'][2]['fields']['X Coordinate']
    Icey = datatask['records'][2]['fields']['Y Coordinate']  
    Icez = datatask['records'][2]['fields']['Z Coordinate'] 
    Icew = datatask['records'][2]['fields']['W Coordinate']
    
    Smallx = datatask['records'][3]['fields']['X Coordinate']
    Smally = datatask['records'][3]['fields']['Y Coordinate']  
    Smallz = datatask['records'][3]['fields']['Z Coordinate'] 
    Smallw = datatask['records'][3]['fields']['W Coordinate']
    
    Prox = datatask['records'][4]['fields']['X Coordinate']
    Proy = datatask['records'][4]['fields']['Y Coordinate']  
    Proz = datatask['records'][4]['fields']['Z Coordinate'] 
    Prow = datatask['records'][4]['fields']['W Coordinate']
    
    B1x = datatask['records'][5]['fields']['X Coordinate']
    B1y = datatask['records'][5]['fields']['Y Coordinate']  
    B1z = datatask['records'][5]['fields']['Z Coordinate'] 
    B1w = datatask['records'][5]['fields']['W Coordinate']
    
    B2x = datatask['records'][6]['fields']['X Coordinate']
    B2y = datatask['records'][6]['fields']['Y Coordinate']  
    B2z = datatask['records'][6]['fields']['Z Coordinate'] 
    B2w = datatask['records'][6]['fields']['W Coordinate']
    
    P1x = datatask['records'][7]['fields']['X Coordinate']
    P1y = datatask['records'][7]['fields']['Y Coordinate']  
    P1z = datatask['records'][7]['fields']['Z Coordinate'] 
    P1w = datatask['records'][7]['fields']['W Coordinate']
    
    P2x = datatask['records'][7]['fields']['X Coordinate']
    P2y = datatask['records'][7]['fields']['Y Coordinate']  
    P2z = datatask['records'][7]['fields']['Z Coordinate'] 
    P2w = datatask['records'][7]['fields']['W Coordinate']
  
    return Cupx, Cupy, Cupz, Cupw, Icex, Icey, Icez, Icew, Smallx, Smally, Smallz, Smallw, Prox, Proy, Proz, Prow, B1x, B1y, B1z, B1w, B2x, B2y, B2z, B2w, P1x, P1y, P1z, P1w, P2x, P2y, P2z, P2w


def main(args=None):
    startProcess = True
    
    rclpy.init(args=args)
    action_client = MovementActionClient()

    #initialize process by setting all fields to ready for robot
    dataTask['records'][1]['fields']['Ready for Robot'] = 1
    dataTask['records'][2]['fields']['Ready for Robot'] = 1
    dataTask['records'][3]['fields']['Ready for Robot'] = 1
    dataTask['records'][4]['fields']['Ready for Robot'] = 1
    dataTask['records'][5]['fields']['Ready for Robot'] = 1
    dataTask['records'][6]['fields']['Ready for Robot'] = 1
    dataTask['records'][7]['fields']['Ready for Robot'] = 1
    dataTask['records'][8]['fields']['Ready for Robot'] = 1
    
    while startProcess:
        #retrieve updated values of each field 
        Rcup, Rice, Rsmall, Rprocessed, Rblender1, Rblender2, Rpickup1, Rpickup2 = getReady()
        
        Dcup, Dice, Dsmall, Dprocessed, Dblender1, Dblender2, Dpickup1, Dpickup2 = getDocked()
        
        Fcup, Fice, Fsmall, Fprocessed, Fblender1, Fblender2, Fpickup1, Fpickup2 = getFinish()
        
        Cupx, Cupy, Cupz, Cupw, Icex, Icey, Icez, Icew, Smallx, Smally, Smallz, Smallw, Prox, Proy, Proz, Prow, B1x, B1y, B1z, B1w, B2x, B2y, B2z, B2w, P1x, P1y, P1z, P1w, P2x, P2y, P2z, P2w = getCoordinates()
        
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
            action_client.send_navigate(Icex, Icey, Icez, Icew) #when ice station is ready, robot will move to that station
        if Dcup == 1:
            Rice = Fice = 0
            self.send_dock() # once robot gets to coordinate, robot will dock
        if Fcup == 1:
            Dice = Rice = 0
            self.send_undock() #once task is finished, robot will undock
            
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
            
        try:
            rclpy.spin(action_client)
        
        except KeyboardInterrupt:
            rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    
        
