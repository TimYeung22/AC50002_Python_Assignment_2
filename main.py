import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():
    growlocation = pd.read_csv("GrowLocations.csv")
    LongRange = [50.681, 57.985]
    LatRange = [-10.592, 1.6848]
    location = growlocation
    location = location.loc[location['Longitude'] > LongRange[0]]
    location = location.loc[location['Longitude'] < LongRange[1]]
    location = location.loc[location['Latitude'] > LatRange[0]]
    location = location.loc[location['Latitude'] < LatRange[1]]
    map = "map7.png"
    im = plt.imread(map)
    fig, ax = plt.subplots()
    plt.title("Plotting Grow Data")
    im = ax.imshow(im, extent=[LatRange[0], LatRange[1], LongRange[0], LongRange[1]])
    for index, row in location.iterrows():
        ax.plot(row['Latitude'], row['Longitude'], 'bo')
    plt.savefig("result.png")

if __name__ == '__main__':
    main()
