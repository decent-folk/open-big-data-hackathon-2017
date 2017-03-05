# requirements-api

The api used for getting requariments for vacancy you want.

# Methods

GET:<br>
/getRequirements?name=Java%20Developer<br>
name - the name of vacancy

# For build image use 

```sh
$ docker build -t requirements-api .
```

# For run container use

```sh
$ docker run -p 5000:5000 -d --name requirements-api requirements-api
```
