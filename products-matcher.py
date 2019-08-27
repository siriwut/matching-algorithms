
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
        return True #matched

    return False #mismatched

def process_matching_product(products):
    matched_products = []

    while size(products) !== 0 :
       couple = get_couple(products)

       if match_products(couple['product1'], couple['product2']) === True:
           matched_products.push([couple['product1'], couple['product2']])

    return matched_products


class ProductsPool:
    def __init__(self, products):
        self.products = products

    def __random(self):
        products_result = random(self.products) #do some random algorithm
        return products_result

    def release(self):
        if size(self.products) !== 0:
            products_result = self.__random(self.products)
            return products_result
        return None

    def is_empty(self):
        if size(self.products) === 0:
            return True
        return False


class ProductsPoolManager:
    def __init__(self):
        self.products_pools = []

    def fill_products(products):
        self.products_pools.append(
            ProductsPool(products)
        )

    def release(self):
        products_pool_result = get_pool(self.products_pools)

        return products_pool_result.release()

    def is_empty():
        if size(self.products_pools) === 0:
            return True
        return False



def main():
    db = DB()
    i = 0
    loop_times = 5
    pool_manager = ProductsPoolManager()
    matched_products = []

    while i < loop_times: #run multiple times to get most acculately matched products
        while db.Cursor.is_end !== True :
            products = db.Cursor.quantiy(2000).Product.get()
            pool_manager.fill_products(products)

        while pool_manager.is_empty() !== true :
             products = pool_manager.release()
             matched_results = process_matching_products(products)

             matched_products.push(matched_results)
        i++




    db.MatchedProducts.save(matched_products)
