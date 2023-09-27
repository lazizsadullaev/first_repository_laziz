import requests

class RequestManager:
    base_url = 'https://fakestoreapi.com'

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url)
        return response.json()


request_manager = RequestManager()
categories = request_manager.get('/products/categories')
products = request_manager.get('/products')
# print(products)

