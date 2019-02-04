from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import subprocess
from distutils.spawn import find_executable
import sys
from typing import Optional
from typing import Sequence
import logging


def _check_tool():  # type: () -> bool
    """

    :return:
    """
    return find_executable('google-java-format') is not None


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    """
    :param argv:
    :return:
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    parser.add_argument('--verbose', action='store_true', help='Be verbose')
    args = parser.parse_args(argv)

    if args.verbose:
        logging.basicConfig(format='%(levelname)5s: %(message)s',
                            level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s',
                            level=logging.INFO)

    command = [find_executable('google-java-format'), '--replace']

    return_code = 0

    if not _check_tool():
        return_code = 1
        logging.error('Could not find google-java-format\n' +
                      'Try \'brew install google-java-format\' on MacOS')
    elif len(args.filenames) > 0:
        for file in args.filenames:
            logging.debug('Checking %s', file)

        command += args.filenames

        logging.debug("Runing \"%s\"", ' '.join(command))

        result = subprocess.run(command, capture_output=True)

        return_code = result.returncode

        if len(result.stdout) > 0:
            logging.info(result.stdout.decode('utf-8', 'replace'))
        if len(result.stderr) > 0:
            logging.info(result.stderr.decode('utf-8', 'replace'))
    else:
        logging.info('No Java files')
    return return_code


if __name__ == '__main__':
    sys.exit(main())
