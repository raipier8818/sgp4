import math
from draw import draw_point_eci

def point_to_eci(latitiude, longitude):
    r = 6365

    x = (
        r
        * math.cos(math.radians(latitiude))
        * math.cos(math.radians(longitude))
    )
    y = (
        r
        * math.cos(math.radians(latitiude))
        * math.sin(math.radians(longitude))
    )
    z = r * math.sin(math.radians(latitiude))

    return (x, y, z)

def eci_to_ecef(x, y, z, time):
    angle = 15 * time

    x = (
        x * math.cos(math.radians(angle))
        + y * math.sin(math.radians(angle))
    )
    y = (
        -x * math.sin(math.radians(angle))
        + y * math.cos(math.radians(angle))
    )
    z = z

    return (x, y, z)

def ecef_to_eci(x, y, z, time):
    angle = 15 * time

    x = (
        x * math.cos(math.radians(angle))
        - y * math.sin(math.radians(angle))
    )
    y = (
        x * math.sin(math.radians(angle))
        + y * math.cos(math.radians(angle))
    )
    z = z

    return (x, y, z)


    
if __name__ == "__main__":
    