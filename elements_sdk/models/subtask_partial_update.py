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


class SubtaskPartialUpdate(object):
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
        'kwargs': 'dict(str, str)',
        'graph_layout': 'dict(str, str)',
        'trigger': 'str',
        'name': 'str',
        'noop_dont_save': 'bool',
        'no_concurrency': 'bool',
        'timeout': 'int',
        'log_variable': 'bool',
        'task': 'str',
        'condition_variable': 'str',
        'condition_value': 'str',
        'sync': 'bool',
        'queue': 'str',
        'enqueue_at_front': 'bool',
        'parent': 'int',
        'relative_to': 'int'
    }

    attribute_map = {
        'kwargs': 'kwargs',
        'graph_layout': 'graph_layout',
        'trigger': 'trigger',
        'name': 'name',
        'noop_dont_save': 'noop_dont_save',
        'no_concurrency': 'no_concurrency',
        'timeout': 'timeout',
        'log_variable': 'log_variable',
        'task': 'task',
        'condition_variable': 'condition_variable',
        'condition_value': 'condition_value',
        'sync': 'sync',
        'queue': 'queue',
        'enqueue_at_front': 'enqueue_at_front',
        'parent': 'parent',
        'relative_to': 'relative_to'
    }

    def __init__(self, kwargs=None, graph_layout=None, trigger=None, name=None, noop_dont_save=None, no_concurrency=None, timeout=None, log_variable=None, task=None, condition_variable=None, condition_value=None, sync=None, queue=None, enqueue_at_front=None, parent=None, relative_to=None, local_vars_configuration=None):  # noqa: E501
        """SubtaskPartialUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kwargs = None
        self._graph_layout = None
        self._trigger = None
        self._name = None
        self._noop_dont_save = None
        self._no_concurrency = None
        self._timeout = None
        self._log_variable = None
        self._task = None
        self._condition_variable = None
        self._condition_value = None
        self._sync = None
        self._queue = None
        self._enqueue_at_front = None
        self._parent = None
        self._relative_to = None
        self.discriminator = None

        if kwargs is not None:
            self.kwargs = kwargs
        if graph_layout is not None:
            self.graph_layout = graph_layout
        self.trigger = trigger
        self.name = name
        if noop_dont_save is not None:
            self.noop_dont_save = noop_dont_save
        if no_concurrency is not None:
            self.no_concurrency = no_concurrency
        self.timeout = timeout
        if log_variable is not None:
            self.log_variable = log_variable
        self.task = task
        self.condition_variable = condition_variable
        self.condition_value = condition_value
        if sync is not None:
            self.sync = sync
        self.queue = queue
        if enqueue_at_front is not None:
            self.enqueue_at_front = enqueue_at_front
        if parent is not None:
            self.parent = parent
        self.relative_to = relative_to

    @property
    def kwargs(self):
        """Gets the kwargs of this SubtaskPartialUpdate.  # noqa: E501


        :return: The kwargs of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._kwargs

    @kwargs.setter
    def kwargs(self, kwargs):
        """Sets the kwargs of this SubtaskPartialUpdate.


        :param kwargs: The kwargs of this SubtaskPartialUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._kwargs = kwargs

    @property
    def graph_layout(self):
        """Gets the graph_layout of this SubtaskPartialUpdate.  # noqa: E501


        :return: The graph_layout of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._graph_layout

    @graph_layout.setter
    def graph_layout(self, graph_layout):
        """Sets the graph_layout of this SubtaskPartialUpdate.


        :param graph_layout: The graph_layout of this SubtaskPartialUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._graph_layout = graph_layout

    @property
    def trigger(self):
        """Gets the trigger of this SubtaskPartialUpdate.  # noqa: E501


        :return: The trigger of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this SubtaskPartialUpdate.


        :param trigger: The trigger of this SubtaskPartialUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"finish", "success", "warning", "error", "noop"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trigger not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger, allowed_values)
            )

        self._trigger = trigger

    @property
    def name(self):
        """Gets the name of this SubtaskPartialUpdate.  # noqa: E501


        :return: The name of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubtaskPartialUpdate.


        :param name: The name of this SubtaskPartialUpdate.  # noqa: E501
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
    def noop_dont_save(self):
        """Gets the noop_dont_save of this SubtaskPartialUpdate.  # noqa: E501


        :return: The noop_dont_save of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._noop_dont_save

    @noop_dont_save.setter
    def noop_dont_save(self, noop_dont_save):
        """Sets the noop_dont_save of this SubtaskPartialUpdate.


        :param noop_dont_save: The noop_dont_save of this SubtaskPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._noop_dont_save = noop_dont_save

    @property
    def no_concurrency(self):
        """Gets the no_concurrency of this SubtaskPartialUpdate.  # noqa: E501


        :return: The no_concurrency of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._no_concurrency

    @no_concurrency.setter
    def no_concurrency(self, no_concurrency):
        """Sets the no_concurrency of this SubtaskPartialUpdate.


        :param no_concurrency: The no_concurrency of this SubtaskPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._no_concurrency = no_concurrency

    @property
    def timeout(self):
        """Gets the timeout of this SubtaskPartialUpdate.  # noqa: E501


        :return: The timeout of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SubtaskPartialUpdate.


        :param timeout: The timeout of this SubtaskPartialUpdate.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def log_variable(self):
        """Gets the log_variable of this SubtaskPartialUpdate.  # noqa: E501


        :return: The log_variable of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._log_variable

    @log_variable.setter
    def log_variable(self, log_variable):
        """Sets the log_variable of this SubtaskPartialUpdate.


        :param log_variable: The log_variable of this SubtaskPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._log_variable = log_variable

    @property
    def task(self):
        """Gets the task of this SubtaskPartialUpdate.  # noqa: E501


        :return: The task of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this SubtaskPartialUpdate.


        :param task: The task of this SubtaskPartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                task is not None and len(task) > 255):
            raise ValueError("Invalid value for `task`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                task is not None and len(task) < 1):
            raise ValueError("Invalid value for `task`, length must be greater than or equal to `1`")  # noqa: E501

        self._task = task

    @property
    def condition_variable(self):
        """Gets the condition_variable of this SubtaskPartialUpdate.  # noqa: E501


        :return: The condition_variable of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._condition_variable

    @condition_variable.setter
    def condition_variable(self, condition_variable):
        """Sets the condition_variable of this SubtaskPartialUpdate.


        :param condition_variable: The condition_variable of this SubtaskPartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                condition_variable is not None and len(condition_variable) > 255):
            raise ValueError("Invalid value for `condition_variable`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                condition_variable is not None and len(condition_variable) < 1):
            raise ValueError("Invalid value for `condition_variable`, length must be greater than or equal to `1`")  # noqa: E501

        self._condition_variable = condition_variable

    @property
    def condition_value(self):
        """Gets the condition_value of this SubtaskPartialUpdate.  # noqa: E501


        :return: The condition_value of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """Sets the condition_value of this SubtaskPartialUpdate.


        :param condition_value: The condition_value of this SubtaskPartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                condition_value is not None and len(condition_value) > 255):
            raise ValueError("Invalid value for `condition_value`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                condition_value is not None and len(condition_value) < 1):
            raise ValueError("Invalid value for `condition_value`, length must be greater than or equal to `1`")  # noqa: E501

        self._condition_value = condition_value

    @property
    def sync(self):
        """Gets the sync of this SubtaskPartialUpdate.  # noqa: E501


        :return: The sync of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this SubtaskPartialUpdate.


        :param sync: The sync of this SubtaskPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._sync = sync

    @property
    def queue(self):
        """Gets the queue of this SubtaskPartialUpdate.  # noqa: E501


        :return: The queue of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this SubtaskPartialUpdate.


        :param queue: The queue of this SubtaskPartialUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                queue is not None and len(queue) > 255):
            raise ValueError("Invalid value for `queue`, length must be less than or equal to `255`")  # noqa: E501

        self._queue = queue

    @property
    def enqueue_at_front(self):
        """Gets the enqueue_at_front of this SubtaskPartialUpdate.  # noqa: E501


        :return: The enqueue_at_front of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._enqueue_at_front

    @enqueue_at_front.setter
    def enqueue_at_front(self, enqueue_at_front):
        """Sets the enqueue_at_front of this SubtaskPartialUpdate.


        :param enqueue_at_front: The enqueue_at_front of this SubtaskPartialUpdate.  # noqa: E501
        :type: bool
        """

        self._enqueue_at_front = enqueue_at_front

    @property
    def parent(self):
        """Gets the parent of this SubtaskPartialUpdate.  # noqa: E501


        :return: The parent of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this SubtaskPartialUpdate.


        :param parent: The parent of this SubtaskPartialUpdate.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def relative_to(self):
        """Gets the relative_to of this SubtaskPartialUpdate.  # noqa: E501


        :return: The relative_to of this SubtaskPartialUpdate.  # noqa: E501
        :rtype: int
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, relative_to):
        """Sets the relative_to of this SubtaskPartialUpdate.


        :param relative_to: The relative_to of this SubtaskPartialUpdate.  # noqa: E501
        :type: int
        """

        self._relative_to = relative_to

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
        if not isinstance(other, SubtaskPartialUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubtaskPartialUpdate):
            return True

        return self.to_dict() != other.to_dict()
