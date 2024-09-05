'''
Author: Wtrwater 1921852290@qq.com
Date: 2024-09-05 17:22:23
LastEditors: Wtrwater 1921852290@qq.com
LastEditTime: 2024-09-05 18:21:37
FilePath: /IsaacLab/mycodes/903_retry/myrewards.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
"""Common functions that can be used to enable reward functions.

The functions can be passed to the :class:`omni.isaac.lab.managers.RewardTermCfg` object to include
the reward introduced by the function.
"""

from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import Articulation, RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.managers.manager_base import ManagerTermBase
from omni.isaac.lab.managers.manager_term_cfg import RewardTermCfg
from omni.isaac.lab.sensors import ContactSensor

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv
"""
Velocity-tracking rewards.
"""


def track_lin_vel_x_exp(env: ManagerBasedRLEnv, std: float, command_name: str, asset_cfg: SceneEntityCfg = SceneEntityCfg("robot")) -> torch.Tensor:
    # extract the used quantities (to enable type-hinting)
    asset: RigidObject = env.scene[asset_cfg.name]
    # compute the error
    lin_vel_error = torch.square(asset.data.lin_vel_b[:, 0] - env.commands[command_name].lin_vel_x)

    return torch.exp(-lin_vel_error / std**2)
