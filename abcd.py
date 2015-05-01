import mechanize, cookielib, urllib, logging, sys
from mechanize import ParseResponse, urlopen, urljoin

def main():
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    r= br.open('http://www.zaffingo.com')

    # Select the second (index one) form
    br.select_form(nr=0)

    # User credentials
    br.form['l_email'] = 'abcismadarchod@gmail.com'
    br.form['l_password'] = 'zaffazaffa'

    # Login
    br.submit()

    # Open up comment page
    posting = 'http://www.zaffingo.com/profile.php?user_id=230'
    rval = 'PoopSandwiches'
    # you can get the rval in other ways, but this will work for testing

    r = br.open(posting)
    print r.read()  # body
    print "Fuck You"
    for i in br.forms():
    	print i
    	#continue
    html = br.response().readlines()
    #print html
    print "Here it goes"
    """
    br = mechanize.Browser()
    br.select_form(nr=0)
    print "Starting the posting action"
    br.form.new_control('textarea','unexistent',{'value':''})
    br.form.fixup()
    br['unexistent'] = 'Hello'
    br.submit()
    """

main()
