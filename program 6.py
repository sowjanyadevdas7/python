import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("soujanyadevdas@gmail.com","31362512")
message = "hello"
server.sendmail("sowjanya.16cs@cmr.edu.in","sowjanya.16cs@cmr.edu.in",message)
print("soujanya")
server.quit()
