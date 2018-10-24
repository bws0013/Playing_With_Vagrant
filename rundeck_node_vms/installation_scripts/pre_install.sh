#/bin/bash

yum install -y vim-enhanced

mkdir ~/.ssh
touch ~/.ssh/authorized_keys

echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmiPNwtkLuxKS1LG0is8nwpbkvVRoJjca3WqbFrrU2GtJc8kcDhiD07inFgTR7uT5tRtuR38KGY4EkaENW/W/Afgs3018Tmgw4MYCGCDGE4ZmcjYEN4IV6Ks9CgyEnxE24jtjO3lX2jbogt1mA31o9Yf2AMnAbxMRoRKJzFhkofRu8eFGCdJdGkK82lnUhKgwlAfocR4QGznscWZsP/YTIlU5jUkdiG5/SxhP7q+3bN8Lxo6+eQKa1SRH+L9AlW3rFte8b1xjqYX3LWX/wAc++qa0Zw1m5v/l+OKSfYIGt9XbpUsfz7XbhXGZlVRL5UJRYrt96gGrRjBE/S2vqDNmB' >> ~/.ssh/authorized_keys

whoami
