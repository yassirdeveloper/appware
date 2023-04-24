import sys
from enum import Enum
from PySlide6.QtWidgets import QtApplication

from .exceptions import BaseError


class Application:
    def run():
        pass


def validate_sys_args(sys_args):
    pass


if __name__ == '__main__':
    try:
        sys_args = validate_sys_args(sys.argv)
        app = Application(sys_args)
        app.run()
    except BaseError as e:
        e.display()
    except Exception as e:
        print(e)
