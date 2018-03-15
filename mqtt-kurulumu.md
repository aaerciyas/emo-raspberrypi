# 20 Mart Sali gunu derse gelmeden once asagidaki islemleri yapmaniz gerekmektedir.
## Mosquitto Kurulumu
```
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key 
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-stretch.list
sudo -i 
apt-get update 
apt-get install mosquitto 
apt-get install mosquitto-clients
```
## Paho Mqtt kurulumu
root kullanicisindan cikmak icin ctrl+D tusuna basin boylelikle pi@raspberrypi kabuguna gecmis olursunuz
`cd` 
yazarak ana dizine gelin
`pwd` yazdiginizda dizin asagidaki gibi gozukmelidir.
`/home/pi`
pip dosyasini yeni bir klasor olusturarak onun icine indirelim.
```
mkdir pip
cd pip
wget https://bootstrap.pypa.io/get-pip.py
```
pip bir package manager'dir. Yani yazilim paketlerini yonetmemizi (yuklememizi ve silmemizi saglar)
pip'i indirdikten sonra kurmak icin:
`sudo python get-pip.py`
Eger bir hata almadiysaniz pip basarili bir sekilde yuklenmistir.
Simdi python programlarinda mqtt protokolunu kullanmamizi saglayacak olan paho-mqtt programini yukleyelim.
`sudo pip install paho-mqtt`
Kurulumun gerceklesip gerceklesmedigini anlamak icin python kabuguna gecerek paho kutuphanesini import edelim.
```
python
import paho
```
Eger bir hata almadiysaniz paho basarili bir sekilde yuklenmistir.
