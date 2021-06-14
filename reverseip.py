from requests import Session,post,get
from re import match,findall
import json

__version__ = "1.0.7"
__name__ = "Reverse Ip Library"
__author__ = "Arya Kresna"

class OsintSH:
  
  def __init__(self):
    self.url = "https://osint.sh/reverseip/"
    self.ip = ""
    self.ua = ""
    self.data = {'domain':self.ip}
  
  def get_data(self,ip,ua=""):
    self.ip = ip
    self.ua = ua
    self.data['domain'] = self.ip
  
  def dump(self):
    if self.ua != "":
      r = post(self.url,data=self.data,headers={"user-agent":self.ua})
    else:
      r = post(self.url,data=self.data)
    return findall(r"Domain\">(.*?)<\/",r.text.replace("\n","").replace(" ",""))

class SonarOmnisintIO:
  
  def __init__(self):
    self.url = "https://sonar.omnisint.io/reverse/"
    self.ip = ""
    self.headers = ""
  
  def get(self,ip,headers=""):
    self.ip = ip
    self.headers = headers
    return True
    
  def dump(self):
    req = get(self.url+self.ip,headers=self.headers).text
    return json.loads(req)
