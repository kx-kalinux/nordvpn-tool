```
    ██╗  ██╗ █████╗ ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
    ██║ ██╔╝██╔══██╗██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
    █████╔╝ ███████║██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝
    ██╔═██╗ ██╔══██║██║     ██║██║╚██╗██║██║   ██║ ██╔██╗
    ██║  ██╗██║  ██║███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
    ═══════════════════════════════════════════════════════
      { S C R I P T }  </>  [ Fueled with Claudc0de ]
    ═══════════════════════════════════════════════════════
```

# NordVPN Terminal Interface Tool

Ein benutzerfreundliches Python-Tool zur Verwaltung von NordVPN über das Terminal.

## Features

- **Installation & Setup**: Automatische Installation der NordVPN CLI
- **Verbindungsoptionen**:
  - Schnellverbindung zum besten Server
  - Verbindung nach Land
  - Verbindung nach spezifischem Server
  - Verbindung nach Stadt
  - Spezialserver (P2P, Onion Over VPN, Double VPN)
- **Nützliche Tools**:
  - Aktuelle IP-Adresse & Geolocation anzeigen
  - VPN-Status prüfen
  - Verfügbare Länder auflisten
  - Einstellungen anzeigen

## Installation

1. Virtual Environment erstellen und Dependencies installieren:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Script ausführbar machen:
```bash
chmod +x nordvpn_tool.py
```

## Verwendung

Mit aktiviertem Virtual Environment:
```bash
source venv/bin/activate
python3 nordvpn_tool.py
```

Oder direkt:
```bash
./nordvpn_tool.py
```

## Erste Schritte

1. Tool starten
2. Option 1 wählen: NordVPN installieren
3. Option 2 wählen: Login (Browser öffnet sich)
4. Option 4 wählen: Schnellverbindung oder andere Verbindungsoptionen nutzen

## Systemanforderungen

- Linux (Debian/Ubuntu oder kompatibel)
- Python 3.6+
- Internetverbindung

## Hinweise

- Für die Installation sind Root-Rechte erforderlich
- NordVPN-Account wird benötigt
- Das Tool nutzt die offizielle NordVPN CLI
