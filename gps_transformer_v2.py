import pyproj

# 设置经纬度起点坐标系
in_proj = pyproj.Proj(proj='latlong', datum='WGS84')

# 设置投影坐标系
out_proj = pyproj.Proj(proj='utm', zone=33, datum='WGS84')

# 经纬度转投影坐标：longitude 经度
lng, lat = 113.977, 22.730
x, y = pyproj.transform(in_proj, out_proj, lng, lat)
print(x, y)



# 10252037.584816232 12244364.077204105