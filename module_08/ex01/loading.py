#!/usr/bin/env python3

from importlib import import_module
import sys

dependencies: list[str] = {
    'pandas': 'Data manipulation ready',
    'requests': 'Network access ready',
    'matplotlib': 'Visualization ready',
    'numpy': 'Numerical computations ready',
}


def get_prefix() -> str:
    return (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
        )


def check_dependencies(dep: dict[str, str] = dependencies) -> list[str]:
    """Runs through the dependencies, trying to import them
    via the import_module. Outputs a comprehensive comparison
    between installed and missing modules. Then returns a list
    of said missing modules."""
    missing: list = []
    for p in list(dep.keys()):
        try:
            module = import_module(p)
            version: str = getattr(module, "__version__", "unknown")
            print(f'[OK] {p} ({version}) - {dep[p]}')
        except ImportError:
            print(f'[KO] {p} - Not installed')
            missing.append(p)
    return missing


def build_graph() -> None:
    import requests as rq
    import pandas as pd
    import matplotlib.pyplot as plt

    url: str = "https://jsonplaceholder.typicode.com/posts"
    try:
        r = rq.get(url, timeout=10)
        # timeout parameter sets amount of time a request can last (in seconds)
        r.raise_for_status()  # if response < 200 or > 299 raises an HTTPError
        data = r.json()  # converts dict in str form to valid json data
        df = pd.DataFrame(data)
        # converts this data into a dataframe object made up of
        # series objects (columns)
        counts = df['userId'].value_counts().sort_index()
        # sorting the dataframe via built-in series methods
        # value_counts looks for each instance of the userId
        # it returns a Series object sorted by most frequency to least
        # we then use sort_index to sort de userId ascendingly
        plt.bar(counts.index, counts.values)
        # takes two inputs to establish the graph
        plt.xticks(counts.index)
        # makes sure there are 10 user slots for the 10 userIds
        plt.title('Instagram posts per user')
        plt.xlabel('User')
        plt.ylabel('Posts')
        # these three last attr just set visual text info
        plt.savefig('matrix_analysis.png')
        # saves in the project folder

    except Exception:
        import numpy as np
        print('[ERROR]: Couldn\'t retrieve data from API')
        print('Trying with backup default data...')
        student_nb = np.random.randint(1350, 2080, size=12)
        d_data: list[dict] = []
        for nb in student_nb:
            score: int = np.random.randint(1500)
            d_data.append(
                {
                    'student': 'st' + str(nb),
                    'score': score,
                }
            )
        d_data = sorted(d_data, key=lambda stu: stu['student'][2:])
        df = pd.DataFrame(d_data)
        plt.figure(figsize=(12, 8))
        plt.bar(df['student'], df['score'])
        plt.title('Students\' scores')
        plt.xlabel('STUDENT')
        plt.ylabel('SCORE')
        plt.xticks(rotation=45)
        plt.yticks(np.linspace(0, 1500, 10))
        plt.savefig('matrix_analysis.png')
    finally:
        plt.close()


if __name__ == '__main__':
    print('\nLOADING STATUS: Loading programs...\n')
    print('Dependency management processes:')
    print('\t- pip: installs packages listed in requirements.txt\n'
          '\t    (installs directly to the the current environment)\n')
    print('\t- Poetry: uses pyproject.toml (a way more descriptive\n'
          '\t  setup) to install dependencies and generates\n'
          '\t  poetry.lock. poetry.lock locks the version used in\n'
          '\t  the first installation of the project, guaranteeing\n'
          '\t  future compatibility\n'
          '\t    (automatically creates a virtualenv where project\n'
          '\t     runs isolated)')
    print('')
    print('Checking dependencies:')

    missing: list[str] = check_dependencies(dependencies)

    if missing:
        print(f'\n[ERROR]: Missing dependencies - {missing}')
        print('Please install missing dependencies:')
        print('\t(with pip)')
        print('\t    pip install -r requirements.txt')
        print('\t    python3 loading.py')
        print()
        print('\t(with Poetry)')
        print('\t    poetry install')
        print('\t    poetry run python loading.py')
        exit(1)

    build_graph()

    print()
    print('Environment check:')
    if get_prefix() != sys.prefix:
        print('Project is running in a virtualenv\n')
    else:
        print('Project is running on a global environment\n')

    print('Analyzing Matrix data...\n'
          'Processing 1000 data points...\n'
          'Generating visualization...\n\n'
          'Analysis complete!\n'
          'Results saved to: matrix_analysis.png')
