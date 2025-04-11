グリッド型探索
================================

ここでは、グリッド型探索を行い、回折データから原子座標を解析する方法について説明します。
グリッド型探索はMPIに対応しています。
探索グリッドを与えるデータ ``MeshData.txt`` を事前に準備する必要があります。

サンプルファイルの場所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

サンプルファイルは ``sample/mapper`` にあります。
フォルダには以下のファイルが格納されています。

- ``base`` ディレクトリ

  メインプログラムでの計算を進めるための参照ファイルを格納するディレクトリ。参照ファイルは ``exp.d``, ``rfac.d``, ``tleed4.i``, ``tleed5.i`` です。

- ``input.toml``

  メインプログラムの入力ファイル

- ``MeshData.txt``

  探索グリッドのデータ

- ``ref_ColorMap.txt``

  計算結果の参照値。計算が正しく実行されたか確認するための output/ColorMap の参照データ。

- ``prepare.sh`` , ``do.sh``

  本チュートリアルを一括計算するために準備されたスクリプト

以下、これらのファイルについて説明したあと、実際の計算結果を紹介します。

参照ファイルの説明
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tleed4.i``, ``tleed5.i``, ``rfac.d`` は satleed のパラメータファイルです。
最適化する原子座標は ``tleed5.i`` の中で ``opt000``, ``opt001`` のようにキーワードとして埋め込みます。
``exp.d`` は参照する実験データです。

実際に探索するグリッドは ``MeshData.txt`` で与えます。
サンプルでは ``MeshData.txt`` の中身は以下のようになっています。

.. code-block::

   1 -0.490000 0.777500
   2 -0.490000 0.977500
   3 -0.490000 1.177500
   4 -0.490000 1.377500
   5 -0.490000 1.577500
   ...

1列目が通し番号、2列目以降は ``base/tleed5.i`` に入る ``opt000`` , ``opt001`` の値が順に指定されています。


.. note::
   
  ``MeshData.txt`` を作成するスクリプト ``make_meshdata.py`` が用意されています。

  .. code-block:: bash

     $ python3 make_meshdata.py > MeshData.txt

  を実行するとメッシュデータが作成されます。


入力ファイルの説明
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここでは、メインプログラム用の入力ファイル ``input.toml`` について説明します。
``input.toml`` の詳細については入力ファイルに記載されています。
以下は、サンプルファイルにある ``input.toml`` の中身になります。

.. code-block::

    [base]
    dimension = 2
    output_dir = "output"
    
    [solver]
    name = "leed"
    [solver.config]
    path_to_first_solver = "../satleed/satl1.exe"
    path_to_second_solver = "../satleed/satl2.exe"
    [solver.param]
    string_list = ["opt000", "opt001"]
    [solver.reference]
    path_to_base_dir = "./base"
    rfactor = "satleed"
    
    [algorithm]
    name = "mapper"
    label_list = ["z1", "z2"]
    [algorithm.param]
    mesh_path = "./MeshData.txt"

    [runner]
    ignore_error = true

最初に ``[base]`` セクションについて説明します。

- ``dimension`` は最適化したい変数の個数です。今の場合は ``base/tleed5.i`` で説明したように2つの変数の最適化を行うので、 ``2`` を指定します。

- ``output_dir`` は出力先のディレクトリ名です。省略した場合はプログラムを実行したディレクトリになります。  

``[solver]`` セクションではメインプログラムの内部で使用するソルバーとその設定を指定します。

- ``name`` は使用したいソルバーの名前です。 ``leed`` に固定されています。

ソルバーの設定は、サブセクションの ``[solver.config]``, ``[solver.param]``, ``[solver.reference]`` で行います。

``[solver.config]`` セクションではメインプログラム内部で呼び出す ``satl1.exe``,  ``satl2.exe`` についてのオプションを指定します。

- ``path_to_first_solver`` は ``satl1.exe`` のコマンド名です。パスを指定するか、コマンド名をPATH環境変数から探索します。

- ``path_to_second_solver`` は ``satl2.exe`` のコマンド名です。パスを指定するか、コマンド名をPATH環境変数から探索します。

``[solver.param]`` セクションではパラメータについての指定を行います。

- ``string_list`` は埋め込みキーワードのリストを指定します。

``[solver.reference]`` セクションでは参照データについての指定を行います。

- ``path_to_base_dir`` は参照データが置いてあるディレクトリ名を指定します。

- ``rfactor`` は R-factor の定義を指定します。デフォルトは ``rpe`` (Pendry R-factor) です。この例では ``satleed`` を指定して、SATLEED が計算した R-factor の値を使用します。

``[algorithm]`` セクションでは、使用するアルゴリスムとその設定をします。

- ``name`` は使用したいアルゴリズムの名前です。このチュートリアルではグリッド探索による解析を行うので、 ``mapper`` を指定します。

- ``label_list`` は、 ``opt000``, ``opt001`` を出力する際につけるラベル名のリストです。

``[algorithm.param]`` セクションでは探索アルゴリズムに関するパラメータを指定します。

- ``mesh_path`` は探索グリッドを記述したファイルを指定します。

``[runner]`` セクションでは外部プログラム実行についての指定を行います。

- ``ignore_error`` を true に指定した場合、外部プログラムの実行と値の評価に関するエラーは NaN として扱い、計算を続行します。
  
その他、入力ファイルで指定可能なパラメータの詳細については入力ファイルの章をご覧ください。

計算実行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

あらかじめ ``sample/satleed`` ディレクトリ内で ``setup.sh`` を実行して SATLEED をコンパイルし、 ``satl1.exe`` と ``satl2.exe`` を作成しておきます。

サンプルファイルが置いてあるフォルダへ移動します。

.. code-block::

    $ cd sample/mapper

メインプログラムを実行します。次のコマンドではプロセス数4のMPI並列を用いた計算を行っています。計算は通常のPCで数分程度で終わります。

.. code-block::

    $ mpiexec -np 4 odatse-LEED input.toml | tee log.txt

実行すると、 ``output`` ディレクトリとその下に各ランクのフォルダが作成され、計算結果が出力されます。また、以下の様なログが標準出力に表示されます。

.. code-block::

    name            : mapper
    label_list      : ['z1', 'z2']
    param.mesh_path : ./MeshData.txt
    Iteration : 1/121
    Iteration : 2/121
    Iteration : 3/121
    Iteration : 4/121
    ...

``z1``, ``z2`` に各メッシュでの候補パラメータと、その時の ``R-factor`` が出力されます。
最終的にグリッド上の全ての点で計算された ``R-factor`` は、 ``ColorMap.txt`` に出力されます。
今回の場合は

.. code-block::

    -0.490000 0.777500 0.861000
    -0.490000 0.977500 1.004700
    -0.490000 1.177500 0.909900
    -0.490000 1.377500 0.896600
    -0.490000 1.577500 1.009500
    -0.490000 1.777500 0.779100
    -0.490000 1.977500 0.944200
    -0.490000 2.177500 0.966500
    -0.490000 2.377500 0.867000
    -0.490000 2.577500 0.907000
    -0.490000 2.777500 0.924100
    -0.390000 0.777500 0.801900
    -0.390000 0.977500 0.793900
    ...

のように得られます。1列目、2列目に ``opt000``, ``opt001`` の値が、3列目に ``R-factor`` が記載されます。
なお、メインプログラムを実行するスクリプトとして ``do.sh`` を用意しています。
``do.sh`` では ``ColorMap.dat`` と ``ref_ColorMap.dat`` の差分も比較しています。
以下、説明は割愛しますが、その中身を掲載します。

.. code-block::

    #!/bin/sh
   
    sh prepare.sh

    time mpiexec -np 4 odatse-LEED input.toml

    echo diff output/ColorMap.txt ref_ColorMap.txt
    res=0
    diff output/ColorMap.txt ref_ColorMap.txt || res=$?
    if [ $res -eq 0 ]; then
      echo TEST PASS
      true
    else
      echo TEST FAILED: ColorMap.txt and ref_ColorMap.txt differ
      false
    fi

計算結果の可視化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``ColorMap.txt`` を図示することで、 ``R-factor`` の小さいパラメータがどこにあるかを推定することができます。
今回の場合は、以下のコマンドを実行すると2次元パラメータ空間の図 ``ColorMapFig.png`` が作成されます。

.. code-block::

    $ python3 plot_colormap_2d.py

作成された図を見ると、(0.0, 1.75) 付近に最小値を持っていることがわかります。

  .. figure:: ../../../common/img/ColorMapFig.*

    2次元パラメータ空間上での R-factor の値。(21 x 21 のメッシュで計算)
