# Routage statique IPv4/IPv6

## Objectif
Configurer et analyser différents types de routes statiques (directement attachées, récursives, fully specified, flottantes, null) en IPv4 et IPv6.

## Technologies
- Routage statique IPv4
- Routage statique IPv6
- Distance administrative
- CEF

## Topologie
![Topologie](captures/topologie.png)

## Configuration

### Routes IPv4

#### Directement attachée

ip route 192.168.2.0 255.255.255.224 f0/0

#### Récursive

ip route 10.2.3.0 255.255.255.0 10.1.2.2

#### Fully specified

ip route 10.2.3.0 255.255.255.0 f0/0 10.1.2.2

#### Floating (backup)

ip route 192.168.3.0 255.255.255.224 s3/0 10.1.3.3
ip route 192.168.3.0 255.255.255.224 s3/1 10.1.3.130 7


#### Null route

ip route 209.165.200.0 255.255.255.0 null0


### Routes IPv6

#### Récursive

ipv6 route 2001:db8:acad:1012::/64 2001:db8:acad:1023::2


#### Fully specified avec lien local

ipv6 route 2001:db8:acad:1012::/64 f0/0 fe80::2:2

#### Floating

ipv6 route 2001:db8:acad:1000::/64 s3/0 2001:db8:acad:1013::1
ipv6 route 2001:db8:acad:1000::/64 s3/1 2001:db8:acad:1014::1 17

#### Null route

ipv6 route 3333::/64 null0

## Vérifications

### Routes IPv4

R1# show ip route static
S    10.2.3.0/24 [1/0] via 10.1.2.2, FastEthernet0/0
S    192.168.2.0/27 is directly connected, FastEthernet0/0
S    192.168.3.0/27 [1/0] via 10.1.3.3, Serial3/0
S    209.165.200.0/24 is directly connected, Null0

### Routes IPv6

R3# show ipv6 route static
S    2001:DB8:ACAD:1012::/64 [1/0] via FE80::2:2, FastEthernet0/0
S    2001:DB8:ACAD:1000::/64 [1/0] via 2001:DB8:ACAD:1013::1, Serial3/0
S    3333::/64 [1/0] via Null0, directly connected

### Basculement floating route

R1# traceroute 192.168.3.1 source loopback0    → via 10.1.3.3
R1(config)# interface s3/0
R1(config-if)# shutdown
R1# traceroute 192.168.3.1 source loopback0    → via 10.1.3.130

## Résultat
- ✅ Routes statiques IPv4/IPv6 opérationnelles
- ✅ Basculement automatique (floating)
- ✅ Routes null pour le filtrage
- ✅ CEF actif

## Fichiers de configuration
- [R1.txt](configs/R1.txt)
- [R2.txt](configs/R2.txt)
- [R3.txt](configs/R3.txt)
