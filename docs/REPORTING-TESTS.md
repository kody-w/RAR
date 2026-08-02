# Testing the reporting machinery

RAR reports public numbers. A wrong number is worse than a missing one, because
nobody goes back to check a figure that looked plausible. So the machinery is
tested at two levels, and the split is deliberate:

| Level | What it covers | Where | When |
|---|---|---|---|
| **Hermetic** | every pure transform — rendering, splicing, joins, guards | `tests/test_reporting.py` | every push, in CI |
| **Live** | the parts that only exist because GitHub is on the other end | this document | by hand, after a change to the collectors |

Nothing in the hermetic suite mocks the GitHub API. Faking an API mostly tests
the fake: it passes while the real call 404s, and the first you hear of it is a
report card full of zeroes. So the live behaviours are driven by a human doing
the actual thing and then checking the actual JSON.

---

## 1. Hermetic — runs in CI

```bash
pytest tests/test_reporting.py -q      # ~0.05s, no network, no token
```

Fifteen tests. The ones that matter most are regressions for bugs that shipped:

**`test_critic_index_resolves_a_dashed_publisher`** and
**`test_a_scored_agent_renders_its_score_not_not_yet_scored`** —
`state/critic_reviews.json` keys its map with an underscore-normalized name
(`@aibast_agents_library/x`) while each record's own `name` field holds the real
dashed one (`@aibast-agents-library/x`). Looking up by dict key silently resolved
*nothing* for every publisher with a dash, which is most of the registry. Every
report card read "not yet scored" while real scores existed. It failed silently
and looked exactly like "no data yet" — the worst way for a metric to break,
because the broken state is indistinguishable from the honest empty state.

> **These replaced a test that could not fail.** The original
> `test_critic_lookup_resolves_dashed_publishers` re-implemented *both* lookups
> inside the test body and compared them to each other. It asserted a property
> of `critic_reviews.json`, never of `publish_reports.py`, so reintroducing the
> bug in the shipped code left it green — while this document cited it as proof.
> A test that cannot fail is worse than no test, because the documentation
> around it becomes a false assurance. The lookup now lives in a named function
> (`reports.critic_index`) that the script itself calls, and both tests were
> verified by reintroducing the bug in a scratch copy and confirming they go
> red. Do that for any test you add here.

**`test_splice_replaces_block_when_end_marker_is_missing`** — the report block is
delimited by `<!-- rar:report:start -->` / `<!-- rar:report:end -->`. If someone
truncated a card mid-edit, START survived without END, and the splice appended a
*second* block instead of replacing the first. Cards would accumulate on every
daily run, forever.

The rest pin the contracts that make a daily rewrite safe to leave unattended:
splice is idempotent and preserves human text on both sides; the seven feedback
channels agree across the collector, the card, and `stats.html`; no two channels
share a reaction; snapshots refuse to overwrite real data with zeroes; and an
unknown download count renders as an em-dash rather than `0`.

> **Why the em-dash matters.** "No release has been cut yet" and "nobody
> downloaded this" are different claims. Printing `0` for the first asserts the
> second, and it is the kind of number that ends up on a slide.

---

## 2. Live scenarios — run by hand

These need a real reaction from a real account, because that is the thing being
measured. Each scenario is: **do the action → run the refresh → diff the JSON.**

### Setup

```bash
export GITHUB_TOKEN=$(gh auth token)
cp state/discussion_ratings.json /tmp/ratings.before.json    # baseline
```

Pick any agent thread: <https://github.com/kody-w/RAR/discussions> — every thread
is titled with its agent's `@publisher/slug`.

### The seven feedback channels

React on the **"How did this agent go?"** comment — the one carrying
`<!-- rar:signal -->`. **Not** the top post, and **not** the download-tally
comment; each object is counted separately and a reaction on the wrong one lands
in a different field or nowhere.

| # | Reaction | Channel | Appears at |
|---|---|---|---|
| S1 | 👍 `THUMBS_UP` | `worked` | `agents["@pub/slug"].signals.worked` |
| S2 | 👎 `THUMBS_DOWN` | `did_not_work` | `…signals.did_not_work` |
| S3 | 😕 `CONFUSED` | `stuck` | `…signals.stuck` |
| S4 | ❤️ `HEART` | `regular_use` | `…signals.regular_use` |
| S5 | 🚀 `ROCKET` | `shipped` | `…signals.shipped` |
| S6 | 👀 `EYES` | `want_to_try` | `…signals.want_to_try` |
| S7 | 🎉 `HOORAY` | `saved_time` | `…signals.saved_time` |

```bash
python scripts/discussion_ratings.py fetch
python - <<'PY'
import json
a=json.load(open('/tmp/ratings.before.json'))['agents']
b=json.load(open('state/discussion_ratings.json'))['agents']
for k in sorted(set(a)|set(b)):
    x,y=a.get(k,{}).get('signals',{}),b.get(k,{}).get('signals',{})
    if x!=y: print(k, {f:(x.get(f,0),y.get(f,0)) for f in set(x)|set(y) if x.get(f)!=y.get(f)})
PY
```

**Expected:** exactly the channel you reacted on moves, by exactly 1.

### S8 — upvotes

React 👍 on the **top post** (not a comment). Refresh as above; `…upvotes`
increments.

### S9 — acquisitions

React 👍 on the comment carrying `<!-- rar:download-tally -->`. This is what the
brainstem/store client taps on install. `…downloads` increments.

### S10 — release-asset downloads *(needs a release carrying assets)*

```bash
curl -sL -o /dev/null https://github.com/kody-w/RAR/releases/latest/download/<asset>.py
sleep 60                                   # GitHub's counter is not synchronous
python scripts/fetch_download_counts.py
```

`state/downloads.json → agents["@pub/slug"].downloads` increments. This is the
only count that includes signed-out fetches.

> Until a release carries assets this is expected to no-op — and it **must**
> no-op rather than write zeroes. `fetch_download_counts.py` refuses to write a
> zeroed snapshot for exactly this reason; `test_download_snapshot_refuses_to_write_zeroes`
> pins it.

### S11 — the report card round-trips

```bash
python scripts/publish_reports.py --dry-run --only "@pub/slug"    # render only
python scripts/publish_reports.py --limit 1 --only "@pub/slug"    # write it
python scripts/publish_reports.py --limit 1 --only "@pub/slug"    # must say "already current"
```

**Expected:** the second write reports `0 updated, 1 already current`. If it
writes twice, idempotence has regressed and every daily run is churning the
thread's edit history.

**Then edit the thread by hand** — add a sentence above the block and delete the
`<!-- rar:report:end -->` marker. Re-run. Your sentence must survive, and the
card must be replaced rather than duplicated.

---

## 3. Counting rules worth knowing before you read a number

- **Reactions are one-per-user-per-emoji.** Counts are of *people*, never events.
  The same person tapping 👍 twice is still 1.
- **Self-reactions count.** A maintainer reacting to their own agent's thread is
  counted like anyone else. Seed data is therefore real data — if you drive these
  scenarios to test, the numbers you create are indistinguishable from organic
  ones afterwards. Un-react to undo.
- **Attribution is public.** Reacting associates your GitHub login with that
  agent publicly. That is the point — it is a review surface, not telemetry — but
  it is not anonymous.
- **The two counts are not the same population.** *Acquisitions* are signed-in
  people who tapped the tally; *release downloads* are every fetch including
  signed-out. They are never summed: they measure different things by different
  methods, and adding them would produce a number neither system could defend.

---

## 4. What is deliberately not tested

- **GitHub's own counter.** `download_count` is asserted, not verified. There is
  no independent way to check it, and pretending otherwise would be theatre.
- **Whether a signal is *honest*.** The suite proves a reaction lands in the
  right field. Whether "worked" means it worked is a human question.
- **The critic panel's judgement.** `critic_review.py` is model-written and
  rotates models by design. Tests pin its plumbing — that scores parse, land, and
  join to the right agent — never the scores themselves.
