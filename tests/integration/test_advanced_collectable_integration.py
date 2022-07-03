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
import pytest, time
from scripts.Advanced_Collecatble.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing lool")

    _simple_collectable, creation_transaction = deploy_and_create()

    time.sleep(60)

    assert _simple_collectable.tokenCount() == 1
