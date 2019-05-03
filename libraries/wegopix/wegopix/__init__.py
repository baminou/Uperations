
from uperations.library import Library
from .operations.login import Login
from .operations.create_stream import CreateStream
from .operations.upload import Upload
from .operations.get_stream import GetStream

class wegopix(Library):

    @staticmethod
    def name():
        return "wegopix"

    @staticmethod
    def description():
        return "Not description provided"

    def _init_operations(self):
        self._operations = {
            'login': Login(self),
            'stream:create': CreateStream(self),
            'stream:get': GetStream(self),
            'upload': Upload(self)
        }
        return

    def operations(self):
        return self._operations