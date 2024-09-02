from pxr import Usd, UsdGeom, Gf
import omni

# 假设已经获取到stage和Prim的引用
stage = omni.usd.get_context().get_stage()

xform_prim = stage.GetPrimAtPath("/CubeTrack")

# 确保Prim是一个Xformable
if not xform_prim.IsA(UsdGeom.Xformable):
    print("The specified prim is not an Xformable.")
    sys.exit(1)

# 创建UsdGeom.Xformable接口
xformable = UsdGeom.Xformable(xform_prim)

# Access the existing transform ops
xform_ops = xformable.GetOrderedXformOps()
scale_op = None
for op in xform_ops:
    if op.GetOpType() == UsdGeom.XformOp.TypeScale:
        scale_op = op
        break

# If a scale operation is not found, create one
if not scale_op:
    scale_op = xformable.AddScaleOp()

# 设置缩放值
scale_value = Gf.Vec3f(1.5, 1.5, 1.5)  # 设置想要的缩放因子
scale_op.Set(scale_value)