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


class VolumeStat(object):
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
        'time': 'int',
        'c_total': 'float',
        'c_used': 'float'
    }

    attribute_map = {
        'time': 'time',
        'c_total': 'c_total',
        'c_used': 'c_used'
    }

    def __init__(self, time=None, c_total=None, c_used=None, local_vars_configuration=None):  # noqa: E501
        """VolumeStat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._c_total = None
        self._c_used = None
        self.discriminator = None

        self.time = time
        self.c_total = c_total
        self.c_used = c_used

    @property
    def time(self):
        """Gets the time of this VolumeStat.  # noqa: E501


        :return: The time of this VolumeStat.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VolumeStat.


        :param time: The time of this VolumeStat.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and time is None:  # noqa: E501
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def c_total(self):
        """Gets the c_total of this VolumeStat.  # noqa: E501


        :return: The c_total of this VolumeStat.  # noqa: E501
        :rtype: float
        """
        return self._c_total

    @c_total.setter
    def c_total(self, c_total):
        """Sets the c_total of this VolumeStat.


        :param c_total: The c_total of this VolumeStat.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and c_total is None:  # noqa: E501
            raise ValueError("Invalid value for `c_total`, must not be `None`")  # noqa: E501

        self._c_total = c_total

    @property
    def c_used(self):
        """Gets the c_used of this VolumeStat.  # noqa: E501


        :return: The c_used of this VolumeStat.  # noqa: E501
        :rtype: float
        """
        return self._c_used

    @c_used.setter
    def c_used(self, c_used):
        """Sets the c_used of this VolumeStat.


        :param c_used: The c_used of this VolumeStat.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and c_used is None:  # noqa: E501
            raise ValueError("Invalid value for `c_used`, must not be `None`")  # noqa: E501

        self._c_used = c_used

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
        if not isinstance(other, VolumeStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeStat):
            return True

        return self.to_dict() != other.to_dict()
