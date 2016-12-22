import requests
import urllib
from collections import OrderedDict
from re import match
from bs4 import BeautifulSoup
import json


class Peri(object):
    PERISCOPE_API_BASE_URL = 'https://api.periscope.tv/api/v2'
    PERISCOPE_WEB_BASE_URL = 'https://www.periscope.tv'

    def request_api(self, endpoint, **params):
        """
        Make a request against the Periscope API and return the result.
        """
        url = self._create_api_request_url(endpoint, **params)
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def get_broadcast_info(self, broadcast_id):
        """
        Retrieve a dict of information about a specific Broadcast.

        Uses Periscope's `accessVideoPublic` API endpoint.
        """
        endpoint = 'accessVideoPublic'
        result = self.request_api(endpoint, broadcast_id=broadcast_id)
        return result['broadcast']

    def get_user_info(self, user_id):
        """
        Retrieve a dict of information about a specific User.

        Uses Periscope's `getUserPublic` API endpoint.
        """
        endpoint = 'getUserPublic'
        result = self.request_api(endpoint, user_id=user_id)
        return result['user']

    def get_user_broadcast_history(self, user_id=None, username=None):
        endpoint = 'getUserBroadcastsPublic'
        session_tokens = self.get_web_public_user_session_tokens(
            user_id, username
        )
        params = {
            'user_id': session_tokens['user_id'],
            'session_id': session_tokens['broadcastHistory'],
            'all': 'true',
        }
        response = self.request_api(endpoint, **params)
        return response['broadcasts']

    def get_web_public_user_session_tokens(self, user_id=None, username=None):
        """
        Request new Public Session Tokens to access endpoints relating to a
        specific user.

        Returns a Dict containing Public Sesion Tokens for:

            * broadcastHistory
            * serviceToken
            * thumbnailPlaylist

        The returned Dict will also contain the requested User's 'user_id'.
        """
        user_url = self.create_user_url(user_id=user_id, username=username)

        data_store = self._get_web_data_store(user_url)
        public_tokens = data_store['SessionToken']['public']

        token_names = [
            'broadcastHistory', 'serviceToken', 'thumbnailPlaylist'
        ]

        out = {'user_id': data_store['Tracking']['userId']}
        for token_name in token_names:
            out[token_name] = public_tokens[token_name]['token']['session_id']

        return out

    @classmethod
    def create_user_url(cls, user_id=None, username=None):
        """
        Create the URL to a User's Periscope page.
        """
        if user_id:
            return '{web_base_url}/u/{user_id}'.format(
                web_base_url=Peri.PERISCOPE_WEB_BASE_URL,
                user_id=user_id
            )
        elif username:
            return '{web_base_url}/{username}'.format(
                web_base_url=Peri.PERISCOPE_WEB_BASE_URL,
                username=username
            )

        raise ValueError('Must specify either user_id or username')

    @classmethod
    def parse_periscope_url(cls, url):
        """
        Get any key information available from the supplied URL.

        Will attempt to retrieve one, or combination of:

        * broadcast_id
        * user_id
        * username
        """

        url_parsers = [
            cls._parse_periscope_w_url,
            cls._parse_periscope_u_url,
            cls._parse_periscope_username_broadcast_id_url,
            cls._parse_periscope_username_url,
        ]

        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        for url_parser in url_parsers:
            parse_result = url_parser(url)
            if parse_result != out:
                return parse_result

        return out

    def _get_web_data_store(self, url):
        """
        Retrieve and return the 'data-store' HTML data attribute from the
        given URL as a Dict.
        """
        r = requests.get(url)
        r.raise_for_status()

        soup = BeautifulSoup(r.content, 'html.parser')
        page_container = soup.find(id='page-container')
        data_store = json.loads(page_container['data-store'])
        return data_store

    @classmethod
    def _create_api_request_url(cls, endpoint, **params):
        """
        Craft a URL to the Periscope API with the supplied endpoint and params.
        """
        # For easier testing, make sure all params are always in a consistent
        # order.
        params_ordered = OrderedDict(sorted(params.items()))

        url = '{base_url}/{endpoint}?{params}'.format(
            base_url=cls.PERISCOPE_API_BASE_URL,
            endpoint=endpoint,
            params=urllib.parse.urlencode(params_ordered),
        )
        return url

    @classmethod
    def _parse_periscope_w_url(cls, url):
        """
        Retrieve the `broadcast_id` from the supplied "/w/" URL.

        "/w/" URLs look like this:

            * https://www.periscope.tv/w/<broadcast_id>

        Returns a dict of `username`, `broadcast_id` and `user_id` values.
        """
        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        w_url_pattern = '{base_url}/w/([A-Za-z0-9]+)'.format(
            base_url=Peri.PERISCOPE_WEB_BASE_URL
        )

        w_result = match(w_url_pattern, url)
        if w_result:
            broadcast_id = w_result.group(1)
            out['broadcast_id'] = broadcast_id
        return out

    @classmethod
    def _parse_periscope_username_url(cls, url):
        """
        Extracts the username from URLs formatted like this:

            * https://www.periscope.tv/<username>

        Returns a dict of `username`, `broadcast_id` and `user_id` values.
        """
        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        username_url_pattern = '{base_url}/([A-Za-z0-9_]+)'.format(
            base_url=Peri.PERISCOPE_WEB_BASE_URL
        )
        username_result = match(username_url_pattern, url)
        if username_result:
            username = username_result.group(1)
            out['username'] = username
        return out

    @classmethod
    def _parse_periscope_username_broadcast_id_url(cls, url):
        """
        Extract the `username`and `broadcast_id` from URLs formatted like this:

            * https://www.periscope.tv/<username>/<broadcast_id>

        Returns a dict of `username`, `broadcast_id` and `user_id` values.
        """
        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        url_pattern = '{base_url}/([A-Za-z0-9_]+)/([A-Za-z0-9]+)'.format(
            base_url=Peri.PERISCOPE_WEB_BASE_URL
        )
        result = match(url_pattern, url)
        if result:
            username = result.group(1)
            broadcast_id = result.group(2)
            out['username'] = username
            out['broadcast_id'] = broadcast_id
        return out

    @classmethod
    def _parse_periscope_u_url(cls, url):
        """
        Retrieve the `user_id` from the supplied "/u/" URL.

        "/u/" URLs look like this:

            * https://www.periscope.tv/u/<user_id>

        Returns a dict of `username`, `broadcast_id` and `user_id` values.
        """
        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        u_url_pattern = '{base_url}/u/([0-9]+)'.format(
            base_url=Peri.PERISCOPE_WEB_BASE_URL
        )

        u_result = match(u_url_pattern, url)
        if u_result:
            broadcast_id = u_result.group(1)
            out['user_id'] = broadcast_id
        return out
