#!/usr/bin/env python3i
""" Manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ A class to manage API
    authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Required path """
        if path is None or excluded_paths is None:
            return True
        if excluded_paths == []:
            return True
        if path in excluded_paths or path + \
                '/' in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user """
        return None
