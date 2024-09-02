"""
Author: Jiadong Lu
Date: 24/05/21
Details: Configuration for a simple CubeTrack robot interactivate scene.
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, BeltObjectCfg, BeltObjectCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.scene import InteractiveScene, InteractiveSceneCfg
from omni.isaac.lab.terrains import TerrainImporterCfg

from omni.isaac.lab.terrains.config.rough import ROUGH_TERRAINS_CFG  # isort: skip
from cubetrack_cfg import CubeTrack_CFG

BELT_CFG = BeltObjectCfg()

@configclass
class CubeTrackSceneCfg(InteractiveSceneCfg):
    """Configuration for a cart-pole scene."""
    
    # ground plane
    ground = AssetBaseCfg(prim_path="/World/defaultGroundPlane", spawn=sim_utils.GroundPlaneCfg())

    # lights
    dome_light = AssetBaseCfg(
        prim_path="/World/Light", spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75))
    )

    # articulation
    CubeTrack: ArticulationCfg = CubeTrack_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

    L_Belt01: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link001")
    L_Belt02: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link002")
    L_Belt03: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link003")
    L_Belt04: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link004")
    L_Belt05: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link005")
    L_Belt06: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link006")
    L_Belt07: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link007")
    L_Belt08: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link008")
    L_Belt09: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link009")
    L_Belt10: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link010")
    L_Belt11: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link011")
    L_Belt12: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link012")
    L_Belt13: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link013")
    L_Belt14: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link014")
    L_Belt15: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link015")
    L_Belt16: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link016")
    L_Belt17: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link017")
    L_Belt18: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link018")
    L_Belt19: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link019")
    L_Belt20: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link020")
    L_Belt21: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link021")
    L_Belt22: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link022")
    L_Belt23: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link023")
    L_Belt24: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link024")
    L_Belt25: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link025")
    L_Belt26: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link026")
    L_Belt27: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link027")
    L_Belt28: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link028")
    L_Belt29: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link029")
    L_Belt30: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link030")
    L_Belt31: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link031")
    L_Belt32: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link032")
    L_Belt33: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link033")
    L_Belt34: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link034")
    L_Belt35: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/L_BELTS/left_belt_link035")

    R_Belt01: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link001")
    R_Belt02: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link002")
    R_Belt03: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link003")
    R_Belt04: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link004")
    R_Belt05: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link005")
    R_Belt06: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link006")
    R_Belt07: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link007")
    R_Belt08: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link008")
    R_Belt09: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link009")
    R_Belt10: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link010")
    R_Belt11: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link011")
    R_Belt12: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link012")
    R_Belt13: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link013")
    R_Belt14: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link014")
    R_Belt15: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link015")
    R_Belt16: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link016")
    R_Belt17: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link017")
    R_Belt18: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link018")
    R_Belt19: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link019")
    R_Belt20: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link020")
    R_Belt21: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link021")
    R_Belt22: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link022")
    R_Belt23: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link023")
    R_Belt24: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link024")
    R_Belt25: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link025")
    R_Belt26: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link026")
    R_Belt27: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link027")
    R_Belt28: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link028")
    R_Belt29: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link029")
    R_Belt30: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link030")
    R_Belt31: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link031")
    R_Belt32: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link032")
    R_Belt33: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link033")
    R_Belt34: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link034")
    R_Belt35: BeltObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot/R_BELTS/right_belt_link035")