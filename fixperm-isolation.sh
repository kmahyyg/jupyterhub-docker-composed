#!/bin/bash
#
# Cron: */2 * * * * bash /root/jobs/fixperm-isolation.sh
#
# this script should be root:root and 0755.
#
chown -R 1000:1000 /userdata/isolation
