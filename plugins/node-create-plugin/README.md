## Rundeck Node-Create Plugin

This a plugin to be run on an existing instance or localhost Rundeck machine to create nodes in Rundeck to be accessed later.

## Install

While I am developing this plugin my zip file will not be available but once it is complete it will be uploaded and available to download. The plugin should be put in your Rundeck instance's plugins directory which is by default located at /var/lib/rundeck/libext/.

## Requirements

I did all of my testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). I have not tested it with any 2.X versions but may do so after development is complete.

## Configuration

There are several required options and some optional options that have built in defaults.

The required attributes include:

## Testing details

As stated previously, all development and testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). The machine used was for testing was the 'centos/7' vagrant box. Initial node.yml files were placed in the directory /var/rundeck/projects/<project name>/etc/resources/.
