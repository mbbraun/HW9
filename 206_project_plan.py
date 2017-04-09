## Your name: Michael Braunstein 	
## The option you've chosen: 2

# Put import statements you expect to need here!
import unittests
import itertools
import collections 
import tweepy
import twitter_info
import json
import sqlite3
















# Write your test cases here.
print ("\n\n BELOW THIS LINE IS OUTPUT FROM TESTS:\n")

class Task1(unittest.TestCase):
	def test_tweet_caching(self):
		f = open("SI206_finalproject_cache.json", "r").read()
		self.assertTrue("tweets" in f)
	def test_movie_caching(self):
		f = open("SI206_finalproject_cache.json", "r").read()
		self.assertTrue("movies" in f)
	def test_get_user_tweets(self):
		res = get_user_tweets("will smith")
		self.assertEqual(type(res), type(['hi', 5]))
	def test_movie_string(self):
		i = Movie(movie_dict)
		self.assertEqual(type(i.__str__(), str))
	def test_movie_title(self):
		i = Movie(movie_dict)
		self.assertEqual(type(i.title), type("Inception"))
	def test_get_actors(self):
		i = Movie(movie_dict)
		self.assertEqual(type(i.get_actors()), type(['hello']))
	def test_actors_tweets(self):
		i = Movie(movie_dict):
		actor = i.get_actors()[0]
		actor_data = get_user_tweets(actor)
		self.assertEqual(actor_data[1]['user']['screen_name'], actor)
	def test_get_user2(self):
		l = get_user_tweets("will smith")
		self.assertEqual(type(l[1]), type({})




## Remember to invoke all your tests...

if __name__ == "__main__":
	unittest.main(verbosity=2)

