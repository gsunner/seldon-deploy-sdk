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


class DeploymentFeatureData(object):
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
        'aggregate_over_time': 'bool',
        'deployment_kind': 'str',
        'deployment_name': 'str',
        'deployment_namespace': 'str',
        'feature': 'str',
        'filters': 'list[FeatureFilter]',
        'interaction': 'FeatureInteraction',
        'parameters': 'FeatureDistributionParameters'
    }

    attribute_map = {
        'aggregate_over_time': 'aggregate_over_time',
        'deployment_kind': 'deployment_kind',
        'deployment_name': 'deployment_name',
        'deployment_namespace': 'deployment_namespace',
        'feature': 'feature',
        'filters': 'filters',
        'interaction': 'interaction',
        'parameters': 'parameters'
    }

    def __init__(self, aggregate_over_time=None, deployment_kind=None, deployment_name=None, deployment_namespace=None, feature=None, filters=None, interaction=None, parameters=None):  # noqa: E501
        """DeploymentFeatureData - a model defined in Swagger"""  # noqa: E501

        self._aggregate_over_time = None
        self._deployment_kind = None
        self._deployment_name = None
        self._deployment_namespace = None
        self._feature = None
        self._filters = None
        self._interaction = None
        self._parameters = None
        self.discriminator = None

        if aggregate_over_time is not None:
            self.aggregate_over_time = aggregate_over_time
        if deployment_kind is not None:
            self.deployment_kind = deployment_kind
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if deployment_namespace is not None:
            self.deployment_namespace = deployment_namespace
        if feature is not None:
            self.feature = feature
        if filters is not None:
            self.filters = filters
        if interaction is not None:
            self.interaction = interaction
        if parameters is not None:
            self.parameters = parameters

    @property
    def aggregate_over_time(self):
        """Gets the aggregate_over_time of this DeploymentFeatureData.  # noqa: E501

        AggregateOverTime is a boolean to decide if the distribution response is to be aggregated over the time period selected  # noqa: E501

        :return: The aggregate_over_time of this DeploymentFeatureData.  # noqa: E501
        :rtype: bool
        """
        return self._aggregate_over_time

    @aggregate_over_time.setter
    def aggregate_over_time(self, aggregate_over_time):
        """Sets the aggregate_over_time of this DeploymentFeatureData.

        AggregateOverTime is a boolean to decide if the distribution response is to be aggregated over the time period selected  # noqa: E501

        :param aggregate_over_time: The aggregate_over_time of this DeploymentFeatureData.  # noqa: E501
        :type: bool
        """

        self._aggregate_over_time = aggregate_over_time

    @property
    def deployment_kind(self):
        """Gets the deployment_kind of this DeploymentFeatureData.  # noqa: E501

        DeploymentType refers to kubernetes kind of the deployment relevant to the feature distribution query  # noqa: E501

        :return: The deployment_kind of this DeploymentFeatureData.  # noqa: E501
        :rtype: str
        """
        return self._deployment_kind

    @deployment_kind.setter
    def deployment_kind(self, deployment_kind):
        """Sets the deployment_kind of this DeploymentFeatureData.

        DeploymentType refers to kubernetes kind of the deployment relevant to the feature distribution query  # noqa: E501

        :param deployment_kind: The deployment_kind of this DeploymentFeatureData.  # noqa: E501
        :type: str
        """

        self._deployment_kind = deployment_kind

    @property
    def deployment_name(self):
        """Gets the deployment_name of this DeploymentFeatureData.  # noqa: E501

        DeploymentName refers to name of the deployment relevant to the feature distribution query  # noqa: E501

        :return: The deployment_name of this DeploymentFeatureData.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this DeploymentFeatureData.

        DeploymentName refers to name of the deployment relevant to the feature distribution query  # noqa: E501

        :param deployment_name: The deployment_name of this DeploymentFeatureData.  # noqa: E501
        :type: str
        """

        self._deployment_name = deployment_name

    @property
    def deployment_namespace(self):
        """Gets the deployment_namespace of this DeploymentFeatureData.  # noqa: E501

        DeploymentNamespace refers to namespace of the deployment relevant to the feature distribution query  # noqa: E501

        :return: The deployment_namespace of this DeploymentFeatureData.  # noqa: E501
        :rtype: str
        """
        return self._deployment_namespace

    @deployment_namespace.setter
    def deployment_namespace(self, deployment_namespace):
        """Sets the deployment_namespace of this DeploymentFeatureData.

        DeploymentNamespace refers to namespace of the deployment relevant to the feature distribution query  # noqa: E501

        :param deployment_namespace: The deployment_namespace of this DeploymentFeatureData.  # noqa: E501
        :type: str
        """

        self._deployment_namespace = deployment_namespace

    @property
    def feature(self):
        """Gets the feature of this DeploymentFeatureData.  # noqa: E501

        FeatureName refers to the name of feature as per the model predictions schema  # noqa: E501

        :return: The feature of this DeploymentFeatureData.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this DeploymentFeatureData.

        FeatureName refers to the name of feature as per the model predictions schema  # noqa: E501

        :param feature: The feature of this DeploymentFeatureData.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def filters(self):
        """Gets the filters of this DeploymentFeatureData.  # noqa: E501

        Filters is a set of time, feature and/or outlier filters for the distribution/stats query  # noqa: E501

        :return: The filters of this DeploymentFeatureData.  # noqa: E501
        :rtype: list[FeatureFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DeploymentFeatureData.

        Filters is a set of time, feature and/or outlier filters for the distribution/stats query  # noqa: E501

        :param filters: The filters of this DeploymentFeatureData.  # noqa: E501
        :type: list[FeatureFilter]
        """

        self._filters = filters

    @property
    def interaction(self):
        """Gets the interaction of this DeploymentFeatureData.  # noqa: E501


        :return: The interaction of this DeploymentFeatureData.  # noqa: E501
        :rtype: FeatureInteraction
        """
        return self._interaction

    @interaction.setter
    def interaction(self, interaction):
        """Sets the interaction of this DeploymentFeatureData.


        :param interaction: The interaction of this DeploymentFeatureData.  # noqa: E501
        :type: FeatureInteraction
        """

        self._interaction = interaction

    @property
    def parameters(self):
        """Gets the parameters of this DeploymentFeatureData.  # noqa: E501


        :return: The parameters of this DeploymentFeatureData.  # noqa: E501
        :rtype: FeatureDistributionParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DeploymentFeatureData.


        :param parameters: The parameters of this DeploymentFeatureData.  # noqa: E501
        :type: FeatureDistributionParameters
        """

        self._parameters = parameters

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
        if issubclass(DeploymentFeatureData, dict):
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
        if not isinstance(other, DeploymentFeatureData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other