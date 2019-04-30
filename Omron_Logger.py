##########################################################
######Omron mobile robot - Status Logger 0.3##############
######Created by ALPS Electric Czech, David Gencansky#####
##########################################################
import telnetlib
import time
import datetime
import re
import csv
#######Variables declaration
HOST = "10.54.22.56"
PORT = "7171"
PASSWORD = "alpsalps"
CMD = "status"
CMD2 = "QueueUpdate"
data = None
LastTime = datetime.datetime.utcnow()
########Connection to robot#
tn = telnetlib.Telnet()
while True:
    try:
        tn.open(HOST,PORT)
        tn.read_until(b"Enter password:" +b"\r\n")
        tn.write(PASSWORD.encode('ascii') + b'\n')
        received = tn.read_until(b"End of commands" + b"\r\n")
        ########Main code
        try:
            while True:
                time.sleep(1)
                tn.write(CMD.encode('ascii') + b'\n')                                     #Send command to Robot
                tn.read_until(b"Extended")                                                #Flush unnecessary data
                received = tn.read_until(b"\n")                                            #Read important data
                data_show = received
                received = received.decode('ascii').strip()                                #Format data
                received = re.match("StatusForHumans: (.*)",received)
                if data != received.group(1):
                    timestamp = datetime.datetime.now()                                      #Saved TimeStamp for log and calculations
                    CurrentStatus = received.group(1)
                    duration = timestamp - LastTime
                    timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")                       #Adjusting format for better parsing in Excel
                    with open('Result.csv', 'a',newline='') as csvfile:                   # Create new file for write all result
                        writer = csv.writer(csvfile)
                        writer.writerow([timestamp, CurrentStatus, duration])                #Write new line of data in format: DataTime, Status, Duration of status
                    print (str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "," + data_show.decode('ascii').strip()+","+ str(duration))    #For debug
                    data = received.group(1)                                                 #Save last result for next iteration
                    LastTime = datetime.datetime.now()                                       #Save last TimeStamp for next calculation
        except AttributeError as e:
            print(e)
            time.sleep(5)
    except (ConnectionResetError, OSError) as e:
        print (e)
        time.sleep(10)