import os
import sys
import time
import urllib
from bs4 import BeautifulSoup
from flickrapi import FlickrAPI
from credential import KEY, SECRET

# 待ち時間を設定して、アクセス過多を防ぐ
waiting_time = 1

# python scraping.py {{ダウンロードしたい画像の名前をnameに格納}}
name = sys.argv[1]
amount = int(sys.argv[2])

# nameディレクトリを作成
save_dir = './data/' + name
os.makedirs(save_dir, exist_ok=True)

# flickr clientを作成、画像をダウンロードするためには、urlが必要
flickr = FlickrAPI(KEY, SECRET, format='parsed-json')

# 検索結果
result = flickr.photos.search(
    # 検索キーワード
    text = name,
    # 取得するデータ件数
    per_page = amount,
    # 検索するデータの種類(ここでは、写真)
    media = 'photos',
    # データの並び順(関連順)
    sort = 'relevance',
    # UI コンテンツを表示しない
    safe_search = 1,
    # 取得したいオプションの値(url_q->画像のアドレスが入っている情報、licence -> ライセンス情報)
    extras = 'url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = save_dir + '/' + str(i).zfill(5) + '.jpg'
    if os.path.exists(filepath): continue
    urllib.request.urlretrieve(url_q, filepath)
    time.sleep(waiting_time)