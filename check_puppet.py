#!/usr/bin/env python

import time
import yaml
import os.path
import logging
import datetime
import logging.handlers
from socket import gethostname


disabledfile = "/home/shumphries/monitor-puppet/logfiles/agent_disabled.lock"
lrsummary = "/home/shumphries/monitor-puppet/logfiles/last_run_summary.yaml"
statefile = "/home/shumphries/monitor-puppet/logfiles/state.yaml"
lrreport = "/home/shumphries/monitor-puppet/logfiles/last_run_report.yaml"

#    agentLockfile = "/var/lib/puppet/state/agent_catalog_run.lock"
#    disablefile = "/var/lib/puppet/state/agent_disabled.lock"
#    statefile = "/var/lib/puppet/state/state.yaml"
#    llreport = "/var/lib/puppet/state/last_run_report.yaml"


my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log')
my_logger.addHandler(handler)


def construct_ruby_object(loader, suffix, node):
    return loader.construct_yaml_map(node)


def construct_ruby_sym(loader, node):
    return loader.construct_yaml_str(node)


yaml.add_multi_constructor(u"!ruby/object:", construct_ruby_object)
yaml.add_constructor(u"!ruby/sym", construct_ruby_sym)


def check_last_time_run():
    # disabledfile = "/var/lib/puppet/state/agent_disabled.lock"
    # lrsummary    = "/var/lib/puppet/state/last_run_summary.yaml"
    # statefile    = "/var/lib/puppet/state/state.yaml"
    if os.path.isfile(lrsummary):
        with open(lrsummary, "r") as fp:
            data = yaml.load(fp)
        timeran = data["time"]["last_run"]
        timediff = time.time() - timeran
        if timediff > 3601:
            timediff2 = str(datetime.timedelta(seconds=timediff))
            msg = gethostname() + ": Puppet not run for" + timediff2
            print msg
#           my_logger.critical(msg)


def check_if_disabled():
    if os.path.isfile(disabledfile):
        with open(disabledfile, 'r') as dis:
            data = yaml.load(dis)
        msg = gethostname()+": Puppet disabled,: "+data["disabled_message"]
        print msg
#        my_logger.critical(msg)


def check_if_failures():
    print "in check failures"
    if os.path.isfile(lrreport):
        print "found file", lrreport
        with open(lrreport, 'r') as lrr:
            data = yaml.load(lrr)
        for key in data:
            print key
        # if data["resource_statuses"]["events"]["status"] == "failure":
        # print data["resource_statuses"]["events"]["message"]

if __name__ == '__main__':
    check_if_failures()
''' check_last_time_run()
    check_if_disabled()
'''
