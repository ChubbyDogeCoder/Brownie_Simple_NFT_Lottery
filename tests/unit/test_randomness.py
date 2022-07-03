# // ### 2 be completed later


from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
)
from brownie import network, config, _Random_Nb

# config["networks"][network.show_active()]["keyhash"],
# config["networks"][network.show_active()]["fee"],
def test_rando():
    account = get_account()
    txx = _Random_Nb.getRandomNumber({"from": account})
    txx1 = txx.fulfillRandomness()
    print(f" this is the nb?? \n {txx1}")
