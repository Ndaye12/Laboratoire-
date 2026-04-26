from netmiko import ConnectHandler
import datetime

# Liste des routeurs (IP, login, mot de passe)
routeurs = [
    {"device_type": "cisco_ios_telnet", "host": "127.0.0.1", "port":5008, "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios_telnet", "host": "127.0.0.1", "port":5007, "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios_telnet", "host": "127.0.0.1", "port":5006, "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios_telnet", "host": "127.0.0.1", "port":5005, "username": "admin", "password": "cisco123"},
]

for router in routeurs:
    try:
        connexion = ConnectHandler(**router)
        config = connexion.send_command("show run")
        nom_fichier = f"{router['host']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nom_fichier, "w") as f:
            f.write(config)
        print(f"Sauvegarde de {router['host']} réussie : {nom_fichier}")
        connexion.disconnect()
    except Exception as e:
        print(f"Erreur pour {router['host']} : {e}")