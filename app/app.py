import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow

from exceptions import BaseError, UnrunnableApplication


class Application(QApplication):
    runnable = False

    def run(self):
        if self.runnable:
            super().exec()
        else:
            raise UnrunnableApplication()


def validate_sys_args(sys_args):
    return sys_args


if __name__ == '__main__':
    try:
        sys_args = validate_sys_args(sys.argv)
        app = Application()
        app.run()
    except BaseError as e:
        e.display()
    except Exception as e:
        print(e)
