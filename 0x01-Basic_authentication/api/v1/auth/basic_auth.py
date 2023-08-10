#!/usr/bin/env python3
""" A module for Basic Authentication """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Perform Basic Auth """
    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """
            Extract header in base64

            Args:
                authorization_header: string in base64

            Return:
                Header in base64 or None
        """
        if authorization_header is None\
           or type(authorization_header) != str\
           or not authorization_header.startswith('Basic ')\
           and not authorization_header.endswith(' '):

            return None

        return authorization_header.split(' ')[1]
