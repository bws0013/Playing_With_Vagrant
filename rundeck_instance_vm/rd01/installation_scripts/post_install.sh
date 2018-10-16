#/bin/bash

echo "----- REPLACING RUNDECK PROPERTIES ------"
echo "-----------------------------------------"

if [ -f /tmp/rundeck-config.properties ];
then
	cd /tmp
	chmod 755 rundeck-config.properties
	chown -R rundeck:rundeck rundeck-config.properties
	rm -f /etc/rundeck/rundeck-config.properties
	mv rundeck-config.properties /etc/rundeck/

else
	echo "No need to change the rundeck-config.properties"
fi

echo "---------- STARTING RUNDECK -------------"
echo "-----------------------------------------"
service rundeckd start

systemctl disable firewalld
systemctl stop firewalld
