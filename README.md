# 1. Structure of Directory
Pandas_refactoring    
│    
├─__pycache__    
│    
├─refactoring    
│  ├─__pycache__    
│  ├─.mypy_cache    
│  ├─data    
│  │  ├─climate_precip.csv    
│  │  ├─climate_temp.csv
│  │  └─output.csv    
│  │
│  ├─main.py    
│  ├─preprocessing.py    
│  ├─computation.py    
│  └─output.py    
│    
├─test    
│  ├─__pycache__    
│  ├─.pytest_cache    
│  ├─test_data    
│  │  └─test.csv    
│  ├─test_preprocessing.py    
│  ├─test_computation.py    
│  └─test_output.py    
│    
├─pyprogect.poml     
└─poetry.lock    


# 2. Refactoring Process
## Step1　環境構築
Poetry環境がなかったため環境構築から行った。Conda上にpoetryの環境を構築。また必要に応じてパッケージのアップ・ダウングレードなどを行った。
## Step2 Blackでコードの整理
refactoringを行う前にBlackでコードをきれいにすることで可読性を上げた。
## Step3 Read the codes
何をするためのコードなのかの理解。そしてデータ取得からゴールまでの手順を把握。
## Step4 Refactoring
1. main.pyの中だけで前処理、計算、出力を行っていたため、それぞれのモジュールを作成。
2. 前処理、計算、出力のモジュールそれぞれにpytestを行うということを意識しながら関数を定義。
3. それぞれの関数はできるだけ１つの作業のみ行うようにした。    
例）日付データ型への変更と月データの抽出を同じ関数内で行わない。日付データへの変更のための関数と月のみを抽出する関数を別々に作成。
4. 関数名を見ただけで何をする関数なのかを分かるようにした。
5. 引数の名前も何のための引数か一目で分かるようにした。
6. 変数名も分かりやすいものに変更した。
7. Type annotaionで引数にどのデータ型を入力すべきかを示した。
8. 負の値をnp.nanへ置き換える作業を一度で完結できるように変更。
9. 気温の平均を表す変数の名前をavg_cloudsからMonthly_Heating_Degreeへ変更。
10. ディレクトリ構造の整理のためoutput.csvもdataディレクトリに出力されるように変更。
## Step5 Pytest
1. テスト用のcsvファイルを作成。
2. テストコードの可読性向上のためにfixtureを作成。
## Step6 コードの整理
1. すべてのモジュールのコードをBlackで整理。
2. mypyで引数に指定の型の値が入っているか確認。
