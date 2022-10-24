# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelStatus(object):
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
        'annotations': 'dict(str, str)',
        'conditions': 'Conditions',
        'observed_generation': 'int',
        'replicas': 'int'
    }

    attribute_map = {
        'annotations': 'annotations',
        'conditions': 'conditions',
        'observed_generation': 'observedGeneration',
        'replicas': 'replicas'
    }

    def __init__(self, annotations=None, conditions=None, observed_generation=None, replicas=None):  # noqa: E501
        """ModelStatus - a model defined in Swagger"""  # noqa: E501

        self._annotations = None
        self._conditions = None
        self._observed_generation = None
        self._replicas = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if conditions is not None:
            self.conditions = conditions
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if replicas is not None:
            self.replicas = replicas

    @property
    def annotations(self):
        """Gets the annotations of this ModelStatus.  # noqa: E501

        Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.  # noqa: E501

        :return: The annotations of this ModelStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ModelStatus.

        Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards.  # noqa: E501

        :param annotations: The annotations of this ModelStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def conditions(self):
        """Gets the conditions of this ModelStatus.  # noqa: E501


        :return: The conditions of this ModelStatus.  # noqa: E501
        :rtype: Conditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ModelStatus.


        :param conditions: The conditions of this ModelStatus.  # noqa: E501
        :type: Conditions
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """Gets the observed_generation of this ModelStatus.  # noqa: E501

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller. +optional  # noqa: E501

        :return: The observed_generation of this ModelStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this ModelStatus.

        ObservedGeneration is the 'Generation' of the Service that was last processed by the controller. +optional  # noqa: E501

        :param observed_generation: The observed_generation of this ModelStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def replicas(self):
        """Gets the replicas of this ModelStatus.  # noqa: E501

        Total number of replicas targeted by this model  # noqa: E501

        :return: The replicas of this ModelStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ModelStatus.

        Total number of replicas targeted by this model  # noqa: E501

        :param replicas: The replicas of this ModelStatus.  # noqa: E501
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
        if issubclass(ModelStatus, dict):
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
        if not isinstance(other, ModelStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
