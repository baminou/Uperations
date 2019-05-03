
from ...operation_types.auth_operation import AuthOperation
from ...utils import create_stream
import json

class CreateStream(AuthOperation):

    @staticmethod
    def name():
        return "CreateStream"

    @staticmethod
    def description():
        return "Create a new stream"

    def _parser(self, main_parser):
        main_parser.add_argument('--name',dest='name',required=True, help="Name of the stream")
        main_parser.add_argument('--host',dest='host', required=True, help="Wegopix host")
        main_parser.add_argument('--output',dest='output', default='.stream.json', help="Output user to json file")
        return

    def _run(self):
        with open(self.args.output,'w') as fp:
            json.dump(create_stream(self.args.host,self.token,self.args.name),fp)
        return
