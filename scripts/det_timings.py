import time
import numpy as np
from mpm_la import gauss, det
import os

path_base = os.path.abspath(os.path.join(os.getcwd(), ".."))

timing_gauss = []
timing_numpy = []
timing_my = []
size_m = []
for i in range(1, 11):
    matrix_size = i * 20
    tmp_matrix = np.random.randint(0, 10, (matrix_size, matrix_size)).tolist()
    start_time = time.time()
    det0, x = gauss(tmp_matrix, tmp_matrix)
    end_time = time.time()
    start_time1 = time.time()
    det1 = np.linalg.det(tmp_matrix)
    end_time1 = time.time()
    tmp_mat = np.array(tmp_matrix)
    start_time2 = time.time()
    det2 = det.det(tmp_mat)
    end_time2 = time.time()
    end_start = end_time - start_time
    end_start1 = end_time1 - start_time1
    end_start2 = end_time2 - start_time2
    timing_gauss.append(end_start)
    timing_numpy.append(end_start1)
    timing_my.append(end_start2)
    size_m.append(matrix_size)

# print(size_m)
# print(timing_gauss)
# print(timing_numpy)
# print(timing_my)

filename = os.path.join(path_base, "results/timings.txt")
with open(filename, "a") as textfile:
    for i in range(10):
        textfile.write(str(size_m[i]) + "       " +
                       str(timing_gauss[i]) + "        " +
                       str(timing_numpy[i]) + "         " +
                       str(timing_my[i]) + "\n")
    textfile.close()
