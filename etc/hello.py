CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'args': (
        '--bind=0.0.0.0:8000',
        '--access-logfile access.log',
        '--error-logfile error.log',
        '--workers=4',
        '--timeout=60',
        
    )
}
