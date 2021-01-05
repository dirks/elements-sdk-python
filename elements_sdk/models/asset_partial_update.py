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


class AssetPartialUpdate(object):
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
        'custom_fields': 'dict(str, str)',
        'tags': 'list[Tag]',
        'set': 'int'
    }

    attribute_map = {
        'custom_fields': 'custom_fields',
        'tags': 'tags',
        'set': 'set'
    }

    def __init__(self, custom_fields=None, tags=None, set=None, local_vars_configuration=None):  # noqa: E501
        """AssetPartialUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._custom_fields = None
        self._tags = None
        self._set = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if tags is not None:
            self.tags = tags
        self.set = set

    @property
    def custom_fields(self):
        """Gets the custom_fields of this AssetPartialUpdate.  # noqa: E501


        :return: The custom_fields of this AssetPartialUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this AssetPartialUpdate.


        :param custom_fields: The custom_fields of this AssetPartialUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_fields = custom_fields

    @property
    def tags(self):
        """Gets the tags of this AssetPartialUpdate.  # noqa: E501


        :return: The tags of this AssetPartialUpdate.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AssetPartialUpdate.


        :param tags: The tags of this AssetPartialUpdate.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def set(self):
        """Gets the set of this AssetPartialUpdate.  # noqa: E501


        :return: The set of this AssetPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._set

    @set.setter
    def set(self, set):
        """Sets the set of this AssetPartialUpdate.


        :param set: The set of this AssetPartialUpdate.  # noqa: E501
        :type: int
        """

        self._set = set

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
        if not isinstance(other, AssetPartialUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetPartialUpdate):
            return True

        return self.to_dict() != other.to_dict()
