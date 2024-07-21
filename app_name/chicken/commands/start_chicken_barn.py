from random import randint
from flask import current_app as app
from app_name.chicken.data.mock_chickens import mock_chickens
from app_name.chicken.models.chicken import Chicken

@app.cli.command("start-chicken-barn")
def start_chicken_barn() -> None:
    """
        mocks a couple of chickens to start
        your barn.
    """
    current = Chicken.find()
    if len(current) > 0: return
    chickens = mock_chickens(randint(1,4))
    print(f">>> 🐔 chicken barn started with {len(chickens)} chickens!")
