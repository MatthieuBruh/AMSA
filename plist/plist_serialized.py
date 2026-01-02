import nska_deserialize

# Charger le fichier avec nska_deserialize et en tenant compte des UIDs
# TODO : changer le path pour la valeur souhaitée
with open("path/MyDaySeverDataHelper%2EallDayTimeline", "rb") as f:
    # Désérialiser le fichier
    data = nska_deserialize.deserialize_plist(f)
    # TODO : à adapter selon les besoins
    value = data["allDayRespirationKey"]["respirationValuesArray"][0]["value"]
    print(value)


# Charger le fichier avec nska_deserialize et en tenant compte des UIDs
# TODO : changer le path pour la valeur souhaitée
'''
with open("path/MyDaySeverDataHelper%2EallDayTimeline", "rb") as f:
    # Désérialiser le fichier
    data = nska_deserialize.deserialize_plist(f)
    TriggerTime = 1692018120000
    # TODO : à adapter selon les besoins
    HeartRateValues = data["allDayHeartRateKey"]["heartRateValues"]
    for HeartRate in HeartRateValues:
        if HeartRate[0] == TriggerTime:
            print(HeartRate[1])
'''