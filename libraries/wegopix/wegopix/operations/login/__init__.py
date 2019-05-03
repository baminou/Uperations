
from uperations.operation import Operation
from ...utils import login
import json

class Login(Operation):

    @staticmethod
    def name():
        return "Login"

    @staticmethod
    def description():
        return "Login to wegopix"

    def _parser(self, main_parser):
        main_parser.add_argument('--email',dest='email', required=True, help="E-mail to login")
        main_parser.add_argument('--password',dest='password', required=True, help="Password of the user")
        main_parser.add_argument('--host',dest='host', required=True, help="Wegopix host")
        main_parser.add_argument('--output',dest='output', default='.user.json', help="Output user to json file")
        return

    def _run(self):
        with open(self.args.output,'w') as fp:
            json.dump(login(self.args.host,self.args.email,self.args.password),fp)
        return