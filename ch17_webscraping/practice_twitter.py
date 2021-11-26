import tweepy

# api key
consumer_key = 'aILHmVi4DYP8xYUTtiAAkgBlO'
consumer_seceret = 'gJv85HDsZwfOYbBzZRIox7vM423pUTvJKSlhF6TdxXxHqLHmGi'

# token
access_token = '1464072278811967489-3K7FZucv3RSi5S6Jeaoqu2GjXZhiPk'
access_secret = 'gfeeFwCM4FMfmdJHYWgCj0YnBRhN8Hn45NehlSqho2siM'

# OAuth 인증
auth = tweepy.OAuthHandler(consumer_key, consumer_seceret)
auth.set_access_token(access_token, access_secret)

# 트위터 API 클래스의 객체 생성
api = tweepy.API(auth)

# print(api.verify_credentials().name)
tweet_update_status = api.update_status('hello')
