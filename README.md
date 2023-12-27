# mypkg
[![test](https://github.com/rensato52/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/rensato52/mypkg/actions/workflows/test.yml)

* ros2のパッケージリポジトリ
* パブリッシャを持つノードtalker.pyが0.5秒ごとに現在時刻とカウントをパブリッシュし，listener.pyがそれらのメッセージを標準出力に表示する．
## インストール方法
* ROS 2を動かすことのできる環境下で以下のコマンドを実行
```bash
$ git clone https://github.com/rensato52/mypkg.git
```

## リポジトリ内のノード
### talker.py
* パブリッシャを持つノードで数字をカウントしてトピック`/countup`を通じて送信する．また，現在時刻をトピック`/current_time`を通じて送信する．
	* トピック`/countup`に流れるメッセージの型は16ビットの符号付き整数（Int16型）．
	* トピック`/current_time`に流れるメッセージの型は文字列を格納するための配列(String型）．

### listener.py
* サブスクライバを持つノードでトピック`/countup`，`/current_time`からメッセージを受け取り表示する

## 実行例
* ros2 runで実行　
```bash
端末1$ ros2 run mypkg talker
(何も表示されない）
端末2$ ros2 run mypkg listener
[INFO] [1703414172.874795979] [listener]: Listen: 0
[INFO] [1703414172.875260496] [listener]: 現在時刻: 2023-12-24 19:36:12
[INFO] [1703414173.364073989] [listener]: Listen: 1
[INFO] [1703414173.365241373] [listener]: 現在時刻: 2023-12-24 19:36:13
[INFO] [1703414173.864099648] [listener]: Listen: 2
[INFO] [1703414173.865173252] [listener]: 現在時刻: 2023-12-24 19:36:13
[INFO] [1703414174.364243806] [listener]: Listen: 3
[INFO] [1703414174.365241269] [listener]: 現在時刻: 2023-12-24 19:36:14
[INFO] [1703414174.864158574] [listener]: Listen: 4
[INFO] [1703414174.865317688] [listener]: 現在時刻: 2023-12-24 19:36:14
・・・
`Ctrl+C`で終了
```

* ros2 launchで実行
```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/satoren/.ros/log/2023-12-24-19-42-53-488994-LAPTOP-T84RS2RQ-6312
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [6314]
[INFO] [listener-2]: process started with pid [6316]
[listener-2] [INFO] [1703414574.387205510] [listener]: Listen: 0
[listener-2] [INFO] [1703414574.388938624] [listener]: 現在時刻: 2023-12-24 19:42:54
[listener-2] [INFO] [1703414574.863974865] [listener]: Listen: 1
[listener-2] [INFO] [1703414574.866099975] [listener]: 現在時刻: 2023-12-24 19:42:54
[listener-2] [INFO] [1703414575.363808598] [listener]: Listen: 2
[listener-2] [INFO] [1703414575.365998024] [listener]: 現在時刻: 2023-12-24 19:42:55
[listener-2] [INFO] [1703414575.863934959] [listener]: Listen: 3
[listener-2] [INFO] [1703414575.865777425] [listener]: 現在時刻: 2023-12-24 19:42:55
[listener-2] [INFO] [1703414576.363629312] [listener]: Listen: 4
[listener-2] [INFO] [1703414576.364674019] [listener]: 現在時刻: 2023-12-24 19:42:56
・・・
`Ctrl+C`で終了
```

## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 20.04
* ROS 2 foxy

## 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作とし、コードの一部を改変したものです．
	*  [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Ren Sato
