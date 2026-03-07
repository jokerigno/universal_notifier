# Universal Notifier - Conversione Completa a UI

## 📋 Tutti i File Generati

### ✅ File Pronti per Download

| # | File Scaricato | → Rinomina in | Destinazione |
|---|----------------|---------------|--------------|
| 1 | `config_flow_v2.py` | `config_flow.py` | `/config/custom_components/universal_notifier/` |
| 2 | `const_v2.py` | `const.py` | `/config/custom_components/universal_notifier/` |
| 3 | `binary_sensor_v2.py` | `binary_sensor.py` | `/config/custom_components/universal_notifier/` |
| 4 | `sensor_v2.py` | `sensor.py` | `/config/custom_components/universal_notifier/` |
| 5 | `select_v2.py` | `select.py` | `/config/custom_components/universal_notifier/` |
| 6 | `init_v2.py` | `__init__.py` | `/config/custom_components/universal_notifier/` |
| 7 | `manifest_v2.json` | `manifest.json` | `/config/custom_components/universal_notifier/` |
| 8 | `strings_v2.json` | `strings.json` | `/config/custom_components/universal_notifier/` |
| 9 | `strings_v2.json` | `en.json` | `/config/custom_components/universal_notifier/translations/` |
| 10 | `utils.py` | `utils.py` | `/config/custom_components/universal_notifier/` (già presente) |
| 11 | `services.yaml` | `services.yaml` | `/config/custom_components/universal_notifier/` (già presente) |

---

## 🚀 Installazione Completa

### Step 1: Backup
```bash
# Backup completo
cp -r /config/custom_components/universal_notifier \
      /config/custom_components/universal_notifier.backup_$(date +%Y%m%d)

# Verifica backup
ls -la /config/custom_components/universal_notifier.backup*
```

### Step 2: Rimuovi Config YAML
Apri `configuration.yaml` e **rimuovi completamente**:
```yaml
# ELIMINA QUESTA INTERA SEZIONE:
universal_notifier:
  assistant_name: "..."
  channels:
    ...
  time_slots:
    ...
  dnd:
    ...
  greetings:
    ...
```

Salva il file.

### Step 3: Sostituisci File
```bash
# Assumendo che i file scaricati siano in /tmp

# File Python
cp /tmp/config_flow_v2.py /config/custom_components/universal_notifier/config_flow.py
cp /tmp/const_v2.py /config/custom_components/universal_notifier/const.py
cp /tmp/binary_sensor_v2.py /config/custom_components/universal_notifier/binary_sensor.py
cp /tmp/sensor_v2.py /config/custom_components/universal_notifier/sensor.py
cp /tmp/select_v2.py /config/custom_components/universal_notifier/select.py
cp /tmp/init_v2.py /config/custom_components/universal_notifier/__init__.py

# File JSON
cp /tmp/manifest_v2.json /config/custom_components/universal_notifier/manifest.json
cp /tmp/strings_v2.json /config/custom_components/universal_notifier/strings.json

# Crea cartella translations e copia
mkdir -p /config/custom_components/universal_notifier/translations
cp /tmp/strings_v2.json /config/custom_components/universal_notifier/translations/en.json

# Verifica permessi
chmod 644 /config/custom_components/universal_notifier/*.py
chmod 644 /config/custom_components/universal_notifier/*.json
chmod 644 /config/custom_components/universal_notifier/*.yaml
```

### Step 4: Verifica File
```bash
# Lista tutti i file
ls -la /config/custom_components/universal_notifier/

# Output atteso:
# __init__.py
# config_flow.py
# const.py
# binary_sensor.py
# sensor.py
# select.py
# utils.py
# manifest.json
# strings.json
# services.yaml
# translations/
#   └── en.json
```

### Step 5: Riavvia Home Assistant
```
UI: Settings → System → Restart Home Assistant
```

**Attendi il riavvio completo** (~1-2 minuti)

### Step 6: Aggiungi Integrazione
```
1. Settings → Devices & Services
2. Click su "+ ADD INTEGRATION"
3. Cerca "Universal Notifier"
4. Click sull'integrazione
```

### Step 7: Completa il Wizard

#### 📝 Step 1/7: Impostazioni Base
```
Nome Assistente: Home Assistant
Formato Data/Ora: %H:%M
Includi Orario: ✓
Prefisso Grassetto: ✓
Volume Priorità: 90%
```
Click **SUBMIT**

#### 📝 Step 2/7: Fasce Orarie
```
Mattino:     07:00 → 0.35
Pomeriggio:  12:00 → 0.40
Sera:        19:00 → 0.30
Notte:       22:00 → 0.10
```
Click **SUBMIT**

#### 📝 Step 3/7: Non Disturbare
```
Inizio DND: 23:00
Fine DND:   07:00
```
Click **SUBMIT**

#### 📝 Step 4/7: Saluti
```
Mattino:     Buongiorno, Ben alzato, Salve
Pomeriggio:  Buon pomeriggio, Ciao, Ben ritrovato
Sera:        Buonasera, Buona serata, Ben tornato
Notte:       Buonanotte, Sogni d'oro, È tardi
```
Click **SUBMIT**

#### 📝 Step 5/7: Menu Canali
```
Canali configurati:
(nessuno ancora)

Action: [Aggiungi nuovo canale]
```
Click **SUBMIT**

#### 📝 Step 6/7: Aggiungi Canale (Ripeti per ogni canale)

**Esempio Alexa:**
```
Nome Canale: alexa_salotto
Servizio: notify.alexa_media_echo_dot
Target: (lascia vuoto)
Entity ID: (lascia vuoto)
È Vocale: ✓
```
Click **SUBMIT** → Torna al menu canali

**Esempio Google Home:**
```
Nome Canale: gh_cucina
Servizio: tts.google_translate_say
Target: tts.google_translate_it_it
Entity ID: media_player.cucina
È Vocale: ✓
```
Click **SUBMIT** → Torna al menu canali

**Esempio Mobile App:**
```
Nome Canale: mobile_app_user
Servizio: notify.mobile_app_phone
Target: (lascia vuoto)
Entity ID: (lascia vuoto)
È Vocale: ✗
```
Click **SUBMIT** → Torna al menu canali

Dopo aver aggiunto tutti i canali:
```
Action: [Termina configurazione]
```
Click **SUBMIT**

#### 📝 Step 7/7: Fine
Il wizard termina e l'integrazione è configurata!

---

## 🎯 Verifica Installazione

### 1. Verifica Integrazione
```
Settings → Devices & Services

Dovresti vedere:
┌─────────────────────────────────┐
│ Universal Notifier (Home Ass... │
│ 3 entities                      │
│ 1 service                       │
└─────────────────────────────────┘
```

### 2. Verifica Entità
```
Developer Tools → States

Cerca:
✓ binary_sensor.universal_notifier_dnd
✓ sensor.universal_notifier_volume
✓ select.universal_notifier_priority_volume
```

### 3. Verifica Servizio
```
Developer Tools → Services

Cerca:
✓ universal_notifier.send
```

### 4. Test Notifica
```yaml
# Developer Tools → Services
service: universal_notifier.send
data:
  message: "Test notifica da UI!"
  targets:
    - alexa_salotto
    - mobile_app_user
```

Click **CALL SERVICE**

Se ricevi la notifica → **✅ Installazione completata!**

---

## 🔧 Modifica Configurazione Post-Setup

### Accesso Options Flow
```
Settings → Devices & Services
→ Universal Notifier
→ CONFIGURE
```

### Menu Disponibili
```
○ Impostazioni Base
  - Nome assistente
  - Formato data
  - Include time
  - Bold prefix
  - Priority volume

○ Fasce Orarie & DND
  - Tutti gli orari e volumi
  - Inizio/fine DND

○ Canali di Notifica
  - Aggiungi nuovo canale
  - Rimuovi canali esistenti
```

---

## 📊 Entità Create

### 1. binary_sensor.universal_notifier_dnd
```yaml
State: on/off
Icon: mdi:bell-off (on) / mdi:bell-ring (off)
Attributes:
  dnd_start: "23:00"
  dnd_end: "07:00"
```

**Uso in Automazione:**
```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.universal_notifier_dnd
    to: "off"
action:
  - service: universal_notifier.send
    data:
      message: "DND terminato, buongiorno!"
      targets: [alexa_salotto]
```

### 2. sensor.universal_notifier_volume
```yaml
State: 35 (%)
Icon: mdi:volume-off/low/medium/high (dinamico)
Attributes:
  current_slot: "morning"
  raw_volume: 0.35
  time_slots: {...}
```

**Uso in Automazione:**
```yaml
trigger:
  - platform: state
    entity_id: sensor.universal_notifier_volume
action:
  - service: notify.persistent_notification
    data:
      message: "Volume cambiato a {{ states('sensor.universal_notifier_volume') }}%"
```

### 3. select.universal_notifier_priority_volume
```yaml
State: "0.9"
Icon: mdi:volume-high
Attributes:
  decimal_value: 0.9
  percentage: "90%"
  description: "Volume usato quando priority=True"
Options:
  - "0.1" (10%)
  - "0.2" (20%)
  - ...
  - "1.0" (100%)
```

**Uso in Automazione:**
```yaml
# Imposta volume massimo di notte
trigger:
  - platform: time
    at: "23:00:00"
action:
  - service: select.select_option
    target:
      entity_id: select.universal_notifier_priority_volume
    data:
      option: "1.0"
```

**Uso in Notifica:**
```yaml
service: universal_notifier.send
data:
  message: "EMERGENZA!"
  targets: [alexa_salotto]
  priority: true  # Userà il volume del select (1.0)
```

---

## 🎨 Dashboard Example

```yaml
type: vertical-stack
cards:
  # Card Status
  - type: entities
    title: Universal Notifier
    entities:
      - entity: binary_sensor.universal_notifier_dnd
        name: Non Disturbare
      - entity: sensor.universal_notifier_volume
        name: Volume Corrente
      - entity: select.universal_notifier_priority_volume
        name: Volume Priorità
  
  # Card Gauge Volume
  - type: gauge
    entity: sensor.universal_notifier_volume
    name: Volume
    needle: true
    min: 0
    max: 100
    severity:
      green: 0
      yellow: 34
      orange: 67
      red: 90
  
  # Card Test
  - type: button
    name: Test Notifica
    icon: mdi:bell-ring
    tap_action:
      action: call-service
      service: universal_notifier.send
      service_data:
        message: Test dalla dashboard!
        targets:
          - alexa_salotto
```

---

## 🐛 Troubleshooting

### Problema: Integrazione non appare

**Soluzione:**
```bash
# 1. Verifica manifest.json
cat /config/custom_components/universal_notifier/manifest.json | grep config_flow
# Output atteso: "config_flow": true

# 2. Controlla log
tail -f /config/home-assistant.log | grep universal_notifier

# 3. Riavvia HA
# Settings → System → Restart
```

### Problema: Entità non appaiono

**Soluzione:**
```bash
# Verifica che i file siano presenti
ls -la /config/custom_components/universal_notifier/ | grep -E "(binary_sensor|sensor|select).py"

# Output atteso:
# binary_sensor.py
# sensor.py
# select.py

# Controlla log per errori
grep -i "universal_notifier" /config/home-assistant.log | grep -i error
```

### Problema: Servizio non funziona

**Soluzione:**
```yaml
# 1. Verifica canali configurati
# Settings → Devices & Services → Universal Notifier → CONFIGURE

# 2. Test semplice
service: universal_notifier.send
data:
  message: "Test"
  targets: [nome_canale_configurato]

# 3. Controlla log
tail -f /config/home-assistant.log | grep UniNotifier
```

### Problema: Select non aggiorna

**Soluzione:**
```yaml
# Developer Tools → Services
service: homeassistant.reload_config_entry
target:
  entity_id: select.universal_notifier_priority_volume
```

---

## 📚 File di Riferimento

| File | Righe | Descrizione |
|------|-------|-------------|
| `config_flow.py` | ~450 | Wizard UI completo |
| `__init__.py` | ~550 | Logica principale |
| `const.py` | ~50 | Costanti (no default) |
| `binary_sensor.py` | ~50 | Entità DND |
| `sensor.py` | ~60 | Entità Volume |
| `select.py` | ~70 | Entità Priority Volume |
| `utils.py` | ~80 | Helper functions |
| `manifest.json` | ~15 | Metadata integrazione |
| `strings.json` | ~200 | Traduzioni UI |
| `services.yaml` | ~100 | Schema servizio |

**Totale**: ~1625 righe di codice

---

## ✅ Checklist Finale

### Pre-Installazione
- [ ] Backup completato
- [ ] Config YAML rimossa
- [ ] Tutti i file scaricati

### Installazione
- [ ] 9 file copiati correttamente
- [ ] Cartella translations/ creata
- [ ] Permessi file verificati
- [ ] HA riavviato

### Post-Installazione
- [ ] Integrazione aggiunta da UI
- [ ] Wizard completato (7 step)
- [ ] Almeno 1 canale configurato
- [ ] 3 entità visibili
- [ ] Servizio disponibile

### Test
- [ ] Notifica test inviata
- [ ] Entità DND funzionante
- [ ] Entità Volume funzionante
- [ ] Select Priority Volume funzionante
- [ ] Options Flow accessibile

---

## 🎉 Completato!

Hai convertito con successo Universal Notifier da configurazione YAML a configurazione UI completa!

**Versione**: 1.0.0  
**Config Flow**: ✅ Abilitato  
**YAML Required**: ❌ No  
**Entità**: 3  
**File Modificati**: 11  

Buon utilizzo! 🚀
