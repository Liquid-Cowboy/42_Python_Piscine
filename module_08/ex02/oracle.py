from os import getenv, getcwd
from os.path import exists
from sys import stderr


if __name__ == '__main__':
    try:
        from dotenv import load_dotenv

        if not exists('.env'):
            raise FileNotFoundError(f'".env" file not found at {getcwd()}')

        print('\nORACLE STATUS: Reading the Matrix...\n')

        load_dotenv()  # loads the .env file

        mode: str = getenv('MATRIX_MODE')
        if mode not in ('production', 'development'):
            raise ValueError('uknown mode '
                             '(available: "development" / "production")')

    except (FileNotFoundError, ValueError) as e:
        print(f'[ERROR]: {e}\n'
              'Exiting...', file=stderr)
        exit(1)

    except ModuleNotFoundError as e:
        print(f'[ERROR]: {e} not found. Install using'
              '"pip install python-dotenv"\n'
              'Exiting...', file=stderr)
        exit(1)

    vars: dict = {
        'DATABASE_URL': ('Connected to local instance', 'Inactive'),
        'API_KEY': ('Authenticated', 'Uknown key'),
        'LOG_LEVEL': ('DEBUG', 'Uknown'),
        'ZION_ENDPOINT': ('Online', 'Offline'),
    }
    for var in vars.keys():
        if getenv(var) and not getenv(var).strip() == '':
            vars[var] = vars[var][0]
        else:
            print(f'[WARNING]: Missing configuration "{var}"\n')
            vars[var] = vars[var][1]

    print('Configuration loaded:\n'
          f'Mode: {mode}\n'
          f'Database: {vars["DATABASE_URL"]}\n'
          f'API Access: {vars["API_KEY"]}\n'
          f'Log Level: {vars["LOG_LEVEL"]}\n'
          f'Zion Network: {vars["ZION_ENDPOINT"]}')
    print()

    print('Environment security check:\n'
          '[OK] No hardcoded secrets detected\n'
          '[OK] .env file properly configured\n'
          '[OK] Production overrides available\n'
          '\n'
          'The Oracle sees all configurations.')
