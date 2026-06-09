"""Cron weekday field: Unix 1-5 (Mon–Fri) vs APScheduler ISO DOW."""
from datetime import datetime
from zoneinfo import ZoneInfo

from src.scheduler.cron_manager import (
    normalize_cron_expression_for_apscheduler,
    preview_next_runs,
)


def test_unix_weekday_1_5_normalizes_to_mon_fri():
    assert normalize_cron_expression_for_apscheduler("0 */6 * * 1-5") == "0 */6 * * mon-fri"


def test_preview_weekday_runs_include_current_monday():
    tz = "Asia/Seoul"
    # Monday 2026-05-18 10:26 KST — next slot should be same day 12:00, not Tuesday midnight.
    runs = preview_next_runs("0 */6 * * 1-5", tz, count=1)
    assert runs
    assert runs[0].startswith("2026-05-18")


def test_preview_mon_fri_alias():
    tz = ZoneInfo("Asia/Seoul")
    now = datetime(2026, 5, 18, 10, 26, 27, tzinfo=tz)
    runs = preview_next_runs("0 */6 * * mon-fri", "Asia/Seoul", count=3)
    assert runs[0] == "2026-05-18 12:00"
    assert runs[1] == "2026-05-18 18:00"
    assert runs[2] == "2026-05-19 00:00"
