from pyproj import Transformer
import pyproj

# 使用pyproj包的Transformer类初始化GPS转utm的类
# 其中第一个参数 4326 是源数据的坐标系ID，文章下文中会再进行说明
# 第二个参数 32750 是要转换的目标坐标系ID
tf = Transformer.from_crs(4326, 32750)

# 取一个经纬度进行转换，并设为基准值，纬度是36.649这个， 经度是117.022
utm_x, utm_y = tf.transform(36.64918343, 117.02233187)
print(utm_x, utm_y)

# 转换其它经纬度坐标并计算差值
x_base = [0.0]
y_base = [0.0]

lon = 113.407579611111
lat = 23.1802382777778

tmp_x, tmp_y = tf.transform(gps_data['wei'][i], gps_data['jing'][i])
x_base.append(tmp_x - utm_x)
y_base.append(tmp_y - utm_y)

print(x_base, y_base)
