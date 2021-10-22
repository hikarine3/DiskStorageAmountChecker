import os
import re
from firstclass_dotenv import Dotenv
import smtplib
import subprocess
from email.header import Header
from email.mime.text import MIMEText
from email import charset
from pprint import pprint

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class DiskStorageAmountChecker():

    def help(self):
        print("Example:")
        print("python3 DiskStorageAmountChecker.py --email=aaa@example.com --servers=server1,server2 --alert=70 --user=ssh_user_id --env_file=...")
        sys.exit(0)

    def __init__(self):
        self.alert = str(50)
        self.servers = []
        self.user = ''
        self.result = ''
        self.debug = 0
        env_file = '.env'

        for argv in sys.argv[1:]:
            matches = []
            if re.search('^--', argv):
                if argv == '--debug':
                    self.debug += 1
                elif re.search('=', argv):
                    matches = re.findall( r'^--([^=]+)=([^=]+)$', argv, re.IGNORECASE | re.DOTALL)
                    name = matches[0][0]
                    value = matches[0][1]
                    if name == 'alert':
                        self.alert = value
                    elif name == 'email':
                        self.email = value
                    elif name == 'env_file':
                        env_file = value
                    elif name == 'user':
                        self.user = value
                    elif name == 'servers':
                        self.servers = value.split(',')

        if(os.path.exists(env_file)):
            dotenv = Dotenv()
            dotenv.load(env_file)
            self.smtp_server = os.environ['MAIL_HOST']
            self.smtp_port = os.environ['MAIL_PORT']
            self.smtp_user = os.environ['MAIL_USERNAME']
            self.smtp_password = os.environ['MAIL_PASSWORD']
            self.from_email = os.environ['MAIL_FROM_ADDRESS']
        elif self.email or self.user:
            print(env_file + "doesn't exist. this must exist and have to include necessary values")
            sys.exit()

        if self.email == "":
            print("please input --email=...")
            sys.exit()

    def check(self):
        for server in self.servers:
            cm = 'ssh -l ' + self.user + ' ' + server +' "df -kh" | perl -e ' +"'" + 'while(<>){$_=~ s{(\d+)\%}{if($1>=' + self.alert + '){print("' + server + '"."\t".$_);}}e;}'+"'"
            print(cm)
            result = subprocess.check_output([cm], shell=True).decode("UTF-8")
            if result:
                self.result += result
            print(self.result)
    
    def report(self):
        if self.result and self.email and self.from_email:
            subject = 'alert: disk full is near'
            self.send({'body':self.result, 'from':self.from_email, 'to':self.email, 'subject':subject})

    def send(self, op):
        cset = 'utf8'
        msg = MIMEText(op['body'], 'plain', cset)
        msg['Subject'] = Header(op['subject'], cset)
        msg['From'] = op['from']
        msg['To'] = op['to']

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            if self.debug:
                server.set_debuglevel(1)
            if self.smtp_user and self.smtp_password:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
            server.sendmail(op['from'], [op['to']], msg.as_string())
            server.quit()
            print("Sent email")
        except:
            print("Failed to send email / ")
            print(sys.exc_info()[0])
            pprint(op)
            print(self.smtp_server)
            print(self.smtp_port)
            print(self.smtp_user)
            print(self.smtp_password)
            sys.exit(1)

    def run(self):
        self.check()
        self.report()

if __name__ == '__main__':
    pro = DiskStorageAmountChecker()
    pro.run()
