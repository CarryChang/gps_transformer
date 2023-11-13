from pyproj import Proj
# longitude: 经度
lon = 113.407579611111
lat = 23.1802382777778
Start = 32600
# “WGS 1984”坐标系的墨卡托投影分度带（UTM ZONE）选择方法
# 可根据公式计算，带数=（经度整数位/6）的整数部分+31
daishu = int(lon / 6) + 31
EPSG = Start + daishu
EPSG = "epsg:" + str(EPSG)
print("EPSG:", EPSG)
# 首先定义要转换的投影坐标系
proj1 = Proj("epsg:32649")
'''
epsg编号通过epsg官网或者arcmap中查询获得，此为WGS 84 / UTM zone 1N投影
或者p1 = Proj('+proj=utm +zone=1 +datum=WGS84 +units=m +no_defs')
'''
lon1, lat1 = proj1(113.407579611111, 23.1802382777778)  # 将地理坐标转换为投影坐标，地理坐标为WGS84下的坐标
print("lon1,lat1:", lon1, lat1)
lon2, lat2 = proj1(-3188153.794, 6554885.105, inverse=True)  # 将投影坐标转换为地理坐标

proj3 = Proj(EPSG)

lon3, lat3 = proj3(113.407579611111, 23.1802382777778)  # 将地理坐标转换为投影坐标，地理坐标为WGS84下的坐标
print("lon3,lat3:", lon3, lat3)
# 逆向投影转换为 gps

lon3, lat3 = proj3(lon3, lat3, inverse=True)  # 将投影坐标转换为地理坐标
print("lon3,lat3:", lon3, lat3)



# https://blog.csdn.net/weixin_42569775/article/details/130225132