from selenium import webdriver
from datetime import datetime
import time




contactList = [
    # phone format -> +XXXxxxxxxxxx
]


print("Please .... Make sure your phone is near you and that you have a stable internet connection")




check = str(input("Did you open whatsapp app in your phone? (y):  \n")) # for user checking
true = True # the main value for the loop

if check == "y": # check for the user resp.
    dateAndTime = datetime.now() # get the time 
    date = dateAndTime.strftime("%b %d %Y") # formate the date
    hourAndMinutes = dateAndTime.strftime("%H:%M") # formate the time
    conter = 1 # the value that we store in it our contacts total number

    while true: # the main loop
        print("Waite please for whats app web open")
        try:
            driver = webdriver.Chrome("/home/hima890/Documents/projects_dontFucingGoThere/whatsApp/chromedriver") # THE DRIVER FULL PATH
            driver.get("https://web.whatsapp.com/") # open the whatsAPP WEB LINK
        except:
            print("An internet error please check your conaction")
        else:

            time.sleep(4)


            message = str(input("Eter the message please:  \n"))

            for number in contactList: # the send mesage loop
                newChat = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[2]/div")
                newChat.click() # click new chat 

                time.sleep(1)

                searsh = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
                searsh.click() # searsh for the contacts number

                time.sleep(0.5)


                intry = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
                intry.send_keys(number) # start rhe searshing

                time.sleep(1.6)

                try: # try blook to catch no much case
                    searshRessolt = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]") # the contact account
                except:
                    time.sleep(1.5)
                    print("no number match!")
                    close = driver.find_element_by_class_name("hYtwT")
                    closed = close.click() # close the serch ressolt
                else: # if the contact account found
                    searshRessolt.click() # click on the searsh resolt

                    time.sleep(.5)

                    try:# to catch the blocked account
                        msgBox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") # solect the maessage bar
                    
                    except:
                        print("blocked account !")

                    else:

                        msgBox.send_keys(message) # type the message

                        time.sleep(.5)

                        send = driver.find_element_by_class_name("_2Ujuu")
                        send.click() # send he message

                        # open file and write a report for the message and the contact
                        with open("/home/hima890/Documents/projects_dontFucingGoThere/whatsApp/reports/reports.txt", "a") as report:
                            report.write(
                                "----------------------------------------------\n" +
                                "Number:  " + str(conter) + "\n" +
                                "Date:  " + str(date) + "\n" +
                                "Time:  "  + str(hourAndMinutes) + "\n" +
                                "Phone number:  " + str(number) + "\n" +
                                "Message:  " + str(message) + "\n" +
                                "----------------------------------------------\n"
                            )
                        conter = conter + 1 # total contact number + 1 after every loop
                time.sleep(2)

        # the faunel report
        with open("/home/hima890/Documents/projects_dontFucingGoThere/whatsApp/reports/reports.txt", "a") as report:
                report.write(
                    "----------------------------------------------\n" +
                    "\t\t\t\t" + "Total sended message:  " + "\n" + "\t\t\t\t"
                    "----------------------------------------------\n"
                )
        
        # an if to guite the programe
        quite = str(input("if you wont to stop type 'y'\n"))
        if quite == 'y':
            true = False
        else:
            true = True
