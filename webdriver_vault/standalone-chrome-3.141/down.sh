#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"
    containers=`docker ps -qa   -f name=${STACK_NAME}_`
    #           list container  filtered by this prefix in container name
        docker stop -t1 $containers
        docker rm   -f  $containers
