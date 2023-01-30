import os
import datetime
import pandas as pd
import mysql.connector
def marge_file():
    sub_file_folder = input_folder + path_slash +str(today)
    if not os.path.exists(sub_file_folder):
     make_folder= os.mkdir(sub_file_folder)
    dir=os.listdir(sub_file_folder)
    all_domain = []
    for file_csv in dir:
        print(file_csv)
        with open(sub_file_folder+path_slash+file_csv ,"r", encoding='utf-8-sig') as file_handle :
            for domains in file_handle:
                # print(domains)
                all_domain.append(domains)
        with open(all_marge_files + path_slash +str(today)+".csv",'w') as ss:
            ss.writelines(iii for iii in all_domain) 
    print("marge all files!")
    print("Done..!")   
def compare_file():
    file1 = pd.read_csv(all_marge_files+path_slash+y_file)
    file2 = pd.read_csv(all_marge_files+path_slash+t_file)
    c_result = file2[~file2.apply(tuple,1).isin(file1.apply(tuple,1))]
    file = pd.DataFrame(c_result)
    file.to_csv(compair_folder+path_slash+t_file,"w",index=False,header=False)
    print("comapare all files!")
    print("Done!")

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
if __name__=="__main__":
    path_slash="\\"
    ScriptPath = os.path.dirname(os.path.abspath(__file__))
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    t_file=str(today)+".csv"
    print(t_file)
    y_file = str(yesterday)+".csv"
    print("file = ",y_file)
    print("1. Parent Script Initiating...")
    input_folder=ScriptPath+path_slash+"input"
    all_marge_files = ScriptPath + path_slash +"marge_file"
    Domain_folder = ScriptPath + path_slash+ "find_domains"
    Source_folder = ScriptPath + path_slash + "find_Source_out"
    compair_folder=ScriptPath+path_slash+"compair_file"
    all_results = compair_folder+path_slash+t_file
    marge_file()
    compare_file()
    upload_to_db(all_results)