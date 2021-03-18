#Overview
GlogalBlog24 is a Django REST framework project. It provides basic API to manage its data. 

#Requirements
+ Python (3.5, 3.6, 3.7, 3.8, 3.9)
+ Django (2.2, 3.0, 3.1)
Highly recommend using only officially support the latest patch release of each Python and Django series.

#User API
Register a new user
```
/auth/users/
```
Retrieve/update the currently logged in user
```
/auth/users/me/
```
Create a JWT by passing a valid user in the post request to this endpoint
```
/auth/jwt/create/
```
Get all user profiles and create a new one
```
/api/v1/accounts/users/
```
Detail view of a user's profile
```
/api/v1/accounts/user/id/
```

#Post API
Create new post
```
/api/v1/post/create/
```
Detail view of a post
```
/api/v1/post/id/
```
Update a post
```
/api/v1/post/update/id/
```
View a posts list
```
/api/v1/posts/
```
Delete a post
```
/api/v1/post/delete/id/
```

#Comment API
Create new comment
```
/api/v1/comment/create/
```
Detail view of a comment
```
/api/v1/comment/id/
```
View a comment list
```
/api/v1/commens/
```
Delete a comment
```
/api/v1/comment/delete/id/
```