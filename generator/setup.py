from distutils.core import setup
import py2exe

data_files = [('images', ['../resources/rr.png'])]

setup(windows=['gui.py'],
      data_files = data_files,
      options={ 'py2exe': {
      "includes":['sip'],
      "dll_excludes": ['MSVFW32.dll',
                       'AVIFIL32.dll',
                       'AVICAP32.dll',
                       'ADVAPI32.dll',
                       'CRYPT32.dll',
                       'WLDAP32.dll',
                       'MSVCP90.dll']
                       }
      })