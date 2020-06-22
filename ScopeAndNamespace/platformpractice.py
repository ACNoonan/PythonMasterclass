import platform


print('platform.version(): '+ platform.version())
print('platform.system(): ' + platform.system())
print('platform.release(): ' + platform.release())
# print('platform.win32_ver() ' + platform.win32_ver())
print('platform.platform() ' + platform.platform())

for i in platform.win32_ver():
    print(i)