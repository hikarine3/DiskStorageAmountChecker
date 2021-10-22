# DiskStorageAmountChecker
## English
This script check disk storage's available amount of specified servers and send alerting message by email if necessary.

For it, you have to configure .env file to set up smtp's usage.

## 日本語
このスクリプトは、指定した複数のサーバーのディスクの利用可能な容量を確認し、指定した利用率を上回るディスクがあれば、警告のメッセージを指定したメールアドレスに送るスクリプトです。

メール昨日も使ってこのスクリプトを利用するには、.envの編集が必要です。

Command example (コマンド例)
```
python3 DiskStorageAmountChecker.py --email=aaa@example.com --servers=server1,server2 --alert=70 --user=ssh_user_id
```

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
