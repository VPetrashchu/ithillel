from PetrashchukV.Lesson28_HT22.api_sql_adapter import ApiSqlAdapter


adapter = ApiSqlAdapter(api_endpoint="https://api.restful-api.dev/objects")

# Test POST+GET => INSERT+SELECT
data = {
    "name": "Apple MacBook Pro 16",
    "description": "Description of MacBook Pro 16",
    "category": "Laptops",
    "price": 1849.99,
    "quantity": 1
}

inserted_id = adapter.post_object(data)
print("Inserted object id:", inserted_id)


# Test PUT+GET => UPDATE+SELECT
update_data = {
    "name": "Apple MacBook Pro 16",
    "description": "Description of MacBook Pro 16",
    "category": "Laptops",
    "price": 1849.99,
    "quantity": 1
}
updated_object = adapter.put_object(inserted_id, update_data)
retrieved_updated_object = adapter.get_object(inserted_id)
print("Updated object:", retrieved_updated_object)

adapter.close_connection()

