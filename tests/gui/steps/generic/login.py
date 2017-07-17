"""Steps used in login page"""

from pytest_bdd import given, parsers
from pytest_bdd import then
from pytest_bdd import when

from tests.gui.conftest import WAIT_FRONTEND
from tests.gui.utils.generic import repeat_failed, parse_seq, transform

__author__ = "Bartek Walkowicz"
__copyright__ = "Copyright (C) 2017 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"


@given(parsers.re('users? of (?P<browser_id_list>.*?) entered '
                  'admin credentials in login form'))
@repeat_failed(timeout=WAIT_FRONTEND)
def g_enter_admin_credentials_to_login_form(selenium, browser_id_list,
                                            admin_credentials, login_page):
    for browser_id in parse_seq(browser_id_list):
        login = login_page(selenium[browser_id])
        login.username = admin_credentials.username
        login.password = admin_credentials.password


@given(parsers.parse('user of {browser_id_list} entered his '
                     'credentials in login form'))
@given(parsers.parse('users of {browser_id_list} entered their '
                     'credentials in login form'))
@repeat_failed(timeout=WAIT_FRONTEND)
def g_enter_user_credentials_to_login_form(selenium, browser_id_list,
                                           users, login_page):
    for browser_id in parse_seq(browser_id_list):
        login = login_page(selenium[browser_id])
        login.username = users[browser_id].username
        login.password = users[browser_id].password


@given(parsers.re(r'users? of (?P<browser_id_list>.*?) pressed Sign in button'))
@repeat_failed(timeout=WAIT_FRONTEND)
def g_press_sign_in_btn_on_login_page(selenium, browser_id_list, login_page):
    for browser_id in parse_seq(browser_id_list):
        login_page(selenium[browser_id]).sign_in()


@when(parsers.re(r'user of (?P<browser_id>.*?) types "(?P<text>.*?)" to '
                 r'(?P<in_box>Username|Password) input in login form'))
@then(parsers.re(r'user of (?P<browser_id>.*?) types "(?P<text>.*?)" to '
                 r'(?P<in_box>Username|Password) input in login form'))
@repeat_failed(timeout=WAIT_FRONTEND)
def wt_enter_text_to_field_in_login_form(selenium, browser_id, in_box,
                                         text, login_page):
    setattr(login_page(selenium[browser_id]), transform(in_box), text)


@when(parsers.parse('user of {browser_id} presses Sign in button'))
@then(parsers.parse('user of {browser_id} presses Sign in button'))
@repeat_failed(timeout=WAIT_FRONTEND)
def wt_press_sign_in_btn_on_login_page(selenium, browser_id, login_page):
    login_page(selenium[browser_id]).sign_in()


@when(parsers.parse('user of {browser_id} sees that he successfully '
                    'logged in {service}'))
@then(parsers.parse('user of {browser_id} sees that he successfully '
                    'logged in {service}'))
@repeat_failed(timeout=WAIT_FRONTEND)
def wt_assert_successful_login(selenium, browser_id, onepage, service):
    logged_in_service = onepage(selenium[browser_id]).service
    assert logged_in_service.lower() == service.lower(), \
        'logged in {} instead of {}'.format(logged_in_service, service)


@when(parsers.parse('user of {browser_id} sees that he was logged out'))
@then(parsers.parse('user of {browser_id} sees that he was logged out'))
@repeat_failed(timeout=WAIT_FRONTEND)
def wt_assert_login_page(selenium, browser_id, login_page):
    _ = login_page(selenium[browser_id]).header


@when(parsers.parse('user of {browser_id} sees error message '
                    'about invalid credentials'))
@then(parsers.parse('user of {browser_id} sees error message '
                    'about invalid credentials'))
@repeat_failed(timeout=WAIT_FRONTEND)
def wt_assert_err_msg_about_credentials(selenium, browser_id, login_page):
    assert login_page(selenium[browser_id]).err_msg, \
        'no err msg about invalid credentials found'
