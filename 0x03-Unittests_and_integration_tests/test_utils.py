#!/usr/bin/env python3
'''implementing test cases for access_nested_map function.'''

import unittest
import requests
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''initializing TestAccessNestedMap class.'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''test function for access_nested_map.'''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''test function for access_nested_map KeyError exception.'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''initializing class TestGetJson.'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, requests_get_mock):
        '''mocking a HTTP request to test the functionality of our endpoint'''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        requests_get_mock.return_value = mock_response

        result = get_json(test_url)

        self.assertEqual(requests_get_mock.call_count, 1)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''initializing class TestMemoize.'''
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        '''testing memoize decorator.'''
        test_instance = self.TestClass()
        with patch.object(test_instance, 'a_method',
             return_value=42) as mock_a_method:

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()
