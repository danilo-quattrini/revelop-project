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
- Then I will save all of them inside the file in local [post.json](posts.json).

## Analyze data from the JSON 
- Calculate the numbers of posts written by each user (identified by the userId)
- Identify the user with the max amount of post.
- We save the data inside the file [analysis_results.json](analysis_results.json) with ID the userId and the value the amount of post for each user.
- Separated them with the dict `analysis_result` with the key `user_post_counts`, `top_user` and `keyword_search_results` 

## Find data from the JSON
-  Implemented a function `search_post(keywords)` where we insert a key-word or a set of them and search if the key is in the body or 
inside the title.
-  The function returns a set of posts that they are equal to the key. 
-  Results are ranked by `match_score` (highest first)

## How to Run
1. Clone the repository or copy the files.  
2. Install dependencies:
   ```bash
   pip install requests
3. Run the scrip:
    ```bash
    python assignment_solution.py

4. When prompted, enter one or more keywords (separated by spaces).

## Files
- `assignment_solution.py`: the main script
- `posts.json`: raw datas took from the API
- `analysis_result.json`: all the analysis results

## Example Output
Sample structure of analysis_results.json:
```json
{
  "user_post_counts": {
    "1": 10,
    "2": 10,
    "3": 10
  },
  "top_user": {
    "userId": 1,
    "total_post": 10,
    "titles": [
      "post title 1",
      "post title 2",
      "post title 3"
    ],
    "summaries": [
      "post body beginning here...",
      "another body snippet..."
    ]
  },
  "keyword_search_results": [
    {
      "userId": 1,
      "id": 1,
      "title": "qui est esse",
      "body": "est rerum tempore vitae...",
      "match_score": 2
    }
  ]
}
````
# License
This Project is covered with the [MIT Licence](LICENSE).