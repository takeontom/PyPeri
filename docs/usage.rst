=====
Usage
=====

Introduction
============

To use PyPeri in a project::

    from pyperi.pyperi import PyPeri
    pp = PyPeri()
    user_info = pp.get_user_info('376827')
    print(user_info['username'])

Outputs::

    george_clinton

The API
=======

get_user_info(<user_id>)
------------------------

Retrieves a dictionary of information about the specified user.

Example usage::

    user_info = pp.get_user_info('376827')

Returns a dict with the following structure::

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
