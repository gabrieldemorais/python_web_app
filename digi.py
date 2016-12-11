from devicecloud import DeviceCloud

def credentials(user, passw):
	dc = DeviceCloud(user, passw)
	if dc.has_valid_credentials():
		return 'valid'
	else:
		return 'invalid'


def get_stream_id(user, passw):
	dc = DeviceCloud(user, passw)
	result = {}
	for stream in dc.streams.get_streams():
		result[stream] = stream.get_stream_id()
	return result

def get_connected_devices(user, passw):
	dc = DeviceCloud(user, passw)
	
	for device in dc.devicecore.get_devices():
	    if device.is_connected():
	        result = device.get_connectware_id()
	return result

def get_current_stream_value(user, passw, mac_node):
	dc = DeviceCloud(user, passw)
	connectware_id = get_connected_devices(user, passw);
	#stream = dc.streams.get_stream('00000000-00000000-00409DFF-FF6064F8/xbee.analog/[00:13:A2:00:41:53:1C:94]!/AD3')
	stream = dc.streams.get_stream_if_exists(connectware_id+'/xbee.analog/['+mac_node+']!/AD3')
	if stream == None:
		return 'None'		
	else:
		dp = stream.get_current_value()
		return dp.get_data()

if __name__ == '__main__':
	print get_connected_devices('intelidev','DGMsmf@123')
	
	#print get_current_stream_value('00:13:A2:00:40:C4:06:F4')


# # show the MAC address of all devices that are currently connected
#
# # This is done using the device cloud DeviceCore functionality
# print "== Connected Devices =="
# for device in dc.devicecore.get_devices():
#     if device.is_connected():
#         print device.get_mac()

# # get the name and current value of all data streams having values
# # with a floating point type

# This is done using the device cloud stream functionality
# for stream in dc.streams.get_streams():
#    print "%s -> %s" % (stream.get_stream_id(), stream.get_description())

# # Navigate folders
# for dirname, directories, files in dc.filedata.walk():
#     for file in files:
#        print file.get_full_path()

# # Print files
# for dirname, directories, files in dc.filedata.walk():
#     for file in files:
#        print file.get_data()
#        print file.get_customer_id()

# Print files
# for dirname, directories, files in dc.filedata.walk():
#     for file in files:       
#        print file.get_customer_id()


