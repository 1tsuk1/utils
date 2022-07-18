import logging
from pathlib import Path

from utils.dataclass import ExperimentConfig
from utils.file_handling import load_dataclass, save_yaml
from utils.logger import set_logger
from utils.timer import timer

if __name__ == "__main__":

    # -----------実験設定の取得-----------
    config = load_dataclass(ExperimentConfig)

    # 結果の出力先を設定
    root_results = Path(config.root_result_dir + "/" + config.result_dir)
    root_results.mkdir(exist_ok=True, parents=True)

    # 実行時のconfigを保存
    config_output_path = root_results / "config.yaml"
    save_yaml(config, config_output_path)

    # -----------ログの設定-----------

    # ロギングレベルの取得
    logging_level = getattr(logging, config.log_level.upper(), None)
    if not isinstance(logging_level, int):
        raise ValueError("Invalid log level: %s" % config.log_level.upper())

    # ログの出力先の取得
    log_filename = config.log_filename
    log_path = root_results / log_filename

    # ロガーの生成
    logger = set_logger(log_path, logging_level)

    logger.info(f"実験設定 \n : {config}")
    # TODO: ----------------以下はよしなに処理を記述していく--------------

    # ログ例
    logger.info("Log file set to {}".format(log_path))
    logger.info("aaaaaa")
    logger.error("aaaaaa")
    logger.warning("aaaaaa")
    logger.debug("aaaaaa")
    # logger.info('| %11s | %11s | %11s | %11s|' %('surr', 'kl', 'ent', 'vf_loss'))

    with timer("process1", logger):
        a = [i for i in range(10 ** 6)]
