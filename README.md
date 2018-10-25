The purpose of this project is to have an appropriate setup for testing various aspects of Rundeck. These include plugin and job development.

The rundeck_instance_vm folder contains a vagrant file for spinning up an instance of the latest version of rundeck

The rundeck_node_vms folder contains at least one vagrant file for spinning up what can be a node of the main instance

The public key from /var/lib/rundeck/.ssh/idrsa.pub needs to be added from the main instance to the node in order for the instance to command the node.

Any other directories than these will primarily focus on whatever aspect of Rundeck I am developing on. Currently that is a plugin to create nodes.
