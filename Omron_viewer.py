##########################################################
######Omron mobile robot - Status Logger viewer 0.01##############
######Created by ALPS Electric Czech, David Gencansky#####
##########################################################
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
#Variable declarations
path = "Result_20190625.csv"   #Adress of File created by Omron Logger
StartDate = "2019-05-01"  #Start date in format YYYY-MM-DD
StartTime = "06:00:00"  #Start time in format HH:MM:SS
EndDate = "2019-05-02"  #Start date in format YYYY-MM-DD
EndTime = "22:00:00"  #Start time in format HH:MM:SS
############################################
#Function definitions
def SumOfSeries(dataseries, UpperIndex=100, LowerIndex=1):
    """
    :param dataframe:
    :param UpperIndex:
    :param LowerIndex:
    :return:
    """
    dataseries = pd.to_timedelta(dataseries)
    Total = datetime.timedelta(0)
    for rows in dataseries:  # [LowerIndex:UpperIndex]:
        Total = Total + rows
    else:
        return Total
def CheckLenght(value,Len=10):
    if isinstance(value,str):
        if len(value) < Len:
            raise AttributeError("Given string is shorter!")
        else:
            raise AttributeError("Given string is longer!")
    elif len(value) == Len:
        return True
    else:
        raise ValueError ("Given variable is not type string!")
def IsEmpty(value,error = True):
    '''
    Test function for checking user inputs.
    Return False if given value is not empy.
    :param value: variable for test
            error: AttributeError on/off, default = True
    :return: True if given value is empty string
    '''
    if isinstance(value,str):
        if value == "":
            if error == False:
                return True
            else:
                raise AttributeError("Empty string was given!")
        else:
            return False
    elif isinstance(value,int):
        if value == 0:
            if error == False:
                return True
            else:
                raise AttributeError("Empty integer was given!")
        else:
            return False
    else:
        AttributeError("Wrong format of input Data!")
def UserCheck(variable,lenght,type,format):
    IsEmpty(variable)
    CheckLenght(variable)
    var1 = variable.strip("-")
#
while True:
    try:
        StartDate = input("Write start date in format YYYY-MM-DD  ")
        IsEmpty(StartDate)
        CheckLenght(StartDate,Len=10)
        StartTime = input("Write start time in format HH:MM:SS  ")
        IsEmpty(StartTime)
        CheckLenght(StartDate, Len=8)
        EndDate = input("Write end date in format YYYY-MM-DD  ")
        IsEmpty(EndDate)
        EndTime = input("Write end time in format HH:MM:SS  ")
        IsEmpty(EndTime)
    except (ValueError,AttributeError) as e:
        print (e)
        continue
    try:
        Start = datetime.datetime.strptime(StartDate+" "+StartTime,'%Y-%m-%d %H:%M:%S')
        End = datetime.datetime.strptime(EndDate+" "+EndTime,'%Y-%m-%d %H:%M:%S')
        Omron = pd.read_csv(path,sep=",",names=["Date","Status","Duration"])           #Load file into memory
    except ValueError as e:
        print (e)
        time.sleep(5)
        continue
    try:
        Omron.Date = pd.to_datetime(Omron.Date,format="%d-%m-%Y-%H-%M")     #Change date format
        Omron.Duration = Omron.Duration.shift(periods=-1)                   #Shift duration collumn in DataFrame
        Omron = Omron.set_index(Omron.Date)                                 #Set new datetime index, for future time slicing
        Omron = Omron.drop(["Date"],axis=1)                                #Delete unnecessary data
    except (ValueError,AttributeError) as e:
        print(e)
        time.sleep(5)
    #
    Status = Omron.Status.unique()                                          #Get all unique values
    Omron = Omron[Start:End]
    Muda = ["Waiting","Checking custom inputs"]
    Move = ["Going to "]
    Error = ["Failed "]
    Park = ["Parking","Parked"]
    Dock = ["Docked","Docking"]
    df_Move = Omron[Omron["Status"].str.contains("Going to")]
    df_Muda = Omron[Omron["Status"].str.contains("|".join(Muda))]
    df_Error = Omron[Omron["Status"].str.contains("Failed")]
    df_Park = Omron[Omron["Status"].str.contains("|".join(Park))]
    df_Dock = Omron[Omron["Status"].str.contains("|".join(Dock))]
#
    print ("Marshaling is", SumOfSeries(df_Muda.Duration))
    print ("Move is",SumOfSeries(df_Move.Duration))
    print ("Error is",SumOfSeries(df_Muda.Duration))
    print ("Parking and docking is",SumOfSeries(df_Park.Duration))
    print ("Docking is",SumOfSeries(df_Dock.Duration))
    print ("Total working time",SumOfSeries(Omron.Duration))
#
