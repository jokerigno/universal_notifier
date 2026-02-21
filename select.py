# /config/custom_components/universal_notifier/select.py
from homeassistant.components.select import SelectEntity
from .const import DOMAIN, CONF_PRIORITY_VOLUME

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([
        PriorityVolumeSelect(hass, entry),
        TextFormatSelect(hass, entry),
        NotificationModeSelect(hass, entry),
    ], True)

class PriorityVolumeSelect(SelectEntity):
    def __init__(self, hass, entry):
        self.hass = hass
        self._entry_id = entry.entry_id
        self._attr_name = "Universal Notifier Priority Volume"
        self._attr_unique_id = f"{DOMAIN}_selector"
        self._attr_options = [str(round(i/10, 1)) for i in range(1, 11)]
        conf = hass.data[DOMAIN][entry.entry_id]["conf"]
        self._attr_current_option = str(conf.get(CONF_PRIORITY_VOLUME, 0.9))

    async def async_select_option(self, option: str) -> None:
        self.hass.data[DOMAIN][self._entry_id]["runtime_priority_vol"] = float(option)
        self._attr_current_option = option
        self.async_write_ha_state()


class TextFormatSelect(SelectEntity):
    _attr_name = "Universal Notifier Text Format"
    _attr_unique_id = f"{DOMAIN}_text_format"
    _attr_options = ["html", "markdown"]
    _attr_icon = "mdi:format-text"

    def __init__(self, hass, entry):
        self.hass = hass
        self._entry_id = entry.entry_id
        self._attr_current_option = "html"

    async def async_select_option(self, option: str) -> None:
        self.hass.data[DOMAIN][self._entry_id]["text_format"] = option
        self._attr_current_option = option
        self.async_write_ha_state()


class NotificationModeSelect(SelectEntity):
    _attr_name = "Universal Notifier Notification Mode"
    _attr_unique_id = f"{DOMAIN}_notification_mode"
    _attr_options = ["Normal", "Voice home", "Text home"]
    _attr_icon = "mdi:home-sound-out"

    def __init__(self, hass, entry):
        self.hass = hass
        self._entry_id = entry.entry_id
        self._attr_current_option = "Normal"

    async def async_select_option(self, option: str) -> None:
        self.hass.data[DOMAIN][self._entry_id]["notification_mode"] = option
        self._attr_current_option = option
        self.async_write_ha_state()