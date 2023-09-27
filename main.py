from db import QueryManager
from API import RequestManager

def main():
    query_manager = QueryManager()
    request_manager = RequestManager()

    categories = request_manager.get('/products/categories')
    query_manager.insert_categories(categories)

if __name__ == '__main__':
    main()