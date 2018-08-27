

from operation_types.operation import Operation
import shutil
import os
from ..utils import library_create

class MakeOperation(Operation):

    @staticmethod
    def name():
        return "make_operation"

    @staticmethod
    def description():
        return "Create a new operation"

    def _parser(self, main_parser):
        main_parser.add_argument('library', help="Name of the library to add the operation")
        main_parser.add_argument('operation', help="Name of the operation")
        return

    def _run(self):

        #Retrieve the library name and path
        library = self.args.get('library')

        #Retrieve the operation name and path
        operation = self.args.get('operation')
        return
        #operation_path = os.path.join(library_path(library),operation)

        template_path = os.path.join(os.path.dirname(os.path.relpath(__file__)),'resources','template')
        #new_init_path = os.path.join(operation_path,'__init__.py')

        library_create(library)

        if os.path.isdir(operation_path) and os.path.isfile(new_init_path):
            raise FileExistsError("The module already exists: "+operation)

        shutil.copytree(template_path,operation_path)
        with open(new_init_path,'r') as f:
            new_text = f.read().replace('NEWOPERATION', MakeOperation.to_camel_case(operation).capitalize())

        with open(new_init_path,'w') as f:
            f.write(new_text)

        cprint("Operation successfully created under: %s" % new_init_path,'green')
        return True


    @staticmethod
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])