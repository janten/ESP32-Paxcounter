#!/usr/bin/python3

import requests
import json

Application = "paxcounter-haltern-01"
APIKey = "NNSXS.KC3536QMBFD6APDTMBE34HVXZCG5M5BIJQKVOTY.OMMRP5TYPVLFWHV54QDPUEZBPIZRSITHJUJURP7MSBFCN4QRHH4A"
Fields = "up.uplink_message.decoded_payload,up.uplink_message.frm_payload"
NumberOfRecords = 30
URL = "https://eu1.cloud.thethings.network/api/v3/as/applications/" + Application + "/packages/storage/uplink_message?order=-received_at&limit=" + str(NumberOfRecords) + "&field_mask=" + Fields
Header = { "Accept": "text/event-stream", "Authorization": "Bearer " + APIKey }

print("\n\nFetching from data storage...\n")

r = requests.get(URL, headers = Header)

print("URL: {}\n".format(r.url))
print("Status: {}\n".format(r.status_code))
print("Response: {}\n".format(r.text))
print("JSON: ")
print(json.dumps(json.loads(JSON), indent = 4))
print()