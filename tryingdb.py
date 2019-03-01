import mysql.connector
import cv2
import numpy as np
import os
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pro_sss"
)
mycursor = mydb.cursor()
sql = "DROP DATABASE testdb"
mycursor.execute(sql)
mydb.close()