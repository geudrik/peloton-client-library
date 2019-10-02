You've found my little repo of doodles and random odds and ends that I've written/collected in my attempts to index my 
cycling data

Peloton hasn't documented their API. I wanted to start indexing my workout data, so I've been poking around trying to 
find what I can. What follows is a rough outline of what I've found that more or less gets me the data I want to index.

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
https://api.onepeloton.com/api/workout/<workout id>?joins=ride,ride.instructor&limit=1&page=0
https://api.onepeloton.com/api/workout/<workout id>/performance_graph?every_n=5
```

It would appear that when you do a `limit=1&page=0`, the most recent workout will be returned, which is great!

Update May 30: Seems like some of these workout endpoints aren't quite as user-friendly as once thought.. `/workout/id`
reuturns information about a workout. Makes sense. But. `/user/id/workouts?joins..` returns a list of workouts, but each
workout has _*different*_  (see, missing - leaderboard info is a prime example) information in each workout than what you get back from `/workout/id`. This is inconsistent,
and even looking at the website, results in additional (and unecessary) API calls being made. :sad:

For example, lets assume we're looking at the latest workout, in my case, workout id `9c0eb00ad49945acbb313c31cf51b5df`
We can get this workout in one of two ways.
* GET `workout/9c0eb00ad49945acbb313c31cf51b5df`
* GET `user/my_user_id/workouts` -> `data[0]`

If we look at the data returned from the first method, it has 27 top level keys. If we look at the second way, we have
24 top level keys returned. The two I noticed are `total_leaderboard_users` and `leaderboard_rank`, but a quick diff
would show them all.

### Ride Info

Rides are the classes that you _can_ take, not necessarily what you _have_ taken/completed (that would be a workout). 
These endpoints give information about a specific class (see: ride.) 
```
https://api.onepeloton.com/api/ride/<ride id>
https://api.onepeloton.com/api/ride/<ride id>/details
```


All classes, no matter the workout type seem to considered a "ride".  The most recent list of classes are available anonymously via this endpoint:
```
https://api.onepeloton.com/api/v2/ride/archived?browse_category=
```
Categories have straightforward names:
- Cycling
- Running
- Outdoor
- Strength
- Yoga
- Meditation
- Stretching
- Bootcamp
- Walking
- Cardio

Querying this endpoint with a specific query parameter will return JSON(truncated).  This appears to be mainly used by the various applicatiions.  

```
"page_count": Number of pages
"instructors": Instructor info and data
"class_types": List of all possible class types, regardless of category
"total": Total number of available classes?
"data": The actual ride data, lot's of good info in here!
"ride_types": Appears to be another version of class_types
"count": ???
"browse_categories": used in the web app to load images
"fitness_disciplines": Sets of data, probably used by the app to associate IDs and names
"show_next": default seems to be true
"sort_by": default is scheduled start time
"show_previous": default is false
"page": current page
"hide_explicit_rides": defaults to null
```
        



@pelotoncycle it would be awesome if you guys could post up some actual API docs! :heart: 

These endppoints will likely not be super useful unless you're looking for class details about the workout you're 
looking at

### Requires header "peloton-platform: web" - no idea what other values are accepted for this header
```
https://api.onepeloton.com/api/user/<user id>/overview?version=1
```
