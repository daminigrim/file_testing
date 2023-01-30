import os
import datetime
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
    Domain_folder = ScriptPath + path_slash+ "find_domains"
    Source_folder = ScriptPath + path_slash + "find_Source_out"
    input_folder=ScriptPath+path_slash+"input"
    all_marge_files = ScriptPath + path_slash +"marge_file"
    sub_file_folder = input_folder + path_slash +str(today)
    if not os.path.exists(sub_file_folder) :
            dd= os.mkdir(sub_file_folder)
    dir=os.listdir(sub_file_folder)
    all_domain = []
    for file_csv in dir:
        print(file_csv)
        with open(sub_file_folder+path_slash+file_csv ,"r", encoding='utf-8-sig') as file_handle :
            for domains in file_handle:
                # print(domains)
                all_domain.append(domains)
    with open(all_marge_files + path_slash +str(today)+".csv",'w',) as ss:
            ss.writelines(iii for iii in all_domain)
    print("done")        