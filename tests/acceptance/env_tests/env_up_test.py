from tests.test_common import *
import os
import subprocess
from env_test_utils import *
import ast

from environment import docker, env


class TestEnvUp:
    @classmethod
    # Run the env_up.py script, capture and parse the output
    def setup_class(cls):
        logdir = get_logdir_name(acceptance_logdir, get_test_name(__file__))
        result = run_env_up_script("env_up.py", [
            '-l', logdir,
            test_utils.test_file('env.json')
        ])
        cls.result = result

    @classmethod
    # Clean up removing all dockers created in the test
    def teardown_class(cls):
        docker.remove(cls.result['docker_ids'], force=True, volumes=True)

    # Test if the env_up.py script works as expected.
    def test_env_up(self):
        env = self.result
        # Check if number of started dockers is correct
        # The number should be:
        # 1 dns node

        # 4 op_worker nodes
        # 2 cluster_manager nodes for op_workers
        # 2 DB nodes for op_workers

        # 1 OZ nodes
        # 1 cluster_manager nodes for oz_worker
        # 1 DB node for oz_worker

        # 2 appmock nodes

        # 2 client nodes
        # ------------
        # 16 nodes
        assert 16 == len(env['docker_ids'])

        check_globalregistry_up(env, 1)
        check_cluster_manager_up(env, 2)
        check_provider_worker_up(env, 4)
        check_appmock_up(env, 2)
        check_client_up(env, 2)
