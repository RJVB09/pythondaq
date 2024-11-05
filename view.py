from matplotlib import pyplot as plt
from diode_experiment import DiodeExperiment

experiment = DiodeExperiment("ASRL9::INSTR")
U, I, U_err, I_err = experiment.scan(start = 0, stop = 1024, iterations = 50)

plt.plot(U, I, "o", markersize=1)
plt.xlabel("U (V)")
plt.ylabel("I (A)")

plt.show()