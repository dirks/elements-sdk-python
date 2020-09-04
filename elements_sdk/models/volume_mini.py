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


class VolumeMini(object):
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
        'path': 'str',
        'display_name': 'str',
        'visual_tag': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'display_name': 'display_name',
        'visual_tag': 'visual_tag',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, path=None, display_name=None, visual_tag=None, type=None, local_vars_configuration=None):  # noqa: E501
        """VolumeMini - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._path = None
        self._display_name = None
        self._visual_tag = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if display_name is not None:
            self.display_name = display_name
        self.visual_tag = visual_tag
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this VolumeMini.  # noqa: E501


        :return: The id of this VolumeMini.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeMini.


        :param id: The id of this VolumeMini.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeMini.  # noqa: E501


        :return: The name of this VolumeMini.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeMini.


        :param name: The name of this VolumeMini.  # noqa: E501
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
    def path(self):
        """Gets the path of this VolumeMini.  # noqa: E501


        :return: The path of this VolumeMini.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this VolumeMini.


        :param path: The path of this VolumeMini.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def display_name(self):
        """Gets the display_name of this VolumeMini.  # noqa: E501


        :return: The display_name of this VolumeMini.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VolumeMini.


        :param display_name: The display_name of this VolumeMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 255):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def visual_tag(self):
        """Gets the visual_tag of this VolumeMini.  # noqa: E501


        :return: The visual_tag of this VolumeMini.  # noqa: E501
        :rtype: str
        """
        return self._visual_tag

    @visual_tag.setter
    def visual_tag(self, visual_tag):
        """Sets the visual_tag of this VolumeMini.


        :param visual_tag: The visual_tag of this VolumeMini.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                visual_tag is not None and len(visual_tag) > 255):
            raise ValueError("Invalid value for `visual_tag`, length must be less than or equal to `255`")  # noqa: E501

        self._visual_tag = visual_tag

    @property
    def type(self):
        """Gets the type of this VolumeMini.  # noqa: E501


        :return: The type of this VolumeMini.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeMini.


        :param type: The type of this VolumeMini.  # noqa: E501
        :type: str
        """
        allowed_values = ["generic", "generic-mount", "snfs", "btrfs", "s3fs", "lizardfs", "bcachefs", "isilon"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, VolumeMini):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeMini):
            return True

        return self.to_dict() != other.to_dict()
