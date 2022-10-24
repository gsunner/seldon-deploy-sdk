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


class MonitorInputData(object):
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
        'deployment_name': 'str',
        'deployment_type': 'str',
        'end': 'str',
        'group_by': 'str',
        'model_image': 'str',
        'model_name': 'str',
        'model_version': 'str',
        'namespace': 'str',
        'offset': 'str',
        'percentile': 'str',
        'predictor_name': 'str',
        'query_template': 'str',
        'range': 'str',
        'start': 'str',
        'step': 'str'
    }

    attribute_map = {
        'deployment_name': 'DeploymentName',
        'deployment_type': 'DeploymentType',
        'end': 'End',
        'group_by': 'GroupBy',
        'model_image': 'ModelImage',
        'model_name': 'ModelName',
        'model_version': 'ModelVersion',
        'namespace': 'Namespace',
        'offset': 'Offset',
        'percentile': 'Percentile',
        'predictor_name': 'PredictorName',
        'query_template': 'QueryTemplate',
        'range': 'Range',
        'start': 'Start',
        'step': 'Step'
    }

    def __init__(self, deployment_name=None, deployment_type=None, end=None, group_by=None, model_image=None, model_name=None, model_version=None, namespace=None, offset=None, percentile=None, predictor_name=None, query_template=None, range=None, start=None, step=None):  # noqa: E501
        """MonitorInputData - a model defined in Swagger"""  # noqa: E501

        self._deployment_name = None
        self._deployment_type = None
        self._end = None
        self._group_by = None
        self._model_image = None
        self._model_name = None
        self._model_version = None
        self._namespace = None
        self._offset = None
        self._percentile = None
        self._predictor_name = None
        self._query_template = None
        self._range = None
        self._start = None
        self._step = None
        self.discriminator = None

        if deployment_name is not None:
            self.deployment_name = deployment_name
        if deployment_type is not None:
            self.deployment_type = deployment_type
        if end is not None:
            self.end = end
        if group_by is not None:
            self.group_by = group_by
        if model_image is not None:
            self.model_image = model_image
        if model_name is not None:
            self.model_name = model_name
        if model_version is not None:
            self.model_version = model_version
        if namespace is not None:
            self.namespace = namespace
        if offset is not None:
            self.offset = offset
        if percentile is not None:
            self.percentile = percentile
        if predictor_name is not None:
            self.predictor_name = predictor_name
        if query_template is not None:
            self.query_template = query_template
        if range is not None:
            self.range = range
        if start is not None:
            self.start = start
        if step is not None:
            self.step = step

    @property
    def deployment_name(self):
        """Gets the deployment_name of this MonitorInputData.  # noqa: E501


        :return: The deployment_name of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this MonitorInputData.


        :param deployment_name: The deployment_name of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._deployment_name = deployment_name

    @property
    def deployment_type(self):
        """Gets the deployment_type of this MonitorInputData.  # noqa: E501


        :return: The deployment_type of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this MonitorInputData.


        :param deployment_type: The deployment_type of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._deployment_type = deployment_type

    @property
    def end(self):
        """Gets the end of this MonitorInputData.  # noqa: E501


        :return: The end of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MonitorInputData.


        :param end: The end of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def group_by(self):
        """Gets the group_by of this MonitorInputData.  # noqa: E501


        :return: The group_by of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this MonitorInputData.


        :param group_by: The group_by of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._group_by = group_by

    @property
    def model_image(self):
        """Gets the model_image of this MonitorInputData.  # noqa: E501


        :return: The model_image of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._model_image

    @model_image.setter
    def model_image(self, model_image):
        """Sets the model_image of this MonitorInputData.


        :param model_image: The model_image of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._model_image = model_image

    @property
    def model_name(self):
        """Gets the model_name of this MonitorInputData.  # noqa: E501


        :return: The model_name of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this MonitorInputData.


        :param model_name: The model_name of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def model_version(self):
        """Gets the model_version of this MonitorInputData.  # noqa: E501


        :return: The model_version of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this MonitorInputData.


        :param model_version: The model_version of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._model_version = model_version

    @property
    def namespace(self):
        """Gets the namespace of this MonitorInputData.  # noqa: E501


        :return: The namespace of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MonitorInputData.


        :param namespace: The namespace of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def offset(self):
        """Gets the offset of this MonitorInputData.  # noqa: E501


        :return: The offset of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this MonitorInputData.


        :param offset: The offset of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._offset = offset

    @property
    def percentile(self):
        """Gets the percentile of this MonitorInputData.  # noqa: E501


        :return: The percentile of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        """Sets the percentile of this MonitorInputData.


        :param percentile: The percentile of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._percentile = percentile

    @property
    def predictor_name(self):
        """Gets the predictor_name of this MonitorInputData.  # noqa: E501


        :return: The predictor_name of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._predictor_name

    @predictor_name.setter
    def predictor_name(self, predictor_name):
        """Sets the predictor_name of this MonitorInputData.


        :param predictor_name: The predictor_name of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._predictor_name = predictor_name

    @property
    def query_template(self):
        """Gets the query_template of this MonitorInputData.  # noqa: E501


        :return: The query_template of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._query_template

    @query_template.setter
    def query_template(self, query_template):
        """Sets the query_template of this MonitorInputData.


        :param query_template: The query_template of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._query_template = query_template

    @property
    def range(self):
        """Gets the range of this MonitorInputData.  # noqa: E501


        :return: The range of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this MonitorInputData.


        :param range: The range of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._range = range

    @property
    def start(self):
        """Gets the start of this MonitorInputData.  # noqa: E501


        :return: The start of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MonitorInputData.


        :param start: The start of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def step(self):
        """Gets the step of this MonitorInputData.  # noqa: E501


        :return: The step of this MonitorInputData.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this MonitorInputData.


        :param step: The step of this MonitorInputData.  # noqa: E501
        :type: str
        """

        self._step = step

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
        if issubclass(MonitorInputData, dict):
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
        if not isinstance(other, MonitorInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
