from os import getenv
# from pathlib import Path
# from tempfile import gettempdir

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