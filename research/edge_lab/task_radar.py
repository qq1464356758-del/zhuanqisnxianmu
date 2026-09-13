"""Generic public task-pool radar.

Use only on public pages whose terms permit automated access. This script does NOT
log in, bypass controls, submit tasks, create accounts, or perform paid work.
It only detects page changes and highlights task-like text for human review.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from urllib.request import Request, urlopen

STATE = Path("task_radar_state.json")
USER_AGENT = "EdgeLabResearch/1.0 (+personal low-frequency monitor)"


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def normalize(text: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_signals(text: str):
    patterns = {
        "money": r"(?:预计收益|奖励|报酬|佣金|礼券)[^。；]{0,30}",
        "slots": r"\b\d+\s*/\s*\d+\b|(?:名额|人数)[^。；]{0,20}",
        "time": r"(?:小时|分钟|截止时间|任务周期)[^。；]{0,30}",
        "qualification": r"(?:认证|考试|精英|等级|优先|团队|审核)[^。；]{0,30}",
    }
    out = {}
    for key, pat in patterns.items():
        out[key] = list(dict.fromkeys(re.findall(pat, text, flags=re.I)))[:20]
    return out


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state():
    if not STATE.exists():
        return {}
    return json.loads(STATE.read_text(encoding="utf-8"))


def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def check(url: str):
    state = load_state()
    raw = fetch(url)
    text = normalize(raw)
    current = digest(text)
    changed = state.get(url) != current
    result = {"url": url, "changed": changed, "signals": extract_signals(text)}
    state[url] = current
    save_state(state)
    return result


if __name__ == "__main__":
    # Add only public task-hall URLs that explicitly permit your access pattern.
    urls = []
    if not urls:
        print("Edit urls = [...] first. Keep polling low-frequency and obey site rules.")
    for url in urls:
        print(json.dumps(check(url), ensure_ascii=False, indent=2))
        time.sleep(3)
