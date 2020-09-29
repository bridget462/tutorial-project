import numpy as np
import matplotlib.pyplot as plt
print('library imported')

# params
SAMPLING_NUM = 100
FRAMES = 10
INTERVAL_TIME_SEC = 1

for i in range(FRAMES):
    data = np.random.rand(SAMPLING_NUM)

    plt.plot(data)

    if (i == FRAMES):
        plt.show()
    else:
        plt.draw()
        plt.pause(INTERVAL_TIME_SEC)
        plt.cla()
