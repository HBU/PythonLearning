import time
localtime = time.localtime(time.time())
print ("本地时间为(未格式化) :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)