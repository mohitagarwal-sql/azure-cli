# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "netappfiles account backup-policy update",
)
class Update(AAZCommand):
    """Update a backup policy for Netapp Account

    :example: Update specific values for an ANF backup policy
        az netappfiles account backup-policy update -g mygroup --account-name myaccountname --backup-policy-name mybackuppolicyname --daily-backups 1 --enabled false
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}/backuppolicies/{}", "2023-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["-a", "--account-name"],
            help="The name of the NetApp account",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,127}$",
            ),
        )
        _args_schema.backup_policy_name = AAZStrArg(
            options=["-b", "-n", "--name", "--backup-policy-name"],
            help="Backup policy Name which uniquely identify backup policy.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.daily_backups = AAZIntArg(
            options=["-d", "--daily-backups"],
            arg_group="Properties",
            help="Daily backups count to keep",
            nullable=True,
        )
        _args_schema.enabled = AAZBoolArg(
            options=["-e", "--enabled"],
            arg_group="Properties",
            help="The property to decide policy is enabled or not",
            nullable=True,
        )
        _args_schema.monthly_backups = AAZIntArg(
            options=["-m", "--monthly-backups"],
            arg_group="Properties",
            help="Monthly backups count to keep",
            nullable=True,
        )
        _args_schema.weekly_backups = AAZIntArg(
            options=["-w", "--weekly-backups"],
            arg_group="Properties",
            help="Weekly backups count to keep",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BackupPoliciesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.BackupPoliciesCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BackupPoliciesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "backupPolicyName", self.ctx.args.backup_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_backup_policy_read(cls._schema_on_200)

            return cls._schema_on_200

    class BackupPoliciesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/backupPolicies/{backupPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "backupPolicyName", self.ctx.args.backup_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_backup_policy_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dailyBackupsToKeep", AAZIntType, ".daily_backups")
                properties.set_prop("enabled", AAZBoolType, ".enabled")
                properties.set_prop("monthlyBackupsToKeep", AAZIntType, ".monthly_backups")
                properties.set_prop("weeklyBackupsToKeep", AAZIntType, ".weekly_backups")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_backup_policy_read = None

    @classmethod
    def _build_schema_backup_policy_read(cls, _schema):
        if cls._schema_backup_policy_read is not None:
            _schema.etag = cls._schema_backup_policy_read.etag
            _schema.id = cls._schema_backup_policy_read.id
            _schema.location = cls._schema_backup_policy_read.location
            _schema.name = cls._schema_backup_policy_read.name
            _schema.properties = cls._schema_backup_policy_read.properties
            _schema.system_data = cls._schema_backup_policy_read.system_data
            _schema.tags = cls._schema_backup_policy_read.tags
            _schema.type = cls._schema_backup_policy_read.type
            return

        cls._schema_backup_policy_read = _schema_backup_policy_read = AAZObjectType()

        backup_policy_read = _schema_backup_policy_read
        backup_policy_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        backup_policy_read.id = AAZStrType(
            flags={"read_only": True},
        )
        backup_policy_read.location = AAZStrType(
            flags={"required": True},
        )
        backup_policy_read.name = AAZStrType(
            flags={"read_only": True},
        )
        backup_policy_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        backup_policy_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        backup_policy_read.tags = AAZDictType()
        backup_policy_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_backup_policy_read.properties
        properties.backup_policy_id = AAZStrType(
            serialized_name="backupPolicyId",
            flags={"read_only": True},
        )
        properties.daily_backups_to_keep = AAZIntType(
            serialized_name="dailyBackupsToKeep",
        )
        properties.enabled = AAZBoolType()
        properties.monthly_backups_to_keep = AAZIntType(
            serialized_name="monthlyBackupsToKeep",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.volume_backups = AAZListType(
            serialized_name="volumeBackups",
            flags={"read_only": True},
        )
        properties.volumes_assigned = AAZIntType(
            serialized_name="volumesAssigned",
            flags={"read_only": True},
        )
        properties.weekly_backups_to_keep = AAZIntType(
            serialized_name="weeklyBackupsToKeep",
        )

        volume_backups = _schema_backup_policy_read.properties.volume_backups
        volume_backups.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_backup_policy_read.properties.volume_backups.Element
        _element.backups_count = AAZIntType(
            serialized_name="backupsCount",
        )
        _element.policy_enabled = AAZBoolType(
            serialized_name="policyEnabled",
        )
        _element.volume_name = AAZStrType(
            serialized_name="volumeName",
        )
        _element.volume_resource_id = AAZStrType(
            serialized_name="volumeResourceId",
        )

        system_data = _schema_backup_policy_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_backup_policy_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_backup_policy_read.etag
        _schema.id = cls._schema_backup_policy_read.id
        _schema.location = cls._schema_backup_policy_read.location
        _schema.name = cls._schema_backup_policy_read.name
        _schema.properties = cls._schema_backup_policy_read.properties
        _schema.system_data = cls._schema_backup_policy_read.system_data
        _schema.tags = cls._schema_backup_policy_read.tags
        _schema.type = cls._schema_backup_policy_read.type


__all__ = ["Update"]
