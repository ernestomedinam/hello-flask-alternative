import os
import sys
from app_name.app import create_app


if __name__ == "__main__":
    import psycopg2
    try_again = True
    while try_again == True:
        host = os.environ.get("POSTGRES_HOST")
        port = os.environ.get("POSTGRES_PORT")
        user = os.environ.get("POSTGRES_USER")
        password = os.environ.get("POSTGRES_PASSWORD")
        db_name = os.environ.get("POSTGRES_DB")
        connection = None
        try: 
            connection = psycopg2.connect(f"host={host} port={port} user={user} password={password} dbname={db_name}")
            connection.close()
            try_again = False
        except psycopg2.OperationalError as error:
            print(f"\n>>> 📛 psql connection failed...: {error}")
            print(">>> 😯 there seems to be an issue with postgresql connection; make sure the service is available and check your environment variables.")
            choice: str = input(">>> 🤓 once you've checked press any key and/or hit 'Enter' to try again, or type 'q' and hit 'Enter' to quit... for now:\n")
            if choice.strip() == "q":
                sys.exit("\n>>> ciao! 😎")

    app_port = os.environ.get("PORT", 5000)
    environment = os.environ.get("ENV", "development")
    app = create_app()
    print(f">>> ✅ starting app & setting up api to listen on port {app_port}")
    app.run(
        host="0.0.0.0", 
        port=app_port, 
        debug=False if environment == "production" else True
    )
