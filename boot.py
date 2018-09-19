
from uperations.kernel import Kernel
from uperation_base import Base

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base()
    })