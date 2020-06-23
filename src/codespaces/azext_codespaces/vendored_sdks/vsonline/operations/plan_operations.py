# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class PlanOperations(object):
    """PlanOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to be used with the HTTP request. Constant value: "2020-05-26-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = config.api_version or "2020-05-26-preview"

        self.config = config

    def get(
            self, resource_group_name, plan_name, custom_headers=None, raw=False, **operation_config):
        """Retrieves information about a VS Online Plan resource.

        Retrieves the properties of a VS Online Plan.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlan or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlan or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlan', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}'}

    def delete(
            self, resource_group_name, plan_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a VS Online Plan resource.

        Deletes an existing VS Online Plan.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}'}

    def create(
            self, resource_group_name, plan_name, vsonline_plan, custom_headers=None, raw=False, **operation_config):
        """Creates a VS Online Plan.

        Creates a VS Online Plan with the specified create parameters.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param vsonline_plan: VS Online Plan create parameters.
        :type vsonline_plan: ~microsoft.vsonline.models.VSOnlinePlan
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlan or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlan or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(vsonline_plan, 'VSOnlinePlan')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlan', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}'}

    def update(
            self, resource_group_name, plan_name, vsonline_plan_update_parameters, custom_headers=None, raw=False, **operation_config):
        """Updates a VS Online Plan.

        Updates the properties of an existing VS Online Plan with the specified
        update parameters.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param vsonline_plan_update_parameters: Parameters for updating the VS
         Online Plan.
        :type vsonline_plan_update_parameters:
         ~microsoft.vsonline.models.VSOPlanUpdateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlan or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlan or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(vsonline_plan_update_parameters, 'VSOPlanUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlan', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}'}

    def read_all_environments_action(
            self, resource_group_name, plan_name, expiration=None, custom_headers=None, raw=False, **operation_config):
        """Get VS Online Plan read environments access token.

        Get VS Online Plan access token which allows listing all environments
        in the Plan.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param expiration: The requested expiration UNIX timestamp (seconds
         since epoch) of a VS Online Plan access token.
        :type expiration: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlanAccessToken or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlanAccessToken or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.read_all_environments_action.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if expiration is not None:
            query_parameters['expiration'] = self._serialize.query("expiration", expiration, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlanAccessToken', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    read_all_environments_action.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}/readAllEnvironments'}

    def write_environments_action(
            self, resource_group_name, plan_name, expiration=None, custom_headers=None, raw=False, **operation_config):
        """Get VS Online Plan write environments access token.

        Get VS Online Plan access token which allows creating, updating,
        deleting and connecting to environments owned by the user.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param expiration: The requested expiration UNIX timestamp (seconds
         since epoch) of a VS Online Plan access token.
        :type expiration: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlanAccessToken or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlanAccessToken or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.write_environments_action.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if expiration is not None:
            query_parameters['expiration'] = self._serialize.query("expiration", expiration, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlanAccessToken', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    write_environments_action.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}/writeEnvironments'}

    def delete_all_environments_action(
            self, resource_group_name, plan_name, expiration=None, custom_headers=None, raw=False, **operation_config):
        """Get VS Online Plan read and delete environments access token.

        Get VS Online Plan access token which allows reading and deleting all
        environments in the Plan.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param expiration: The requested expiration UNIX timestamp (seconds
         since epoch) of a VS Online Plan access token.
        :type expiration: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlanAccessToken or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlanAccessToken or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.delete_all_environments_action.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if expiration is not None:
            query_parameters['expiration'] = self._serialize.query("expiration", expiration, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlanAccessToken', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_all_environments_action.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}/deleteAllEnvironments'}

    def write_delegates_action(
            self, resource_group_name, plan_name, delegate_request, custom_headers=None, raw=False, **operation_config):
        """Get VS Online Plan delegated write environments access token.

        Get VS Online Plan delegated access token which allows creating,
        updating, deleting and connecting to environments owned by the user.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param plan_name: Name of the VS Online Plan
        :type plan_name: str
        :param delegate_request: VS Online Plan delegate access token
         parameters.
        :type delegate_request:
         ~microsoft.vsonline.models.VSOnlineDelegateAccessTokenRequestBody
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VSOnlinePlanAccessToken or ClientRawResponse if raw=true
        :rtype: ~microsoft.vsonline.models.VSOnlinePlanAccessToken or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        # Construct URL
        url = self.write_delegates_action.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'planName': self._serialize.url("plan_name", plan_name, 'str', pattern=r'^[a-zA-Z0-9]')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(delegate_request, 'VSOnlineDelegateAccessTokenRequestBody')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.VSOPlanErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VSOnlinePlanAccessToken', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    write_delegates_action.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans/{planName}/writeDelegates'}

    def list_by_resource_group(
            self, resource_group_name, custom_headers=None, raw=False, **operation_config):
        """Retrieves information about all VS Online Plan resources under the
        given subscription and resource group.

        Retrieves the properties of all VS Online Plans.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of VSOnlinePlan
        :rtype:
         ~microsoft.vsonline.models.VSOnlinePlanPaged[~microsoft.vsonline.models.VSOnlinePlan]
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.VSOPlanErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.VSOnlinePlanPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.VSOnlinePlanPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VSOnline/plans'}

    def list_by_subscription(
            self, custom_headers=None, raw=False, **operation_config):
        """Retrieves information about all VS Online Plan resources under the
        given subscription.

        Retrieves the properties of all VS Online Plans.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of VSOnlinePlan
        :rtype:
         ~microsoft.vsonline.models.VSOnlinePlanPaged[~microsoft.vsonline.models.VSOnlinePlan]
        :raises:
         :class:`VSOPlanErrorResponseException<microsoft.vsonline.models.VSOPlanErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.VSOPlanErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.VSOnlinePlanPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.VSOnlinePlanPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.VSOnline/plans'}
