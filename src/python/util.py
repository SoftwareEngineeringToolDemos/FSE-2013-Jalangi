import os
import subprocess
import sys

class JalangiInstall:

    def instrumentation_script(self):
        return self.get_home() + "/src/js/instrument/esnstrument.js"

    def get_home(self):
        if hasattr(self,"home"):
            return self.home
        else:
            return os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,os.pardir))

    def self_or_env(self,local,env):
        if hasattr(self,local):
            return self.getattr(local)
        else:
            return os.environ[env]

    def coverage(self):
        return self_or_env("use_coverage", "USE_COVERAGE")

    def timed(self):
        return self_or_env("use_time", "USE_TIME")

DEFAULT_INSTALL = JalangiInstall()
        
class JalangiException(Exception):
    """Any error that happens during the Jalangi 
    analysis process

    Attributes:
       install -- the JalangiInstall being used
       msg -- User understandable message of what went wrong
       trigger -- Exception that caused this error (if any)
       """
    def __init__(self, install, message, trigger=None):
        self.install = install
        self.message = message
        self.trigger = trigger


def run_node_script(script, *args):
    """Execute script and returns output string"""
    return subprocess.check_output(["node", script] + [x for x in args]) 
