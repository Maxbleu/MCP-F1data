import os, requests

def launch_request_f1db(path: str):
    headers = {
        "Authorization": f"Bearer {os.getenv("JWT_TOKEN")}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        response = requests.get(
            url=f"https://apif1db-production.up.railway.app/api{path}",
            headers=headers,
            timeout=10,
            allow_redirects=True
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise
    except requests.exceptions.RequestException as req_err:
        raise
    except ValueError as json_err:
        raise