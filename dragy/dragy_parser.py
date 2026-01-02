import csv
import tempfile

from pathlib import Path
from datetime import datetime, timezone

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from pyubx2 import UBXReader

# Install requirements and change filepath and outpath in man block and the end

KEY = b"\x69\x32\x46\x6c\x65\x5a\x6e\x64\x00\x00\x00\x00\x00\x00\x00\x00"
IV = b"\x69\x33\x65\x76\x38\x6c\x65\x6e\x00\x00\x00\x00\x00\x00\x00\x00"

def pull_from_phone():
    pass


def decrypt(filepath):
    for file in filepath:
        with open(file, 'rb') as ubx_file:
            header = ubx_file.read(2)
        if header == b"\xB5\x62":
            yield file

        with open(file, "rb") as f:
            ciphertext = f.read()

        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with tempfile.NamedTemporaryFile(suffix=".udx") as temp:
            temp.write(plaintext)

            yield temp.name


def main(filepath, out_path):
    #pull_from_phone()
    filepath = decrypt(filepath)

    for file in filepath:
        parse(file, out_path)


def parse(file, out_path):
    with open(file, 'rb') as ubx_file, open(out_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=";", quoting=csv.QUOTE_NONNUMERIC,
                                fieldnames=["Type",
                                            "TimeStamp", "DateTime (UTC-0)", "iTOW",
                                            "Latitude", "Longitude", "Horizontal Accuracy [m]",
                                            "Height [m]", "Height Accuracy [m]",
                                            "Speed [m/s]", "Speed Accuracy [m/s]",
                                            "Heading", "Heading accuracy",
                                            "FixType", "pDOP",
                                            "NumSV"])
        writer.writeheader()

        content = ubx_file.read()
        messages = [b"\xB5\x62" + e for e in content.split(b"\xB5\x62") if e != b""]
        pass

        for message in messages:
            try:
                m = UBXReader.parse(message)
            except Exception:
                continue

            if m.identity != "NAV-PVT":
                continue

            data = {}

            data["Type"] = m.identity

            timestamp = datetime(m.year, m.month, m.day, m.hour, m.min, m.second, tzinfo=timezone.utc)
            data["TimeStamp"] = timestamp.timestamp() + m.nano / 1e9
            data["DateTime (UTC-0)"] = timestamp.strftime("%Y-%m-%d %H:%M:%S.") + f"{int(m.nano / 1e6):03d}"
            data["iTOW"] = m.iTOW

            data["Latitude"] = m.lat
            data["Longitude"] = m.lon
            data["Horizontal Accuracy [m]"] = m.hAcc / 1000
            data["Height [m]"] = m.hMSL / 1000
            data["Height Accuracy [m]"] = m.vAcc / 1000
            data["Speed [m/s]"] = m.gSpeed / 100
            data["Speed Accuracy [m/s]"] = m.sAcc / 100
            data["Heading"] = m.headMot
            data["Heading accuracy"] = m.headAcc
            data["FixType"] = m.fixType
            data["pDOP"] = m.pDOP
            data["NumSV"] = m.numSV

            writer.writerow(data)

if __name__ == '__main__':
    filepath = [Path(r"data/DRAG_20251023_094740_380878640.ebin"), ]
    out_path = Path(r"results/test.csv")
    main(filepath, out_path)
