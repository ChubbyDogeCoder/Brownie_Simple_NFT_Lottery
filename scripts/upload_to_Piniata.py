from brownie import config
import os, requests
from pathlib import Path


PINIATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath0 = "./img/st-bernard.png"
filename0 = filepath0.split("/")[-1:][0]

filepath1 = "./img/st-bernard.png"
filename1 = filepath1.split("/")[-1:][0]


# Alternative way using brownie config

### First Method
# headers = {
#     "pinata_api_key": config["Piniata"]["public_key"],
#     "pinata_secret_api_key": config["Piniata"]["Secret_key"],
# }

### Second Method
headers = {
    "pinata_api_key": config["wallets"]["public_key"],
    "pinata_secret_api_key": config["wallets"]["Secret_key"],
}

##  Third Method
# headers = {
#     "pinata_api_key": os.getenv("API_KEY_PINIATA"),
#     "pinata_secret_api_key": os.getenv("SECRET_API_KEY_PINIATA"),
# }


def do_the_thingy_wingy(filepath, filename):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINIATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(f"jeez that was willd and new 😏😏😏😏🤑🤑\n{response.json()}")


def main():
    do_the_thingy_wingy(filepath0, filename0)
    do_the_thingy_wingy(filepath1, filename1)
