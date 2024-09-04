import pytest

from src.discount_processor import calculate_final_price, get_currency_symbol


@pytest.mark.parametrize(
    "base_price, discount_percentage, tax_rate, expected",
    [
        (100, 0, 0, 100),  # Caso trivial
        (100, 10, 0.1, 99),  # Caso estándar
        (100, 0, 0.1, 110),  # Sin descuento
        (100, 10, 0, 90),  # Sin impuestos
    ],
)
def test_calculate_final_price(base_price, discount_percentage, tax_rate, expected):
    assert (
        calculate_final_price(base_price, discount_percentage, tax_rate) == expected
    ), "Calcula el precio final correcto"


# Verifica que se lance una excepción para un porcentaje de descuento inválido
@pytest.mark.parametrize("discount_percentage", [-1, 101])
def test_invalid_discount_percentage_raises_error(discount_percentage):
    with pytest.raises(ValueError):
        calculate_final_price(100, discount_percentage, 0.1)


# Verifica que se lance una excepción para una tasa de impuesto negativa
def test_negative_tax_rate_raises_error():
    with pytest.raises(ValueError):
        calculate_final_price(100, 10, -0.1)


def test_get_currency_symbol():
    assert get_currency_symbol() == "USD$"

# Mutante 3
# Este mutante altera a condição de discount_percentage > 100 para discount_percentage >= 100.
# Para eliminá-lo, você precisa de um teste que verifique especificamente que um percentual de
# desconto exatamente igual a 100 é tratado corretamente pelo seu código.
def test_discount_percentage_of_exactly_100_is_valid():
    # Assegura que um desconto de 100% reduz o preço base a 0 antes de aplicar o imposto
    # O resultado esperado dependerá de como você deseja lidar com o imposto nesse caso
    final_price = calculate_final_price(100, 100, 0.1)
    expected_price = 0  # Assumindo que o imposto não é aplicado sobre um preço base de 0
    assert final_price == expected_price, "Um desconto de 100% deve reduzir o preço a 0 antes do imposto"

# Mutante 6
# Este mutante altera a mensagem de erro para um percentual de desconto inválido.
# Para eliminá-lo, você precisa de um teste que verifique a mensagem de erro exata.
def test_invalid_discount_percentage_error_message():
    with pytest.raises(ValueError) as exc_info:
        calculate_final_price(100, 101, 0.1)
    assert str(exc_info.value) == "O percentual de desconto deve estar entre 0 e 100"

# Mutante 9
# Similar ao mutante 10, mas para a taxa de imposto. Você precisa verificar a mensagem
# de erro para uma taxa de imposto negativa.
def test_negative_tax_rate_error_message():
    with pytest.raises(ValueError) as exc_info:
        calculate_final_price(100, 10, -0.1)
    assert str(exc_info.value) == "A taxa de imposto deve ser positiva"

# Mutante 20
# Este mutante altera a precisão do arredondamento de 2 para 3 casas decimais.
# Para eliminá-lo, você pode adicionar um teste que verifique que o arredondamento
# é realizado corretamente para duas casas decimais.
def test_rounding_to_two_decimals():
    # Usar um preço, desconto e taxa de imposto que resultem em um valor não arredondado diretamente para duas casas decimais.
    assert calculate_final_price(100, 10, 0.12345) == 101.11

# Incorporando esses testes adicionais, você deve ser capaz de "eliminar" os mutantes sobreviventes e, portanto,
# melhorar a cobertura e a robustez dos seus testes unitários.

