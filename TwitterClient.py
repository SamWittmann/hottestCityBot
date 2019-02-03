from requests_oauthlib import OAuth1Session
import logging
import yaml


class TwitterClient:
    def __init__(self):
        self.initialized = False
        self._twitter_auth = None
        self.config = yaml.safe_load(file('config.yml', 'r'))
        self.logger = logging.getLogger('HottestCityBot')

        self._post_tweet_url = "https://api.twitter.com/1.1/statuses/update.json"
        self._request_token_url = "https://api.twitter.com/oauth/request_token"
        self._access_token_url = "https://api.twitter.com/oauth/access_token"
        self._CLIENT_KEY = "client_key"
        self._CLIENT_SECRET = "client_secret"
        self._OWNER_KEY = "resource_owner_key"
        self._OWNER_SECRET = "resource_owner_secret"

    def _init_client(self):
        client_key = self.config.get(self._CLIENT_KEY)
        client_secret = self.config.get(self._CLIENT_SECRET)
        resource_owner_key = self.config.get(self._OWNER_KEY)
        resource_owner_secret = self.config.get(self._OWNER_SECRET)

        if not (client_key and client_secret and resource_owner_key and resource_owner_secret):
            raise EnvironmentError("Client creation failed: couldn't read properties from config file")

        self._twitter_auth = OAuth1Session(client_key,
                                          client_secret=client_secret,
                                          resource_owner_key=resource_owner_key,
                                          resource_owner_secret=resource_owner_secret)

    def post_text_tweet(self, text_content):
        if not self._twitter_auth:
            raise AttributeError("Twitter client has not yet been implemented")

        self._twitter_auth.post(url=self._post_tweet_url, data={"status": text_content})
        self.logger.info("Tweet posted!")


    def get_client(self):
        if self.initialized:
            return self

        self._init_client()
        self.initialized = True
        return self
