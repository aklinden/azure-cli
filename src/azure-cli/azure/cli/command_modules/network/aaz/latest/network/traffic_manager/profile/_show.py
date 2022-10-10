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
    "network traffic-manager profile show",
)
class Show(AAZCommand):
    """Get the details of a traffic manager profile.

    :example: Get the details of a traffic manager profile.
        az network traffic-manager profile show -g MyResourceGroup -n MyTmProfile
    """

    _aaz_info = {
        "version": "2018-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/trafficmanagerprofiles/{}", "2018-08-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.profile_name = AAZStrArg(
            options=["-n", "--name", "--profile-name"],
            help="The name of the Traffic Manager profile.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.ProfilesGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ProfilesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2018-08-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType()

            properties = cls._schema_on_200.properties
            properties.allowed_endpoint_record_types = AAZListType(
                serialized_name="allowedEndpointRecordTypes",
            )
            properties.dns_config = AAZObjectType(
                serialized_name="dnsConfig",
            )
            properties.endpoints = AAZListType()
            properties.max_return = AAZIntType(
                serialized_name="maxReturn",
            )
            properties.monitor_config = AAZObjectType(
                serialized_name="monitorConfig",
            )
            properties.profile_status = AAZStrType(
                serialized_name="profileStatus",
            )
            properties.traffic_routing_method = AAZStrType(
                serialized_name="trafficRoutingMethod",
            )
            properties.traffic_view_enrollment_status = AAZStrType(
                serialized_name="trafficViewEnrollmentStatus",
            )

            allowed_endpoint_record_types = cls._schema_on_200.properties.allowed_endpoint_record_types
            allowed_endpoint_record_types.Element = AAZStrType()

            dns_config = cls._schema_on_200.properties.dns_config
            dns_config.fqdn = AAZStrType(
                flags={"read_only": True},
            )
            dns_config.relative_name = AAZStrType(
                serialized_name="relativeName",
            )
            dns_config.ttl = AAZIntType()

            endpoints = cls._schema_on_200.properties.endpoints
            endpoints.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.endpoints.Element
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType()

            properties = cls._schema_on_200.properties.endpoints.Element.properties
            properties.custom_headers = AAZListType(
                serialized_name="customHeaders",
            )
            properties.endpoint_location = AAZStrType(
                serialized_name="endpointLocation",
            )
            properties.endpoint_monitor_status = AAZStrType(
                serialized_name="endpointMonitorStatus",
            )
            properties.endpoint_status = AAZStrType(
                serialized_name="endpointStatus",
            )
            properties.geo_mapping = AAZListType(
                serialized_name="geoMapping",
            )
            properties.min_child_endpoints = AAZIntType(
                serialized_name="minChildEndpoints",
            )
            properties.min_child_endpoints_i_pv4 = AAZIntType(
                serialized_name="minChildEndpointsIPv4",
            )
            properties.min_child_endpoints_i_pv6 = AAZIntType(
                serialized_name="minChildEndpointsIPv6",
            )
            properties.priority = AAZIntType()
            properties.subnets = AAZListType()
            properties.target = AAZStrType()
            properties.target_resource_id = AAZStrType(
                serialized_name="targetResourceId",
            )
            properties.weight = AAZIntType()

            custom_headers = cls._schema_on_200.properties.endpoints.Element.properties.custom_headers
            custom_headers.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.endpoints.Element.properties.custom_headers.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            geo_mapping = cls._schema_on_200.properties.endpoints.Element.properties.geo_mapping
            geo_mapping.Element = AAZStrType()

            subnets = cls._schema_on_200.properties.endpoints.Element.properties.subnets
            subnets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.endpoints.Element.properties.subnets.Element
            _element.first = AAZStrType()
            _element.last = AAZStrType()
            _element.scope = AAZIntType()

            monitor_config = cls._schema_on_200.properties.monitor_config
            monitor_config.custom_headers = AAZListType(
                serialized_name="customHeaders",
            )
            monitor_config.expected_status_code_ranges = AAZListType(
                serialized_name="expectedStatusCodeRanges",
            )
            monitor_config.interval_in_seconds = AAZIntType(
                serialized_name="intervalInSeconds",
            )
            monitor_config.path = AAZStrType()
            monitor_config.port = AAZIntType()
            monitor_config.profile_monitor_status = AAZStrType(
                serialized_name="profileMonitorStatus",
            )
            monitor_config.protocol = AAZStrType()
            monitor_config.timeout_in_seconds = AAZIntType(
                serialized_name="timeoutInSeconds",
            )
            monitor_config.tolerated_number_of_failures = AAZIntType(
                serialized_name="toleratedNumberOfFailures",
            )

            custom_headers = cls._schema_on_200.properties.monitor_config.custom_headers
            custom_headers.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.monitor_config.custom_headers.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            expected_status_code_ranges = cls._schema_on_200.properties.monitor_config.expected_status_code_ranges
            expected_status_code_ranges.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.monitor_config.expected_status_code_ranges.Element
            _element.max = AAZIntType()
            _element.min = AAZIntType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Show"]