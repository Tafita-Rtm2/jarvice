# point d'entrée principal de l'application JARVIS pour l'APK
from ecran import main_screen
from fonctionalite import JarvisCore

def main():
    print("Démarrage de l'application JARVIS...")
    main_screen()
    JarvisCore()
    print("JARVIS est prêt.")

if __name__ == '__main__':
    main()
