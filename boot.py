
from uperations.kernel import Kernel
from uperation_base import Base

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base()
    })

    Kernel.get_instance().set_observers({
        #operation().__class__ : [
        #   observer().__class__
        # ]
    })
