#!/bin/bash

for p in $(ps ax | grep deny.sh | grep -v grep| awk '{$1=$1}1' | cut -f 1 -d ' ')
do
        kill $p 1>/dev/null
done

for k in $(ps ax | grep fswatch | grep -v grep | awk '{$1=$1}1' | cut -f 1 -d ' ')
do
        kill $k 1>/dev/null
done
