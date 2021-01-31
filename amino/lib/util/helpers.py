import re
import json
import base64
from secrets import token_hex

def generate_device_info():
    # I'm still trying to figure out how to generate the device id. So far, decompilation is proving difficult,
    # so sniffed values are being used
    return {
        "device_id": "01B592EF5658F82E1339B39AA893FF661D7E8B8F1D16227E396EF4B1BF60F33D25566A35AB1514DAB5",
        "device_id_sig": "AaauX/ZA2gM3ozqk1U5j6ek89SMu",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)"
    }

def decode_base64(data: str):
    data = re.sub(rb'[^a-zA-Z0-9+/]', b'', data.encode())[:162]
    return base64.b64decode(data + b'=' * (-len(data) % 4)).decode("cp437")[1:]

def sid_to_uid(SID: str):
    return json.loads(decode_base64(SID))["2"]

def sid_to_ip_address(SID: str):
    return json.loads(decode_base64(SID))["4"]