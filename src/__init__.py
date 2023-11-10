from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .bme680 import BME680


Registry.register_resource_creator(Sensor.SUBTYPE, BME680.MODEL, ResourceCreatorRegistration(BME680.new))
Registry.register_resource_creator(Sensor.SUBTYPE, BME680.MODEL_FAKE, ResourceCreatorRegistration(BME680.new_fake))
