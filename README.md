# Revelop-project
The idea of this project is to retrive from a public API some datas 
that are they are to these post that each of them contains:
- `userId`, `id`, `title`, and `body`.
## Imported libraries
Inside the project I used the library included in python:

- `requests`: for the operation with the API such as: `request.get(url)`, `request.status_code` and `request.json()`.
- `json`: when we serialize and deserialize the data we get from the API and the file [post.json](post.json) and [analysis_results.json]().

## Retrive data from the API
- The first task is to write a script where we 
take all the data from the API: https://jsonplaceholder.typicode.com/posts%60
- Then I will save all of them inside the file [post.json](post.json).

## Analyze data from the JSON 
- calculate the numbers of posts written by each user (identified by the userId)
- identify the user with the max amount of post