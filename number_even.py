var_int = 8785
var_int1 = ((var_int // 1000) + 1) % 2
var_int2 = ((var_int // 100) + 1) % 2
var_int3 = ((var_int // 10) + 1) % 2
var_int4 = ((var_int // 1) + 1) % 2
print(var_int1 + var_int2 + var_int3 + var_int4)