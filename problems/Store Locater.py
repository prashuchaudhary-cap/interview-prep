Models
User 
Lat 
Lng
Name
Email


Product
- name
- image
- category_id
Store
Lat
Lng

StoreItem
store_id
Product_id
quantity

Product Category
name
 

API
categories/
Categories index API to fetch all categories
 This data should be cached into any memory store

	
HTTP GET - /products?category_id=121&page=0&size=10
Headers: {
	Auth: “dafasfdsdsfsfd”
}
Response - 
{
	status: 200,
	count: 100,
	products: [
		“Name”: Nike
		“Image”: image.com/nike
		“Stores”: [
			{
				“Name”: Store name
				“Distance”: “100”
				“Distance_unit”: “meters”
}
]
]
}


MySQL
	

Product_repo - 

	Create 

	GET 
	Update
	Delete
	Search

product_Interactor



function(category, page, size, user) => [product, [store]]
products = Get list of products for this category  
Stores - pass user lat lng and product ids to Database. Do calculation for 
	

Select 
Store.name, 
COMPUTE_DISTANCE(store.lat, store.lng, user.lat, user.lng) as distance
from 
stores 
inner join store_items on store_items.store_id = store.id 
where store_items.product_id in (products_ids) 
And store_items.quantity > 1
AND COMPUTE_DISTANCE(store.lat, store.lng, user.lat, user.lng) as distance < 5000 group by store_items.product_id


COMPUTE_DISTANCE returns a float, not an boolean
Stores does not have product_id on the table
Group by means everything in select should either be product_id or an aggregate (ex: count)

// What happens here?

Identify which zone/center user lies in based on his lat-long
Cache[Indiranagar_Zone] = Stores from center of indiranagar
filter these stores based on the proximity of the user and return 

