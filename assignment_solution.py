"""
 Libraries we need for this project:

 - requests: to retrive the datas from the API
 - json: where we will write the datas from the API
 - os: is a built-in module used to check the existence of a file or working with path
"""
import requests
import json
import os
from setuptools.command.bdist_egg import analyze_egg

API_URL = "https://jsonplaceholder.typicode.com/posts%60" # In the var we save the URL of the API we want to access
post_file = "posts.json"  # We define the JSON file where we save all the posts
analysis_file = "analysis_results.json" # Defined the JSON file where we save all the result form the analysis
# Define The dict for the presentation option of the datas
analysis_result = { "user_post_counts": {} , "top_user": {}, "keyword_search_results": {}}
# Defined the function to request the data from the API
def get_datas(url):
    # We send a GET request to the API where we ask to pick the datas from the URL
    request = requests.get(url)

    # The function .status_code helps us to check if the response of the GET request went well
    if request.status_code == 200:
        json_data = request.json()
        write_data(post_file, json_data)

"""
Divided the JSON operation in function where we have the:

    - retrive_data(file): The function to get the data from the JSON file + new check
      with the try/catch we see if the file exits or no, in case we create a new one
    
    - write_data(file, data): The function to write data inside the JSON file + new check 
      for the file existence and the append operation.
"""
def retrive_data(file):
    if  os.path.getsize(file) > 0:
        with open(file,"r") as f:
            data = json.load(f)
            return data
    else:
        print(f"The file: \"{file}\" is empty")
        return None


def write_data(file, new_data):
   # Check if the file exists and the size is less than or equal to zero
   if os.path.exists(analysis_file) and os.path.getsize(analysis_file) == 0:

       # Then we write a new content inside the file
       with open(file, "w") as f:
          json.dump(new_data, f, indent=4)

   # In the other hand if the file has content, we append it
   elif os.path.getsize(analysis_file) > 0:
       with open(file, "r+") as f:
           # Load existing data into a dictionary
           old_data = retrive_data(file)

           # Update the dict with the new data with the function .update()
           old_data.update(new_data)

           # Write the updated data back to the file
           json.dump(old_data, f, indent=4)

"""
Functions I used to analyze the data inside JSON file:

    - count_post(post_list) return user_post_count: we take a list of dict of user 
    and we check if the user is not already inside the new dict we initialize the first
    post counter to 1, otherwise we increment the value related to the user.
"""
def count_post(post_list):
    user_post_tracker = {}
    for post in post_list:
        userId = post["userId"]
        # if the user is not inside the dict, then we add the first one
        if post.get("userId") not in user_post_tracker:
            user_post_tracker[userId] = 1
        else:
        # if it's already there, then we increase the value of the num of post
            user_post_tracker[userId] += 1
    return user_post_tracker

def find_top_user(user_posts, post_list):
    top_users = {}
    user_id = 0
    num_post = []
    titles = []
    summaries = []
    max_posts = max(user_posts.values())
    # defined the max user inside the list
    for user, num_post in user_posts.items():
        if max_posts == num_post: user_id = user

    # then we filter the posts for the user with the greatest number and save in the lis
    for post in post_list:
        if post.get("userId") == user_id: num_post.append(post)

    # I grab the first five posts
    first_five = num_post[:5]
    # I save the first five titles of the first five one
    for post in first_five:
        titles.append(post["title"])
        summaries.append(post["body"][:50])
    # save the user inside the dict top_users
    top_users.update({"userId": user_id, "total_post": max_posts, "titles": titles, "summaries": summaries })
    return top_users

"""
Retrive data from the API:
    - I just pass the API_URL inside th function where, I'm going to save all the data inside 
    the file posts.json
"""
get_datas(API_URL)

""" 
Analyze the data:

    -  Calculate the numbers of posts written by each user (identified by the userId)
    -  Save the datas inside a dict and write them into the file analysis_result.json 
    -  Identify the user with the major amount of post
"""
posts_list = retrive_data(post_file)
#  Get the number of posts for each user
user_post_count = count_post(posts_list)

# Identify the user with the major amount of post
top_user = find_top_user(user_post_count, posts_list)
analysis_result.update({"user_post_counts": user_post_count, "top_user": top_user})

"""
Archive data: 
    
    - Saved the data inside the file analysis_results.json

"""
write_data(analysis_file,analysis_result)
