## 実装内容

- ロギングレベルに合わせた出力色の変更
- dataclassによる設定管理
- コマンドラインでの設定変更
- configの保存
- ログの保存

## 導入方法

1. `git clone https://github.com/1tsuk1/utils` でこのリポジトリをクローン


## 環境構築


### pipenv 
```
pipenv sync
```


### docker
1. デスクトップ用のdockerアプリをinstall
3. 2のアプリを起動
4. `docker compose up -d --build` を実行して、コンテナを作成
5. `docker compose exec python3 zsh` でコンテナへ接続


## 実装
6. main.pyで不必要な部分を削除して、よしなに実装
7. ライブラリのインストールが必要であれば、`pipenv install hogehoge` で追加
8. dataclass.pyで、開発環境に見合った設定を行う
9.  ログを活用しながら、よしなにコーディング

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