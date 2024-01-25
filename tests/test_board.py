import unittest

from rookpoly import Board
from rookpoly.polynomial import Polynomial


class TestBoard(unittest.TestCase):
    empty_boards_limit = 7

    def setUp(self):
        self.empty_boards = [Board(['0' * i for _ in range(i)]) for i in range(self.empty_boards_limit)]
        self.board_global_1 = Board(["110", "100", "000", "001"])
        self.board_global_2 = Board(["00111", "00111", "11100", "11100", "11000"])

    def test_init(self):
        # Testowanie poprawnej inicjalizacji planszy
        board = Board(["100", "010"])
        self.assertEqual(board.n, 2)
        self.assertEqual(board.m, 3)

    def test_n(self):
        # Testowanie właściwości n, zwracającej liczbę wierszy
        self.assertEqual(self.board_global_1.n, 4)
        self.assertEqual(self.board_global_2.n, 5)

    def test_m(self):
        # Testowanie właściwości m, zwracającej liczbę kolumn
        self.assertEqual(self.board_global_1.m, 3)
        self.assertEqual(self.board_global_2.m, 5)

    def test_flip(self):
        # Testowanie odwracania planszy
        board = Board(["100", "010", "001"])
        board.flip()
        self.assertEqual(board, Board(["001", "010", "100"]))

    def test_rotate(self):
        # Testowanie rotacji planszy
        for (i, board) in enumerate(self.empty_boards):
            board.rotate()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_global_1.rotate()
        self.assertEqual(self.board_global_1, ["0011", "0001", "1000"])

        self.board_global_2.rotate()
        self.assertEqual(self.board_global_2, ["11100", "11100", "01111", "00011", "00011"])

    def test_rtrim(self):
        # Testowanie przycinania pustych miejsc po prawej stronie planszy
        for (i, board) in enumerate(self.empty_boards):
            board.rtrim()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_global_1.rtrim()
        self.assertEqual(self.board_global_1, ["110", "100", "000", "001"])

        self.board_global_2.rtrim()
        self.assertEqual(self.board_global_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_remove_filled_rows(self):
        # Testowanie usuwania wypełnionych wierszy z planszy
        board = Board(["111", "000", "010"])
        board.remove_filled_rows()
        self.assertEqual(board, Board(["000", "010"]))

    def test_simplify(self):
        # Testowanie uproszczenia planszy
        for (i, board) in enumerate(self.empty_boards):
            board.simplify()
            self.assertEqual(board, ['0' * i for _ in range(i)])

        self.board_global_1.simplify()
        self.assertEqual(self.board_global_1, ["0011", "0001", "1000"])

        self.board_global_2.simplify()
        self.assertEqual(self.board_global_2, ["00111", "00111", "11100", "11100", "11000"])

    def test_get_empty_squares(self):
        # Testowanie identyfikacji pustych kwadratów na planszy
        board = Board(["100", "001", "010"])
        empty_squares = list(board.get_empty_squares())
        self.assertEqual(empty_squares, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)])

    def test_get_set(self):
        # Testowanie odczytu i zapisu wartości w komórkach planszy
        board = Board(["000", "000", "000"])
        board.set(1, 1, '1')
        self.assertEqual(board.get(1, 1), '1')

    def test_is_valid_cut_column(self):
        # Testowanie, czy kolumna może być przecięta
        board = Board(["1001", "1111", "1001"])
        self.assertTrue(board.is_valid_cut_column(1))
        self.assertFalse(board.is_valid_cut_column(2))

    def test_get_cuttable_columns(self):
        # Testowanie identyfikacji kolumn, które mogą być przecięte
        board = Board(["1001", "1111", "1001"])
        cuttable_columns = list(board.get_cuttable_columns())
        self.assertEqual(cuttable_columns, [1, 3])

    def test_cut_columns(self):
        # Testowanie przycinania kolumn z planszy
        board = Board(["100", "110", "100"])
        sub_boards = list(board.cut_columns())
        self.assertEqual(len(sub_boards), 2)
        self.assertEqual(sub_boards[0], Board(["1", "1", "1"]))
        self.assertEqual(sub_boards[1], Board(["00", "10", "00"]))

    def test_get_sub_board(self):
        # Testowanie pobierania podplanszy
        self.assertEqual(self.board_global_1.get_sub_board(2, 0, 4, 3), ["000", "001"])

    def test_get_poly(self):
        # Testowanie generowania wielomianu na podstawie planszy
        self.assertEqual(self.empty_boards[0].get_poly(), Polynomial(1))
        self.assertEqual(self.empty_boards[1].get_poly(), Polynomial(1, 1))
        self.assertEqual(self.empty_boards[2].get_poly(), Polynomial(1, 4, 2))
        self.assertEqual(self.empty_boards[3].get_poly(), Polynomial(1, 9, 18, 6))
        self.assertEqual(self.empty_boards[4].get_poly(), Polynomial(1, 16, 72, 96, 24))
        self.assertEqual(self.empty_boards[5].get_poly(), Polynomial(1, 25, 200, 600, 600, 120))
        self.assertEqual(self.empty_boards[6].get_poly(), Polynomial(1, 36, 450, 2400, 5400, 4320, 720))
        self.assertEqual(self.board_global_1.get_poly(), Polynomial(1, 8, 16, 7))
        self.assertEqual(self.board_global_2.get_poly(), Polynomial(1, 11, 40, 56, 28, 4))

    def test_eq(self):
        # Testowanie porównywania dwóch plansz
        board_1 = Board(["100", "010", "001"])
        board_2 = Board(["100", "010", "001"])
        board_3 = Board(["101", "010", "001"])
        self.assertTrue(board_1 == board_2)
        self.assertFalse(board_1 == board_3)

    def test_repr_str(self):
        # Testowanie reprezentacji stringowej obiektu
        board = Board(["100", "010", "001"])
        self.assertEqual(repr(board), "[['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]")
        self.assertEqual(str(board), "100\n010\n001")


if __name__ == '__main__':
    unittest.main()
