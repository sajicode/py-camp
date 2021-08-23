def return_day(a):
      days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]

      if a > 0 & a <= len(days):
        return days[a - 1]
      return None


