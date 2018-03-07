import os


def env(key, default=None, typ=None, prefix=''):
    value = os.environ.get('{}{}'.format(prefix, key))
    if value:
        if typ:
            if typ == bool:
                if value.lower() == 'true':
                    return True
                elif value.lower() == 'false':
                    return False
            else:
                value = typ(value)
        if default and not callable(default) and not typ:
            value = type(default)(value)

    return value or (default() if callable(default) else default)


# Server
HOST = env('HOST', '0.0.0.0')
PORT = env('PORT', 5000)
SSL_KEY = env('SSL_KEY')
SSL_CERT = env('SSL_CERT')
ENABLE_ACCESS_LOG = env('ENABLE_ACCESS_LOG', False, bool)
