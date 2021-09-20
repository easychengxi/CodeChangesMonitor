import smtplib

class SendEmail:
    def __init__(self,web):
        self.gmail_user = 'chengxi.gao@gmail.com'
        self.gmail_password = 'chengxi89'
        self.to = ['chengxi.gao@mcg.com']
        self.subject = 'test'
        self.body = """
Web page:
%s 
has been updated
""" %web
        self.sent_from = self.gmail_user
        self.email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (self.sent_from, ", ".join(self.to), self.subject, self.body)

    def emailout(self):
        try:
            self.smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.smtp_server.ehlo()
            self.smtp_server.login(self.gmail_user, self.gmail_password)
            self.smtp_server.sendmail(self.sent_from, self.to, self.email_text)
            self.smtp_server.close()
            print ("Email sent successfully!")
        except smtplib.Exception as ex:
            print ("Something went wrong….",ex)