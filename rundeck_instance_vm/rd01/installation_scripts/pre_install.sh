#/bin/bash

yum install -y epel-release vim-enhanced java-1.8.0 nginx

# determine if we also need to install bind-utils 

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
