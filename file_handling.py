from datetime import datetime
from pathlib import PosixPath
from typing import Union

from omegaconf import DictConfig, ListConfig, OmegaConf


def current_time():
    """Get current time as strings format in the system's time zone."""
    now = datetime.now()
    now_str = datetime.strftime(now, "%Y-%m-%d_%H-%M-%S")
    return now_str

def load_dataclass(dataclass) -> Union[DictConfig, ListConfig]:
    base_config = OmegaConf.structured(dataclass)
    cli_config = OmegaConf.from_cli()
    config = OmegaConf.merge(base_config, cli_config)

    return config


def load_yaml(YAML_PATH: PosixPath) -> Union[DictConfig, ListConfig]:
    """Load yaml file"""
    config = OmegaConf.load(YAML_PATH)
    return config


def save_yaml(config: dict, OUTPUT_PATH: PosixPath) -> None:
    """Save yaml file"""
    OmegaConf.save(config=config, f=OUTPUT_PATH)
