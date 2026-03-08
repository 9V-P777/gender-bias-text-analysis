# gender-bias-text-analysis
Analysis of Gender Gap in Japan's Physics/STEM Fields using NLP and Text Mining
＃＃＃〜エコーチェンバー現象を考慮した言説の共起構造分析〜

＃＃🌟 プロジェクト概要
日本のSTEM分野（物理学・数学・工学等）における女性比率の低さを打破するため、過去20年間の支援策が世論にどのような影響を与えたかを分析した研究リポジトリです。
2003年から2023年までのネット上の書き込みや専門家の言説を対象に、自然言語処理（NLP）を用いてジェンダーバイアスの変遷を可視化しました。

> **Note**: 本研究は「自由すぎる研究エキスポ」にて一次審査を通過した内容をベースに、Pythonを用いたデータサイエンスの手法を取り入れてさらに発展させたものです。（※最終審査向けの動画は、実装と分析に没頭するあまり送り忘れて辞退となってしまいましたが、内容はさらに磨きをかけています！）

＃＃🧪 分析の核心：データの信頼性と客観性の担保
ネット上の匿名データには、特定の過激な意見が増幅される「エコーチェンバー現象」が含まれがちです。本研究では、単なるテキストマイニングに留まらず、以下の高度なデータクレンジングを実施しました。

### 1. 主観性スコアリングによるフィルタリング（TextBlob）
Pythonライブラリ **TextBlob** を活用し、各文章の「主観性（Subjectivity）」を数値化しました。
- **指標**: `subjectivity`（0.0: 客観的 〜 1.0: 主観的）
- **課題**: 感情的で極端な意見が分析結果を歪める可能性。
- **解決策**: 主観性スコアに基づき、`subjectivity > 0.8`（極端に主観的な意見）を統計的に除外。これにより、一時的な感情に左右されない「冷静な世論」を抽出しました。
- 

### 2. 形態素解析とカスタム辞書（Janome）
**Janome** を用いて独自のカスタム辞書を作成し、表記揺れの統一（例：「リケジョ」→「女性」）や分析ノイズの除去を行い、共起関係の精度を向上させました。

### 3. 感情極性（Polarity）による意識分析
TextBlob の polarity スコア（-1.0: ネガティブ 〜 1.0: ポジティブ）を用いて、言説の背後にある感情の傾向を分析しました。

## 📊 主要な分析結果

### 1. 2021年を境とした意識の変容
データを「2021年以前」と「2021年以降」に分けて分析した結果、明確な変化が見られました。
- **2021年以前**: 感情極性の分布に「負の歪み（ネガティブな偏り）」が強く、ステレオタイプに基づく否定的な反応が目立ちました。
- **2021年以降**: 分布の中央値がプラス側にシフト。支援策の浸透により、STEM進出を前向きに捉える「期待感」が可視化されました。

### 2. 心理的障壁から構造的障壁へ
クレンジング後のデータにより、課題の質的な変化が浮き彫りになりました。
- **過去**: 「性別による能力差」といった**心理的な固定観念**が主な障壁。
- **現在**: 心理的障壁が緩和された一方、「待遇差」や「キャリア形成の不安」といった**社会構造的・物理的な障害**が、次の解決すべき課題として明確に可視化されました。
  
各文章の「感情極性（Polarity）」の数値化↓
<img width="1132" height="589" alt="image" src="https://github.com/user-attachments/assets/2d94add1-d3ae-4990-870b-6ed3c318e946" />
<img width="1145" height="600" alt="image" src="https://github.com/user-attachments/assets/518a8881-ba47-430e-82da-dc8bc3c8b92b" />
各文章の「主観性（Subjectivity）」の数値化↓
<img width="1212" height="704" alt="image" src="https://github.com/user-attachments/assets/1c283658-cd9d-482a-ab4b-91bfd13e0b08" />
<img width="1094" height="709" alt="image" src="https://github.com/user-attachments/assets/b3e25298-b8ff-4419-ad7c-af0e78bef7bf" />
上記二つを踏まえてデータクレンジングする前後のテキストマイニングのデータ↓
<img width="448" height="286" alt="image" src="https://github.com/user-attachments/assets/7abfbaf1-5d01-4d50-9eb4-93d502356dcf" />
<img width="448" height="315" alt="image" src="https://github.com/user-attachments/assets/bcc596b0-b683-4075-9547-4f48079072c2" />

🚀 技術スタック
Language: Python 3.11

NLP: TextBlob (Polarity＆Subjectivity Analysis), Janome (Morphological Analysis)

Visualization: User Local AI Text Mining (Word Clouds, Co-occurrence Networks)

## 💻 核心アルゴリズム（Python抜粋）
主観性を排除し、データの信頼性を高めるためのフィルタリングコードです。

```python
from textblob import TextBlob

# 分析対象のテキストに対して主観性をチェック
blob = TextBlob(text)
# スコアが0.8未満（客観性が高い）ものだけを分析に採用
if blob.sentiment.subjectivity < 0.8:
    process_analysis(text)

```
🌐 English Summary

This project investigates the gender gap in Japan's STEM fields using NLP. By implementing a filtering process based on TextBlob subjectivity scores, this study successfully mitigates the "Echo Chamber" effect in online discourse. Findings suggest a transition from psychological stereotypes to structural/systemic challenges in gender representation.

💡 執筆者より

このリポジトリは、社会課題に対してデータサイエンスがどう貢献できるかを探求したものです。もし内容に興味を持っていただけたら、ぜひStarやフィードバックをお願いします。
