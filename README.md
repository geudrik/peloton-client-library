You've found my little repo of doodles and random odds and ends that I've written/collected in my attempts to index my cycling data

Peloton hasn't documented their API. I wanted to start indexing my workout data, so I've been poking around trying to find what I can. What follows is a rough outline of what I've found that more or less gets me the data I want to index.

## Authenticate to Peloton API
```
import requests

s = requests.Session()
payload = {'username_or_email':'Your username or email', 'password':'your password'}
s.post('https://api.onepeloton.com/auth/login', json=payload)
```

With that done, you can now access any endpoint that requires authentication simply by doing `s.get()`

## Anonymous Endpoints
```
https://api.onepeloton.com/api/instructor
https://api.onepeloton.com/api/instructor/<instructor id>
https://api.onepeloton.com/api/ride/metadata_mappings
```

## Privileged Endpoints

### Essential information about the logged in user
```
https://api.onepeloton.com/api/me
```

### User details and workouts completed
```
https://api.onepeloton.com/api/user/<user id>
https://api.onepeloton.com/api/user/<user id>/workouts
https://api.onepeloton.com/api/user/<user id>/workouts?joins=ride,ride.instructor&limit=10&page=0
```

### Workout specific info

Note that workouts, in this context, are what a user did. So, a workout can either be a tread or bike workout.
```
https://api.onepeloton.com/api/workout/<workout id>
https://api.onepeloton.com/api/workout/<workout id>/performance_graph?every_n=5
```

### Ride Info

Rides are the classes that you _can_ take, not necessarily what you _have_ taken/completed (that would be a workout). These endpoints give information about a specific class (see: ride. No idea what the Tread endpoint is as I adon't have a tread or really looked into it)
```
https://api.onepeloton.com/api/ride/<ride id>
https://api.onepeloton.com/api/ride/<ride id>/details
```

### Requires header "peloton-platform: web" - no idea what other values are accepted for this header
```
https://api.onepeloton.com/api/user/<user id>/overview?version=1
```
