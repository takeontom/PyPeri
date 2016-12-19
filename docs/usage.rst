=====
Usage
=====

Introduction
============

To use PyPeri in a project::

    >>> from pyperi.pyperi import PyPeri
    >>> pp = PyPeri()
    >>> user_info = pp.get_user_info('376827')
    >>> print(user_info['username'])
    george_clinton


The API
=======

get_user_info(user_id)
----------------------

Retrieves a dictionary of information about the specified user.

Internally, this uses the `getUserPublic` Periscope API endpoint.

Example usage::

    >>> pp.get_user_info('376827')
    {'class_name': 'User',
     'created_at': '2015-03-28T19:52:59.150319197-07:00',
     'description': "It's always gotten better by Thursday. www.georgeclinton.com",
     'display_name': 'George Clinton',
     'id': '376827',
     'initials': '',
     'is_beta_user': False,
     'is_employee': False,
     'is_twitter_verified': True,
     'n_followers': 14535,
     'n_following': 739,
     'n_hearts': 2768274,
     'profile_image_urls': [{'height': 128,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
                             'width': 128},
                            {'height': 200,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_200x200.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_200x200.jpeg',
                             'width': 200},
                            {'height': 400,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_400x400.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_400x400.jpeg',
                             'width': 400}],
     'twitter_id': '23177270',
     'twitter_screen_name': 'george_clinton',
     'username': 'george_clinton'}


get_broadcast_info(broadcast_id)
--------------------------------

Retrieves a dictionary of information about the specified broadcast.

Internally, this uses the `accessVideoPublic` Periscope API endpoint.

Example usage::

    >>> pp.get_broadcast_info('1zqKVWybqeDGB')
    {'available_for_replay': True,
     'camera_rotation': 271,
     'city': '',
     'class_name': 'Broadcast',
     'country': '',
     'country_state': '',
     'created_at': '2016-12-12T10:26:50.779286143-08:00',
     'end': '2016-12-12T11:43:16.649191397-08:00',
     'expiration': -1,
     'featured': False,
     'friend_chat': False,
     'has_location': False,
     'has_moderation': True,
     'height': 568,
     'highlight_available': True,
     'id': '1zqKVWybqeDGB',
     'image_url': 'https://tn.periscope.tv/C1RnUS8FqSm9cmrM0cXRM3MV3epaqaZgHc7WM_kUgiABO6iDkhwyNl56XVdvdkOV6R5vWZbUaLgsefoJYg_0GA/chunk_878.jpg?Expires=1796931805&Signature=FMb0NHoTz5BLpZIPCSS~xyVTDTmYRHLlxQoNqsn96ffDMgs5N1WVBsIMtthsTujYcaCNie3QdP02SyxUsqQcmuqJaHodcAdYt~8qDxs6qX2~8-foURHADqzOAMm6xUhvnjap4SuF~nZSsdmVPhuwl0lbF4ylG443huQB6qmQdzzlAZG1~gVU9dHQXA5cdH0smEcOIc1ujkcmGX1wk-t2Gkd~C4ujC1szvcDBi5Bpjxb80k2-oKDZs3TLqfOVzXaGaJesFshePFugFfVSrenJK2SQUEbulWAWOeWQf5ab~RvwSvucVqy2CAzkR3xtxWFY1CfBR8Rmt8vTpa8uN~r9Ag__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
     'image_url_small': 'https://tn.periscope.tv/C1RnUS8FqSm9cmrM0cXRM3MV3epaqaZgHc7WM_kUgiABO6iDkhwyNl56XVdvdkOV6R5vWZbUaLgsefoJYg_0GA/chunk_878_thumb_128.jpg?Expires=1796931805&Signature=JW9iFJZDqYeXKglWAsNh-f-D8QtBp7abjKKks2p80~k~LoSGFdY289CDX~DFquTamf2t-HVB6oFwNaAXel49xbY1TZFI5VyOVfVp2UCZwxXsF03b4WgmCfO13EZFpD~DIi0afALw~oxoHmk7n-WaBwlnBXogegSCbKmLPu5BGRlZJW9N7WTT7keLq-9DGRa5BSppcz-e3frgieZEJBbldef01do1sQsywK5z86FY21XE~xszIfb6new2dWFtJ7Jr0QQmyQBMaK-TU8o6y8kkqKU5cfjLPn~TwGUTUN2A0uyE6QDY2BRsO3sZJ7HoXzk-Cvxys0FzXr-i6iDU3McrKQ__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
     'ip_lat': 0,
     'ip_lng': 0,
     'is_locked': False,
     'iso_code': '',
     'language': 'en',
     'ping': '2016-12-12T11:43:08.860300617-08:00',
     'profile_image_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
     'start': '2016-12-12T10:41:09.286489243-08:00',
     'state': 'ENDED',
     'status': '🍋🍊#GeorgeClinton funkin N D Garden to take to grandmother n law '
               'fish already packed🚘🛤🚜 while listening to Music',
     'tags': ['GeorgeClinton'],
     'tweet_id': '808381195981451264',
     'twitter_username': 'george_clinton',
     'updated_at': '2016-12-12T11:43:25.626913215-08:00',
     'user_display_name': 'George Clinton',
     'user_id': '376827',
     'username': 'george_clinton',
     'width': 320}


get_user_broadcast_history(user_id=None, username=None)
-------------------------------------------------------

Attempt to retrieve the available broadcast history for the specified user.
If all goes well, it will return a Dict containing the same broadcast history
as shown a user's Periscope profile.

Example usage::

    >>> pp.get_user_broadcast_history(username='george_clinton')
    {}


get_web_public_user_session_tokens(user_id=None, username=None)
---------------------------------------------------------------

Request Public Session Tokens from Periscope, which are required for accesing
some endpoints of the Web API.

User Session Tokens will provide you with access to endpoints for a specific
Periscope User... they also expire after a few minutes, so it's recommended to
request new Tokens for each request which requires them, rather than attempting
to keep track of what Tokens you have, when they're about to expire, etc.

Returns a Dict containing the following Service Tokens:

* broadcastHistory
* serviceToken
* thumbnailPlaylist

Example usage::

    >>> pp.get_web_public_user_session_tokens(username='george_clinton')
    {}


get_web_data_store(url)
-----------------------

Data in the Web API is contained within the JSON found in the `data-store`
HTML data attribute on a `<div id="page-container">`. The
`get_web_data_store(url)` method grabs this data from the given URL and
returns it as a Dict.

This can be a useful tool during debugging and development.

Example usage::

    >>> pp.get_web_data_store('https://www.periscope.tv/george_clinton')
    {'Auth': {'cookie': None, 'user': None},
     'Blocked': {},
     'Broadcast': {'error': {'isNotFound': False,
                             'isServerError': False,
                             'isUnavailable': False},
                   'failed': [],
                   'forceUpdate': False,
                   'pending': []},
     ...
     'Replay': {'available': False,
                'duration': 1,
                'elapsed': 0,
                'percentage': 0,
                'replayAvailable': False,
                'requestedPosition': None},
     ...
     'ServiceToken': {'channels': {'failed': False,
                                   'pending': False,
                                   'token': None},
                      'safety': {'failed': False, 'pending': False, 'token': None}},
     'SessionToken': {'authed': {'broadcastHistory': {'expiry': 1482031213812,
                                                      'token': {'session_id': '1gJPr-JgpLDOA7UvVagJfGZ4_rUK6acqwXFLzkYW_MLAHJXABHtpcI8M_MhVHCtIkAjVLoETaQyeOSVGCujUOw1oVza00M78tOGiG'}},
                                 'serviceToken': {'expiry': 1482031213812,
                                                  'token': {'session_id': '1KQrcgw8pD_sWSG5q7xz2NX_T0uTiQsnQrG109M7k6wvH0xFaOfRrIejX8tcbz3WcyNduut19WBhUUW_EymQ7fwDY6Pj5IUYLKdrh'}},
                                 'thumbnailPlaylist': {'expiry': 1482031213812,
                                                       'token': {'session_id': '1sgxhozS2x3xlaHXOu6p7d8-SCAWeAdAQCRbaMnCSx3lx3R1QIdgdPWvXY4tx7X5yzPVb1va2HnPbVKYwyu75TyKBrUHephsMdZttl0bwpi9xogmE'}}},
                      'public': {'broadcastHistory': {'expiry': 1482031213812,
                                                      'token': {'session_id': '1ZRK3wcy1OwIkNSyfOYPW6cmC53DrI2o9W742xvH7H16jcOX8dPXaa74wYeGuk21N5wcsP7sffZmhRox8EE1Y9vkPYPS0QOqDO2jh3D3ujCoufkSv'}},
                                 'serviceToken': {'expiry': 1482031213812,
                                                  'token': {'session_id': '1xI6XnW-7lsGUIkDIqHJLobjwXtcwHqttcP4R4OhLyeezHTOTp3F5ay7oLym6lPOWa85-fElUN7kqfi2Lmz509aJIBCD1i7Um90kMBOKSxm8p'}},
                                 'thumbnailPlaylist': {'expiry': 1482031213812,
                                                       'token': {'session_id': '1FCYL0froR-yukXuob4fDX9D1BxZLsErK0dhr2RJrR-4uaPWMbJ08m9IbeMpy7GhCTWIhNhm9mgpuPVQJ6D252J4ynAV2MLAi9lgV7TqdAsbT9x_x1klILS-z'}}}},
     'Tracking': {'type': 'periscope/USER_BROADCAST_HISTORY_REQUEST',
                  'userId': '376827'},
     'User': {'error': {},
              'failed': [],
              'failedFollowing': [],
              'failedUnfollowing': [],
              'pending': [],
              'pendingFollowing': [],
              'pendingUnfollowing': []},
     'UserBroadcastHistory': {'broadcastIds': None,
                              'error': None,
                              'failed': [],
                              'pending': []},
     'UserBroadcastHistoryCache': {'histories': {}},
     'VideoPlayer': {'appAvailable': False,
                     'audio': 'OFF',
                     'autoplay': False,
                     'cinema': False,
                     'dimensions': {'height': 0, 'width': 0},
                     'includeVideoUI': False,
                     'isAutoplay': False,
                     'isCinemaPlayer': False,
                     'isConnected': False,
                     'isConnecting': False,
                     'isExpectingVideo': False,
                     'isInterstitialPresentation': True,
                     'isLiveMode': False,
                     'isLoadingVideo': False,
                     'isPaused': False,
                     'isPlayback': False,
                     'isPlaying': False,
                     'isReplayMode': False,
                     'isStalled': False,
                     'isStopped': True,
                     'isStoppedInterstitial': True,
                     'isUnknownMode': True,
                     'isVideoPresentation': False,
                     'muted': True,
                     'orientation': 0,
                     'playbackSupported': False,
                     'playerBackgroundReady': False,
                     'playerIsUnavailable': False,
                     'playerMode': 'UNKNOWN',
                     'playerState': 'STOPPED',
                     'presentation': 'INTERSTITIAL',
                     'requestedTimecode': -1,
                     'timecodePresent': False,
                     'unmuted': False,
                     'videoHasStarted': False},
     'routing': {}}

The structure and actual data returned by this method will vary wildly
depending on the requested URL.


create_user_url(self, user_id=None, username=None)
--------------------------------------------------

Create a URL to the specified User's Periscope page. The generated URL will
be different depending on whether the `user_id` or `username` was supplied.

Example usage::

    >>> pp.create_user_url(username='george_clinton')
    'https://www.periscope.tv/w/1eaKbRMEMEQKX'

    >>> pp.create_user_url(user_id='376827')
    'https://www.periscope.tv/u/376827'


parse_periscope_url(url)
------------------------

Attempts to extract the `broadcast_id`, `user_id`, `username` or a combination
of these from the supplied URL.

Supports the following URL formats:

* https://www.periscope.tv/w/<broadcast_id>
* https://www.periscope.tv/u/<user_id>
* https://www.periscope.tv/<username>
* https://www.periscope.tv/<username>/<broadcast_id>

Example usage::

    >>> pp.parse_periscope_url('https://www.periscope.tv/w/1eaKbRMEMEQKX')
    {'broadcast_id': '1eaKbRMEMEQKX', 'username': None, 'user_id': None}


create_api_request_url(endpoint, **params)
------------------------------------------

Craft a URL to the Periscope API with the supplied endpoint and params.

The params will be added to URL in a consistent, alphabetical order.

Example usage::

    >>> pp.create_api_request_url('getUserPublic', user_id='123456', a='b')
    'https://api.periscope.tv/api/v2/getUserPublic?a=b&user_id=123456'


request_api(endpoint, **params)
-------------------------------

Makes a request to the Periscope API, with the supplied params and returns
the result as a Dict.

Example usage::

    >>> pp.request_api('getUserPublic', user_id='376827')
    {'class_name': 'User',
     'created_at': '2015-03-28T19:52:59.150319197-07:00',
     'description': "It's always gotten better by Thursday. www.georgeclinton.com",
     'display_name': 'George Clinton',
     'id': '376827',
     'initials': '',
     'is_beta_user': False,
     'is_employee': False,
     'is_twitter_verified': True,
     'n_followers': 14535,
     'n_following': 739,
     'n_hearts': 2768274,
     'profile_image_urls': [{'height': 128,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
                             'width': 128},
                            {'height': 200,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_200x200.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_200x200.jpeg',
                             'width': 200},
                            {'height': 400,
                             'ssl_url': 'https://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_400x400.jpeg',
                             'url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_400x400.jpeg',
                             'width': 400}],
     'twitter_id': '23177270',
     'twitter_screen_name': 'george_clinton',
     'username': 'george_clinton'}
