pay_part_one = {"john": 1000, "kevin": 60, "ben": 300, "janet": 500, "jean": 30}
pay_part_two = {"jean": 50, "ben": 300, "kevin": 700, "janet": 40, "jack": 1230}

z = set(pay_part_one)
x = set(pay_part_two)
result_list = {}

for i in z | x:
    c = pay_part_one.get(i, 0) + pay_part_two.get(i, 0)
    result_list[i] = c
result = sorted(result_list.items(),key=lambda item: item[1], reverse=True)
print(result)
