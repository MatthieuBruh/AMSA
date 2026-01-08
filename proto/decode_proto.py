import blackboxprotobuf

# TODO : changer nom fichier
with open ('./amsa_data', 'rb') as f:
    record_data = f.read()

data, _ = blackboxprotobuf.decode_message(record_data)
print(data)