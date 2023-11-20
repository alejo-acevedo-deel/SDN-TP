from mininet.topo import Topo
from mininet.link import TCLink
import sys

HOSTS_AMOUNT = 2
SWITCHES_AMOUNT_PATH = "amount_switches.txt"

def get_first_value_from_file(path):
    try:
        with open(path, "r") as f:
            return int(f.readline())
    except FileNotFoundError:
        print("Error: El archivo ha sido eliminado durante la ejecución. Vuelva a intentar.")

class Project(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        num_switches = get_first_value_from_file(SWITCHES_AMOUNT_PATH)

        # Add hosts
        print("Adding hosts..")
        hosts_list = []
        for i in range(1, HOSTS_AMOUNT + 1):
            hosts_list.append(self.addHost("h{0}".format(i), ip="10.0.0.{0}".format(i)))
            print("Creating host h{0}..".format(i) + " with ip address 10.0.0.{0}".format(i))

        # Add switches
        print("Adding switches..")
        switches_list = []
        for i in range(1, num_switches + 1):
            switches_list.append(self.addSwitch("s{0}".format(i)))
            print("Creating switch s{0}..".format(i))

        # Add links from hosts to switches - First host to first switch & last/second host to last switch.
        print("Adding link between the first host and the second switch...")
        self.addLink(hosts_list[0], switches_list[0])
        print("Adding link between the last host and the last switch...")
        self.addLink(hosts_list[-1], switches_list[-1])
        
        print("Adding links between switches..")
        for i in range(1, num_switches)
            print("Adding link {0}..".format(i))
            self.addLink(switches_list[i], switches_list[i+1], cls=TCLink, loss=0)

topos = {'project': (lambda: Project())}
