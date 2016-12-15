import requests
import urllib
from collections import OrderedDict
from re import match


class PyPeri(object):
    PERISCOPE_API_BASE_URL = 'https://api.periscope.tv/api/v2/'
    PERISCOPE_WEB_BASE_URL = 'https://www.periscope.tv/'

    def request_api(self, endpoint, **params):
        """
        Make a request against the Periscope API and return the result.
        """
        url = self.create_api_request_url(endpoint, **params)
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def create_api_request_url(self, endpoint, **params):
        """
        Craft a URL to the Periscope API with the supplied endpoint and params.
        """
        # For easier testing, make sure all params are always in a consistent
        # order.
        params_ordered = OrderedDict(sorted(params.items()))

        url = '{base_url}{endpoint}?{params}'.format(
            base_url=PyPeri.PERISCOPE_API_BASE_URL,
            endpoint=endpoint,
            params=urllib.parse.urlencode(params_ordered),
        )
        return url

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

    def parse_periscope_url(self, url):
        """
        Get any key information available from the supplied URL.

        Will attempt to retrieve one, or combination of:

        * broadcast_id
        * user_id
        * username
        """
        out = {
            'broadcast_id': None,
            'user_id': None,
            'username': None,
        }

        w_url_pattern = '{base_url}w/([A-Za-z0-9]+)'.format(
            base_url=PyPeri.PERISCOPE_WEB_BASE_URL
        )
        w_result = match(w_url_pattern, url)
        if w_result:
            out['broadcast_id'] = w_result.group(1)

        return out
