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


class InferenceServiceStatus(object):
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
        'address': 'Addressable',
        'canary': 'ComponentStatusMap',
        'canary_traffic': 'int',
        'conditions': 'Conditions',
        'default': 'ComponentStatusMap',
        'observed_generation': 'int',
        'traffic': 'int',
        'url': 'str'
    }

    attribute_map = {
        'address': 'address',
        'canary': 'canary',
        'canary_traffic': 'canaryTraffic',
        'conditions': 'conditions',
        'default': 'default',
        'observed_generation': 'observedGeneration',
        'traffic': 'traffic',
        'url': 'url'
    }

    def __init__(self, address=None, canary=None, canary_traffic=None, conditions=None, default=None, observed_generation=None, traffic=None, url=None):  # noqa: E501
        """InferenceServiceStatus - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._canary = None
        self._canary_traffic = None
        self._conditions = None
        self._default = None
        self._observed_generation = None
        self._traffic = None
        self._url = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if canary is not None:
            self.canary = canary
        if canary_traffic is not None:
            self.canary_traffic = canary_traffic
        if conditions is not None:
            self.conditions = conditions
        if default is not None:
            self.default = default
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if traffic is not None:
            self.traffic = traffic
        if url is not None:
            self.url = url

    @property
    def address(self):
        """Gets the address of this InferenceServiceStatus.  # noqa: E501


        :return: The address of this InferenceServiceStatus.  # noqa: E501
        :rtype: Addressable
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InferenceServiceStatus.


        :param address: The address of this InferenceServiceStatus.  # noqa: E501
        :type: Addressable
        """

        self._address = address

    @property
    def canary(self):
        """Gets the canary of this InferenceServiceStatus.  # noqa: E501


        :return: The canary of this InferenceServiceStatus.  # noqa: E501
        :rtype: ComponentStatusMap
        """
        return self._canary

    @canary.setter
    def canary(self, canary):
        """Sets the canary of this InferenceServiceStatus.


        :param canary: The canary of this InferenceServiceStatus.  # noqa: E501
        :type: ComponentStatusMap
        """

        self._canary = canary

    @property
    def canary_traffic(self):
        """Gets the canary_traffic of this InferenceServiceStatus.  # noqa: E501

        Traffic percentage that goes to canary services  # noqa: E501

        :return: The canary_traffic of this InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._canary_traffic

    @canary_traffic.setter
    def canary_traffic(self, canary_traffic):
        """Sets the canary_traffic of this InferenceServiceStatus.

        Traffic percentage that goes to canary services  # noqa: E501

        :param canary_traffic: The canary_traffic of this InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._canary_traffic = canary_traffic

    @property
    def conditions(self):
        """Gets the conditions of this InferenceServiceStatus.  # noqa: E501


        :return: The conditions of this InferenceServiceStatus.  # noqa: E501
        :rtype: Conditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this InferenceServiceStatus.


        :param conditions: The conditions of this InferenceServiceStatus.  # noqa: E501
        :type: Conditions
        """

        self._conditions = conditions

    @property
    def default(self):
        """Gets the default of this InferenceServiceStatus.  # noqa: E501


        :return: The default of this InferenceServiceStatus.  # noqa: E501
        :rtype: ComponentStatusMap
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this InferenceServiceStatus.


        :param default: The default of this InferenceServiceStatus.  # noqa: E501
        :type: ComponentStatusMap
        """

        self._default = default

    @property
    def observed_generation(self):
        """Gets the observed_generation of this InferenceServiceStatus.  # noqa: E501

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller. +optional  # noqa: E501

        :return: The observed_generation of this InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this InferenceServiceStatus.

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller. +optional  # noqa: E501

        :param observed_generation: The observed_generation of this InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def traffic(self):
        """Gets the traffic of this InferenceServiceStatus.  # noqa: E501

        Traffic percentage that goes to default services  # noqa: E501

        :return: The traffic of this InferenceServiceStatus.  # noqa: E501
        :rtype: int
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this InferenceServiceStatus.

        Traffic percentage that goes to default services  # noqa: E501

        :param traffic: The traffic of this InferenceServiceStatus.  # noqa: E501
        :type: int
        """

        self._traffic = traffic

    @property
    def url(self):
        """Gets the url of this InferenceServiceStatus.  # noqa: E501

        URL of the InferenceService  # noqa: E501

        :return: The url of this InferenceServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InferenceServiceStatus.

        URL of the InferenceService  # noqa: E501

        :param url: The url of this InferenceServiceStatus.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(InferenceServiceStatus, dict):
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
        if not isinstance(other, InferenceServiceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
