ssh bağlantısı yapabilmek için Raspberry Pi'yi hdmi bağlantısı ile bir ekrana bağlamanız ve komut yazabilmeniz için usb klavye kullanmanız gerekmektedir. Klavye ve mouse'u bağladıktan sonra raspberry pi'ye güç vererek aşağıdaki işlemleri gerçekleştirebilirsiniz.
# Klavye Duzeni
Raspberry Pi'yi ekrana bagladiginizda dikkat edeceginiz ilk sey klavyeni UK klavye olacagi. 
sudo raspi-config
komutunu girerek Localisation Options'u secin sonrasinda Change Keyboard Layout bolumuna gidin. Karsiniza cikan ekranda (Generic 105-key)
secenegine gelip enterlayin. sonrasinda other'dan Turkish'i bulun ve tikladiktan sonra tekrar Turkish'i secin. Default Keybord
Layout deginizde klavyeniz artik Turkce'dir.

# Wifi Ag Ayarlari
Bu işlem raspberry'yi kendi wifi'nize bağlamanızı sağlar.
Terminale 
```sudo nano /etc/network/interfaces```
yazin ve dosyayi asagidaki gibi degistirin.
```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
auto wlan0
iface wlan0 inet dhcp
        wpa-ssid WIFI ADINIZ
        wpa-psk WIFI SIFRENIZ
#       address 192.168.4.X
#       gateway 192.168.4.1
#       mask 255.255.255.0
```
`sudo reboot` sistem restart olacak dediginizde Wifi'ye baglanmis olacaksiniz :)

# PuTTY ile SSH Baglantisi Yapmak
Raspberry tekrar acildiginda
```ifconfig```
komutunu terminale girin. Eger wireless kullaniyorsaniz wlan0, ethernet kullaniyorsaniz eth0 ile baslayan satirin altinda `inet 192.168.1.x` benzerinde bir satir goreceksiniz. bu adrese PuTTY uzerinden daha once gosterdigim sekilde baglanabilirsiniz.
##Vaktiniz olursa guncelleme yapin
Raspberryleri guncelleyecek internetimiz ve vaktimiz olmadigindan eger guncellemek isterseniz asagidaki satirlari girin. Bu islem biraz zaman alabilir.
`sudo apt-get update`
`sudo apt-get upgrade`
# ONEMLI!!! KURSA GELMEDEN ONCE MUHAKKAK AYARLARI GERI ALIN
Kursa gelmeden once daha once degistirdigimiz interfaces dosyasini eski halina asagidaki gibi geri getirmelisiniz. Aksi takdirde EMO'nun wifi adresine bağlanmayacaktır.
```sudo nano /etc/network/interfaces```
```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
auto wlan0
iface wlan0 inet static
       wpa-ssid EMO1
       wpa-psk EMOtmmob1954
       address 192.168.4.X
       gateway 192.168.4.1
       mask 255.255.255.0
```
X size verilen static IP numarasi.
TESEKKURLER!
