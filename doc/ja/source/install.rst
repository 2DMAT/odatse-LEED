odatse-LEED のインストール
=============================

実行環境・必要なパッケージ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- python 3.9 以上

- pythonパッケージ

  - numpy (>= 1.14)
  - pydantic (>= 2.0)
  - fortranformat
  - ODAT-SE (>=3.0)
   
- SATLEED

  - コンパイルには Fortranコンパイラが必要

ダウンロード・インストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ODAT-SE をインストールする

   - ソースコードからのインストール

     リポジトリから ODAT-SE のソースファイルを取得します。

     .. code-block:: bash

        $ git clone https://github.com/issp-center-dev/ODAT-SE.git

     pip コマンドを実行してインストールします。

     .. code-block:: bash

        $ cd ODAT-SE
        $ python3 -m pip install .

     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。

     .. note::
        Python 3.7未満の環境では以下のようなエラーが発生します。本パッケージではPython 3.9以上を利用するようにしてください。

        .. code-block:: bash

           Directory '.' is not installable. File 'setup.py' not found.

     ``python3 -m pip install .[all]`` を実行するとオプションのパッケージも同時にインストールします。

2. odatse-LEED をインストールする

   odatse-LEED のソースファイルは GitHub リポジトリから取得できます。以下の手順でリポジトリをクローンした後、pip コマンドを実行してインストールします。

     .. code-block:: bash
      
        $ cd ../
        $ git clone https://github.com/2DMAT/odatse-LEED.git
        $ cd odatse-LEED
        $ python3 -m pip install .

     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。

     odatse-LEED のライブラリと、実行コマンド ``odatse-LEED`` がインストールされます。

3. SATLEED をインストールする

   - ``SATLEED`` のソースコードは以下の URL から取得できます。

     .. code-block::

	http://www.icts.hkbu.edu.hk/VanHove_files/leed/leedsatl.zip

     ファイルを展開し、所定の手続きに従ってコンパイルします。

   - ``SATLEED`` は計算したい系の詳細によってソースコードのパラメータを適宜書き換える必要があります。 
     ステップ2 で取得した odatse-LEED のソースファイルの ``sample/satleed`` ディレクトリに、サンプルを実行する場合の書き換え ``leedsatl.patch`` とコンパイルを自動で行うスクリプト ``setup.sh`` が用意されているので、それを利用しインストールすることもできます。

     .. code-block:: bash

         $ cd odatse-LEED/sample/satleed
         $ sh ./setup.sh

     ``setup.sh`` を実行すると、現在のディレクトリに ``satl1.exe`` と ``satl2.exe`` が作成されます。

     コンパイラやコンパイルオプションを変更する場合は ``setup.sh`` を編集してください。
   

実行方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODAT-SE では順問題ソルバと逆問題解析アルゴリズムを組み合わせて解析を行います。
LEEDの解析を行うには次の2通りの方法があります。

1. このパッケージに含まれる odatse-LEED プログラムを利用して解析を行います。ユーザは、プログラムの入力となるパラメータファルを TOML 形式で作成し、プログラムの引数に指定してコマンドを実行します。逆問題解析のアルゴリズムはパラメータで選択できます。

2. odatse-LEED ライブラリと ODAT-SE フレームワークを用いてプログラムを作成し、解析を行います。逆問題解析アルゴリズムは import するモジュールで選択します。プログラム中に入力データの生成を組み込むなど、柔軟な使い方ができます。

パラメータの種類やライブラリの利用方法については以降の章で説明します。


アンインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

odatse-LEED モジュールおよび ODAT-SE モジュールをアンインストールするには、以下のコマンドを実行します。

.. code-block:: bash

    $ python3 -m pip uninstall odatse-LEED ODAT-SE

