import os
import sys
import subprocess

HOSTS_AMOUNT = 4
ARGUMENTS_AMOUNT = 2
SWITCHES_AMOUT_PATH = "amount_switches.txt"

def run(*popenargs, **kwargs):
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:
        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr

def append_logs(log, path):
    try:
        with open(path, "r") as f:
            old_content = f.read()
            with open(path, "w") as f:
                f.write(log)
                f.write("\n")
                f.write(old_content)
    except IOError:
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
            mn_command = ["sudo", "mn", "--custom", "mininet/topology.py", "--topo", "project", "--controller", "remote"]
            run(mn_command)
        else:
            print("Error: el primer parametro (cantidad de switches) tiene que estar entre 1 y 10.")
    else:
        print("Error: Todos los inputs deben ser numeros enteros positivos.")
