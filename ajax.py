import cjson
import urllib
import urllib2
import cookielib
 
URL = "http://www.zaffingo.com"
params = urllib.urlencode({ 'l_email' : 'abcismadarchod@gmail.com', 'l_password' : 'zaffazaffa' })
headers = {"Content-type": "application/x-www-form-urlencoded"}
request = urllib2.Request(URL, params, headers)
cookies = cookielib.CookieJar()
ck_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
try:
    response = ck_opener.open(request)
    rspTxt = response.read()
    rslt = cjson.decode(rspTxt)
except:
    print "Failed open URL\n"
    #return
 
if (rslt['Result'] == 'SUCCESS'):
    print "Login successfully\n"
else:
    print "Login failed\n"
