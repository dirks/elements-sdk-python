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


class StorageNode(object):
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
        'name': 'str',
        'address': 'str',
        'address_override': 'str',
        'backend': 'Backend',
        'type': 'int',
        'ipmi': 'int',
        'interfaces': 'list[Interface]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'address_override': 'address_override',
        'backend': 'backend',
        'type': 'type',
        'ipmi': 'ipmi',
        'interfaces': 'interfaces'
    }

    def __init__(self, id=None, name=None, address=None, address_override=None, backend=None, type=None, ipmi=None, interfaces=None, local_vars_configuration=None):  # noqa: E501
        """StorageNode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._address = None
        self._address_override = None
        self._backend = None
        self._type = None
        self._ipmi = None
        self._interfaces = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        self.address_override = address_override
        if backend is not None:
            self.backend = backend
        if type is not None:
            self.type = type
        if ipmi is not None:
            self.ipmi = ipmi
        if interfaces is not None:
            self.interfaces = interfaces

    @property
    def id(self):
        """Gets the id of this StorageNode.  # noqa: E501


        :return: The id of this StorageNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageNode.


        :param id: The id of this StorageNode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StorageNode.  # noqa: E501


        :return: The name of this StorageNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageNode.


        :param name: The name of this StorageNode.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this StorageNode.  # noqa: E501

        For communication between nodes only  # noqa: E501

        :return: The address of this StorageNode.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StorageNode.

        For communication between nodes only  # noqa: E501

        :param address: The address of this StorageNode.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address is not None and len(address) > 255):
            raise ValueError("Invalid value for `address`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                address is not None and len(address) < 1):
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `1`")  # noqa: E501

        self._address = address

    @property
    def address_override(self):
        """Gets the address_override of this StorageNode.  # noqa: E501

        Enforces mounting from a specific address/hostname instead of the available interfaces  # noqa: E501

        :return: The address_override of this StorageNode.  # noqa: E501
        :rtype: str
        """
        return self._address_override

    @address_override.setter
    def address_override(self, address_override):
        """Sets the address_override of this StorageNode.

        Enforces mounting from a specific address/hostname instead of the available interfaces  # noqa: E501

        :param address_override: The address_override of this StorageNode.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_override is not None and len(address_override) > 255):
            raise ValueError("Invalid value for `address_override`, length must be less than or equal to `255`")  # noqa: E501

        self._address_override = address_override

    @property
    def backend(self):
        """Gets the backend of this StorageNode.  # noqa: E501


        :return: The backend of this StorageNode.  # noqa: E501
        :rtype: Backend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this StorageNode.


        :param backend: The backend of this StorageNode.  # noqa: E501
        :type: Backend
        """

        self._backend = backend

    @property
    def type(self):
        """Gets the type of this StorageNode.  # noqa: E501


        :return: The type of this StorageNode.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StorageNode.


        :param type: The type of this StorageNode.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def ipmi(self):
        """Gets the ipmi of this StorageNode.  # noqa: E501


        :return: The ipmi of this StorageNode.  # noqa: E501
        :rtype: int
        """
        return self._ipmi

    @ipmi.setter
    def ipmi(self, ipmi):
        """Sets the ipmi of this StorageNode.


        :param ipmi: The ipmi of this StorageNode.  # noqa: E501
        :type: int
        """

        self._ipmi = ipmi

    @property
    def interfaces(self):
        """Gets the interfaces of this StorageNode.  # noqa: E501


        :return: The interfaces of this StorageNode.  # noqa: E501
        :rtype: list[Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this StorageNode.


        :param interfaces: The interfaces of this StorageNode.  # noqa: E501
        :type: list[Interface]
        """

        self._interfaces = interfaces

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
        if not isinstance(other, StorageNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageNode):
            return True

        return self.to_dict() != other.to_dict()
