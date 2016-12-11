import csv
from digi import get_current_stream_value

def get_pin_parameters():
	with open('pin_list.csv', 'rb') as f:
		reader = csv.reader(f)
		pin = []
		for row in reader:	   
			if row[1] == 'active':				
				pin = [row[0], row[2], row[3], row[4], row[5]]				
	return pin

def set_threshold(value):
	with open('pin_list.csv', 'rb') as f:
		reader = csv.reader(f)
		lines = [l for l in reader]

		for row in lines:
			if(row[1] == 'active'):
				row[4] = value
	with open('pin_list.csv', 'wb') as g:
		writer = csv.writer(g)
		writer.writerows(lines)
	return lines

def get_geolocation_from_mac(user, passw, mac_address):
	pin = get_pin_parameters()
	with open('mac_list.csv', 'rb') as f:
		reader = csv.reader(f)		
		geo = []
		for row in reader:	   
			if row[0] == mac_address:				
				geo = [row[1], row[2], get_current_stream_value(user, passw, mac_address.upper()), pin[3], pin[4]]				
	return geo

def get_geolocation_from_list_of_macs(user, passw, list_of_macs):
	location = []
	cnt = 0;
	with open('mac_list.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			found = 0;
			for i in list_of_macs:
				if(i == row[0]):
					location.append(get_geolocation_from_mac(user, passw, list_of_macs[cnt]))
					cnt = cnt + 1;
					found = 1
			if (found == 0):
				location.append([row[1], row[2], 'disconnected'])

	return location

if __name__ == '__main__':
	# MAC = ["00:13:a2:00:40:c4:06:f4", "00:13:a2:00:41:48:32:bb"]
	# result = get_geolocation_from_list_of_macs('intelidev', 'DGMsmf@123', MAC)		
	# print result
	a = set_threshold('150')

	