import unittest
import csvCombiner
import pyexcel as pe

class Test(unittest.TestCase):

    def test_fileNotExist_error(self):
        self.assertRaises(Exception, csvCombiner.merge_csv(['./fixtures/accessories.csv', '32.csv', 'test.csv']))
        self.assertRaises(Exception, csvCombiner.merge_csv(['./dsaaaas.csv', 'sadawdsaasd.csv', 'test.csv']))
        self.assertRaises(Exception, csvCombiner.merge_csv(['./accessories.csv', '32.csv']))

    def test_NotCsvError(self):
        with self.assertRaises(Exception) as context:
            csvCombiner.merge_csv(['./fixtures/accessories.csv', './fixtures/clothing.txt', 'test.csv'])
        self.assertTrue("Input and output must be CSV file" in str(context.exception))

        with self.assertRaises(Exception) as context:
            csvCombiner.merge_csv(['./fixtures/accessories.csv', '.csv', 'test.csv'])
        self.assertTrue("Input and output must be CSV file" in str(context.exception))

        with self.assertRaises(Exception) as context:
            csvCombiner.merge_csv(['./fixtures/accessories.csv', '', 'test.csv'])
        self.assertTrue("Input and output must be CSV file" in str(context.exception))

    def testMerge(self):
        csvCombiner.merge_csv(['','./fixtures/accessories.csv', './fixtures/clothing.csv', 'test.csv'])
        expected_sheet = pe.load("test.csv", name_columns_by_row=0)
        actual_sheet = pe.load("./test/test1.csv", name_columns_by_row=0)
        assert actual_sheet.to_dict() == expected_sheet.to_dict()

    def testSelfMerge(self):
        csvCombiner.merge_csv(['','./fixtures/clothing.csv', './fixtures/clothing.csv', 'test.csv'])
        expected_sheet = pe.load("test.csv", name_columns_by_row=0)
        actual_sheet = pe.load("./test/test2.csv", name_columns_by_row=0)
        assert actual_sheet.to_dict() == expected_sheet.to_dict()

    def testLargeMerge(self):
        csvCombiner.merge_csv(['','./fixtures/clothing.csv', './fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv', 'test.csv'])
        expected_sheet = pe.load("test.csv", name_columns_by_row=0)
        actual_sheet = pe.load("./test/test3.csv", name_columns_by_row=0)
        assert actual_sheet.to_dict() == expected_sheet.to_dict()


if __name__ == '__main__':
    unittest.main()
