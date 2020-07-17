from datetime import datetime as dt


def current_dt_utc():
    d = dt.now(timezone.utc)
    strd = d.strftime("%Y-%m-%d-%H%M")
    return strd
