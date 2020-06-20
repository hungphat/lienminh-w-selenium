#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"
    docker-compose  -f "$SH/docker-compose.yml"  -p $STACK_NAME             up  -d               --scale chrome=1      --force-recreate --remove-orphans
    #               docker-compose file path      prefix for container name  .   run as daemon   TODO best scaled at?  TODO when do we need these?
