import unittest
import unittest.mock
import asyncio
import Tethys
from typing import List


class MockGuild(object):
    def __init__(self):
        self.channels = []


class MockChannel(object):
    def __init__(self):
        self.name = ""
        self.id = -1
        self.send_count = 0
        self.send_data: List() = []

    async def send(self, args, **kwargs):
        self.send_count = self.send_count + 1
        self.send_data.append(args)


class TestTethysCore(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_getting_join_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs"
        tc5.id = 4

        tc6 = MockChannel()
        tc6.name = "tethys-logs"
        tc6.id = 5

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_join_leave_log_channel(mockGuild)
        self.assertTrue(log_channel.id == tc4.id)

    def test_getting_edit_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs"
        tc5.id = 5

        tc6 = MockChannel()
        tc6.name = "tethys-logs"
        tc6.id = 6

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_edit_delete_log_channel(mockGuild)
        self.assertTrue(log_channel.id == tc5.id)

    def test_getting_default_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs"
        tc5.id = 5

        tc6 = MockChannel()
        tc6.name = "tethys-logs"
        tc6.id = 6

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_default_log_channel(mockGuild)
        self.assertTrue(log_channel.id == tc6.id)

    def test_getting_fallback_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        tc0 = MockChannel()
        tc0.name = "fallback"
        tc0.id = 101

        testTethys.get_channel = unittest.mock.MagicMock(return_value=tc0)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs"
        tc5.id = 5

        tc6 = MockChannel()
        tc6.name = "tethys-logs-isnt-here"
        tc6.id = 6

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_default_log_channel(mockGuild)
        self.assertTrue(log_channel.id == int(testConfig["log_channel"]))
        testTethys.get_channel.assert_called_with(101)

    def test_getting_default_via_join_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs-not-here"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs"
        tc5.id = 4

        tc6 = MockChannel()
        tc6.name = "tethys-logs"
        tc6.id = 5

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_join_leave_log_channel(mockGuild)
        self.assertTrue(log_channel.id == tc6.id)

    def test_getting_default_via_edit_log_channel(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        mockGuild = MockGuild()
        tc1 = MockChannel()
        tc1.name = "test1"
        tc1.id = 1

        tc2 = MockChannel()
        tc2.name = "test2"
        tc2.id = 2

        tc3 = MockChannel()
        tc3.name = "test3"
        tc3.id = 3

        tc4 = MockChannel()
        tc4.name = "join-leave-logs"
        tc4.id = 4

        tc5 = MockChannel()
        tc5.name = "edit-delete-logs-not-here"
        tc5.id = 5

        tc6 = MockChannel()
        tc6.name = "tethys-logs"
        tc6.id = 6

        mockGuild.channels = [
            tc1, tc2, tc3, tc4, tc5, tc6
        ]

        log_channel = testTethys.get_edit_delete_log_channel(mockGuild)
        self.assertTrue(log_channel.id == tc6.id)

    def test_on_ready(self):
        testConfig = {"log_channel": 101}
        testTethys = Tethys.Tethys(testConfig)

        tc0 = MockChannel()
        tc0.name = "fallback"
        tc0.id = 101

        testTethys.get_channel = unittest.mock.Mock(return_value=tc0)
        testTethys.change_presence = unittest.mock.Mock(return_value=asyncio.Future())
        testTethys.change_presence.return_value.set_result(None)
        testTethys.application_info = unittest.mock.Mock(return_value=asyncio.Future())
        testTethys.application_info.return_value.set_result(tc0)

        self.loop.run_until_complete(testTethys.on_ready())

        self.assertEqual(tc0.send_count, 2)
        self.assertIn("Tethys has just started up", tc0.send_data)
        self.assertIn("https://discordapp.com/api/oauth2/authorize?client_id=101&permissions=0&scope=bot", tc0.send_data)
