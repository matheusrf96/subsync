#coding: utf-8

def timeUnitTransfer(time):
    result = []
    count = 0

    if time >= 60:
        while time >= 60:
            time -= 60
            count += 1

        result.append(time)
        result.append(count)
    elif time < 0:
        while time < 0:
            time += 60
            count -= 1

        result.append(time)
        result.append(count)
    else:    
        result.append(time)
        result.append(count)

    return result

def converter(num):
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)

    return num

def milliConverter(num):
    if num < 10:
        num = "00" + str(num)
    elif num < 100 and num >= 10:
        num = "0" + str(num)
    else:
        num = str(num)

    return num

def sixtyUpdate(line, time, values):
    milli = values[0]
    time = int(time)

    hr = line[0:2]
    minutes = line[3:5]
    sec = line[6:8]

    hr = int(hr)
    minutes = int(minutes)
    sec = int(sec)

    time += values[1]

    sec += time

    tut = timeUnitTransfer(sec)
    sec = tut[0]
    minutes += tut[1]

    tut = timeUnitTransfer(minutes)
    minutes = tut[0]
    hr += tut[1]

    if hr > 99:
        hr = 99

    hr = converter(hr)
    minutes = converter(minutes)
    sec = converter(sec)
    milli = milliConverter(milli)

    newLine = str(hr + ":" + minutes + ":" + sec + "," + milli)

    return newLine


def millisecondUpdate(mill, time):
    values = []

    count = 0

    mill = int(mill)
    time = int(time)

    mill = mill + time

    if mill > 999:
        while mill > 999:
            mill -= 999
            count += 1
    elif mill < 0:
        while mill < 0:
            mill += 1000
            count -= 1

    values.append(mill)
    values.append(count)

    return values

def updateLine(line1, line2, time):
    newLine = ""

    time1 = line1[0:8]
    mill1 = line1[9:12]
    
    time2 = line2[0:8]
    mill2 = line2[9:12]

    mill1 = int(mill1)
    mill2 = int(mill2)

    if time.find('.') != -1:
        t = time.split('.', 2)
        second = t[0]
        millisecond = t[1]
    else:
        second = time
        millisecond = "000"

    if len(millisecond) == 1:
        millisecond = millisecond + "00"
    elif len(millisecond) == 2:
        millisecond = millisecond + "0"

    if time[0] == '-':
        millisecond = "-" + millisecond

    msu = millisecondUpdate(mill1, millisecond)
    newLine += sixtyUpdate(time1, second, msu)

    newLine += " --> "

    msu = millisecondUpdate(mill2, millisecond)
    newLine += sixtyUpdate(time2, second, msu)

    return newLine

def temporalLogic(line, time):
    string = ""

    if str(line.strip()) != '':
        if line.find("-->") != -1:
            line = str(line)
            time = str(time)

            time1 = line[0:12]
            time2 = line[17:29]

            string = updateLine(time1, time2, time)
        else:
            string = line.strip()

    return string

def getNewFile(filepath, time):
    newFile = ""

    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 1
    
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))

            newFile += temporalLogic(line.strip(), time) + "\n"

            line = fp.readline()        
            cnt += 1
    
    return newFile

def writeNewFile(content):
    file = open("UPDATED-"+filepath, "w")
    file.write(content)
    file.close()

    return True

filepath = raw_input("Insert the name of the a file to be updated: ")
time = input("Insert how many seconds you want to delay(negative number[use '-' before the number]) or haste(positive number[without '+']) the subtitles: ")

if writeNewFile(getNewFile(filepath, time)):
    print("A new file was created!")
else:
    print("Error!")
