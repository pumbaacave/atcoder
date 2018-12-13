import numpy as np
from scipy.signal import convolve2d


def get_power_level(x, y, grid_serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5
    return power_level


def cal_power_matrix():
    GRID_SERIAL = 9810
    MEM = np.zeros((300,300),dtype='int8')
    for i in range(1,301):
        for j in range(1,301):
            MEM[i-1,j-1] = get_power_level(i, j, GRID_SERIAL)

    results = np.zeros((300, 3))
    for kernal_size in range(1,301):
        print(f'working on {kernal_size}')
        kernal = np.ones((kernal_size, kernal_size))
        conv = convolve2d(MEM, kernal, mode='full', boundary='fill', fillvalue=0)
        ind = np.unravel_index(np.argmax(conv, axis=None), conv.shape)
        # print(conv)
        results[kernal_size-1, 0]= np.amax(conv)
        results[kernal_size-1, 1]= ind[0] - 1
        results[kernal_size-1, 2]= ind[1] - 1

    max_axix0 = np.argmax(conv, axis=0)
    print(results[max_axix0[0]])
    # result is ind = x,y return x-1, y-1

def run():
    cal_power_matrix()

run()
