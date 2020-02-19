import pytest
from mock import patch

import game
from game.board import Board


class TestBoard:
    board = Board(3)

    def setup_method(self):
        self.board = Board(3)

    def test_move_success(self):
        self.board.move(1, 1, 1)
        assert True

    def test_move_failure(self):
        with pytest.raises(Exception) as e:
            self.board.move(1, 4, 1)
        assert str(e.value) == "invalid move"

    def test_is_solved_true(self):
        is_solved = self.board.is_solved()
        assert is_solved is False

    def test_is_solve_false(self):
        self.board.move(0, 0, 1)
        self.board.move(0, 1, 1)
        self.board.move(0, 2, 1)
        is_solved = self.board.is_solved()
        assert is_solved is True

    def test_draw_empty_board(self):
        self.board.draw()
        assert True

    def test_draw_filled_board(self):
        self.board.move(1, 1, 1)
        self.board.draw()
        assert True

    @patch("game.board.Board.draw")
    @patch("game.board.Board.move")
    @patch("game.board.Board.is_solved")
    @patch("builtins.input")
    def test_start_game_success(self, input, solved, move, draw):
        move.return_value = None
        draw.return_value = None
        input.side_effect = ["1 1", "2 1", "2 2", "1 2", "3 3"]
        solved.side_effect = [False, False, False, False, True]
        self.board.start_game(2)
        assert True

    @patch("game.board.Board.draw")
    @patch("game.board.Board.move")
    @patch("game.board.Board.is_solved")
    @patch("builtins.input")
    def test_start_game_move_failure_and_match_drawn(self, input, solved, move, draw):
        draw.return_value = None
        move.side_effect = [None, Exception("invalid move"), None, None, None, None, None, None, None, None]
        input.side_effect = ["1 1", "1 1", "2 1", "2 2", "1 2", "3 1", "3 3", "3 2", "1 3", "2 3"]
        solved.side_effect = [False, False, False, False, False, False, False, False, False]
        self.board.start_game(2)
        assert True

    @patch("game.board.Board.draw")
    @patch("game.board.Board.start_game")
    @patch("builtins.input")
    def test_play_success(self, input, start_game, draw):
        draw.return_value = None
        start_game.return_value = None
        input.side_effect = ['3', '5']
        # game.input = lambda: '1'
        game.play()
        game.play()
        assert True
        # game.input = input
