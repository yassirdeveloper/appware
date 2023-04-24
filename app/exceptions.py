class BaseError(Exception):

    def display():
        pass


class CommandError(BaseError):
    pass


class InterfaceError(BaseError):
    pass


class InvalidSysArgs(CommandError):
    pass
