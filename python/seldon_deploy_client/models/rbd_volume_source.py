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


class RBDVolumeSource(object):
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
        'fs_type': 'str',
        'image': 'str',
        'keyring': 'str',
        'monitors': 'list[str]',
        'pool': 'str',
        'read_only': 'bool',
        'secret_ref': 'LocalObjectReference',
        'user': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'image': 'image',
        'keyring': 'keyring',
        'monitors': 'monitors',
        'pool': 'pool',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'user': 'user'
    }

    def __init__(self, fs_type=None, image=None, keyring=None, monitors=None, pool=None, read_only=None, secret_ref=None, user=None):  # noqa: E501
        """RBDVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._fs_type = None
        self._image = None
        self._keyring = None
        self._monitors = None
        self._pool = None
        self._read_only = None
        self._secret_ref = None
        self._user = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if image is not None:
            self.image = image
        if keyring is not None:
            self.keyring = keyring
        if monitors is not None:
            self.monitors = monitors
        if pool is not None:
            self.pool = pool
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if user is not None:
            self.user = user

    @property
    def fs_type(self):
        """Gets the fs_type of this RBDVolumeSource.  # noqa: E501

        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd TODO: how do we prevent errors in the filesystem from compromising the machine +optional  # noqa: E501

        :return: The fs_type of this RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this RBDVolumeSource.

        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd TODO: how do we prevent errors in the filesystem from compromising the machine +optional  # noqa: E501

        :param fs_type: The fs_type of this RBDVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def image(self):
        """Gets the image of this RBDVolumeSource.  # noqa: E501

        The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The image of this RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this RBDVolumeSource.

        The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param image: The image of this RBDVolumeSource.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def keyring(self):
        """Gets the keyring of this RBDVolumeSource.  # noqa: E501

        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :return: The keyring of this RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._keyring

    @keyring.setter
    def keyring(self, keyring):
        """Sets the keyring of this RBDVolumeSource.

        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :param keyring: The keyring of this RBDVolumeSource.  # noqa: E501
        :type: str
        """

        self._keyring = keyring

    @property
    def monitors(self):
        """Gets the monitors of this RBDVolumeSource.  # noqa: E501

        A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :return: The monitors of this RBDVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this RBDVolumeSource.

        A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it  # noqa: E501

        :param monitors: The monitors of this RBDVolumeSource.  # noqa: E501
        :type: list[str]
        """

        self._monitors = monitors

    @property
    def pool(self):
        """Gets the pool of this RBDVolumeSource.  # noqa: E501

        The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :return: The pool of this RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this RBDVolumeSource.

        The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :param pool: The pool of this RBDVolumeSource.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def read_only(self):
        """Gets the read_only of this RBDVolumeSource.  # noqa: E501

        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :return: The read_only of this RBDVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this RBDVolumeSource.

        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :param read_only: The read_only of this RBDVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this RBDVolumeSource.  # noqa: E501


        :return: The secret_ref of this RBDVolumeSource.  # noqa: E501
        :rtype: LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this RBDVolumeSource.


        :param secret_ref: The secret_ref of this RBDVolumeSource.  # noqa: E501
        :type: LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def user(self):
        """Gets the user of this RBDVolumeSource.  # noqa: E501

        The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :return: The user of this RBDVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RBDVolumeSource.

        The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it +optional  # noqa: E501

        :param user: The user of this RBDVolumeSource.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(RBDVolumeSource, dict):
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
        if not isinstance(other, RBDVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
