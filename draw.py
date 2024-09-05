from calendar import c
from time import sleep
import matplotlib.pyplot as plt
import numpy as np


def draw_orbits_eci(data: dict):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    a = 6378
    b = 6356

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = a * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color="b", alpha=0.5)
    colors = ["r", "g", "b", "y", "m", "c", "k"]
    idx = 0
    for name in data.keys():
        color = colors[idx]
        idx += 1
        idx %= len(colors)

        ax.plot(
            data[name][:, 0],
            data[name][:, 1],
            data[name][:, 2],
            label=name,
            color=color,
        )
        ax.plot(
            [data[name][0, 0], data[name][-1, 0]],
            [data[name][0, 1], data[name][-1, 1]],
            [
                data[name][0, 2],
                data[name][-1, 2],
            ],
            # color=color,
        )

    plt.legend(
        data.keys(), loc="lower left", fontsize="x-small", bbox_to_anchor=(1.2, 0.0)
    )
    plt.show()


def draw_point_eci(data: dict):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    a = 6378
    b = 6356

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = a * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color="b", alpha=0.5)

    colors = ["r", "g", "b", "y", "m", "c", "k"]
    idx = 0
    for name in data.keys():
        color = colors[idx]
        idx += 1
        idx %= len(colors)

        ax.scatter(
            data[name][0],
            data[name][1],
            data[name][2],
            label=name,
            color=color,
        )

    plt.legend(
        data.keys(), loc="lower left", fontsize="x-small", bbox_to_anchor=(1.2, 0.0)
    )
    plt.show()


if __name__ == "__main__":
    draw_orbits_eci(None)
