#!/bin/bash
# SPDX-FileCopyrightText: 2023 Ren Sato
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'

cat /tmp/mypkg.log |
grep '現在時刻:'

