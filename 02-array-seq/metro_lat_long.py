"""
嵌套元组拆包
"""
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

"""
{:15}——位置映射，相当于{0:15}，对应于format中的''，15为字符宽度
|——字符串间的分隔符
{:^9}——位置映射，相当于{1:^9}，对应于format中的'lat.'，^为居中对齐，9为字符宽度
|——字符串间的分隔符
{:^9}——位置映射，相当于{2:^9}，对应于format中的'long.'，^为居中对齐，9为字符宽度
"""
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))
