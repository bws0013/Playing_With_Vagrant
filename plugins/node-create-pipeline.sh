#!/bin/bash
zip -r node-create-plugin.zip node-create-plugin/

keypath='/Users/bensmith/Documents/Rundeck_Stuff/rundeck_instance_vm/rd01/.vagrant/machines/default/virtualbox/private_key'

vagrant scp node-create-plugin.zip 3e10c49:/tmp

cd /Users/bensmith/Documents/Rundeck_Stuff/rundeck_instance_vm/rd01
vagrant ssh default -c "sudo mv /tmp/node-create-plugin.zip /var/lib/rundeck/libext/"
