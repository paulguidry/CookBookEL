from pathlib import Path
import sys

if Path(__file__).parent.parent not in sys.path:
    sys.path.append(Path(__file__).parent.parent)

if Path(__file__).parent not in sys.path:
    sys.path.append(Path(__file__).parent)


try:
    import LambdaUtil as lh
except Exception as mnfe:
    import CookBookEL.LambdaUtil as lh






class EchoHandler(lh.LambdaHandlerBase):
    """Echo handler."""

    def __init__(self):
        lh.LambdaHandlerBase.__init__(self, lambda_name='test_lambda2')

    def DoWork(self, request, **kwargs):
        """Echo perform method."""
        self.EventReturn['my_data'] = 'big_data'


echo_handler = EchoHandler()