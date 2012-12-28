#!/usr/bin/python
import requests
import argparse

API_ENDPOINT = 'http://imdbapi.org/'

def search_by_title(title):
    movies = imdbquery(title)

    if isinstance(movies,dict) and movies['code'] == 404:
        print "Film not Found"
    else:
        for movie in movies:
            print "\t- %s (%s) - %s - Rating: %s\n\t\t%s\n" % (movie['title'], movie['year'], ', '.join(movie['genres']),\
                                                           movie['rating'],movie.get('plot_simple',None))

def rating_for_title(title):
    movie = imdbquery(title,limit=1)

    if isinstance(movie,dict) and movie['code'] == 404:
       print "Film not Found"
    else:
        print "%s" % movie[0]['rating']


def imdbquery(title, type='json',yg = 0, mt = 'none', plot = 'simple',limit = 5,lang = 'en-US',aka = 'simple',release = 'simple'):

    get_params = {'title': title,'type': type, 'plot': plot, 'limit': limit ,'yg': yg,'lang': lang, 'mt': mt, 'release': release, 'aka': aka}
    r = requests.get(API_ENDPOINT,params=get_params)
    response = r.json()

    return response


def main():
    parser = argparse.ArgumentParser(description='IMDBq')
    parser.add_argument('-t','--title',help = 'Title of the movie to search for',dest = "title")
    parser.add_argument('-r','--rating', help = 'Display only the movie rating of the first result returned', action="store_true", default = False)
    args = parser.parse_args()

    if args.title and not args.rating:
        search_by_title(args.title)
    elif args.title and args.rating:
        rating_for_title(args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()