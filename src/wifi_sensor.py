import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from typing_extensions import Self
from viam.components.sensor import Sensor
from viam.operations import run_with_operation
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

class MySensor(Sensor):
    # Subclass the Viam Arm component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("fahmina","wifi_sensor"), "linux")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
        quality = content[2]
        quality = quality.split(" ")
        clean_quality = [x for x in quality if x != '']
        return {"link": clean_quality[2], "level": clean_quality[3], "noise": clean_quality[4]}

async def main():
    wifi=MySensor(name="wifi")
    signal = await wifi.get_readings()
    print(signal)

if __name__ == '__main__':
    asyncio.run(main())