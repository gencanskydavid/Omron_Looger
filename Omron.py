import pandas as pd
#import matplotlib.pyplot as plt
import datetime
import time
#Function definitions
def SumOfSeries(dataseries, UpperIndex=100, LowerIndex=1):
    """
    :param dataseries: Input dataseries that will be counted
    :param UpperIndex:
    :param LowerIndex:
    :return:
    """
    dataseries = pd.to_timedelta(dataseries)
    Total = datetime.timedelta(0)
    #InSec = dataseries.total_seconds()
    for rows in dataseries:  # [LowerIndex:UpperIndex]:
        Total = Total + rows
    else:
        return Total
def CheckLenght(value,Len=10):
    if isinstance(value,str):
        if len(value) < Len:
            raise AttributeError("Given string is shorter!")
        if len(value) > Len:
            raise AttributeError("Given string is longer!")
        if len(value) == Len:
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
#
def CheckDate(date,format='%Y-%m-%d'):
    '''
    Function for check user date input validity.
    return None
    :param date: date string.
            format: desired time format.
    '''
    try:
        datetime.datetime.strptime(date,format)
    except ValueError as e:
        print(e)
#
def CheckTime(time,format='%H:%M:%S'):
    '''
    Function for check user time format validity.
    return None
    :param time: time string.
            format: desired time format.
    '''
    try:
        datetime.datetime.strptime(time,format)
    except ValueError as e:
        print(e)
#
def Shifts(dataframe,shift='Morning',morning='06:00',afternoon='14:00',night='22:00',time_period=8):
    '''
    Function takes pandas DataFrame with DatetimeIndex and
    return DataFrame that has only Selected Shifts for each day.
    :param dataframe - pandas dataframe with DatetimeIndex
            type - shift, such as Morning,Afternoon or Night
            morning - start of Morning Shifts and end of Night shift
            afternoon - start of Afternoon shifts and end of Morning shift
            night - start of Night shifts and end of Afternoon shift
            time_period - T.B.D
    :return Data - dataframe with certain periods of day.
    '''
    try:
        if isinstance(dataframe,pd.DataFrame) and isinstance(dataframe.index,pd.DatetimeIndex):
            if shift == 'Morning':
                Data = dataframe.between_time(morning,afternoon)
                return Data
            if shift == 'Afternoon':
                Data = dataframe.between_time(afternoon,night)
                return Data
            if shift == 'Night':
                Data = dataframe.between_tim(night,morning)
                return Data
        else:
            ValueError("Input value is not DataFrame or DataFrame with wrong index")
    except (ValueError,AttributeError) as e:
        return e
