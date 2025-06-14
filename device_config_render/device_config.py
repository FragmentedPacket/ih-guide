from infrahub_sdk.transforms import InfrahubTransform


class DeviceConfigTransform(InfrahubTransform):
    query = "device_config_query"

    async def transform(self, data):
        device = self.nodes[0]
        device_name = device.name.value
        device_description = device.description.value
        return {
            "device_hostname": device_name,
            "device_description": f"*{device_description}*",
        }
