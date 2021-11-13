class TestHookup:
    def test_import_lowercase(self):
        """
        Hookup supports importing by name Hookup or lowercase hookup
        """
        from hookup import hookup  # noqa: F401

    def test_change_target_attribute(self, fixture_hookup_class):
        """
        Callbacks should be triggered when a Hooked up attribute is changed value
        """
        initial_callback_count = fixture_hookup_class.callback_count

        # Set the initial value for hooked_up from None to "something"
        # This should NOT trigger a callback
        fixture_hookup_class.hooked_up = "something"
        assert fixture_hookup_class.callback_count == initial_callback_count

        # Change the value of hooked_up from "something" to "changed"
        # This SHOULD trigger a callback
        fixture_hookup_class.hooked_up = "changed"
        assert fixture_hookup_class.callback_count == initial_callback_count + 1

    def test_change_target_uninitialised_attribute(self, fixture_hookup_class):
        """
        Hookup should be able to manage attributes that are not initialised at object instantiation
        """
        initial_callback_count = fixture_hookup_class.callback_count

        fixture_hookup_class.uninitialised = "something"
        fixture_hookup_class.uninitialised = "changed"
        assert fixture_hookup_class.callback_count == initial_callback_count + 1

    def test_change_other_attribute(self, fixture_hookup_class):
        """
        Callbacks should not be called when a non-hooked-up attribute is changed
        """
        initial_callback_count = fixture_hookup_class.callback_count

        fixture_hookup_class.not_hooked_up = "something"
        fixture_hookup_class.not_hooked_up = "changed"
        assert fixture_hookup_class.callback_count == initial_callback_count

    def test_callback_not_exists(self, fixture_hookup_class):
        pass
