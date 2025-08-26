"""
 Libraries we need for this project:

 - requests: to retrive the datas from the API
 - json: where we will write the datas from the API
"""
import requests
import json

# Defined the function to request the data from the API
def get_datas(url):
    # We send a GET request to the API where we ask to pick the datas from the URL
    request = requests.get(url)

    # The function .status_code helps us to check if the response of the GET request went well
    if request.status_code == 200:
        datas = request.json()
        with open("post.json", "w") as f:
            json.dump(datas, f, indent=4)

# 1. Retrive the data from the API and save them inside the JSON file

# In the var we save the URL of the API we want to access
url_API = "https://jsonplaceholder.typicode.com/posts"
get_datas(url_API)