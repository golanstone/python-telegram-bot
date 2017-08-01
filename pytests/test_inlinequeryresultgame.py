#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import json

import pytest

from telegram import (InlineKeyboardButton, InlineQueryResultGame,
                      InlineQueryResultVoice, InlineKeyboardMarkup)


@pytest.fixture(scope='class')
def inline_query_result_game():
    return InlineQueryResultGame(TestInlineQueryResultGame.id,
                                 TestInlineQueryResultGame.game_short_name,
                                 reply_markup=TestInlineQueryResultGame.reply_markup)


class TestInlineQueryResultGame:
    id = 'id'
    type = 'game'
    game_short_name = 'game short name'
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('reply_markup')]])

    def test_expected_values(self, inline_query_result_game):
        assert inline_query_result_game.type == self.type
        assert inline_query_result_game.id == self.id
        assert inline_query_result_game.game_short_name == self.game_short_name
        assert inline_query_result_game.reply_markup.to_dict() == \
               self.reply_markup.to_dict()

    def test_to_json(self, inline_query_result_game):
        json.loads(inline_query_result_game.to_json())

    def test_to_dict(self, inline_query_result_game):
        inline_query_result_game_dict = inline_query_result_game.to_dict()

        assert isinstance(inline_query_result_game_dict, dict)
        assert inline_query_result_game_dict['type'] == self.type
        assert inline_query_result_game_dict['id'] == self.id
        assert inline_query_result_game_dict['game_short_name'] == self.game_short_name
        assert inline_query_result_game_dict['reply_markup'] == \
               self.reply_markup.to_dict()

    def test_equality(self):
        a = InlineQueryResultGame(self.id, self.game_short_name)
        b = InlineQueryResultGame(self.id, self.game_short_name)
        c = InlineQueryResultGame(self.id, "")
        d = InlineQueryResultGame("", self.game_short_name)
        e = InlineQueryResultVoice(self.id, "", "")

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a == c
        assert hash(a) == hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
