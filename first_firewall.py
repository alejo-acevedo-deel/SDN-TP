from pox.core import core
from pox.openflow import libopenflow_01 as of
from pox.lib import packet as pkt # POX convention
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool

log = core.getLogger()

class LinkFirewall (object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        def install_firewall():
            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match(dl_type = pkt.ethernet.IP_TYPE, nw_proto = pkt.ipv4.TCP_PROTOCOL, tp_dst = 80)
            self.connection.send(msg)
            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match(dl_type = pkt.ethernet.IP_TYPE, nw_proto = pkt.ipv4.UDP_PROTOCOL, tp_dst = 80)
            self.connection.send(msg)
        
        install_firewall()

    def _handle_PacketIn (self, event):
        packet = event.parsed
        log.debug("Packet-in resend %s -> %s" %
                  (packet.src, packet.dst))

class first_firewall (object):
    def __init__(self):
        log.debug('initing first_firewall')
        core.openflow.addListeners(self)

    def _handle_ConnectionUp (self, event):
        log.debug("Connection %s" % (event.connection,))
        LinkFirewall(event.connection)
    
def launch():
    log.debug('Launching first_firewall')

    core.registerNew(first_firewall)
