from distutils.core import setup

setup(name='planarium-dictionary',
      version='1.0.0',
      scripts = ['planarium-dictionary'],
      data_files = [
      ('share/pixmaps',             ['images/planarium_icon_26x26.png']),
      ('share/applications/hildon', ['planarium-dictionary.desktop']),
      ('share/dbus-1/services',     ['planarium_dictionary.service'])
      ]
     )
