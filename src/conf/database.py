from envparse import env

env.read_envfile()


DB_CONFIG = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': env('POSTGRES_HOST', None),
                'port': '5432',
                'user': env('POSTGRES_USER', None),
                'password': env('POSTGRES_PASSWORD', None),
                'database': env('POSTGRES_DB', None),
            }
        },
    },
    'apps': {
        'models': {
            'models': ['src.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}
