'''
Author: Wtrwater 1921852290@qq.com
Date: 2024-09-05 16:21:25
LastEditors: Wtrwater 1921852290@qq.com
LastEditTime: 2024-09-05 19:16:41
FilePath: /IsaacLab/mycodes/903_retry/run_cubetrack_rl_env.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
"""Launch Isaac Sim Simulator first."""

import argparse

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Tutorial on running the cartpole RL environment.")
parser.add_argument("--num_envs", type=int, default=16, help="Number of environments to spawn.")

# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app
"""Rest everything follows."""

import torch
import math

from omni.isaac.lab.envs import ManagerBasedRLEnv

from cubetrack_env_cfg import CubeTrackEnvCfg


def convert_vel_to_rad(vel, radius):
    return vel / (radius)


def main():
    """Main function."""
    # create environment configuration
    env_cfg = CubeTrackEnvCfg()
    env_cfg.scene.num_envs = args_cli.num_envs
    # setup RL environment
    env = ManagerBasedRLEnv(cfg=env_cfg)

    # simulate physics
    count = 0
    while simulation_app.is_running():
        with torch.inference_mode():
            # reset
            if count % 300 == 0:
                count = 0
                env.reset()
                print("-" * 80)
                print("[INFO]: Resetting environment...")
            # sample random actions
            joint_efforts = torch.zeros_like(env.action_manager.action)
            joint_efforts[:, 2:] = convert_vel_to_rad(0.5, 0.09455)

            # step the environment
            obs, rew, terminated, truncated, info = env.step(joint_efforts)

            # print("[Env 0]: Pole joint: ", obs["policy"][0][1].item())
            print("[Env 0]: Base velo: ", obs["policy"][0][7].item())  # cubetrack is heading y-axis
            # update counter
            count += 1

    # close the environment
    env.close()


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
