import pytest
from app_name.chicken.models.css_color import CSSColor

def test_get_all_valid_css_colors(client):
    """
        tests user may get all valid css
        color names to create livestock animals.
    """
    response = client.fetch(
        method="get",
        path="css-colors"
    )
    assert response.status_code == 200
    assert len(response.json) == len(CSSColor.list_color_names())
    assert "yellowgreen" in list(map(
        lambda colorObject: colorObject["value"],
        response.json
    ))
