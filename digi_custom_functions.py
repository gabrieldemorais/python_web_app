import httplib
import base64 
from lxml import etree
from digi import get_connected_devices

def get_mac_from_device_list(response_body):
	root = etree.XML(response_body)
	#root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")
	results = root.findall('sci_reply')
	#textnumbers = [r.findall('send_message/device/rci_reply/do_command/discover/device/ext_addr').text for r in results]
	textelem = root.findall('send_message/device/rci_reply/do_command/discover/device/ext_addr')
	str_out = []
	for r in textelem:
		oldstr = r.text
		newstr = oldstr.replace("!","")
		str_out.append(newstr) 
	return str_out

def get_device_list(user, passw):
	username = user 
	password = passw 

	auth = base64.encodestring("%s:%s"%(username,password))[:-1]
	webservice = httplib.HTTPSConnection("devicecloud.digi.com")
	webservice.putrequest("GET", "/ws/XbeeCore")
	webservice.putheader("Authorization", "Basic %s"%auth)
	webservice.endheaders()

	# get the response
	response = webservice.getresponse()
	statuscode = response.status
	statusmessage = response.reason
	response_body = response.read()
	return get_mac_from_device_list(response_body)

def discover_nodes(user, passw):
	username = user 
	password = passw

	auth = base64.encodestring("%s:%s"%(username,password))[:-1]

	connectware_id = '"'+get_connected_devices(user, passw)+'"';

	# message to send to server
	message = """
	<sci_request version="1.0">
	  <send_message allowOffline="false">
	    <targets>
	      <device id="""+connectware_id+"""/>
	    </targets>
	    <rci_request version="1.1">
	      <do_command target="zigbee">
	        <discover option="clear"/>
	      </do_command>
	    </rci_request>
	  </send_message>
	</sci_request>
	"""
	webservice = httplib.HTTPSConnection("devicecloud.digi.com")
	webservice.putrequest("POST", "/ws/sci")
	webservice.putheader("Authorization", "Basic %s"%auth)
	webservice.putheader("Content-type", "text/xml")
	webservice.putheader("Content-length", "%d" % len(message))
	webservice.putheader("Accept", "text/xml");
	webservice.endheaders()
	webservice.send(message)

	# get the response
	response = webservice.getresponse()
	statuscode = response.status
	statusmessage = response.reason
	response_body = response.read()

	# print the output to standard out
	# print (statuscode, statusmessage)
	return get_mac_from_device_list(response_body)


def turn_led_on(user, passw):
	username = user 
	password = passw

	auth = base64.encodestring("%s:%s"%(username,password))[:-1]

	# message to send to server
	message = """
	<sci_request version="1.0">
	  <send_message allowOffline="false">
	    <targets>
	      <device id="00000000-00000000-00409DFF-FF6064F8"/>
	    </targets>
	<rci_request version="1.1">
	  <do_command target="zigbee">
	    <set_setting addr="00:13:A2:00:41:53:1C:94!">
	      <radio>
	        <dio4_config>4</dio4_config>
	      </radio>
	    </set_setting>
	  </do_command>
	</rci_request>
	</send_message>
	</sci_request>
	"""
	webservice = httplib.HTTPSConnection("devicecloud.digi.com")
	webservice.putrequest("POST", "/ws/sci")
	webservice.putheader("Authorization", "Basic %s"%auth)
	webservice.putheader("Content-type", "text/xml")
	webservice.putheader("Content-length", "%d" % len(message))
	webservice.putheader("Accept", "text/xml");
	webservice.endheaders()
	webservice.send(message)

	# get the response
	response = webservice.getresponse()
	statuscode = response.status
	statusmessage = response.reason
	response_body = response.read()

	# print the output to standard out
	# print (statuscode, statusmessage)
	return "sent"



if __name__ == '__main__':

	response_body = discover_nodes()
	print response_body
	

