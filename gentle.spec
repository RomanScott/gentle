# -*- mode: python -*-

import os

block_cipher = None

k3Exe = 'ext/k3.exe' if os.name == 'nt' else 'ext/k3'
m3Exe = 'ext/m3.exe' if os.name == 'nt' else 'ext/m3'

a = Analysis(['serve.py'],
             pathex=[os.path.dirname(os.path.abspath(__file__))],
             binaries=[],
             datas=[
             (k3Exe, 'ext'),
             (m3Exe, 'ext'),
             ('www', 'www'),
             ('exp', 'exp'),
             ('COPYING', '.'),
             ('README.md', '.')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gentle',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
