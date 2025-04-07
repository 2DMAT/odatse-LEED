入出力
********************************

``odatse-LEED`` モジュールは ``SATLEED`` を用いて原子位置などから Rocking curve を計算し、実験で得られた Rocking curve からの誤差を :math:`f(x)` として返す ``Solver`` です。

この章では、入力パラメータおよび入力データと出力データについて説明します。入力パラメータは Info　クラスの ``solver`` の項目が該当します。TOMLファイルを入力として与える場合は ``[solver]`` セクションに記述します。dict形式でパラメータを作成する場合は ``solver`` キー以下に入れ子の dict形式でデータを用意します。以下では、TOML形式でパラメータ項目を説明します。

入力データは、ターゲットとなる参照データとバルク構造データです。出力データは最適解の結果を格納したファイルです。以下の節で内容を示します。


入力パラメータ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``solver`` セクションおよびサブセクション ``config``, ``param``, ``reference`` を利用します。

- ``name``

  形式: string型

  説明: 順問題ソルバーの名称を指定する。省略可。

- ``dimension``

  形式: int型

  説明: パラメータの次元を指定する。指定しない場合は [base] セクションの値が使われる。


[``config``] セクション
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``path_to_first_solver``

  形式: string型

  説明: ソルバー ``satl1.exe`` へのパス。デフォルト値は ``satl1.exe`` 。

- ``path_to_second_solver``

  形式: string型

  説明: ソルバー ``satl2.exe`` へのパス。デフォルト値は ``satl2.exe`` 。

- ``sigma_file_path``

  形式: string型

  説明: 実験データを格納したファイルへのパス。デフォルト値は ``exp.d`` 。

- ``remove_work_dir``

  形式: bool型

  説明: 各探索点でのソルバーの出力ファイルは ``LogXXXX_YYYY`` というディレクトリに書き出される。XXXX はステップ数、YYYY はレプリカ等の識別子である。 ``remove_work_dir`` が True の場合、探索点の評価が終わった後にこのディレクトリを消去する。デフォルト値は False。

- ``use_tmpdir``

  形式: bool型

  説明: 中間ファイルを書き出すディレクトリを /tmp または環境変数 TMPDIR で指定されるディレクトリ内の一時ディレクトリに指定する。デフォルト値は False。


[``param``] セクション
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``string_list``

  形式: string型のリスト

  説明: 入力ファイルのテンプレートに埋め込まれたキーワードのリスト

  
[``reference``] セクション
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``path_to_base_dir``

  形式: string型

  説明: ソルバーを実行するための入力ファイル ``exp.d``, ``rfac.d``, ``tleed4.i``, ``tleed5.i`` が格納されたディレクトリへのパス

- ``rfactor``

  形式: string型または辞書型

  説明: R-factor のタイプ。複数のタイプの荷重平均を指定することもでき、その場合はタイプと相対ウェイトの辞書型で指定する。(但し複数のタイプを指定できるのは ``r1`` 〜 ``rpe`` のみ)

  指定可能なタイプは後述する。デフォルト値は ``rpe`` (Pendry R-factor)。

- ``rescale``

  形式: bool型

  説明: True の場合、R-factor の計算において :math:`I_t` のリスケールを行う。デフォルト値は False。

- ``smoothing_factor``

  形式: float型

  説明: I-V曲線のスムージングを行う場合のパラメータ。0.0 の場合はスムージングを行わない。デフォルト値は 0.0。

- ``vi_value``

  形式: float型

  説明: Pendry R-factor を計算する際に必要な inner potential の虚部の値。 ``vi_value`` で明示的に指定した場合はこの値を利用する。指定しない場合は SATLEED の入力ファイル ``tleed5.i`` から取得する。

  
R-factor のタイプ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``rfactor`` パラメータに指定可能なタイプは次のとおりです。

以下では、 :math:`\sum_b` はビームについての和を示し、 :math:`\sideset{}{'}\sum_b = \sum_b w_b` は各ビームのエネルギー範囲についての相対ウェイト :math:`w_b = {\int dE}/{\sum_b \int dE}` を考慮した和です。また、 ``rescale`` が True の場合は :math:`c = {\int I_e dE}/{\int I_t dE}` 、False の場合は :math:`c=1` です。

- rsq

  .. math::

     R = \sqrt{ \dfrac{\sum_b \int \left(I_e - I_t\right)^2 dE}{\sum_b \int I_e^{\,2} dE} }

- rsq_modified

  .. math::

     R = \sqrt{ \sideset{}{'}\sum_b \dfrac{\int \left(I_e - I_t\right)^2 dE}{\int I_e^{\,2} dE} }

- r1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e - c I_t \right| dE}{\int I_e dE}

- r2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e - c I_t \right)^2 dE}{\int I_e^{\,2} dE}

- rp1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e^\prime - c I_t^\prime \right| dE}{\int \left|I_e^\prime\right| dE}

- rp2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e^\prime - c I_t^\prime \right)^2 dE}{\int (I_e^\prime)^{2} dE}

- rpp1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right| dE}{\int \left|I_e^{\prime\prime}\right| dE}

- rpp2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e^{\prime\prime} - c I_t^{\prime\prime} \right)^2 dE}{\int (I_e^{\prime\prime})^{2} dE}


- rrzj (reduced Zanazzi-Jona R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{1}{0.027 \int I_e dE} \int \dfrac{\left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right|\cdot\left| I_e^{\prime} - c I_t^{\prime} \right|}{\left|I_e^{\prime}\right| + {\rm max}\left|I_e^{\prime}\right|} dE

- rmzj (modified Zanazzi-Jona R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{1}{\int I_e^{\prime\prime} dE} \int \dfrac{\left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right|\cdot\left| I_e^{\prime} - c I_t^{\prime} \right|}{\left|I_e^{\prime}\right| + c\cdot{\rm max}\left|I_t^{\prime}\right|} dE

- rpe (Pendry R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left(Y_e - Y_t\right)^2 dE}{\int Y_e^{\,2} + Y_t^{\,2} dE}, \quad Y = \dfrac{L}{1 + V_{0i}^{\,2} L^2}, \quad L = {\tilde I}^\prime / {\tilde I}.

  Pendry R-factor では、 :math:`{\tilde I} = I_t + \kappa {\langle I \rangle}` です。 :math:`\kappa` は ``PERSH`` で指定されるパラメータで 0.05 が使われています。 :math:`{\langle I \rangle}` は :math:`I` のピークに関する平均です。また、 :math:`V_{0i}` は inner potential の虚部を示します。

  ※留意: rfac.d の WR(10) パラメータが 1 の場合 (satl2.exe で Pendry R-factor を計算する場合)、出力される I-V 曲線データ iv 1〜 iv N は :math:`{\tilde I}` が出力されます。そのため、R-factor のタイプに ``satleed`` を指定する場合以外は rfac.d の WR(10) パラメータは 0 にする必要があります。

- satleed

  satl2.exe の出力 (search.s) から R-factor の値を取得します。

  
ソルバー用補助ファイル
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ターゲット参照ファイル
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ターゲットにするデータが格納されたファイル。 [``reference``] セクションの ``path_to_base_dir`` 中にある ``tleed4.i`` および ``tleed5.i`` を編集します。

最適化したいパラメータ値をキーワードに置き換えます。
キーワードはパラメータの種別によって異なり、座標値や変位の場合は ``opt`` で始まる文字列、内部エネルギーの場合は ``IP`` で始まる文字列、Debye温度の場合は ``debye`` で始まる文字列です。
キーワードは入力ファイルの solver.param.string_list に列挙します。
string_list の要素数・並び順は、最適化する値を入れる変数のリストの個数・順番と一致させる必要があります。

文字列は入力ファイルの書式に従ってフォーマットされた数値に置き換えられるので、書式に合わせてテンプレート中に埋め込む必要があります。以下の例では、 ``opt000``, ``opt001`` に対応する数値(例えば 0.23)は Fortran の ``(F7.4)`` (全体の幅7桁、小数点以下4桁) に従って ``␣0.2300`` のように整形されて置き換えられます。

なお、IFLAG, LSFLAGを0にしない場合はsatleed側での最適化も行われます。

以下、ファイル例を記載します。

.. code-block::

    1  0  0                          IPR ISTART LRFLAG
    1 10  0.02  0.2                  NSYM  NSYMS ASTEP VSTEP
    5  1  2  2                       NT0  NSET LSMAX LLCUT
    5                                NINSET
    1.0000 0.0000                  1      PQEX
    1.0000 2.0000                  2      PQEX
    1.0000 1.0000                  3      PQEX
    2.0000 2.0000                  4      PQEX
    2.0000 0.0000                  5      PQEX
    3                                NDIM
   opt000 0.0000 0.0000  0           DISP(1,j)  j=1,3
    0.0000opt001 0.0000  0           DISP(2,j)  j=1,3
    0.0000 0.0000 0.0000  1           DISP(3,j)  j=1,3
    0.0000 0.0000 0.0000  0           DISP(4,j)  j=1,3
    0.0000  0                         DVOPT  LSFLAG
    3  0  0                          MFLAG NGRID NIV
    ...
   
出力ファイル
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``leed`` では、 ``output_dir`` に指定する出力ディレクトリ内のランクの番号が記載されたフォルダ下に、評価点ごとのサブフォルダ ``LogXXXX_YYYY`` が作成され、その中に計算時に出力されるファイル一式が出力されます。
``XXXX`` はステップ数、 ``YYYY`` はレプリカ番号等の識別子です。
