#8. Install and use snort for network intrusion detection.
#LINUX/UBUNTU
#sudo apt-get install snort
# chmod +x exp8.sh
# sudo ./exp8.sh

#!/bin/bash

echo "=== 1. Checking Snort Version ==="
snort -V

echo -e "\n=== 2. Validating Snort Configuration ==="
sudo snort -c /etc/snort/snort.lua -T

echo -e "\n=== 3. Executing Live Traffic Detection on Interface eth0 ==="
sudo snort -c /etc/snort/snort.lua -R local.rules -i eth0 -A alert_fast -q
