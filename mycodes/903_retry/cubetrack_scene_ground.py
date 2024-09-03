"""
Author: Jiadong Lu
Date: 24/05/21
Details: Configuration for a simple CubeTrack robot interactive scene.
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.scene import InteractiveScene, InteractiveSceneCfg
from omni.isaac.lab.terrains import TerrainImporterCfg
from pxr import Usd, UsdGeom, UsdPhysics, Gf

from omni.isaac.lab.terrains.config.rough import ROUGH_TERRAINS_CFG  # isort: skip
from cubetrack_cfg import CubeTrack_CFG

BELT_CFG = RigidObjectCfg()


@configclass
class CubeTrackSceneCfg(InteractiveSceneCfg):
    """Configuration for a CubeTrack scene."""

    # ground plane
    ground = AssetBaseCfg(prim_path="/World/defaultGroundPlane", spawn=sim_utils.GroundPlaneCfg())

    # lights
    dome_light = AssetBaseCfg(prim_path="/World/Light", spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75)))

    # articulation
    CubeTrack: ArticulationCfg = CubeTrack_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack")  # type: ignore

    R_Belt001: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link001",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.2546006441116333, 0.06399192810058593),
                                                                                           rot=(0.9807853648311435, -0.19508989756786554, -1.969965915618229e-08, -3.9184969767193966e-09)))
    R_Belt002: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link002",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.2984684109687805, 0.10142369717359542),
                                                                                           rot=(0.8757476614499029, -0.48276913060491555, 1.434840687371208e-08, 7.909776088375923e-09)))
    R_Belt003: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link003",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.31169408559799194, 0.1574784755706787),
                                                                                           rot=(-0.6797413783110932, 0.7334518788648203, 8.0433587127269e-07, 8.678913405111728e-07)))
    R_Belt004: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link004",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.28955209255218506, 0.2106071837246418),
                                                                                           rot=(-0.41485463280427287, 0.9098877038628588, -3.4389266348652846e-08, -7.542490337878597e-08)))
    R_Belt005: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link005",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.2404121458530426, 0.2406541645526886),
                                                                                           rot=(-0.10908329167434282, 0.9940326128842435, -1.2950304398671695e-08, -1.1801096869618729e-07)))
    R_Belt006: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link006",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.18146565556526184, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt007: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link007",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.12206563353538513, 0.2445499986410141),
                                                                                           rot=(6.123233995736766e-17, 0.9999999999999911, -8.153579261448262e-24, 1.331580545039615e-07)))
    R_Belt008: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link008",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.0626656711101532, 0.2445499986410141),
                                                                                           rot=(-1.6081226496766364e-16, 0.9999999999999911, 8.153578775457068e-24, 1.3315804656712298e-07)))
    R_Belt009: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link009",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.003265678882598877, 0.2445499986410141),
                                                                                           rot=(1.3315805419983656e-07, 0.9999999999999822, -1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt010: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link010",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.05613432079553604, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt011: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link011",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.11553432792425156, 0.2445499986410141),
                                                                                           rot=(6.123233995736766e-17, 0.9999999999999911, -8.153579261448262e-24, 1.331580545039615e-07)))
    R_Belt012: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link012",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.17493435740470886, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt013: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link013",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.23433437943458557, 0.2445499986410141),
                                                                                           rot=(1.3315805419983656e-07, 0.9999999999999822, -1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt014: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link014",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.2937343716621399, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    R_Belt015: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link015",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.3531344532966614, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.773106429778839e-14, 1.3315803069344468e-07)))
    R_Belt016: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link016",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.4125344157218933, 0.2445499986410141),
                                                                                           rot=(-1.6081226496766364e-16, 0.9999999999999911, 8.153578775457068e-24, 1.3315804656712298e-07)))
    R_Belt017: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link017",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.47193443775177, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999911, 2.713356549466485e-21, 2.0376961508237458e-14)))
    R_Belt018: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link018",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.5312000513076782, 0.2430364578962326),
                                                                                           rot=(0.05122398234634278, 0.9986871900813398, 7.169819434593754e-09, -1.397862191992625e-07)))
    R_Belt019: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link019",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.5842878818511963, 0.22041238248348236),
                                                                                           rot=(0.351679456524898, 0.9361204836228895, 1.9522131723958207e-17, -5.19651263436472e-17)))
    R_Belt020: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link020",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.6141855716705322, 0.1711785826832056),
                                                                                           rot=(0.6264384731116782, 0.7794708714284982, -5.125806181890269e-08, 6.377987277067048e-08)))
    R_Belt021: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link021",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.6092199087142944, 0.11372697129845619),
                                                                                           rot=(0.8327645233796706, 0.5536273553575718, 8.854543971334196e-08, -5.8865593143334815e-08)))
    R_Belt022: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link022",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.5714471340179443, 0.070181006193161),
                                                                                           rot=(0.9618950226821511, 0.2734190288536481, 1.7194340872505535e-07, -4.887497982919223e-08)))
    R_Belt023: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link023",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.5151703357696533, 0.055771307647228235),
                                                                                           rot=(0.9999413771049563, 0.010827850820453067, 2.313033605248919e-07, -2.5046651127536807e-09)))
    R_Belt024: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link024",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.4557860493659973, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt025: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link025",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.39638620615005493, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt026: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link026",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.33698606491088867, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt027: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link027",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.2775862216949463, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt028: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link028",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.2181861400604248, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt029: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link029",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.15878629684448242, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt030: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link030",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.09938618540763855, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt031: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link031",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, 0.03998635709285736, 0.0554499939084053), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt032: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link032",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.019413739442825317, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt033: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link033",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.07881361246109009, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt034: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link034",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.13821366429328918, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    R_Belt035: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/R_BELTS/right_belt_link035",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(0.2375, -0.1976136565208435, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt001: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link001",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.2546006441116333, 0.06399192810058593),
                                                                                           rot=(0.9807853648311435, -0.19508989756786554, -1.969965915618229e-08, -3.9184969767193966e-09)))
    L_Belt002: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link002",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.2984684109687805, 0.10142369717359542),
                                                                                           rot=(0.8757476614499029, -0.48276913060491555, 1.434840687371208e-08, 7.909776088375923e-09)))
    L_Belt003: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link003",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.31169408559799194, 0.1574784755706787),
                                                                                           rot=(-0.6797413783110932, 0.7334518788648203, 8.0433587127269e-07, 8.678913405111728e-07)))
    L_Belt004: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link004",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.28955209255218506, 0.2106071837246418),
                                                                                           rot=(-0.41485463280427287, 0.9098877038628588, -3.4389266348652846e-08, -7.542490337878597e-08)))
    L_Belt005: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link005",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.2404121458530426, 0.2406541645526886),
                                                                                           rot=(-0.10908329167434282, 0.9940326128842435, -1.2950304398671695e-08, -1.1801096869618729e-07)))
    L_Belt006: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link006",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.18146565556526184, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt007: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link007",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.12206563353538513, 0.2445499986410141),
                                                                                           rot=(6.123233995736766e-17, 0.9999999999999911, -8.153579261448262e-24, 1.331580545039615e-07)))
    L_Belt008: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link008",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.0626656711101532, 0.2445499986410141),
                                                                                           rot=(-1.6081226496766364e-16, 0.9999999999999911, 8.153578775457068e-24, 1.3315804656712298e-07)))
    L_Belt009: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link009",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.003265678882598877, 0.2445499986410141),
                                                                                           rot=(1.3315805419983656e-07, 0.9999999999999822, -1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt010: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link010",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.05613432079553604, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt011: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link011",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.11553432792425156, 0.2445499986410141),
                                                                                           rot=(6.123233995736766e-17, 0.9999999999999911, -8.153579261448262e-24, 1.331580545039615e-07)))
    L_Belt012: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link012",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.17493435740470886, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt013: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link013",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.23433437943458557, 0.2445499986410141),
                                                                                           rot=(1.3315805419983656e-07, 0.9999999999999822, -1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt014: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link014",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.2937343716621399, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.7731067468350324e-14, 1.3315805450396032e-07)))
    L_Belt015: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link015",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.3531344532966614, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999822, 1.773106429778839e-14, 1.3315803069344468e-07)))
    L_Belt016: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link016",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.4125344157218933, 0.2445499986410141),
                                                                                           rot=(-1.6081226496766364e-16, 0.9999999999999911, 8.153578775457068e-24, 1.3315804656712298e-07)))
    L_Belt017: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link017",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.47193443775177, 0.2445499986410141),
                                                                                           rot=(-1.3315805452146108e-07, 0.9999999999999911, 2.713356549466485e-21, 2.0376961508237458e-14)))
    L_Belt018: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link018",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.5312000513076782, 0.2430364578962326),
                                                                                           rot=(0.05122398234634278, 0.9986871900813398, 7.169819434593754e-09, -1.397862191992625e-07)))
    L_Belt019: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link019",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.5842878818511963, 0.22041238248348236),
                                                                                           rot=(0.351679456524898, 0.9361204836228895, 1.9522131723958207e-17, -5.19651263436472e-17)))
    L_Belt020: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link020",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.6141855716705322, 0.1711785826832056),
                                                                                           rot=(0.6264384731116782, 0.7794708714284982, -5.125806181890269e-08, 6.377987277067048e-08)))
    L_Belt021: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link021",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.6092199087142944, 0.11372697129845619),
                                                                                           rot=(0.8327645233796706, 0.5536273553575718, 8.854543971334196e-08, -5.8865593143334815e-08)))
    L_Belt022: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link022",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.5714471340179443, 0.070181006193161),
                                                                                           rot=(0.9618950226821511, 0.2734190288536481, 1.7194340872505535e-07, -4.887497982919223e-08)))
    L_Belt023: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link023",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.5151703357696533, 0.055771307647228235),
                                                                                           rot=(0.9999413771049563, 0.010827850820453067, 2.313033605248919e-07, -2.5046651127536807e-09)))
    L_Belt024: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link024",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.4557860493659973, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt025: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link025",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.39638620615005493, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt026: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link026",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.33698606491088867, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt027: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link027",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.2775862216949463, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt028: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link028",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.2181861400604248, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt029: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link029",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.15878629684448242, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt030: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link030",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.09938618540763855, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt031: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link031",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, 0.03998635709285736, 0.0554499939084053), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt032: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link032",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.019413739442825317, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt033: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link033",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.07881361246109009, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt034: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link034",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.13821366429328918, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
    L_Belt035: RigidObjectCfg = BELT_CFG.replace(prim_path="{ENV_REGEX_NS}/CubeTrack/L_BELTS/left_belt_link035",
                                                 init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.2375, -0.1976136565208435, 0.055450001358985895), rot=(1.0, 0.0, 0.0, 0.0)))
