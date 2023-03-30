import json
from urllib.request import urlopen


# Hàm dùng chung
def check_session(request, session_name):
    return session_name in request.session  # True / False


def read_json_internet(url):
    url_response = urlopen(url)
    data = json.loads(url_response.read().decode())
    return data
