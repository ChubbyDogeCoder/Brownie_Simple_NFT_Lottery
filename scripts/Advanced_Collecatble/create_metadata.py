from brownie import AdvancedCollectable, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests, json, os


breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def main():
    _advanced_collectible = AdvancedCollectable[-1]
    number_of_advanced_collecatbles = _advanced_collectible.tokenCount()
    print(
        f" 🍨🍨 You have created :::::  {number_of_advanced_collecatbles}  :::: items of AdvancedCollectable "
    )
    for token_id in range(number_of_advanced_collecatbles):
        breed = get_breed(_advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectable_metadata = metadata_template
        print(f" Ice cream 🧊🧊 {metadata_file_name}")
        if Path(metadata_file_name).exists():
            print(f" THe 🌰🌰 {metadata_file_name} alreay eists. DElETE it to OVERWRITE")
        else:
            print(f" Creatiung metadatafie: {metadata_file_name}  💨💨💨")
            collectable_metadata["name"] = breed
            collectable_metadata["description"] = f"an Adorrorabe {breed} puug"
            image_file_path = "./img/" + breed.lower().replace("_", "-") + ".png"

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_IIPF(image_file_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]

            collectable_metadata["image"] = image_uri
            print(
                f"Tjis is the result of 'collectable_metadata' \n\n\n 💫💫💫💫💫💫\n {collectable_metadata}"
            )
            with open(metadata_file_name, "w") as file:
                json.dump(collectable_metadata, file)

            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_IIPF(metadata_file_name)

            print(
                f"Tjis is the result of 'metadata_file_name' \n\n\n 🐱‍🏍🐱‍🏍🐱‍🏍🐱‍🏍🐱‍🏍🐱‍🏍\n {metadata_file_name}"
            )


def upload_to_IIPF(image_file_path):
    with Path(image_file_path).open("rb") as fp:
        image_binary = fp.read()
        # Upload part on IPFS
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]

        # CoolAss PY FUnction ; From: "./img/xxx.png" => "xxx.png"
        filename = image_file_path.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(f"This the final result tadaa ! 💟💟🚀🚀\n{image_uri}")
        return image_uri
