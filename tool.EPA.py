import socket


print("""


          _                             _     ______ _____        
    /\   | |                           | |   |  ____|  __ \ /\    
   /  \  | |__   __ _ _ __   ___  _   _| |__ | |__  | |__) /  \   
  / /\ \ | '_ \ / _` | '_ \ / _ \| | | | '_ \|  __| |  ___/ /\ \  
 / ____ \| |_) | (_| | | | | (_) | |_| | |_) | |____| |  / ____ \ 
/_/    \_\_.__/ \__,_|_| |_|\___/ \__,_|_.__/|______|_| /_/    \_\
                                                                  
 ___ _   _  _    __  __   _   _  _ 
|_ _/ \ / \| |  / _|/ _| / \ | \| |
 | ( o | o ) |_ \_ ( (_ | o || \\ |
 |_|\_/ \_/|___||__/\__||_n_||_|\_|
                                   


                                                                   """)


print(" hello...  this is the tool of eng-Abanoub.EPA")

print("""
my website       (   https://linktr.ee/abanoubepa   )  
                        * contact with me *
""")
print("""
            _   _       
           | | (_)      
  __ _  ___| |_ _ _ __  
 / _` |/ _ \ __| | '_ \ 
| (_| |  __/ |_| | |_) |
 \__, |\___|\__|_| .__/ 
  __/ |          | |    
 |___/           |_|    


""")
import socket
ip = input("enter your site: ")


n = socket.gethostbyname(ip)


print(("  thes your ip   "),n)

print(("thes site"),ip)

print(""" 
 _____  _____ _____ _                     _   _             
|  __ \|  ___|_   _| |                   | | (_)            
| |  \/| |__   | | | |     ___   ___ __ _| |_ _  ___  _ __  
| | __ |  __|  | | | |    / _ \ / __/ _` | __| |/ _ \| '_ \ 
| |_\ \| |___  | | | |___| (_) | (_| (_| | |_| | (_) | | | |
 \____/\____/  \_/ \_____/\___/ \___\__,_|\__|_|\___/|_| |_|
                                                            
           my website       (   https://linktr.ee/abanoubepa   )  
                        * contact with me *  """)


import geocoder
import folium


get_ip = input("get ip: ")

get_ip = geocoder.ip(get_ip)
location = get_ip.latlng


our_map = folium.Map(location=location, zone_start=10)
folium.Marker(location).add_to(our_map)
our_map.save("map.html")


print(location)

print("""                                      _   _       
 ___  ___ __ _ _ __  _ __   ___  _ __| |_(_)_ __  
/ __|/ __/ _` | '_ \| '_ \ / _ \| '__| __| | '_ \ 
\__ \ (_| (_| | | | | |_) | (_) | |  | |_| | |_) |
|___/\___\__,_|_| |_| .__/ \___/|_|   \__|_| .__/ 
                    |_|                    |_|    
     my website       (   https://linktr.ee/abanoubepa   )  
                        * contact with me * """)



import socket
host = input("enter  the ip address: ")
try:
    for port in range(1,2000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0:
            print("the port{}is open.".format(port))
        else:
            print("no port opend")
except:
    print("Error")



