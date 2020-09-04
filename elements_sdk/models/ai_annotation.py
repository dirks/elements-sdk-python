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


class AIAnnotation(object):
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
        'id': 'str',
        'relative_left': 'float',
        'relative_top': 'float',
        'relative_width': 'float',
        'relative_height': 'float',
        'track': 'str',
        'image': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'relative_left': 'relative_left',
        'relative_top': 'relative_top',
        'relative_width': 'relative_width',
        'relative_height': 'relative_height',
        'track': 'track',
        'image': 'image',
        'category': 'category'
    }

    def __init__(self, id=None, relative_left=None, relative_top=None, relative_width=None, relative_height=None, track=None, image=None, category=None, local_vars_configuration=None):  # noqa: E501
        """AIAnnotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._relative_left = None
        self._relative_top = None
        self._relative_width = None
        self._relative_height = None
        self._track = None
        self._image = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.relative_left = relative_left
        self.relative_top = relative_top
        self.relative_width = relative_width
        self.relative_height = relative_height
        if track is not None:
            self.track = track
        self.image = image
        self.category = category

    @property
    def id(self):
        """Gets the id of this AIAnnotation.  # noqa: E501


        :return: The id of this AIAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AIAnnotation.


        :param id: The id of this AIAnnotation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def relative_left(self):
        """Gets the relative_left of this AIAnnotation.  # noqa: E501


        :return: The relative_left of this AIAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._relative_left

    @relative_left.setter
    def relative_left(self, relative_left):
        """Sets the relative_left of this AIAnnotation.


        :param relative_left: The relative_left of this AIAnnotation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and relative_left is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_left`, must not be `None`")  # noqa: E501

        self._relative_left = relative_left

    @property
    def relative_top(self):
        """Gets the relative_top of this AIAnnotation.  # noqa: E501


        :return: The relative_top of this AIAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._relative_top

    @relative_top.setter
    def relative_top(self, relative_top):
        """Sets the relative_top of this AIAnnotation.


        :param relative_top: The relative_top of this AIAnnotation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and relative_top is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_top`, must not be `None`")  # noqa: E501

        self._relative_top = relative_top

    @property
    def relative_width(self):
        """Gets the relative_width of this AIAnnotation.  # noqa: E501


        :return: The relative_width of this AIAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._relative_width

    @relative_width.setter
    def relative_width(self, relative_width):
        """Sets the relative_width of this AIAnnotation.


        :param relative_width: The relative_width of this AIAnnotation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and relative_width is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_width`, must not be `None`")  # noqa: E501

        self._relative_width = relative_width

    @property
    def relative_height(self):
        """Gets the relative_height of this AIAnnotation.  # noqa: E501


        :return: The relative_height of this AIAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._relative_height

    @relative_height.setter
    def relative_height(self, relative_height):
        """Sets the relative_height of this AIAnnotation.


        :param relative_height: The relative_height of this AIAnnotation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and relative_height is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_height`, must not be `None`")  # noqa: E501

        self._relative_height = relative_height

    @property
    def track(self):
        """Gets the track of this AIAnnotation.  # noqa: E501


        :return: The track of this AIAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._track

    @track.setter
    def track(self, track):
        """Sets the track of this AIAnnotation.


        :param track: The track of this AIAnnotation.  # noqa: E501
        :type: str
        """

        self._track = track

    @property
    def image(self):
        """Gets the image of this AIAnnotation.  # noqa: E501


        :return: The image of this AIAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AIAnnotation.


        :param image: The image of this AIAnnotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def category(self):
        """Gets the category of this AIAnnotation.  # noqa: E501


        :return: The category of this AIAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AIAnnotation.


        :param category: The category of this AIAnnotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

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
        if not isinstance(other, AIAnnotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AIAnnotation):
            return True

        return self.to_dict() != other.to_dict()
