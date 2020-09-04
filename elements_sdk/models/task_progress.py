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


class TaskProgress(object):
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
        'message': 'str',
        'current': 'int',
        'max': 'int'
    }

    attribute_map = {
        'message': 'message',
        'current': 'current',
        'max': 'max'
    }

    def __init__(self, message=None, current=None, max=None, local_vars_configuration=None):  # noqa: E501
        """TaskProgress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._current = None
        self._max = None
        self.discriminator = None

        self.message = message
        self.current = current
        self.max = max

    @property
    def message(self):
        """Gets the message of this TaskProgress.  # noqa: E501


        :return: The message of this TaskProgress.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TaskProgress.


        :param message: The message of this TaskProgress.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def current(self):
        """Gets the current of this TaskProgress.  # noqa: E501


        :return: The current of this TaskProgress.  # noqa: E501
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this TaskProgress.


        :param current: The current of this TaskProgress.  # noqa: E501
        :type: int
        """

        self._current = current

    @property
    def max(self):
        """Gets the max of this TaskProgress.  # noqa: E501


        :return: The max of this TaskProgress.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this TaskProgress.


        :param max: The max of this TaskProgress.  # noqa: E501
        :type: int
        """

        self._max = max

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
        if not isinstance(other, TaskProgress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskProgress):
            return True

        return self.to_dict() != other.to_dict()
