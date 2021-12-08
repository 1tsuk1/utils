from dataclasses import dataclass, field
from typing import List, Tuple, Union

from file_handling import current_time


@dataclass
class DataConfig:
    data_path: str = "./data/test.csv"


@dataclass
class ModelParamConfig:
    objective: str = "regression"
    metric: str = "rmse"
    verbose: int = -1  # 「No further splits with positive gain」を表示しない


@dataclass
class TrainConfig:
    TARGET: str = "classes"
    FEATURES: List[str] = field(
        default_factory=lambda: [
            "feature1",
            "feature2"
            # "feature3",
        ]
    )



@dataclass
class ExperimentConfig:
    data: DataConfig = DataConfig()
    model: ModelParamConfig = ModelParamConfig()
    train: TrainConfig = TrainConfig()

    root_result_dir: str = "results"
    result_dir: str = current_time()
    log_level: str = "INFO"
    log_filename: str = "log.log"


if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path

    from file_handling import load_dataclass, save_yaml

    def current_time():
        """現在時刻を取得"""
        now = datetime.now()
        now_str = datetime.strftime(now, "%Y-%m-%d_%H-%M-%S")
        return now_str

    config = load_dataclass(ExperimentConfig)
    # logger.info(f"実験設定 \n : {config}")

    # 結果の出力先を設定
    root_results = Path(config.result_dir + "/" + current_time())
    root_results.mkdir(exist_ok=True)

    # 実行時のconfigを保存
    config_output_path = root_results / "config.yaml"
    save_yaml(config, config_output_path)
