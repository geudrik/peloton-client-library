## Peloton Client Library
Hello Peloton! I wanted to thank you for being sane people and utilizing an API to move data around, at the very
least, from within your web app (I have no idea how you do it on the bike etc).

I wrote (see: am writing) this library for a couple reasons, not the least of which is to be able to mess around with
my workout data, and eventually attempt to build (my first practical idea) an algorithm that predicts target resistance
to match an instructors cadence/output requirement. For funsies.

I've tried to be as reasonable as I can in developing this client lib - I lazy load as much data as possible to limit API
calls, and if you look in your logs, you'll see a header that clearly indicates that this library is making API calls
(look for `peloton-client-library/` in your logs). I
have also tried to mimic the paging/granularity that's made by your web UI (going under the assumption that your
backend is optimsed for those calls) - the last thing I want to do is piss you off! <3

If you have any questions or concerns, please, ping me (I'm not hard to find).

### API Documentation
This all started out of a curiosity when I looked at a ride details page. I threw open dev tools and .. boom, you've got
an actual web app that's making API calls to drive the UI. A+, friends.

As I've been poking around in your WebUI, I've essentially been looking at the API calls that are made. I've
been keeping notes on all of this [here](https://github.com/geudrik/peloton-api/blob/master/API_DOCS.md).

### Using the Client Library
Utilizing the library is pretty simple. A super quick example is below, with more thorough documentation to follow as I
find time (this is a side/pet project after all).

#### Configuration
The library requires a configuration file, whos path is either pulled from the environment variale `PELOTON_CONFIG`,
or looked for in the hard-coded `~/.config/peloton` (which can be a symlink to a unified config if you have many). The
only config block that the library looks for is shown below.

```bash
[peloton]
username = Your_Peloton_Username_Or_Email
password = Your_Peloton_Password

# Optional: Whether or not to ignore warnings that are thrown (default: True)
ignore_warnings = True

# Optional: Verify SSL Authenticity (default: True)
ssl_verify = True

# Optional: Filepath to a local cert bundle. Useful when SSL MITM is in play (default: None)
ssl_cert = ''

```

You may also specify the environment variables `PELOTON_USERNAME` and `PELOTON_PASSWORD` which will take precedence over the config file.

#### Example Usage
```python

>>> from peloton import PelotonWorkout
>>> workouts = PelotonWorkout.list()
>>> workout = workouts[0]

>>> dir(workout)
['_get_metrics', 'achievements', 'created', 'created_at', 'end_time', 'fitness_discipline', 'get', 'id', 'leaderboard_rank', 'list', 'metrics', 'ride', 'serialize', 'start_time', 'status', 'total_leaderboard_users']

>>> workout.status
'COMPLETE'

>>> workout.ride
<peloton.peloton.PelotonRide object at 0x104516e48>

>>> dir(workout.ride)
['description', 'duration', 'get', 'id', 'instructor_id', 'serialize', 'title']

>>> workout.ride.title
'45 min Max Capacity Ride'
```
