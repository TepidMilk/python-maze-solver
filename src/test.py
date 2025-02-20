import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_many_cells(self):
        num_cols = 1000
        num_rows = 1000
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2._create_cells()
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )
    
    def test_maze_invalid_maze_size(self):
        num_cols = -12
        num_rows = -10
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        with self.assertRaises(Exception):
            m3._create_cells()
    
    def test_maze_invalid_cell_size(self):
        num_cols = 12
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 0, 0)
        with self.assertRaises(Exception):
            m4._create_cells()

    def test_maze_reset_method(self):
        num_cols = 12
        num_rows = 10
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m5._create_cells()
        m5._break_walls_r(0,0)
        m5._reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m5._cells[i][j].visited, False)
        
    def test_empty_maze_reset(self):
        m6 = Maze(0, 0, 0, 0, 10, 10)
        m6._reset_cells_visited()

        

if __name__ == "__main__":
    unittest.main()