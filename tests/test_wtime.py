import datetime
import unittest

import wtime


class WTimeTestCase(unittest.TestCase):
    def test_fmt_datetime(self):
        dt_fmt = wtime.FmtDatetime(datetime.datetime.fromisoformat("2023-02-10"), "%Y-%m-%d")
        self.assertEqual(dt_fmt.the_day_before_yesterday, "2023-02-08")
        self.assertEqual(dt_fmt.yesterday, "2023-02-09")
        self.assertEqual(dt_fmt.tomorrow, "2023-02-11")
        self.assertEqual(dt_fmt.the_day_after_tomorrow, "2023-02-12")
        self.assertEqual(dt_fmt.first_day_of_month, "2023-02-01")
        self.assertEqual(dt_fmt.last_day_of_month, "2023-02-28")
        self.assertEqual(dt_fmt.first_day_of_last_month, "2023-01-01")
        self.assertEqual(dt_fmt.last_day_of_last_month, "2023-01-31")
        self.assertEqual(dt_fmt.is_weekend, False)
        self.assertEqual(dt_fmt.first_day_of_week, "2023-02-06")
        self.assertEqual(dt_fmt.last_day_of_week, "2023-02-12")
        self.assertEqual(dt_fmt.first_day_of_last_week, "2023-01-30")
        self.assertEqual(dt_fmt.last_day_of_last_week, "2023-02-05")
        self.assertEqual(dt_fmt.iso_quarter, 1)
        self.assertEqual(dt_fmt.first_day_of_quarter, "2023-01-01")
        self.assertEqual(dt_fmt.last_day_of_quarter, "2023-03-31")
        self.assertEqual(dt_fmt.first_day_of_last_quarter, "2022-10-01")
        self.assertEqual(dt_fmt.last_day_of_last_quarter, "2022-12-31")
        self.assertEqual(dt_fmt.first_day_of_year, "2023-01-01")
        self.assertEqual(dt_fmt.last_day_of_year, "2023-12-31")
        self.assertEqual(dt_fmt.first_day_of_last_year, "2022-01-01")
        self.assertEqual(dt_fmt.last_day_of_last_year, "2022-12-31")


if __name__ == '__main__':
    unittest.main()
