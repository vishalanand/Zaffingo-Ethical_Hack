from requests import Session

session = Session()
session.head('http://www.zaffingo.com')
response = session.post(
    url='ajax/add_testimonial.php',
    data={
        'for_user_id': (230),
        'testimonial': ("aaa"),
        'privacy_status': 0 
    },
    headers={
        'Referer': 'http://sportsbeta.ladbrokes.com/football'
    }
)

print response.text


url = "http://www.zaffingo.com/"
    USERNAME = 'abcismadarchod@gmail.com'
    PASSWORD = 'zaffazaffa'
    #c.get(url)
    login_data = dict(l_email=USERNAME, l_password=PASSWORD, next='/')
    c.post(url,data=login_data, headers={"Referer": "http://www.zaffingo.com"})
    page = c.get("http://www.zaffingo.com")
    print page.content