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


class StartTaskRequest(object):
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
        'task_type': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'task_type': 'task_type',
        'parameters': 'parameters'
    }

    def __init__(self, task_type=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """StartTaskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._task_type = None
        self._parameters = None
        self.discriminator = None

        self.task_type = task_type
        self.parameters = parameters

    @property
    def task_type(self):
        """Gets the task_type of this StartTaskRequest.  # noqa: E501


        :return: The task_type of this StartTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this StartTaskRequest.


        :param task_type: The task_type of this StartTaskRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and task_type is None:  # noqa: E501
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                task_type is not None and len(task_type) < 1):
            raise ValueError("Invalid value for `task_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._task_type = task_type

    @property
    def parameters(self):
        """Gets the parameters of this StartTaskRequest.  # noqa: E501


        :return: The parameters of this StartTaskRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this StartTaskRequest.


        :param parameters: The parameters of this StartTaskRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, StartTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
