from brownie import AdvancedCollectable
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3

## Extra parametosrs (string memory tokenURI)
def main():
    account = get_account()
    _AdvancedCollectable = AdvancedCollectable[-1]
    fund_with_link(_AdvancedCollectable.address, amount=Web3.toWei(0.1, "ether"))
    creating_tx = _AdvancedCollectable.createollectable({"from": account})
    creating_tx.wait(1)
    print("😘😘😘New tokken has been created")
