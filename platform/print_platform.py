import sys
import platform
from os import getenv
# from pathlib import Path
# from tempfile import gettempdir

def print_platform_info():
  # ==============================
  _platform = platform.platform()
  print(f'Platform: {_platform}')                     # Platform: Windows-10-10.0.19041-SP0

  _system = platform.system()
  print(f'System: {_system}')                         # System: Windows

  _release = platform.release()
  print(f'Release: {_release}')                       # Release: 10

  _version = platform.version()
  print(f'Version: {_version}')                       # Version: 10.0.19041

  _machine = platform.machine()
  print(f'Machine: {_machine}')                       # Machine: AMD64

  _processor = platform.processor()
  print(f'Processor: {_processor}')                   # Processor: Intel64 Family 6 Model 142 Stepping 12, GenuineIntel

  _architecture = platform.architecture()
  print(f'Architecture: {_architecture}')             # Architecture: ('64bit', 'WindowsPE')

  _node = platform.node()
  print(f'Node: {_node}')                             # Node: Kitchen

  _uname = platform.uname()
  print(f'Uname: {_uname}')                           # Uname: uname_result(system='Windows', node='Kitchen', release='10', version='10.0.19041', machine='AMD64', processor='Intel64 Family 6 Model 142 Stepping 12, GenuineIntel')

  _python_build = platform.python_build()
  print(f'Python build: {_python_build}')             # Python build: ('default', 'Oct  8 2020 12:12:24')

  _python_compiler = platform.python_compiler()
  print(f'Python compiler: {_python_compiler}')       # Python compiler: MSC v.1916 64 bit (AMD64)

  _python_branch = platform.python_branch()
  print(f'Python branch: {_python_branch}')           # Python branch: tags/v3.8.6

  _python_implementation = platform.python_implementation()
  print(f'Python implementation: {_python_implementation}')   # Python implementation: CPython

  _python_revision = platform.python_revision()
  print(f'Python revision: {_python_revision}')       # Python revision: 0

  _python_version = platform.python_version()
  print(f'Python version: {_python_version}')         # Python version: 3.8.6

  _python_version_tuple = platform.python_version_tuple()
  print(f'Python version tuple: {_python_version_tuple}')     # Python version tuple: ('3', '8', '6')


def print_windows_env():
  # ==============================
  _computer_name = getenv('COMPUTERNAME')             # コンピュータ名
  print(f'Computer name: {_computer_name}')           # Computer name: Kitchen

  _user_domain = getenv('USERDOMAIN')                 # ドメイン名
  print(f'User domain: {_user_domain}')               # User domain: Kitchen

  _user_name = getenv('USERNAME')                     # ユーザー名
  print(f'User name: {_user_name}')                   # User name: ユーザー名

  _user_profile = getenv('USERPROFILE')               # ユーザープロファイル
  # _user_profile = Path.home()
  print(f'User profile: {_user_profile}')             # User profile: C:\Users\ユーザー名

  _appdata = getenv('APPDATA')                        # Roaming フォルダ
  print(f'Roaming: {_appdata}')                       # Roaming: C:\Users\ユーザー名\AppData\Roaming

  _local_appdata = getenv('LOCALAPPDATA')             # Local フォルダ
  print(f'Local: {_local_appdata}')                   # Local: C:\Users\ユーザー名\AppData\Local

  _temp = getenv('TEMP')                              # Temp フォルダ
  # _temp = gettempdir()
  print(f'Temp: {_temp}')                             # Temp: C:\Users\ユーザー名\AppData\Local\Temp

  _program_files = getenv('PROGRAMFILES')             # Program Files フォルダ
  print(f'Program Files: {_program_files}')           # Program Files: C:\Program Files

  _program_files_86 = getenv('PROGRAMFILES(X86)')     # Program Files (x86) フォルダ
  print(f'Program Files (x86): {_program_files_86}')  # Program Files (x86): C:\Program Files (x86)

  _root = getenv('SystemRoot')                        # Windows フォルダ
  print(f'Root: {_root}')                             # Root: C:\WINDOWS

if __name__ == '__main__':
  args = sys.argv
  print_platform_info()
  print_windows_env()