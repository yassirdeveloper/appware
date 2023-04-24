from errors import ErrorWidget


class BaseError(Exception):

    @classmethod
    def display(cls):
        pass


class CommandError(BaseError):
    pass


class InterfaceError(BaseError):
    message = None
    code = None

    def __init__(self):
        ErrorWidget(exception=self)
        super().__init__()


class InvalidCommand(CommandError):
    pass


class UnknownCommandOptions(CommandError):
    pass


class FileNotFoundCommandError(CommandError):
    pass


class UnrunnableApplication(InterfaceError):
    message = "Can't run the application"
