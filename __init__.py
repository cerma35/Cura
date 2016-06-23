# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.
from . import NetworkPrinterOutputDevicePlugin
from . import DiscoverUM3Action
from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "plugin": {
            "name": "Wifi connection",
            "author": "Ultimaker",
            "description": catalog.i18nc("Wifi connection", "Wifi connection"),
            "api": 3
        }
    }

def register(app):
    return { "output_device": NetworkPrinterOutputDevicePlugin.NetworkPrinterOutputDevicePlugin(), "machine_action": DiscoverUM3Action.DiscoverUM3Action()}