# 20 Mart Sali gunu derse gelmeden once asagidaki islemleri yapmaniz gerekmektedir.

```
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key 
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
sudo -i 
apt-get update 
apt-get install mosquitto 
apt-get install mosquitto-clients
```
