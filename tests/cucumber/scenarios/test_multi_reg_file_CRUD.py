"""Test suite for CRUD operations on regular files in onedata,
in multi-client environment.
"""
__author__ = "Jakub Kudzia"
__copyright__ = "Copyright (C) 2015 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"

from tests.cucumber.steps.cucumber_utils import *
from tests.cucumber.steps.env_steps import *
from tests.cucumber.steps.multi_auth_steps import *
from tests.cucumber.steps.multi_dir_steps import *
from tests.cucumber.steps.multi_file_steps import *
from tests.cucumber.steps.multi_reg_file_steps import *

from functools import partial

from tests.utils.path_utils import env_file
from pytest_bdd import scenario
import pytest


@pytest.fixture(scope="module",
                params=["singleprovider_multiclient_directio.json"])
def env_description_file(request):
    return env_file(DEFAULT_CUCUMBER_ENV_DIR, request.param)

scenario = partial(scenario, '../features/multi_reg_file_CRUD.feature')


@scenario('Create regular file')
def test_create(env_description_file):
    pass


@scenario('Rename regular file without permission')
def test_rename_without_permission(env_description_file):
    pass


@scenario('Rename regular file with permission')
def test_rename_with_permission(env_description_file):
    pass


@scenario('Delete regular file by owner')
def test_delete_by_owner(env_description_file):
    pass


@scenario('Delete regular file by other user')
def test_delete_by_other_user(env_description_file):
    pass


@scenario('Read and write to regular file')
def test_read_write(env_description_file):
    pass


@scenario('Read regular file without read permission')
def test_read_without_permission(env_description_file):
    pass


@scenario('Write to regular file with write permission')
def test_write_with_permission(env_description_file):
    pass


@scenario('Write to regular file without write permission')
def test_write_without_permission(env_description_file):
    pass


@scenario('Execute file with execute permission')
def test_execute_with_permission(env_description_file):
    pass


@scenario('Execute file without execute permission')
def test_execute_without_permission(env_description_file):
    pass


#  TODO
@pytest.mark.xfail_env(
    envs=["singleprovider_multiclient_directio",
          "singleprovider_multiclient_proxy",
          "multiprovider_proxy",
          "multiprovider_directio"],
    reason="move is being reimplemented")
@scenario('Move regular file and read')
def test_move(env_description_file):
    pass


# TODO
@pytest.mark.xfail_env(
    envs=["singleprovider_multiclient_directio",
          "singleprovider_multiclient_proxy",
          "multiprovider_proxy",
          "multiprovider_directio"],
    reason="move is being reimplemented")
@scenario('Move big regular file and check MD5')
def test_move_big(env_description_file):
    pass


@scenario('Copy regular file and read')
def test_copy(env_description_file):
    pass


@scenario('Copy big regular file and check MD5')
def test_copy_big(env_description_file):
    pass


@scenario('Opened file')
def test_open(env_description_file):
    pass
