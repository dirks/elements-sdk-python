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


class Address(object):
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
        'id': 'int',
        'address': 'str',
        'use_for_mounts': 'bool',
        'priority': 'int',
        'network': 'int',
        'interface': 'int'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'use_for_mounts': 'use_for_mounts',
        'priority': 'priority',
        'network': 'network',
        'interface': 'interface'
    }

    def __init__(self, id=None, address=None, use_for_mounts=None, priority=None, network=None, interface=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._address = None
        self._use_for_mounts = None
        self._priority = None
        self._network = None
        self._interface = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.address = address
        if use_for_mounts is not None:
            self.use_for_mounts = use_for_mounts
        if priority is not None:
            self.priority = priority
        self.network = network
        self.interface = interface

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501


        :return: The id of this Address.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.


        :param id: The id of this Address.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this Address.  # noqa: E501


        :return: The address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Address.


        :param address: The address of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                address is not None and len(address) > 255):
            raise ValueError("Invalid value for `address`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                address is not None and len(address) < 1):
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `1`")  # noqa: E501

        self._address = address

    @property
    def use_for_mounts(self):
        """Gets the use_for_mounts of this Address.  # noqa: E501


        :return: The use_for_mounts of this Address.  # noqa: E501
        :rtype: bool
        """
        return self._use_for_mounts

    @use_for_mounts.setter
    def use_for_mounts(self, use_for_mounts):
        """Sets the use_for_mounts of this Address.


        :param use_for_mounts: The use_for_mounts of this Address.  # noqa: E501
        :type: bool
        """

        self._use_for_mounts = use_for_mounts

    @property
    def priority(self):
        """Gets the priority of this Address.  # noqa: E501


        :return: The priority of this Address.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Address.


        :param priority: The priority of this Address.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                priority is not None and priority > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                priority is not None and priority < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._priority = priority

    @property
    def network(self):
        """Gets the network of this Address.  # noqa: E501


        :return: The network of this Address.  # noqa: E501
        :rtype: int
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Address.


        :param network: The network of this Address.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def interface(self):
        """Gets the interface of this Address.  # noqa: E501


        :return: The interface of this Address.  # noqa: E501
        :rtype: int
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this Address.


        :param interface: The interface of this Address.  # noqa: E501
        :type: int
        """

        self._interface = interface

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()