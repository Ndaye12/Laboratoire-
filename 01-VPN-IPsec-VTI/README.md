# VPN IPsec VTI site‑à‑site
## Objectif
Créer un tunnel VPN chiffré entre deux sites avec OSPF dynamique à travers le tunnel.

## Technologies utilisées
- IPsec VTI
- OSPF
- GRE
- ACL
- SSH

## Topologie
(Image à ajouter plus tard)

## Configuration

### Phase 1 – ISAKMP

crypto isakmp policy 10
encryption aes 256
hash sha256
authentication pre-share
group 14
lifetime 3600
crypto isakmp key cisco123 address 64.100.1.2

### Phase 2 – IPsec

crypto ipsec transform-set VTI-VPN esp-aes 256 esp-sha256-hmac
mode tunnel
crypto ipsec profile VTI-PROFILE
set transform-set VTI-VPN

### Tunnel VTI

interface Tunnel1
ip address 172.16.1.1 255.255.255.252
tunnel source 64.100.0.2
tunnel destination 64.100.1.2
tunnel mode ipsec ipv4
tunnel protection ipsec profile VTI-PROFILE

### OSPF dans le tunnel

router ospf 123
network 172.16.1.0 0.0.0.3 area 0

## Vérifications

### Phase 1 IKE

R1# show crypto isakmp sa
dst         src         state      conn-id status
64.100.1.2  64.100.0.2  QM_IDLE    1001    ACTIVE

### Phase 2 IPsec

R1# show crypto ipsec sa
#pkts encaps: 40, #pkts encrypt: 40
#pkts decaps: 34, #pkts decrypt: 34

### OSPF

R1# show ip ospf neighbor
Neighbor ID  Pri  State      Dead Time  Address
3.3.3.1      1    FULL/DR    00:00:34   172.16.1.2

## Résultat
- ✅ Tunnel up/up
- ✅ OSPF voisinage via tunnel
- ✅ Trafic chiffré (ESP)

## Fichiers de configuration
- [R1.txt](configs/R1.txt)
- [R3.txt](configs/R3.txt)
