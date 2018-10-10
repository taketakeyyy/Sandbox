# -*- coding: utf-8 -*-

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

#msg = EmailMessage()
msg = MIMEText("あいう")
msg.set_content("これは本文です")

msg["Subject"] = "これは件名です"
msg["From"] = ""
msg["To"] = ""

FROM_ADDRESS = ""
MY_PASSWORD = ""
s = smtplib.SMTP(host="smtp.mail.yahoo.co.jp", port=587)
s.ehlo()
#s.starttls()
s.ehlo()
s.login(FROM_ADDRESS, MY_PASSWORD)
#s.sendmail(from_addr, to_addrs, msg.as_string())
s.send_message(msg)
s.close()
#s.quit()
