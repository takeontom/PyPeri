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


parse_periscope_url(url)
------------------------

Attempts to extract the `broadcast_id`, `user_id`, `username` or a combination
of these from the supplied URL.

Supports the following URL formats:

* https://www.periscope.tv/w/<broadcast_id>

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
