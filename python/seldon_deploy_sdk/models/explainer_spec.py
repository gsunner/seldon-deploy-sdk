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


class ExplainerSpec(object):
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
        'model_ref': 'str',
        'pipeline_ref': 'str',
        'type': 'str'
    }

    attribute_map = {
        'model_ref': 'modelRef',
        'pipeline_ref': 'pipelineRef',
        'type': 'type'
    }

    def __init__(self, model_ref=None, pipeline_ref=None, type=None):  # noqa: E501
        """ExplainerSpec - a model defined in Swagger"""  # noqa: E501

        self._model_ref = None
        self._pipeline_ref = None
        self._type = None
        self.discriminator = None

        if model_ref is not None:
            self.model_ref = model_ref
        if pipeline_ref is not None:
            self.pipeline_ref = pipeline_ref
        if type is not None:
            self.type = type

    @property
    def model_ref(self):
        """Gets the model_ref of this ExplainerSpec.  # noqa: E501

        one of the following need to be set for blackbox explainers Reference to Model +optional  # noqa: E501

        :return: The model_ref of this ExplainerSpec.  # noqa: E501
        :rtype: str
        """
        return self._model_ref

    @model_ref.setter
    def model_ref(self, model_ref):
        """Sets the model_ref of this ExplainerSpec.

        one of the following need to be set for blackbox explainers Reference to Model +optional  # noqa: E501

        :param model_ref: The model_ref of this ExplainerSpec.  # noqa: E501
        :type: str
        """

        self._model_ref = model_ref

    @property
    def pipeline_ref(self):
        """Gets the pipeline_ref of this ExplainerSpec.  # noqa: E501

        Reference to Pipeline +optional  # noqa: E501

        :return: The pipeline_ref of this ExplainerSpec.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_ref

    @pipeline_ref.setter
    def pipeline_ref(self, pipeline_ref):
        """Sets the pipeline_ref of this ExplainerSpec.

        Reference to Pipeline +optional  # noqa: E501

        :param pipeline_ref: The pipeline_ref of this ExplainerSpec.  # noqa: E501
        :type: str
        """

        self._pipeline_ref = pipeline_ref

    @property
    def type(self):
        """Gets the type of this ExplainerSpec.  # noqa: E501

        type of explainer  # noqa: E501

        :return: The type of this ExplainerSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExplainerSpec.

        type of explainer  # noqa: E501

        :param type: The type of this ExplainerSpec.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ExplainerSpec, dict):
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
        if not isinstance(other, ExplainerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
