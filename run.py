import os
from app_name.app import create_app

app = create_app()

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    print(f">>> ✅ app is up & listening on port {port}")
    app.run(host="0.0.0.0", port=port)
