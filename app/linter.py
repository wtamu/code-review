import os.path
from pylint import epylint


USER_UPLOADS_PATH = 'app/uploads/'


class Linter(object):
    """Runs static code analysis on input file. Example:
    * linter = Linter('example.py')
    * result = linter.run()
    """

    def __init__(self, filename, *options):
        self.filename = os.path.join(USER_UPLOADS_PATH, filename)
        self.options = options or ['--enable=all', '--output-format=json']

    def run(self, *options):
        if options:
            self.options.extend(options)

        pylint_stdout, pylint_stderr = epylint.py_run(
            self.filename + ' ' + ' '.join(self.options), return_std=True
        )

        return pylint_stdout.getvalue()
