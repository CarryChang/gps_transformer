# -*-coding=utf-8 -*-
import pyproj

proj_4326 = pyproj.Proj(init="epsg:4326")  # wgs坐标系统的EPSG Code
proj_3857 = pyproj.Proj(init="epsg:3857")  # 球体墨卡托——转换投影坐标系统的EPSG Code
# gps
lng, lat = 112.901623, 27.984723
x, y = pyproj.transform(proj_4326, proj_3857, lng, lat)
# 投影坐标

print(x, y)


# https://www.cnblogs.com/Kaivenblog/p/8607803.html
# https://www.cnblogs.com/caiyiying/p/14878582.html
# 12568151.182094144 3247047.8459646017

