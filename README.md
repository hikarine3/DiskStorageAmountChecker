# DiskStorageAmountChecker
This script heck disk storage's amount of specified servers and send alerting message by email if necessary.

For it, you have to configure .env file to set up smtp's usage.

Command example
```
python3 DiskStorageAmountChecker.py --email=aaa@example.com --servers=server1,server2 --alert=70 --user=ssh_user_id
```

If you want to check only disk which is near disk full through shell command,

```
#!/bin/sh
user=UserId; # please change
alert_per=75; # please adjust
servers=('server1' 'server2') # please change
for server in ${servers[@]}
do
        ssh -l $user $server 'df -kh' | perl -e 'while(<>){$_=~ s{(\d+)\%}{if($1>='$alert_per'){print("'$server'"."\t".$_);}}e;}'
done
```
is enough


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
