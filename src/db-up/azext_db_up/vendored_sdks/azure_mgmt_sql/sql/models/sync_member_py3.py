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

from .proxy_resource_py3 import ProxyResource


class SyncMember(ProxyResource):
    """An Azure SQL Database sync member.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param database_type: Database type of the sync member. Possible values
     include: 'AzureSqlDatabase', 'SqlServerDatabase'
    :type database_type: str or ~azure.mgmt.sql.models.SyncMemberDbType
    :param sync_agent_id: ARM resource id of the sync agent in the sync
     member.
    :type sync_agent_id: str
    :param sql_server_database_id: SQL Server database id of the sync member.
    :type sql_server_database_id: str
    :param server_name: Server name of the member database in the sync member
    :type server_name: str
    :param database_name: Database name of the member database in the sync
     member.
    :type database_name: str
    :param user_name: User name of the member database in the sync member.
    :type user_name: str
    :param password: Password of the member database in the sync member.
    :type password: str
    :param sync_direction: Sync direction of the sync member. Possible values
     include: 'Bidirectional', 'OneWayMemberToHub', 'OneWayHubToMember'
    :type sync_direction: str or ~azure.mgmt.sql.models.SyncDirection
    :ivar sync_state: Sync state of the sync member. Possible values include:
     'SyncInProgress', 'SyncSucceeded', 'SyncFailed',
     'DisabledTombstoneCleanup', 'DisabledBackupRestore',
     'SyncSucceededWithWarnings', 'SyncCancelling', 'SyncCancelled',
     'UnProvisioned', 'Provisioning', 'Provisioned', 'ProvisionFailed',
     'DeProvisioning', 'DeProvisioned', 'DeProvisionFailed', 'Reprovisioning',
     'ReprovisionFailed', 'UnReprovisioned'
    :vartype sync_state: str or ~azure.mgmt.sql.models.SyncMemberState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'sync_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'database_type': {'key': 'properties.databaseType', 'type': 'str'},
        'sync_agent_id': {'key': 'properties.syncAgentId', 'type': 'str'},
        'sql_server_database_id': {'key': 'properties.sqlServerDatabaseId', 'type': 'str'},
        'server_name': {'key': 'properties.serverName', 'type': 'str'},
        'database_name': {'key': 'properties.databaseName', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'sync_direction': {'key': 'properties.syncDirection', 'type': 'str'},
        'sync_state': {'key': 'properties.syncState', 'type': 'str'},
    }

    def __init__(self, *, database_type=None, sync_agent_id: str=None, sql_server_database_id: str=None, server_name: str=None, database_name: str=None, user_name: str=None, password: str=None, sync_direction=None, **kwargs) -> None:
        super(SyncMember, self).__init__(**kwargs)
        self.database_type = database_type
        self.sync_agent_id = sync_agent_id
        self.sql_server_database_id = sql_server_database_id
        self.server_name = server_name
        self.database_name = database_name
        self.user_name = user_name
        self.password = password
        self.sync_direction = sync_direction
        self.sync_state = None
