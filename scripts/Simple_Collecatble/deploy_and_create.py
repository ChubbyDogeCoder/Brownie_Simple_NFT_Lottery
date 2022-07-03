from scripts.helpful_scripts import get_account, network, OPENSEA_URL
from brownie import SimpleCollectable

active = network.show_active()


sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    deploy_and_create()


def deploy_and_create():
    account = get_account()
    _SimpleCollectable = SimpleCollectable.deploy({"from": account})
    tx = _SimpleCollectable.createCollectable(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"greaat, your NFT is vieable at {OPENSEA_URL.format(network.show_active(), _SimpleCollectable.address, _SimpleCollectable.tokenCounter() - 1)}"
    )
    print("Waiting for Metadeata refersh take up to 20 mins ;) ")
    return _SimpleCollectable
