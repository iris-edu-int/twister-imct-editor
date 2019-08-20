# -*- mode: python -*-

from obspy.imaging.cm import viridis
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
#from PyInstaller.compat import modname_tkinter

block_cipher = None

_hiddenimports=[]

#import_submodules = (
#'alembic',
#'altgraph',
#'apscheduler',
#'certifi',
#'chardet',
#'dateutil',
#'future',
#'humanize',
#'idna',
#'jsonpickle',
#'libfuturize',
#'libpasteurize',
#'lxml',
#'macholib',
#'mako',
#'markupsafe',
#'matplotlib',
#'mpl_toolkits',
#'numpy',
#'obspy',
#'ordlookup',
#'past',
#'pytz',
#'requests',
#'scipy',
#'selenium',
#'setuptools',
#'slugify',
#'sqlalchemy',
#'tornado',
#'tzlocal',
#'unidecode',
#'urllib3',
#'wheel')

import_submodules = (
'alembic',
'scipy'
)

for submod in import_submodules:
	_hiddenimports += collect_submodules(submod)

# pyinstaller:  collect_data_files(package,include_py_files=False,subdir=None)
_datas=collect_data_files('yasmine')
_datas += collect_data_files('yasmine',False,'static')
_datas.append( ('/usr/local/lib/python3.6/site-packages/obspy/imaging/data/*.*','site-packages/obspy/imaging/data') )

a = Analysis(['yasmine.py'],
             pathex=['/opt/yasmine/backend'],
             binaries=[],
             datas=_datas,
             hiddenimports=_hiddenimports,
#             excludedimports = [modname_tkinter],
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
          name='yasmine.exe',
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
               name='yasmine')

