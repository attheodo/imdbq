#!/usr/bin/python
import requests
import argparse

API_ENDPOINT = 'http://imdbapi.org/'

def search_by_title(title):
    print "\n[-] Querying for \"%s\"\n" % title

    get_params = {'title': title,'type': 'json', 'plot': 'simple', 'limit': 5 ,'yg': 0,'lang': 'en-US', 'mt': 'none', 'release': 'simple'}
    r = requests.get(API_ENDPOINT,params=get_params)
    response = r.json()

    for movie in response:
       print "\t- %s (%s) - %s\n\t\tRating: %s\n\t\t%s\n" % (movie['title'], movie['year'], ', '.join(movie['genres']), movie['rating'],movie.get('plot_simple',None))

def main():
    parser = argparse.ArgumentParser(description='IMDBq')
    parser.add_argument('-t','--title',help = 'Title of the movie to search for',dest = "title")
    args = parser.parse_args()

    if args.title:
        search_by_title(args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()