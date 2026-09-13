"""Simple calculator for gated microtask/night-shift economics.

Use only for manual, platform-permitted work. It does not automate task completion.
"""

from dataclasses import dataclass


@dataclass
class Scenario:
    points_per_task: float = 10
    yuan_per_100_points: float = 1.0
    seconds_per_task: float = 20
    idle_rate: float = 0.20
    valid_rate: float = 0.95
    hours_per_day: float = 2
    days_per_month: int = 20

    @property
    def yuan_per_task(self) -> float:
        return self.points_per_task / 100 * self.yuan_per_100_points

    @property
    def theoretical_tasks_per_hour(self) -> float:
        return 3600 / self.seconds_per_task

    @property
    def net_hourly(self) -> float:
        return (
            self.theoretical_tasks_per_hour
            * self.yuan_per_task
            * (1 - self.idle_rate)
            * self.valid_rate
        )

    @property
    def monthly(self) -> float:
        return self.net_hourly * self.hours_per_day * self.days_per_month


def print_grid() -> None:
    print("秒/题 | 6分普通档 | 10分夜间档")
    print("------|-----------|------------")
    for seconds in (10, 15, 20, 25, 30, 40):
        normal = Scenario(points_per_task=6, seconds_per_task=seconds,
                          idle_rate=0, valid_rate=1).net_hourly
        night = Scenario(points_per_task=10, seconds_per_task=seconds,
                         idle_rate=0, valid_rate=1).net_hourly
        print(f"{seconds:>5} | ¥{normal:>8.2f} | ¥{night:>9.2f}")


if __name__ == "__main__":
    print_grid()
    s = Scenario()
    print("\n示例（含20%空闲、95%有效率）：")
    print(f"净时薪约：¥{s.net_hourly:.2f}")
    print(f"按每天{s.hours_per_day:g}小时、每月{s.days_per_month}天：¥{s.monthly:.2f}/月")
