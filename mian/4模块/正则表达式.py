import re

s = input("input id_no")

def validate_id_format(id_number):
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01](@ref))\d{3}[\dXx]$'
    return re.match(pattern, id_number) is not None

print(validate_id_format(s))