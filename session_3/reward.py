def reward_function(params):
    '''
    Follow centre line and avoid excessive steering
    '''

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    current_steps = params['steps']
    progress = params['progress']
    speed = params['speed']

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    step_threshhold = 100
    speed_max_threshhold = 1.0
    speed_min_threshhold = 0.5

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    if progress > (current_steps / step_threshhold) * 100:
        reward += 1.0

    if speed > speed_min_threshhold and speed < speed_max_threshhold:
        reward += 1.0

    return float(reward)