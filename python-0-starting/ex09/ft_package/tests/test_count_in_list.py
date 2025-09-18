import unittest
from ft_package import count_in_list


class TestCountInList(unittest.TestCase):
    '''Test cases for count_in_list function'''

    def test_count(self):
        '''Existing tests'''
        subject_list = ['toto', 'tata', 'toto']
        self.assertEqual(count_in_list(subject_list, 'toto'), 2)
        self.assertEqual(count_in_list(subject_list, 'tutu'), 0)
        self.assertEqual(count_in_list(subject_list, 'tata'), 1)

    def test_empty_list(self):
        '''Test with empty list'''
        empty_list = []
        self.assertEqual(count_in_list(empty_list, 'toto'), 0)
        self.assertEqual(count_in_list(empty_list, ''), 0)

    def test_single_element_list(self):
        '''Test with list containing one element'''
        single_list = ['toto']
        self.assertEqual(count_in_list(single_list, 'toto'), 1)
        self.assertEqual(count_in_list(single_list, 'tata'), 0)

    def test_all_same_elements(self):
        '''Test with list where all elements are the same'''
        same_list = ['toto', 'toto', 'toto']
        self.assertEqual(count_in_list(same_list, 'toto'), 3)
        self.assertEqual(count_in_list(same_list, 'tata'), 0)

    def test_no_occurrences(self):
        '''Test with no occurrences of the element'''
        no_match_list = ['a', 'b', 'c']
        self.assertEqual(count_in_list(no_match_list, 'd'), 0)

    def test_with_integers(self):
        '''Test with integer list (since function is generic)'''
        int_list = [1, 2, 2, 3, 2]
        self.assertEqual(count_in_list(int_list, 2), 3)
        self.assertEqual(count_in_list(int_list, 4), 0)

    def test_with_mixed_types(self):
        '''Test with mixed types
        (though TypeVar suggests homogeneous, but test robustness)'''
        mixed_list = ['toto', 1, 'toto', 1]
        self.assertEqual(count_in_list(mixed_list, 'toto'), 2)
        self.assertEqual(count_in_list(mixed_list, 1), 2)
        self.assertEqual(count_in_list(mixed_list, 'tata'), 0)

    def test_with_none(self):
        '''Test with None values'''
        none_list = [None, 'toto', None]
        self.assertEqual(count_in_list(none_list, None), 2)
        self.assertEqual(count_in_list(none_list, 'toto'), 1)

    def test_case_sensitivity(self):
        '''Test case sensitivity for strings'''
        case_list = ['Toto', 'toto', 'TOTO']
        self.assertEqual(count_in_list(case_list, 'toto'), 1)
        self.assertEqual(count_in_list(case_list, 'Toto'), 1)
        self.assertEqual(count_in_list(case_list, 'TOTO'), 1)


if __name__ == '__main__':
    unittest.main()
