import pytest 

def test_get_all_chickens(client, chicken_factory):
    """
        tests chickens resource for get method
        with no querystring in order to get all
        chickens in the barn.
        each chicken should be a json dictionary: {
            "name": str,
            "id": int,
            "color": (str, str),
            "traits": list({
                "trait": str,
                "order": int,
                "chicken_id": int
            })
        }
    """
    chickens = chicken_factory(5)
    response = client.fetch(
        method="get",
        path="chickens"
    )
    assert response.status_code == 200
    assert len(response.json) == len(chickens)

def test_create_a_chicken(client):
    """
        tests a chicken can be created using
        post method on chickens resource.
        request body includes name and color: {
            "name": str,
            "color": str
        }
    """
    response = client.fetch(
        method="post",
        path="chickens",
        json={
            "name": "test chicken",
            "color": "yellowgreen"
        }
    )
    assert response.status_code == 201
    assert response.json["name"] == "test chicken"
    assert len(response.json["color"]) == 2
    assert response.json["color"][0] == "yellowgreen"
    assert "id" in response.json
