import requests

def fetch_context(query):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        res = requests.get(url).json()
        return res.get("extract", "")
    except:
        return ""