import ctypes 

dll = ctypes.cdll.LoadLibrary("C:\\Users\\USER\\Desktop\\buuctf\\re\\snake\\Snake\\Snake_Data\\Plugins\\Interface.dll")

for i in range(17,20):
    dll.GameObject(i)
