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


class WorkspacePermission(object):
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
        'user': 'ElementsUser',
        'group': 'ElementsGroup',
        'read_only': 'bool',
        'workspace': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'group': 'group',
        'read_only': 'read_only',
        'workspace': 'workspace'
    }

    def __init__(self, id=None, user=None, group=None, read_only=None, workspace=None, local_vars_configuration=None):  # noqa: E501
        """WorkspacePermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user = None
        self._group = None
        self._read_only = None
        self._workspace = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if group is not None:
            self.group = group
        if read_only is not None:
            self.read_only = read_only
        self.workspace = workspace

    @property
    def id(self):
        """Gets the id of this WorkspacePermission.  # noqa: E501


        :return: The id of this WorkspacePermission.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspacePermission.


        :param id: The id of this WorkspacePermission.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this WorkspacePermission.  # noqa: E501


        :return: The user of this WorkspacePermission.  # noqa: E501
        :rtype: ElementsUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkspacePermission.


        :param user: The user of this WorkspacePermission.  # noqa: E501
        :type: ElementsUser
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this WorkspacePermission.  # noqa: E501


        :return: The group of this WorkspacePermission.  # noqa: E501
        :rtype: ElementsGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this WorkspacePermission.


        :param group: The group of this WorkspacePermission.  # noqa: E501
        :type: ElementsGroup
        """

        self._group = group

    @property
    def read_only(self):
        """Gets the read_only of this WorkspacePermission.  # noqa: E501


        :return: The read_only of this WorkspacePermission.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this WorkspacePermission.


        :param read_only: The read_only of this WorkspacePermission.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def workspace(self):
        """Gets the workspace of this WorkspacePermission.  # noqa: E501


        :return: The workspace of this WorkspacePermission.  # noqa: E501
        :rtype: int
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this WorkspacePermission.


        :param workspace: The workspace of this WorkspacePermission.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and workspace is None:  # noqa: E501
            raise ValueError("Invalid value for `workspace`, must not be `None`")  # noqa: E501

        self._workspace = workspace

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
        if not isinstance(other, WorkspacePermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspacePermission):
            return True

        return self.to_dict() != other.to_dict()
