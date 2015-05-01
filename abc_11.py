import requests, mechanize

with requests.Session() as c:
	headers={ 'content-type':'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding': 'gzip, deflate','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0','Referer' : 'http://www.zaffingo.com',
    }
	url = "http://www.zaffingo.com/"
	USERNAME = 'abcismadarchod@gmail.com'
	PASSWORD = 'zaffazaffa'
	c.get(url)
	login_data = dict(l_email='abcismadarchod@gmail.com', l_password='zaffazaffa', next='/')
	c.post(url,data=login_data, headers={"Referer": "http://www.zaffingo.com"})
	for i in range(17,1272):
		c.post(
			url='http://www.zaffingo.com/ajax/add_testimonial.php',
			data={
				'for_user_id': (i),
				'testimonial': ("I want you to know that you are awesome, all the best! :)"),
				'privacy_status': 0 
				}
		)
