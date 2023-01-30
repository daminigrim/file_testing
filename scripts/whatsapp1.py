from alright import WhatsApp
import time
import os
if __name__ == "__main__":
    Script_path = os.getcwd()
    ###################### number file path #######################
    PathSlash = "\\"
    Number_file = Script_path + PathSlash + "numbers.csv"
    messenger = WhatsApp()
    ##################### read file ########################
    N_file = open(Number_file,'r')
    N_read = N_file.readlines()
    for number in N_read:
        find_num = number.replace("\n",'')
        if len(find_num) == 10:
            messenger.find_user(find_num)
            time.sleep(1)
            # message = "hello"
            messenger.send_file(r"find_domains\Domain_file(16).csv")
            # messenger.send_message("Today Not Found Any Domain!")
            # messenger.send_file('path-to-file') # send file with this function
            # messenger.send_picture('path-to-file') # send file with this function
            time.sleep(10)
            print("send message successfuly to ",find_num)
        else:
            print("Number is worng = ",find_num)