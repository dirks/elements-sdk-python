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


class ProductionPartialUpdate(object):
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
        'name': 'str',
        'obscure_name': 'bool',
        'description': 'str',
        'long_description': 'str',
        'active': 'bool',
        'template': 'int',
        'default_group': 'int'
    }

    attribute_map = {
        'name': 'name',
        'obscure_name': 'obscure_name',
        'description': 'description',
        'long_description': 'long_description',
        'active': 'active',
        'template': 'template',
        'default_group': 'default_group'
    }

    def __init__(self, name=None, obscure_name=None, description=None, long_description=None, active=None, template=None, default_group=None, local_vars_configuration=None):  # noqa: E501
        """ProductionPartialUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._obscure_name = None
        self._description = None
        self._long_description = None
        self._active = None
        self._template = None
        self._default_group = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if obscure_name is not None:
            self.obscure_name = obscure_name
        self.description = description
        if long_description is not None:
            self.long_description = long_description
        if active is not None:
            self.active = active
        self.template = template
        self.default_group = default_group

    @property
    def name(self):
        """Gets the name of this ProductionPartialUpdate.  # noqa: E501


        :return: The name of this ProductionPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductionPartialUpdate.


        :param name: The name of this ProductionPartialUpdate.  # noqa: E501
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
    def obscure_name(self):
        """Gets the obscure_name of this ProductionPartialUpdate.  # noqa: E501


        :return: The obscure_name of this ProductionPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._obscure_name

    @obscure_name.setter
    def obscure_name(self, obscure_name):
        """Sets the obscure_name of this ProductionPartialUpdate.


        :param obscure_name: The obscure_name of this ProductionPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._obscure_name = obscure_name

    @property
    def description(self):
        """Gets the description of this ProductionPartialUpdate.  # noqa: E501


        :return: The description of this ProductionPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductionPartialUpdate.


        :param description: The description of this ProductionPartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def long_description(self):
        """Gets the long_description of this ProductionPartialUpdate.  # noqa: E501


        :return: The long_description of this ProductionPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this ProductionPartialUpdate.


        :param long_description: The long_description of this ProductionPartialUpdate.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def active(self):
        """Gets the active of this ProductionPartialUpdate.  # noqa: E501


        :return: The active of this ProductionPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ProductionPartialUpdate.


        :param active: The active of this ProductionPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def template(self):
        """Gets the template of this ProductionPartialUpdate.  # noqa: E501


        :return: The template of this ProductionPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ProductionPartialUpdate.


        :param template: The template of this ProductionPartialUpdate.  # noqa: E501
        :type: int
        """

        self._template = template

    @property
    def default_group(self):
        """Gets the default_group of this ProductionPartialUpdate.  # noqa: E501


        :return: The default_group of this ProductionPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this ProductionPartialUpdate.


        :param default_group: The default_group of this ProductionPartialUpdate.  # noqa: E501
        :type: int
        """

        self._default_group = default_group

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
        if not isinstance(other, ProductionPartialUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductionPartialUpdate):
            return True

        return self.to_dict() != other.to_dict()