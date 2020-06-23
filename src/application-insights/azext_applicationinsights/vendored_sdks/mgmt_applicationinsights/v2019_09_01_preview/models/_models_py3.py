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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AzureResourceProperties(Model):
    """An Azure resource QueryPack-Query object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureResourceProperties, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Describe the format of an Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class QueryPacksResource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(QueryPacksResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class LogAnalyticsQueryPack(QueryPacksResource):
    """An Log Analytics QueryPack definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar query_pack_id: The unique ID of your application. This field cannot
     be changed.
    :vartype query_pack_id: str
    :ivar time_created: Creation Date for the Log Analytics QueryPack, in ISO
     8601 format.
    :vartype time_created: datetime
    :ivar time_modified: Last modified date of the Log Analytics QueryPack, in
     ISO 8601 format.
    :vartype time_modified: datetime
    :ivar provisioning_state: Current state of this QueryPack: whether or not
     is has been provisioned within the resource group it is defined. Users
     cannot change this value but are able to read from it. Values will include
     Succeeded, Deploying, Canceled, and Failed.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'query_pack_id': {'readonly': True},
        'time_created': {'readonly': True},
        'time_modified': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'query_pack_id': {'key': 'properties.queryPackId', 'type': 'str'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(LogAnalyticsQueryPack, self).__init__(location=location, tags=tags, **kwargs)
        self.query_pack_id = None
        self.time_created = None
        self.time_modified = None
        self.provisioning_state = None


class LogAnalyticsQueryPackQuery(AzureResourceProperties):
    """A Log Analytics QueryPack-Query definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar query_id: The unique ID of your application. This field cannot be
     changed.
    :vartype query_id: str
    :param display_name: Required. Unique display name for your query within
     the Query Pack.
    :type display_name: str
    :ivar time_created: Creation Date for the Log Analytics Query, in ISO 8601
     format.
    :vartype time_created: datetime
    :ivar time_modified: Last modified date of the Log Analytics Query, in ISO
     8601 format.
    :vartype time_modified: datetime
    :ivar author: Object Id of user creating the query.
    :vartype author: str
    :param description: Description of the query.
    :type description: str
    :param body: Required. Body of the query.
    :type body: str
    :param linked_resource_id: Resource id associated with the query.
    :type linked_resource_id: str
    :param categories: Categories associated with the query.
    :type categories: list[str]
    :param resource_types: Resource Types associated with the query.
    :type resource_types: list[str]
    :param labels: Labels associated with the query.
    :type labels: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'query_id': {'readonly': True},
        'display_name': {'required': True},
        'time_created': {'readonly': True},
        'time_modified': {'readonly': True},
        'author': {'readonly': True},
        'body': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'query_id': {'key': 'properties.queryId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'body': {'key': 'properties.body', 'type': 'str'},
        'linked_resource_id': {'key': 'properties.linkedResourceId', 'type': 'str'},
        'categories': {'key': 'properties.categories', 'type': '[str]'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[str]'},
        'labels': {'key': 'properties.labels', 'type': '[str]'},
    }

    def __init__(self, *, display_name: str, body: str, description: str=None, linked_resource_id: str=None, categories=None, resource_types=None, labels=None, **kwargs) -> None:
        super(LogAnalyticsQueryPackQuery, self).__init__(**kwargs)
        self.query_id = None
        self.display_name = display_name
        self.time_created = None
        self.time_modified = None
        self.author = None
        self.description = description
        self.body = body
        self.linked_resource_id = linked_resource_id
        self.categories = categories
        self.resource_types = resource_types
        self.labels = labels


class LogAnalyticsQueryPackQuerySearchProperties(Model):
    """Properties that define an Log Analytics QueryPack-Query search properties.

    :param categories: Categories associated with the query.
    :type categories: list[str]
    :param resource_types: Resource Types associated with the query.
    :type resource_types: list[str]
    :param labels: Labels associated with the query.
    :type labels: list[str]
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'resource_types': {'key': 'resourceTypes', 'type': '[str]'},
        'labels': {'key': 'labels', 'type': '[str]'},
    }

    def __init__(self, *, categories=None, resource_types=None, labels=None, **kwargs) -> None:
        super(LogAnalyticsQueryPackQuerySearchProperties, self).__init__(**kwargs)
        self.categories = categories
        self.resource_types = resource_types
        self.labels = labels


class TagsResource(Model):
    """A container holding only the Tags for a resource, allowing the user to
    update the tags on a QueryPack instance.

    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(TagsResource, self).__init__(**kwargs)
        self.tags = tags
