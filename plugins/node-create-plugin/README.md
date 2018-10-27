## Rundeck Node-Create Plugin

This a plugin to be run on an existing instance or localhost Rundeck machine to create nodes in Rundeck to be accessed later.

## Install

While I am developing this plugin my zip file will not be available but once it is complete it will be uploaded and available to download. The plugin should be put in your Rundeck instance's plugins directory which is by default located at `/var/lib/rundeck/libext/`.

## Requirements

I did all of my testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). I have not tested it with any 2.X versions but may do so after development is complete.

There should not be any other dependencies apart from Rundeck.

It is important to note that this plugin will create, open and edit files. There may be some behaviors that occur from this that are unexpected so it would be best if when a job is called no other jobs are currently running that might use the node being created. That being said, maybe it will all be fine.

## Configuration

There are several required options and some optional options that have built in defaults.

There are a number of attributes that will be used in the creation of the node. It is important that none of these be left blank as this could cause issues with how the node is read.

The attributes include
  * **Node Name:** The name of your node as it appears in Rundeck. If you are making an individual node file then this the file name will be in the format `node_name.yml`.  
  * **Hostname:** The address used by Rundeck to login to this particular node. It can be either an ip address or a hostname.
  * **Login Username:** This shall be the username you intend to use to login to the node with. The format that rundeck will use to access a node is similar to `ssh <username>@<hostname/ip>`. This username should exist on the device, usually set to root or rundeck (if you make a rundeck user on the target node).
  * **File Path\*:** This will be assumed by the plugin as the default location of the node file or directory. You should change this if the default location is incorrect. By default it is `/var/rundeck/projects/<project name>/etc/resources(.yml)`. There will be a little more explanation of this later.
  * **Node Description:** (Optional) This can be whatever you would like but should not be blank. The plugin may add a basic description if none is included.
  * **Tags:** (Optional) This should be a comma separated list containing no spaces in between tags. The plugin may add a basic tag if none is included. Example input: `first,test,rundeck1`
  * **Overwrite:** If an existing node has the same Node Name as you have just entered should the existing node be overwritten with the new information?

\***Note on File Path**: I have encountered two common configurations when it comes to Rundeck Node setups. The most common is to have a single `resources.yml` file containing information on all nodes. The other is to have a folder called resources which contains a series of `<node name>.yml` files. My program checks to see if the File Path is to a file or a directory and acts accordingly. There is a less common configuration where you have both a `resources.yml` file as well as a resources folder. If you are using this just enter either the file or folder and the program will act accordingly. If you choose to name your `resources.yml` file something else that is fine just add its name instead of the default.



## Testing details

As stated previously, all development and testing for this plugin occurred in Rundeck version 3.0.7-20181008 (jalapeño popper deepskyblue flag). The machine used was for testing was the 'centos/7' vagrant box. Initial node.yml files were placed in the directory `/var/rundeck/projects/<project name>/etc/resources/`.
