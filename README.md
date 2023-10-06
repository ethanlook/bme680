# BME 680

This is a Viam module for the [BME 680 sensor](https://www.adafruit.com/product/3660).

## Attributes

| Name                 | Description                                                                                                        | Default     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| `sea_level_pressure` | Match your location's pressure (hPa) at sea level. This varies!                                                    | 1013.25 hPa |
| `temperature offset` | An offset to account for the temperature of the sensor. Usually around 5° but use an external sensor to calibrate. | -5° C       |

## Sensor readings

| Name                | Units |
| ------------------- | ----- |
| `altitude`          | m     |
| `gas`               | ohm   |
| `pressure`          | hPa   |
| `relative_humidity` | %     |
| `temperature`       | ° C   |
