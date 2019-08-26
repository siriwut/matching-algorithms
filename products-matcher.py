
example_product1 = {
    'name': 'Louis Vuitton Super Bag - Marvel Endgame Model',
    'image': 'https://img.com/louis-vuitton-marvel',
    'price': 9999.99,
    'attributes': {
        'brand': 'Louis Vuitton',
        'color': 'Red',
        'model_number': 'A1234',
    }
}

example_product2 = {
    'name': 'Chanel Perfume - Number Four',
    'image': 'https://img.com/chanel-perfume-number-four',
    'price': 7999.99,
    'attributes': {
        'brand': 'Chanel',
        'color': 'Brown',
        'model_number': 'C1234',
    }
}


# algorithm sudo code
def match_products(product1, product2):
    similar_name_value = similar_name(product1['name'], product2['name']))
    similar_image_value = similar_image(product1['image'], product2['image']))
    similar_price_value = similar_price(product1['price'], product2['price']))
    similar_attributes_value = similar_attributes(product1['attributes'], product2['attributes']))

    if average_values(
        similar_name_value,
        similar_image_value,
        similar_price_value,
        similar_attributes_value
    ) >= 0.5: #tuning value
        return true #matched

    return false #mismatched

class ProductsPool:
    def __init__(self, products):
        self.products = products

    def __random():
        #random products...
        return result_products

    def release(self):
        if self.products !== empty:
            result = self.__random()
            return result
    return nil

class ProductsPoolManager:
    def __init__(self):
        self.products_pools = []

    def load_products(products):
        self.products_pools.append(
            ProductsPool(products)
        )

    def release(self):
        #process something...
        return products_pool_result.release()


def main():
    
