from enum import Enum


class AssetCriticality(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"


class AssetStatus(str, Enum):
    online = "online"
    offline = "offline"
    maintenance = "maintenance"


class AssetEnvironment(str, Enum):
    production = "production"
    development = "development"
    testing = "testing"


class AssetType(str, Enum):
    server = "server"
    workstation = "workstation"
    laptop = "laptop"
    network_device = "network_device"
    database = "database"
    firewall = "firewall"
    application = "application"