from uperations.operation import Operation
import argparse
import json

class StreamOperation(Operation):

    def _parser(self, main_parser):
        super(StreamOperation, self)._parser(main_parser)
        main_parser.add_argument('--stream',dest='stream_json',default='.stream.json', help="Stream.json file", type=argparse.FileType('r'))
        return main_parser

    def _before_start(self):
        super(StreamOperation, self)._before_start()
        self.stream_data = json.load(self.args.stream_json)
        return True

    def _on_running(self):
        super(StreamOperation, self)._on_running()
        return True

    def _on_error(self, exception):
        super(StreamOperation, self)._on_error(exception)
        return True

    def _on_completed(self):
        super(StreamOperation, self)._on_completed()
        return True

    @property
    def alias(self):
        return self.stream_data.get('alias')

    @property
    def upload_token(self):
        return self.stream_data.get('upload_token')