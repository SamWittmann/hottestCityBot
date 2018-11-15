from requests_oauthlib import OAuth1Session
import os


class TwitterClient:
    def __init__(self):
        self.initialized = False
        self._twitter_auth = None

        self._post_tweet_url = "https://api.twitter.com/1.1/statuses/update.json"
        self._request_token_url = "https://api.twitter.com/oauth/request_token"
        self._access_token_url = "https://api.twitter.com/oauth/access_token"
        self._CLIENT_KEY = "client_key"
        self._CLIENT_SECRET = "client_secret"
        self._OWNER_KEY = "resource_owner_key"
        self._OWNER_SECRET = "resource_owner_secret"

    def _init_client(self):
        client_key = os.getenv(self._CLIENT_KEY)
        client_secret = os.getenv(self._CLIENT_SECRET)
        resource_owner_key = os.getenv(self._OWNER_KEY)
        resource_owner_secret = os.getenv(self._OWNER_SECRET)

        if not (client_key and client_secret and resource_owner_key and resource_owner_secret):
            raise EnvironmentError("Client creation failed: a needed environment variable is null")

        self._twitter_auth = OAuth1Session(client_key,
                                          client_secret=client_secret,
                                          resource_owner_key=resource_owner_key,
                                          resource_owner_secret=resource_owner_secret)

    def post_text_tweet(self, text_content):
        if not self._twitter_auth:
            raise AttributeError("Twitter client has not yet been implemented")

        self._twitter_auth.post(url=self._post_tweet_url, data={"status": text_content})

    def get_client(self):
        if self.initialized:
            return self

        self._init_client()
        self.initialized = True
        return self
