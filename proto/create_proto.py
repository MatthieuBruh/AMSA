# Encodez un fichier :
# 1. protobuf==3.10.0
# 2. pip install grpcio-tools
# 3. python -m grpc_tools.protoc -I. --python_out=. .\amsa.proto
# 4. Exécutez ce code :

import amsa_pb2

msg = amsa_pb2.amsa()
msg.nom_du_cours = "Algorithmique"
msg.year = 2026

with open("amsa_data", "wb") as f:
    f.write(msg.SerializeToString())