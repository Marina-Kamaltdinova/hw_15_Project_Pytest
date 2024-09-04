from selene import browser, be
import pytest


def test_github_desktop(browser_config):
    if browser_config == 'mobile':
        pytest.skip(reason='Разрешение экрана для телефона')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


def test_github_mobile(browser_config):
    if browser_config == 'desktop':
        pytest.skip(reason='Разрешение экрана для компьютера')
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
