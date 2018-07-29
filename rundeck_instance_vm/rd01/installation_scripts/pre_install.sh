#/bin/bash

yum install install java-1.8.0 -y
yum install -y vim-enhanced

if [ ! -f /etc/rundeck/rundeck-config.properties ]; 
then
	echo "-------- PROVISIONING RUNDECK -----------"
	echo "-----------------------------------------"
	rpm -Uvh http://repo.rundeck.org/latest.rpm
	yum install rundeck -y --nogpgcheck
else
	echo "CHECK - Rundeck already installed"
fi

whoami


