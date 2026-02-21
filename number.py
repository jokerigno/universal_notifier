# /config/custom_components/universal_notifier/number.py
from homeassistant.components.number import NumberEntity, NumberMode
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    async_add_entities([UNotifierBufferVoice(hass, entry)], True)


class UNotifierBufferVoice(NumberEntity):
    _attr_name = "Universal Notifier Voice Buffer"
    _attr_unique_id = f"{DOMAIN}_buffer_voice"
    _attr_native_min_value = 0.5
    _attr_native_max_value = 10.0
    _attr_native_step = 0.5
    _attr_native_unit_of_measurement = "s"
    _attr_mode = NumberMode.SLIDER
    _attr_icon = "mdi:timer-outline"

    def __init__(self, hass, entry):
        self.hass = hass
        self._entry_id = entry.entry_id
        self._attr_native_value = 1.5  # default

    async def async_set_native_value(self, value: float) -> None:
        self.hass.data[DOMAIN][self._entry_id]["tts_buffer"] = value
        self._attr_native_value = value
        self.async_write_ha_state()
