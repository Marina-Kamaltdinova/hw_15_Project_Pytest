import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(1280, 720), (1920, 1080), (2560, 1440)],
                ids=['1280', '1920', '2560'])
def browser_desktop(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(414, 896), (360, 740), (480, 854)],
                ids=['414', '360', '480'])
def browser_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1280, 720), (1920, 1080), (414, 896), (480, 854)],
                ids=['1280', '1920', '414', '480'])
def browser_config(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width >= 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
