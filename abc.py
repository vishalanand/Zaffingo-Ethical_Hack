import requests, mechanize

with requests.Session() as c:
	url = "http://www.zaffingo.com/"
	#url = "http://www.zaffingo.com/profile.php?user_id="+str(url_no)
	#http://www.zaffingo.com/profile.php?user_id=230
	USERNAME = 'abcismadarchod@gmail.com'
	PASSWORD = 'zaffazaffa'
	#c.get(url)
	login_data = dict(l_email=USERNAME, l_password=PASSWORD, next='/')
	c.post(url,data=login_data, headers={"Referer": "http://www.zaffingo.com"})
	#page = c.get("http://www.zaffingo.com/profile.php")
	page = c.get("http://www.zaffingo.com/profile.php?user_id=230")
	print page.content
	"""
	for url_no in range(149, 151):
		url = "http://www.zaffingo.com/profile.php?user_id="+str(url_no)
		br = mechanize.Browser()
		br.open(url)
		br.select_form(nr=0)
		br['l_email'] = username
		br['l_password']= password
		br.submit()
		for form in br.forms():
	    	print form
	"""
"""
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
"""
