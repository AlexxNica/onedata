"""Utils and fixtures to facilitate operations on
common operations between various services.
"""

from abc import ABCMeta, abstractmethod

from tests.gui.utils.core.web_elements import WebItemsSequence, Label, WebElement
from tests.gui.utils.core.web_objects import ButtonWithTextPageObject
from tests.gui.utils.core.base import PageObject

from tests.gui.utils.generic import find_web_elem


__author__ = "Bartosz Walkowicz"
__copyright__ = "Copyright (C) 2017 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"


class OnePage(object):
    __metaclass__ = ABCMeta

    opened_tab = Label('#main-menu-container ul.main-menu '
                       'li.main-menu-item.active')
    main_menu = WebItemsSequence('#main-menu-container ul.main-menu '
                                 'li.main-menu-item',
                                 cls=ButtonWithTextPageObject)

    def __init__(self, driver):
        self.driver = self.web_elem = driver

    @abstractmethod
    def __str__(self):
        pass


class Sidebar(PageObject):
    title = Label('.col-title')

    def __str__(self):
        return '{} sidebar in {}'.format(self.title, self.parent)


class SidebarRecord(PageObject):
    @property
    def _content(self):
        return find_web_elem(self.driver, '.col-content',
                             lambda: '{} not found'.format(self))


class Toggle(PageObject):
    _lock = WebElement('.one-way-toggle-readonly-icon')

    def __str__(self):
        return 'toggle switch in {}'.format(self.parent)

    def is_checked(self):
        return self.web_elem.find_element_by_css_selector('input').is_selected()

    def check(self):
        if not self.is_checked():
            self.click()

    def uncheck(self):
        if self.is_checked():
            self.click()

    def is_enabled(self):
        try:
            self._lock
        except RuntimeError:
            return True
        else:
            return False