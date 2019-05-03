
from ...operation_types.auth_operation import AuthOperation
from ...operation_types.stream_operation import StreamOperation
import argparse
from ...utils import upload
import json

class Upload(AuthOperation, StreamOperation):

    @staticmethod
    def name():
        return "Upload"

    @staticmethod
    def description():
        return "Upload a picture to a stream"

    def _parser(self, main_parser):
        main_parser.add_argument('--picture',dest='picture',required=True,help="Picture to upload", type=argparse.FileType('rb'))
        main_parser.add_argument('--host',dest='host', required=True, help="Wegopix host")
        main_parser.add_argument('--marvel-host',dest='marvel_host',help="Marvel host", required=True)
        return

    def _run(self):
        print(json.dumps(upload(self.args.host,self.args.marvel_host,self.token,self.alias,self.upload_token,self.args.picture)))
        return