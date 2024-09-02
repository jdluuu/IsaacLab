import omni
from pxr import Usd, UsdGeom, Gf
from omni.isaac.cloner import GridCloner

# 初始化一个场景
stage = omni.usd.get_context().get_stage()

import ipdb
ipdb.set_trace()

# # 获取要复制的原始对象路径
# original_path = "/World/my_object"

# # 确认对象存在
# if stage.GetPrimAtPath(original_path):
#     # 创建一个新的路径用于复制的对象
#     copy_path = "/World/my_copied_object"
    
#     # 使用USD的复制功能复制对象
#     Usd.Copy(stage.GetPrimAtPath(original_path), stage.GetPrimAtPath(copy_path).GetParent(), copy_path)

#     # 移动复制的对象以便区分（可选）
#     translate = UsdGeom.Xformable(stage.GetPrimAtPath(copy_path))
#     translate.AddTranslateOp().Set(value=Gf.Vec3f(10.0, 0.0, 0.0))
