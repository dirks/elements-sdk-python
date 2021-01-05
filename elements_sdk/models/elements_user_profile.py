# coding: utf-8

"""
    ELEMENTS API

    The version of the OpenAPI document: 2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from elements_sdk.configuration import Configuration


class ElementsUserProfile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'avatar': 'str',
        'default_page': 'str',
        'full_name': 'str',
        'language': 'str',
        'fm_bookmarks': 'list[str]',
        'id': 'int',
        'username': 'str',
        'unix_username': 'str',
        'display_name': 'str',
        'email': 'str',
        'ldap': 'LDAPServer',
        'effective_permissions': 'list[str]'
    }

    attribute_map = {
        'avatar': 'avatar',
        'default_page': 'default_page',
        'full_name': 'full_name',
        'language': 'language',
        'fm_bookmarks': 'fm_bookmarks',
        'id': 'id',
        'username': 'username',
        'unix_username': 'unix_username',
        'display_name': 'display_name',
        'email': 'email',
        'ldap': 'ldap',
        'effective_permissions': 'effective_permissions'
    }

    def __init__(self, avatar=None, default_page=None, full_name=None, language=None, fm_bookmarks=None, id=None, username=None, unix_username=None, display_name=None, email=None, ldap=None, effective_permissions=None, local_vars_configuration=None):  # noqa: E501
        """ElementsUserProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._avatar = None
        self._default_page = None
        self._full_name = None
        self._language = None
        self._fm_bookmarks = None
        self._id = None
        self._username = None
        self._unix_username = None
        self._display_name = None
        self._email = None
        self._ldap = None
        self._effective_permissions = None
        self.discriminator = None

        self.avatar = avatar
        if default_page is not None:
            self.default_page = default_page
        self.full_name = full_name
        self.language = language
        if fm_bookmarks is not None:
            self.fm_bookmarks = fm_bookmarks
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if unix_username is not None:
            self.unix_username = unix_username
        if display_name is not None:
            self.display_name = display_name
        if email is not None:
            self.email = email
        self.ldap = ldap
        if effective_permissions is not None:
            self.effective_permissions = effective_permissions

    @property
    def avatar(self):
        """Gets the avatar of this ElementsUserProfile.  # noqa: E501


        :return: The avatar of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this ElementsUserProfile.


        :param avatar: The avatar of this ElementsUserProfile.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def default_page(self):
        """Gets the default_page of this ElementsUserProfile.  # noqa: E501


        :return: The default_page of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._default_page

    @default_page.setter
    def default_page(self, default_page):
        """Sets the default_page of this ElementsUserProfile.


        :param default_page: The default_page of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_page is not None and len(default_page) > 63):
            raise ValueError("Invalid value for `default_page`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                default_page is not None and len(default_page) < 1):
            raise ValueError("Invalid value for `default_page`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_page = default_page

    @property
    def full_name(self):
        """Gets the full_name of this ElementsUserProfile.  # noqa: E501


        :return: The full_name of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ElementsUserProfile.


        :param full_name: The full_name of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                full_name is not None and len(full_name) > 255):
            raise ValueError("Invalid value for `full_name`, length must be less than or equal to `255`")  # noqa: E501

        self._full_name = full_name

    @property
    def language(self):
        """Gets the language of this ElementsUserProfile.  # noqa: E501


        :return: The language of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ElementsUserProfile.


        :param language: The language of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"en", "de", "ru"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def fm_bookmarks(self):
        """Gets the fm_bookmarks of this ElementsUserProfile.  # noqa: E501


        :return: The fm_bookmarks of this ElementsUserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._fm_bookmarks

    @fm_bookmarks.setter
    def fm_bookmarks(self, fm_bookmarks):
        """Sets the fm_bookmarks of this ElementsUserProfile.


        :param fm_bookmarks: The fm_bookmarks of this ElementsUserProfile.  # noqa: E501
        :type: list[str]
        """

        self._fm_bookmarks = fm_bookmarks

    @property
    def id(self):
        """Gets the id of this ElementsUserProfile.  # noqa: E501


        :return: The id of this ElementsUserProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElementsUserProfile.


        :param id: The id of this ElementsUserProfile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this ElementsUserProfile.  # noqa: E501


        :return: The username of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ElementsUserProfile.


        :param username: The username of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def unix_username(self):
        """Gets the unix_username of this ElementsUserProfile.  # noqa: E501


        :return: The unix_username of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._unix_username

    @unix_username.setter
    def unix_username(self, unix_username):
        """Sets the unix_username of this ElementsUserProfile.


        :param unix_username: The unix_username of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unix_username is not None and len(unix_username) < 1):
            raise ValueError("Invalid value for `unix_username`, length must be greater than or equal to `1`")  # noqa: E501

        self._unix_username = unix_username

    @property
    def display_name(self):
        """Gets the display_name of this ElementsUserProfile.  # noqa: E501


        :return: The display_name of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ElementsUserProfile.


        :param display_name: The display_name of this ElementsUserProfile.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this ElementsUserProfile.  # noqa: E501


        :return: The email of this ElementsUserProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ElementsUserProfile.


        :param email: The email of this ElementsUserProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def ldap(self):
        """Gets the ldap of this ElementsUserProfile.  # noqa: E501


        :return: The ldap of this ElementsUserProfile.  # noqa: E501
        :rtype: LDAPServer
        """
        return self._ldap

    @ldap.setter
    def ldap(self, ldap):
        """Sets the ldap of this ElementsUserProfile.


        :param ldap: The ldap of this ElementsUserProfile.  # noqa: E501
        :type: LDAPServer
        """
        if self.local_vars_configuration.client_side_validation and ldap is None:  # noqa: E501
            raise ValueError("Invalid value for `ldap`, must not be `None`")  # noqa: E501

        self._ldap = ldap

    @property
    def effective_permissions(self):
        """Gets the effective_permissions of this ElementsUserProfile.  # noqa: E501


        :return: The effective_permissions of this ElementsUserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """Sets the effective_permissions of this ElementsUserProfile.


        :param effective_permissions: The effective_permissions of this ElementsUserProfile.  # noqa: E501
        :type: list[str]
        """

        self._effective_permissions = effective_permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ElementsUserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementsUserProfile):
            return True

        return self.to_dict() != other.to_dict()
