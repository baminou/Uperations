
from abc import abstractmethod
from operations.documentable import Documentable
import os
import threading
import inspect
import time

class Operation(Documentable):
    """This abstract class is the mother class for operations. An operation is a specific action on a JTracker workflow.
    Two methods have to be implemented for childen classes.
    _schema and _run"""

    def __init__(self):
        self.output = None
        self.main_thread = None
        return

    @property
    def args(self):
        """
        Return:
            dict: Arguments
        """
        return self._args

    @args.setter
    def args(self, value):
        self._args = value
        return

    def set_output(self, output):
        """
        Set the output attribute

        Args:
            output: The available output at the end of the operation
        """
        self.output = output
        return

    def get_output(self):
        """
        Return the output attribute

        Return:
            The output value
        """
        return self.output

    @abstractmethod
    def _schema(self):
        """
        Returns the validation schema for the config file needed to run the operation.
        
        Return:
            dict: A validation dictionary 
        
        Raises:
            NotImplementedError: The method has not been implemented yet
        """
        raise NotImplementedError

    @abstractmethod
    def _run(self):
        """
        The logic of the operation. The config dictionary can be retrieved in the config dictionary: self._config
        
        Raises:
            NotImplementedError: The method has not been implemented yet
        """
        raise NotImplementedError

    @classmethod
    def execute(cls, args):
        """
        This method is the main one executed. It triggers all the hooks, before_start, on_running, on_error, on_completed.

        Args:
            args (dict): The required arguments to run the operation
        """
        obj = cls()
        obj.args = args

        run = obj.before_start()

        if run:
            obj.main_thread = threading.Thread(target=obj.run)
            obj.main_thread.start()
            while obj.main_thread.is_alive():
                obj.on_running()
                time.sleep(obj.args.TIMER)
            obj.on_completed()
        return

    def run(self):
        ""
        try:
            self.set_output(self._run())
        except Exception as err:
            self.on_error(err)
        return


    @classmethod
    def parser(cls, main_parser):
        obj = cls()
        for parent in obj.__class__.__bases__:
            if issubclass(parent, Operation):
                parent.parser(main_parser)
        obj._parser(main_parser)
        return

    def _parser(self, main_parser):
        main_parser.add_argument('--TIMER',default=1, help="Interval seconds for on_running method")
        return

    @staticmethod
    def environ_or_required(key):
        if os.environ.get(key):
            return {'default': os.environ.get(key)}
        else:
            return {'required': True}

    def before_start(self):
        """
        This method is triggered right before executing the run. At this point, the arguments are already accessible
        in the class. This is the perfection function to establish some rules before running the operation. If those rules are
        not respected, return False and the operation is not going to be run. This method should not be overriden.

        Return:
            bool: False if the operation cannot be run, True otherwhise
        """
        return self._before_start()

    def _before_start(self):
        """
        This method is wrapped under before_start method to be overriden. This method contains the specific logic of an operation.
        Return:
            bool: False if the operation cannot be run, True otherwhise
        """
        return True

    def on_completed(self):
        """
        Once the operation is done, this hook is ran. This method should not be overriden.
        Return:
            bool: True if everything was done successfully, False otherwise
        """
        return  self._on_completed()

    def _on_completed(self):
        """
        This method is wrapped under on_completed to be overriden. This method contains the specific logic for an operation
        Return:
            bool: True if everything was done successfully, False otherwise
        """
        return True

    def on_running(self):
        """
        While the operation is running, this method is triggerred. In orther to change the invterval in second, this method is executed,
        the user can provide --TIMER {time_in_second}. This operation should not be overriden
        Return:
            bool: True if the operation should keep running, False otherwise
        """
        return self._on_running()

    def _on_running(self):
        """
        This method is wrapped under on_running method to be overriden. This method contains the specific logic on an operation
        Return:
            bool: True if the operation should keep running, False otherwise
        """
        return True

    def on_error(self, exception):
        """
        This method is triggered in case of an exception. This method should not be overriden.

        Parms:
            exception: The exception raised by the operation
        """
        return self._on_error(exception)

    def _on_error(self, exception):
        """
        This method is wrapped under on_error to be overriden. This method contains the specific logic for an operaion in case of an error.

        Raises:
            The operation exception raised by the operation while running.
        """
        raise Exception

    @classmethod
    def install(cls):
        """
        Install everything required to run the operation. This method should not be overriden.
        """
        requirements = os.path.dirname(inspect.getfile(cls))+"/requirements.txt"
        if os.path.isfile(requirements):
            os.system('pip3 install -r %s' % requirements)
        return
