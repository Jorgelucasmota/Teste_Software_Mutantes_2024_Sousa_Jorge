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


# Este teste nos dá 100% de cobertura
def test_add_product_already_exists_adds_quantity_correctly(inventory):
    quantidade_original = inventory.inventory["Apple"]
    quantidade_adicionada = 5
    inventory.add_product("Apple", quantidade_adicionada)
    assert (
        inventory.inventory["Apple"] == quantidade_original + quantidade_adicionada
    ), "A quantidade do produto deve aumentar corretamente quando ele já existe"

def test_sell_product_exact_stock(inventory):
    assert inventory.sell_product("Apple", 10) is True
    assert inventory.inventory["Apple"] == 0

def test_check_stock_returns_true_for_single_item(inventory):
    inventory.add_product("SingleItem", 1)
    assert inventory.check_stock("SingleItem") is True, "Deve retornar True para 1 item em estoque"
