
import logging
import sys
from logging import getLogger

from termcolor import colored

DATE_FMT = '%m%d %H:%M:%S'

class _MyFormatter(logging.Formatter):
    def format(self, record):
        """
        出力フォーマットやロギングレベルごとの色の設定を行う

        ＜出力例＞
        [1207 15:54:49 @logger.py:87] Log file set to test.log
        [1207 15:54:49 @logger.py:91] aaaaaa
        [1207 15:54:49 @logger.py:92] ERR aaaaaa
        [1207 15:54:49 @logger.py:93] WRN aaaaaa
        [1207 15:55:48 @logger.py:98] DEG aaaaaa
        """

        date = colored('[%(asctime)s @%(filename)s:%(lineno)d]', 'green')
        msg = '%(message)s'

        # ロギングレベルごとの設定
        if record.levelno == logging.WARNING:
            fmt = date + ' ' + colored('WRN', 'yellow', attrs=["underline"]) + ' ' + msg
        elif record.levelno == logging.ERROR or record.levelno == logging.CRITICAL:
            fmt = date + ' ' + colored('ERR', 'red', attrs=['underline']) + ' ' + msg
        elif record.levelno == logging.DEBUG:
            fmt = date + ' ' + colored('DEG', 'green') + ' ' + msg
        else:
            fmt = date + ' ' + msg

        if hasattr(self, '_style'):
            self._style._fmt = fmt
            self._fmt = fmt

        return super(self.__class__, self).format(record)


def set_logger(log_path: str, logging_level: int) -> logging.Logger:
    """
    標準出力、ファイルへの書き込みを行うロガーを設定する

    Args:
        log_path (str):ログの書き込み先
        logging_level (str): ログを出力するレベル（INFO、DEBUG、WARN、ERROR、CRITICAL）を表す整数

    Returns:
        設定したログ
    """
    logger = getLogger(__name__)

    logger.setLevel(logging_level)

    # [ログの出力先①]標準出力
    con_handler = logging.StreamHandler(sys.stdout)
    con_handler.setFormatter(_MyFormatter(datefmt=DATE_FMT))
    logger.addHandler(con_handler)

    # [ログの出力先②]ファイルへの書き出し
    file_handler = logging.FileHandler(filename=log_path, encoding='utf-8', mode='w')
    file_handler.setFormatter(_MyFormatter(datefmt=DATE_FMT))
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":

    import argparse
    from pathlib import Path


    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--log_level", help='set log level',
                            type=str,
                            default="INFO")
        parser.add_argument("--log_path", help='set output log path', type=str,
                            default="log.log")
        return parser.parse_args()

    args = parse_arguments()

    # ロギングレベルの取得
    logging_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(logging_level, int):
        raise ValueError('Invalid log level: %s' % args.log_level.upper())

    # ログの出力先の取得
    log_path = args.log_path

    # 出力先の親ディレクトリまでが存在しなければ生成
    parent_log_path = Path(log_path).parent
    parent_log_path.mkdir(exist_ok=True)

    # ロガーの生成
    logger = set_logger(log_path, logging_level)

    # ログ例
    logger.info('Log file set to {}'.format(log_path))
    logger.info("aaaaaa")
    logger.error("aaaaaa")
    logger.warning("aaaaaa")
    logger.debug("aaaaaa")
    # logger.info('| %11s | %11s | %11s | %11s|' %('surr', 'kl', 'ent', 'vf_loss'))
