#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyperi
----------------------------------

Tests for `pyperi` module.
"""

import httpretty
import pytest  # noqa

from pyperi import Peri


@httpretty.activate
def test_request_api():
    mock_url = (
        'https://api.periscope.tv/api/v2/testEndpoint?'
        'test_param=something&test_param2=else'
    )
    mock_body = '{"test":"ok"}'
    httpretty.register_uri(httpretty.GET, mock_url, mock_body)
    pp = Peri()
    result = pp.request_api(
        'testEndpoint', test_param='something', test_param2='else'
    )
    assert result == {'test': 'ok'}


def test_create_api_request_url():
    pp = Peri()
    url = pp._create_api_request_url(
        'testEndpoint', test_param='something', test_param2='else'
    )
    assert url == (
        'https://api.periscope.tv/api/v2/testEndpoint?'
        'test_param=something&test_param2=else'
    )

    url_no_params = pp._create_api_request_url('testEndpoint')
    assert url_no_params == 'https://api.periscope.tv/api/v2/testEndpoint?'


@httpretty.activate
def test_get_broadcast_info():
    broadcast_id = '1zqKVWybqeDGB'
    mock_url = (
        'https://api.periscope.tv/api/v2/accessVideoPublic?'
        'broadcast_id={broadcast_id}'
    ).format(broadcast_id=broadcast_id)
    mock_body_file = open('tests/responses/accessVideoPublic.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, mock_url, mock_body)

    pp = Peri()
    result = pp.get_broadcast_info(broadcast_id)
    assert result['id'] == broadcast_id
    assert result['user_id'] == '376827'
    assert result['username'] == 'george_clinton'


@httpretty.activate
def test_get_user_info():
    user_id = '376827'
    mock_url = (
        'https://api.periscope.tv/api/v2/getUserPublic?'
        'user_id={user_id}'
    ).format(user_id=user_id)
    mock_body_file = open('tests/responses/getUserPublic.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, mock_url, mock_body)

    pp = Peri()
    result = pp.get_user_info(user_id)
    assert result['id'] == user_id
    assert result['username'] == 'george_clinton'


@httpretty.activate
def test_get_user_broadcast_history__username():
    user_url = ('https://www.periscope.tv/george_clinton')
    mock_user_file = open('tests/responses/web_username.txt', 'r')
    mock_user_body = mock_user_file.read()
    httpretty.register_uri(httpretty.GET, user_url, mock_user_body)

    url = (
        'https://api.periscope.tv/api/v2/getUserBroadcastsPublic?'
        'user_id={user_id}&all=true&session_id={session}'.format(
            user_id='376827',
            session=(
                '103Aiku2x7oAhlnIYwnmpk6x1FHSedRbvP4SRo0cgjRgEHJ9ud2msVD3Pxcr'
                'gZP7ox5_i18nfbfKzdKBTxrjMjJRTiQ8Um4t6LzFTgTZPADPhY_Mk'
            )
        )
    )
    mock_body_file = open('tests/responses/getUserBroadcastsPublic.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, url, mock_body)

    username = 'george_clinton'
    pp = Peri()
    broadcast_history = pp.get_user_broadcast_history(username=username)

    assert broadcast_history[0]['id'] == '1vAxRdlLBdjGl'

    common_keys = [
        'start', 'ping', 'status', 'user_display_name', 'user_id', 'username',
        'state', 'image_url', 'image_url_small',
    ]
    for broadcast in broadcast_history:
        for key in common_keys:
            assert key in broadcast.keys()


@httpretty.activate
def test_get_user_broadcast_history__user_id():
    user_url = ('https://www.periscope.tv/u/376827')
    mock_user_file = open('tests/responses/web_user_id.txt', 'r')
    mock_user_body = mock_user_file.read()
    httpretty.register_uri(httpretty.GET, user_url, mock_user_body)

    url = (
        'https://api.periscope.tv/api/v2/getUserBroadcastsPublic?'
        'user_id={user_id}&all=true&session_id={session}'.format(
            user_id='376827',
            session=(
                '103Aiku2x7oAhlnIYwnmpk6x1FHSedRbvP4SRo0cgjRgEHJ9ud2msVD3Pxcr'
                'gZP7ox5_i18nfbfKzdKBTxrjMjJRTiQ8Um4t6LzFTgTZPADPhY_Mk'
            )
        )
    )
    mock_body_file = open('tests/responses/getUserBroadcastsPublic.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, url, mock_body)

    user_id = '376827'

    broadcast_histories = []
    pp = Peri()
    broadcast_histories.append(pp.get_user_broadcast_history(user_id=user_id))
    broadcast_histories.append(pp.get_user_broadcast_history(user_id))

    for broadcast_history in broadcast_histories:
        assert broadcast_history[0]['id'] == '1vAxRdlLBdjGl'

        common_keys = [
            'start', 'ping', 'status', 'user_display_name', 'user_id', 'username',
            'state', 'image_url', 'image_url_small',
        ]
        for broadcast in broadcast_history:
            for key in common_keys:
                assert key in broadcast.keys()


@httpretty.activate
def test_get_web_data_store():
    url = ('https://www.periscope.tv/george_clinton')
    mock_body_file = open('tests/responses/web_username.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, url, mock_body)

    pp = Peri()
    data_store = pp._get_web_data_store(url)

    # Check useful session tokens are available
    session_tokens = data_store['SessionToken']
    public_session_tokens = session_tokens['public']
    broadcast_history_session_token = public_session_tokens['broadcastHistory']
    assert broadcast_history_session_token['token']['session_id'] == (
        '103Aiku2x7oAhlnIYwnmpk6x1FHSedRbvP4SRo0cgjRgEHJ9ud2msVD3PxcrgZP7ox5_i'
        '18nfbfKzdKBTxrjMjJRTiQ8Um4t6LzFTgTZPADPhY_Mk'
    )

    # Check we can get the user ID
    assert data_store['Tracking']['userId'] == '376827'


@httpretty.activate
def test_get_web_public_user_session_tokens__username():
    url = ('https://www.periscope.tv/george_clinton')
    mock_body_file = open('tests/responses/web_username.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, url, mock_body)

    pp = Peri()
    tokens = pp.get_web_public_user_session_tokens(username='george_clinton')
    assert tokens['broadcastHistory'] == (
        '103Aiku2x7oAhlnIYwnmpk6x1FHSedRbvP4SRo0cgjRgEHJ9ud2msVD3PxcrgZP7ox5_i'
        '18nfbfKzdKBTxrjMjJRTiQ8Um4t6LzFTgTZPADPhY_Mk'
    )
    assert tokens['user_id'] == '376827'


@httpretty.activate
def test_get_web_public_user_session_tokens__user_id():
    url = ('https://www.periscope.tv/u/376827')
    mock_body_file = open('tests/responses/web_user_id.txt', 'r')
    mock_body = mock_body_file.read()
    httpretty.register_uri(httpretty.GET, url, mock_body)

    pp = Peri()
    tokens = pp.get_web_public_user_session_tokens(user_id='376827')
    assert tokens['broadcastHistory'] == (
        '1LPbupzBov6kqt2N79-0mX8OFzgkyz-yUga5-NnYbJX6ETrEuCBq427H4jVItOvgDkOaEuU5YqsUQ4vS3S6x40ZB'
        'hpaXf0_U0a07g55PlwLAa5Jqz'
    )
    assert tokens['user_id'] == '376827'


def test_create_user_url():
    pp = Peri()

    url = pp.create_user_url('376827')
    assert url == 'https://www.periscope.tv/u/376827'

    url = pp.create_user_url(user_id='376827')
    assert url == 'https://www.periscope.tv/u/376827'

    url = pp.create_user_url(username='george_clinton')
    assert url == 'https://www.periscope.tv/george_clinton'

    with pytest.raises(ValueError):
        pp.create_user_url()


def test_parse_periscope_url_w():
    pp = Peri()
    broadcast_ids = [
        '1zqKVWybqeDGB',
    ]

    for broadcast_id in broadcast_ids:
        w_url = 'https://www.periscope.tv/w/{broadcast_id}'.format(
            broadcast_id=broadcast_id
        )
        assert pp.parse_periscope_url(w_url) == {
            'broadcast_id': broadcast_id, 'user_id': None, 'username': None
        }


def test_parse_periscope_url_username():
    pp = Peri()
    usernames = [
        'someusername',
        'some_username',
        'SomeUsername',
    ]

    for username in usernames:
        username_url = 'https://www.periscope.tv/{username}'.format(
            username=username
        )
        assert pp.parse_periscope_url(username_url) == {
            'broadcast_id': None, 'user_id': None, 'username': username
        }


def test_parse_periscope_url_username_broadcast_id():
    pp = Peri()
    usernames = [
        'someusername',
        'some_username',
        'SomeUsername',
    ]
    broadcast_ids = [
        '1zqKVWybqeDGB',
    ]

    for username in usernames:
        for broadcast_id in broadcast_ids:
            username_url = 'https://www.periscope.tv/{username}/{broadcast_id}'.format(
                username=username,
                broadcast_id=broadcast_id,
            )
            assert pp.parse_periscope_url(username_url) == {
                'user_id': None,
                'username': username,
                'broadcast_id': broadcast_id,
            }


def test_parse_periscope_url_u():
    pp = Peri()
    user_ids = [
        '376827',
    ]

    for user_id in user_ids:
        url = 'https://www.periscope.tv/u/{user_id}'.format(
            user_id=user_id
        )
        assert pp.parse_periscope_url(url) == {
            'username': None,
            'user_id': user_id,
            'broadcast_id': None,
        }


def test_parse_periscope_w_url():
    pp = Peri()
    broadcast_ids = [
        '1zqKVWybqeDGB',
    ]

    for broadcast_id in broadcast_ids:
        w_url = 'https://www.periscope.tv/w/{broadcast_id}'.format(
            broadcast_id=broadcast_id
        )
        assert pp._parse_periscope_w_url(w_url) == {
            'user_id': None,
            'username': None,
            'broadcast_id': broadcast_id,
        }


def test_parse_periscope_username_url():
    pp = Peri()
    usernames = [
        'someusername',
        'some_username',
        'SomeUsername',
    ]

    for username in usernames:
        username_url = 'https://www.periscope.tv/{username}'.format(
            username=username
        )
        assert pp._parse_periscope_username_url(username_url) == {
            'user_id': None,
            'username': username,
            'broadcast_id': None,
        }


def test_parse_periscope_username_broadcast_id_url():
    pp = Peri()
    usernames = [
        'someusername',
        'some_username',
        'SomeUsername',
    ]
    broadcast_ids = [
        '1zqKVWybqeDGB',
    ]

    for username in usernames:
        for broadcast_id in broadcast_ids:
            username_url = 'https://www.periscope.tv/{username}/{broadcast_id}'.format(
                username=username,
                broadcast_id=broadcast_id,
            )
            assert pp._parse_periscope_username_broadcast_id_url(username_url) == {
                'user_id': None,
                'username': username,
                'broadcast_id': broadcast_id,
            }

    blank_result = {
        'user_id': None,
        'username': None,
        'broadcast_id': None,
    }

    assert pp._parse_periscope_username_broadcast_id_url(
        'https://www.periscope.tv/okUsername/'
    ) == blank_result

    assert pp._parse_periscope_username_broadcast_id_url(
        'https://www.periscope.tv/okUsername/'
    ) == blank_result


def test_parse_periscope_u_url():
    pp = Peri()
    user_ids = [
        '376827',
    ]

    for user_id in user_ids:
        url = 'https://www.periscope.tv/u/{user_id}'.format(
            user_id=user_id
        )
        assert pp._parse_periscope_u_url(url) == {
            'username': None,
            'user_id': user_id,
            'broadcast_id': None,
        }
