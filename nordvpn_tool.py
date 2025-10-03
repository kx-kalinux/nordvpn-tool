#!/usr/bin/env venv/bin/python3
"""
NordVPN Terminal Interface Tool
Ein benutzerfreundliches Terminal-Interface für NordVPN
"""

import subprocess
import sys
import os
import requests
from typing import Optional, List, Dict

class Colors:
    """ANSI Farbcodes für Terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class NordVPNTool:
    def __init__(self):
        self.nordvpn_installed = self.check_nordvpn_installed()

    def check_nordvpn_installed(self) -> bool:
        """Prüft ob NordVPN installiert ist"""
        try:
            subprocess.run(["nordvpn", "--version"],
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def install_nordvpn(self):
        """Installiert NordVPN CLI"""
        print(f"\n{Colors.HEADER}=== NordVPN Installation ==={Colors.ENDC}")
        print(f"\n{Colors.WARNING}NordVPN wird installiert...{Colors.ENDC}")

        try:
            # Download und Installation für Debian/Ubuntu basierte Systeme
            print("Lade NordVPN herunter...")
            subprocess.run([
                "sh", "-c",
                "curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh | sh"
            ], check=True)

            print(f"{Colors.OKGREEN}✓ NordVPN erfolgreich installiert!{Colors.ENDC}")
            print(f"\n{Colors.OKCYAN}Bitte melde dich an mit: nordvpn login{Colors.ENDC}")
            self.nordvpn_installed = True

        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Installation fehlgeschlagen: {e}{Colors.ENDC}")
            print(f"\n{Colors.WARNING}Manuelle Installation:{Colors.ENDC}")
            print("Besuche: https://nordvpn.com/download/linux/")

    def get_current_ip(self):
        """Zeigt die aktuelle IP-Adresse"""
        print(f"\n{Colors.HEADER}=== IP-Informationen ==={Colors.ENDC}\n")

        try:
            # Externe IP abfragen
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            ip_data = response.json()
            print(f"{Colors.OKBLUE}Externe IP:{Colors.ENDC} {ip_data['ip']}")

            # Detaillierte Informationen
            response = requests.get(f"http://ip-api.com/json/{ip_data['ip']}", timeout=5)
            geo_data = response.json()

            print(f"{Colors.OKBLUE}Land:{Colors.ENDC} {geo_data.get('country', 'N/A')}")
            print(f"{Colors.OKBLUE}Stadt:{Colors.ENDC} {geo_data.get('city', 'N/A')}")
            print(f"{Colors.OKBLUE}ISP:{Colors.ENDC} {geo_data.get('isp', 'N/A')}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Fehler beim Abrufen der IP: {e}{Colors.ENDC}")

    def show_status(self):
        """Zeigt den aktuellen NordVPN Status"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            result = subprocess.run(["nordvpn", "status"],
                                  capture_output=True, text=True, check=True)
            print(f"\n{Colors.HEADER}=== NordVPN Status ==={Colors.ENDC}\n")
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Fehler beim Abrufen des Status{Colors.ENDC}")

    def connect_to_country(self, country: str):
        """Verbindet zu einem bestimmten Land"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            print(f"\n{Colors.WARNING}Verbinde zu {country}...{Colors.ENDC}")
            result = subprocess.run(["nordvpn", "connect", country],
                                  capture_output=True, text=True, check=True)
            print(f"{Colors.OKGREEN}✓ {result.stdout}{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Verbindung fehlgeschlagen: {e.stderr}{Colors.ENDC}")

    def connect_to_server(self, server: str):
        """Verbindet zu einem bestimmten Server"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            print(f"\n{Colors.WARNING}Verbinde zu Server {server}...{Colors.ENDC}")
            result = subprocess.run(["nordvpn", "connect", server],
                                  capture_output=True, text=True, check=True)
            print(f"{Colors.OKGREEN}✓ {result.stdout}{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Verbindung fehlgeschlagen: {e.stderr}{Colors.ENDC}")

    def connect_specialty(self, specialty: str):
        """Verbindet zu spezialisierten Servern (P2P, Onion, etc.)"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            print(f"\n{Colors.WARNING}Verbinde zu {specialty} Server...{Colors.ENDC}")
            result = subprocess.run(["nordvpn", "connect", "--group", specialty],
                                  capture_output=True, text=True, check=True)
            print(f"{Colors.OKGREEN}✓ {result.stdout}{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Verbindung fehlgeschlagen: {e.stderr}{Colors.ENDC}")

    def disconnect(self):
        """Trennt die VPN-Verbindung"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            result = subprocess.run(["nordvpn", "disconnect"],
                                  capture_output=True, text=True, check=True)
            print(f"{Colors.OKGREEN}✓ {result.stdout}{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Fehler beim Trennen: {e.stderr}{Colors.ENDC}")

    def quick_connect(self):
        """Schnellverbindung zum besten Server"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            print(f"\n{Colors.WARNING}Verbinde zum besten Server...{Colors.ENDC}")
            result = subprocess.run(["nordvpn", "connect"],
                                  capture_output=True, text=True, check=True)
            print(f"{Colors.OKGREEN}✓ {result.stdout}{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}✗ Verbindung fehlgeschlagen: {e.stderr}{Colors.ENDC}")

    def show_countries(self):
        """Zeigt verfügbare Länder"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            result = subprocess.run(["nordvpn", "countries"],
                                  capture_output=True, text=True, check=True)
            print(f"\n{Colors.HEADER}=== Verfügbare Länder ==={Colors.ENDC}\n")
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Fehler beim Abrufen der Länder{Colors.ENDC}")

    def show_cities(self, country: str):
        """Zeigt verfügbare Städte in einem Land"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            result = subprocess.run(["nordvpn", "cities", country],
                                  capture_output=True, text=True, check=True)
            print(f"\n{Colors.HEADER}=== Verfügbare Städte in {country} ==={Colors.ENDC}\n")
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Fehler beim Abrufen der Städte{Colors.ENDC}")

    def login(self):
        """NordVPN Login"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        print(f"\n{Colors.OKCYAN}Öffne Browser für Login...{Colors.ENDC}")
        try:
            subprocess.run(["nordvpn", "login"], check=True)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Login fehlgeschlagen{Colors.ENDC}")

    def logout(self):
        """NordVPN Logout"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            subprocess.run(["nordvpn", "logout"], check=True)
            print(f"{Colors.OKGREEN}✓ Erfolgreich abgemeldet{Colors.ENDC}")
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Logout fehlgeschlagen{Colors.ENDC}")

    def show_settings(self):
        """Zeigt aktuelle NordVPN Einstellungen"""
        if not self.nordvpn_installed:
            print(f"{Colors.FAIL}✗ NordVPN ist nicht installiert{Colors.ENDC}")
            return

        try:
            result = subprocess.run(["nordvpn", "settings"],
                                  capture_output=True, text=True, check=True)
            print(f"\n{Colors.HEADER}=== NordVPN Einstellungen ==={Colors.ENDC}\n")
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}✗ Fehler beim Abrufen der Einstellungen{Colors.ENDC}")

def print_banner():
    """Zeigt Banner"""
    banner = f"""
{Colors.OKCYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════╗
║          NordVPN Terminal Interface Tool          ║
╚═══════════════════════════════════════════════════╝
{Colors.ENDC}
    """
    print(banner)

def print_menu():
    """Zeigt das Hauptmenü"""
    menu = f"""
{Colors.HEADER}=== Hauptmenü ==={Colors.ENDC}

{Colors.BOLD}Installation & Setup:{Colors.ENDC}
  1)  NordVPN installieren
  2)  Login
  3)  Logout

{Colors.BOLD}Verbindung:{Colors.ENDC}
  4)  Schnellverbindung (bester Server)
  5)  Nach Land verbinden
  6)  Nach Server verbinden
  7)  Nach Stadt verbinden
  8)  Spezialserver (P2P, Onion, etc.)
  9)  Trennen

{Colors.BOLD}Informationen:{Colors.ENDC}
  10) Status anzeigen
  11) Aktuelle IP anzeigen
  12) Verfügbare Länder anzeigen
  13) Einstellungen anzeigen

{Colors.BOLD}Sonstiges:{Colors.ENDC}
  0)  Beenden

{Colors.OKGREEN}Auswahl:{Colors.ENDC} """

    return input(menu)

def main():
    """Hauptfunktion"""
    tool = NordVPNTool()

    print_banner()

    # Warnung wenn NordVPN nicht installiert ist
    if not tool.nordvpn_installed:
        print(f"{Colors.WARNING}⚠ NordVPN ist nicht installiert!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Wähle Option 1 um NordVPN zu installieren.{Colors.ENDC}\n")

    while True:
        try:
            choice = print_menu()

            if choice == "0":
                print(f"\n{Colors.OKCYAN}Auf Wiedersehen!{Colors.ENDC}\n")
                break

            elif choice == "1":
                tool.install_nordvpn()

            elif choice == "2":
                tool.login()

            elif choice == "3":
                tool.logout()

            elif choice == "4":
                tool.quick_connect()

            elif choice == "5":
                tool.show_countries()
                country = input(f"\n{Colors.OKGREEN}Land eingeben:{Colors.ENDC} ")
                if country:
                    tool.connect_to_country(country)

            elif choice == "6":
                server = input(f"\n{Colors.OKGREEN}Server eingeben (z.B. de123):{Colors.ENDC} ")
                if server:
                    tool.connect_to_server(server)

            elif choice == "7":
                country = input(f"\n{Colors.OKGREEN}Land eingeben:{Colors.ENDC} ")
                if country:
                    tool.show_cities(country)
                    city = input(f"\n{Colors.OKGREEN}Stadt eingeben:{Colors.ENDC} ")
                    if city:
                        tool.connect_to_server(city)

            elif choice == "8":
                print(f"\n{Colors.HEADER}Spezialserver:{Colors.ENDC}")
                print("  1) P2P")
                print("  2) Onion Over VPN")
                print("  3) Double VPN")
                specialty_choice = input(f"\n{Colors.OKGREEN}Auswahl:{Colors.ENDC} ")

                specialty_map = {
                    "1": "p2p",
                    "2": "onion_over_vpn",
                    "3": "double_vpn"
                }

                if specialty_choice in specialty_map:
                    tool.connect_specialty(specialty_map[specialty_choice])

            elif choice == "9":
                tool.disconnect()

            elif choice == "10":
                tool.show_status()

            elif choice == "11":
                tool.get_current_ip()

            elif choice == "12":
                tool.show_countries()

            elif choice == "13":
                tool.show_settings()

            else:
                print(f"{Colors.FAIL}✗ Ungültige Auswahl{Colors.ENDC}")

            input(f"\n{Colors.OKCYAN}Drücke Enter um fortzufahren...{Colors.ENDC}")

            # Clear screen
            os.system('clear' if os.name == 'posix' else 'cls')
            print_banner()

        except KeyboardInterrupt:
            print(f"\n\n{Colors.OKCYAN}Auf Wiedersehen!{Colors.ENDC}\n")
            break
        except Exception as e:
            print(f"\n{Colors.FAIL}✗ Fehler: {e}{Colors.ENDC}")
            input(f"\n{Colors.OKCYAN}Drücke Enter um fortzufahren...{Colors.ENDC}")

if __name__ == "__main__":
    main()
