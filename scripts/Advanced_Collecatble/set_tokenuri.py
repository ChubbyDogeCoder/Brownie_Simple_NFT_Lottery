from brownie import AdvancedCollectable, network
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

dog_metadata_dictonnary = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    _advanced_collectible = AdvancedCollectable[-1]
    number_of_advanced_collecatbles = _advanced_collectible.tokenCount()
    print(
        f" 🍨🍨 You have created :::::  {number_of_advanced_collecatbles}  :::: items of AdvancedCollectable "
    )
    for token_id in range(number_of_advanced_collecatbles):
        breed = get_breed(_advanced_collectible.tokenIdToBreed(token_id))
        if not _advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"\n\n🎏🎏🎏Setting the tokk URI of  {token_id}\n\n")
            set_tokenURI(
                token_id, _advanced_collectible, dog_metadata_dictonnary[breed]
            )


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    _txx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    _txx.wait(1)
    print("Waiting for Metadeata refersh take up to 20 mins \n ")
    print(
        f"🎇🎇🎇🎇 AWesom, you can now view you NFT at {OPENSEA_URL.format(network.show_active(), nft_contract.address, token_id)} \n🎉🎉🎉🎉\n\n\n"
    )
