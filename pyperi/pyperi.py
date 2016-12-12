import requests
import urllib
from collections import OrderedDict


class PyPeri(object):
    PERISCOPE_API_BASE_URL = 'https://api.periscope.tv/api/v2/'

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
        Craft a URL to the Periscope API from the supplied endpoint and params.
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
        """
