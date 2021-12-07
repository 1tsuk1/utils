

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
```