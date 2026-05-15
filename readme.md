# StarLight Custom Library

a simple python script to make your own custom starlight library

## How does it work?

It's really simple: host spoofing, on your phone, you must download AdAway or any VPN that allows redirecting, then, redirect "starlight.allofus.dev" to your computer's IP.
Note that you'll need a custom starlight build and use Caddy/Nix to provide a local CA certificate

### ALL known API paths

ALL only accept GET requests
these paths are found in ApiService.java (full name: dev.allofus.starlight.api.ApiService)

#### /api/v3/health

checks if the server is alive

#### /api/v3/mods

lists all mods

#### /api/v3/mods/{modid}

lists a specific mod information
there are subpaths but generally ignored as the mod information probably takes priority

#### /api/v3/mods/trending

it takes these arguments: limit (integer) and offset (integer)
lists the trending mods (shown on the top of the starlight app)

#### /api/v3/mods/search

it's a GET method that takes these arguments: q (string), limit (integer) and offset (integer)
it's just the result of a search

#### /api/v3/mods/total /api/v3/news/posts/total and /api/v3/servers/total

lists the total of mods, news posts and servers respectively
on the official API, redirects to itself

#### /api/v3/news/posts/

takes these arguments: offset (integer) and limit (integer)
lists all news posts

#### /api/v3/servers

lists all servers
