from dataclasses import dataclass, field
from typing import List, Tuple, Union

from file_handling import current_time


@dataclass
class DataConfig:
    actual_buttan_path: str = "./data/my_preprocessed/actual_buttan.csv"
    actual_num_tokusya_path: str = "./data/my_preprocessed/model_num_tokusya.csv"
    temperature_path: str = "./data/my_preprocessed/temperature.csv"


@dataclass
class ModelParamConfig:
    objective: str = "regression"
    metric: str = "rmse"
    verbose: int = -1  # 「No further splits with positive gain」を表示しない


@dataclass
class TrainConfig:
    TARGET: str = "num_tokusya"
    FEATURES: List[str] = field(
        default_factory=lambda: [
            "actual_buttan",
            "temperature"
            # "actual_buttan_b1",
        ]
    )


@dataclass
class DateConfig:
    VARIFY_EXEC_DATE: str = "2021-04-29"
    pred_exec_date: str = "2021-06-03"
    PASS_DAY_TO_START: int = 4  # 木曜日から月曜日までの経過日数は4日
    PASS_DAY_TO_END: int = 9  # 木曜日から土曜日までの経過日数は9日


@dataclass
class ExperimentConfig:
    data: DataConfig = DataConfig()
    model: ModelParamConfig = ModelParamConfig()
    train: TrainConfig = TrainConfig()
    date: DateConfig = DateConfig()

    root_result_dir: str = "results"
    result_dir: str = current_time()
    log_level: str = "INFO"
    log_filename: str = "log.log"


if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path

    from file_handling import load_dataclass, save_yaml

    def current_time():
        """Get current time as strings format in the system's time zone."""
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
