# -*- mode: python -*-

block_cipher = None


a = Analysis(['pythonApplication_learnpyqt5_russangame.py'],
             pathex=['C:\\Users\\crige\\source\\repos\\Learn_Pyqt5\\PythonApplication_LearnPyqt5_russangame\\PythonApplication_LearnPyqt5_russangame'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pythonApplication_learnpyqt5_russangame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pythonApplication_learnpyqt5_russangame')
