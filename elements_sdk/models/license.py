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


class License(object):
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
        'product': 'str',
        'hardware_key': 'str',
        'rdc_slots': 'int',
        'expires': 'datetime',
        'components': 'dict(str, bool)',
        'components_license': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'product': 'product',
        'hardware_key': 'hardware_key',
        'rdc_slots': 'rdc_slots',
        'expires': 'expires',
        'components': 'components',
        'components_license': 'components_license'
    }

    def __init__(self, name=None, product=None, hardware_key=None, rdc_slots=None, expires=None, components=None, components_license=None, local_vars_configuration=None):  # noqa: E501
        """License - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._product = None
        self._hardware_key = None
        self._rdc_slots = None
        self._expires = None
        self._components = None
        self._components_license = None
        self.discriminator = None

        self.name = name
        self.product = product
        self.hardware_key = hardware_key
        self.rdc_slots = rdc_slots
        self.expires = expires
        self.components = components
        self.components_license = components_license

    @property
    def name(self):
        """Gets the name of this License.  # noqa: E501


        :return: The name of this License.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this License.


        :param name: The name of this License.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def product(self):
        """Gets the product of this License.  # noqa: E501


        :return: The product of this License.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this License.


        :param product: The product of this License.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                product is not None and len(product) < 1):
            raise ValueError("Invalid value for `product`, length must be greater than or equal to `1`")  # noqa: E501

        self._product = product

    @property
    def hardware_key(self):
        """Gets the hardware_key of this License.  # noqa: E501


        :return: The hardware_key of this License.  # noqa: E501
        :rtype: str
        """
        return self._hardware_key

    @hardware_key.setter
    def hardware_key(self, hardware_key):
        """Sets the hardware_key of this License.


        :param hardware_key: The hardware_key of this License.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hardware_key is None:  # noqa: E501
            raise ValueError("Invalid value for `hardware_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware_key is not None and len(hardware_key) < 1):
            raise ValueError("Invalid value for `hardware_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._hardware_key = hardware_key

    @property
    def rdc_slots(self):
        """Gets the rdc_slots of this License.  # noqa: E501


        :return: The rdc_slots of this License.  # noqa: E501
        :rtype: int
        """
        return self._rdc_slots

    @rdc_slots.setter
    def rdc_slots(self, rdc_slots):
        """Sets the rdc_slots of this License.


        :param rdc_slots: The rdc_slots of this License.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and rdc_slots is None:  # noqa: E501
            raise ValueError("Invalid value for `rdc_slots`, must not be `None`")  # noqa: E501

        self._rdc_slots = rdc_slots

    @property
    def expires(self):
        """Gets the expires of this License.  # noqa: E501


        :return: The expires of this License.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this License.


        :param expires: The expires of this License.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and expires is None:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

    @property
    def components(self):
        """Gets the components of this License.  # noqa: E501


        :return: The components of this License.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this License.


        :param components: The components of this License.  # noqa: E501
        :type: dict(str, bool)
        """
        if self.local_vars_configuration.client_side_validation and components is None:  # noqa: E501
            raise ValueError("Invalid value for `components`, must not be `None`")  # noqa: E501

        self._components = components

    @property
    def components_license(self):
        """Gets the components_license of this License.  # noqa: E501


        :return: The components_license of this License.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._components_license

    @components_license.setter
    def components_license(self, components_license):
        """Sets the components_license of this License.


        :param components_license: The components_license of this License.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and components_license is None:  # noqa: E501
            raise ValueError("Invalid value for `components_license`, must not be `None`")  # noqa: E501

        self._components_license = components_license

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
        if not isinstance(other, License):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, License):
            return True

        return self.to_dict() != other.to_dict()
