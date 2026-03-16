# Raspberry Pi 5 Home Lab

## Overview
このプロジェクトは、Raspberry Pi 5 を用いて小さなインフラを実際に構築しながら、Linuxサーバー運用、ネットワーク、DNS、Web、監視、セキュリティ、Python/SQL/Web技術を学ぶ個人プロジェクトである。

最終的には Raspberry Pi 上に  
Hardware → OS → Network → DNS → Web Server → Application → Database → Monitoring → Security  
の層を持つ小さなホームラボ環境を作ることを目指す。

## Goals
このプロジェクトで主に扱う対象は以下である。

- Linux
- Networking
- DNS
- HTTP / Web infrastructure
- Monitoring
- Security
- Python API
- SQL
- Web UI
- インフラの中で言語を使う感覚

## Project Policy
このプロジェクトでは「実装しながら理解する」を基本方針とする。

実装 → 疑問が出る → 調べる → 理解する

ただし、内容理解ゼロで先に進まないこと、最初から完全理解を求めすぎないことを重視する。  
目標は「最低限説明できる理解」を持って前進すること。

また、まずは最小構成で全体像を通し、その後で理解や構成を深める進め方を取る。

## Phase Structure
- Phase 1: Linux基盤
- Phase 2: リモートアクセス
- Phase 3: ネットワーク理解
- Phase 4: DNS
- Phase 5: Webサーバー
- Phase 6: 実用品の最小版構築
- Phase 7: Monitoring
- Phase 8: 外部公開

## Repository Structure
- `notes/phase-1-linux/`
- `notes/phase-2-remote-access/`
- `notes/phase-3-network/`
- `notes/phase-4-dns/`
- `scripts/python/`
- `app/learning-log/`
- `infra/`
- `assets/screenshots/`

## Notes Policy
作業記録は phase ごとにディレクトリを分け、日付ベースの個別ファイルとして追加する。  
ファイル名は日付のみとし、例として `2026-03-12.md` のようにする。  
大きなログファイルを逐次更新するより、新しい記録を追加していく運用を優先する。

## Output Policy
このリポジトリでは、コードだけでなく、学習記録、実装記録、設定例、試行錯誤の記録も含めて整理して残す。  
各フェーズで、小さくても動く成果物を残すことを重視する。
