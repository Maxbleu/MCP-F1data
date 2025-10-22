import os, requests

def launch_request_f1db(path: str, data={}):
    headers = {
        "Authorization": f"Bearer {os.getenv("JWT_TOKEN")}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        url = f"https://apif1db-production.up.railway.app/api{path}"
        timeout = 10
        allow_redirects = True
        if not data:
            response = requests.get(
                url=url,
                headers=headers,
                timeout=timeout,
                allow_redirects=allow_redirects
            )
        elif len(data) > 0:
            response = requests.get(
                url=url,
                headers=headers,
                data=data,
                timeout=timeout,
                allow_redirects=allow_redirects
            )

        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise
    except requests.exceptions.RequestException as req_err:
        raise
    except ValueError as json_err:
        raise