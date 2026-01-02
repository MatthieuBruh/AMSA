# Formats de fichiers et structures de données sur smartphones

---

## Tableau récapitulatif — Structures de données simples

| Format | Plateforme | Type | Extension | En-tête / Signature | Remarques |
|------|-----------|------|-----------|---------------------|-----------|
| CSV | Android, iOS | Texte | .csv | Aucune              | Structure à plat |
| XML | Android | Texte structuré | .xml | \<?xml …?>          | Hiérarchique |
| PLIST XML | Apple | Texte structuré | .plist | XML + DOCTYPE plist | Config système |
| PLIST binaire | Apple | Binaire | .plist | bplist00            | Optimisé |
| PLIST NSKeyedArchive | Apple | Binaire | .plist | NSKeyedArchive      | Objets sérialisés |
| ABX | Android ≥ 12 | Binaire | .xml | ABX\0               | XML binaire |
| JSON | Android, iOS | Texte structuré | .json | { ou [              | Léger, API |

---

## Tableau récapitulatif — Structures de données évoluées

| Format | Plateforme | Type | Extension | Signature | Remarques |
|------|-----------|------|-----------|-----------|-----------|
| SQLite | Android, iOS | Relationnelle | .db, .sqlite | SQLite format 3 | Base embarquée |
| Protobuf | Android, iOS | Binaire | variable | Aucune | Schéma externe |
| LevelDB | Android, Chromium | NoSQL KV | .log, .ldb | Footer spécifique | Clé/valeur |
| Realm | Android, iOS | NoSQL objet | .realm | T-DB | Orienté objet |
| SEGB | iOS ≥ 15 | Binaire | .segb | Magic + version | Données usage |

---

# Structures de données simples

## CSV (Comma Separated Values)
### Présentation
Format texte simple destiné au stockage de données tabulaires, sans structure hiérarchique.

### Structure interne
- Une ligne = un enregistrement
- Colonnes séparées par des délimiteurs (, ; tabulation)
- Première ligne parfois utilisée comme en-tête

### Caractéristiques
- Aucun typage
- Aucune métadonnée
- Pas d’en-tête

### Points clés examen
- Format à plat
- Très lisible mais peu robuste
- Interprétation dépendante de l’application

---

## XML (eXtensible Markup Language)
### Présentation
Format texte structuré et hiérarchique, très répandu sur Android.

### Structure interne
- Organisation en arbre
- Balises ouvrantes / fermantes
- Attributs optionnels

### En-tête
```xml
<?xml version="1.0" encoding="UTF-8"?>
```

### Utilisation mobile
- shared_prefs Android
- Fichiers de configuration
- Paramètres applicatifs

### Points clés examen
- Auto-descriptif
- Très lisible
- Souvent utilisé pour stocker des données sensibles en clair

---

## PLIST (Property List) — XML
### Présentation
Format historique Apple pour le stockage des préférences.

### Structure interne
- XML hiérarchique
- Paires clé / valeur
- Dictionnaires et tableaux imbriqués

### Types de données
String, Integer, Real, Boolean, Date, Data

### Points clés examen
- Spécifique Apple
- Facilement analysable
- Utilisé pour paramètres système et applicatifs

---

## PLIST — Binaire
### Présentation
Version optimisée du plist XML, plus compacte et plus rapide.

### Signature
```
bplist00
```

### Structure interne
- Header
- Table des objets
- Table des offsets
- Footer

### Intérêt forensique
- Non lisible sans outil
- Même contenu logique que le plist XML

### Points clés examen
- Toujours identifier via la signature
- Extension .plist non suffisante

---

## PLIST — NSKeyedArchive
### Présentation
Format Apple de sérialisation d’objets complexes.

### Caractéristiques
- Basé sur des classes Objective-C / Swift
- Dépend fortement du code applicatif

### Difficulté d’analyse
- Structure variable
- Compréhension du modèle objet souvent nécessaire

### Points clés examen
- Sérialisation d’objets
- Analyse plus complexe que les plist classiques

---

## ABX (Android Binary XML)
### Présentation
Représentation binaire du XML introduite pour améliorer performances et stockage.

### Signature
```
ABX\0
```

### Structure interne
- Tokens
- Données typées
- Évènements XML

### Points clés examen
- Conversion nécessaire pour lecture
- XML logique conservé

---

## JSON (JavaScript Object Notation)
### Présentation
Format texte léger largement utilisé pour les API et configurations.

### Structure interne
- Objets {}
- Tableaux []
- Paires clé / valeur

### Avantages
- Compact
- Lisible
- Portable

### Limites
- Pas de schéma strict intégré

---

# Structures de données évoluées

## SQLite
### Présentation
Base de données relationnelle embarquée standard sur mobile.

### Signature
```
SQLite format 3
```

### Structure interne
- Pages de taille fixe
- Page 1 : en-tête (100 octets) + sqlite_master
- Tables, index, vues, triggers

### Journalisation
- Rollback journal (-journal)
- WAL (-wal)

### Points clés examen
- L’extension n’est pas fiable
- Données souvent récupérables après suppression

---

## Protocol Buffers (Protobuf)
### Présentation
Format binaire de sérialisation développé par Google.

### Caractéristiques
- Très compact
- Typage strict
- Pas d’en-tête

### Structure
- Champ = ID + type + longueur + valeur
- Encodage VARINT, LEN, I32, I64

### Points clés examen
- Schéma .proto absent
- Analyse basée sur structure complète

---

## LevelDB
### Présentation
Base NoSQL clé-valeur utilisée par de nombreuses applications Google.

### Architecture
- .log : écritures récentes
- .ldb : tables ordonnées
- MANIFEST, CURRENT, LOCK

### Fonctionnement
- Écritures → .log
- Compaction → .ldb
- Valeurs souvent encodées en Protobuf

### Points clés examen
- Pas de SQL
- Données arbitraires clé/valeur

---

## Realm
### Présentation
Base NoSQL orientée objet, alternative à SQLite.

### Signature
```
T-DB (0x542D4442)
```

### Structure
- .realm
- .realm.lock
- .realm.management

### Modèle de données
- Classes → objets
- Attributs → propriétés

### Points clés examen
- Forte dépendance au modèle applicatif

---

## SEGB (Biomes)
### Présentation
Format Apple introduit avec iOS 15 pour stocker les données d’utilisation de l’appareil.

### Versions
- v1 : iOS 15
- v2 : iOS 17 (footer ajouté)

### Structure
- En-tête
- Trames
- Payload (majoritairement Protobuf)
- Footer (v2)

### Données stockées
- Utilisation applications
- Réseau
- Localisation
- Activité système

### Points clés examen
- Remplace partiellement knowledgeC.db
- Données riches mais durée de vie limitée (~28 jours)
