# ru-mobile-whitelist-srs

Автособираемые `.srs` rule-set'ы для [sing-box](https://sing-box.sagernet.org/) на основе
[hxehex/russia-mobile-internet-whitelist](https://github.com/hxehex/russia-mobile-internet-whitelist).

GitHub Actions раз в день (06:00 UTC) проверяет апстрим. Если списки изменились —
автоматически собирает новые `.srs` и публикует их в [Releases](../../releases)
(а так же raw JSON, из которых эти .srs скомпилированы).

Можно также запустить сборку руками: Actions → Sync upstream and build sing-box rule-sets → Run workflow.

## Файлы в каждом релизе

- `ru-whitelist-domains.srs` — домены (SNI) из `whitelist.txt`
- `ru-whitelist-ips.srs` — IP/CIDR из `ipwhitelist.txt` + `cidrwhitelist.txt`
- `*.json` — несжатые версии тех же rule-set'ов (для дебага)

## Использование в sing-box

Скачать конкретный релиз и указать как `local` rule-set:

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "ru-whitelist-domains",
        "type": "local",
        "format": "binary",
        "path": "ru-whitelist-domains.srs"
      },
      {
        "tag": "ru-whitelist-ips",
        "type": "local",
        "format": "binary",
        "path": "ru-whitelist-ips.srs"
      }
    ]
  }
}
```

Либо как `remote` rule-set прямо по ссылке на последний релиз (sing-box сам скачает и закэширует):

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "ru-whitelist-domains",
        "type": "remote",
        "format": "binary",
        "url": "https://github.com/<your-username>/<your-repo>/releases/latest/download/ru-whitelist-domains.srs",
        "update_interval": "24h"
      },
      {
        "tag": "ru-whitelist-ips",
        "type": "remote",
        "format": "binary",
        "url": "https://github.com/<your-username>/<your-repo>/releases/latest/download/ru-whitelist-ips.srs",
        "update_interval": "24h"
      }
    ]
  }
}
```

С `remote` + `update_interval: 24h` тебе вообще не придётся руками что-то перекачивать —
sing-box сам подтянет новую версию при каждом обновлении.

## Лицензия

Списки доменов/IP принадлежат [hxehex/russia-mobile-internet-whitelist](https://github.com/hxehex/russia-mobile-internet-whitelist)
(MIT). Этот репозиторий только автоматизирует их конвертацию в формат sing-box.
