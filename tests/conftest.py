import pytest

from hookup import Hookup


@pytest.fixture(scope="function")
def fixture_hookup_class():
    @Hookup(attrs=["hooked_up", "uninitialised"], callback="first_callback")
    @Hookup(attrs=["hooked_up"], callback="second_callback")
    class HookupClass:
        def __init__(self):
            self.hooked_up = None
            self.not_hooked_up = None

            # Callback calls are tracked directly on the fixture
            # If we mock the callback, Hotwire doesn't call the mock
            self.first_callback_count = 0
            self.second_callback_count = 0

        def first_callback(self):
            self.first_callback_count += 1

        def second_callback(self):
            self.second_callback_count += 1

    return HookupClass()
