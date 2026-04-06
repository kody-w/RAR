#!/usr/bin/env python3
"""
Dream Catcher — Parallel content production at scale, zero collision.

The Dream Catcher pattern applied to Rappterpedia: parallel fleet workers
produce deltas (isolated content fragments), which merge deterministically
at frame boundaries using (frame, utc, author, title) as composite PK.

Nothing is ever overwritten, only appended. This is how AI content
production scales without collision.

== THE PATTERN ==

1. Streams never modify shared state. They produce DELTAS.
2. Each delta is tagged with (frame, utc, stream_id) — globally unique.
3. Merge is ADDITIVE: append, deduplicate by composite PK.
4. The output of frame N is the input to frame N+1.
5. Nothing produced in any frame is ever lost.

== USAGE ==

  # Worker produces a delta (called by each fleet worker)
  python rappterpedia/dream_catcher.py produce --stream alpha --frame 42

  # Merge all deltas for a frame (called by merge job)
  python rappterpedia/dream_catcher.py merge --frame 42

  # Full cycle: produce + merge (single machine)
  python rappterpedia/dream_catcher.py cycle --streams 5 --frame 42

== OLLAMA SUPPORT ==

  Set OLLAMA_MODEL to use a local Ollama model as the LLM backend:
  OLLAMA_MODEL=gemma4 python rappterpedia/dream_catcher.py produce --stream alpha
"""

from __future__ import annotations

import json
import os
import random
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent
RAR_DIR = BASE_DIR.parent
DELTAS_DIR = BASE_DIR / "stream_deltas"
STATE_FILE = BASE_DIR / "rappterpedia_state.json"
EXPORT_FILE = BASE_DIR / "rappterpedia_export.json"
REVIEWS_FILE = RAR_DIR / "state" / "curator_reviews.json"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LLM Backends — multi-stream intelligence
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _get_token():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        try:
            r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=5)
            if r.returncode == 0:
                token = r.stdout.strip()
        except Exception:
            pass
    return token


def llm_github(system: str, user: str, max_tokens: int = 500) -> str:
    """GitHub Models API backend."""
    token = _get_token()
    if not token:
        raise RuntimeError("No GITHUB_TOKEN")
    model = os.environ.get("RAPPTERVERSE_MODEL", "openai/gpt-4.1-mini")
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.85, "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"].strip()


def llm_ollama(system: str, user: str, max_tokens: int = 500) -> str:
    """Ollama local backend — Gemma 4, Llama, Mistral, etc."""
    model = os.environ.get("OLLAMA_MODEL", "gemma4")
    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "stream": False,
        "options": {"num_predict": max_tokens, "temperature": 0.85},
    }).encode()
    req = urllib.request.Request(
        f"{host}/api/chat", data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return data["message"]["content"].strip()


def llm_copilot(system: str, user: str, max_tokens: int = 500) -> str:
    """GitHub Copilot CLI — UNLIMITED tokens. Always try first."""
    combined = f"{system}\n\n{user}"
    try:
        result = subprocess.run(
            ["gh", "copilot", "--", "-p", combined],
            capture_output=True, text=True, timeout=300,
        )
    except FileNotFoundError:
        raise RuntimeError("gh CLI not found")
    except subprocess.TimeoutExpired:
        raise RuntimeError("Copilot CLI timed out")

    if result.returncode != 0:
        raise RuntimeError(f"Copilot CLI error: {result.stderr.strip()}")

    raw = result.stdout.strip()
    if not raw:
        raise RuntimeError("Copilot CLI returned empty output")

    # Strip trailing usage stats
    lines = raw.split("\n")
    content_lines = []
    for line in lines:
        if line.strip().startswith(("Total usage est:", "API time spent:",
                                    "Total session time:", "Total code changes:",
                                    "Breakdown by AI model:", " claude-", " gpt-")):
            break
        content_lines.append(line)
    return "\n".join(content_lines).strip()


def llm_generate(system: str, user: str, max_tokens: int = 500) -> str | None:
    """Try all LLM backends. Copilot CLI FIRST — unlimited tokens, infinite, free.
    Fallback: Copilot CLI → GitHub Models → Ollama."""
    backends = [
        ("copilot", llm_copilot),    # FIRST — unlimited, infinite, free
        ("github", llm_github),       # Second — rate-limited
    ]
    if os.environ.get("OLLAMA_MODEL", ""):
        backends.append(("ollama", llm_ollama))

    for name, fn in backends:
        try:
            result = fn(system, user, max_tokens)
            if result:
                return result
        except Exception as e:
            print(f"  [{name.upper()}] Failed: {e}")
    return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Utilities
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def load_json(p):
    if not Path(p).exists(): return {}
    with open(p) as f: return json.load(f)

def save_json(p, d):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f: json.dump(d, f, indent=2)

def load_registry():
    reg = load_json(RAR_DIR / "registry.json")
    return reg.get("agents", [])

def composite_pk(frame, utc, author, title):
    """The globally unique key — collision-free by construction."""
    return f"{frame}:{utc}:{author}:{title[:80]}"


SYSTEM_PROMPT = """You are a Rappterpedia curator for the RAPP Agent ecosystem wiki.

Key facts:
- RAR is an open single-file agent ecosystem. Every agent is ONE .py file.
- Agents have a __manifest__ dict, inherit BasicAgent, implement perform(**kwargs) returning str.
- The registry builder uses AST parsing (no code execution).
- Categories: core, pipeline, integrations, productivity, devtools, plus industry verticals.
- Quality tiers: community → verified → official.
- The Agent Store is a zero-dependency single HTML file.

Write clearly, specifically, and practically. Use markdown. No filler."""

AUTHORS = [
    "AgentSmith", "RAPPBuilder", "CodeForge", "SingleFileDevotee",
    "ManifestMaster", "PyAgent", "RegistryRunner", "HoloDeckEng",
    "FederationFan", "WorkbenchWizard", "PipelinePro", "IntegrationDev",
    "CardCollector", "ASTWalker", "TierClimber", "VersionBumper",
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Delta Production — each stream produces a delta file
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def produce_delta(stream_id: str, frame: int, ticks: int = 3) -> dict:
    """
    Produce a content delta for one stream.
    A delta contains ONLY what this stream created — never reads or modifies shared state.
    """
    ts = now_iso()
    agents = load_registry()

    # Read previous state for echoes (read-only — we never write to it)
    prev_state = load_json(STATE_FILE)
    recent_titles = set()
    for a in prev_state.get("articles", [])[-20:]:
        recent_titles.add(a.get("title", ""))
    for t in prev_state.get("threads", [])[-20:]:
        recent_titles.add(t.get("title", ""))
    covered_agents = set(prev_state.get("generated_agent_ids", []))

    delta = {
        "frame": frame,
        "stream_id": stream_id,
        "completed_at": "",  # Set after production
        "articles_created": [],
        "threads_created": [],
        "reviews_created": [],
    }

    echo_context = (
        f"Frame {frame}, stream {stream_id}. "
        f"Total existing: {len(prev_state.get('articles',[]))} articles, "
        f"{len(prev_state.get('threads',[]))} threads. "
        f"Don't repeat recent topics: {', '.join(list(recent_titles)[:5])}."
    )

    for tick in range(ticks):
        # ── Article ──
        if agents:
            uncovered = [a for a in agents if a.get("name") not in covered_agents]
            agent = random.choice(uncovered if uncovered else agents)
            ctx = {
                "name": agent.get("display_name", ""),
                "agent_name": agent.get("name", ""),
                "description": agent.get("description", ""),
                "category": agent.get("category", "general").replace("_", " "),
                "lines": agent.get("_lines", 0),
                "tier": agent.get("quality_tier", "community"),
                "tags": ", ".join(agent.get("tags", [])),
            }

            title = f"Deep Dive: {ctx['name']}"
            if title in recent_titles:
                title = f"How {ctx['name']} Works"
            if title in recent_titles:
                title = f"Using {ctx['name']} in Production"

            content = llm_generate(
                system=SYSTEM_PROMPT,
                user=f"Write a wiki article: \"{title}\"\n\nAgent: {ctx['name']} ({ctx['agent_name']})\nDescription: {ctx['description']}\nCategory: {ctx['category']}, {ctx['lines']} lines, {ctx['tier']} tier\nTags: {ctx['tags']}\n\n{echo_context}\n\nWrite practical, specific content with ## headers.",
            )
            if not content:
                print(f"  [SKIP] No LLM response for article: {title}")
                continue  # LLM-only — no template fallback

            author = random.choice(AUTHORS)
            pk = composite_pk(frame, ts, author, title)
            delta["articles_created"].append({
                "pk": pk, "title": title, "category": "agents",
                "tags": agent.get("tags", [])[:4] + ["deep-dive"],
                "content": content, "author": author,
                "source": "llm",
                "created": ts, "updated": ts,
            })
            recent_titles.add(title)
            covered_agents.add(agent.get("name", ""))

        # ── Thread ──
        topics = [
            "the single-file principle", "agent testing best practices",
            "the Holo card system", "federation for teams",
            "manifest design patterns", "the Agent Workbench",
            "community quality standards", "agent versioning strategy",
        ]
        topic = random.choice(topics)
        thread_title = f"Discussion: {topic}"
        body = llm_generate(
            system="You are a community member in the Rappterpedia forum. Write an authentic, detailed post about the RAPP agent ecosystem. Be specific about agents, manifests, perform(), BasicAgent, the single-file principle. Write 3-5 paragraphs.",
            user=f"Write a forum post titled \"{thread_title}\".\n\n{echo_context}",
            max_tokens=400,
        )
        if not body:
            print(f"  [SKIP] No LLM response for thread: {thread_title}")
            continue  # LLM-only — no template fallback

        author = random.choice(AUTHORS)
        pk = composite_pk(frame, ts, author, thread_title)

        # Generate 1-3 replies (LLM-only, skip if no response)
        replies = []
        for _ in range(random.randint(1, 3)):
            reply_author = random.choice(AUTHORS)
            reply_text = llm_generate(
                system="Reply to a Rappterpedia forum thread. Be helpful, specific, and conversational. Reference RAR concepts like manifests, perform(), BasicAgent, quality tiers, the registry.",
                user=f"Thread: {thread_title}\nPost: {body[:300]}\n\nWrite a thoughtful 2-3 sentence reply.",
                max_tokens=150,
            )
            if reply_text:
                replies.append({"author": reply_author, "content": reply_text, "source": "llm", "created": ts})

        delta["threads_created"].append({
            "pk": pk, "title": thread_title, "channel": "general",
            "content": body, "author": author, "source": "llm",
            "created": ts, "updated": ts,
            "votes": random.randint(1, 8), "replies": replies,
        })

        # ── Reviews ──
        if agents:
            agent = random.choice(agents)
            review_text = llm_generate(
                system="Write a 2-3 sentence review of a RAR agent. Be specific, opinionated, and reference the agent's actual characteristics. Mention specific things like line count, category, what perform() does, env var requirements. No generic praise.",
                user=f"Review: {agent.get('display_name','')} ({agent.get('name','')})\nCategory: {agent.get('category','')}\n{agent.get('_lines',0)} lines, {agent.get('quality_tier','community')} tier\nDescription: {agent.get('description','')}\nTags: {', '.join(agent.get('tags',[]))}\nEnv vars: {', '.join(agent.get('requires_env',[])) or 'none'}\n\nWrite a specific, opinionated review.",
                max_tokens=150,
            )
            if not review_text:
                print(f"  [SKIP] No LLM response for review: {agent.get('name','')}")
                continue  # LLM-only

            delta["reviews_created"].append({
                "agent_name": agent.get("name", ""),
                "user": random.choice(AUTHORS),
                "rating": random.randint(3, 5),
                "text": review_text,
                "source": "llm",
                "angle": random.choice(["primary", "usability", "code_quality", "community"]),
                "timestamp": ts,
            })

    delta["completed_at"] = now_iso()
    return delta


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Dream Catcher Merge — additive, deterministic, collision-free
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def merge_deltas(frame: int) -> dict:
    """
    Merge all deltas for a frame into shared state.
    Additive only — deduplicate by composite PK, never overwrite.
    """
    state = load_json(STATE_FILE)
    if not state:
        state = {"tick_count": 0, "articles": [], "threads": [], "reviews": {},
                 "next_article_id": 1, "next_thread_id": 1, "generated_topics": [],
                 "generated_agent_ids": []}

    # Collect existing PKs for dedup
    existing_article_pks = {a.get("pk", a.get("id", "")) for a in state.get("articles", [])}
    existing_thread_pks = {t.get("pk", t.get("id", "")) for t in state.get("threads", [])}

    # Find all delta files for this frame
    delta_files = sorted(DELTAS_DIR.glob(f"frame-{frame}-*.json"))
    if not delta_files:
        print(f"  No deltas found for frame {frame}")
        return state

    new_articles = 0
    new_threads = 0
    new_reviews = 0

    for delta_path in delta_files:
        delta = load_json(delta_path)
        stream = delta.get("stream_id", "?")

        for article in delta.get("articles_created", []):
            pk = article.get("pk", "")
            if pk and pk not in existing_article_pks:
                article["id"] = f"dc-art-{state['next_article_id']:04d}"
                state["next_article_id"] += 1
                state["articles"].append(article)
                existing_article_pks.add(pk)
                new_articles += 1

        for thread in delta.get("threads_created", []):
            pk = thread.get("pk", "")
            if pk and pk not in existing_thread_pks:
                thread["id"] = f"dc-thr-{state.get('next_thread_id', 1):04d}"
                state["next_thread_id"] = state.get("next_thread_id", 1) + 1
                state["threads"].append(thread)
                existing_thread_pks.add(pk)
                new_threads += 1

        for review in delta.get("reviews_created", []):
            agent_name = review.get("agent_name", "")
            existing = state.setdefault("reviews", {}).setdefault(agent_name, [])
            # Dedup by text content
            if not any(r.get("text") == review.get("text") for r in existing):
                existing.append(review)
                new_reviews += 1

        print(f"  Merged delta: {stream} ({len(delta.get('articles_created',[]))}a, "
              f"{len(delta.get('threads_created',[]))}t, {len(delta.get('reviews_created',[]))}r)")

    state["tick_count"] = frame

    # Save merged state
    save_json(STATE_FILE, state)

    # Export for web
    save_json(EXPORT_FILE, {
        "version": "1.0", "generated": now_iso(), "tick_count": frame,
        "articles": state["articles"], "threads": state["threads"],
        "stats": {
            "total_articles": len(state["articles"]),
            "total_threads": len(state["threads"]),
            "total_replies": sum(len(t.get("replies", [])) for t in state["threads"]),
        },
    })

    # Export reviews for store
    save_json(REVIEWS_FILE, {"agents": state.get("reviews", {})})

    print(f"\n  Dream Catcher merge complete (frame {frame}):")
    print(f"    +{new_articles} articles, +{new_threads} threads, +{new_reviews} reviews")
    print(f"    Total: {len(state['articles'])} articles, {len(state['threads'])} threads")

    return state


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CLI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_current_frame():
    state = load_json(STATE_FILE)
    return state.get("tick_count", 0) + 1


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Dream Catcher — parallel content at scale")
    sub = parser.add_subparsers(dest="command")

    p_produce = sub.add_parser("produce", help="Produce a delta for one stream")
    p_produce.add_argument("--stream", required=True, help="Stream ID (alpha, bravo, etc.)")
    p_produce.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")
    p_produce.add_argument("--ticks", type=int, default=3, help="Ticks per delta")

    p_merge = sub.add_parser("merge", help="Merge all deltas for a frame")
    p_merge.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")

    p_cycle = sub.add_parser("cycle", help="Full cycle: produce N streams + merge")
    p_cycle.add_argument("--streams", type=int, default=5, help="Number of parallel streams")
    p_cycle.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")
    p_cycle.add_argument("--ticks", type=int, default=3, help="Ticks per stream")

    args = parser.parse_args()

    if args.command == "produce":
        frame = args.frame or get_current_frame()
        print(f"Dream Catcher: producing delta for stream {args.stream}, frame {frame}")
        delta = produce_delta(args.stream, frame, args.ticks)
        DELTAS_DIR.mkdir(parents=True, exist_ok=True)
        delta_path = DELTAS_DIR / f"frame-{frame}-{args.stream}.json"
        save_json(delta_path, delta)
        a = len(delta["articles_created"])
        t = len(delta["threads_created"])
        r = len(delta["reviews_created"])
        print(f"  Delta saved: {a} articles, {t} threads, {r} reviews")
        print(f"  Path: {delta_path}")

    elif args.command == "merge":
        frame = args.frame or get_current_frame()
        print(f"Dream Catcher: merging deltas for frame {frame}")
        merge_deltas(frame)

    elif args.command == "cycle":
        frame = args.frame or get_current_frame()
        streams = ["alpha", "bravo", "charlie", "delta", "echo"][:args.streams]
        print(f"Dream Catcher: full cycle, frame {frame}, {len(streams)} streams")
        print(f"{'=' * 50}")

        DELTAS_DIR.mkdir(parents=True, exist_ok=True)
        for stream in streams:
            print(f"\n  Stream {stream}...")
            delta = produce_delta(stream, frame, args.ticks)
            save_json(DELTAS_DIR / f"frame-{frame}-{stream}.json", delta)
            a = len(delta["articles_created"])
            t = len(delta["threads_created"])
            r = len(delta["reviews_created"])
            print(f"    {a} articles, {t} threads, {r} reviews")

        print(f"\n{'=' * 50}")
        print(f"  Merging...")
        merge_deltas(frame)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
