#!/usr/bin/env python

import sys
import os.path
import time

def checkit():
    print "in checkit"
    enabled = True
    running = False
    lastrun_failed = False
    lastrun = 0
    failcount_resources = 0
    failcount_events = 0
    warn = 0
    crit = 0
    total_failure = False
    enabled_only = False
    failures = False
    disable_perfdata = False
    warn = 1800
    crit = 3600
#    agent_lockfile = "/var/lib/puppet/state/agent_catalog_run.lock"
#    agent_disabled_lockfile = "/var/lib/puppet/state/agent_disabled.lock"
#    statefile = "/var/lib/puppet/state/state.yaml"
#    summaryfile = "/var/lib/puppet/state/last_run_summary.yaml"
    agent_lockfile = "./logfiles/agent_catalog_run.lock"
    agent_disabled_lockfile = "./logfiles/agent_disabled.lock"
    statefile = "./logfiles/state.yaml"
    summaryfile = "./logfiles/last_run_summary.yaml"

    
    if warn == 0 or crit == 0:
        print "Please specify a warning and critical level"
        sys.exit(3)
    
    if os.path.isfile(agent_lockfile):
           enabled = False
    else:
           running = True

    if os.path.isfile(agent_disabled_lockfile): 
        enabled = False

    if os.path.isfile(statefile):
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(statefile)
        lastrun=mtime
        print lastrun

        try:
            with open(summaryfile,"r") as fp:
                for line in fp:
                    if 'last_run:' in line:
                        print line,
        except:
            print "nada"
            sys.exit(100)
    sys.exit()
    
'''            # it wont have anything but last_run in it
            unless summary.include?("events")
                failcount_resources = 99
                failcount_events = 99
                total_failure = True
            else:
                # and unless there are failures, the events hash just wont have the failure count
                failcount_resources = summary["resources"]["failed"] or 0
                failcount_events = summary["events"]["failure"] or 0
        except:
            failcount_resources = 0
            failcount_events = 0
            summary = nil
    time_since_last_run = Time.now.to_i - lastrun
    
    time_since_last_run_string = "#{time_since_last_run} seconds ago"
    if time_since_last_run >= 3600:
      time_since_last_run_string = "#{time_since_last_run / 60 / 60} hours ago at #{Time.at(Time.now - time_since_last_run).utc.strftime('%R:%S')} UTC"
    elsif time_since_last_run >= 60
      time_since_last_run_string = "#{time_since_last_run / 60} minutes ago"
    
    if disable_perfdata:
      perfdata_time = ""
    else:
      perfdata_time = "|time_since_last_run=#{time_since_last_run}s;#{warn};#{crit};0 failed_resources=#{failcount_resources};;;0 failed_events=#{failcount_events};;;0"
    
    unless failures
        if enabled_only && enabled == False:
            print "OK: Puppet is currently disabled, not alerting. Last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events#{perfdata_time}"
            exit 0
    
        if total_failure:
            print "CRITICAL: FAILED - Puppet failed to run. Missing depencies? Catalog compilation failed? Last run #{time_since_last_run_string}#{perfdata_time}"
            exit 2
        elsif time_since_last_run >= crit
            print "CRITICAL: last run #{time_since_last_run_string}, expected < #{crit}s#{perfdata_time}"
            exit 2
    
        elsif time_since_last_run >= warn
            print "WARNING: last run #{time_since_last_run_string}, expected < #{warn}s#{perfdata_time}"
            exit 1
    
        else:
            if enabled:
                print "OK: last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events and currently enabled#{perfdata_time}"
            else:
                print "WARNING: last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events and currently disabled#{perfdata_time}"
                exit 1
    
            exit 0
    else:
        if enabled_only && enabled == False:
            print "OK: Puppet is currently disabled, not alerting. Last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events#{perfdata_time}"
            exit 0
    
        if total_failure:
            exit 2
        elsif failcount_resources >= crit
            print "CRITICAL: Puppet last ran had #{failcount_resources} failed resources #{failcount_events} failed events, expected < #{crit}#{perfdata_time}"
            exit 2
    
        elsif failcount_resources >= warn
            print "WARNING: Puppet last ran had #{failcount_resources} failed resources #{failcount_events} failed events, expected < #{warn}#{perfdata_time}"
            exit 1
    
        else:
            if enabled:
                print "OK: last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events and currently enabled#{perfdata_time}"
            else:
                print "WARNING: last run #{time_since_last_run_string} with #{failcount_resources} failed resources #{failcount_events} failed events and currently disabled#{perfdata_time}"
                exit 1
    
            exit 0
    '''


if __name__ == '__main__':
    print"starting"
    checkit()
