# Name（classifier）
 
CNNを使った画像分類機
 
# DEMO
 

 
# Features
 

 
# Requirement
 
## scraping.py
python==3.7.7
urllib3==1.25.9
beautifulsoup4==4.9.0
flickrapi==2.4.0
 
## run.py

# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明する
 
```terminal
pip install -r requirements.txt
```
 
# Usage
 

 
```bash
git clone https://github.com/fumitrial8/classifier.git
cd classifier
mkdir data
```
credential.pyファイルを作成し、そこにKEYとSECRETを記述

## scraping.py
```terminal
# python3 scraping.py 取得したい画像 取得数
python3 scraping.py elephant 200
```
 
# Author
* fumitrial8