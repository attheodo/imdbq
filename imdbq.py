#!/usr/bin/python
import requests
import argparse

API_ENDPOINT = 'http://imdbapi.org/'

def search_by_title(title):

    movies = imdbquery(title)
    for movie in movies:
        print "\t- %s (%s) - %s - Rating: %s\n\t\t%s\n" % (movie['title'], movie['year'], ', '.join(movie['genres']),\
                                                           movie['rating'],movie.get('plot_simple',None))

def imdbquery(title, type='json',yg = 0, mt = 'none', plot = 'simple',limit = 5,lang = 'en-US',aka = 'simple',release = 'simple'):

    get_params = {'title': title,'type': type, 'plot': plot, 'limit': limit ,'yg': yg,'lang': lang, 'mt': mt, 'release': release, 'aka': aka}
    r = requests.get(API_ENDPOINT,params=get_params)
    response = r.json()

    return response


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