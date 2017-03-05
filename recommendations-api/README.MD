# requirements-api

The api used for getting recommendations for skill you want.

# Methods

GET:<br>
/getCourses?skill=Java<br>
skill - the name of skill

/getBooks?title=Java
title - the name of book

# For build image use 

```sh
$ docker build -t recommendations-api .
```

# For run container use

```sh
$ docker run -p 5002:5000 -d --name recommendations-api recommendations-api
```
