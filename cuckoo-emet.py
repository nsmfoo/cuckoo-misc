import logging
import wmi
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from lib.common.abstracts import Auxiliary
from lib.common.results import NetlogFile

log = logging.getLogger(__name__)
dadada = []

class EMET(Auxiliary):

    def start(self):
        log.info("Starting EMET auxilary module")

    def stop(self):
        log.info("Collecting EMET events...")

        c = wmi.WMI(privileges=['Security'])
        for event in c._raw_query('SELECT * FROM Win32_NTLogEvent'):
            if event.SourceName == "EMET":
               #https://msdn.microsoft.com/en-us/library/aa394226(v=vs.85).aspx maybe add more values?
          dadada.append([event.SourceName, event.Category, event.Type, event.ComputerName, event.User, event.Message])

        bleekscheet = "\n".join(str(x) for x in dadada)
        nf = NetlogFile()
        nf.init("logs/emet_events.log")
        nf.send(bleekscheet)
        nf.close()
        return True