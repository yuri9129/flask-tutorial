# 環境構築

PowerShellの場合
```
pip install Flaks=2.2.5
$env:FLASK_APP = "hello"
$env:FLASK_ENV = "development"
```

bashの場合
```
export FLASK_APP=hello
export FLASK_ENV=development
```

# 実行
```
flask run
```

# 参考ドキュメント
https://flask.palletsprojects.com/en/2.0.x/