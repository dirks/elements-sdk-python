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


class Job(object):
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
        'subtasks': 'list[Subtask]',
        'schedules': 'list[Schedule]',
        'allow_users': 'list[ElementsUser]',
        'allow_groups': 'list[ElementsGroup]',
        'startable': 'bool',
        'variable_definitions': 'list[str]',
        'media_roots': 'list[int]',
        'webhook_url': 'str',
        'special_type': 'int',
        'name': 'str',
        'enabled': 'bool',
        'allow_others_to_start': 'bool',
        'allow_client_to_start': 'bool',
        'show_as_button': 'bool',
        'input_type': 'str',
        'hook': 'str',
        'webhook_secret': 'str',
        'security_context': 'int',
        'part_of_workflow_for': 'int'
    }

    attribute_map = {
        'id': 'id',
        'subtasks': 'subtasks',
        'schedules': 'schedules',
        'allow_users': 'allow_users',
        'allow_groups': 'allow_groups',
        'startable': 'startable',
        'variable_definitions': 'variable_definitions',
        'media_roots': 'media_roots',
        'webhook_url': 'webhook_url',
        'special_type': 'special_type',
        'name': 'name',
        'enabled': 'enabled',
        'allow_others_to_start': 'allow_others_to_start',
        'allow_client_to_start': 'allow_client_to_start',
        'show_as_button': 'show_as_button',
        'input_type': 'input_type',
        'hook': 'hook',
        'webhook_secret': 'webhook_secret',
        'security_context': 'security_context',
        'part_of_workflow_for': 'part_of_workflow_for'
    }

    def __init__(self, id=None, subtasks=None, schedules=None, allow_users=None, allow_groups=None, startable=None, variable_definitions=None, media_roots=None, webhook_url=None, special_type=None, name=None, enabled=None, allow_others_to_start=None, allow_client_to_start=None, show_as_button=None, input_type=None, hook=None, webhook_secret=None, security_context=None, part_of_workflow_for=None, local_vars_configuration=None):  # noqa: E501
        """Job - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._subtasks = None
        self._schedules = None
        self._allow_users = None
        self._allow_groups = None
        self._startable = None
        self._variable_definitions = None
        self._media_roots = None
        self._webhook_url = None
        self._special_type = None
        self._name = None
        self._enabled = None
        self._allow_others_to_start = None
        self._allow_client_to_start = None
        self._show_as_button = None
        self._input_type = None
        self._hook = None
        self._webhook_secret = None
        self._security_context = None
        self._part_of_workflow_for = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subtasks is not None:
            self.subtasks = subtasks
        if schedules is not None:
            self.schedules = schedules
        if allow_users is not None:
            self.allow_users = allow_users
        if allow_groups is not None:
            self.allow_groups = allow_groups
        if startable is not None:
            self.startable = startable
        if variable_definitions is not None:
            self.variable_definitions = variable_definitions
        if media_roots is not None:
            self.media_roots = media_roots
        if webhook_url is not None:
            self.webhook_url = webhook_url
        self.special_type = special_type
        self.name = name
        if enabled is not None:
            self.enabled = enabled
        if allow_others_to_start is not None:
            self.allow_others_to_start = allow_others_to_start
        if allow_client_to_start is not None:
            self.allow_client_to_start = allow_client_to_start
        if show_as_button is not None:
            self.show_as_button = show_as_button
        self.input_type = input_type
        self.hook = hook
        self.webhook_secret = webhook_secret
        self.security_context = security_context
        self.part_of_workflow_for = part_of_workflow_for

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def subtasks(self):
        """Gets the subtasks of this Job.  # noqa: E501


        :return: The subtasks of this Job.  # noqa: E501
        :rtype: list[Subtask]
        """
        return self._subtasks

    @subtasks.setter
    def subtasks(self, subtasks):
        """Sets the subtasks of this Job.


        :param subtasks: The subtasks of this Job.  # noqa: E501
        :type: list[Subtask]
        """

        self._subtasks = subtasks

    @property
    def schedules(self):
        """Gets the schedules of this Job.  # noqa: E501


        :return: The schedules of this Job.  # noqa: E501
        :rtype: list[Schedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this Job.


        :param schedules: The schedules of this Job.  # noqa: E501
        :type: list[Schedule]
        """

        self._schedules = schedules

    @property
    def allow_users(self):
        """Gets the allow_users of this Job.  # noqa: E501


        :return: The allow_users of this Job.  # noqa: E501
        :rtype: list[ElementsUser]
        """
        return self._allow_users

    @allow_users.setter
    def allow_users(self, allow_users):
        """Sets the allow_users of this Job.


        :param allow_users: The allow_users of this Job.  # noqa: E501
        :type: list[ElementsUser]
        """

        self._allow_users = allow_users

    @property
    def allow_groups(self):
        """Gets the allow_groups of this Job.  # noqa: E501


        :return: The allow_groups of this Job.  # noqa: E501
        :rtype: list[ElementsGroup]
        """
        return self._allow_groups

    @allow_groups.setter
    def allow_groups(self, allow_groups):
        """Sets the allow_groups of this Job.


        :param allow_groups: The allow_groups of this Job.  # noqa: E501
        :type: list[ElementsGroup]
        """

        self._allow_groups = allow_groups

    @property
    def startable(self):
        """Gets the startable of this Job.  # noqa: E501


        :return: The startable of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._startable

    @startable.setter
    def startable(self, startable):
        """Sets the startable of this Job.


        :param startable: The startable of this Job.  # noqa: E501
        :type: bool
        """

        self._startable = startable

    @property
    def variable_definitions(self):
        """Gets the variable_definitions of this Job.  # noqa: E501


        :return: The variable_definitions of this Job.  # noqa: E501
        :rtype: list[str]
        """
        return self._variable_definitions

    @variable_definitions.setter
    def variable_definitions(self, variable_definitions):
        """Sets the variable_definitions of this Job.


        :param variable_definitions: The variable_definitions of this Job.  # noqa: E501
        :type: list[str]
        """

        self._variable_definitions = variable_definitions

    @property
    def media_roots(self):
        """Gets the media_roots of this Job.  # noqa: E501


        :return: The media_roots of this Job.  # noqa: E501
        :rtype: list[int]
        """
        return self._media_roots

    @media_roots.setter
    def media_roots(self, media_roots):
        """Sets the media_roots of this Job.


        :param media_roots: The media_roots of this Job.  # noqa: E501
        :type: list[int]
        """

        self._media_roots = media_roots

    @property
    def webhook_url(self):
        """Gets the webhook_url of this Job.  # noqa: E501


        :return: The webhook_url of this Job.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this Job.


        :param webhook_url: The webhook_url of this Job.  # noqa: E501
        :type: str
        """

        self._webhook_url = webhook_url

    @property
    def special_type(self):
        """Gets the special_type of this Job.  # noqa: E501


        :return: The special_type of this Job.  # noqa: E501
        :rtype: int
        """
        return self._special_type

    @special_type.setter
    def special_type(self, special_type):
        """Sets the special_type of this Job.


        :param special_type: The special_type of this Job.  # noqa: E501
        :type: int
        """

        self._special_type = special_type

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501


        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.


        :param name: The name of this Job.  # noqa: E501
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
    def enabled(self):
        """Gets the enabled of this Job.  # noqa: E501


        :return: The enabled of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Job.


        :param enabled: The enabled of this Job.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def allow_others_to_start(self):
        """Gets the allow_others_to_start of this Job.  # noqa: E501


        :return: The allow_others_to_start of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._allow_others_to_start

    @allow_others_to_start.setter
    def allow_others_to_start(self, allow_others_to_start):
        """Sets the allow_others_to_start of this Job.


        :param allow_others_to_start: The allow_others_to_start of this Job.  # noqa: E501
        :type: bool
        """

        self._allow_others_to_start = allow_others_to_start

    @property
    def allow_client_to_start(self):
        """Gets the allow_client_to_start of this Job.  # noqa: E501


        :return: The allow_client_to_start of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._allow_client_to_start

    @allow_client_to_start.setter
    def allow_client_to_start(self, allow_client_to_start):
        """Sets the allow_client_to_start of this Job.


        :param allow_client_to_start: The allow_client_to_start of this Job.  # noqa: E501
        :type: bool
        """

        self._allow_client_to_start = allow_client_to_start

    @property
    def show_as_button(self):
        """Gets the show_as_button of this Job.  # noqa: E501


        :return: The show_as_button of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._show_as_button

    @show_as_button.setter
    def show_as_button(self, show_as_button):
        """Sets the show_as_button of this Job.


        :param show_as_button: The show_as_button of this Job.  # noqa: E501
        :type: bool
        """

        self._show_as_button = show_as_button

    @property
    def input_type(self):
        """Gets the input_type of this Job.  # noqa: E501


        :return: The input_type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this Job.


        :param input_type: The input_type of this Job.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"path", "dir", "paths", "dirs"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and input_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `input_type` ({0}), must be one of {1}"  # noqa: E501
                .format(input_type, allowed_values)
            )

        self._input_type = input_type

    @property
    def hook(self):
        """Gets the hook of this Job.  # noqa: E501


        :return: The hook of this Job.  # noqa: E501
        :rtype: str
        """
        return self._hook

    @hook.setter
    def hook(self, hook):
        """Sets the hook of this Job.


        :param hook: The hook of this Job.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hook is not None and len(hook) > 255):
            raise ValueError("Invalid value for `hook`, length must be less than or equal to `255`")  # noqa: E501

        self._hook = hook

    @property
    def webhook_secret(self):
        """Gets the webhook_secret of this Job.  # noqa: E501


        :return: The webhook_secret of this Job.  # noqa: E501
        :rtype: str
        """
        return self._webhook_secret

    @webhook_secret.setter
    def webhook_secret(self, webhook_secret):
        """Sets the webhook_secret of this Job.


        :param webhook_secret: The webhook_secret of this Job.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                webhook_secret is not None and len(webhook_secret) > 128):
            raise ValueError("Invalid value for `webhook_secret`, length must be less than or equal to `128`")  # noqa: E501

        self._webhook_secret = webhook_secret

    @property
    def security_context(self):
        """Gets the security_context of this Job.  # noqa: E501


        :return: The security_context of this Job.  # noqa: E501
        :rtype: int
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this Job.


        :param security_context: The security_context of this Job.  # noqa: E501
        :type: int
        """

        self._security_context = security_context

    @property
    def part_of_workflow_for(self):
        """Gets the part_of_workflow_for of this Job.  # noqa: E501


        :return: The part_of_workflow_for of this Job.  # noqa: E501
        :rtype: int
        """
        return self._part_of_workflow_for

    @part_of_workflow_for.setter
    def part_of_workflow_for(self, part_of_workflow_for):
        """Sets the part_of_workflow_for of this Job.


        :param part_of_workflow_for: The part_of_workflow_for of this Job.  # noqa: E501
        :type: int
        """

        self._part_of_workflow_for = part_of_workflow_for

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
        if not isinstance(other, Job):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Job):
            return True

        return self.to_dict() != other.to_dict()
