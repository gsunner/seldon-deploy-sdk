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


class StatusConfigurationSpec(object):
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
        'host': 'str',
        'name': 'str',
        'replicas': 'int'
    }

    attribute_map = {
        'host': 'host',
        'name': 'name',
        'replicas': 'replicas'
    }

    def __init__(self, host=None, name=None, replicas=None):  # noqa: E501
        """StatusConfigurationSpec - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._name = None
        self._replicas = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        if replicas is not None:
            self.replicas = replicas

    @property
    def host(self):
        """Gets the host of this StatusConfigurationSpec.  # noqa: E501

        Host name of the service  # noqa: E501

        :return: The host of this StatusConfigurationSpec.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this StatusConfigurationSpec.

        Host name of the service  # noqa: E501

        :param host: The host of this StatusConfigurationSpec.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this StatusConfigurationSpec.  # noqa: E501

        Latest revision name that is in ready state  # noqa: E501

        :return: The name of this StatusConfigurationSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatusConfigurationSpec.

        Latest revision name that is in ready state  # noqa: E501

        :param name: The name of this StatusConfigurationSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def replicas(self):
        """Gets the replicas of this StatusConfigurationSpec.  # noqa: E501


        :return: The replicas of this StatusConfigurationSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this StatusConfigurationSpec.


        :param replicas: The replicas of this StatusConfigurationSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

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
        if issubclass(StatusConfigurationSpec, dict):
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
        if not isinstance(other, StatusConfigurationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
