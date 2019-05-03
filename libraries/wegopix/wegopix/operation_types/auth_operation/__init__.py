from uperations.operation import Operation
import json
import argparse

class AuthOperation(Operation):

    def _parser(self, main_parser):
        super(AuthOperation, self)._parser(main_parser)
        main_parser.add_argument('--user',dest='user_json',default='.user.json', help="User.json file", type=argparse.FileType('r'))
        return main_parser

    def _before_start(self):
        super(AuthOperation, self)._before_start()
        self.user_data = json.load(self.args.user_json)
        return True

    def _on_running(self):
        super(AuthOperation, self)._on_running()
        return True

    def _on_error(self, exception):
        super(AuthOperation, self)._on_error(exception)
        return True

    def _on_completed(self):
        super(AuthOperation, self)._on_completed()
        return True

    @property
    def username(self):
        return self.user_data.get('user').get('username')

    @property
    def token(self):
        return self.user_data.get('token')