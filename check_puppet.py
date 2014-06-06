#!/usr/bin/env python

import sys
import time
import yaml
import os.path
import logging
import datetime
import logging.handlers
from socket import gethostname


def check_ok():
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)
    handler = logging.handlers.SysLogHandler(address='/dev/log')
    my_logger.addHandler(handler)
    disabledfile = "/home/shumphries/monitor-puppet/logfiles/agent_disabled.lock"
    lrsummary = "/home/shumphries/monitor-puppet/logfiles/last_run_summary.yaml"
    statefile = "/home/shumphries/monitor-puppet/logfiles/state.yaml"

    if os.path.isfile(disabledfile):
        with open(disabledfile,'r') as dis:
            data = yaml.load(dis)
        msg = gethostname() + "Puppet disabled: " + data["disabled_message"]
        my_logger.critical(msg)

    if os.path.isfile(statefile):
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(statefile)
        lastrun = mtime

        with open(lrsummary, "r") as fp:
            for line in fp:
                if 'last_run:' in line:
                    line2 = line.strip()
                    l1, l2 = line2.split(":", 1)
                    l3 = int(l2)
                    linef = int(l3)
                    timediff = time.time() - linef
                    if timediff > 3601:
                        timediff2 = str(datetime.timedelta(seconds=timediff))
                        msg = "Puppet not run on " + gethostname() + " for " + timediff2
                        my_logger.critical(msg)

    sys.exit()


if __name__ == '__main__':
    check_ok()
