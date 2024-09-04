def calculate_final_price(base_price, discount_percentage, tax_rate):
    """Calcula o preço final após aplicar o desconto e o imposto."""
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("O percentual de desconto deve estar entre 0 e 100")
    if tax_rate < 0:
        raise ValueError("A taxa de imposto deve ser positiva")

    discount_amount = base_price * (discount_percentage / 100)
    discounted_price = base_price - discount_amount
    tax_amount = discounted_price * tax_rate
    final_price = discounted_price + tax_amount

    return round(final_price, 2)



def get_currency_symbol():
    return "USD$"  # Probar pragma: no mutate
