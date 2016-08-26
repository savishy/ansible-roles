#!/bin/bash
set -e
while read p; do
    if [[ $p == \#* ]]; then
        continue
    fi
    x=$p
    splits=(${x//:/ })
    if [[ ${#splits} -gt 0 ]]; then
        plugin=${splits[0]}
        version=${splits[1]}
        echo "install $plugin v$version"
        
        wget -P $JENKINS_HOME/plugins https://updates.jenkins-ci.org/download/plugins/$plugin/$version/$plugin.hpi
    fi
done<$1
