from __future__ import annotations

import math
import random
from dataclasses import dataclass, asdict
from statistics import mean

METRICS = [
    "built_in_demand", "demand_depth", "zero_capital", "low_skill",
    "repeatability", "edge_capacity", "ai_leverage", "rmb_cashout",
    "rule_stability", "first_cash_speed", "saturation_resistance", "online_fit",
]

BASE_WEIGHTS = {
    "built_in_demand": 1.8,
    "demand_depth": 1.3,
    "zero_capital": 1.7,
    "low_skill": 1.3,
    "repeatability": 1.5,
    "edge_capacity": 1.7,
    "ai_leverage": 0.8,
    "rmb_cashout": 1.2,
    "rule_stability": 1.2,
    "first_cash_speed": 1.1,
    "saturation_resistance": 1.5,
    "online_fit": 1.6,
}

CANDIDATES = {
    "qualification_gated_task_queue": [10,10,10,8,8,9,7,10,8,7,9,10],
    "crowdtest_task_radar": [10,8,10,7,7,9,8,10,8,9,8,10],
    "search_ai_eval_microtasks": [10,10,10,8,8,8,7,10,7,7,8,10],
    "rare_device_compat_testing": [10,8,9,7,7,9,7,10,8,8,9,10],
    "official_game_low_level_supply": [10,9,9,9,9,10,5,9,6,7,9,10],
    "public_buy_request_matching": [10,8,10,8,7,10,7,9,7,7,9,10],
    "online_app_mystery_testing": [9,7,10,9,6,8,6,10,8,8,7,10],
    "remote_customer_service_shifts": [10,9,10,8,9,6,5,10,9,7,6,10],
    "legacy_file_rescue": [8,7,10,6,8,9,9,10,8,6,9,10],
    "user_research_panels": [9,7,10,10,5,7,4,10,8,8,5,10],
    "digital_templates": [7,7,10,9,7,7,9,10,8,6,5,10],
    "bug_bounty": [10,8,10,2,6,9,10,10,9,4,8,10],
    "creator_bonus_pool": [10,7,10,9,3,4,7,10,6,7,3,10],
    "long_tail_dropshipping": [10,10,8,7,8,8,7,10,6,6,5,10],
}


def weighted_score(values, weights):
    numerator = sum(values[i] * weights[m] for i, m in enumerate(METRICS))
    return numerator / sum(weights.values())


def monte_carlo(iterations=50000, sigma=0.30, seed=42):
    rng = random.Random(seed)
    stats = {name: {"wins": 0, "top3": 0, "ranks": [], "scores": []} for name in CANDIDATES}

    for _ in range(iterations):
        weights = {}
        for metric, base in BASE_WEIGHTS.items():
            # log-normal-ish perturbation without third-party dependencies
            factor = math.exp(rng.gauss(0, sigma))
            weights[metric] = base * factor

        scored = [(weighted_score(values, weights), name) for name, values in CANDIDATES.items()]
        scored.sort(reverse=True)
        for rank, (score, name) in enumerate(scored, start=1):
            stats[name]["scores"].append(score)
            stats[name]["ranks"].append(rank)
            if rank == 1:
                stats[name]["wins"] += 1
            if rank <= 3:
                stats[name]["top3"] += 1

    rows = []
    for name, s in stats.items():
        rows.append({
            "candidate": name,
            "base_score": round(weighted_score(CANDIDATES[name], BASE_WEIGHTS), 3),
            "mc_mean": round(mean(s["scores"]), 3),
            "win_rate": round(s["wins"] / iterations, 4),
            "top3_rate": round(s["top3"] / iterations, 4),
            "mean_rank": round(mean(s["ranks"]), 3),
        })
    return sorted(rows, key=lambda x: (-x["mc_mean"], -x["top3_rate"]))


if __name__ == "__main__":
    print("Edge Lab opportunity ranking\n")
    for i, row in enumerate(monte_carlo(), start=1):
        print(
            f"{i:>2}. {row['candidate']:<36} "
            f"score={row['mc_mean']:.3f} top3={row['top3_rate']:.1%} "
            f"win={row['win_rate']:.1%} mean_rank={row['mean_rank']:.2f}"
        )
