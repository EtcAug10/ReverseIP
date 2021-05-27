from requests import Session,post,get
from re import match,findall

__version__ = "1.0.0"
__name__ = "Reverse Ip Library"
__author__ = "Arya Kresna"

class Osint_SH:
  
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
