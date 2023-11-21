import sys
sys.path.append('.')

from pox.core import core
from pox.openflow import libopenflow_01 as of
from pox.lib import packet as pkt # POX convention
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool
from pox.lib.addresses import IPAddr


import JsonParser

log = core.getLogger()

class LinkFirewall (object):
    def __init__(self, connection, rules):
        self.connection = connection
        connection.addListeners(self)

        def install_firewall():
            for rule in rules:
                msg = of.ofp_flow_mod()

                block_match = of.ofp_match()
                block_match.dl_type = pkt.ethernet.IP_TYPE
                block_match.nw_proto = rule['nw_proto']

                if(rule['nw_src'] != None):
                    block_match.nw_src=IPAddr(rule['nw_src'])
                
                if(rule['nw_dst']  != None):
                    block_match.nw_dst=IPAddr(rule['nw_dst'])

                if(rule['tp_src'] != None):
                    block_match.tp_src=rule['tp_src']

                if(rule['tp_dst'] != None):
                    block_match.tp_dst=rule['tp_dst']

                msg.match = block_match

                self.connection.send(msg)

        
        install_firewall()

class configurable_firewall (object):
    def __init__(self, rules):
        log.debug('initing configurable_firewall')
        core.openflow.addListeners(self)
        self.rules = rules

    def _handle_ConnectionUp (self, event):
        log.debug("Connection %s" % (event.connection,))
        LinkFirewall(event.connection, self.rules)
    
def launch():
    log.debug('Launching configurable firewall')

    jsonParser = JsonParser.JsonParser.load_json('./config.json')
    rules = jsonParser.get_rules()

    core.registerNew(configurable_firewall, rules)