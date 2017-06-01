from cx_Freeze import setup, Executable

exe=Executable(
     script="main.pyw",
     base="Win32Gui",
     icon="output.ico"
     )

includes = ["os","configparser","time","glob","ctypes"]

setup(
    name = "informer_msg", 
    version = "1",
    description = "informer_msg", 
    executables = [exe],
    )