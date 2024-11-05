from matplotlib import pyplot as plt
from diode_experiment import DiodeExperiment

experiment = DiodeExperiment("ASRL9::INSTR")
U, I = experiment.scan(0,1024)

plt.plot(U, I, "o", markersize=1)
plt.xlabel("U (V)")
plt.ylabel("I (A)")

plt.show()