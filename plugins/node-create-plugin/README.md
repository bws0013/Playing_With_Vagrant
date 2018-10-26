## Rundeck Node-Create Plugin

This a plugin to be run on an existing instance or localhost Rundeck machine to create nodes in Rundeck to be accessed later.

## Install

While I am developing this plugin my zip file will not be available but once it is complete it will be uploaded and available to download. The plugin should be put in your Rundeck instance's plugins directory which is by default located at /var/lib/rundeck/libext/.

## Requirements

I did all of my testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). I have not tested it with any 2.X versions but may do so after development is complete.

There should not be any other dependencies apart from Rundeck.

It is important to note that this plugin will create, open and edit files. There may be some behaviors that occur from this that are unexpected so it would be best if when a job is called no other jobs are currently running that might use the node being created. That being said, maybe it will all be fine.

## Configuration

There are several required options and some optional options that have built in defaults.

There are a number of attributes that will be used in the creation of the node. It is important that none of these be left blank as this could cause issues with how the node is read.

The attributes include
  * **Node Name:** This will be the name of your node as it appears in Rundeck. If you are making an individual node file then this the file name will be in the format `node_name.yml`. The name of the attribute in the plugin is called `node_name`.  
  * **Hostname:**
  * **Login Username:**
  * **Project Name:**
  * **Node Description:**
  * **Tags:**
  * **File Path:**
  * **Overwrite:**





## Testing details

As stated previously, all development and testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). The machine used was for testing was the 'centos/7' vagrant box. Initial node.yml files were placed in the directory /var/rundeck/projects/<project name>/etc/resources/.
