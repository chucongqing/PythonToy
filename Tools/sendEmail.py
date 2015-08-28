#coding:utf-8
import smtplib
import json
from email import Encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from testMail import toEmail


def sendMail(fromEmail, username,  password, serverAddress, subject, htmlContent, toEmail):
    '''
    fromEmail: ʹ���ĸ������ַ����
    username: ��½������������û�����һ����fromEmail��ͬ
    password: ��½������
    serverAddress: �������ĵ�ַ�������˿ڣ�
    subject: �ʼ�����
    htmlContent: �ʼ����ģ�ʹ��html��ʽ��д
    toEmail: Ҫ���͵��������ַ������д���
    '''
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = ', '.join(toEmail)
    msg["Accept-Language"]="zh-CN"                      #ָ�����Ի���������
    msg["Accept-Charset"]="ISO-8859-1,utf-8"        #ָ��ʹ���ض��ı��룬��ֹ����
    part = MIMEText(htmlContent, 'html', 'UTF-8')
    msg.attach(part)
    
    s = smtplib.SMTP(serverAddress)
    print "Try to login"
    s.login(username, password)
    print "login successfully, try to send"
    s.sendmail(fromEmail, toEmail, msg.as_string())
    print "send successfully"
    s.quit()
    

sendMail(fromEmail='chucongqing@163.com', 
         username="chucongqing@163.com", 
         password="caonima250", 
         serverAddress='smtp.163.com:25', 
         subject='Python�ʼ��������', 
         htmlContent="plain text content",
        toEmail= ['chucongqing@qq.com'])