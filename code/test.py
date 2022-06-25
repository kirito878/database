from tkinter import *
import backend
import os
import datetime
import time
import random
import pymysql
import tree
import avtrain

db_settings = backend.dbset()
# Defining Some Initial Variables
current_date = datetime.date.today()
# A Ticket can be Booked 1 Months before the Actual Trip
max_date = current_date + datetime.timedelta(days=30)


def ShowBookings(mobile_no):
    """
    ShowBookings() -> Shows the Bookings Made by an User
    Parameters -> None
    """
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM booking where Mobile_No="{}" order by Date_Of_Booking'.format(mobile_no))
    result = cursor.fetchall()
    column = (
        "Booking_ID", "Train_No", "姓名", "電話", "搭高鐵日期", "起始車站",
        "目的車站",
        "搭車時間")
    t=len(result)
    if t ==0:
        res ='error'
        return res,result, column
    else:
        return 'res', result, column
    cursor.close()
    conn.close()


def AvailableTrains(OriginStationcode, DestinationStationcode, deptime, arrtime,date):
    """
    AvailableTrains() -> Shows the List of Available Trains according to the User Requirement
    Parameters -> None
    """
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()
    cursor.execute(
        f'SELECT OriginStationID , OriginStationName,DestinationStationID,DestinationStationName,Fares,ori.TrainNo,'
        f'ori.ArrivalTime ,ori.DepartureTime,des.ArrivalTime,des.DepartureTime ,seat.TrainDate FROM  train.fares,'
        f'(select * from '
        f'train.timetable  ) as ori , (select * from train.timetable  ) as des ,train.seat where ori.StationName = '
        f'OriginStationName and des.StationName = DestinationStationName and ori.TrainNo = des.TrainNo and '
        f'ori.ArrivalTime<des.ArrivalTime and  OriginStationID ={OriginStationcode} and seat.TrainDate = {date} and '
        f'DestinationStationID = '
        f'{DestinationStationcode} and ori.DepartureTime > {deptime} and des.ArrivalTime< {arrtime}  and '
        f'seat.StandardSeatStatus="O" and seat.TrainNo=ori.TrainNo and seat.StationName = ori.StationName  and '
        f'seat.NextStationName = DestinationStationName order by '
        f'ori.ArrivalTime ')
    result = cursor.fetchall()
    column = ("起始站ID",
              "起始站", "終點站ID", "終點站",
              "票價", "車次", "起始站抵達時間", "起始站出發時間", "目的站抵達時間", "目的站離開時間","高鐵時間")
    res_len= len(result)
    if res_len ==0:
        return 'error',column, result
    else:
        return 'py',column, result
    cursor.close()
    conn.close()


def BookTrain(train_no, Name, Mobile,origin,des,dep,day):
    """
    BookTrain() -> Let's a User Book a Train
    Parameters -> None
    """
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()
    result = check(train_no)
    if result == 0:
        return 'error'
    else:
        Time_of_Booking = datetime.datetime.now()
        date = Time_of_Booking.date()
        date = date.strftime("%y-%m-%d")
        # Creating Unique ID for each Booking
        id = random.randint(1, 10000)
        cursor.execute("SELECT Booking_ID FROM booking")
        result = cursor.fetchall()
        Used_ID = []
        for x in result:
            for y in x:
                Used_ID.append(y)
        while True:
            if id in Used_ID:
                id = random.randint(1, 10000)
            else:
                break
        command = "INSERT INTO booking values({}, '{}', '{}', '{}', '{}' ,'{}','{}','{}')".format(
            id, train_no, Name, Mobile, day,origin,des,dep)
        cursor.execute(command)
        conn.commit()
        cursor.close()
        conn.close()
        return 'success'


def check(num):
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()
    command = f'SELECT * FROM train.timetable where TrainNo ={num};'
    cursor.execute(command)
    result = cursor.fetchall()
    return len(result)
