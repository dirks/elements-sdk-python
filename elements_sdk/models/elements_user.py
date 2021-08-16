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


class ElementsUser(object):
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
        'allow_changing_password': 'bool',
        'allow_wan_login': 'bool',
        'allowed_fs_paths': 'list[str]',
        'allowed_fs_write_paths': 'list[str]',
        'avatar': 'str',
        'client_sessions': 'list[ClientSession]',
        'default_page': 'str',
        'display_name': 'str',
        'effective_permissions': 'list[str]',
        'email': 'str',
        'expiry': 'datetime',
        'ancillary_path_read_only': 'bool',
        'ancillary_path': 'str',
        'fm_bookmarks': 'list[str]',
        'full_name': 'str',
        'gid': 'int',
        'group_permissions': 'list[str]',
        'has_password': 'bool',
        'home': 'int',
        'is_external': 'bool',
        'is_cloud': 'bool',
        'is_cloud_default': 'bool',
        'is_enabled': 'bool',
        'language': 'str',
        'last_seen': 'datetime',
        'ldap': 'int',
        'ldap_dn': 'str',
        'password_change_required': 'bool',
        'permissions': 'list[str]',
        'shaper_ceiling': 'int',
        'shaper_rate': 'int',
        'sync_id': 'str',
        'totp_enabled': 'bool',
        'uid': 'int',
        'unix_username': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'allow_changing_password': 'allow_changing_password',
        'allow_wan_login': 'allow_wan_login',
        'allowed_fs_paths': 'allowed_fs_paths',
        'allowed_fs_write_paths': 'allowed_fs_write_paths',
        'avatar': 'avatar',
        'client_sessions': 'client_sessions',
        'default_page': 'default_page',
        'display_name': 'display_name',
        'effective_permissions': 'effective_permissions',
        'email': 'email',
        'expiry': 'expiry',
        'ancillary_path_read_only': 'ancillary_path_read_only',
        'ancillary_path': 'ancillary_path',
        'fm_bookmarks': 'fm_bookmarks',
        'full_name': 'full_name',
        'gid': 'gid',
        'group_permissions': 'group_permissions',
        'has_password': 'has_password',
        'home': 'home',
        'is_external': 'is_external',
        'is_cloud': 'is_cloud',
        'is_cloud_default': 'is_cloud_default',
        'is_enabled': 'is_enabled',
        'language': 'language',
        'last_seen': 'last_seen',
        'ldap': 'ldap',
        'ldap_dn': 'ldap_dn',
        'password_change_required': 'password_change_required',
        'permissions': 'permissions',
        'shaper_ceiling': 'shaper_ceiling',
        'shaper_rate': 'shaper_rate',
        'sync_id': 'sync_id',
        'totp_enabled': 'totp_enabled',
        'uid': 'uid',
        'unix_username': 'unix_username',
        'username': 'username'
    }

    def __init__(self, id=None, allow_changing_password=None, allow_wan_login=None, allowed_fs_paths=None, allowed_fs_write_paths=None, avatar=None, client_sessions=None, default_page=None, display_name=None, effective_permissions=None, email=None, expiry=None, ancillary_path_read_only=None, ancillary_path=None, fm_bookmarks=None, full_name=None, gid=None, group_permissions=None, has_password=None, home=None, is_external=None, is_cloud=None, is_cloud_default=None, is_enabled=None, language=None, last_seen=None, ldap=None, ldap_dn=None, password_change_required=None, permissions=None, shaper_ceiling=None, shaper_rate=None, sync_id=None, totp_enabled=None, uid=None, unix_username=None, username=None, local_vars_configuration=None):  # noqa: E501
        """ElementsUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._allow_changing_password = None
        self._allow_wan_login = None
        self._allowed_fs_paths = None
        self._allowed_fs_write_paths = None
        self._avatar = None
        self._client_sessions = None
        self._default_page = None
        self._display_name = None
        self._effective_permissions = None
        self._email = None
        self._expiry = None
        self._ancillary_path_read_only = None
        self._ancillary_path = None
        self._fm_bookmarks = None
        self._full_name = None
        self._gid = None
        self._group_permissions = None
        self._has_password = None
        self._home = None
        self._is_external = None
        self._is_cloud = None
        self._is_cloud_default = None
        self._is_enabled = None
        self._language = None
        self._last_seen = None
        self._ldap = None
        self._ldap_dn = None
        self._password_change_required = None
        self._permissions = None
        self._shaper_ceiling = None
        self._shaper_rate = None
        self._sync_id = None
        self._totp_enabled = None
        self._uid = None
        self._unix_username = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if allow_changing_password is not None:
            self.allow_changing_password = allow_changing_password
        if allow_wan_login is not None:
            self.allow_wan_login = allow_wan_login
        if allowed_fs_paths is not None:
            self.allowed_fs_paths = allowed_fs_paths
        if allowed_fs_write_paths is not None:
            self.allowed_fs_write_paths = allowed_fs_write_paths
        self.avatar = avatar
        if client_sessions is not None:
            self.client_sessions = client_sessions
        if default_page is not None:
            self.default_page = default_page
        if display_name is not None:
            self.display_name = display_name
        if effective_permissions is not None:
            self.effective_permissions = effective_permissions
        self.email = email
        self.expiry = expiry
        if ancillary_path_read_only is not None:
            self.ancillary_path_read_only = ancillary_path_read_only
        if ancillary_path is not None:
            self.ancillary_path = ancillary_path
        if fm_bookmarks is not None:
            self.fm_bookmarks = fm_bookmarks
        self.full_name = full_name
        self.gid = gid
        if group_permissions is not None:
            self.group_permissions = group_permissions
        if has_password is not None:
            self.has_password = has_password
        self.home = home
        if is_external is not None:
            self.is_external = is_external
        if is_cloud is not None:
            self.is_cloud = is_cloud
        if is_cloud_default is not None:
            self.is_cloud_default = is_cloud_default
        if is_enabled is not None:
            self.is_enabled = is_enabled
        self.language = language
        if last_seen is not None:
            self.last_seen = last_seen
        if ldap is not None:
            self.ldap = ldap
        if ldap_dn is not None:
            self.ldap_dn = ldap_dn
        if password_change_required is not None:
            self.password_change_required = password_change_required
        self.permissions = permissions
        self.shaper_ceiling = shaper_ceiling
        self.shaper_rate = shaper_rate
        if sync_id is not None:
            self.sync_id = sync_id
        if totp_enabled is not None:
            self.totp_enabled = totp_enabled
        self.uid = uid
        self.unix_username = unix_username
        self.username = username

    @property
    def id(self):
        """Gets the id of this ElementsUser.  # noqa: E501


        :return: The id of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElementsUser.


        :param id: The id of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def allow_changing_password(self):
        """Gets the allow_changing_password of this ElementsUser.  # noqa: E501


        :return: The allow_changing_password of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._allow_changing_password

    @allow_changing_password.setter
    def allow_changing_password(self, allow_changing_password):
        """Sets the allow_changing_password of this ElementsUser.


        :param allow_changing_password: The allow_changing_password of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._allow_changing_password = allow_changing_password

    @property
    def allow_wan_login(self):
        """Gets the allow_wan_login of this ElementsUser.  # noqa: E501


        :return: The allow_wan_login of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._allow_wan_login

    @allow_wan_login.setter
    def allow_wan_login(self, allow_wan_login):
        """Sets the allow_wan_login of this ElementsUser.


        :param allow_wan_login: The allow_wan_login of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._allow_wan_login = allow_wan_login

    @property
    def allowed_fs_paths(self):
        """Gets the allowed_fs_paths of this ElementsUser.  # noqa: E501


        :return: The allowed_fs_paths of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_fs_paths

    @allowed_fs_paths.setter
    def allowed_fs_paths(self, allowed_fs_paths):
        """Sets the allowed_fs_paths of this ElementsUser.


        :param allowed_fs_paths: The allowed_fs_paths of this ElementsUser.  # noqa: E501
        :type: list[str]
        """

        self._allowed_fs_paths = allowed_fs_paths

    @property
    def allowed_fs_write_paths(self):
        """Gets the allowed_fs_write_paths of this ElementsUser.  # noqa: E501


        :return: The allowed_fs_write_paths of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_fs_write_paths

    @allowed_fs_write_paths.setter
    def allowed_fs_write_paths(self, allowed_fs_write_paths):
        """Sets the allowed_fs_write_paths of this ElementsUser.


        :param allowed_fs_write_paths: The allowed_fs_write_paths of this ElementsUser.  # noqa: E501
        :type: list[str]
        """

        self._allowed_fs_write_paths = allowed_fs_write_paths

    @property
    def avatar(self):
        """Gets the avatar of this ElementsUser.  # noqa: E501


        :return: The avatar of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this ElementsUser.


        :param avatar: The avatar of this ElementsUser.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def client_sessions(self):
        """Gets the client_sessions of this ElementsUser.  # noqa: E501


        :return: The client_sessions of this ElementsUser.  # noqa: E501
        :rtype: list[ClientSession]
        """
        return self._client_sessions

    @client_sessions.setter
    def client_sessions(self, client_sessions):
        """Sets the client_sessions of this ElementsUser.


        :param client_sessions: The client_sessions of this ElementsUser.  # noqa: E501
        :type: list[ClientSession]
        """

        self._client_sessions = client_sessions

    @property
    def default_page(self):
        """Gets the default_page of this ElementsUser.  # noqa: E501


        :return: The default_page of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._default_page

    @default_page.setter
    def default_page(self, default_page):
        """Sets the default_page of this ElementsUser.


        :param default_page: The default_page of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_page is not None and len(default_page) > 63):
            raise ValueError("Invalid value for `default_page`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                default_page is not None and len(default_page) < 1):
            raise ValueError("Invalid value for `default_page`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_page = default_page

    @property
    def display_name(self):
        """Gets the display_name of this ElementsUser.  # noqa: E501


        :return: The display_name of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ElementsUser.


        :param display_name: The display_name of this ElementsUser.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def effective_permissions(self):
        """Gets the effective_permissions of this ElementsUser.  # noqa: E501


        :return: The effective_permissions of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """Sets the effective_permissions of this ElementsUser.


        :param effective_permissions: The effective_permissions of this ElementsUser.  # noqa: E501
        :type: list[str]
        """

        self._effective_permissions = effective_permissions

    @property
    def email(self):
        """Gets the email of this ElementsUser.  # noqa: E501


        :return: The email of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ElementsUser.


        :param email: The email of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 255):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501

        self._email = email

    @property
    def expiry(self):
        """Gets the expiry of this ElementsUser.  # noqa: E501


        :return: The expiry of this ElementsUser.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this ElementsUser.


        :param expiry: The expiry of this ElementsUser.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def ancillary_path_read_only(self):
        """Gets the ancillary_path_read_only of this ElementsUser.  # noqa: E501


        :return: The ancillary_path_read_only of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._ancillary_path_read_only

    @ancillary_path_read_only.setter
    def ancillary_path_read_only(self, ancillary_path_read_only):
        """Sets the ancillary_path_read_only of this ElementsUser.


        :param ancillary_path_read_only: The ancillary_path_read_only of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._ancillary_path_read_only = ancillary_path_read_only

    @property
    def ancillary_path(self):
        """Gets the ancillary_path of this ElementsUser.  # noqa: E501


        :return: The ancillary_path of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._ancillary_path

    @ancillary_path.setter
    def ancillary_path(self, ancillary_path):
        """Sets the ancillary_path of this ElementsUser.


        :param ancillary_path: The ancillary_path of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ancillary_path is not None and len(ancillary_path) > 255):
            raise ValueError("Invalid value for `ancillary_path`, length must be less than or equal to `255`")  # noqa: E501

        self._ancillary_path = ancillary_path

    @property
    def fm_bookmarks(self):
        """Gets the fm_bookmarks of this ElementsUser.  # noqa: E501


        :return: The fm_bookmarks of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._fm_bookmarks

    @fm_bookmarks.setter
    def fm_bookmarks(self, fm_bookmarks):
        """Sets the fm_bookmarks of this ElementsUser.


        :param fm_bookmarks: The fm_bookmarks of this ElementsUser.  # noqa: E501
        :type: list[str]
        """

        self._fm_bookmarks = fm_bookmarks

    @property
    def full_name(self):
        """Gets the full_name of this ElementsUser.  # noqa: E501


        :return: The full_name of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ElementsUser.


        :param full_name: The full_name of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                full_name is not None and len(full_name) > 255):
            raise ValueError("Invalid value for `full_name`, length must be less than or equal to `255`")  # noqa: E501

        self._full_name = full_name

    @property
    def gid(self):
        """Gets the gid of this ElementsUser.  # noqa: E501


        :return: The gid of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ElementsUser.


        :param gid: The gid of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._gid = gid

    @property
    def group_permissions(self):
        """Gets the group_permissions of this ElementsUser.  # noqa: E501


        :return: The group_permissions of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_permissions

    @group_permissions.setter
    def group_permissions(self, group_permissions):
        """Sets the group_permissions of this ElementsUser.


        :param group_permissions: The group_permissions of this ElementsUser.  # noqa: E501
        :type: list[str]
        """

        self._group_permissions = group_permissions

    @property
    def has_password(self):
        """Gets the has_password of this ElementsUser.  # noqa: E501


        :return: The has_password of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this ElementsUser.


        :param has_password: The has_password of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._has_password = has_password

    @property
    def home(self):
        """Gets the home of this ElementsUser.  # noqa: E501


        :return: The home of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this ElementsUser.


        :param home: The home of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._home = home

    @property
    def is_external(self):
        """Gets the is_external of this ElementsUser.  # noqa: E501


        :return: The is_external of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this ElementsUser.


        :param is_external: The is_external of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._is_external = is_external

    @property
    def is_cloud(self):
        """Gets the is_cloud of this ElementsUser.  # noqa: E501


        :return: The is_cloud of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloud

    @is_cloud.setter
    def is_cloud(self, is_cloud):
        """Sets the is_cloud of this ElementsUser.


        :param is_cloud: The is_cloud of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._is_cloud = is_cloud

    @property
    def is_cloud_default(self):
        """Gets the is_cloud_default of this ElementsUser.  # noqa: E501


        :return: The is_cloud_default of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloud_default

    @is_cloud_default.setter
    def is_cloud_default(self, is_cloud_default):
        """Sets the is_cloud_default of this ElementsUser.


        :param is_cloud_default: The is_cloud_default of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._is_cloud_default = is_cloud_default

    @property
    def is_enabled(self):
        """Gets the is_enabled of this ElementsUser.  # noqa: E501


        :return: The is_enabled of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this ElementsUser.


        :param is_enabled: The is_enabled of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def language(self):
        """Gets the language of this ElementsUser.  # noqa: E501


        :return: The language of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ElementsUser.


        :param language: The language of this ElementsUser.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"en", "fr", "de", "ru"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def last_seen(self):
        """Gets the last_seen of this ElementsUser.  # noqa: E501


        :return: The last_seen of this ElementsUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this ElementsUser.


        :param last_seen: The last_seen of this ElementsUser.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def ldap(self):
        """Gets the ldap of this ElementsUser.  # noqa: E501


        :return: The ldap of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._ldap

    @ldap.setter
    def ldap(self, ldap):
        """Sets the ldap of this ElementsUser.


        :param ldap: The ldap of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._ldap = ldap

    @property
    def ldap_dn(self):
        """Gets the ldap_dn of this ElementsUser.  # noqa: E501


        :return: The ldap_dn of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._ldap_dn

    @ldap_dn.setter
    def ldap_dn(self, ldap_dn):
        """Sets the ldap_dn of this ElementsUser.


        :param ldap_dn: The ldap_dn of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ldap_dn is not None and len(ldap_dn) < 1):
            raise ValueError("Invalid value for `ldap_dn`, length must be greater than or equal to `1`")  # noqa: E501

        self._ldap_dn = ldap_dn

    @property
    def password_change_required(self):
        """Gets the password_change_required of this ElementsUser.  # noqa: E501


        :return: The password_change_required of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._password_change_required

    @password_change_required.setter
    def password_change_required(self, password_change_required):
        """Sets the password_change_required of this ElementsUser.


        :param password_change_required: The password_change_required of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._password_change_required = password_change_required

    @property
    def permissions(self):
        """Gets the permissions of this ElementsUser.  # noqa: E501


        :return: The permissions of this ElementsUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ElementsUser.


        :param permissions: The permissions of this ElementsUser.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def shaper_ceiling(self):
        """Gets the shaper_ceiling of this ElementsUser.  # noqa: E501


        :return: The shaper_ceiling of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._shaper_ceiling

    @shaper_ceiling.setter
    def shaper_ceiling(self, shaper_ceiling):
        """Sets the shaper_ceiling of this ElementsUser.


        :param shaper_ceiling: The shaper_ceiling of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._shaper_ceiling = shaper_ceiling

    @property
    def shaper_rate(self):
        """Gets the shaper_rate of this ElementsUser.  # noqa: E501


        :return: The shaper_rate of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._shaper_rate

    @shaper_rate.setter
    def shaper_rate(self, shaper_rate):
        """Sets the shaper_rate of this ElementsUser.


        :param shaper_rate: The shaper_rate of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._shaper_rate = shaper_rate

    @property
    def sync_id(self):
        """Gets the sync_id of this ElementsUser.  # noqa: E501


        :return: The sync_id of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this ElementsUser.


        :param sync_id: The sync_id of this ElementsUser.  # noqa: E501
        :type: str
        """

        self._sync_id = sync_id

    @property
    def totp_enabled(self):
        """Gets the totp_enabled of this ElementsUser.  # noqa: E501


        :return: The totp_enabled of this ElementsUser.  # noqa: E501
        :rtype: bool
        """
        return self._totp_enabled

    @totp_enabled.setter
    def totp_enabled(self, totp_enabled):
        """Sets the totp_enabled of this ElementsUser.


        :param totp_enabled: The totp_enabled of this ElementsUser.  # noqa: E501
        :type: bool
        """

        self._totp_enabled = totp_enabled

    @property
    def uid(self):
        """Gets the uid of this ElementsUser.  # noqa: E501


        :return: The uid of this ElementsUser.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ElementsUser.


        :param uid: The uid of this ElementsUser.  # noqa: E501
        :type: int
        """

        self._uid = uid

    @property
    def unix_username(self):
        """Gets the unix_username of this ElementsUser.  # noqa: E501


        :return: The unix_username of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._unix_username

    @unix_username.setter
    def unix_username(self, unix_username):
        """Sets the unix_username of this ElementsUser.


        :param unix_username: The unix_username of this ElementsUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unix_username is not None and len(unix_username) > 255):
            raise ValueError("Invalid value for `unix_username`, length must be less than or equal to `255`")  # noqa: E501

        self._unix_username = unix_username

    @property
    def username(self):
        """Gets the username of this ElementsUser.  # noqa: E501


        :return: The username of this ElementsUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ElementsUser.


        :param username: The username of this ElementsUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 255):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, ElementsUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementsUser):
            return True

        return self.to_dict() != other.to_dict()
