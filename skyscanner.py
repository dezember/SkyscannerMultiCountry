import numpy 
import webbrowser
import time

country=["IN","AF","AL","DZ","AS","AO","AI","AQ","AG","AR","AM","AW","AU","AT","AZ","BS","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BA","BW","BR","VG","BN","BG","BF","BI","KH","CM"
,"CA","CV","BQ","KY","CF","TD","CL","CN","CX","CC","CO","KM","CG","CK","CR","HR","CU","CW","CY","CZ","DK","DJ","DM","DO","CD","TL","EC","EG","SV","GQ","ER","EE","ET","FK","FO"
,"FJ","FI","FR","GF","PF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GU","GT","GG","GN","GW","GY","HT"
,"HN","HK","HU","IS","IN","ID","IR","IQ","IE","IL","IT","CI","JM","JP","JO","KZ","KE","KI","KO","KW","KG","LA","LV","LB","LS","LR","LY","LT","LU","MO","MG","MW","MY","MV","ML","MT","MH","MQ","MR","MU","YT","MX","FM","MD","MC","MN","ME","MS","MA","MZ","MM","NA","NR","NP","NL","NC","NZ","NI","NE","NG","NU","KP","MP","NO","OM","PK","PW","PA","PG","PY","PE","PH","PL","PT","PR","QA","MK","RE","RO","RU","RW","BL","KN","LC","VC","WS","ST","SA","SN","RS","SC","SL","SG","SK","SI","SB","SO","ZA","KR","SS","ES","LK","SX","PM","SD","SR","SZ","SE","CH","SY","TW","TJ","TZ","TH","TG","TO","TT","TN","TR","TM","TC","TV","UG","UA","AE","UK","US","UY","UZ","VU","VE","VN","VI","WF","YE","ZM","ZW"]
 

for i in country:
        url="http://www.skyscanner.net/transport/flights/nyca/ams/150310/150515/airfares-from-new-york-to-amsterdam-in-march-2015-and-may-2015.html?adults=1&children=0&infants=0&cabinclass=economy&preferdirects=false&rtn=1&outboundaltsenabled=false&inboundaltsenabled=false&usrplace="+i+"&_ga=1.261604493.1064652340.1416570493"
        webbrowser.open_new_tab(url)
        time.sleep(4)
        #print i
        
