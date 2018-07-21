# -*- mode: python -*-

import os

block_cipher = None

k3Exe = 'ext/gentleK3.exe' if os.name == 'nt' else 'ext/gentleK3'
m3Exe = 'ext/gentleM3.exe' if os.name == 'nt' else 'ext/gentleM3'
ffmpegExe = 'ext/ffmpeg.exe' if os.name == 'nt' else 'ext/ffmpeg'
datasMac = [
             (k3Exe, 'ext'),
             (m3Exe, 'ext'),
             (ffmpegExe, 'ext'),
             ('www', 'www'),
             ('exp', 'exp'),
             ('COPYING', '.'),
             ('README.md', '.')
           ]
datasWindows = [
             (k3Exe, 'ext'),
             (m3Exe, 'ext'),
             (ffmpegExe, 'ext'),
             ('ext/libgcc_s_seh-1.dll', 'ext'),
             ('ext/libgfortran-3.dll', 'ext'),
             ('ext/libopenblas.dll', 'ext'),
             ('ext/libquadmath-0.dll', 'ext'),
             ('ext/openfst64.dll', 'ext'),
             ('ext/pthreadVC2.dll', 'ext'),
             ('www', 'www'),
             ('exp', 'exp'),
             ('COPYING', '.'),
             ('README.md', '.')
           ]

a = Analysis(['serve.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=datasWindows if os.name == 'nt' else datasMac,
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
          name='cursesearch',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True)
