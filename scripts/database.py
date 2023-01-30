import pandas as pd
import mysql.connector
from datetime import datetime
import os
def upload_to_db(all_results):
    mydb = mysql.connector.connect(
            host="64.227.176.243",
            user="phpmyadmin",
            password="Possibilities123.@",
            database="Domains_Input"
        )
    with open(all_results,'r') as qq:
        out_qq = qq.read()
    mycursor = mydb.cursor()
    ssl = "INSERT into domain_input (Date, Domain_type, Domain_list) VALUE (now(),%s,%s)"
    val = ("News_Domains",out_qq)
    mycursor.execute(ssl,val)
    mydb.commit()
    return print("print all") ######### send email ##########

    
all_results = r"F:\file_working\compair_file\Domain_file(07).csv"
upload_to_db(all_results)