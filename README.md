## 実装内容

- ロギングレベルに合わせた出力色の変更
- dataclassによる設定管理
- コマンドラインでの設定変更
- configの保存
- ログの保存

## 導入方法

1. `git clone [https://github.com/1tsuk1/utils](https://github.com/1tsuk1/utils)` でこのリポジトリをクローン
2. `pipenv sync` で仮想環境を構築する
   1. 必要があれば、Pipfileのpythonのバージョンを変更する
3. main.pyで不必要な部分を削除して、よしなに実装
4. ライブラリのインストールが必要であれば、`pipenv install hogehoge` で追加
5. dataclass.pyで、開発環境に見合った設定を行う
6. ログを活用しながら、よしなにコーディング

## Q&A


### 実験結果のディレクトリ名を変更したい

```
#experimentへ変更（デフォルトは日時。ex. 2021-12-08_10-55-34）
python main.py --result_dir experiment
```


### ログを表示するレベルを変更したい

```
#DEBUGへの変更（デフォルトはINFO）
python main.py --log_level debug
```

### ログファイル名を変更したい

```
#log_pathで指定する
python main.py --log_path log.log
```