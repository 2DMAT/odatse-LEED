ユーザープログラムによる解析
================================

ここでは、odatse-LEED モジュールを用いたユーザープログラムを作成し、解析を行う方法を説明します。逆問題アルゴリズムは例としてNelder-Mead法を用います。


サンプルファイルの場所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
サンプルファイルは ``sample/user_program`` にあります。
フォルダには以下のファイルが格納されています。

- ``simple.py``

  メインプログラム。パラメータを ``input.toml`` ファイルから読み込んで解析を行う。

- ``input.toml``

  ``simple.py`` で利用する入力パラメータファイル

- ``base/``

  メインプログラムでの計算を進めるための参照ファイルを格納するディレクトリ。参照ファイルは ``exp.d``, ``rfac.d``, ``tleed4.i``, ``tleed5.i`` .

- ``ref.txt``

  本チュートリアルで得られる結果の比較データ

- ``prepare.sh``, ``do.sh``

  本チュートリアルを一括計算するために準備されたスクリプト

以下、これらのファイルについて説明したのち、実際の計算結果を紹介します。

プログラムの説明
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``simple.py`` は odatse-LEED モジュールを用いて解析を行うシンプルなプログラムです。
プログラムの全体を以下に示します。

.. code-block:: python

    import odatse
    import odatse.algorithm.min_search
    from odatse.extra.LEED import Solver
    
    info = odatse.Info.from_file("input.toml")
    
    solver = Solver(info)
    runner = odatse.Runner(solver, info)
    alg = odatse.algorithm.min_search.Algorithm(info, runner)
    alg.main()

プログラムではまず、必要なモジュールを import します。

- ODAT-SE のメインモジュール ``odatse``

- 今回利用する逆問題解析アルゴリズム ``odatse.algorithm.min_search``

- 順問題ソルバーモジュール ``odatse.extra.LEED``

次に、解析で利用するクラスのインスタンスを作成します。

- ``odatse.Info`` クラス

  パラメータを格納するクラスです。 ``from_file`` クラスメソッドに TOML ファイルのパスを渡して作成することができます。

- ``odatse.extra.LEED.Solver`` クラス

  odatse-LEED モジュールの順問題ソルバーです。Info クラスのインスタンスを渡して作成します。

- ``odatse.Runner`` クラス

  順問題ソルバーと逆問題解析アルゴリズムを繋ぐクラスです。Solver クラスのインスタンスおよび Info クラスのパラメータを渡して作成します。

- ``odatse.algorithm.min_search.Algorithm`` クラス

  逆問題解析アルゴリズムのクラスです。ここでは Nelder-Mead法による最適化アルゴリズムのクラスモジュール ``min_search`` を利用します。Runner のインスタンスをわたして作成します。

Solver, Runner, Algorithm の順にインスタンスを作成した後、Algorithm クラスの ``main()`` メソッドを呼んで解析を行います。

上記のプログラムでは、入力パラメータを TOML形式のファイルから読み込む形ですが、パラメータを dict 形式で渡すこともできます。


入力ファイルの説明
~~~~~~~~~~~~~~~~~~~
メインプログラム用の入力ファイル ``input.toml`` に、順問題ソルバーおよび逆問題解析アルゴリズムのパラメータを指定します。 ``base`` および ``solver`` セクションの内容は前述のグリッド型探索の場合と同じです。

逆問題解析アルゴリズムについては、Nelder-Mead法のパラメータを ``algorithm.param`` の項目に指定します。なお、アルゴリズムの種類を指定する ``algorithm.name`` パラメータの値は無視されます。

- ``min_list``, ``max_list`` は探索領域の指定で、領域の下端と上端を変数についてのリストの形式で与えます。

- ``initial_list`` と ``initial_scale_list`` は初期シンプレックスを指定するパラメータです。2変数の例では、 ``initial_list = [z1, z2]``, ``initial_scale_list = [dz1, dz2]`` を指定した場合、 ``[z1, z2]``, ``[z1+dz1, z2]``, ``[z1, z2+dz2]`` を頂点とする三角形を初期シンプレックスにとります。


計算実行
~~~~~~~~~~~~

あらかじめ ``sample/satleed`` ディレクトリ内で ``setup.sh`` を実行して SATLEED をコンパイルし、 ``satl1.exe`` と ``satl2.exe`` を作成しておきます。

サンプルファイルが置いてあるフォルダへ移動します。

.. code-block::

    $ cd sample/user_program

メインプログラムを実行します。計算時間は通常のPCで数分程度で終わります。
    
.. code-block::

    $ python3 simple.py | tee log.txt

実行すると、以下の様な出力がされます。

.. code-block::

    label_list      : ['z1', 'z2']
    param.min_list  : [-0.5, 0.75]
    param.max_list  : [0.5, 2.75]
    param.initial_list: [-0.2, 1.75]
    minimize.initial_scale_list: [0.02, 0.02]
    eval: x=[-0.18  1.75], fun=0.9422
    eval: x=[-0.14  1.72], fun=0.8607
    eval: x=[-0.12  1.745], fun=0.7262
    eval: x=[-0.03  1.6975], fun=0.4055
    eval: x=[-0.01  1.7225], fun=0.3186
    eval: x=[-0.01  1.7225], fun=0.3186
    eval: x=[-0.045 1.71875], fun=0.2953
    eval: x=[-0.025 1.74375], fun=0.2157
    ...

``x=[z1, z2]`` に各ステップでの候補パラメータと、その時の ``fun=R-factor`` が出力されます。
最終的に推定されたパラメータは、 ``output/res.dat`` に出力されます。今の場合、

.. code-block::

    fx = 0.2101
    z1 = -0.01991012930870084
    z2 = 1.7509844067692764
        
となります。リファレンス ref.txt が再現されているか確かめてください。

なお、一連の計算を行う ``do.sh`` スクリプトが用意されています。
