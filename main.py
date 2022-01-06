import threading
import YanAPI

ips = ["10.123.41.14", "10.123.41.23"]

def robot_dance(ip):
    YanAPI.yan_api_init(ip)
    YanAPI.start_play_motion(name="GangnamStyle")

x = threading.Thread(target=robot_dance, args=(ips[0],))
y = threading.Thread(target=robot_dance, args=(ips[1],))

x.start()
y.start()

for ip in ips:
    YanAPI.yan_api_init(ip)
    YanAPI.start_play_motion(name="Stop")
