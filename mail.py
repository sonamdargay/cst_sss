import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("cst.sss101@gmail.com", "Raspberrypi")
server.sendmail(
  "cst.sss101@gmail.com", 
  "sonamdargay167@gmail.com", 
  "this message is from python")
server.quit()