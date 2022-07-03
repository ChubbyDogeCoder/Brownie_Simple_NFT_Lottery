from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedCollectable, network, config

active = network.show_active()


def deploy_and_create():
    account = get_account()
    _AdvancedCollectable = AdvancedCollectable.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print(f"Account deployed at this addess ...  🤨🤨🤨  {_AdvancedCollectable}")

    random_number = fund_with_link(_AdvancedCollectable.address)
    print(f"this is the random number 🤖🤖🤖🤖: {random_number}")

    creating_tx = _AdvancedCollectable.createollectable({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    print("Waiting for Metadeata refersh take up to 20 mins ;) ")

    print(
        f"greaat, your NFT is vieable at {OPENSEA_URL.format(network.show_active(), _AdvancedCollectable.address, _AdvancedCollectable.tokenCount() - 1)}"
    )

    return _AdvancedCollectable, creating_tx

    # tx = _AdvancedCollectable.createollectable(sample_token_uri, {"from": account})
    # tx.wait(1)


def main():
    deploy_and_create()
