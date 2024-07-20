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
