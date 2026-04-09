#!/usr/bin/env python3
"""
Dream Catcher Review Frame — AI-driven reviews for all agents.

Runs as a standalone frame: reads registry.json, generates one genuine
LLM review per agent, writes to state/curator_reviews.json.

Usage:
    python scripts/generate_reviews.py
"""

import json
import os
import random
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "registry.json"
OUTPUT = REPO_ROOT / "state" / "curator_reviews.json"

REVIEWER_NAMES = [
    "Virtual Curator", "The Architect", "Agent Auditor", "Registry Reviewer",
    "CardSmith Review Desk", "Community Sentinel", "Quality Gate",
    "The Assessor", "Pattern Scanner", "Code Lens",
    "Deck Builder Review", "Agent Spotlight", "Tier Watch",
]

REVIEW_ANGLES = [
    "overall quality", "usability and setup", "code quality",
    "community value", "compared to alternatives",
]


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        try:
            r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=5)
            if r.returncode == 0:
                token = r.stdout.strip()
        except Exception:
            pass
    return token


def llm_review(agent: dict, angle: str, token: str) -> "tuple[str, int] | None":
    """Generate one AI review for an agent. Returns (text, rating) or None."""
    name = agent.get("name", "")
    display = agent.get("display_name", name)
    desc = agent.get("description", "")
    cat = agent.get("category", "").replace("_", " ")
    lines = agent.get("_lines", "?")
    size = agent.get("_size_kb", "?")
    ver = agent.get("version", "1.0.0")
    tier = agent.get("quality_tier", "community")
    tags = ", ".join(agent.get("tags", []))
    env_vars = ", ".join(agent.get("requires_env", [])) or "none"
    deps = ", ".join(agent.get("dependencies", [])) or "none"
    publisher = name.split("/")[0] if "/" in name else "unknown"

    system = (
        "You are a Rappterpedia reviewer — a knowledgeable, encouraging voice "
        "in the RAPP Agent ecosystem. You write genuine reviews that celebrate "
        "what each agent does well while being specific and honest. "
        "You understand that every agent represents someone's real effort. "
        "A 3000+ line agent is extraordinary. A 200-line focused utility is elegant. "
        "Find what makes each agent special.\n\n"
        "Rules:\n"
        "- Be specific — reference actual line count, features, tags, category\n"
        "- Be constructive — highlight strengths, frame improvements as opportunities\n"
        "- Be proportional — massive agents deserve recognition for their scope\n"
        "- Never say an agent 'needs to differentiate' — every shipped agent IS different\n"
        "- 2-3 sentences max\n"
        "- Also return a star rating 1-5 on the LAST line as just the number\n"
        "- Rating guide: 1=broken, 2=minimal, 3=solid, 4=impressive, 5=exceptional\n"
        "- Most agents that work should be 3-4. Large/complex agents should be 4-5."
    )

    user = (
        f"Review this agent from the angle of '{angle}':\n\n"
        f"Name: {display} ({name})\n"
        f"Category: {cat}\n"
        f"Description: {desc}\n"
        f"Lines: {lines}\n"
        f"Size: {size} KB\n"
        f"Version: {ver}\n"
        f"Tier: {tier}\n"
        f"Tags: {tags}\n"
        f"Env vars required: {env_vars}\n"
        f"Dependencies: {deps}\n"
        f"Publisher: {publisher}\n\n"
        f"Write a genuine 2-3 sentence review, then put ONLY the star rating (1-5) "
        f"on the last line as a single digit."
    )

    payload = json.dumps({
        "model": os.environ.get("RAPPTERVERSE_MODEL", "openai/gpt-4.1-mini"),
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.85,
        "max_tokens": 200,
    }).encode()

    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        result = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return None

    # Parse rating from last line
    result_lines = result.splitlines()
    rating = 4
    text = result
    for line in reversed(result_lines):
        stripped = line.strip().rstrip(".*★☆/5")
        if stripped.isdigit() and 1 <= int(stripped) <= 5:
            rating = int(stripped)
            text = "\n".join(result_lines[:result_lines.index(line)]).strip()
            break

    if not text or len(text) < 20:
        return None

    return text, rating


def main():
    token = get_token()
    if not token:
        print("ERROR: No GitHub token available")
        return 1

    reg = json.load(REGISTRY.open())
    agents = reg["agents"]
    print(f"🔥 Dream Catcher Review Frame — {len(agents)} agents")
    print(f"   Model: {os.environ.get('RAPPTERVERSE_MODEL', 'openai/gpt-4.1-mini')}")

    ts = datetime.now(timezone.utc).isoformat()
    all_reviews: dict[str, list] = {}
    success = 0
    failed = 0

    for i, agent in enumerate(agents):
        name = agent.get("name", "")
        angle = random.choice(REVIEW_ANGLES)

        result = llm_review(agent, angle, token)
        if result:
            text, rating = result
            reviewer = random.choice(REVIEWER_NAMES)
            all_reviews.setdefault(name, []).append({
                "user": "curator",
                "rating": rating,
                "text": text,
                "timestamp": ts,
            })
            success += 1
            stars = "★" * rating
            if (i + 1) % 10 == 0:
                print(f"  [{i+1}/{len(agents)}] {stars} {name}")
        else:
            failed += 1
            print(f"  [{i+1}] ✗ {name}")

        # Rate limit: ~15 RPM for free tier, be conservative
        if (i + 1) % 10 == 0:
            time.sleep(2)

    print(f"\n✅ {success} reviews generated, {failed} failed")

    # Rating distribution
    dist: dict[int, int] = {}
    for revs in all_reviews.values():
        for r in revs:
            dist[r["rating"]] = dist.get(r["rating"], 0) + 1
    print("Rating distribution:")
    for k in sorted(dist.keys()):
        print(f"  {k}★: {dist[k]}")

    # Save
    export = {"agents": all_reviews, "updated_at": ts}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(export, OUTPUT.open("w"), indent=2)
    print(f"Saved to {OUTPUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
