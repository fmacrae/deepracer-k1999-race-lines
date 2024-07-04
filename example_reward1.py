import numpy as np


def get_racing_line_waypoints():
    #waypoints will be inserted by the race line calc notebook
    return #####WAYPOINTS#####


def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def get_waypoints_ordered_in_driving_direction(params, waypoints):
    # waypoints are always provided in counter clock wise order
    if params['is_reversed']: # driving clock wise.
        return list(reversed(waypoints))
    else: # driving counter clock wise.
        return waypoints
    


def reward_function(params):
    '''
    Example of being near the nearest racing line 
    '''

    
    waypoints_input = np.array(get_racing_line_waypoints())
    racing_line = waypoints_input[:,6:8]
    waypoints = params["waypoints"]
    ordered_racing_line = get_waypoints_ordered_in_driving_direction(params, racing_line)
    ordered_waypoints = get_waypoints_ordered_in_driving_direction(params, waypoints)
    car = [params['x'], params['y']]
    distances = [dist(p, car) for p in ordered_waypoints]
    min_dist = min(distances)
    i_closest = distances.index(min_dist)
    #find the distance to the racing line point for the closest waypoint you are at
    dist_from_racingline = dist(car, ordered_racing_line[i_closest])
    #check for divide by 0 and then limit the reward to between 1 and 0.001 normally
    if dist_from_racingline == 0:
        #if it is exactly on the racing line give it an extra point
        reward = 2
    else:
        reward = 1/dist_from_racingline
        if reward > 10: reward =10
        if reward < 0.01: reward = 0.01
        reward = reward /10

    #add extra speed boost if in good track position
    
    if reward > 0.5:
        if params['speed']>3.0:
            reward = reward + 1
        if params['speed']>3.3:
            reward=reward+1
        if params['speed']>3.5:
            reward=reward+1
        if params['speed']>3.7:
            reward=reward+1
    return reward
    
