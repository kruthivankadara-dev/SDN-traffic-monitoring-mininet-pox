from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.recoco import Timer

log = core.getLogger()

class SimpleSwitch(object):

    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        Timer(5, self.request_stats, recurring=True)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        log.info("Packet received")

        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(msg)

        fm = of.ofp_flow_mod()
        fm.match = of.ofp_match.from_packet(packet)
        fm.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(fm)

    def request_stats(self):
        self.connection.send(
            of.ofp_stats_request(
                body=of.ofp_flow_stats_request()
            )
        )

    def _handle_FlowStatsReceived(self, event):
        log.info("Flow Stats from %s", dpidToStr(event.connection.dpid))
        for flow in event.stats:
            log.info("Packets: %s Bytes: %s",
                     flow.packet_count,
                     flow.byte_count)

def start_switch(event):
    log.info("Custom controller running...")
    SimpleSwitch(event.connection)

def launch():
    core.openflow.addListenerByName("ConnectionUp", start_switch)