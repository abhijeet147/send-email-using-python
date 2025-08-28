import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("sender email", "your password")
server.sendmail("sender email", "receiver email", "Hello from Python!")
server.quit()
