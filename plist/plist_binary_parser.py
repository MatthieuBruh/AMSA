import plistlib

# Ouvrir et lire un fichier plist binaire
# TODO : Changer data.plist avec le nom du fichier
with open('data.plist', 'rb') as file:
    data = plistlib.load(file, fmt=plistlib.FMT_XML)
    print(data)