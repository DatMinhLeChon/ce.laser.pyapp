import pandas as pd
import pyodbc

# define const string connect

DRIVER = 'SQL Server'
HOST = 'localhost'
PORT = '1433'
DB_PUSH = 'TutorialDB'; TABLE_ACTUAL ='LASER_P3'
DB_GET = 'CE_Control_Plan'; TABLE_CONTROL_PLAN ='LASER_P3_CONTROL_PLAN'
USER = 'sa'
PASSWORD = 'Password1'

## function push control plan from database admin
def push_db_controlplan(worksheet, size):
    cnxn = pyodbc.connect("Driver={" + DRIVER +"}"\
                        +";Server=" + HOST +", port=" + PORT\
                        +";Database="+ DB_GET\
                        +";Trusted_Connection=yes"\
                        +";user=" +USER\
                        +";password=" + PASSWORD)

    cursor = cnxn.excute("SELECT * FROM" + TABLE_CONTROL_PLAN)
    for i in range(7, size):
        cnxn.execute('INSERT INTO' + TABLE_CONTROL_PLAN + 'VALUES ("{worksheet.cell[i,3]}", "{worksheet.cell[i,4]}", "{worksheet.cell[i,5]}", "{worksheet.cell[i,6]}")')


## Get data from control plan to trackback
def control_plan_server_get(worksheet, size):
    cnxn = pyodbc.connect("Driver={" + DRIVER +"}"\
                        +";Server=" + HOST +", port=" + PORT\
                        +";Database="+ DB_GET\
                        +";Trusted_Connection=yes"\
                        +";user=" +USER\
                        +";password=" + PASSWORD)
    df = pd.read_sql("SELECT * FROM" + TABLE_CONTROL_PLAN, cnxn) 
    for i in range (7, size):
        for j in range (3, 6):
            if str(df.iloc[i, j]) != None:
                worksheet.cell[i, j].value = str(df.iloc[i, j])
            else:
                worksheet.cell[i, j] == None
    cnxn.close()

## Push actual value to DB after get data from XML SChema to worksheet
def push_db_actual(worksheet, size):
    cnxn = pyodbc.connect("Driver={" + DRIVER +"}"\
                        +";Server=" + HOST +", port=" + PORT\
                        +";Database="+ DB_PUSH\
                        +";Trusted_Connection=yes"\
                        +";user=" +USER\
                        +";password=" + PASSWORD)
    for i in range (7, size):
        cnxn.execute('INSERT INTO' + TABLE_ACTUAL + 'VALUES ("worksheet.cell[i,7])')
    
