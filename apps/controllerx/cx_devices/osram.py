from cx_const import DefaultActionsMapping, Light, Z2MLight
from cx_core import LightController, Z2MLightController
from cx_core.integration import EventData


class OsramAC025XX00NZ2MJLightController(Z2MLightController):
    # This mapping works for: AC0251100NJ / AC0251400NJ / AC0251600NJ / AC0251700NJ
    # (different models are just different colours)

    def get_z2m_actions_mapping(self) -> DefaultActionsMapping:
        return {
            # Click Arrow up
            "on": Z2MLight.ON,
            # Click Arrow up (legacy)
            "up": Z2MLight.ON,
            # Hold Arrow Up
            "brightness_move_up": Z2MLight.HOLD_BRIGHTNESS_UP,
            # Hold Arrow Up (legacy)
            "up_hold": Z2MLight.HOLD_BRIGHTNESS_UP,
            # Release Arrow Up
            "brightness_stop": Z2MLight.RELEASE,
            # Release Arrow Up (legacy)
            "up_release": Z2MLight.RELEASE,
            # Click Circle button
            "brightness_move_to_level": Z2MLight.BRIGHTNESS_FROM_CONTROLLER_LEVEL,
            "color_temperature_move": Z2MLight.COLORTEMP_FROM_CONTROLLER,
            # Click Circle button (legacy)
            "circle_click": Z2MLight.BRIGHTNESS_FROM_CONTROLLER_LEVEL,
            # Hold Circle button
            "move_to_saturation": None,
            "hue_move": Z2MLight.HOLD_COLOR_TEMP_UP,
            # Hold Circle button (legacy)
            "circle_hold": Z2MLight.HOLD_COLOR_TEMP_UP,
            # Release Circle button
            "hue_stop": Z2MLight.RELEASE,
            # Click Arrow down
            "off": Z2MLight.OFF,
            # Click Arrow down (legacy)
            "down": Z2MLight.OFF,
            # Hold Arrow down
            "brightness_move_down": Z2MLight.HOLD_BRIGHTNESS_DOWN,
            # Hold Arrow down (legacy)
            "down_hold": Z2MLight.HOLD_BRIGHTNESS_DOWN,
            # Release Arrow Down (Taken care of by up release)
            # "brightness_stop": Z2MLight.RELEASE,
            # Release Arrow Down (legacy)
            "down_release": Z2MLight.RELEASE,
        }


class OsramAC025XX00NJLightController(LightController):
    # This mapping works for: AC0251100NJ / AC0251400NJ / AC0251600NJ / AC0251700NJ
    # (different models are just different colours)

    def get_z2m_actions_mapping(self) -> DefaultActionsMapping:
        return {
            # Click Arrow up
            "on": Light.ON,
            # Click Arrow up (legacy)
            "up": Light.ON,
            # Hold Arrow Up
            "brightness_move_up": Light.HOLD_BRIGHTNESS_UP,
            # Hold Arrow Up (legacy)
            "up_hold": Light.HOLD_BRIGHTNESS_UP,
            # Release Arrow Up
            "brightness_stop": Light.RELEASE,
            # Release Arrow Up (legacy)
            "up_release": Light.RELEASE,
            # Click Circle button
            "brightness_move_to_level": Light.BRIGHTNESS_FROM_CONTROLLER_LEVEL,
            "color_temperature_move": Light.COLORTEMP_FROM_CONTROLLER,
            # Click Circle button (legacy)
            "circle_click": Light.SYNC,
            # Hold Circle button
            "move_to_saturation": None,
            "hue_move": Light.HOLD_COLOR_UP,
            # Hold Circle button (legacy)
            "circle_hold": Light.HOLD_COLOR_UP,
            # Release Circle button
            "hue_stop": Light.RELEASE,
            # Release Circle button (legacy)
            "circle_release": Light.RELEASE,
            # Click Arrow down
            "off": Light.OFF,
            # Click Arrow down (legacy)
            "down": Light.OFF,
            # Hold Arrow down
            "brightness_move_down": Light.HOLD_BRIGHTNESS_DOWN,
            # Hold Arrow down (legacy)
            "down_hold": Light.HOLD_BRIGHTNESS_DOWN,
            # Release Arrow Down (Taken care of by up release)
            # "brightness_stop": Light.RELEASE,
            # Release Arrow Down (legacy)
            "down_release": Light.RELEASE,
        }

    def get_deconz_actions_mapping(self) -> DefaultActionsMapping:
        return {
            1002: Light.ON,  # Click Arrow up
            1001: Light.HOLD_BRIGHTNESS_UP,  # Hold Arrow Up
            1003: Light.RELEASE,  # Release Arrow Up
            2002: Light.OFF,  # Click Arrow down
            2001: Light.HOLD_BRIGHTNESS_DOWN,  # Hold Arrow down
            2003: Light.RELEASE,  # Release Arrow down
            3002: Light.SYNC,  # Click Circle button
            3001: Light.HOLD_COLOR_UP,  # Hold Circle button
            3003: Light.RELEASE,  # Release Circle button
        }

    def get_zha_actions_mapping(self) -> DefaultActionsMapping:
        return {
            "1_on": Light.ON,
            "1_move_with_on_off": Light.HOLD_BRIGHTNESS_UP,
            "1_stop": Light.RELEASE,
            "3_move_to_level_with_on_off": None,
            "3_move_to_color_temp": Light.SYNC,
            "3_move_to_saturation": Light.HOLD_COLOR_UP,
            "3_move_hue": Light.RELEASE,
            "2_off": Light.OFF,
            "2_move": Light.HOLD_BRIGHTNESS_DOWN,
            "2_stop": Light.RELEASE,
        }

    def get_zha_action(self, data: EventData) -> str:
        return f"{data['endpoint_id']}_{data['command']}"
