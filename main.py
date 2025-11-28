from datetime import datetime, time
from zoneinfo import ZoneInfo
from storage import BELL_TIMES

def get_now(timezone):
    tz_syd = ZoneInfo(timezone)
    now_syd = datetime.now(tz_syd)
    return now_syd

def get_s():
    now_syd = get_now("Australia/Sydney")
    mn_syd = datetime.combine(now_syd.date(), time.min, tzinfo=ZoneInfo("Australia/Sydney"))
    diff = now_syd - mn_syd
    mn_syd_now = diff.total_seconds() // 60
    return int(mn_syd_now)

def get_d():
    now_syd = get_now("Australia/Sydney")
    day_num = now_syd.weekday()
    day_num_text = now_syd.strftime('%A')
    return {"index": day_num, "text": day_num_text}

print(get_s())
print(get_d())