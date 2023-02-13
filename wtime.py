import time
import datetime
import zoneinfo
import calendar


class FmtDatetime(object):

    def __init__(self, dt: datetime.datetime, fmt: str):
        """
        以指定fmt格式, 初始化dt时间相关的所有周边时间
        :param dt:
        :param fmt:
        """
        parse_obj = ParseDatetime(dt)
        self.the_day_before_yesterday = parse_obj.the_day_before_yesterday().strftime(fmt)
        self.yesterday = parse_obj.yesterday().strftime(fmt)
        self.tomorrow = parse_obj.tomorrow().strftime(fmt)
        self.the_day_after_tomorrow = parse_obj.the_day_after_tomorrow().strftime(fmt)
        self.first_day_of_month = parse_obj.first_day_of_month().strftime(fmt)
        self.last_day_of_month = parse_obj.last_day_of_month().strftime(fmt)
        self.first_day_of_last_month = parse_obj.first_day_of_last_month().strftime(fmt)
        self.last_day_of_last_month = parse_obj.last_day_of_last_month().strftime(fmt)
        self.first_day_of_week = parse_obj.first_day_of_week().strftime(fmt)
        self.last_day_of_week = parse_obj.last_day_of_week().strftime(fmt)
        self.first_day_of_last_week = parse_obj.first_day_of_last_week().strftime(fmt)
        self.last_day_of_last_week = parse_obj.last_day_of_last_week().strftime(fmt)
        self.first_day_of_quarter = parse_obj.first_day_of_quarter().strftime(fmt)
        self.last_day_of_quarter = parse_obj.last_day_of_quarter().strftime(fmt)
        self.first_day_of_last_quarter = parse_obj.first_day_of_last_quarter().strftime(fmt)
        self.last_day_of_last_quarter = parse_obj.last_day_of_last_quarter().strftime(fmt)
        self.first_day_of_year = parse_obj.first_day_of_year().strftime(fmt)
        self.last_day_of_year = parse_obj.last_day_of_year().strftime(fmt)
        self.first_day_of_last_year = parse_obj.first_day_of_last_year().strftime(fmt)
        self.last_day_of_last_year = parse_obj.last_day_of_last_year().strftime(fmt)


class ParseDatetime(object):

    def __init__(self, dt: datetime.datetime):
        """
        解析dt时间相关的周边时间, 相关时间为 datetime.datetime
        如果想一次性以指定fmt格式实例化所有周边时间, 请调用 FmtDatetime
        :param dt:
        """
        self.__dt = dt

    def days_diff(self, days):
        """
        计算相差多少天的日期
        :param days: 相差天数
        :return:
        """
        timestamp = self.__dt.timestamp() + days*86400
        return datetime.datetime.fromtimestamp(timestamp)

    def yesterday(self):
        """
        昨天
        :return:
        """
        return self.days_diff(-1)

    def the_day_before_yesterday(self):
        """
        前天
        :return:
        """
        return self.days_diff(-2)

    def tomorrow(self):
        """
        明天
        :return:
        """
        return self.days_diff(1)

    def the_day_after_tomorrow(self):
        """
        后天
        :return:
        """
        return self.days_diff(2)

    def first_day_of_month(self):
        """
        所在月份第一天
        :return:
        """
        return self.__dt.replace(day=1)

    def last_day_of_month(self):
        """
        所在月份最后一天
        :return:
        """
        dt_month_max_day = calendar.monthrange(self.__dt.year, self.__dt.month)[1]
        return self.__dt.replace(day=dt_month_max_day)

    def first_day_of_last_month(self):
        """
        上个月份第一天
        :return:
        """
        return self.last_day_of_last_month().replace(day=1)

    def last_day_of_last_month(self):
        """
        所在月份最后一天
        :return:
        """
        timestamp = self.first_day_of_month().timestamp() - 86400
        return datetime.datetime.fromtimestamp(timestamp)

    def is_weekend(self):
        """
        是否周末
        :return:
        """
        return self.__dt.isoweekday() in [6, 7]

    def first_day_of_week(self):
        """
        所在周的第一天
        :return:
        """
        # 和周一相差天数
        days = 1 - self.__dt.isoweekday()
        return self.days_diff(days)

    def last_day_of_week(self):
        """
        所在周的最后一天
        :return:
        """
        # 和周日相差天数
        days = 7 - self.__dt.isoweekday()
        return self.days_diff(days)

    def first_day_of_last_week(self):
        """
        上个星期的第一天
        :return:
        """
        timestamp = self.first_day_of_week().timestamp() - 86400*7
        return datetime.datetime.fromtimestamp(timestamp)

    def last_day_of_last_week(self):
        """
        上个星期的最后一天
        :return:
        """
        timestamp = self.last_day_of_week().timestamp() - 86400*7
        return datetime.datetime.fromtimestamp(timestamp)

    @staticmethod
    def get_quarter_by_month(month):
        """
        根据月份获取所在季度, 第一季度 为 0
        :param month:
        :return:
        """
        quarter = (month - 1) // 3
        return {
            "quarter": quarter,
            "iso_quarter": quarter + 1,
            "first_month": quarter*3 + 1,
            "last_month": quarter*3 + 3,
        }

    def quarter(self):
        """
        当前日期所属季度, 第一季度 为 0
        :return:
        """
        return self.get_quarter_by_month(self.__dt.month).get("quarter")

    def iso_quarter(self):
        """
        当前日期所属季度, 第一季度 为 1
        :return:
        """
        return self.get_quarter_by_month(self.__dt.month).get("iso_quarter")

    def first_day_of_quarter(self):
        """
        所在季度的第一天
        :return:
        """
        month = self.get_quarter_by_month(self.__dt.month).get("first_month")
        return self.__dt.replace(month=month, day=1)

    def last_day_of_quarter(self):
        """
        所在季度的最后一天
        :return:
        """
        month = self.get_quarter_by_month(self.__dt.month).get("last_month")
        day = calendar.monthrange(year=self.__dt.year, month=month)[1]
        return self.__dt.replace(month=month, day=day)

    def first_day_of_last_quarter(self):
        """
        上个季度的第一天
        :return:
        """
        last_day_of_last_quarter = self.last_day_of_last_quarter()
        month = self.get_quarter_by_month(last_day_of_last_quarter.month).get("first_month")
        return self.__dt.replace(year=last_day_of_last_quarter.year, month=month, day=1)

    def last_day_of_last_quarter(self):
        """
        上个季度的最后一天
        :return:
        """
        # 本季度的第一天, 减去一天, 是上个季度的最后一天
        timestamp = self.first_day_of_quarter().timestamp() - 86400
        return datetime.datetime.fromtimestamp(timestamp)

    def first_day_of_year(self):
        """
        所在年的第一天
        :return:
        """
        return self.__dt.replace(month=1, day=1)

    def last_day_of_year(self):
        """
        所在年的最后一天
        :return:
        """
        return self.__dt.replace(month=12, day=31)

    def first_day_of_last_year(self):
        """
        去年的第一天
        :return:
        """
        year = self.__dt.year - 1
        return self.__dt.replace(year=year, month=1, day=1)

    def last_day_of_last_year(self):
        """
        去年的最后一天
        :return:
        """
        year = self.__dt.year - 1
        return self.__dt.replace(year=year, month=12, day=31)

