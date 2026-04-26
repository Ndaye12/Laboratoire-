# 🏢 Réseau Multi-Sites Sécurisé

## Objectif
Concevoir une infrastructure réseau multi-sites sécurisée avec routage dynamique, redondance, firewalling avancé et accès distant.

---

## Technologies utilisées
- OSPF multi-area
- VLAN & Inter-VLAN Routing
- GRE (IPv4 / IPv6)
- IPsec VTI (site-à-site)
- HSRP
- IP SLA + Tracking
- ACL 
- Zone-Based Firewall (ZBF)
- Firewall Fortinet (FortiGate)
- NAT/PAT
- SSL VPN

---

## Topologie

---

## Architecture

- 4 routeurs principaux (R1, R2, R3, R4)
- 1 routeur secondaire (R1-BIS) pour redondance
- Switchs VLAN
- Firewall FortiGate en bordure (WAN)

---

## Configuration

### 🔹 OSPF multi-area

router ospf 1
network 10.0.0.0 0.0.0.255 area 0
network 192.168.10.0 0.0.0.255 area 1
network 192.168.20.0 0.0.0.255 area 2

---

### 🔹 HSRP (Redondance passerelle)

interface GigabitEthernet0/0
standby 1 ip 192.168.10.1
standby 1 priority 110
standby 1 preempt

---

### 🔹 IP SLA + Tracking

ip sla 1
icmp-echo 8.8.8.8
frequency 5

track 1 ip sla 1 reachability

---

### 🔹 Tunnel GRE

interface Tunnel0
ip address 172.16.10.1 255.255.255.252
tunnel source GigabitEthernet0/1
tunnel destination 10.10.10.2

---

### 🔹 IPsec VTI

interface Tunnel1
ip address 172.16.1.1 255.255.255.252
tunnel source 64.100.0.2
tunnel destination 64.100.1.2
tunnel mode ipsec ipv4

---

### 🔹 Zone-Based Firewall (ZBF)

zone security LAN
zone security WAN

policy-map type inspect POLICY-LAN-WAN
class type inspect class-default
inspect

---

### 🔹 FortiGate – Policies

- LAN → WAN : NAT enabled
- WAN → LAN : Deny
- SSL VPN → LAN : Allow

---

### 🔹 Web Filtering

- Blocage facebook.com

---

### 🔹 Application Control

- Blocage : Tor, WhatsApp, BitTorrent

---

### 🔹 SSL VPN

- Port : 443
- Accès distant sécurisé
- Groupe : VPN_Users

---

## Vérifications

### 🔹 OSPF

R1# show ip ospf neighbor

---

### 🔹 HSRP

R1# show standby brief

---

### 🔹 IPsec

R1# show crypto ipsec sa

---

### 🔹 IP SLA

R1# show track

---

### 🔹 ZBF

R1# show policy-map type inspect zone-pair

---

### 🔹 FortiGate

- Vérification des policies
- Test blocage web (Facebook)

---

### 🔹 Test utilisateur

VPCS> ping 8.8.8.8  
✔ Connectivité Internet

VPCS> curl facebook.com  
❌ Bloqué

VPCS> curl google.com  
✔ Autorisé

---

## Résultat

- ✅ Routage dynamique opérationnel (OSPF)
- ✅ Redondance fonctionnelle (HSRP + IP SLA)
- ✅ Tunnel sécurisé (IPsec + GRE)
- ✅ Sécurité réseau appliquée (ACL + ZBF)
- ✅ Firewall FortiGate opérationnel
- ✅ Filtrage web et applicatif actif
- ✅ Accès distant via SSL VPN configuré

---

## Fichiers de configuration

- [R1](config/cisco/R1.txt)
- [R1-BIS](config/cisco/R1-bis.txt)
- [R2](https://github.com/Ndaye12/Ndaye-Network-Projects/blob/main/Multi-Site-Secure-Network/Config/Cisco/R2.txt)
- [R3](https://github.com/Ndaye12/Ndaye-Network-Projects/blob/main/Multi-Site-Secure-Network/Config/Cisco/R3.txt)
- [R4](https://github.com/Ndaye12/Ndaye-Network-Projects/blob/main/Multi-Site-Secure-Network/Config/Cisco/R4.txt)
- [FortiGate](https://github.com/Ndaye12/Ndaye-Network-Projects/blob/main/Multi-Site-Secure-Network/Config/Fortigate/fortigate-config.txt)

---

## Captures

- Topologie réseau
- OSPF & routage
- HSRP
- IP SLA tracking
- Tunnel IPsec
- ZBF
- Policies FortiGate
- Web filtering
- Test curl (Facebook bloqué)
