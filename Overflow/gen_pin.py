#!/usr/bin/python3
import ctypes
local_c_initial = 0x6b8b4567
local_c = 0x6b8b4567
local_8 = 0
while (local_8 <10):
	local_c = local_c * 0x59 + 0x14
	local_8 = local_8 + 1

PIN = ctypes.c_int(local_c ^ local_c_initial).value
print("The PIN code is: ", PIN)
