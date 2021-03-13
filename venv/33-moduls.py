import os
import libs # импортирует весь код из модуля


print(__name__)
# print(libs.get_len('hello'))
print(os.getcwd())

f = libs.get_len
print(f('hello'))