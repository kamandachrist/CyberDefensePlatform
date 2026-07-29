from enum import Enum


class AssetCriticality(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AssetStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"


class AssetEnvironment(str, Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"


class AssetType(str, Enum):
    SERVER = "server"
    WORKSTATION = "workstation"
    LAPTOP = "laptop"
    NETWORK_DEVICE = "network_device"
    DATABASE = "database"
    FIREWALL = "firewall"
    APPLICATION = "application"