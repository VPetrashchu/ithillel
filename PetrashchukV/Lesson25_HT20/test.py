import requests
from PetrashchukV.Lesson25_HT20.infrastructure import Phone

#GET_1 request test
def test_check_phone_listing(phone):
    list_of_phones = phone.get_list_of_all_objets()
    assert list_of_phones.status_code == 200
    print(list_of_phones.json())

#GET_1.1 request test
def test_check_phone_listing1(phone):
    list_of_phones = phone.get_list_of_all_objets()
    assert list_of_phones.status_code == 200
    assert isinstance(list_of_phones.json(), list)

#GET_2 request test
def test_check_single_phone(phone):
    single_phone = phone.get_single_phone(10)
    assert single_phone.status_code == 200
    print(single_phone.json())

#GET_2.1 request test
def test_check_single_phone1(phone):
    single_phone = phone.get_single_phone(10)
    assert single_phone.status_code == 200
    assert 'name' in single_phone.json()

#POST_1 request test
def test_create_phone_with_default_value1(phone):
    default_phone = phone.create_single_default_object()
    assert default_phone.status_code == 200
    assert 'id' in default_phone.json()

#POST_New request test
def test_create_phone_with_default_value(phone):
    default_phone = phone.create_single_default_object()
    print(default_phone.json())
    assert default_phone.status_code == 200

# PUT request test
def test_update_phone_with_id():
    phone = Phone()
    response = phone.update_phone_new(device_id='ff8081818f1bcc43018f262ae5a411df')
    assert response.status_code == 200
    assert response.json()['data']['year'] == 2021
    assert response.json()['data']['price'] == 2055.99

#GET, checking previosly PUT request
def test_check_single_phone(phone):
    single_phone = phone.get_single_phone('ff8081818f1bcc43018f262ae5a411df')
    assert single_phone.status_code == 200
    print(single_phone.json())

# PATCH request test
def test_partial_update_phone(phone):
    updated_name = phone.updated_data["name"]
    single_phone = phone.partial_update_phone('ff8081818f1bcc43018f262ae5a411df')
    assert single_phone.status_code == 200
    assert single_phone.json()['name'] == updated_name
    print(single_phone.json())

# DELETE request test
def test_check_single_phone1(phone):
    single_phone = phone.get_single_phone('ff8081818f1bcc43018f262ae5a411df')
    assert single_phone.status_code == 200
    assert 'name' in single_phone.json()


#Creating new request and update some data
def test_create_phone_and_update_with_id(phone):
    create_phone_response = phone.create_single_default_object()
    assert create_phone_response.status_code == 200
    assert 'id' in create_phone_response.json()
    phone_id = create_phone_response.json()['id']
    update_phone_response = phone.update_phone_with_created_id()
    assert update_phone_response.status_code == 200
    assert update_phone_response.json()['data']['year'] == 2021
    assert update_phone_response.json()['data']['price'] == 2055.99

#Take new data after creating and updating some previously data
def test_get_created_phone(phone):
    create_phone_response = phone.create_single_default_object()
    assert create_phone_response.status_code == 200
    assert 'id' in create_phone_response.json()
    phone_id = create_phone_response.json()['id']
    get_phone_response = phone.get_single_phone(device_id=phone_id)
    assert get_phone_response.status_code == 200
    created_phone_data = get_phone_response.json()
    assert created_phone_data['name'] == phone.default_phone_data['name']
    assert created_phone_data['data']['year'] == phone.default_phone_data['data']['year']
    assert created_phone_data['data']['price'] == phone.default_phone_data['data']['price']
    assert created_phone_data['data']['CPU model'] == phone.default_phone_data['data']['CPU model']
    assert created_phone_data['data']['Hard disk size'] == phone.default_phone_data['data']['Hard disk size']
    print(get_phone_response.json())

