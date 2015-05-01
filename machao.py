import re
import mechanize

username = 'abcismadarchod@gmail.com'
password = 'zaffazaffa'

for url_no in range(149, 151):
	url = "http://www.zaffingo.com/profile.php?user_id="+str(url_no)
	br = mechanize.Browser()
	br.open(url)
	br.select_form(nr=0) #check yoursite forms to match the correct number
	br['l_email'] = username #use the proper input type=text name
	br['l_password']= password #use the proper input type=password name
	br.submit()
	
	for form in br.forms():
	    print form
