from orders import orders_pages # Flask instance of the API

def test_index_route():
    response = 200

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Testing, Flask!'