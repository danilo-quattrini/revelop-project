"""
 Libraries we need for this project:

 - requests: to retrive the datas from the API
 - json: where we will write the datas from the API
"""
import requests
import json
API_URL = "https://jsonplaceholder.typicode.com/posts" # In the var we save the URL of the API we want to access
post_file = "post.json" # We define the JSON file where we save all the posts

# Defined the function to request the data from the API
def get_datas(url):
    # We send a GET request to the API where we ask to pick the datas from the URL
    request = requests.get(url)

    # The function .status_code helps us to check if the response of the GET request went well
    if request.status_code == 200:
        datas = request.json()
        with open(post_file, "w") as f:
            json.dump(datas, f, indent=4)

# Defined the function to get the data from the JSON file
def retrive_data(file):
    data = []
    with open(file,"r") as f:
        data = json.load(f)
    return data

def count_post(post_list):
    user_post_count = {}
    for post in post_list:
        userId = post["userId"]
        # if the user is not inside the dict then we add the first one
        if post.get("userId") not in user_post_count:
            user_post_count[userId] = 1
        else:
        # if it's already there, then we increase the value of the num of post
            user_post_count[userId] += 1
    print(user_post_count)
# 1. Retrive the data from the API and save them inside the JSON file
get_datas(API_URL)

""" 
2. Analyze the data that we retrieved:
    -  calculate the numbers of posts written by each user (identified by the userId)
"""
# We define a list of post
posts_list = retrive_data(post_file)
count_post(posts_list)