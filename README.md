# DiskStorageAmountChecker
## English
This script check disk storage's available amount of specified servers and send alerting message by email if necessary.

For it, you have to configure .env file to set up smtp's usage.

## 日本語
このスクリプトは、指定した複数のサーバーのディスクの利用可能な容量を確認し、指定した利用率を上回るディスクがあれば、警告のメッセージを指定したメールアドレスに送るスクリプトです。

メール機能も使ってこのスクリプトを利用するには、.envの編集が必要です。

AWS・SendgridやGmail等のSMTPサーバの該当情報を入力して下さい。

.envの例
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

--servers=... <= servers to be checked (チェックするサーバー名/パスワード無しでsshでログイン出来る事が必須)

--user=... <= user id which will be used for ssh login (sshログインに使うユーザーID)

#### Optional parameters (オプション項目)

--alert=... <= If rused disk amount's percentage is above this, you will get alert.

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
