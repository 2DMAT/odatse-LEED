.. 2dmat documentation master file, created by
   sphinx-quickstart on Tue May 26 18:44:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

チュートリアル
==================================

順問題ソルバーとして用意されている ``odatse-LEED`` は M.A. Van Hove氏により作成された低速電子線回折(LEED)の解析ソフトウェア ``SATLEED`` を ODAT-SE で利用するモジュールとして作成されています。
SATLEED では、与えられた原子座標に対して回折データをシミュレーションで計算します。これを順問題と見なしたとき、回折データが実験で与えられたときにそれを再現する原子座標を求める問題は逆問題に相当します。ODAT-SE はこの逆問題を解くフレームワークを提供します。

このチュートリアルでは、全探索法 (mapper) を用いてもっともらしい原子座標を推定する問題を例として odatse-LEED の使い方を説明します。
以下では odatse-LEED に付属の ``odatse-LEED`` プログラムを利用し、TOML形式のパラメータファイルを入力として解析を行います。
次に、ユーザープログラムの項では、メインプログラムを自分で作成して使う方法を説明します。

.. toctree::
   :maxdepth: 1

   mapper
   user_program

