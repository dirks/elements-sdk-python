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


class MediaFileBundleMini(object):
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
        'asset': 'int',
        'name': 'str',
        'location': 'int',
        'mainfile': 'MediaFileMini'
    }

    attribute_map = {
        'id': 'id',
        'asset': 'asset',
        'name': 'name',
        'location': 'location',
        'mainfile': 'mainfile'
    }

    def __init__(self, id=None, asset=None, name=None, location=None, mainfile=None, local_vars_configuration=None):  # noqa: E501
        """MediaFileBundleMini - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._asset = None
        self._name = None
        self._location = None
        self._mainfile = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.asset = asset
        self.name = name
        self.location = location
        if mainfile is not None:
            self.mainfile = mainfile

    @property
    def id(self):
        """Gets the id of this MediaFileBundleMini.  # noqa: E501


        :return: The id of this MediaFileBundleMini.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaFileBundleMini.


        :param id: The id of this MediaFileBundleMini.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def asset(self):
        """Gets the asset of this MediaFileBundleMini.  # noqa: E501


        :return: The asset of this MediaFileBundleMini.  # noqa: E501
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this MediaFileBundleMini.


        :param asset: The asset of this MediaFileBundleMini.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and asset is None:  # noqa: E501
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def name(self):
        """Gets the name of this MediaFileBundleMini.  # noqa: E501


        :return: The name of this MediaFileBundleMini.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaFileBundleMini.


        :param name: The name of this MediaFileBundleMini.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 1023):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1023`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def location(self):
        """Gets the location of this MediaFileBundleMini.  # noqa: E501


        :return: The location of this MediaFileBundleMini.  # noqa: E501
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MediaFileBundleMini.


        :param location: The location of this MediaFileBundleMini.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def mainfile(self):
        """Gets the mainfile of this MediaFileBundleMini.  # noqa: E501


        :return: The mainfile of this MediaFileBundleMini.  # noqa: E501
        :rtype: MediaFileMini
        """
        return self._mainfile

    @mainfile.setter
    def mainfile(self, mainfile):
        """Sets the mainfile of this MediaFileBundleMini.


        :param mainfile: The mainfile of this MediaFileBundleMini.  # noqa: E501
        :type: MediaFileMini
        """

        self._mainfile = mainfile

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
        if not isinstance(other, MediaFileBundleMini):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaFileBundleMini):
            return True

        return self.to_dict() != other.to_dict()
