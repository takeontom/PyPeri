#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyperi
----------------------------------

Tests for `pyperi` module.
"""

import httpretty
import pytest  # noqa

from pyperi.pyperi import PyPeri


@httpretty.activate
def test_request_api():
    mock_url = (
        'https://api.periscope.tv/api/v2/testEndpoint?'
        'test_param=something&test_param2=else'
    )
    mock_body = '{"test":"ok"}'
    httpretty.register_uri(httpretty.GET, mock_url, mock_body)
    pp = PyPeri()
    result = pp.request_api(
        'testEndpoint', test_param='something', test_param2='else'
    )
    assert result == {'test': 'ok'}


def test_create_api_request_url():
    pp = PyPeri()
    url = pp.create_api_request_url(
        'testEndpoint', test_param='something', test_param2='else'
    )
    assert url == (
        'https://api.periscope.tv/api/v2/testEndpoint?'
        'test_param=something&test_param2=else'
    )

    url_no_params = pp.create_api_request_url('testEndpoint')
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

    pp = PyPeri()
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

    pp = PyPeri()
    result = pp.get_user_info(user_id)
    assert result['id'] == user_id
    assert result['username'] == 'george_clinton'


def test_parse_periscope_url_w():
    pp = PyPeri()
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
    pp = PyPeri()
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
    pp = PyPeri()
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
    pp = PyPeri()
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
    pp = PyPeri()
    broadcast_ids = [
        '1zqKVWybqeDGB',
    ]

    for broadcast_id in broadcast_ids:
        w_url = 'https://www.periscope.tv/w/{broadcast_id}'.format(
            broadcast_id=broadcast_id
        )
        assert pp.parse_periscope_w_url(w_url) == {
            'user_id': None,
            'username': None,
            'broadcast_id': broadcast_id,
        }


def test_parse_periscope_username_url():
    pp = PyPeri()
    usernames = [
        'someusername',
        'some_username',
        'SomeUsername',
    ]

    for username in usernames:
        username_url = 'https://www.periscope.tv/{username}'.format(
            username=username
        )
        assert pp.parse_periscope_username_url(username_url) == {
            'user_id': None,
            'username': username,
            'broadcast_id': None,
        }


def test_parse_periscope_username_broadcast_id_url():
    pp = PyPeri()
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
            assert pp.parse_periscope_username_broadcast_id_url(username_url) == {
                'user_id': None,
                'username': username,
                'broadcast_id': broadcast_id,
            }

    blank_result = {
        'user_id': None,
        'username': None,
        'broadcast_id': None,
    }

    assert pp.parse_periscope_username_broadcast_id_url(
        'https://www.periscope.tv/okUsername/'
    ) == blank_result

    assert pp.parse_periscope_username_broadcast_id_url(
        'https://www.periscope.tv/okUsername/'
    ) == blank_result


def test_parse_periscope_u_url():
    pp = PyPeri()
    user_ids = [
        '376827',
    ]

    for user_id in user_ids:
        url = 'https://www.periscope.tv/u/{user_id}'.format(
            user_id=user_id
        )
        assert pp.parse_periscope_u_url(url) == {
            'username': None,
            'user_id': user_id,
            'broadcast_id': None,
        }
