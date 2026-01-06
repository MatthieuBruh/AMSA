# Sandboxing sur iOS et Android

## Vue d'ensemble

iOS et Android utilisent tous deux des mécanismes de **sandboxing** pour isoler les applications et protéger les données utilisateur. Bien que les objectifs soient similaires, les approches techniques et philosophiques diffèrent.

---

## Sandboxing sur iOS

### 📌 Comment ça marche

* Chaque application iOS est automatiquement isolée dans un **"sandbox" qui lui est propre**.
* Une app ne peut accéder qu'à **ses propres fichiers, données et ressources** (réseau, matériel, etc.) que si elle a les permissions appropriées.
* Les applications doivent être **signées par Apple** (certificat Apple) pour fonctionner sur un appareil iOS, ce qui fait partie du modèle de confiance.

### 📌 Effets pratiques

* Une app iOS **ne peut pas lire ou modifier** les fichiers d'une autre app à moins d'utiliser des mécanismes spécifiques (partage de données via API Apple).
* L'accès au matériel et données sensibles (photos, caméra, localisation, etc.) nécessite une **autorisation explicite de l'utilisateur**.

### 👉 En résumé

L'isolation est **stricte par défaut**, avec contrôle granulaire des accès.

---

## Sandboxing sur Android

### 📌 Comment ça marche

* Android utilise aussi une sandbox pour chaque application, mais elle est construite **au-dessus du noyau Linux** (chaque application a un UID utilisateur unique).
* Par défaut, une app ne voit pas les données d'une autre app ni les ressources système, sauf si l'utilisateur l'autorise via un **système de permissions**.

### 📌 Effets pratiques

* L'accès aux fonctionnalités sensibles (microphone, localisation, contacts…) se fait via des **permissions demandées** à l'installation ou à l'exécution.
* Android permet souvent **plus de flexibilité fonctionnelle** (par exemple, partages inter-app plus souples) à condition d'obtenir les permissions nécessaires.

### 👉 En résumé

Android applique aussi l'isolation, mais l'accent est souvent mis sur les **permissions utilisateur** plutôt que l'isolation stricte par défaut.

---

## Tableau comparatif

| Élément | iOS | Android |
|---------|-----|---------|
| **Isolation stricte** | Apps isolées dans leur sandbox avec accès très restreint par défaut | Chaque app a son sandbox via UID Linux, mais certains accès peuvent être débloqués via permissions |
| **Permissions utilisateur** | Permissions explicites requises pour accéder aux ressources sensibles (caméra, localisation, etc.) | Permissions similaires, mais l'utilisateur peut parfois accorder plus de contrôle ou les annuler après installation |
| **Signature obligatoire** | Oui, Apple exige des apps signées | Non obligatoire (APK peuvent être installés hors Play Store si autorisé) |
| **Approche système** | Sandbox fortement reliée à l'écosystème Apple fermé | Sandbox basée sur Linux + permissions étendues |

---

## Résumé objectif

### Points communs

**iOS et Android isolent tous les deux les apps dans des sandboxes** pour empêcher l'accès non autorisé aux données d'autres apps ou ressources système.

### Différences principales

La différence principale réside dans **comment cette isolation est contrôlée et étendue** :

#### iOS
* L'isolation est généralement **plus stricte par défaut**
* Écosystème **fermé** avec contrôle centralisé
* Permissions centrées sur l'utilisateur et la **signature Apple obligatoire**
* Moins de flexibilité, mais plus de sécurité par défaut

#### Android
* L'isolation repose sur le **système d'utilisateurs Linux**
* Permissions installées/accordées par l'utilisateur avec **plus de souplesse**
* Possibilité d'installer des apps hors du store officiel
* **Plus de responsabilités pour l'utilisateur** en termes de sécurité