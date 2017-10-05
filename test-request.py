import requests
import time

cnt = 0
id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10]
print (time.time())
t_end = time.time() + 1
# id = [2]
# t_start = time.time()
# r = requests.post('http://127.0.0.1:8000/api/get_prediction', data = {"id":3})
# t_end = time.time()
for x in id:	
	while time.time() < t_end:
		r = requests.post('http://127.0.0.1:8000/api/get_prediction', data = {"id":x})
		cnt += 1
		# print (r.json())
print (t_end)
print ("{} request/sec".format(cnt))
# r = requests.post('http://127.0.0.1:8000/api/get_prediction', data = {"id":3, "v":'aa'})
# print(r)