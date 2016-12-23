=====
Usage
=====

Introduction
============

To use PyPeri in a project::

    >>> from pyperi import Peri
    >>> pp = Peri()
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
If all goes well, it will return a List containing Dicts of broadcast history.

Example usage::

    >>> pp.get_user_broadcast_history(username='george_clinton')
    [
        {'available_for_replay': True,
        'camera_rotation': 0,
        'city': 'Lake Hiawatha, NJ',
        'class_name': 'Broadcast',
        'country': 'United States',
        'country_state': '',
        'created_at': '2016-05-27T20:03:44.732179203-07:00',
        'end': '2016-05-27T20:10:34.727278696-07:00',
        'expiration': -1,
        'featured': False,
        'friend_chat': False,
        'has_location': True,
        'has_moderation': False,
        'height': 568,
        'id': '1YqGoOkLbLAGv',
        'image_url': 'https://tn.periscope.tv/x4AraTkCeWbW6CyWIQXoYrer45aCkUJZML7TdClEUrPD62GMRa8RE4ztZpvt-3nBxp-eoZTZa9hEagUpQy9U9Q==/chunk_94.jpg?Expires=1779765037&Signature=X3idH7qrnCykvVYqlThNFa-z-i9g~mH7AUi8Lm5XdfuZwbV10GOh52xtGnfR5B45n4l0xSdz2Vz66rijM0QbimzPrUjyD09Gu72nNj2JPZzxOK3YZSjIZFDwzJLi71WO7L5I051k7mFwYj5l4~s2JmXr9TM5ZHiRkQTZ72sBYLIYJ6tmiWnWDAPE6wwcJ0ZIJfVqHyL8mRBGw5J4eFfbYe8JO7CkiDtNaQBI1H7n8BgzbnAqdU1J0k9kUErFdHgdi6gD-RAnPvhQOFmA2lTdVhha2LHRs4gCIR9GNSL9PLNzyYqBnaxtH2Jo4sZPNsymZhYgklF7GOc7YS7KhmSilg__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
        'image_url_small': 'https://tn.periscope.tv/x4AraTkCeWbW6CyWIQXoYrer45aCkUJZML7TdClEUrPD62GMRa8RE4ztZpvt-3nBxp-eoZTZa9hEagUpQy9U9Q==/chunk_94_thumb_128.jpg?Expires=1779765037&Signature=RwiKlnFJZrhkkZCSkNcJaaLlK~PwFEeCZH8Df-IoPt6FCxQZ-oVXGJzPMePl0Hm-4FxuzHyZDREBNlvnJof5qRPYR7TL9QPEtAstLDbidUqnXSKMNs-gLUqMv5P7VP~mAckViUW4nKv6kVxnX8XHuHFJkDbCGyX8c3lIkCUOt~Wk1nV0OzdHC72KJrwcR~9752EQYSBKJxATlcYM0gTEPLDk8CGDuGqWS211D7ATcnfJcNJ9a8NliNSFPQTXsa2ue5vaPPlWsjpLX8sQCJq-2SYbIHsDw7csmoPEMCYW-40jiSoLdSYbE4h9Xvjg0JupPrfjB9I6f3OfE8YrKVLJDQ__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
        'ip_lat': 40.862,
        'ip_lng': -74.412,
        'is_locked': False,
        'iso_code': 'US',
        'language': 'en',
        'n_total_watched': 529,
        'n_total_watching': 0,
        'n_watching': 0,
        'n_web_watching': 0,
        'ping': '2016-05-27T20:10:29.619904440-07:00',
        'profile_image_url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
        'start': '2016-05-27T20:04:44.636015867-07:00',
        'state': 'ENDED',
        'status': '#George Clinton',
        'tags': ['George'],
        'twitter_username': 'george_clinton',
        'updated_at': '2016-05-27T20:10:37.315814298-07:00',
        'user_display_name': 'George Clinton',
        'user_id': '376827',
        'username': 'george_clinton',
        'width': 320},
        {'available_for_replay': True,
        'camera_rotation': 0,
        'city': '',
        'class_name': 'Broadcast',
        'country': '',
        'country_state': '',
        'created_at': '2016-05-27T15:06:18.751291780-07:00',
        'end': '2016-05-27T15:12:58.781942930-07:00',
        'expiration': -1,
        'featured': False,
        'friend_chat': False,
        'has_location': False,
        'has_moderation': False,
        'height': 568,
        'id': '1nAKEnBDXXnGL',
        'image_url': 'https://tn.periscope.tv/eurvYFivZmErfex_Bnj33ESp711ZJPTfUC_KDr5p7xfRuEl77eusMM59moAk00cBb7nI_U8orb95ivVVprgUkA==/chunk_96.jpg?Expires=1779747181&Signature=XWyaURZLs808ds7u-vhmhpcf8zHjkWF~6Jg9kwbdASu4Do7kUOjw11qNQodPfA3EtCFvE5ClN7Jvyt7lSzIArdp7VS5XlULPepu9YoIXBMRaB7RNeL7aIwNSrv3o3yw3ryZAoCyloG31H-hqOjLsFSQBXkfrmC-pQM~wgwsJp41wSQDx8HSGjkPzh7U1MOBc6Nvf4KCvHgpVhSHtmkkGRRsXjVVJLQ0qEpws0GjMYC-hRuzSdf8~9p4BwwPpAO79Cdl0w8haSKsxd9MI4F8JgdU1AtnyP575t7HZQH1wCk3b97U3F2fTm1ij0l-RX6Y8ivnDnUcXIoB7j3ZTvt1piA__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
        'image_url_small': 'https://tn.periscope.tv/eurvYFivZmErfex_Bnj33ESp711ZJPTfUC_KDr5p7xfRuEl77eusMM59moAk00cBb7nI_U8orb95ivVVprgUkA==/chunk_96_thumb_128.jpg?Expires=1779747181&Signature=a5KZMriA7-CoEYXCpHWU2j4TM~1WkZof-wpeQtDsgO9haZcUL0qQy5hiuPWcGOD3IiYCAegYfRzZtaAgO78qM0QkbKZl5vEZLenXHep16ZB4qQAiDXBayN2fIqWKpAIefTPpT-l11NZgs9JfWGOn4LZ2KDzGl7du1ZqwoViP56b1B2evPCAH0HSXgUhfvE4lcoBkunBwamK1amy8rDCTe-u9kI3vqV~bN500RxbfiKyYeZW8ukwjqtYMSilPFilmlv8znaBXNiRA4lsOG4XGJC0xuHQ46JD0Wp5T85gH-UH6Faqq0bh~aTOesVo~lRd9v0y6Uo3yIZGHK~vEz9McJw__&Key-Pair-Id=APKAIHCXHHQVRTVSFRWQ',
        'ip_lat': 0,
        'ip_lng': 0,
        'is_locked': False,
        'iso_code': '',
        'language': 'en',
        'n_total_watched': 1643,
        'n_total_watching': 0,
        'n_watching': 0,
        'n_web_watching': 0,
        'ping': '2016-05-27T15:12:48.828646925-07:00',
        'profile_image_url': 'http://pbs.twimg.com/profile_images/482413674338869248/7GBlIsEm_reasonably_small.jpeg',
        'start': '2016-05-27T15:06:52.018796186-07:00',
        'state': 'ENDED',
        'status': '#George Clinton talking with driver',
        'tags': ['George'],
        'twitter_username': 'george_clinton',
        'updated_at': '2016-05-27T15:13:01.172799853-07:00',
        'user_display_name': 'George Clinton',
        'user_id': '376827',
        'username': 'george_clinton',
        'width': 320}
    ]


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

For convenience, it will also contain the User ID to which the tokens give
access to.

Example usage::

    >>> pp.get_web_public_user_session_tokens(username='george_clinton')
    {
        'broadcastHistory': '17f710-p1JiBEUn0sEib_RdubMEIlN97QWGNF8BJ4eyajbdvMr4sIlwtDHQceV2yYnxSyCg4otO1Hf5eIRP7vzRKMnztRhTbW2WU6KBJ_R6vt9rSJ',
        'serviceToken': '1-FeXtdwxPTDokFl0ZIoJVMN_9d2Pb5IdaaIx_XrX40fQWAm-nbT6ga0Kk_0_QJhWB7ZlqGuuT-Cl3BFu0okWRRenAAHi1NreE0FX2Q5AfMfT',
        'thumbnailPlaylist': '1B4NxFGPCQH1IunHtK5cRWOkkbifgOK7Ipsx8uC9k_WfKC6m1AU6MpnC5cKzxivdnJHC4ngY0EespKKzOzSTn49woz56N9YIuyNkl3Ao977oeC-uvY_xrxXW5',
        'user_id': '376827'
    }


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


request_api(endpoint, \*\*params)
---------------------------------

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
