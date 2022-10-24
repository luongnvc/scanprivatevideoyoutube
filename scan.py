import requests
import secrets
import string
import threading

N = 12

def randomString():
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase +string.digits)
		for i in range(N))
    return res
def scanVideo():  
	a = 0  
	while 1 > 0:
		url = 'https://www.youtube.com/watch?v='+randomString()+'&ab_channel=TMGROUP2'
		x = requests.get(url)
		textHtml = x.text
	
		if "lengthSeconds" in textHtml:
			print(url)
for z in range(5):			
	x = threading.Thread(target=scanVideo, args=())
	x.start()
	y = threading.Thread(target=scanVideo, args=())
	y.start()
	z = threading.Thread(target=scanVideo, args=())
	z.start()	
  	
	
print(threading.active_count())
print(threading.enumerate())

