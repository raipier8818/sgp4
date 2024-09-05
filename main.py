from datetime import date
import datetime
import sys
from sgp4.api import Satrec, jday
from draw import draw_orbits_eci
from read_tle import read_tle, read_tle_from_tle_api
import numpy as np

def main(mode:str="local"):
    if mode == "local":
        tles = read_tle("tles/")
    else:
        tles = read_tle_from_tle_api()
    data = {}

    today = datetime.datetime.now()
    year = today.year
    month = today.month
    day = today.day
    jd_today = jday(year, month, day, 0, 0, 0)[0]


    for name in tles.keys():
        sat = Satrec.twoline2rv(tles[name][0], tles[name][1])
        period = 2 * np.pi / (sat.nm * 60 * 24)
        jd = np.arange(jd_today, jd_today + period, 0.0001)
        fr = np.zeros(len(jd))
        e, r, v = sat.sgp4_array(jd, fr)

        data[name] = np.array(r)

    draw_orbits_eci(data)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"
    mode_type = ["local", "remote"]
    if mode not in mode_type:
        raise Exception(f"Mode must be one of {mode_type}")

    main(mode)