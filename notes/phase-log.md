# Phase Log

このファイルに進捗を記録する。

## プロジェクト概要
Raspberry Pi 5 を使って小さなホームラボを構築しながら、Linux、ネットワーク、DNS、Web、監視、セキュリティを学ぶプロジェクト。

## 現在までにやったこと

### Raspberry Pi セットアップ　
- Raspberry Pi 5 を用意した
- Raspberry Pi OS を起動した
- 有線LANで接続した
- SSH で接続できるようにした
- Pironman 5 Max を動作させた

### リモートアクセス 2026/3/11
- Tailscale を導入した
- Tailscale のIPを確認した
- 外部から SSH 接続できることを確認した

### GitHub
- GitHub アカウントを用意した
- `raspi-home-lab` リポジトリを作成した
- 最小ディレクトリ構成を作成した

## 理解したこと
- Raspberry Pi はこのプロジェクト全体の土台になる
- SSH を使うことで GUI なしでも遠隔操作できる
- Tailscale を使うことで安全寄りに外部から接続できる
- GitHub はコード置き場だけでなく、学習記録と成果物の置き場でもある

## 次にやること
- GitHub の README を整える
- Phase 3 に向けてネットワーク理解を進める
- `ip a`, `ip r`, `ss`, `ping`, `dig` などを触る
- 小さな Python スクリプトを作り始める
