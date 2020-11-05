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


class CSIVolumeSource(object):
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
        'driver': 'str',
        'fs_type': 'str',
        'node_publish_secret_ref': 'LocalObjectReference',
        'read_only': 'bool',
        'volume_attributes': 'dict(str, str)'
    }

    attribute_map = {
        'driver': 'driver',
        'fs_type': 'fsType',
        'node_publish_secret_ref': 'nodePublishSecretRef',
        'read_only': 'readOnly',
        'volume_attributes': 'volumeAttributes'
    }

    def __init__(self, driver=None, fs_type=None, node_publish_secret_ref=None, read_only=None, volume_attributes=None):  # noqa: E501
        """CSIVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._driver = None
        self._fs_type = None
        self._node_publish_secret_ref = None
        self._read_only = None
        self._volume_attributes = None
        self.discriminator = None

        if driver is not None:
            self.driver = driver
        if fs_type is not None:
            self.fs_type = fs_type
        if node_publish_secret_ref is not None:
            self.node_publish_secret_ref = node_publish_secret_ref
        if read_only is not None:
            self.read_only = read_only
        if volume_attributes is not None:
            self.volume_attributes = volume_attributes

    @property
    def driver(self):
        """Gets the driver of this CSIVolumeSource.  # noqa: E501

        Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.  # noqa: E501

        :return: The driver of this CSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this CSIVolumeSource.

        Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.  # noqa: E501

        :param driver: The driver of this CSIVolumeSource.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def fs_type(self):
        """Gets the fs_type of this CSIVolumeSource.  # noqa: E501

        Filesystem type to mount. Ex. \"ext4\", \"xfs\", \"ntfs\". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. +optional  # noqa: E501

        :return: The fs_type of this CSIVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this CSIVolumeSource.

        Filesystem type to mount. Ex. \"ext4\", \"xfs\", \"ntfs\". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. +optional  # noqa: E501

        :param fs_type: The fs_type of this CSIVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def node_publish_secret_ref(self):
        """Gets the node_publish_secret_ref of this CSIVolumeSource.  # noqa: E501


        :return: The node_publish_secret_ref of this CSIVolumeSource.  # noqa: E501
        :rtype: LocalObjectReference
        """
        return self._node_publish_secret_ref

    @node_publish_secret_ref.setter
    def node_publish_secret_ref(self, node_publish_secret_ref):
        """Sets the node_publish_secret_ref of this CSIVolumeSource.


        :param node_publish_secret_ref: The node_publish_secret_ref of this CSIVolumeSource.  # noqa: E501
        :type: LocalObjectReference
        """

        self._node_publish_secret_ref = node_publish_secret_ref

    @property
    def read_only(self):
        """Gets the read_only of this CSIVolumeSource.  # noqa: E501

        Specifies a read-only configuration for the volume. Defaults to false (read/write). +optional  # noqa: E501

        :return: The read_only of this CSIVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this CSIVolumeSource.

        Specifies a read-only configuration for the volume. Defaults to false (read/write). +optional  # noqa: E501

        :param read_only: The read_only of this CSIVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def volume_attributes(self):
        """Gets the volume_attributes of this CSIVolumeSource.  # noqa: E501

        VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. +optional  # noqa: E501

        :return: The volume_attributes of this CSIVolumeSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._volume_attributes

    @volume_attributes.setter
    def volume_attributes(self, volume_attributes):
        """Sets the volume_attributes of this CSIVolumeSource.

        VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. +optional  # noqa: E501

        :param volume_attributes: The volume_attributes of this CSIVolumeSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._volume_attributes = volume_attributes

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
        if issubclass(CSIVolumeSource, dict):
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
        if not isinstance(other, CSIVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
