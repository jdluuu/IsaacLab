from pxr import UsdPhysics, Gf, UsdGeom

# Get the stage
stage = omni.usd.get_context().get_stage()

def extract_scale_from_matrix(matrix):
	x_axis = Gf.Vec3d(matrix.GetRow(0)[:3])
	y_axis = Gf.Vec3d(matrix.GetRow(1)[:3])
	z_axis = Gf.Vec3d(matrix.GetRow(2)[:3])
	
	scale_x = x_axis.GetLength()
	scale_y = y_axis.GetLength()
	scale_z = z_axis.GetLength()
	
	return Gf.Vec3f(scale_x, scale_y, scale_z)

for i in range(1, 71):
	path = f"/CubeTrackV2_Isaac_0508_2125/belt_link_{i:03}"
	xform_prim = stage.GetPrimAtPath(path)
	if xform_prim and xform_prim.IsA(UsdGeom.Xformable):
		xformable = UsdGeom.Xformable(xform_prim)
		world_transform = xformable.ComputeLocalToWorldTransform(Usd.TimeCode.Default())
		
		translation = world_transform.ExtractTranslation()

		rotation_matrix = world_transform.ExtractRotation().GetQuat()
		rotation = Gf.Rotation(rotation_matrix).Decompose(Gf.Vec3d(1, 0, 0), Gf.Vec3d(0, 1, 0), Gf.Vec3d(0, 0, 1))
		print(f"Rotation of {path}: {rotation}")

		newpath = f"/CubeTrack/L_BELTS/belt_link{i:03}"
		xform_prim2 = stage.GetPrimAtPath(newpath)
		if xform_prim2 :
			print("Already have")
		else:
			xform = UsdGeom.Xform.Define(stage, newpath)
			xform_collisions = UsdGeom.Xform.Define(stage, newpath + "/collisions")
			translate_op = xform.AddTranslateOp()
			new_trans = Gf.Vec3d(0, translation[1], translation[2])
			translate_op.Set(new_trans)
			
			rotate_op = xform.AddRotateXYZOp()
			rotate_op.Set(rotation)
			
			cube = UsdGeom.Cube.Define(stage, newpath + "/collisions/mesh")
			scale_op = xform.AddScaleOp()
			scale_op.Set(Gf.Vec3f(0.025, 0.01485, 0.005))


	else:
		print(f"{object_path} is not a transformable prim or does not exist.")
