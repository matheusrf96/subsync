from content.timeConverter import *

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

def writeNewFile(content, filepath):
    file = open("UPDATED-"+filepath, "w")
    file.write(content)
    file.close()

    return True