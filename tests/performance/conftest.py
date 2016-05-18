"""
This module contains functions that are used to run performance tests on
acceptance level.
"""
import inspect
import json

from environment import docker

from tests import *
from tests.utils.client_utils import mount_users
from tests.utils.path_utils import get_file_name
from tests.utils.git_utils import get_branch_name, get_commit, get_repository
from tests.utils.performance_utils import *
from tests.utils.utils import get_copyright, get_authors, get_suite_description

__author__ = "Jakub Kudzia"
__copyright__ = """(C) 2016 ACK CYFRONET AGH
This software is released under the MIT license cited in 'LICENSE.txt'."""


@pytest.fixture(scope="session")
def json_output(request):
    performance_report = PerformanceReport("performance", get_repository(),
                                           get_commit(), get_branch_name())

    def fin():
        if not os.path.exists(PERFORMANCE_LOGDIR):
            os.makedirs(PERFORMANCE_LOGDIR)
        f = open(PERFORMANCE_OUTPUT, 'w')
        f.write(json.dumps(performance_report.report))

    request.addfinalizer(fin)
    return performance_report


class AbstractPerformanceTest:
    @pytest.fixture(scope="module")
    def suite_report(self, request, env_report):
        module = inspect.getmodule(self.__class__)
        name = get_file_name(inspect.getfile(self.__class__))
        report = SuiteReport(name, get_suite_description(module),
                             get_copyright(module), get_authors(module))

        def fin():
            env_report.add_to_report("suites", report)

        request.addfinalizer(fin)
        return report

    @pytest.fixture(scope="module")
    def env_report(self, request, json_output, env_description_file):
        name = env_description_file.split(os.path.sep)[-1]
        report = EnvironmentReport(name)

        def fin():
            json_output.add_to_report("envs", report)

        request.addfinalizer(fin)
        return report

    @pytest.fixture()
    def clients(self, request, environment, context, client_ids,
                env_description_file):

        mount_users(request, environment, context, client_ids,
                    env_description_file, **get_users(environment))


def get_users(environment):
    data = environment['client_data']
    users = []
    client_instances = []
    mount_paths = []
    client_hosts = []
    tokens = []
    for client_host in data.keys():
        for client_instance in data[client_host].keys():
            d = data[client_host][client_instance]
            users.append(d['token_for'])
            client_instances.append(client_instance)
            mount_paths.append(d['mounting_path'])
            client_hosts.append(client_host)
            tokens.append('token')
    return {"users": users,
            "client_instances": client_instances,
            "mount_paths": mount_paths,
            "client_hosts": client_hosts,
            "tokens": tokens}
