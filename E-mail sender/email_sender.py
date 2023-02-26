from email.message import EmailMessage
import ssl
import smtplib

e_send='golamthauhid@gmail.com'
e_pass='kbnwyozqemxgbsfr'

e_receive=input("Enter the email address: ")
sub='Python project check'
body="""
I made an python project that can send emails.
"""
em= EmailMessage()
em['From']=e_send
em['To']=e_receive
em['Subject']=sub
em.set_content(body)

context= ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(e_send, e_pass)
    smtp.sendmail(e_send, e_receive, em.as_string())