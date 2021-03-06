import requests
import json
from datetime import datetime, timedelta
from tracking_mgt.models import GpsData, LastLocation, BlackList
import time

class GPSHandler():
    base_url="http://api.gps.id/"
    address = ''
    apikey = ''
    birthday = ''
    coname = ''
    createdate = ''
    domain = ''
    email = ''
    fullname = ''
    campaign_name = ''
    id = ''
    password = ''
    phone = ''
    privilege = ''
    remark = ''
    sessionKey = ''
    username = ''
    
    profile = {}
    vehicles = {}

    def get_data(self,url, data):
        #print(url)
        response = requests.post(url, data=data).text
        print(response)
        try:
            data = json.loads(response)['data']
        except Exception as e:
            print(e)
            data={'response':'NO'}
        return data

    def get_data_last_location(self,lat, lng):
        url = "https://nominatim.openstreetmap.org/reverse?\
        format=json&lat=%s&lon=%s&zoom=18&addressdetails=1"\
        %(lat, lng)
        response = requests.get(url).text
        print(response)
        try:
            data = json.loads(response)
        except Exception as e:
            print(e)
            data = ""
        return data

    def login(self):
        path = 'login'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'password': self.password,
            }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.sessionKey = data['sessionKey']
                self.apikey = data['apikey']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def logout(self):
        path = 'logout'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.sessionKey = ''
                self.apikey = ''
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_profile_user(self):
        path = 'profile'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.profile = data['profile']
                self.id = self.profile['id']
                self.apikey = self.profile['apikey']
                self.privilege = self.profile['privilege']
                self.fullname = self.profile['fullname']
                self.conama = self.profile['coname']
                self.phone = self.profile['phone']
                self.email = self.profile['email']
                self.address = self.profile['address']
                self.remark = self.profile['remark']
                self.createdate = self.profile['createdate']
                self.birthday = self.profile['birthday']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_all_vehicle(self):
        path = 'getvehicle'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.vehicles = data['vehicle']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_locate_vehicle(self, terminal):
        path = 'locatevehicle'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey,
            'terminal': terminal
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                vehicle = data['vehicle']
                return {'response':'OK', 'vehicle': vehicle}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_history_vehicle(self, terminal, date_start, date_end):
        path = 'track'
        url = self.base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey,
            'terminal': terminal,
            'gpsstart': date_start,
            'gpsend': date_end
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                track = data['track']
                return {'response':'OK', 'track': track}
        except Exception as e:
            print(e)
        return {'response':'NO'}

credentials = {
    'phd' : {
        'username' : 'abpluss_phd',
        'password' : 'ABPluss88'
    },
    'marugame' : {
        'username' : 'ABPLUSS_MARUGAMEJKT',
        'password' : '000000'
    },
}

max_day = 0
day = 2
last_day = day - 1
campaign_name = input('Masukan nama campaign:') 
try:
    day = int(input('Masukan hari:'))
    last_day = day - 1
except Exception as e:
    print(e)
    exit()
try:
    credential = credentials[campaign_name]
except:
    print('campaign not found')
    exit()
while True:
    print('Getting data from the last %s day'%day)
    time.sleep(3)
    gps_handler = GPSHandler()
    gps_handler.username = credential['username']
    gps_handler.password = credential['password']
    res = gps_handler.login()
    print('LOGIN TO DATABASE CAMPAIGN : %s'%campaign_name)
    if res['response'] == 'OK':
        print("Login as {} Success".format(gps_handler.username))
        print("Session Key : {}".format(gps_handler.sessionKey))
        print("Api Key : {}".format(gps_handler.apikey))
    else:
        print("Login Failed")
        exit()
    res = gps_handler.get_profile_user()
    if res['response'] == 'OK':
        print("Get Profile of {} Success".format(gps_handler.username))
    else:
        print("Get Profile User Failed")
        exit()

    now = datetime.now()
    while day > max_day:
        res = gps_handler.get_all_vehicle()
        if res['response'] == 'OK':
            print("Get all vehicles of {} Success".format(gps_handler.username))
        else:
            print("Get all vehicles Failed")
            exit()
        date_start = now - timedelta(days = day) + timedelta(hours = 7)
        date_now = now - timedelta(days = last_day) + timedelta(hours = 7)
        date_start = date_start.strftime('%Y-%m-%d %H:%M:%S')
        date_end = date_now.strftime('%Y-%m-%d %H:%M:%S')

        print('Getting data from %s'%date_start)
        print('to %s'%date_end)
        time.sleep(13)
        day -= 1
        last_day = day - 1
        for vehicle in gps_handler.vehicles:
            history = {}
            license_no = vehicle['license']
            try:
                blocked = BlackList.objects.get(
                    campaign_name = campaign_name,
                    license_no = license_no
                    )
            except:
                blocked = False

            if blocked:
                continue
            print('Get location of {}'.format(license_no))
            location = gps_handler.get_locate_vehicle(vehicle['terminal'])
            try:
                location_data = location['vehicle'][0]
                #print(json.dumps(track_data, indent=4, sort_keys=True))
            except Exception as e:
                location_data = 'NONE'
                print(e)
                print(location)
                continue
            print(location_data)
            if location_data:
                timestamp = location_data['time_second']
                timeformat = datetime.strptime(location_data['time_format'], '%d %b %Y %H:%M:%S')
                last_location, stat = LastLocation.objects.get_or_create(
                        license_no = license_no.replace(" ","").upper(),
                        campaign_name = campaign_name
                    )
                #print(gps.timestamp)
                if last_location:
                    last_location.data = location_data
                    last_location.timestamp = timestamp
                    last_location.created_date = timeformat
                    last_location.latitude = location_data['latitude']
                    last_location.longitude = location_data['longitude']
                    last_location.status_vehicle = location_data['status_vehicle']
                    last_location.status_engine = location_data['status_engine']
                    last_location.mileage = location_data['mileage']
                    last_location.save()
                print('%s - %s'%(last_location, stat))
                print('Getting last location data of %s'%license_no)
                last_location_data = gps_handler.get_data_last_location(last_location.latitude, last_location.longitude)
                if last_location_data:
                    last_location.address = last_location_data['display_name']
                    try:
                        city = last_location_data['address']['state_district']
                    except Exception as e:
                        print(e)
                        try:
                            city = last_location_data['address']['state']
                        except Exception as e:
                            print(e)
                            try:
                                city = last_location_data['address']['city']
                            except Exception as e:
                                print(e)
                                city = "Other"

                    last_location.city = city
                    try:
                        postcode = last_location_data['address']['postcode']
                    except Exception as e:
                        print(e)
                        postcode = ''
                    last_location.postal_code = postcode
                    last_location.save()
                    print(last_location.city)


            print('Get history of {}'.format(license_no))
            history = gps_handler.get_history_vehicle(vehicle['terminal'], date_start, date_end)
            try:
                track_data = history['track']['track_data']
                #print(json.dumps(track_data, indent=4, sort_keys=True))
            except Exception as e:
                track_data = 'NONE'
                print(e)
                print(history)
                continue
            print(track_data)

            idx=0
            if track_data:
                #print(GpsData.objects.all().count())
                #print([data for data in track_data])
                license_plate = license_no.replace(" ","").upper()
                for data in track_data:
                    idx += 1
                    timestamp = data['time_second']
                    timeformat = datetime.strptime(data['time_format'], '%d %b %Y %H:%M:%S')
                    gps, stat = GpsData.objects.get_or_create(
                            license_no = license_plate,
                            timestamp = timestamp
                        )
                    #print(gps.timestamp)
                    if gps:
                        gps.data = data
                        gps.campaign_name = campaign_name
                        gps.created_date = timeformat
                        gps.save()
                    print('%s :: %s : %s - %s - %s -%s'%(gps.campaign_name, license_no.replace(" ","").upper(), idx, stat, data['time_format'], gps.campaign_name))
                    


    is_logged_out = gps_handler.logout()
    if is_logged_out['response'] == 'OK':
        print('DONE')
        del(gps_handler)
    else :
        print('LOGOUT ERROR')
        del(gps_handler)

    max_day = 0
    day = 1
    last_day = day - 1

    sleep_time = 240
    st = 0
    print("sleeping for %s minutes"%(sleep_time))
    while st <= sleep_time:
       st += 1
       print("%s minutes remaining"%(sleep_time-st))
       time.sleep(60)
