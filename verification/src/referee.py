from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "friday"
    FUNCTION_NAMES = {
        "python_3": "friday",
        "js_node": "friday"
    }
    ENV_COVERCODE = {
        
    }