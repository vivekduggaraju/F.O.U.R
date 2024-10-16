def checkdist():
    ''' Refer to the realization of basic functions-ultrasonic module '''

while 1:
    print('Automatic obstacle avoidance mode')
    if scanPos == 1:
        pwm.set_pwm(servoPort, 0, servoLeft)
        time.sleep(0.3)
        scanList[0] = checkdist()
    elif scanPos == 2:
        pwm.set_pwm(servoPort, 0, servoMiddle)
        time.sleep(0.3)
        scanList[1] = checkdist()
    elif scanPos == 3:
        pwm.set_pwm(servoPort, 0, servoRight)
        time.sleep(0.3)
        scanList[2] = checkdist()

    scanPos = scanPos + scanDir

    if scanPos > scanNum or scanPos < 1:
        if scanDir == 1:scanDir = -1
        elif scanDir == -1:scanDir = 1
        scanPos = scanPos + scanDir*2
    print(scanList)

    if min(scanList) < rangeKeep:
        if scanList.index(min(scanList)) == 0: #The shortest distance detected on the left
            '''
            Turn right
            '''
        print('Turn right')
        elif scanList.index(min(scanList)) == 1: #The shortest distance detected in the middle
            if scanList[0] < scanList[2]:
                '''
                If the detected distance on the left is shorter than the right, turn to the right
                '''
        print('Turn right')
    else:
        '''''
        Otherwise, turn left
        '''
        print('Turn left')
    elif scanList.index(min(scanList)) == 2: #The shortest distance detected on the right
        '''
        Turn Left
        '''
        print('Turn Left')
    if max(scanList) < rangeKeep:
        '''
        If the distances in the left, center, and right directions are all closer than rangeKeep, reverse
        '''
        print('reverse')
    else:
        '''
        All three directions are farther than rangeKeep
        '''
        print('Go forward')