# Revelop-project
The idea of this project is to retrive from a public API some datas 
that are they are to these post that each of them contains:
- `userId`, `id`, `title`, and `body`.
## Imported libraries
Inside the project I used the library included in python:

- `requests`: for the operation with the API such as: `request.get(url)`, `request.status_code` and `request.json()`.
- `json`: when we serialize and deserialize the data we get from the API and the file [post.json](posts.json) and [analysis_results.json]().
-  `os`: built in module of Python to check if a file exists and work with file paths.

## Retrive data from the API
- The first task is to write a script where we 
take all the data from the API: https://jsonplaceholder.typicode.com/posts%60
- Then I will save all of them inside the file [post.json](posts.json).

## Analyze data from the JSON 
- Calculate the numbers of posts written by each user (identified by the userId)
- Identify the user with the max amount of post.
- We save the data inside the file [analysis_results.json](analysis_results.json) with ID the userId and the value the amount of post for each user.
- Separated them with the dict `analysis_result` with the key `user_post_counts`, `top_user` and `keyword_search_results` 