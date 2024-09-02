import pytest

from src.inventory_manager import InventoryManager


@pytest.fixture
def inventory():
    inv = InventoryManager()
    inv.add_product("Apple", 10)
    return inv


def test_add_product(inventory):
    inventory.add_product("Banana", 5)
    assert inventory.inventory["Banana"] == 5


def test_sell_product(inventory):
    assert inventory.sell_product("Apple", 5) is True
    assert inventory.inventory["Apple"] == 5


def test_sell_product_not_enough_stock(inventory):
    assert inventory.sell_product("Apple", 15) is False


def test_check_stock(inventory):
    assert inventory.check_stock("Apple") is True
    assert inventory.check_stock("Banana") is False


# TODO: ------- DESCOMENTAR ESTA SECCION PARA MATAR A LOS MUTANTES 👾 -------


# # Este test nos da la cobertura del 100%
# def test_add_product_already_exists_adds_quantity_correctly(inventory):
#     original_quantity = inventory.inventory["Apple"]
#     add_quantity = 5
#     inventory.add_product("Apple", add_quantity)
#     assert (
#         inventory.inventory["Apple"] == original_quantity + add_quantity
#     ), "The quantity of the product should correctly increase when it already exists"


# def test_sell_product_exact_stock(inventory):
#     assert inventory.sell_product("Apple", 10) is True
#     assert inventory.inventory["Apple"] == 0


# def test_check_stock_returns_true_for_single_item(inventory):
#     inventory.add_product("SingleItem", 1)
#     assert inventory.check_stock("SingleItem") is True, "Should return True for 1 item in stock"
