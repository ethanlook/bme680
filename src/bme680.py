import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from random import uniform
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
import adafruit_bme680
import board


class BME680(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("ethanlook", "sensor"), "bme680")
    MODEL_FAKE: ClassVar[Model] = Model(ModelFamily("ethanlook", "sensor"), "bme680fake")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        sensor.is_fake = False
        i2c = board.I2C()
        sensor.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
        sensor.bme680.sea_level_pressure = config.attributes.fields["sea_level_pressure"].number_value or 1013.25
        sensor.temperature_offset = config.attributes.fields["temperature_offset"].number_value or -5
        return sensor

    @classmethod
    def new_fake(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        sensor.is_fake = True
        sensor.temperature_offset = config.attributes.fields["temperature_offset"].number_value or -5
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        if self.is_fake:
            return {
                "temperature": uniform(19,20) + self.temperature_offset,
                "gas": uniform(0,0.3),
                "relative_humidity": uniform(0.5,0.7),
                "pressure": uniform(20,22),
                "altitude": uniform(10,11),
            }

        return {
            "temperature": self.bme680.temperature + self.temperature_offset,
            "gas": self.bme680.gas,
            "relative_humidity": self.bme680.relative_humidity,
            "pressure": self.bme680.pressure,
            "altitude": self.bme680.altitude,
        }
