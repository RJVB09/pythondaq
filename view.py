from matplotlib import pyplot as plt
from diode_experiment import DiodeExperiment

# Compare two LEDs and display the results in a scatterplot
experiment = DiodeExperiment("ASRL9::INSTR")

iterations = int(input("Number of experiment iterations: "))
start = int(input("Start measurement bound: "))
stop = int(input("Stop measurement bound: "))

print(input("Place LED 1, and press any key..."))
U_1, I_1, U_1_err, I_1_err = experiment.scan(start = start, stop = stop, iterations = iterations)

print(input("Place LED 2, and press any key..."))
U_2, I_2, U_2_err, I_2_err = experiment.scan(start = start, stop = stop, iterations = iterations)


plt.errorbar(x=U_1, y=I_1, yerr=I_1_err, xerr=U_1_err, fmt="ro", markersize=1.5, ecolor="r", elinewidth=0.75, label="LED 1")
plt.errorbar(x=U_2, y=I_2, yerr=I_2_err, xerr=U_2_err, fmt="bo", markersize=1.5, ecolor="b", elinewidth=0.75, label="LED 2")
plt.xlabel("U (V)")
plt.ylabel("I (A)")
plt.legend()

plt.show()