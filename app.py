from flask import * #Flask, request, render_template
from digi import *
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from read_csv import *
from digi_custom_functions import *
import os

app = Flask(__name__)

username = 0
password = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	global username
	global password
	if request.method == 'POST':		
		username = request.form['username']
		password = request.form['password']
		if credentials(username, password) == 'valid':
			session['logged_in'] = True
			return redirect(url_for('mapview')) 	
	return render_template('login.html')

@app.route("/map", methods=['GET', 'POST'])
def mapview():
	global username
	global password
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		print '[logged in]'	
		print credentials(username, password)	
		device_list = discover_nodes(username, password);	
		pin_parameters = get_pin_parameters();
		current_threshold = pin_parameters[3];
		location = get_geolocation_from_list_of_macs(username, password, device_list)
	
		if request.method == 'POST':
			new_threshold = request.form['threshold']
			set_threshold(new_threshold)
			pin_parameters = get_pin_parameters();
			current_threshold = pin_parameters[3];

		return render_template('map.html', loc = location, current_threshold = current_threshold)	
	
@app.route("/logout")
def logout():
	session['logged_in'] = False
	return redirect(url_for('login')) 	

@app.route("/send")
def send_message():
	#device_list = get_device_list();
	username = 'intelidev'
	password = 'DGMsmf@123'
	turn_led_on(username, password)	
	#return render_template('send.html')
	return "use led on"

@app.route("/limite", methods=['GET', 'POST'])
def limite():
	pin_parameters = get_pin_parameters();
	current_threshold = pin_parameters[3];

	if request.method == 'POST':
		new_threshold = request.form['threshold']
		set_threshold(new_threshold)

	return render_template('limite.html', current_threshold = current_threshold)

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run()