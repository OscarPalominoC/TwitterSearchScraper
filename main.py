import tweepy
# API key: X4Y7Y04awoRF1MCyQa7GihgnP
# API secret key: 1Df4QFiMAxSmDNx2mpFv1DSLx3CZgHwQWDC4eO3QG8T6vCXv4E
# Bearer token: AAAAAAAAAAAAAAAAAAAAALg8HgEAAAAA39cREsdqUFaFKjLPI10LuDzSOdo%3D58W5NRZXsfjn9DT3s9kJBTuwqkPBnmxZpIdegJSfbfbpy6WYpC
# Access token: 375970946-vtiEnm2V2cv7GehiKclmzglcOXODsiYk4NHAH6Ty
# Access token secret: 4igL12gmSDv9hxmN9Uk87xKaMEbVUYLummFetGrLLHBT2
# Authenticate to Twitter
auth = tweepy.OAuthHandler("X4Y7Y04awoRF1MCyQa7GihgnP", 
    "1Df4QFiMAxSmDNx2mpFv1DSLx3CZgHwQWDC4eO3QG8T6vCXv4E")
auth.set_access_token("375970946-vtiEnm2V2cv7GehiKclmzglcOXODsiYk4NHAH6Ty", 
    "4igL12gmSDv9hxmN9Uk87xKaMEbVUYLummFetGrLLHBT2")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
