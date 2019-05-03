
from uperations.kernel import Kernel
from uperation_base import Base
from libraries.wegopix.wegopix import wegopix

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base(),
        wegopix.name(): wegopix()
    })

    Kernel.get_instance().set_observers({
        #operation().__class__ : [
        #   observer().__class__
        # ]
    })