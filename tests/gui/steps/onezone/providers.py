"""Steps for GO TO YOUR FILES panel and provider popup features of Onezone page.
"""

from pytest_bdd import parsers, when, then
from pytest_selenium_multi.pytest_selenium_multi import select_browser

from tests.gui.conftest import WAIT_BACKEND, SELENIUM_IMPLICIT_WAIT
from tests.gui.utils.generic import repeat_failed, implicit_wait

__author__ = "Bartosz Walkowicz"
__copyright__ = "Copyright (C) 2016 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"


@when(parsers.parse('user of {browser_id} sees that provider popup for provider '
                    'named "{provider}" has appeared on world map'))
@then(parsers.parse('user of {browser_id} sees that provider popup for provider '
                    'named "{provider}" has appeared on world map'))
def assert_provider_popup_has_appeared_on_map(selenium, browser_id,
                                              provider, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND, timeout=True)
    def assert_popup_appeared(d, provider_name):
        prov = oz_page(d)['world map'].get_provider_with_displayed_panel()
        err_msg = 'Popup displayed for provider named "{}" ' \
                  'instead of "{}"'.format(prov.name, provider_name)
        assert provider_name == prov.name, err_msg

    assert_popup_appeared(driver, provider)


@when(parsers.re(r'user of (?P<browser_id>.+?) clicks on the '
                 r'"(?P<btn>Go to your files|copy hostname)" button in '
                 r'"(?P<provider>.+?)" provider\'s popup displayed on world map'))
@then(parsers.re(r'user of (?P<browser_id>.+?) clicks on the '
                 r'"(?P<btn>Go to your files|copy hostname)" button in '
                 r'"(?P<provider>.+?)" provider\'s popup displayed on world map'))
def click_on_btn_in_provider_popup(selenium, browser_id, btn, provider, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND, timeout=True)
    def click_on_btn(d, provider_name):
        prov = oz_page(d)['world map'].get_provider_with_displayed_panel()
        err_msg = 'Popup displayed for provider named "{}" ' \
                  'instead of "{}"'.format(prov.name, provider_name)
        assert provider_name == prov.name, err_msg
        action = getattr(prov, btn.lower().replace(' ', '_'))
        action()

    click_on_btn(driver, provider)


@when(parsers.re(r'user of {browser_id} unsets provider named "{provider}" '
                 r'from home by clicking on home icon in that provider '
                 r'record in expanded "GO TO YOUR FILES" Onezone panel'))
@then(parsers.re(r'user of {browser_id} unsets provider named "{provider}" '
                 r'from home by clicking on home icon in that provider '
                 r'record in expanded "GO TO YOUR FILES" Onezone panel'))
def unset_given_item_from_home_by_clicking_on_home_icon(selenium, browser_id,
                                                        provider, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND, timeout=True)
    def set_as_home(d, item):
        item_record = oz_page(d)['go to your files'][item]
        item_record.unset_from_home()

    with implicit_wait(driver, 0.2, SELENIUM_IMPLICIT_WAIT):
        set_as_home(driver, provider)


@when(parsers.re(r'user of (?P<browser_id>.+?) sees that there is no '
                 r'displayed provider popup next to '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map'))
@then(parsers.re(r'user of (?P<browser_id>.+?) sees that there is no '
                 r'displayed provider popup next to '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map'))
@when(parsers.re(r'user of (?P<browser_id>.+?) sees that provider popup next to '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map has disappeared'))
@then(parsers.re(r'user of (?P<browser_id>.+?) sees that provider popup next to '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map has disappeared'))
def assert_no_provider_popup_next_to_provider_circle(selenium, browser_id,
                                                     ordinal, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND)
    def assert_not_displayed(d, index):
        world_map = oz_page(d)['world map']
        provider = world_map[index]
        err_msg = 'provider popup for {} circle is displayed ' \
                  'while it should not be'.format(ordinal)
        assert not provider.is_displayed, err_msg

    with implicit_wait(driver, 0.2, SELENIUM_IMPLICIT_WAIT):
        assert_not_displayed(driver, int(ordinal[:-2]) - 1)


@when(parsers.re(r'user of (?P<browser_id>.+?) clicks on '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map'))
@then(parsers.re(r'user of (?P<browser_id>.+?) clicks on '
                 r'(?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|\d*?11th|'
                 r'\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|\d*?[^1]3rd) '
                 r'provider circle on Onezone world map'))
def click_on_provider_circle(selenium, browser_id, ordinal, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND)
    def click_on_provider(d, index):
        world_map = oz_page(d)['world map']
        provider = world_map[index]
        provider.click()

    click_on_provider(driver, int(ordinal[:-2]) - 1)


@when(parsers.re(r'user of (?P<browser_id>.+?) sees that provider popup has '
                 r'appeared next to (?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|'
                 r'\d*?11th|\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|'
                 r'\d*?[^1]3rd) provider circle on Onezone world map'))
@then(parsers.re(r'user of (?P<browser_id>.+?) sees that provider popup has '
                 r'appeared next to (?P<ordinal>1st|2nd|3rd|\d*?[4567890]th|'
                 r'\d*?11th|\d*?12th|\d*?13th|\d*?[^1]1st|\d*?[^1]2nd|'
                 r'\d*?[^1]3rd) provider circle on Onezone world map'))
def assert_provider_popup_next_to_provider_circle(selenium, browser_id,
                                                  ordinal, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND)
    def assert_provider_popup(d, index):
        world_map = oz_page(d)['world map']
        provider = world_map[index]
        err_msg = 'provider popup for {} circle is not displayed ' \
                  'while it should be'.format(ordinal)
        assert provider.is_displayed, err_msg

    with implicit_wait(driver, 0.2, SELENIUM_IMPLICIT_WAIT):
        assert_provider_popup(driver, int(ordinal[:-2]) - 1)


@when(parsers.parse('user of {browser_id} clicks on Onezone world map'))
@then(parsers.parse('user of {browser_id} clicks on Onezone world map'))
def click_on_world_map(selenium, browser_id, oz_page):
    driver = select_browser(selenium, browser_id)

    @repeat_failed(attempts=WAIT_BACKEND)
    def click_on_map(d):
        world_map = oz_page(d)['world map']
        world_map.click()

    click_on_map(driver)
