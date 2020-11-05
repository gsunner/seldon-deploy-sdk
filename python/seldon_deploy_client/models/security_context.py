# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecurityContext(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_privilege_escalation': 'bool',
        'capabilities': 'Capabilities',
        'privileged': 'bool',
        'proc_mount': 'ProcMountType',
        'read_only_root_filesystem': 'bool',
        'run_as_group': 'int',
        'run_as_non_root': 'bool',
        'run_as_user': 'int',
        'se_linux_options': 'SELinuxOptions',
        'windows_options': 'WindowsSecurityContextOptions'
    }

    attribute_map = {
        'allow_privilege_escalation': 'allowPrivilegeEscalation',
        'capabilities': 'capabilities',
        'privileged': 'privileged',
        'proc_mount': 'procMount',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
        'run_as_group': 'runAsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'windows_options': 'windowsOptions'
    }

    def __init__(self, allow_privilege_escalation=None, capabilities=None, privileged=None, proc_mount=None, read_only_root_filesystem=None, run_as_group=None, run_as_non_root=None, run_as_user=None, se_linux_options=None, windows_options=None):  # noqa: E501
        """SecurityContext - a model defined in Swagger"""  # noqa: E501

        self._allow_privilege_escalation = None
        self._capabilities = None
        self._privileged = None
        self._proc_mount = None
        self._read_only_root_filesystem = None
        self._run_as_group = None
        self._run_as_non_root = None
        self._run_as_user = None
        self._se_linux_options = None
        self._windows_options = None
        self.discriminator = None

        if allow_privilege_escalation is not None:
            self.allow_privilege_escalation = allow_privilege_escalation
        if capabilities is not None:
            self.capabilities = capabilities
        if privileged is not None:
            self.privileged = privileged
        if proc_mount is not None:
            self.proc_mount = proc_mount
        if read_only_root_filesystem is not None:
            self.read_only_root_filesystem = read_only_root_filesystem
        if run_as_group is not None:
            self.run_as_group = run_as_group
        if run_as_non_root is not None:
            self.run_as_non_root = run_as_non_root
        if run_as_user is not None:
            self.run_as_user = run_as_user
        if se_linux_options is not None:
            self.se_linux_options = se_linux_options
        if windows_options is not None:
            self.windows_options = windows_options

    @property
    def allow_privilege_escalation(self):
        """Gets the allow_privilege_escalation of this SecurityContext.  # noqa: E501

        AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN +optional  # noqa: E501

        :return: The allow_privilege_escalation of this SecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._allow_privilege_escalation

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation):
        """Sets the allow_privilege_escalation of this SecurityContext.

        AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN +optional  # noqa: E501

        :param allow_privilege_escalation: The allow_privilege_escalation of this SecurityContext.  # noqa: E501
        :type: bool
        """

        self._allow_privilege_escalation = allow_privilege_escalation

    @property
    def capabilities(self):
        """Gets the capabilities of this SecurityContext.  # noqa: E501


        :return: The capabilities of this SecurityContext.  # noqa: E501
        :rtype: Capabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this SecurityContext.


        :param capabilities: The capabilities of this SecurityContext.  # noqa: E501
        :type: Capabilities
        """

        self._capabilities = capabilities

    @property
    def privileged(self):
        """Gets the privileged of this SecurityContext.  # noqa: E501

        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. +optional  # noqa: E501

        :return: The privileged of this SecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this SecurityContext.

        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. +optional  # noqa: E501

        :param privileged: The privileged of this SecurityContext.  # noqa: E501
        :type: bool
        """

        self._privileged = privileged

    @property
    def proc_mount(self):
        """Gets the proc_mount of this SecurityContext.  # noqa: E501


        :return: The proc_mount of this SecurityContext.  # noqa: E501
        :rtype: ProcMountType
        """
        return self._proc_mount

    @proc_mount.setter
    def proc_mount(self, proc_mount):
        """Sets the proc_mount of this SecurityContext.


        :param proc_mount: The proc_mount of this SecurityContext.  # noqa: E501
        :type: ProcMountType
        """

        self._proc_mount = proc_mount

    @property
    def read_only_root_filesystem(self):
        """Gets the read_only_root_filesystem of this SecurityContext.  # noqa: E501

        Whether this container has a read-only root filesystem. Default is false. +optional  # noqa: E501

        :return: The read_only_root_filesystem of this SecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """Sets the read_only_root_filesystem of this SecurityContext.

        Whether this container has a read-only root filesystem. Default is false. +optional  # noqa: E501

        :param read_only_root_filesystem: The read_only_root_filesystem of this SecurityContext.  # noqa: E501
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def run_as_group(self):
        """Gets the run_as_group of this SecurityContext.  # noqa: E501

        The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :return: The run_as_group of this SecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._run_as_group

    @run_as_group.setter
    def run_as_group(self, run_as_group):
        """Sets the run_as_group of this SecurityContext.

        The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :param run_as_group: The run_as_group of this SecurityContext.  # noqa: E501
        :type: int
        """

        self._run_as_group = run_as_group

    @property
    def run_as_non_root(self):
        """Gets the run_as_non_root of this SecurityContext.  # noqa: E501

        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :return: The run_as_non_root of this SecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_non_root

    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root):
        """Sets the run_as_non_root of this SecurityContext.

        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :param run_as_non_root: The run_as_non_root of this SecurityContext.  # noqa: E501
        :type: bool
        """

        self._run_as_non_root = run_as_non_root

    @property
    def run_as_user(self):
        """Gets the run_as_user of this SecurityContext.  # noqa: E501

        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :return: The run_as_user of this SecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this SecurityContext.

        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional  # noqa: E501

        :param run_as_user: The run_as_user of this SecurityContext.  # noqa: E501
        :type: int
        """

        self._run_as_user = run_as_user

    @property
    def se_linux_options(self):
        """Gets the se_linux_options of this SecurityContext.  # noqa: E501


        :return: The se_linux_options of this SecurityContext.  # noqa: E501
        :rtype: SELinuxOptions
        """
        return self._se_linux_options

    @se_linux_options.setter
    def se_linux_options(self, se_linux_options):
        """Sets the se_linux_options of this SecurityContext.


        :param se_linux_options: The se_linux_options of this SecurityContext.  # noqa: E501
        :type: SELinuxOptions
        """

        self._se_linux_options = se_linux_options

    @property
    def windows_options(self):
        """Gets the windows_options of this SecurityContext.  # noqa: E501


        :return: The windows_options of this SecurityContext.  # noqa: E501
        :rtype: WindowsSecurityContextOptions
        """
        return self._windows_options

    @windows_options.setter
    def windows_options(self, windows_options):
        """Sets the windows_options of this SecurityContext.


        :param windows_options: The windows_options of this SecurityContext.  # noqa: E501
        :type: WindowsSecurityContextOptions
        """

        self._windows_options = windows_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SecurityContext, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
