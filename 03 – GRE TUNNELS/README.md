# GRE Tunnels – IPv4 / IPv6

## Objectif
Configurer des tunnels GRE (Generic Routing Encapsulation) pour transporter du trafic IPv4 et IPv6 à travers un réseau sous-jacent (underlay).

## Technologies
- GRE (Generic Routing Encapsulation)
- OSPF over tunnel
- Routage statique
- IPv4 / IPv6

## Topologie
![Topologie](captures/topologie.png)

## Configuration

### Tunnel IPv4 (R1 ↔ R3)

interface Tunnel0
ip address 100.100.100.1 255.255.255.252
tunnel source Loopback0
tunnel destination 192.168.3.1

### Tunnel IPv6 (R1 ↔ R3)

interface Tunnel1
ipv6 address 2001:db8:ffff::1/64
tunnel source Loopback0
tunnel destination 2001:db8:acad:3::1
tunnel mode gre ipv6

### OSPF dans le tunnel

router ospf 4
network 100.100.100.0 0.0.0.3 area 0

## Vérifications

### Tunnel IPv4 up

R1# show interfaces tunnel 0
Tunnel0 is up, line protocol is up

### Tunnel IPv6 up

R1# show interfaces tunnel 1
Tunnel1 is up, line protocol is up


### Ping entre extrémités

R1# ping 100.100.100.2
!!!!!
R1# ping 2001:db8:ffff::2
!!!!!

### OSPF via tunnel

R1# show ip ospf neighbor
Neighbor ID     Pri   State      Dead Time   Address
3.3.3.3         1     FULL/DR    00:00:34    100.100.100.2

### Démonstration routage récursif

R3(config)# router ospf 4
R3(config-router)# network 192.168.1.0 0.0.0.255 area 0
%TUN-5-RECURDOWN: Tunnel0 temporarily disabled due to recursive routing

## Résultat
- ✅ Tunnels GRE IPv4 et IPv6 opérationnels
- ✅ OSPF à travers le tunnel
- ✅ Compréhension du routage récursif
- ✅ Connectivité inter-sites

## Fichiers de configuration
- [R1.txt](configs/R1.txt)
- [R2.txt](configs/R2.txt)
- [R3.txt](configs/R3.txt)
