#!/usr/bin/env python3

################################################################################

# Copyright (c) 2023, Tinker Twins
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

################################################################################

# Import libraries
from attrdict import AttrDict

# ROS publishers and subscribers
pub_sub_dict = AttrDict({
    'subscribers': [
        # Co-simulation subscribers
        {'topic':'/autodrive/f1tenth_1/cosim_mode', 'type': 'int', 'name': 'sub_cosim_mode'},
        {'topic':'/autodrive/f1tenth_1/pose_command', 'type': 'pose', 'name': 'sub_pose_command'},
        # Vehicle data subscribers
        {'topic':'/autodrive/f1tenth_1/throttle_command', 'type': 'float', 'name': 'sub_throttle_command'},
        {'topic':'/autodrive/f1tenth_1/steering_command', 'type': 'float', 'name': 'sub_steering_command'}
    ],
    'publishers': [
        # Vehicle data publishers
        {'topic': '/autodrive/f1tenth_1/throttle', 'type': 'float', 'name': 'pub_throttle'},
        {'topic': '/autodrive/f1tenth_1/steering', 'type': 'float', 'name': 'pub_steering'},
        {'topic': '/autodrive/f1tenth_1/left_encoder', 'type': 'joint_state', 'name': 'pub_left_encoder'},
        {'topic': '/autodrive/f1tenth_1/right_encoder', 'type': 'joint_state', 'name': 'pub_right_encoder'},
        {'topic': '/autodrive/f1tenth_1/ips', 'type': 'point', 'name': 'pub_ips'},
        {'topic': '/autodrive/f1tenth_1/imu', 'type': 'imu', 'name': 'pub_imu'},
        {'topic': '/autodrive/f1tenth_1/lidar', 'type': 'laser_scan', 'name': 'pub_lidar'},
        {'topic': '/autodrive/f1tenth_1/front_camera', 'type': 'image', 'name': 'pub_front_camera'}
    ]
})

# Co-simulation commands
cosim_mode = 0 # [0 = false, 1 = true]
posX_command = 0.0 # [-∞, ∞]
posY_command = 0.0 # [-∞, ∞]
posZ_command = 0.0 # [-∞, ∞]
rotX_command = 0.0 # [-1, 1]
rotY_command = 0.0 # [-1, 1]
rotZ_command = 0.0 # [-1, 1]
rotW_command = 1.0 # [-1, 1]

# Vehicle control commands
throttle_command = 0 # [-1, 1]
steering_command = 0 # [-1, 1]