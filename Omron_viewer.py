import pandas as pd
import matplotlib.pyplot as plt
import datetime
#
Omron = pd.read_csv("20190429_Result.csv",sep=",",names=["Date","Status","Duration"])     #Load file into memory
Omron.Date = pd.to_datetime(Omron.Date,format="%d-%m-%Y-%H-%M")     #Change date format
Omron.Duration = Omron.Duration.shift(periods=-1)                   #Shift duration collumn in DataFrame
Omron = Omron.set_index(Omron.Date)                                 #Set new datetime index, for future time slicing
Omron = Omron.drop(["Date"],axis=1)                                #Delete unnecessary data
#
Status = Omron.Status.unique()
Muda = ["Waiting","Checking custom inputs"]
Move = ["Going to "]
Error = ["Failed "]
Park = ["Parking","Docked"]
df_Move = Omron[Omron["Status"].str.contains("Going to")]
df_Muda = Omron[Omron["Status"].str.contains("|".join(Muda))]
df_Error = Omron[Omron["Status"].str.contains("Failed")]
df_Park = Omron[Omron["Status"].str.contains("|".join(Park))]
#print (Status)
#df_Muda.Duration = pd.to_timedelta(df_Muda.Duration)
#df_Muda = df_Muda.set_index(df_Muda.Date)
#df_Muda = df_Muda.drop(["Date"],axis=1)
Start = "2019-03-11 06:00:00"
End = "2019-03-11 14:00:00"
Marshaling = df_Muda[Start:End]
Move = df_Move[Start:End]
Muda = df_Error[Start:End]
Park = df_Park[Start:End]
Omron = Omron[Start:End]
#for index,rows in Omron[["Status","Duration"]].iterrows():

def SumOfSeries(dataseries,UpperIndex,LowerIndex):
    """
    :param dataframe:
    :param UpperIndex:
    :param LowerIndex:
    :return:
    """
    dataseries = pd.to_timedelta(dataseries)
    Total = datetime.timedelta(0)
    for rows in dataseries:  #[LowerIndex:UpperIndex]:
        Total = Total + rows
    else:
        return Total

print ("Marshaling is", SumOfSeries(Marshaling.Duration,1,100))
print ("Move is",SumOfSeries(Move.Duration,1,100))
print ("Error is",SumOfSeries(Muda.Duration,1,100))
print ("Parking and docking is",SumOfSeries(Park.Duration,1,100))
print ("Total working time",SumOfSeries(Omron.Duration,1,100))
#
