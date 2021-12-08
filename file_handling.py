from datetime import datetime
from pathlib import PosixPath
from typing import Union

from omegaconf import DictConfig, ListConfig, OmegaConf


def current_time():
    """現在時刻を取得"""
    now = datetime.now()
    now_str = datetime.strftime(now, "%Y-%m-%d_%H-%M-%S")
    return now_str

def load_dataclass(dataclass) -> Union[DictConfig, ListConfig]:
    base_config = OmegaConf.structured(dataclass)
    cli_config = OmegaConf.from_cli()
    config = OmegaConf.merge(base_config, cli_config)

    return config


def load_yaml(YAML_PATH: PosixPath) -> Union[DictConfig, ListConfig]:
    """yamlファイルを読み込む"""
    config = OmegaConf.load(YAML_PATH)
    return config


def save_yaml(config: dict, OUTPUT_PATH: PosixPath) -> None:
    """yamlファイルを保存する"""
    OmegaConf.save(config=config, f=OUTPUT_PATH)
