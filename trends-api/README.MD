# requirements-api

The api used for getting google trends for skill you want.

# Methods

GET:<br>
/getTrends?skill=Java<br>
skill - the name of the skill

# For build image use 

```sh
$ docker build -t trends-api .
```

# For run container use

```sh
$ docker run -p 5001:5000 -d --name trends-api trends-api
```
