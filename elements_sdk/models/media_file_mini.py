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


class MediaFileMini(object):
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
        'bundle': 'int',
        'full_path': 'str',
        'custom_fields': 'object',
        'mtime': 'int',
        'parent': 'dict(str, str)',
        'path': 'str',
        'present': 'bool',
        'size': 'int',
        'volume': 'VolumeMini'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bundle': 'bundle',
        'full_path': 'full_path',
        'custom_fields': 'custom_fields',
        'mtime': 'mtime',
        'parent': 'parent',
        'path': 'path',
        'present': 'present',
        'size': 'size',
        'volume': 'volume'
    }

    def __init__(self, id=None, name=None, bundle=None, full_path=None, custom_fields=None, mtime=None, parent=None, path=None, present=None, size=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """MediaFileMini - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._bundle = None
        self._full_path = None
        self._custom_fields = None
        self._mtime = None
        self._parent = None
        self._path = None
        self._present = None
        self._size = None
        self._volume = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if bundle is not None:
            self.bundle = bundle
        if full_path is not None:
            self.full_path = full_path
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if mtime is not None:
            self.mtime = mtime
        if parent is not None:
            self.parent = parent
        if path is not None:
            self.path = path
        if present is not None:
            self.present = present
        if size is not None:
            self.size = size
        if volume is not None:
            self.volume = volume

    @property
    def id(self):
        """Gets the id of this MediaFileMini.  # noqa: E501


        :return: The id of this MediaFileMini.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaFileMini.


        :param id: The id of this MediaFileMini.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MediaFileMini.  # noqa: E501


        :return: The name of this MediaFileMini.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaFileMini.


        :param name: The name of this MediaFileMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def bundle(self):
        """Gets the bundle of this MediaFileMini.  # noqa: E501


        :return: The bundle of this MediaFileMini.  # noqa: E501
        :rtype: int
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """Sets the bundle of this MediaFileMini.


        :param bundle: The bundle of this MediaFileMini.  # noqa: E501
        :type: int
        """

        self._bundle = bundle

    @property
    def full_path(self):
        """Gets the full_path of this MediaFileMini.  # noqa: E501


        :return: The full_path of this MediaFileMini.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this MediaFileMini.


        :param full_path: The full_path of this MediaFileMini.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def custom_fields(self):
        """Gets the custom_fields of this MediaFileMini.  # noqa: E501


        :return: The custom_fields of this MediaFileMini.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this MediaFileMini.


        :param custom_fields: The custom_fields of this MediaFileMini.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def mtime(self):
        """Gets the mtime of this MediaFileMini.  # noqa: E501


        :return: The mtime of this MediaFileMini.  # noqa: E501
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this MediaFileMini.


        :param mtime: The mtime of this MediaFileMini.  # noqa: E501
        :type: int
        """

        self._mtime = mtime

    @property
    def parent(self):
        """Gets the parent of this MediaFileMini.  # noqa: E501


        :return: The parent of this MediaFileMini.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this MediaFileMini.


        :param parent: The parent of this MediaFileMini.  # noqa: E501
        :type: dict(str, str)
        """

        self._parent = parent

    @property
    def path(self):
        """Gets the path of this MediaFileMini.  # noqa: E501


        :return: The path of this MediaFileMini.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MediaFileMini.


        :param path: The path of this MediaFileMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def present(self):
        """Gets the present of this MediaFileMini.  # noqa: E501


        :return: The present of this MediaFileMini.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this MediaFileMini.


        :param present: The present of this MediaFileMini.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def size(self):
        """Gets the size of this MediaFileMini.  # noqa: E501


        :return: The size of this MediaFileMini.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MediaFileMini.


        :param size: The size of this MediaFileMini.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def volume(self):
        """Gets the volume of this MediaFileMini.  # noqa: E501


        :return: The volume of this MediaFileMini.  # noqa: E501
        :rtype: VolumeMini
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MediaFileMini.


        :param volume: The volume of this MediaFileMini.  # noqa: E501
        :type: VolumeMini
        """

        self._volume = volume

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
        if not isinstance(other, MediaFileMini):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaFileMini):
            return True

        return self.to_dict() != other.to_dict()
