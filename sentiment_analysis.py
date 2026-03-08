###Add sentiment analysis script（分析用メインコードの追加）
from textblob import TextBlob
from janome.tokenfilter import TokenFilter
# 分析したいテキスト
text = "I love you"
 
# TextBlobオブジェクトを作成
blob = TextBlob(text)
 
# 感情分析を実行
sentiment = blob.sentiment
 
# 結果を表示
print("感情の極性: {sentiment.polarity}, 感情の主観性: {sentiment.subjectivity}")
