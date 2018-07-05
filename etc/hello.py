
CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web',
  'args': (
    '--bind=0.0.0.0:8080',
    '--workers=2',
    '--timeout=15',
    '--log-level=debug',
    'hello:app'
  )
}
