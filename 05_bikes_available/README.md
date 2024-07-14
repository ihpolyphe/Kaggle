# bikes_available

## データチェック
`status.csv`に学習データとテストデータが含まれている。学習データは`predict`が0のもの、テストデータは`predict`が1のものになる。
|id|year|month|day|hour|station_id|bikes_available|predict|
|--|--|--|--|--|--|--|--|
|8761|2014|9|1|1|0||1|
|10031|2014|10|23|23|0||0|


「予測対象日の翌日（24時間分）の台数状況は欠損値となっています。」ということなので`predict`が0のものも存在する。
答えがわからず学習データとしては使用できないので、学習データからは除外しておく必要がある。

テストデータ2014/9~2015/8

# 公式情報
https://signate.jp/competitions/567/data
データ説明
自転車の台数状況データ（status.csv）
説明　　　： 各サイクルステーションで1時間ごとに記録された利用可能な自転車数（目的変数）の履歴データです。
レコード数： 1,226,400
カラム	ヘッダ名称	データ型	説明
0	id	int	インデックスとして使用
1	year	int	記録日時（年）
2	month	int	記録日時（月）
3	day	int	記録日時（日）
4	hour	int	記録日時（時）
5	station_id	int	ステーションID
6	bikes_available	int	利用可能な自転車数（台数）
7	predict	int	予測対象フラグ（0=予測対象外, 1=予測対象）
※黄色く色付けされた変数が目的変数です（カラム「predict」に1が記載されている行の「bikes_available」が予測対象です）


利用者の移動履歴データ（trip.csv）
説明　　　： 利用者がシェアサイクルで移動した時間、起点駅、終点駅等を記録した移動履歴データです。
レコード数： 669,959
カラム	ヘッダ名称	データ型	説明
0	trip_id	int	移動履歴ID
1	duration	int	移動時間（秒）
2	start_date	char	移動を開始した日時
3	start_station_id	int	移動を開始したステーションID
4	end_date	char	移動を終了した日時
5	end_station_id	int	移動を終了したステーションID
6	bike_id	int	利用された自転車ID
7	subscription_type	char	利用者の登録種別（Customer=一時利用者, Subscriber=定額プラン利用者）

ステーション情報（station.csv）
説明　　　： サイクルステーションの緯度・経度、ドック数（最大で停められる自転車数）、設置日のデータです。
レコード数： 70
カラム	ヘッダ名称	データ型	説明
0	station_id	int	ステーションID
1	lat	float	ステーション設置場所の緯度
2	long	float	ステーション設置場所の経度
3	dock_count	int	ドック数（最大で停められる自転車数）
4	city	char	ステーションが設置されている都市（具体的な都市名は非開示）
5	installation_date	char	ステーションが設置された日時

気象情報（weather.csv）
説明　　　：都市中心部における1日ごとの気象予報データです。※0時時点の予報データ
レコード数：730

カラム	ヘッダ名称	データ型	説明
0	date
char
記録日（時間情報は付与されていませんが、0時時点の予報データとなります）
1	max_temperature
int
最高気温（単位: 華氏）
2	mean_temperature
int
平均気温（単位: 華氏）
3	min_temperature
int	最低気温（単位: 華氏）
4	max_dew_point
int
最高露点温度（単位: 華氏）
5	mean_dew_point
int
平均露点温度（単位: 華氏）
6	min_dew_point
int	最低露点温度（単位: 華氏）
7	max_humidity
int
最大湿度
8	mean_humidity
int
平均湿度
9	min_humidity
int	最小湿度
10	max_sea_level_pressure
float
最大海面気圧
11	mean_sea_level_pressure
float
平均海面気圧
12	min_sea_level_pressure
float	最小海面気圧
13	max_visibility
int
最大視程（単位: mile）
14	mean_visibility
int
平均視程（単位: mile）
15	min_visibility
int	最小視程（単位: mile）
16	max_wind_Speed
int
最大風速（単位: mph）
17	mean_wind_speed
int
平均風速（単位: mph）
18	precipitation
float
降水量（単位: inch）
19	cloud_cover
int	雲量
20	events
char
予報された気象現象
21	wind_dir_degrees
int	平均風向
応募用サンプルファイル（sample_submit.csv）
説明　　　：予測結果の投稿用に、自転車の台数状況データ（status.csv）の"predict"列に1が記載された行のidと、すべて一律の値で予測した結果を記載したデータです。
カラム	ヘッダ名称	データ型	説明
0	無し	int	インデックスとして使用
1	無し	float	予測した自転車数（※整数値である必要はありません）

投稿方法
1列目に、自転車の台数状況データ（status.csv）の"predict"列に1が記載された行のidを、2列目にその"id"に対応する予測結果（予測した自転車台数の数値）を記入したファイルを、ヘッダ無しのcsv形式で投稿ください。

## 予測対象
予測対象日、予測対象時間のイメージ
・自転車の台数状況データ（status.csv）には、2013年9月～2015年8月まで（2年分）の予測対象日時と予測対象外となる日時の両方の台数状況が記録されています。
・予測対象となるのは、2014年9月～2015年8月までの1年分の期間で各月から10日ずつ選ばれた予測対象日の「1時～23時（1時間ごと）」の自転車台数です。
・予測対象日の0時は予測対象外であり、0時時点の台数は開示されています。
・また、予測対象日の翌日（24時間分）の台数状況は欠損値となっています。