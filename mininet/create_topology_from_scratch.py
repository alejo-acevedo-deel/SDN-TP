import os
import sys
import subprocess

HOSTS_AMOUNT = 2
ARGUMENTS_AMOUNT = 2
SWITCHES_AMOUT_PATH = "amount_switches.txt"

def append_logs(log, path):
    try:
        with open(path, "r") as f:
            old_content = f.read()
            with open(path, "w") as f:
                f.write(log)
                f.write("\n")
                f.write(old_content)
    except FileNotFoundError:
        with open(path, "w") as f:
            f.write(log)

def create_logs(switches_amount):
    print("El numero de switches sera: {0}".format(switches_amount))
    print("El numero de hosts sera: {0}".format(HOSTS_AMOUNT))
    append_logs(str(switches_amount), SWITCHES_AMOUT_PATH)

if len(sys.argv) != ARGUMENTS_AMOUNT:
    print("Por favor ingresa como primer parametro la cantidad de switches (entre 1 y 10).")
    switches_parameter = input("Ingrese la cantidad de switches: ")
else:
    switches_parameter = sys.argv[1]

    if switches_parameter.isdigit():
        switches_amount = int(switches_parameter)
            if switches_amount >= 1 and switches_amount <= 10:
                create_logs(switches_amount)
                mn_command = ["sudo", "mn", "--custom", "topology.py", "--topo", "project"]
                subprocess.run(mn_command)
            else:
                print("Error: el primer parametro (cantidad de switches) tiene que estar entre 1 y 10.")
    else:
        print("Error: Todos los inputs deben ser numeros enteros positivos.")
