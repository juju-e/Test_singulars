import unittest
import compute_singular
class singular_matrix(unittest.TestCase):

    def test_singular_matrix(self):
       self.assertTrue (compute_singular.is_singular([[1,2],[-2,-4]]))
       self.assertTrue (compute_singular.is_singular([[-3,-1,-3],[3,2,3],[2,1,2]]))
       self.assertTrue (compute_singular.is_singular([[3,6],[2,4]]))
    def test_non_singular_matrix(self):
       self.assertFalse(compute_singular.is_singular([[5,5,9,7,0,7],[3,8, 6 ,4 ,3 ,9],[5, 2 ,5, 3, 0, 9],[0 ,3, 7, 7 ,4, 9],[5 ,3 ,8, 6, 7 ,2],[8 ,1 ,7 ,3 ,9 ,9]]))
       self.assertFalse(compute_singular.is_singular([[29 ,32 ,20 ,53],[83 ,123 ,120 ,33],[15 ,54 ,104 ,68],[96 ,107 ,104 ,20]]))
       self.assertFalse(compute_singular.is_singular([[105 ,124 ,4 ,54 ,69],[88 ,67 ,94 ,105 ,100],[78 ,53 ,28 ,6 ,19],[41 ,109 ,96 ,110 ,7],[23 ,116 ,114 ,9 ,10]]))
       self.assertFalse(compute_singular.is_singular([[3, 0, 0],[2, 1, 4],[1, 0, 5]]))
if __name__ == "__main__":
    unittest.main()
