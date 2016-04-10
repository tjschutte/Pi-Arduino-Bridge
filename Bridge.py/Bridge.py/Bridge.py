import requests
import serial

url = 'http://192.81.208.150/getNdumbers'
port = '/dev/ttyACM0'
baudrate = 9600

ser = serial.Serial(port, baudrate)
ser.open()

response = requests.get(url, verify=False) # make connection

# if bad things
if response.status_code != 200:
	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	exit()

# le JSON
data = response.json()

'''debug stuff

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
	# Nabbing the terms so that we can make a string to pass to arduino
	term1 = data['term1']
	term2 = data['term2']
	packet = str(term1) + " + " + str(term2)
	ser.write(packet)