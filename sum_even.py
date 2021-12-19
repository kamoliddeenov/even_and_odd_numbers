var_int = 8548
sum_even = 0
var_int1 = var_int // 1000
var_int1 *= (var_int1 + 1) % 2
var_int2 = var_int // 100 % 10
var_int2 *= (var_int2 + 1) % 2
var_int3 = var_int // 10 % 10
var_int3 *= (var_int3 + 1) % 2
var_int4 = var_int // 1 % 10
var_int4 *= (var_int4 + 1) % 2
sum_even = var_int1 + var_int2 + var_int3 + var_int4
print(sum_even)