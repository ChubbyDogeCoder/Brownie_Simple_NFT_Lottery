# def test_get_breed():
#     # Arrange / Act
#     breed = get_breed(0)
#     # Assert
#     assert breed == "PUG"


from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
)
from brownie import network, AdvancedCollectable
import pytest
from scripts.Advanced_Collecatble.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for loca testing lool")

    _simple_collectable, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["requestedCollecatble"]["requestId"]
    random_number = 666
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, 666, _simple_collectable.address, {"from": get_account()}
    )

    assert _simple_collectable.tokenCount() == 1
    assert _simple_collectable.tokenIdToBreed(0) == random_number % 3
