import requests

url = 'http://localhost:5000/add_product'
data = {
    'name': 'New Product',
    'price': 29.99,
    'description': 'Description of the new product',
    'image': 'product_image.jpg',
    'category': 'New Category'
}

response = requests.post(url, json=data)
print(response.json())
