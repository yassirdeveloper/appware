class BaseError(Exception):

    def display():
        pass


class CommandError(BaseError):
    pass


class InterfaceError(BaseError):
    pass


class InvalidCommand(CommandError):
    pass


class UnknownCommandOptions(CommandError):
    pass


class FileNotFoundCommandError(CommandError):
    pass