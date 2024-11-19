from matplotlib import pyplot as plt
import csv
from pythondaq.models.diode_experiment import DiodeExperiment
import pythondaq.views.view_methods as vm
            

def main():
    """Main view code to run
    """
    # Compare two LEDs and display the results in a scatterplot
    experiment = DiodeExperiment("ASRL9::INSTR")

    # Ask for all measurement parameters and inform the user about their input.
    iterations = vm.clamp_input(1,50,vm.try_integer_input("Number of experiment iterations: "), "iterations")
    start = vm.clamp_input(0,1024,vm.try_integer_input("Start measurement bound: "), "start")
    stop = vm.clamp_input(0,1024,vm.try_integer_input("Stop measurement bound: "), "stop")

    # Warn the user if the stop value is smaller than the start value
    if stop < start:
        print("Warning: stop measurement bound is smaller than start measurement bound, no measurements will be done.")

    # Do the measurements
    print(input("Place LED 1, and press any key..."))
    U_1, I_1, U_1_err, I_1_err = experiment.scan(start = start, stop = stop, iterations = iterations)

    print(input("Place LED 2, and press any key..."))
    U_2, I_2, U_2_err, I_2_err = experiment.scan(start = start, stop = stop, iterations = iterations)

    # Display the results of both LEDs in the same graph
    plt.errorbar(x=U_1, y=I_1, yerr=I_1_err, xerr=U_1_err, fmt="ro", markersize=1.5, ecolor="r", elinewidth=0.75, label="LED 1", capsize=1)
    plt.errorbar(x=U_2, y=I_2, yerr=I_2_err, xerr=U_2_err, fmt="bo", markersize=1.5, ecolor="b", elinewidth=0.75, label="LED 2", capsize=1)
    plt.xlabel("U (V)")
    plt.ylabel("I (A)")
    plt.legend()

    plt.show()

    # Generate csv files
    vm.create_csv("MetingenLed1", (U_1, I_1, U_1_err, I_1_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))
    vm.create_csv("MetingenLed2", (U_2, I_2, U_2_err, I_2_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))

if __name__ == "__main__":
    main()

