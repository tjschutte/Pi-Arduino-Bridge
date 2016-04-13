import requests
import serial
import time

url = 'http://192.81.208.150/getNumbers'
port = '/dev/ttyACM0'
baudrate = 9600

ser = serial.Serial(port, baudrate)
ser.close()
ser.open()

response = requests.get(url, verify=False) # make connection

# if bad things
if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

# le JSON
data = response.json()


'''debug stuff only uncomment if bad things are happening!'''
'''
#showing entire JSON object for debug
print(data)
#nabbing the terms
term1 = data['term1']
term2 = data['term2']
#disp terms
print('term1: ' + str(term1) + ' term2: ' + str(term2))
'''
# loop forever cause I said so!
while 1:
        # make connection
        response = requests.get(url, verify=False)
        data = response.json()
        # Nabbing the terms so that we can make a string to pass to arduino
        term1 = data['term1']
        if (term1 < 10):
                t1 = "0" + str(term1)
        else:
                t1 = str(term1)
        term2 = data['term2']
        if (term2 < 10):
                t2 = "0" + str(term2)
        else:
                t2 = str(term2)
        packet = "_" + t1 + " " + t2
        ser.write(packet)
        print packet
        time.sleep(1);
