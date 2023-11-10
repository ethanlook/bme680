import asyncio

from viam.module.module import Module
from viam.components.sensor import Sensor

from .bme680 import BME680 


async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered.
    """

    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, BME680.MODEL)
    module.add_model_from_registry(Sensor.SUBTYPE, BME680.MODEL_FAKE)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
