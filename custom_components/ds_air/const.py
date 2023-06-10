from homeassistant.const import TEMP_CELSIUS, PERCENTAGE, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, \
    CONCENTRATION_PARTS_PER_MILLION, CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, DEVICE_CLASS_HUMIDITY, \
    DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_CO2, DEVICE_CLASS_PM25, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS_PARTS

from .ds_air_service.ctrl_enum import EnumSensor

DOMAIN = "ds_air"
CONF_GW = "gw"
DEFAULT_HOST = "192.168.1."
DEFAULT_PORT = 8008
DEFAULT_GW = "DTA117C611"
GW_LIST = ["DTA117C611", "DTA117B611"]
SENSOR_TYPES = {
    "temp": [TEMP_CELSIUS, None, DEVICE_CLASS_TEMPERATURE, 10],
    "humidity": [PERCENTAGE, None, DEVICE_CLASS_HUMIDITY, 10],
    "pm25": [CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None, DEVICE_CLASS_PM25, 1],
    "co2": [CONCENTRATION_PARTS_PER_MILLION, None, DEVICE_CLASS_CO2, 1],
    "tvoc": [CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, None, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS_PARTS, 100],
    "voc": [None, None, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS_PARTS, EnumSensor.Voc],
    "hcho": [CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, None, None, 100],
}
