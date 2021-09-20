import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class SendEmail:
    def __init__(self, web):
        self.strFrom = 'MCGsystemcontrol@gmail.com'
        self.strTo = ['chengxi.gao@mcg.com','erin.johnson@mcg.com']
        # Create the root message and fill in the from, to, and subject headers
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = 'Web page got updated'
        self.msgRoot['From'] = self.strFrom
        self.msgRoot['To'] = ", ".join(self.strTo)
        self.msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        self.msgAlternative = MIMEMultipart('alternative')
        self.msgRoot.attach(self.msgAlternative)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        self.msgText = MIMEText(
            'Website <b><i>%s</i> </b> got updated. \rScreenshot: \r <br><img src="cid:image1"><br>' % web, 'html')
        self.msgAlternative.attach(self.msgText)

        # This example assumes the image is in the current directory
        self.fp = open('C:/Users/cgao/Documents/Python projects/CodeChangesMonitor/web_screenshot.png', 'rb')
        self.msgImage = MIMEImage(self.fp.read())
        self.fp.close()

        # Define the image's ID as referenced above
        self.msgImage.add_header('Content-ID', '<image1>')
        self.msgRoot.attach(self.msgImage)

    def emailout(self):
        try:
            self.smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.smtp_server.ehlo()
            self.smtp_server.login('MCGsystemcontrol@gmail.com', 'W3lcom3123#')
            self.smtp_server.sendmail(self.strFrom, self.strTo, self.msgRoot.as_string())
            self.smtp_server.close()
            print("Email sent successfully!")
        except Exception as ex:
            print("Something went wrong….", ex)