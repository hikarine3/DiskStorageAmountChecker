# DiskStorageAmountChecker
## What is this script? (このスクリプトは何ですか?)
This script check disk storage's available amount of specified servers and send alerting message by email if necessary.

このスクリプトは、指定した複数のサーバーのディスクの利用可能な容量を確認し、指定した利用率を上回るディスクがあれば、警告のメッセージを指定したメールアドレスに送るスクリプトです。

![スクリーンショット-2021-10-22-21-05-44-1- (1)](https://user-images.githubusercontent.com/197538/138454771-67bd1dff-2a16-4399-b4f7-9cd299326581.png)

## Necessary step 1 before you use this script (このスクリプトを使う前の準備1)
```
pip3 install firstclass_dotenv;
```

## Necessary step 2 before you use this script (このスクリプトを使う前の準備2)
If you want to get alert through email, you have to configure .env file to set up smtp's usage.

Please set values for using your smtp server in .env.

メール機能も使ってこのスクリプトを利用するには、.envの編集が必要です。

貴方が利用可能なAWS・SendgridやGmail等のSMTPサーバの該当情報を入力して下さい。

Example of .env (.envの例)
```
MAIL_DRIVER=smtp
MAIL_HOST=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USERNAME=apikey
MAIL_PASSWORD=Example........
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=example@example.com
```

## Command example (コマンド例)
### Check available disk amount with email function


```
python3 DiskStorageAmountChecker.py --email=aaa@example.com --servers=server1,server2 --alert=70 --user=ssh_user_id --env_file=../config/.env
```

#### Mandatory parameters (必須の引数)

##### --servers=
servers to be checked. You can specify multiple servers with ",".

チェックするサーバー名/パスワード無しでsshでログイン出来る事が必須。カンマ区切りで複数指定可能

##### --user=...
user id which will be used for ssh login

sshログインに使うユーザーID

#### Optional parameters (オプション項目)

##### --alert=...
If used disk amount's percentage is above this, you will get alert. If you don't specify, 50% will be used.

もしも使用ディスク割合がこのパーセンテージを超えていれば、警告が出ます。指定しなければ50%が使われます。

##### --email=...
Mail address to which alert will be sent.

警告が送られるメールアドレス

##### --env_file=...
If you use .env which is not under execution directory, please specify the path to .env.

実行ディレクトリの.env以外を使う場合には、.envの場所を指定して下さい。

# License / ライセンス / 执照

MIT

# Author / 作者

## Name / 名前 / 全名
Hajime Kurita

## Twitter
- EN: https://twitter.com/hajimekurita
- JP: https://twitter.com/hikarine3

## Technical web services / 提供してる技術関連Webサービス / 技术网络服务
### VPS & Infra comparison / VPS比較 / VPS比较
- EN: https://vpsranking.com/en/
- CN: https://vpsranking.com/zh/
- JP: https://vpshikaku.com/

### Programming Language Comparison / プログラミング言語比較 / 编程语言比较
- EN: https://programminglang.com/en/
- CN: https://programminglang.com/zh/
- JP: https://programminglang.com/ja/

### OSS
- Docker: https://hub.docker.com/u/1stclass/
- Github: https://github.com/hikarine3
- NPM: https://www.npmjs.com/~hikarine3
- Perl: http://search.cpan.org/~hikarine/
- PHP: https://packagist.org/packages/hikarine3/
- Python: https://pypi.org/user/hikarine3/
