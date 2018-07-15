# -*- mode: python -*-

import os

block_cipher = None

k3Exe = 'ext/gentleK3.exe' if os.name == 'nt' else 'ext/gentleK3'
m3Exe = 'ext/gentleM3.exe' if os.name == 'nt' else 'ext/gentleM3'
ffmpegExe = 'ext/ffmpeg.exe' if os.name == 'nt' else 'ext/ffmpeg'

a = Analysis(['serve.py'],
             pathex=[os.path.dirname(os.path.abspath(__file__))],
             binaries=[],
             datas=[
             (k3Exe, 'ext'),
             (m3Exe, 'ext'),
             (ffmpegExe, 'ext'),
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
