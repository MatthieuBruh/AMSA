import hashlib
## Entrer Domaine-Chemindufchier
# A UTILISER UNIQUEMENT SI MANIFEST.DB PAS DISPO !!
string = "HealthDomain-Health/healthdb_secure.sqlite"
string1 = string.encode("utf-8")
print(hashlib.sha1(string1).hexdigest())
print("Les deux premiers caractères correspondent au chemin d'accès du fichier en Backup Itunes")