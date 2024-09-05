import os


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


if __name__ == "__main__":
    print(read_tle("tle/"))
