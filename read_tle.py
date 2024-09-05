import os
from pprint import pprint
from matplotlib.pylab import f
import requests


def get_tle_list(path):
    return os.listdir(path)


def read_tle(path):
    tle_files = get_tle_list(path)
    tle = {}

    for tle_data in tle_files:
        idx = 0
        with open(path + tle_data, "r") as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break

                if idx % 3 == 0:
                    name = line
                elif idx % 3 == 1:
                    r = line
                elif idx % 3 == 2:
                    v = line
                    tle[name] = (r, v)
                else:
                    Exception("Error")
                idx += 1

            tle[name] = (r, v)

    return tle


def read_tle_from_tle_api():
    try:
        url = "https://tle.ivanstanojevic.me/api/tle"
        response = requests.get(url)
        tle = {}
        
        if response.status_code != 200:
            raise Exception('API Error with {}'.format(response.status_code))
        data = response.json()
        
        for member in data.member:
            tle[member.name] = (member.line1, member.line2)
            
        return tle
    except Exception as e:
        print(e)
        return {}

if __name__ == "__main__":
    print(read_tle("tle/"))
