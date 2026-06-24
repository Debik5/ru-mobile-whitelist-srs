#!/usr/bin/env python3
"""
Собирает rule-set JSON (sing-box формат) из исходных txt-списков
репозитория hxehex/russia-mobile-internet-whitelist.

Вход:  src/whitelist.txt, src/ipwhitelist.txt, src/cidrwhitelist.txt
Выход: dist/ru-whitelist-domains.json, dist/ru-whitelist-ips.json
"""
import json
import os

SRC = "src"
DIST = "dist"
os.makedirs(DIST, exist_ok=True)


def read_lines(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() and not l.startswith("#")]


def build_domains():
    domains = read_lines(os.path.join(SRC, "whitelist.txt"))
    rs = {"version": 1, "rules": [{"domain_suffix": domains}]}
    out_path = os.path.join(DIST, "ru-whitelist-domains.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rs, f, indent=2, ensure_ascii=False)
    print(f"domains: {len(domains)} -> {out_path}")


def build_ips():
    cidrs = []
    for fname in ("ipwhitelist.txt", "cidrwhitelist.txt"):
        for line in read_lines(os.path.join(SRC, fname)):
            cidrs.append(line if "/" in line else line + "/32")
    cidrs = sorted(set(cidrs))
    rs = {"version": 1, "rules": [{"ip_cidr": cidrs}]}
    out_path = os.path.join(DIST, "ru-whitelist-ips.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rs, f, indent=2, ensure_ascii=False)
    print(f"ip/cidr: {len(cidrs)} -> {out_path}")


if __name__ == "__main__":
    build_domains()
    build_ips()
