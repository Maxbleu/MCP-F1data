import os, requests

def launch_request_f1db(path: str):
    headers = {"Authorization": f"Bearer {os.getenv("JWT_TOKEN")}"}
    response = requests.get(url=f"https://apif1db-production.up.railway.app/api/{path}",headers=headers)
    if response.status_code == 200:
        json = response.json()
        return json