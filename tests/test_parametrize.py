from selene import browser, be
import pytest

desktop_only = pytest.mark.parametrize('browser_config', [(1280, 720), (1920, 1080)], indirect=True,
                                       ids=['1280', '1920'])
mobile_only = pytest.mark.parametrize('browser_config', [(414, 896), (480, 854)], indirect=True,
                                      ids=['414', '480'])


@desktop_only
def test_github_desktop(browser_config):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@mobile_only
def test_github_mobile(browser_config):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
