
from ...operation_types.auth_operation import AuthOperation
from ...utils import get_stream
import json


class GetStream(AuthOperation):

    @staticmethod
    def name():
        return "GetStream"

    @staticmethod
    def description():
        return "Retrieve a stream with alias"

    def _parser(self, main_parser):
        main_parser.add_argument('--alias', dest='alias',help="Alias of the stream")
        main_parser.add_argument('--host',dest='host', required=True, help="Wegopix host")
        main_parser.add_argument('--output',dest='output', default='.stream.json', help="Output user to json file")
        return

    def _run(self):
        with open(self.args.output,'w') as fp:
            json.dump(get_stream(self.args.host,self.token,self.args.alias).json(),fp)
        return