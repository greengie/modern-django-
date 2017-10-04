import requests
import time

# t_end = time.time() + 1
# cnt = 0
# while time.time() < t_end:
# 	r = requests.post('http://127.0.0.1:8000/api/get_prediction', data = {"id":3})
# 	cnt += 1
# 	# print (r.json())
# print ("{} request/sec".format(cnt))
r = requests.post('http://127.0.0.1:8000/api/get_prediction', data = {"id":3, "v":'aa'})
print(r)