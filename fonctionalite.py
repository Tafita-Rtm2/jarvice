# Fonctionnalités principales et liaisons JARVIS
import os

def exec_command(cmd):
    print(f"Exécution de la commande : {cmd}")
    return os.popen(cmd).read()

def JarvisCore():
    print("Core de JARVIS chargé avec succès.")

if __name__ == "__main__":
    JarvisCore()
