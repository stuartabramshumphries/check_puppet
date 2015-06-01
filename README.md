python script to check when puppet last ran on a node, if disabled and why, any any resources that failed.

for the yaml checker (added this for hiera checks) need yaml module:
sudo pip install PyYaml

./check_yaml.py ../puppet/hiera/global.yaml 
../puppet/hiera/global.yaml: Syntax OK
