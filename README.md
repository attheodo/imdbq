#imdbq#

Simple IMDB querying console tool written in Python

## Requirements
**imdbq** requires the excellent HTTP Requests module by Kenneth Reitz (http://python-requests.org).
Get the module via
```sudo pip install requests```

## Usage
```
usage: imdbq.py [-h] [-t TITLE] [-r]

IMDBq

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Title of the movie to search for
  -r, --rating          Display only the movie rating of the first result
                        returned
```