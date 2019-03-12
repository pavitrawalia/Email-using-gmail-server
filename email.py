import smtplib
fromaddr='pythongeeks5@gmail.com'
toaddr='pavitrawalia@gmail.com'
message='sample'
password='Noreply@'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr, toaddr,message)
print "sucess"
server.quit()
