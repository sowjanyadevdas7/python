import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("soujanyadevdas@gmail.com","31362512")
message = """\
subject: Testing mail

hello, Good morning!
"""

s.sendmail("soujanyadevdas@gmail.com","soujanyadevdas@gmail.com",message)
print("done")
s.quit()
