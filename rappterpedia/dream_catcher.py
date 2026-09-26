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

  # Worker produces a delta (called by each fleet worker, into its own directory)
  python rappterpedia/dream_catcher.py produce --stream alpha --frame 42 --out-dir delta-out

  # Copy the workers' deltas in, never overwriting one (called by merge job)
  python rappterpedia/dream_catcher.py collect --from delta-output

  # Merge all deltas for a frame (called by merge job)
  python rappterpedia/dream_catcher.py merge --frame 42

  # Full cycle: produce + merge (single machine)
  python rappterpedia/dream_catcher.py cycle --streams 5 --frame 42

  # Fold loose deltas of merged frames into bundles (merge does this itself)
  python rappterpedia/dream_catcher.py fold

  # Re-materialize every bundled delta as its original file, byte for byte
  python rappterpedia/dream_catcher.py extract --out some/dir

== DELTA BUNDLES ==

  A delta stays a loose file (stream_deltas/frame-<N>-<stream>.json) until its
  frame has merged. Merge then folds it into the bundle for its 100-frame window
  (stream_deltas/bundles/frames-001500-001599.json), keyed by its original file
  name, with the SHA-256 of its original bytes. A bundle never exceeds
  BUNDLE_MAX_BYTES, which keeps it inside the 1 MiB ceiling that RAPP/1 frame
  discovery reads. Nothing is dropped: each file's exact bytes are
  json.dumps(delta, indent=2), and a loose file is removed only after the
  written bundle reproduces them. Anything that does not reproduce stays loose,
  as does any delta named in HELD_LOOSE.

  A delta file name is written once. produce, cycle and refill write
  frame-<N>-<stream>.json only if no loose or bundled delta has that name, and
  otherwise the next free "frame-<N>-<stream> 2.json", " 3.json" and so on, so a
  delta committed before its frame ran survives, and merges, beside the new one.
  collect copies deltas in the same way; a delta already there, byte for byte,
  is not copied again. produce --out-dir writes into an empty directory instead.
  extract never overwrites a file either, and never writes into stream_deltas/.

== OLLAMA SUPPORT ==

  Set OLLAMA_MODEL to use a local Ollama model as the LLM backend:
  OLLAMA_MODEL=gemma4 python rappterpedia/dream_catcher.py produce --stream alpha
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import random
import re
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
BUNDLES_DIR = DELTAS_DIR / "bundles"
STATE_FILE = BASE_DIR / "rappterpedia_state.json"
EXPORT_FILE = BASE_DIR / "rappterpedia_export.json"

BUNDLE_SCHEMA = "rappterpedia-delta-bundle/1.0"
BUNDLE_WINDOW = 100
BUNDLE_MAX_BYTES = 768 * 1024
BUNDLE_FILE_BYTES = "json.dumps(delta, indent=2) as UTF-8, no trailing newline; sha256 is over those bytes"
DELTA_NAME = re.compile(r"^frame-(\d+)-(.*)\.json$")
BUNDLE_NAME = re.compile(r"^frames-(\d+)-(\d+)(?:-part(\d+))?\.json$")

# Deltas the fold leaves exactly where they are, byte for byte, until their owner
# has reviewed their text: it quotes local tool output, and folding would copy
# that into a new file. To redact one, edit it in place or delete it, then remove
# its name here; an edited delta folds on the next merge.
HELD_LOOSE = frozenset({
    "frame-101-review-borg-cardsmith_agent.json",
    "frame-101-review-discreetRappers-copilot_studio_transpiler.json",
    "frame-101-review-discreetRappers-rapp_pipeline.json",
    "frame-101-review-kody-agent_workbench.json",
    "frame-101-review-kody-rar_remote_agent.json",
})


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
    """GitHub Copilot CLI — tried first (preferred backend)."""
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
    """Try all LLM backends. The GitHub Copilot CLI is tried first (preferred backend).
    Fallback: Copilot CLI → GitHub Models → Ollama."""
    backends = [
        ("copilot", llm_copilot),    # first (preferred backend)
        ("github", llm_github),       # Second — rate-limited
    ]
    if os.environ.get("OLLAMA_MODEL", ""):
        backends.append(("ollama", llm_ollama))

    for name, fn in backends:
        try:
            result = fn(system, user, max_tokens)
            if result and "copilot [command]" not in result and "gh copilot" not in result:
                return result
            elif result:
                print(f"  [{name.upper()}] Rejected: got CLI help text instead of content")
        except Exception as e:
            print(f"  [{name.upper()}] Failed: {e}")
    return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Utilities
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clamp_review_rating(rating) -> int:
    """Keep generated curator reviews in the encouraging 4-5 star range."""
    try:
        rating = int(rating)
    except (TypeError, ValueError):
        rating = 4
    return max(4, min(5, rating))

def load_json(p):
    if not Path(p).exists(): return {}
    with open(p) as f: return json.load(f)

def save_json(p, d):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f: json.dump(d, f, indent=2)

def load_registry():
    reg = load_json(RAR_DIR / "registry.json")
    return reg.get("agents", [])

def composite_pk(frame):
    """The globally unique key: frame (virtual time) + UTC (real time).
    Each call generates a fresh UTC timestamp for natural uniqueness."""
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return f"{frame}:{utc}"


SYSTEM_PROMPT = """You are a Rappterpedia curator for the RAPP Agent ecosystem wiki.

Key facts:
- RAPP is an open single-file agent ecosystem. Every agent is ONE .py file.
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

MIN_CONTENT_WORDS = 60

def produce_refill_delta(stream_id: str, frame: int, batch_size: int = 5) -> dict:
    """
    Find bare articles (< MIN_CONTENT_WORDS) and produce LLM-enriched replacements.
    Deltas carry _refill_id to tell merge to REPLACE existing content.
    """
    ts = now_iso()
    agents = load_registry()
    agent_lookup = {a.get("name", ""): a for a in agents}

    prev_state = load_json(STATE_FILE)
    all_articles = prev_state.get("articles", [])

    bare = [a for a in all_articles if len(a.get("content", "").split()) < MIN_CONTENT_WORDS]
    random.shuffle(bare)
    targets = bare[:batch_size]

    if not targets:
        print(f"  No bare articles found (all ≥ {MIN_CONTENT_WORDS} words)")
        return {"frame": frame, "stream_id": stream_id, "completed_at": ts,
                "articles_created": [], "threads_created": [], "reviews_created": []}

    print(f"  Found {len(bare)} bare articles, refilling {len(targets)} this frame")

    delta = {
        "frame": frame, "stream_id": stream_id, "completed_at": "",
        "articles_created": [], "threads_created": [], "reviews_created": [],
    }

    for article in targets:
        title = article.get("title", "")
        category = article.get("category", "")
        tags = article.get("tags", [])
        old_content = article.get("content", "")
        article_id = article.get("id", "")
        generated_by = article.get("generated_by", "")

        # Build context based on category
        context_hint = ""
        if category == "agents":
            # Try to find the agent in registry
            for tag in tags:
                for name, a in agent_lookup.items():
                    if tag in name or tag in a.get("display_name", "").lower():
                        context_hint = (f"Agent: {a.get('display_name','')} ({a.get('name','')})\n"
                                       f"Description: {a.get('description','')}\n"
                                       f"Category: {a.get('category','')}, {a.get('_lines',0)} lines\n"
                                       f"Tags: {', '.join(a.get('tags',[]))}")
                        break
                if context_hint:
                    break

        prompt = (f"Expand this Rappterpedia article into a complete, substantive wiki entry.\n\n"
                  f"Title: {title}\nCategory: {category}\nTags: {', '.join(tags)}\n\n"
                  f"Existing stub content:\n{old_content}\n\n"
                  f"{context_hint}\n\n"
                  f"Write a complete article with 150-300 words. Use ## headers. "
                  f"Be specific and practical — reference actual RAPP concepts like manifests, "
                  f"perform(), BasicAgent, the single-file principle, quality tiers, categories. "
                  f"Don't repeat the stub verbatim — expand it into something genuinely useful.")

        content = llm_generate(system=SYSTEM_PROMPT, user=prompt, max_tokens=600)
        if not content:
            print(f"  [SKIP] No LLM response for refill: {title}")
            continue

        if len(content.split()) < MIN_CONTENT_WORDS:
            print(f"  [SKIP] LLM response too short for: {title} ({len(content.split())}w)")
            continue

        pk = composite_pk(frame)
        delta["articles_created"].append({
            "pk": pk,
            "_refill_id": article_id,
            "title": title,
            "category": category,
            "tags": tags,
            "content": content,
            "author": article.get("author", random.choice(AUTHORS)),
            "source": "llm-refill",
            "created": article.get("created", ts),
            "updated": ts,
        })
        print(f"  [REFILL] {title} ({len(old_content.split())}w → {len(content.split())}w)")

    delta["completed_at"] = now_iso()
    return delta


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
            pk = composite_pk(frame)
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
        pk = composite_pk(frame)

        # Generate 1-3 replies (LLM-only, skip if no response)
        replies = []
        for _ in range(random.randint(1, 3)):
            reply_author = random.choice(AUTHORS)
            reply_text = llm_generate(
                system="Reply to a Rappterpedia forum thread. Be helpful, specific, and conversational. Reference RAPP concepts like manifests, perform(), BasicAgent, quality tiers, the registry.",
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

        # (Automated agent reviews were retired 2026-08-18: RAR carries human reviews only.)

    delta["completed_at"] = now_iso()
    return delta


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
            pk = composite_pk(frame)
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
        pk = composite_pk(frame)

        # Generate 1-3 replies (LLM-only, skip if no response)
        replies = []
        for _ in range(random.randint(1, 3)):
            reply_author = random.choice(AUTHORS)
            reply_text = llm_generate(
                system="Reply to a Rappterpedia forum thread. Be helpful, specific, and conversational. Reference RAPP concepts like manifests, perform(), BasicAgent, quality tiers, the registry.",
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
        # (Automated agent reviews retired 2026-08-18 — human reviews only.)

    delta["completed_at"] = now_iso()
    return delta


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Delta Bundles — merged deltas folded losslessly, one file per window
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def delta_file_bytes(delta) -> bytes:
    """The exact bytes save_json writes for a delta, so the bytes of every loose delta file."""
    return json.dumps(delta, indent=2).encode("utf-8")


def _reject_constant(token):
    raise ValueError(f"non-standard JSON constant {token}")


def _bundle_window(frame: int) -> tuple[int, int]:
    first = frame - frame % BUNDLE_WINDOW
    return first, first + BUNDLE_WINDOW - 1


def _bundle_file_name(first: int, last: int, part: int) -> str:
    suffix = "" if part == 1 else f"-part{part}"
    return f"frames-{first:06d}-{last:06d}{suffix}.json"


def _new_bundle(first: int, last: int) -> dict:
    return {"schema": BUNDLE_SCHEMA, "first_frame": first, "last_frame": last,
            "file_bytes": BUNDLE_FILE_BYTES, "deltas": {}, "sha256": {}}


def _bundle_text(bundle: dict) -> str:
    return json.dumps(bundle, indent=2)


def _entry_order(name: str) -> tuple[int, str]:
    return int(DELTA_NAME.match(name).group(1)), name


def bundle_paths() -> list[Path]:
    """Every bundle file, in name order."""
    if not BUNDLES_DIR.is_dir():
        return []
    return sorted(p for p in BUNDLES_DIR.iterdir()
                  if BUNDLE_NAME.match(p.name) and p.is_file() and not p.is_symlink())


def load_bundle(path) -> dict:
    """Read one bundle, refusing anything that is not a bundle of the window its name claims."""
    path = Path(path)
    bundle = json.loads(path.read_bytes())
    match = BUNDLE_NAME.match(path.name)
    if (
        not match
        or not isinstance(bundle, dict)
        or bundle.get("schema") != BUNDLE_SCHEMA
        or bundle.get("first_frame") != int(match.group(1))
        or bundle.get("last_frame") != int(match.group(2))
        or not isinstance(bundle.get("deltas"), dict)
        or not isinstance(bundle.get("sha256"), dict)
        or set(bundle["deltas"]) != set(bundle["sha256"])
    ):
        raise ValueError(f"{path.name} is not a {BUNDLE_SCHEMA} bundle for its window")
    for name in bundle["deltas"]:
        named = DELTA_NAME.match(name)
        if (
            not named
            or any(bad in name for bad in ("/", "\\", "\x00"))
            or not bundle["first_frame"] <= int(named.group(1)) <= bundle["last_frame"]
        ):
            raise ValueError(f"{path.name}: {name!r} is not a delta file name inside its window")
    return bundle


def load_frame_deltas(frame: int) -> list[tuple[str, dict]]:
    """Every delta for one frame, bundled or still loose, as (file name, delta) in name order.

    Selects exactly what glob(f"frame-{frame}-*.json") selected before bundles existed.
    A loose file wins over a bundled entry of the same name, just as a newer file of that
    name always replaced the older one."""
    pattern = f"frame-{frame}-*.json"
    found = {}
    for path in bundle_paths():
        match = BUNDLE_NAME.match(path.name)
        if int(match.group(1)) <= frame <= int(match.group(2)):
            for name, delta in load_bundle(path)["deltas"].items():
                if fnmatch.fnmatchcase(name, pattern):
                    found[name] = delta
    for path in DELTAS_DIR.glob(pattern):
        found[path.name] = load_json(path)
    return sorted(found.items())


def _unfoldable(raw: bytes) -> str | None:
    """Why a loose delta has to stay loose, or None when a bundle can reproduce it exactly."""
    try:
        value = json.loads(raw, parse_constant=_reject_constant)
    except ValueError as exc:
        return f"not strict JSON ({exc})"
    if not isinstance(value, dict):
        return "not a JSON object"
    if "spec" in value:
        return "carries a top-level spec, so it stays visible to RAPP/1 frame discovery"
    if delta_file_bytes(value) != raw:
        return "its bytes are not json.dumps(delta, indent=2)"
    return None


def _fits(bundle: dict) -> bool:
    return len(_bundle_text(bundle).encode("utf-8")) <= BUNDLE_MAX_BYTES


def _with_entries(bundle: dict, entries) -> dict:
    """A copy of the bundle that also holds entries, kept in (frame, name) order."""
    deltas, digests = dict(bundle["deltas"]), dict(bundle["sha256"])
    for name, value, raw in entries:
        deltas[name] = value
        digests[name] = hashlib.sha256(raw).hexdigest()
    order = sorted(deltas, key=_entry_order)
    return {**bundle, "deltas": {n: deltas[n] for n in order},
            "sha256": {n: digests[n] for n in order}}


def _place(bundles: dict, first: int, last: int, entries: list) -> tuple[dict, list]:
    """Add a window's entries to its newest bundle part, opening the next part on overflow.

    Returns ({bundle file name: entries placed there}, [entries no bundle can hold])."""
    parts = sorted((int(BUNDLE_NAME.match(name).group(3) or 1), name) for name, bundle in bundles.items()
                   if (bundle["first_frame"], bundle["last_frame"]) == (first, last))
    part, name = parts[-1] if parts else (1, _bundle_file_name(first, last, 1))
    bundle = bundles.get(name) or _new_bundle(first, last)
    trial = _with_entries(bundle, entries)
    if _fits(trial):
        bundles[name] = trial
        return {name: list(entries)}, []
    placed, too_big = {}, []
    for entry in entries:
        trial = _with_entries(bundle, [entry])
        if not _fits(trial):
            trial = _with_entries(_new_bundle(first, last), [entry])
            if not _fits(trial):
                too_big.append(entry)
                continue
            part += 1
            name = _bundle_file_name(first, last, part)
        bundle = bundles[name] = trial
        placed.setdefault(name, []).append(entry)
    return placed, too_big


def _write_atomic(path: Path, text: str):
    partial = path.with_name(path.name + ".partial")
    partial.write_text(text, encoding="utf-8")
    os.replace(partial, path)


def fold_merged_deltas(through_frame: int | None = None) -> dict:
    """Fold loose deltas of merged frames into bundles, losslessly and idempotently.

    Every loose delta whose frame is at or below the merged boundary (default: the
    state's tick_count) moves into the bundle of its window, keyed by its original
    file name. Loose files are removed only after the bundles on disk have been re-read
    and reproduce each file's exact bytes and SHA-256. A delta of a frame that has not
    merged yet, one no bundle could reproduce byte for byte, or one in HELD_LOOSE stays
    loose. Running it again changes nothing."""
    if through_frame is None:
        through_frame = load_json(STATE_FILE).get("tick_count", 0)
    report = {"folded": 0, "kept": {}, "written": []}
    bundles = {path.name: load_bundle(path) for path in bundle_paths()}
    home = {name: bundle_name for bundle_name, bundle in bundles.items() for name in bundle["deltas"]}
    windows, duplicates = {}, []
    for path in sorted(DELTAS_DIR.glob("frame-*.json")):
        match = DELTA_NAME.match(path.name)
        if not match or path.is_symlink() or not path.is_file() or int(match.group(1)) > through_frame:
            continue
        if path.name in HELD_LOOSE:
            report["kept"][path.name] = "held loose for owner review (HELD_LOOSE)"
            continue
        raw = path.read_bytes()
        why = _unfoldable(raw)
        if why:
            report["kept"][path.name] = why
        elif path.name in home:
            kept = bundles[home[path.name]]
            if (delta_file_bytes(kept["deltas"][path.name]) == raw
                    and kept["sha256"][path.name] == hashlib.sha256(raw).hexdigest()):
                duplicates.append(path)
            else:
                report["kept"][path.name] = f"differs from the copy already in {home[path.name]}"
        else:
            window = _bundle_window(int(match.group(1)))
            windows.setdefault(window, []).append((path.name, json.loads(raw), raw))

    placed = {}
    for (first, last), entries in sorted(windows.items()):
        entries.sort(key=lambda entry: _entry_order(entry[0]))
        done, too_big = _place(bundles, first, last, entries)
        for name, items in done.items():
            placed.setdefault(name, []).extend(items)
        for entry in too_big:
            report["kept"][entry[0]] = f"too large for a {BUNDLE_MAX_BYTES}-byte bundle"

    if placed:
        BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
    for name in sorted(placed):
        _write_atomic(BUNDLES_DIR / name, _bundle_text(bundles[name]))
        report["written"].append(name)
    for name, items in placed.items():
        path = BUNDLES_DIR / name
        on_disk = load_bundle(path)
        if path.stat().st_size > BUNDLE_MAX_BYTES:
            raise RuntimeError(f"{name} exceeds {BUNDLE_MAX_BYTES} bytes; loose deltas left in place")
        for delta_name, _, raw in items:
            if (delta_name not in on_disk["deltas"]
                    or delta_file_bytes(on_disk["deltas"][delta_name]) != raw
                    or on_disk["sha256"][delta_name] != hashlib.sha256(raw).hexdigest()):
                raise RuntimeError(f"{name} does not reproduce {delta_name}; loose deltas left in place")

    for items in placed.values():
        for delta_name, _, _ in items:
            (DELTAS_DIR / delta_name).unlink()
            report["folded"] += 1
    for path in duplicates:
        path.unlink()
        report["folded"] += 1
    return report


def print_fold_report(report: dict):
    if report["folded"]:
        print(f"  Folded {report['folded']} merged deltas into bundles "
              f"({', '.join(report['written']) or 'already bundled'})")
    for name, why in sorted(report["kept"].items()):
        print(f"  [KEPT LOOSE] {name}: {why}")


def extract_bundled_deltas(out_dir) -> int:
    """Write every bundled delta back out as its original file, byte for byte.

    It never overwrites: a file already there with exactly those bytes is left as
    it is, and a different file of that name stops the extract (FileExistsError).
    It refuses stream_deltas/ and anything inside it, where the copies would sit
    beside the bundles as loose duplicates."""
    out = Path(out_dir)
    deltas = DELTAS_DIR.resolve()
    if out.resolve() == deltas or deltas in out.resolve().parents:
        raise ValueError(f"extract writes copies, never into {DELTAS_DIR}; choose another directory")
    out.mkdir(parents=True, exist_ok=True)
    written = 0
    for path in bundle_paths():
        bundle = load_bundle(path)
        for name, delta in bundle["deltas"].items():
            data = delta_file_bytes(delta)
            if hashlib.sha256(data).hexdigest() != bundle["sha256"][name]:
                raise ValueError(f"{path.name}: {name} does not reproduce its recorded sha256")
            target = out / name
            if not _create(target, data) and (
                    target.is_symlink() or not target.is_file() or target.read_bytes() != data):
                raise FileExistsError(f"{target} already exists with other content; extract never overwrites")
            written += 1
    return written


def _taken_delta_names() -> tuple[dict, dict]:
    """({loose delta name: path}, {bundled delta name: delta}) as they are now."""
    loose = {path.name: path for path in DELTAS_DIR.glob("frame-*.json")} if DELTAS_DIR.is_dir() else {}
    bundled = {}
    for path in bundle_paths():
        bundled.update(load_bundle(path)["deltas"])
    return loose, bundled


def _holds(name: str, raw: bytes, loose: dict, bundled: dict) -> bool:
    """Whether a loose or bundled delta of this name has exactly these bytes."""
    path = loose.get(name)
    if path is not None and path.is_file() and not path.is_symlink() and path.read_bytes() == raw:
        return True
    return name in bundled and delta_file_bytes(bundled[name]) == raw


def _names_for(name: str):
    """name, then "<stem> 2.json", "<stem> 3.json" and so on."""
    yield name
    stem, k = name[: -len(".json")], 2
    while True:
        yield f"{stem} {k}.json"
        k += 1


def _create(path: Path, raw: bytes) -> bool:
    """Write a new file; False, and nothing written, if the name already exists."""
    try:
        with open(path, "xb") as handle:
            handle.write(raw)
    except FileExistsError:
        return False
    return True


def save_new_delta(frame: int, stream: str, delta, out_dir=None) -> Path:
    """Write a new delta and return its path, never overwriting any delta.

    Into stream_deltas/ it goes under frame-<N>-<stream>.json, or the next free
    "frame-<N>-<stream> <k>.json" if a loose or bundled delta already has that
    name. With out_dir it is out_dir/frame-<N>-<stream>.json, which must not
    exist yet (FileExistsError)."""
    name, raw = f"frame-{frame}-{stream}.json", delta_file_bytes(delta)
    if out_dir is not None:
        path = Path(out_dir) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not _create(path, raw):
            raise FileExistsError(f"{path} already exists; a delta is written once")
        return path
    DELTAS_DIR.mkdir(parents=True, exist_ok=True)
    loose, bundled = _taken_delta_names()
    for candidate in _names_for(name):
        if candidate not in loose and candidate not in bundled and _create(DELTAS_DIR / candidate, raw):
            return DELTAS_DIR / candidate


def collect_deltas(source) -> dict:
    """Copy every frame-*.json delta under source into stream_deltas/, never overwriting one.

    A delta already there with exactly these bytes, loose or bundled, under its
    name or one of its "<stem> <k>.json" names, is not copied again. Any other
    delta goes in under its name, or under the next free one if a different
    delta has it. Returns {"collected": {source: stored name}, "present":
    {source: name}}."""
    report = {"collected": {}, "present": {}}
    DELTAS_DIR.mkdir(parents=True, exist_ok=True)
    loose, bundled = _taken_delta_names()
    for path in sorted(Path(source).rglob("frame-*.json")):
        if path.is_symlink() or not path.is_file() or not DELTA_NAME.match(path.name):
            continue
        raw = path.read_bytes()
        for candidate in _names_for(path.name):
            if _holds(candidate, raw, loose, bundled):
                report["present"][str(path)] = candidate
                break
            if candidate not in loose and candidate not in bundled and _create(DELTAS_DIR / candidate, raw):
                loose[candidate] = DELTAS_DIR / candidate
                report["collected"][str(path)] = candidate
                break
    return report


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

    # Find all deltas for this frame, loose or already folded into a bundle
    frame_deltas = load_frame_deltas(frame)
    if not frame_deltas:
        print(f"  No deltas found for frame {frame}")
        return state

    new_articles = 0
    new_threads = 0
    new_reviews = 0

    for _, delta in frame_deltas:
        stream = delta.get("stream_id", "?")

        for article in delta.get("articles_created", []):
            refill_id = article.get("_refill_id")
            if refill_id:
                # Refill: replace content of existing article by ID
                for existing in state.get("articles", []):
                    if existing.get("id") == refill_id:
                        existing["content"] = article["content"]
                        existing["updated"] = article.get("updated", now_iso())
                        existing["source"] = article.get("source", "llm-refill")
                        new_articles += 1
                        break
            else:
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

    print(f"\n  Dream Catcher merge complete (frame {frame}):")
    print(f"    +{new_articles} articles, +{new_threads} threads, +{new_reviews} reviews")
    print(f"    Total: {len(state['articles'])} articles, {len(state['threads'])} threads")

    print_fold_report(fold_merged_deltas(frame))

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
    p_produce.add_argument("--out-dir", default=None,
                           help="Write the delta into this directory instead of stream_deltas/ (it must not hold it yet)")

    p_merge = sub.add_parser("merge", help="Merge all deltas for a frame")
    p_merge.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")

    p_cycle = sub.add_parser("cycle", help="Full cycle: produce N streams + merge")
    p_cycle.add_argument("--streams", type=int, default=5, help="Number of parallel streams")
    p_cycle.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")
    p_cycle.add_argument("--ticks", type=int, default=3, help="Ticks per stream")

    p_refill = sub.add_parser("refill", help="Refill bare articles with LLM content")
    p_refill.add_argument("--stream", default="refill", help="Stream ID")
    p_refill.add_argument("--frame", type=int, default=0, help="Frame number (0=auto)")
    p_refill.add_argument("--batch", type=int, default=5, help="Articles per batch")

    p_fold = sub.add_parser("fold", help="Fold loose deltas of merged frames into bundles")
    p_fold.add_argument("--through-frame", type=int, default=0,
                        help="Last frame to fold (0=the state's tick_count)")

    p_extract = sub.add_parser("extract", help="Write every bundled delta back out as its original file")
    p_extract.add_argument("--out", required=True, help="Directory to write the delta files into")

    p_collect = sub.add_parser("collect", help="Copy deltas into stream_deltas/ without overwriting any")
    p_collect.add_argument("--from", dest="source", required=True,
                           help="Directory searched for frame-*.json deltas (for example downloaded artifacts)")

    args = parser.parse_args()

    if args.command == "produce":
        frame = args.frame or get_current_frame()
        print(f"Dream Catcher: producing delta for stream {args.stream}, frame {frame}")
        delta = produce_delta(args.stream, frame, args.ticks)
        delta_path = save_new_delta(frame, args.stream, delta, out_dir=args.out_dir)
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

        for stream in streams:
            print(f"\n  Stream {stream}...")
            delta = produce_delta(stream, frame, args.ticks)
            save_new_delta(frame, stream, delta)
            a = len(delta["articles_created"])
            t = len(delta["threads_created"])
            r = len(delta["reviews_created"])
            print(f"    {a} articles, {t} threads, {r} reviews")

        print(f"\n{'=' * 50}")
        print(f"  Merging...")
        merge_deltas(frame)

    elif args.command == "refill":
        frame = args.frame or get_current_frame()
        print(f"Dream Catcher: refill bare articles, frame {frame}, batch {args.batch}")
        delta = produce_refill_delta(args.stream, frame, args.batch)
        delta_path = save_new_delta(frame, args.stream, delta)
        a = len(delta["articles_created"])
        print(f"  Refill delta saved: {a} articles enriched")
        print(f"  Path: {delta_path}")
        print(f"  Merging...")
        merge_deltas(frame)

    elif args.command == "fold":
        print("Dream Catcher: fold merged deltas into bundles")
        report = fold_merged_deltas(args.through_frame or None)
        print_fold_report(report)
        if not report["folded"] and not report["kept"]:
            print("  Nothing to fold")

    elif args.command == "extract":
        count = extract_bundled_deltas(args.out)
        print(f"Dream Catcher: extracted {count} bundled deltas into {args.out}")

    elif args.command == "collect":
        print(f"Dream Catcher: collect deltas from {args.source}")
        report = collect_deltas(args.source)
        for source, name in report["collected"].items():
            renamed = "" if Path(source).name == name else f" (the name {Path(source).name} is taken)"
            print(f"  Collected {name}{renamed}")
        for source, name in report["present"].items():
            print(f"  Already present: {name}")
        if not report["collected"] and not report["present"]:
            print("  No deltas found")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
