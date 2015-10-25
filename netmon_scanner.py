import pytz
import requests
from datetime import datetime
import tzlocal


BASE_URL = 'http://localhost:8080/netmon/api'


def main():
    mac_address = '82-92-6E-49-3D-F6'
    local_timezone = str(tzlocal.get_localzone())
    status_timestamp = str(datetime.now(pytz.timezone(local_timezone)))

    payload = {'device': mac_address, 'timestamp': status_timestamp}
    url = '%s/deviceStatus/' % BASE_URL
    response = requests.post(url, json=payload)
    print response.json()
    #utc_timestamp = str(dateparse.parse_datetime(status_timestamp).astimezone(pytz.utc))
    #response = requests.get(url)
    #print response.json()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
