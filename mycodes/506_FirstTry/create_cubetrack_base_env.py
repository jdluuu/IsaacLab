# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
This script demonstrates how to create a simple environment with a cartpole. It combines the concepts of
scene, action, observation and event managers to create an environment.
"""

"""Launch Isaac Sim Simulator first."""


import argparse

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Tutorial on creating a cartpole base environment.")
parser.add_argument("--num_envs", type=int, default=16, help="Number of environments to spawn.")

# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

import math
import time
import torch

import omni.isaac.lab.envs.mdp as mdp
from omni.isaac.lab.envs import ManagerBasedEnv, ManagerBasedEnvCfg
from omni.isaac.lab.managers import EventTermCfg as EventTerm
from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils import configclass

# from omni.isaac.lab_tasks.manager_based.classic.cartpole.cartpole_env_cfg import CartpoleSceneCfg
from cubetrack_scene_ground import CubeTrackSceneCfg


@configclass
class ActionsCfg:
    """Action specifications for the environment."""

    # joint_efforts = mdp.JointEffortActionCfg(asset_name="robot", joint_names=["slider_to_cart"], scale=5.0)
    joint_positions = mdp.JointPositionActionCfg(asset_name="CubeTrack", joint_names=['Flipper_to_R_QsETM_Verti', 'Flipper_to_L_QsETM_Verti'])
    joint_velocities = mdp.JointVelocityActionCfg(asset_name="CubeTrack", joint_names=['R_QsETM_VERTI_Joint', 'L_QsETM_VERTI_Joint', 'r_starwheel_joint', 'l_starwheel_joint'])


@configclass
class ObservationsCfg:
    """Observation specifications for the environment."""

    @configclass
    class PolicyCfg(ObsGroup):
        """Observations for policy group."""

        # observation terms (order preserved)
        joint_pos_rel = ObsTerm(func=mdp.joint_pos_rel, params={"asset_cfg": SceneEntityCfg("CubeTrack")})
        joint_vel_rel = ObsTerm(func=mdp.joint_vel_rel, params={"asset_cfg": SceneEntityCfg("CubeTrack")})

        def __post_init__(self) -> None:
            self.enable_corruption = False
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()


@configclass
class EventCfg:
    """Configuration for events."""
    # on reset
    reset_cart_position = EventTerm(
        func=mdp.reset_cubetrack_scene_to_default,
        mode="reset",
    )

@configclass
class CartpoleEnvCfg(ManagerBasedEnvCfg):
    """Configuration for the cartpole environment."""

    # Scene settings
    scene = CubeTrackSceneCfg(num_envs=1024, env_spacing=2.5)
    # Basic settings
    observations = ObservationsCfg()
    actions = ActionsCfg()
    events = EventCfg()

    def __post_init__(self):
        """Post initialization."""
        # viewer settings
        self.viewer.eye = [10.0, 0.0, 6.0]
        self.viewer.lookat = [4.0, 0.0, 2.0]
        # step settings
        self.decimation = 4  # env step every 4 sim steps: 200Hz / 4 = 50Hz
        # simulation settings
        self.sim.dt = 0.001  # sim step every 5ms: 200Hz


def main():
    """Main function."""
    # parse the arguments
    env_cfg = CartpoleEnvCfg()
    env_cfg.scene.num_envs = args_cli.num_envs
    # setup base environment
    env = ManagerBasedEnv(cfg=env_cfg)
    last_time = time.time()
    # simulate physics
    count = 0
    while simulation_app.is_running():
        with torch.inference_mode():
            # reset
            if count % 30 == 0:
                count = 0
                env.reset()
                print("-" * 80)
                now_time = time.time()
                delta = now_time-last_time
                print("[INFO "+str(delta)+"]: Resetting environment...")
                last_time = now_time
            # sample random actions
            joint_efforts = torch.zeros_like(env.action_manager.action)
            joint_efforts[:,0:2] = 0.5 * math.pi
            # step the environment
            obs, _ = env.step(joint_efforts)
            # print current orientation of pole
            # print("[Env 0]: Pole joint: ", obs["policy"][0][1].item())
            # update counter
            count += 1

    # close the environment
    env.close()


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
