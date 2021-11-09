import pytest

from hookup import Hookup


@pytest.fixture(scope="function")
def fixture_hookup_class():
    @Hookup(attrs=["hooked_up", "uninitialised"], callback="my_callback")
    class HookupClass:
        def __init__(self):
            self.hooked_up = None
            self.not_hooked_up = None

            # Callback calls are tracked directly on the fixture
            # If we mock the callback, Hotwire doesn't call the mock
            self.callback_count = 0

        def my_callback(self):
            self.callback_count += 1

    return HookupClass()
