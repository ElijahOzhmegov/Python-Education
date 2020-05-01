import pandas as pd
import modin.pandas as mpd
import time
import os

# os.environ["MODIN_ENGINE"] = "ray"  # Modin will use Ray


if __name__ == '__main__':
    name = 'us-counties.csv'

    s = time.time()
    df = pd.read_csv(name)
    e = time.time()
    print("Pandas Concat Time = {}".format(e - s))


    s = time.time()
    mdf = mpd.read_csv(name)
    e = time.time()
    print("Modin Concat Time = {}".format(e - s))