import smtplib as smt
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
sender='Youremail'
receiver=input("Receiver: ") #reciever email
subject=input("Subject: ") #subject of mail
msg=MIMEMultipart()
msg['From']=sender
msg['To']=receiver
msg['Subject']=subject
body=input("Body: ") # Enter of body mail
msg.attach(MIMEText(body,'plain'))
filename=input('File(txt/png/jpeg/jpg): ') # Files to upload
attachment=open(filename,'rb')
part=MIMEBase('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text=msg.as_string()
server=smt.SMTP('smtp.gmail.com',587) #using the smtp server
server.starttls()
server.login(sender,'Passward')
server.sendmail(sender,receiver,text)
server.quit()
