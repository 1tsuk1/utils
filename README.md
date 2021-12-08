## 実装内容

- ロギングレベルに合わせた出力色の変更
- dataclassによる設定管理
- コマンドラインでの設定変更
- configの保存
- ログの保存

## 導入方法

1. main.pyで不必要な部分を削除
2. dataclass.pyで、開発環境に見合った設定を行う
3. ログを活用しながら、よしなにコーディング

## Q&A


### 実験結果のディレクトリ名を変更したい

```
#experimentへ変更（デフォルトは日時。ex. 2021-12-08_10-55-34）
python example_main.py --result_dir experiment
```


### ログを表示するレベルを変更したい

```
#DEBUGへの変更（デフォルトはINFO）
python example_main.py --log_level debug
```

### ログファイル名を変更したい

```
#log_pathで指定する
python example_main.py --log_path log.log

#複数のディレクトリを跨いでもok
python example_main.py --log_path ./log/log2/log.log

<!-- 

## logger

### 導入したい

1. _MyFormatter、set_loggerを導入
2. 「if __name__ == "__main__":」以下をコピペ
3. logger.info系を削除し、それらを参考に任意の場所にログを設定する

### ログを表示するレベルを変更したい

```
#DEBUGへの変更（デフォルトはINFO）
python logger.py --log_level debug
```

### 出力ファイルのパスを変更したい

```
#log_pathで指定する
python logger.py --log_path ./log/log.log

#複数のディレクトリを跨いでもok
python logger.py --log_path ./log/log2/log.log
``` -->