"""Steps for features of Onezone login page.
"""

__author__ = "Jakub Liput"
__copyright__ = "Copyright (C) 2016 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"


from tests.gui.conftest import WAIT_BACKEND, WAIT_FRONTEND
from tests.gui.steps.onezone_logged_in_common import panel_to_css
from tests.utils.acceptance_utils import list_parser

from selenium.webdriver.support.ui import WebDriverWait as Wait

from pytest_bdd import when, then, parsers
from pytest_selenium_multi.pytest_selenium_multi import select_browser


def _get_items_from_panel_list(driver, panel, item_type):
    panel = panel_to_css[panel.lower()]
    items = driver.find_elements_by_css_selector('{0} .{1}s-accordion-item, '
                                                 '{0} .{1}s-accordion-item '
                                                 '.{1}s-accordion-heading '
                                                 '.{1}-header'.format(panel,
                                                                      item_type))

    return {label.text: item for label, item in zip(items[1::2], items[::2])}


def _not_in_panel_list(driver, panel, item_type, item_list):
    items = _get_items_from_panel_list(driver, panel, item_type)
    for item in list_parser(item_list):
        if item in items:
            return False
    return True


@when(parsers.re(r'user of (?P<browser_id>.+?) sees that (?P<items>.+?) '
                 r'(has|have) disappeared from (?P<item_type>.+?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
@then(parsers.re(r'user of (?P<browser_id>.+?) sees that (?P<items>.+?) '
                 r'(has|have) disappeared from (?P<item_type>.+?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
@when(parsers.re(r'user of (?P<browser_id>.*?) does not see (?P<items>.*?) '
                 r'on (?P<item_type>.*?) list in expanded '
                 r'"(?P<panel>.+?)" Onezone panel'))
@then(parsers.re(r'user of (?P<browser_id>.*?) does not see (?P<items>.*?) '
                 r'on (?P<item_type>.*?) list in expanded '
                 r'"(?P<panel>.+?)" Onezone panel'))
def is_not_present_in_panel_list(selenium, browser_id, items,
                                 item_type, panel, tmp_memory):
    driver = select_browser(selenium, browser_id)
    items = tmp_memory[browser_id]['gen_str'] if items == 'new item' else items
    Wait(driver, WAIT_BACKEND).until(
        lambda d: _not_in_panel_list(driver, panel, item_type, items),
        message='checking for absence of {items} on {list} list'
                ''.format(items=items, list=item_type)
    )


@when(parsers.re(r'user of (?P<browser_id>.*?) sees that (?P<items>.*?) '
                 r'(has|have) appeared on (?P<item_type>.*?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
@then(parsers.re(r'user of (?P<browser_id>.*?) sees that (?P<items>.*?) '
                 r'(has|have) appeared on (?P<item_type>.*?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
@when(parsers.re(r'user of (?P<browser_id>.*?) sees (?P<items>.*?) '
                 r'on (?P<item_type>.*?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
@then(parsers.re(r'user of (?P<browser_id>.*?) sees (?P<items>.*?) '
                 r'on (?P<item_type>.*?) list '
                 r'in expanded "(?P<panel>.+?)" Onezone panel'))
def is_present_in_panel_list(selenium, browser_id, items,
                             item_type, panel, tmp_memory):
    driver = select_browser(selenium, browser_id)
    items = tmp_memory[browser_id]['gen_str'] if items == 'new item' else items
    Wait(driver, WAIT_BACKEND).until_not(
        lambda d: _not_in_panel_list(driver, panel, item_type, items),
        message='checking for presence of {items} on {list} list'
                ''.format(items=items, list=item_type)
    )










def _get_icon_and_home_icon_of_item_from_list(driver, panel,
                                              item_name, item_type):
    return Wait(driver, WAIT_FRONTEND).until(
        lambda d: _get_items_from_panel_list(driver, panel,
                                             item_type).get(item_name, None),
        message='searching for {} on {} list in expanded {} Onezone panel'
                ''.format(item_name, item_type, panel)
    ).find_element_by_css_selector('.oneicon-{}, .oneicon-home'
                                   ''.format(item_type))


@when(parsers.re('user of (?P<browser_id>.+?) can (?P<action>set|unset) '
                 '(?P<item_name>.+?) from (?P<item_type>.+?)s list in '
                 'expanded "(?P<panel>.+?)" Onezone panel '
                 '(as|from) home (?P=item_type)'))
@then(parsers.re('user of (?P<browser_id>.+?) can (?P<action>set|unset) '
                 '(?P<item_name>.+?) from (?P<item_type>.+?)s list in '
                 'expanded "(?P<panel>.+?)" Onezone panel '
                 '(as|from) home (?P=item_type)'))
def set_or_unset_item_to_home_item(selenium, browser_id, action,
                                   item_name, item_type, panel):
    driver = select_browser(selenium, browser_id)
    item_type_icon, home = _get_icon_and_home_icon_of_item_from_list(driver, panel,
                                                                     item_name, item_type)

    if action == 'set' and 'home-outline' in home_icon and 'home' \
            or action == 'unset' and 'home-outline' not in home_icon:
        home.click()


@when(parsers.re('user of (?P<browser_id>.+?) sees (?P<item_name>.+?) '
                 'from (?P<item_type>.+?)s list in expanded "(?P<panel>.+?)" '
                 'Onezone panel as home (?P=item_type)'))
@then(parsers.re('user of (?P<browser_id>.+?) sees (?P<item_name>.+?) '
                 'from (?P<item_type>.+?)s list in expanded "(?P<panel>.+?)" '
                 'Onezone panel as home (?P=item_type)'))
def is_item_home_item(selenium, browser_id, item_name, item_type, panel):
    driver = select_browser(selenium, browser_id)
    item = Wait(driver, WAIT_FRONTEND).until(
        lambda d: _get_items_from_panel_list(driver, panel,
                                             item_type).get(item_name, None),
        message='searching for {} on {} list in expanded {} Onezone panel'
                ''.format(item_name, item_type, panel)
    )
    home = item.find_element_by_css_selector('.oneicon-home')
    assert 'home-outline' not in home.get_attribute('class')


@when(parsers.re('user of (?P<browser_id>.+?) does not see (?P<item_name>.+?) '
                 'from (?P<item_type>.+?)s list in expanded "(?P<panel>.+?)" '
                 'Onezone panel as home (?P=item_type)'))
@then(parsers.re('user of (?P<browser_id>.+?) does not see (?P<item_name>.+?) '
                 'from (?P<item_type>.+?)s list in expanded "(?P<panel>.+?)" '
                 'Onezone panel as home (?P=item_type)'))
def not_is_item_home_item(selenium, browser_id, item_name, item_type, panel):
    driver = select_browser(selenium, browser_id)
    item = Wait(driver, WAIT_FRONTEND).until(
        lambda d: _get_items_from_panel_list(driver, panel,
                                             item_type).get(item_name, None),
        message='searching for {} on {} list in expanded {} Onezone panel'
                ''.format(item_name, item_type, panel)
    )
    home = item.find_element_by_css_selector('.oneicon-home')
    assert 'home-outline' in home.get_attribute('class')
