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


class MediaRootMini(object):
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
        'full_path': 'str',
        'custom_fields': 'list[CustomField]',
        'volume': 'VolumeMini',
        'path': 'str',
        'prefetch_thumbnail_strips': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'full_path': 'full_path',
        'custom_fields': 'custom_fields',
        'volume': 'volume',
        'path': 'path',
        'prefetch_thumbnail_strips': 'prefetch_thumbnail_strips'
    }

    def __init__(self, id=None, name=None, full_path=None, custom_fields=None, volume=None, path=None, prefetch_thumbnail_strips=None, local_vars_configuration=None):  # noqa: E501
        """MediaRootMini - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._full_path = None
        self._custom_fields = None
        self._volume = None
        self._path = None
        self._prefetch_thumbnail_strips = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if full_path is not None:
            self.full_path = full_path
        if custom_fields is not None:
            self.custom_fields = custom_fields
        self.volume = volume
        if path is not None:
            self.path = path
        if prefetch_thumbnail_strips is not None:
            self.prefetch_thumbnail_strips = prefetch_thumbnail_strips

    @property
    def id(self):
        """Gets the id of this MediaRootMini.  # noqa: E501


        :return: The id of this MediaRootMini.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaRootMini.


        :param id: The id of this MediaRootMini.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MediaRootMini.  # noqa: E501


        :return: The name of this MediaRootMini.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaRootMini.


        :param name: The name of this MediaRootMini.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def full_path(self):
        """Gets the full_path of this MediaRootMini.  # noqa: E501


        :return: The full_path of this MediaRootMini.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this MediaRootMini.


        :param full_path: The full_path of this MediaRootMini.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def custom_fields(self):
        """Gets the custom_fields of this MediaRootMini.  # noqa: E501


        :return: The custom_fields of this MediaRootMini.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this MediaRootMini.


        :param custom_fields: The custom_fields of this MediaRootMini.  # noqa: E501
        :type: list[CustomField]
        """

        self._custom_fields = custom_fields

    @property
    def volume(self):
        """Gets the volume of this MediaRootMini.  # noqa: E501


        :return: The volume of this MediaRootMini.  # noqa: E501
        :rtype: VolumeMini
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MediaRootMini.


        :param volume: The volume of this MediaRootMini.  # noqa: E501
        :type: VolumeMini
        """
        if self.local_vars_configuration.client_side_validation and volume is None:  # noqa: E501
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def path(self):
        """Gets the path of this MediaRootMini.  # noqa: E501


        :return: The path of this MediaRootMini.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MediaRootMini.


        :param path: The path of this MediaRootMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) > 255):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `255`")  # noqa: E501

        self._path = path

    @property
    def prefetch_thumbnail_strips(self):
        """Gets the prefetch_thumbnail_strips of this MediaRootMini.  # noqa: E501


        :return: The prefetch_thumbnail_strips of this MediaRootMini.  # noqa: E501
        :rtype: bool
        """
        return self._prefetch_thumbnail_strips

    @prefetch_thumbnail_strips.setter
    def prefetch_thumbnail_strips(self, prefetch_thumbnail_strips):
        """Sets the prefetch_thumbnail_strips of this MediaRootMini.


        :param prefetch_thumbnail_strips: The prefetch_thumbnail_strips of this MediaRootMini.  # noqa: E501
        :type: bool
        """

        self._prefetch_thumbnail_strips = prefetch_thumbnail_strips

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
        if not isinstance(other, MediaRootMini):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaRootMini):
            return True

        return self.to_dict() != other.to_dict()
