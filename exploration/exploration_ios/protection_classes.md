# Classes de protection des données iOS

## Vue d'ensemble

iOS propose quatre classes de protection des données (`NSFileProtection`), qui déterminent quand et comment les fichiers peuvent être déchiffrés en fonction de l'état de verrouillage de l'appareil.

---

## Classe A — "Le plus strict"

**Protection maximale** : `NSFileProtectionComplete`

### Fonctionnement
* La clé nécessaire pour déchiffrer est liée au code utilisateur (et au matériel).
* Quand l'appareil est verrouillé, iOS retire de la mémoire la clé déchiffrée de cette classe.
* Les fichiers deviennent **cryptographiquement inaccessibles** jusqu'au prochain déverrouillage.

### Usage typique
* Secrets sensibles (mots de passe, tokens)
* Données santé très privées
* Notes très sensibles
* Informations financières critiques

---

## Classe B — "A, mais tolère les fichiers déjà ouverts"

**Protection stricte avec exception** : `NSFileProtectionCompleteUnlessOpen`

### Fonctionnement
* Objectif : permettre un cas pratique où l'app écrit un flux/log/téléchargement et l'utilisateur verrouille.
* Si le fichier est **ouvert au moment du verrouillage**, iOS permet de continuer à y accéder tant qu'il reste ouvert.
* Dès que le fichier est fermé, la clé "par fichier" n'est plus conservée → il redevient inaccessible comme en Classe A.

### Usage typique
* Enregistrements audio/vidéo en cours
* Téléchargements actifs
* Bases de données ou archives en écriture continue

---

## Classe C — "Pratique pour le background après un déverrouillage"

**Protection modérée** : `NSFileProtectionCompleteUntilFirstUserAuthentication`

### Fonctionnement
* Après le **premier déverrouillage** depuis un redémarrage, la clé de classe reste disponible même si l'appareil est reverrouillé.
* L'app peut continuer des tâches en arrière-plan (sync, notifications avec contenu, indexation, etc.) même écran verrouillé.
* C'est le **défaut le plus courant** pour les données d'app tierces si rien n'est spécifié.

### Usage typique
* Données utilisateur "normales" qui doivent rester accessibles aux services background
* Cache applicatif
* Base de données de l'app
* Messages à afficher dans les notifications
* Contenu synchronisé en arrière-plan

---

## Classe D — "Pas vraiment de protection par code"

**Protection minimale** : `NSFileProtectionNone`

### Fonctionnement
* Les clés nécessaires sont sur l'appareil (liées au matériel uniquement).
* Les fichiers restent accessibles **même sans que l'utilisateur ait entré le code**.
* L'intérêt principal : si on efface certaines clés (remote wipe), ça peut rendre les données inutilisables rapidement.

### Usage typique
* Contenu non sensible
* Caches système
* Ressources téléchargeables publiques
* Données qu'on accepte d'exposer si l'appareil est compromis physiquement

---

## Tableau récapitulatif

| Classe | Nom technique | Accessible quand verrouillé ? | Usage principal |
|--------|---------------|-------------------------------|-----------------|
| **A** | `NSFileProtectionComplete` | Non                     | Données très sensibles |
| **B** | `NSFileProtectionCompleteUnlessOpen` | Si déjà ouvert          | Flux continus en écriture |
| **C** | `NSFileProtectionCompleteUntilFirstUserAuthentication` | AFU                           | Données d'app standard (défaut) |
| **D** | `NSFileProtectionNone` | BFU                           | Contenu non sensible |

- La classe A et B implique indirectement que l'appareil est en mode AFU.
---

## Recommandations

1. **Par défaut** : Classe C est un bon compromis pour la plupart des apps
2. **Données sensibles** : Utilisez Classe A pour les secrets critiques
3. **Background tasks** : Classe C est nécessaire pour les opérations en arrière-plan
4. **Contenu public** : Classe D uniquement pour les ressources non sensibles