import os
import time
import CoT

ATAK_IP = os.getenv('ATAK_IP', '10.0.0.104')
ATAK_PORT = int(os.getenv('ATAK_PORT', '4242'))
ATAK_PROTO = os.getenv('ATAK_PROTO', 'TCP')

params = {  # SWX parking lot
    "lat": 38.8892687,
    "lon": -77.0518607,
    "uid": "MSRS",
    "identity": "hostile",
    "dimension": "land-unit",
    "entity": "military",
    "type": "U-C"
#    "type": "U-C-R-H"
}

for i in range(0, 10):
    #    params["lat"] = params["lat"] + i/10000.0
    #    params["lon"] = params["lon"] + i/10000.0
    print("Params:\n" + str(params))
    cot = CoT.CursorOnTarget()
    cot_xml = cot.atoms(params)

    print("\nXML message:")
    print(cot_xml)

    print("\nPushing to ATAK...")
    if ATAK_PROTO == "TCP":
        sent = cot.pushTCP(ATAK_IP, ATAK_PORT, cot_xml)
    else:
        sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_xml)
    print(str(sent) + " bytes sent to " + ATAK_IP + " on port " + str(ATAK_PORT))
    time.sleep(2)