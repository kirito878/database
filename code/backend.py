import train_data
from wsgiref.handlers import format_date_time
import os
from time import mktime
import os
import datetime
import pymysql
def dbset():
    db_set = {
        "host": "database-2.c9rs0mr29ooi.us-east-1.rds.amazonaws.com",
        "port": 3306,
        "user": "admin",
        "password": "a20268a20268",
        "db": "train",
        "charset": "utf8"
    }
    return db_set


db_settings = dbset()


def clear_table(table):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"TRUNCATE  TABLE  {table}"
        cursor.execute(command)
        conn.commit()


def create_station_table():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "CREATE TABLE `train`.`station` (\
        `LocationCity` VARCHAR(80) NOT NULL,\
      `LocationCityCode` VARCHAR(80) NOT NULL,\
      `LocationTown` VARCHAR(80) NOT NULL,\
     `LocationTownCode` VARCHAR(80) NOT NULL,\
      `StationCode` VARCHAR(80) NOT NULL,\
      `StationID` VARCHAR(80) NOT NULL,\
          `StationName` VARCHAR(80) NOT NULL,\
      PRIMARY KEY (`StationID`))\
    ENGINE = InnoDB\
    DEFAULT CHARACTER SET = utf8\
    COLLATE = utf8_bin;"
        cursor.execute(command)
        conn.commit()


def insert_station_datas():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"INSERT INTO station (LocationCity, LocationCityCode, LocationTown,LocationTownCode,StationCode," \
                  f"StationID,StationName)VALUES(%s, %s, %s,%s,%s,%s,%s) "
        data = train_data.station_data()
        for row in data:
            cursor.execute(
                command, (row["LocationCity"], row["LocationCityCode"], row["LocationTown"], row["LocationTownCode"],
                          row["StationCode"], row["StationID"], row["StationName"]["Zh_tw"]))
        conn.commit()

def create_fares_table():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "CREATE TABLE `train`.`fares` ( `OriginStationID` VARCHAR(45) NOT NULL,\
 `OriginStationName` VARCHAR(45) NOT NULL,\
  `DestinationStationID` VARCHAR(30) NOT NULL,\
  `DestinationStationName` VARCHAR(30) NOT NULL,\
  `Fares` VARCHAR(30) NOT NULL,\
  PRIMARY KEY (`OriginStationID`, `DestinationStationID`))\
ENGINE = InnoDB\
DEFAULT CHARACTER SET = utf8\
COLLATE = utf8_bin;"
        cursor.execute(command)
        conn.commit()


def insert_fares_datas():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"INSERT INTO fares (OriginStationID, OriginStationName, DestinationStationID," \
                  f"DestinationStationName,Fares)VALUES(%s, %s, %s,%s,%s) "
        data = train_data.fares()
        for row in data:
            for i in row['Fares']:
                if i['CabinClass'] == 1 and i['FareClass'] == 1 and i['TicketType'] == 1:
                    cursor.execute(command, (
                        row["OriginStationID"], row["OriginStationName"]['Zh_tw'], row["DestinationStationID"],
                        row["DestinationStationName"]['Zh_tw'], str(i['Price'])))
        conn.commit()

def create_timetable_table():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "CREATE TABLE `train`.`timetable` (\
  `Direction` VARCHAR(10) NOT NULL,\
  `TrainNo` VARCHAR(45) NOT NULL,\
  `StationName` VARCHAR(45) NOT NULL,\
  `ArrivalTime` VARCHAR(45) NOT NULL,\
  `DepartureTime` VARCHAR(45) NOT NULL,\
  PRIMARY KEY (`Direction`, `TrainNo`, `StationName`))\
ENGINE = InnoDB\
DEFAULT CHARACTER SET = utf8\
COLLATE = utf8_bin;"
        cursor.execute(command)
        conn.commit()


def insert_timetable_datas():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"INSERT INTO timetable (Direction, TrainNo,StationName, ArrivalTime,DepartureTime)VALUES(%s, %s, " \
                  f"%s,%s,%s) "
        data = train_data.timetable()
        for rows in data:
            for row in rows['GeneralTimetable']['StopTimes']:


                try:

                    cursor.execute(command, (rows['GeneralTimetable']['GeneralTrainInfo']["Direction"],
                                             rows['GeneralTimetable']['GeneralTrainInfo']["TrainNo"],
                                             row['StationName']['Zh_tw'], row['ArrivalTime'], row['DepartureTime']))
                except :
                    try:

                        cursor.execute(command, (rows['GeneralTimetable']['GeneralTrainInfo']["Direction"],
                                                 rows['GeneralTimetable']['GeneralTrainInfo']["TrainNo"],
                                                 row['StationName']['Zh_tw'], row['ArrivalTime'], row['ArrivalTime']))
                    except :
                        cursor.execute(command, (rows['GeneralTimetable']['GeneralTrainInfo']["Direction"],
                                                 rows['GeneralTimetable']['GeneralTrainInfo']["TrainNo"],
                                                 row['StationName']['Zh_tw'], row['DepartureTime'],
                                                 row['DepartureTime']))
        conn.commit()

def booking_table():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "CREATE TABLE `train`.`booking` (\
  `Booking_ID` VARCHAR(45) NOT NULL,\
  `TrainNo` VARCHAR(10) NOT NULL,\
  `Passenger_Name` VARCHAR(45) NOT NULL,\
  `Mobile_No` VARCHAR(10) NOT NULL,\
  `Date_Of_Booking` VARCHAR(45) NOT NULL,\
  PRIMARY KEY (`Booking_ID`),\
  INDEX `index` (`Date_Of_Booking` ASC) VISIBLE)\
ENGINE = InnoDB\
DEFAULT CHARACTER SET = utf8\
COLLATE = utf8_bin;"
        cursor.execute(command)
        conn.commit()


def delete_booking_table(ID):
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"DELETE FROM train.booking WHERE Booking_ID={ID}"
        cursor.execute(command)
        conn.commit()


def station_datas():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"select * FROM train.station "
        cursor.execute(command)
        column = ['LocationCity', 'LocationCityCode', 'LocationTown', 'LTCode', 'StationCode', 'StationID',
                  'StationName']
        result = cursor.fetchall()
    return column, result


def seat_table():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "CREATE TABLE `train`.`seat` (\
  `StationName` VARCHAR(45) NOT NULL,\
  `NextStationName` VARCHAR(45) NOT NULL,\
  `StandardSeatStatus` VARCHAR(45) NULL,\
  `TrainNo` VARCHAR(45) NOT NULL,\
  `TrainDate` VARCHAR(45) NOT NULL,\
  PRIMARY KEY (`TrainDate`, `TrainNo`, `StationName`, `NextStationName`))\
ENGINE = InnoDB\
DEFAULT CHARACTER SET = utf8\
COLLATE = utf8_bin;"
        cursor.execute(command)
        conn.commit()
def insert_seats_datas():
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = f"INSERT INTO seat (StationName, NextStationName, StandardSeatStatus," \
                  f"TrainNo,TrainDate)VALUES(%s, %s, %s,%s,%s) "
        current_date = datetime.date.today()
        max_date = current_date + datetime.timedelta(days=20)
        a = int(str(max_date - current_date)[:2])
        for i in range(a):
            date = current_date + datetime.timedelta(days=i)
            data=train_data.seat(date)
            for row in data['AvailableSeats']:

               for i in row['StopStations']:
                  #  print(i['StationName']['Zh_tw'])
                    cursor.execute(command, (
                        i['StationName']['Zh_tw'], i["NextStationName"]['Zh_tw'], i["StandardSeatStatus"],
                        row["TrainNo"], data['TrainDate']))
        conn.commit()
def sec():
    conn= pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command="select max(TrainDate) from train.seat"
        cursor.execute(command)
        result = cursor.fetchone()
    return (result[0])
def update_seats_datas():
    conn = pymysql.connect(**db_settings)
    str1 = sec()
    with conn.cursor() as cursor:
        command = f"INSERT INTO seat (StationName, NextStationName, StandardSeatStatus," \
                  f"TrainNo,TrainDate)VALUES(%s, %s, %s,%s,%s) "
        current_date = datetime.date.today()
        max_date = current_date + datetime.timedelta(days=20)
        a = int(str(max_date - current_date)[:2])
        str2 = str1.split('-')
        begin_day = datetime.date(int(str2[0]),int(str2[1]), int(str2[2]))
        c = int(str(begin_day - current_date)[:2])
        day=20-c
        try:
            for i in range(day):
                date = begin_day + datetime.timedelta(days=i)
                data=train_data.seat(date)
                for row in data['AvailableSeats']:

                   for i in row['StopStations']:

                        cursor.execute(command, (
                            i['StationName']['Zh_tw'], i["NextStationName"]['Zh_tw'], i["StandardSeatStatus"],
                            row["TrainNo"], data['TrainDate']))
            conn.commit()
            print("success_update")
        except:
            print("no_insert")
def delte_seat() :
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        current_date = datetime.date.today()
        current_date ="'"+ str(current_date)+"'"
        command = f"DELETE  from train.seat WHERE TrainDate <{current_date} "
        cursor.execute(command)
        conn.commit()
        print("success_update")
update_seats_datas()
delte_seat()




