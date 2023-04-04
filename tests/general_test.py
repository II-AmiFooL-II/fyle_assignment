def test_unavilable_api(client):
    response = client.post(
            '/qwert',
            )
    error_response = response.json
    assert response.status_code == 404

def test_home(client):
    response = client.get(
            '/',
            )
    assert response.status_code == 200
