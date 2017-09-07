# coding=utf-8
from __future__ import print_function
import h5py
from matplotlib import pyplot


def load_matlab_data(
        mat_file="../simulink_model/from_ext_ctrl_3_optimisations.mat"):
    f = h5py.File(mat_file)
    matlab_data = f["ans"]
    time = []
    h1 = []
    h2 = []
    h3 = []
    ctrl = []
    for i in range(len(matlab_data)):
        row = matlab_data[i]
        time.append(row[0])
        h1.append(row[1])
        h2.append(row[2])
        h3.append(row[3])
        ctrl.append(row[4])
        if len(ctrl) > 2:
            last_index = len(ctrl) - 1
            if ctrl[last_index] not in (0.0, 100.0) and abs(ctrl[last_index] -
                    ctrl[last_index - 1]) >= 10:
                print("Got a new optimisation end at %f" % time[last_index - 1])
                calculate_error(h1[last_index - 1], h2[last_index - 1],
                                h3[last_index - 1])
    return time, h1, h2, h3, ctrl


def calculate_error(h1_val, h2_val, h3_val):
    h1_final = round(h1_val, 0)
    h2_final = round(h2_val, 0)
    h3_final = round(h3_val, 0)
    print("Final point of optimisation: %f, %f, %f" % (h1_final, h2_final,
                                                       h3_final))
    error = 0
    error += pow(h1_final - h1_val, 2)
    error += pow(h2_final - h2_val, 2)
    error += pow(h3_final - h3_val, 2)
    print("Verification error: %f" % error)


def plot_things(time, h1, h2, h3, control):
    pyplot.close(3)
    pyplot.figure(4)
    pyplot.subplot(4, 1, 1)
    pyplot.plot(time, h1)
    pyplot.grid(True)
    pyplot.ylabel('Poziom 1')
    pyplot.title(u'Dane z aplikacji sterowania bezpośredniego')

    pyplot.subplot(4, 1, 2)
    pyplot.plot(time, h2)
    pyplot.grid(True)
    pyplot.ylabel('Poziom 2')

    pyplot.subplot(4, 1, 3)
    pyplot.plot(time, h3)
    pyplot.grid(True)
    pyplot.ylabel('Poziom 3')

    pyplot.subplot(4, 1, 4)
    pyplot.plot(time, control)
    pyplot.grid(True)
    pyplot.ylabel("Sterowanie")
    pyplot.xlabel('Czas [s]')
    pyplot.show()


def main():
    time, h1, h2, h3, ctrl = load_matlab_data()
    plot_things(time, h1, h2, h3, ctrl)


if __name__ == '__main__':
    main()
