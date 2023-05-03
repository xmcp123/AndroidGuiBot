__version__ = "0.10"

from androidguibot.controllers import ADBAndroidController, EmulatorController

class AndroidGuiBot(object):
    def __init__(
        self,
        adb_ip=None,
        adb_port=None,
        use_adb=False,
        adb_click=None,
        adb_screenshot=None,
    ):
        self.use_adb = use_adb
        # if use_adb is true, screenshot using ADB unless told otherwise
        self.adb_screenshot = (
            True if self.use_adb and adb_screenshot is None else adb_screenshot
        )
        # if use_adb is true, click using ADB unless told otherwise
        self.adb_click = True if self.use_adb and adb_click is None else adb_click
        self.controller = (
            ADBAndroidController(adb_ip, adb_port)
            if self.use_adb
            else EmulatorController()
        )
        self.__getattr_orig__ = self.__getattr__
    def get_controller(self):
        return self.controller
    def __getattr__(self, item):
        """
        Forward all function calls to the relevant controller
        :param item: Attribute name
        :return: Attribute
        """
        if hasattr(self.controller, item):
            return self.controller.__getattribute__(item)
        else:
            return self.__getattr_orig__(item)
