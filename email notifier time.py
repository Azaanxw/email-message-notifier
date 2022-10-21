import smtplib
sender = input("Enter the email that is going to be sending the message (gmail account e.g. test123@gmail.com): ")
reciever = input("Enter the email that the message is going to: ")
server = smtplib.SMTP("smtp.gmail.com",587)
app_pass = input("Enter app_password for your gmail account (check README if unsure): ")
server.starttls()
message = input("Message: ")
server.login(sender,app_pass)
server.sendmail(sender,reciever,message)
