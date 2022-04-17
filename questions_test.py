import unittest
import questions as q


class TestQuestions(unittest.TestCase):

    def test_check_company_dates(self):
        first_exp = {
            "start": "2017-01-01",
            "end": None
            }
        second_exp = {
            "start": "2020-01-01",
            "end": None
        }
        third_exp = {
            "start": "2022-01-01",
            "end": None
        }
        fourth_exp = {
            "start": "2008-01-01",
            "end": "2016-01-01"
        }

        results1 = q.check_company_dates(first_exp, second_exp) # overlap and min 6 months
        results2 = q.check_company_dates(first_exp, third_exp) # third_exp is less than 6 months
        results3 = q.check_company_dates(first_exp, fourth_exp) # fourth_exp is out of range of first_exp
        results4 = q.check_company_dates(second_exp, third_exp) #third_exp is less than 6 months
        results5 = q.check_company_dates(second_exp, fourth_exp) #fourth_exp is out of range of second_exp
        results6 = q.check_company_dates(third_exp, fourth_exp) #fourth_exp is out of range of third_exp
        self.assertEqual(results1, True)
        self.assertEqual(results2, False)
        self.assertEqual(results3, False)
        self.assertEqual(results4, False)
        self.assertEqual(results5, False)
        self.assertEqual(results6, False)

    def test_get_connected_company_people(self):
        results0 = q.get_connected_people('./persons.json', 0 , None, "company")
        results1 = q.get_connected_people('./persons.json', 1, None, "company")
        results2 = q.get_connected_people('./persons.json', 2, None, "company")
        results3 = q.get_connected_people('./persons.json', 3, None, "company")
        results4 = q.get_connected_people('./persons.json', 4, None, "company")
        results5 = q.get_connected_people('./persons.json', 5, None, "company")
        results6 = q.get_connected_people('./persons.json', 6, None, "company")
        results7 = q.get_connected_people('./persons.json', 7, None, "company")
        results8 = q.get_connected_people('./persons.json', 8, None, "company")
        results9 = q.get_connected_people('./persons.json', 9, None, "company")
        results10 = q.get_connected_people('./persons.json', 10, None, "company")
        self.assertEqual(results0, [1, 8]) # 0 is connected to 1 and 8
        self.assertEqual(results1, [0]) # 1 is connected to 0
        self.assertEqual(results2, []) # 2 is not connected to anyone
        self.assertEqual(results3, [7]) # 3 is connected to 7
        self.assertEqual(results4, []) # 4 is not connected to anyone
        self.assertEqual(results5, [6, 7]) # 5 is connected to 6 and 7
        self.assertEqual(results6, [5, 7]) # 6 is connected to 5 and 7
        self.assertEqual(results7, [3, 5, 6]) # 7 is connected to 3, 5 and 6
        self.assertEqual(results8, [0]) # 8 is connected to 0
        self.assertEqual(results9, [10]) # 9 is connected to 10
        self.assertEqual(results10, [9]) # 10 is connected to 9
    
    def test_normalize_phone(self):
        results0 = q.normalize_phone('(123) 456-7890')
        results1 = q.normalize_phone('+11234567891')
        results2 = q.normalize_phone('11234567891')
        results3 = q.normalize_phone('1-1234567800')
        self.assertEqual(results0, '1-1234567890')
        self.assertEqual(results1, '1-1234567891')
        self.assertEqual(results2, '1-1234567891')
        self.assertEqual(results3, '1-1234567800')

    def test_get_contact_connected_people(self):
        results0 = q.get_connected_people('./persons.json', 5, './contacts.json', "contact")
        results1 = q.get_connected_people('./persons.json', 6, './contacts.json', "contact")
        results2 = q.get_connected_people('./persons.json', 2, './contacts.json', "contact")
        self.assertEqual(results0, [10, 0]) # 0 is not connected to anyone
        self.assertEqual(results1, [0]) # 1 is not connected to anyone
        self.assertEqual(results2, []) # 2 is not connected to anyone

    def test_get_total_connected_people(self):
        results0 = q.get_connected_people('./persons.json', 5, './contacts.json', "both")
        results1 = q.get_connected_people('./persons.json', 6, './contacts.json', "both")
        self.assertEqual(results0, [0, 6, 7, 10]) # 0 is connected to results from persons list and contacts list
        self.assertEqual(results1, [0, 5,7]) # 1 is connected to results from persons list and contacts list
        

if __name__ == '__main__':
    unittest.main()