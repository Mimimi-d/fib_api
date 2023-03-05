# 概要
指定したn番目のフィボナッチ数を返すREST APIです。

### エンドポイント
<http://yutaokazima.pythonanywhere.com/fib>

# ソースコードの構成

fib_api
├ app.py   # フィボナッチ数を返すFlaskのコード
└ unit_test.py # ユニットテスト用のコード

# 使い方

- リクエスト例
  例えば、99番目ののフィボナッチ数を取得するには、以下のように実行します。
    <http://yutaokazima.pythonanywhere.com/fib?n=99>
- レスポンス例

```json
{"result":218922995834555169026}
```

### curlコマンド実行例

```
curl -X GET -H "Content-Type: application/json" "http://yutaokazima.pythonanywhere.com/fib?n=99"   
{"result":218922995834555169026}
```

# 仕様

### 成功時

ステータスコード: 200
レスポンス:

```json
{"result": "<番目のフィボナッチ数列の数字>"}
```

### エラー事例

ステータスコード: 400
レスポンス:
- nが指定されていない時
```json
{
  "status": 400,
  "message": "n is required"
}
```
- nが範囲外の時(文字列やマイナスなど)

```json
{
  "status": 400,
  "message": "n = <n>. n must be a positive integer"
}
```

### メソッドエラー事例
ステータスコード: 405
レスポンス:
```json
{
  "status": 405,
  "message": "Method (<method>) Not Allowed"
}
```

### エンドポイント外のリクエストについて
ステータスコード: 404
レスポンス:
```json
{
  "status": 404,
  "message": "Not Found."
}
```

# ユニットテストについて
pytest モジュールを使用して、アプリケーションの /fib エンドポイントに対して、異なるパラメータを渡した場合の結果をテストしています。


`test_fib`: 正しいパラメータ（99）を渡した場合のFibonacci数列のテストを行います。  
`test_fib_missing_parameter`: リクエストにパラメータが含まれていない場合のエラーをテストします。  
`test_fib_invalid_string_parameter`: リクエストで文字列が含まれている場合のエラーをテストします。  
`test_fib_invalid_negative_parameter`: リクエストで負の数が含まれている場合のエラーをテストします。  
`test_fib_invalid_float_parameter`: リクエストで小数が含まれている場合のエラーをテストします。  
`test_fib_method_not_allowed`: GET以外のHTTPメソッドが使用された場合のエラーをテストします。  
`test_unknown_route`: 存在しないエンドポイントへのリクエストがあった場合のエラーをテストします。  
