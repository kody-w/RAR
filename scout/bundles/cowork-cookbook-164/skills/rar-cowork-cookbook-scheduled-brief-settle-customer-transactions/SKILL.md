---
name: "rar-cowork-cookbook-scheduled-brief-settle-customer-transactions"
description: "Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_settle_customer_transactions", "rar_sha256": "0beda0fb47b40e9a2f349fe217d14ded71ab64c48fed4c669945855fc79bb9e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_settle_customer_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-settle-customer-transactions:f08b7c7cb1c3007e87918133fe924275bdc83867294ad01b8f73bdaefe633f43", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_settle_customer_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_settle_customer_transactions_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Settle customer transactions Scheduled Email Brief — Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 0beda0fb47b40e9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_settle_customer_transactions_agent.py` first:

```bash
python3 scheduled_brief_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_settle_customer_transactions_agent.py   # or on stdin
python3 scheduled_brief_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Scheduled Email Brief — Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_settle_customer_transactions',
    "version": '2.0.0',
    "display_name": 'Settle customer transactions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c719fdd5924f8a15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefSettleCustomerTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSettleCustomerTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(ScheduledBriefSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZPiyLLmX9HkfajuS1aifcljbTYChAABAm2AutqytIQWtKIVqaf/+4SAzKq6ffrM7TPzMJRlJZI8fPfPPRT5+5NVV0FWPL0+qcBKEdGK4zAABWKlLjLN2qyI4K8ssuEP4mRpVYR2XWVF+fT85ILSKcK8CrN0WO4EwK1jy44BkmRFGqb+Z7sIgYeAxApjpKyTxCrCHt5HSlBVkMypyypLoLCqsNLScgZOJeJl8EYAkAKUObwOB4ZZm4LiHwiUGPopcJEqQ4o6RVzIuEMgfQtAFHcvUClwtZI8BuXT66+/PT+F8PvT6+9PTmyV5TclgTsZNFNvakwfWmjfKQEZxVbqwxV5B92TwuscFFCzBN5yoU2Pq59KEHvPyH/+Z9RahV/+/PolRR6fL0/DPwVqORhTZVZZQcUdK7fsMA6r7gXh49bqSmhnVRfQbgspoXdT/+W+8hunLEd+GZ79dBfy4oPqpy9PGVTBGpT98vTz4IIvT9Aj8PvLwCX/6eeXOGtB8dPP3/iUtX0GTjUwg1q/vD2uH2wh4TfS0LtJ/QVyvUfZBl+evjNu+Nz1HuyEK59ezlmY/nRnnBdZA1IrdcBPP/8VWxgIJ4rDsvpv8f31zjgAlgtteij+8/PNyb8ho4dBHzz/WmwOw/p3LIHk7+KekYej/or3zf//hXUcpqD88Pg/ZffPFox+QX79S9v+1YJnxPvyNANx2MDsgJXzivz+pu6E6a+f3G83P/32B2T9f2SjZnXh3Di8JVYaeqCs3t5+/VTebn/67ddPdQ5zDVjJW13E/4znP/PrTc4PHnxQ/fTjWihfT6MUFj7ykenI71n+P4o/XhDDikP32/3yFfm+XobPCBmMeBd6d8F3NVNCXb/z489Pf0CsSKE19aP+X5/+4z+QTegUWZl5FaI6WV0NkFOFCRiU14KwRLRHUX9VpeV6/ZK4XxF4dyh3CBFWHVeIWAzQB+thiPhgQeYhX/+nc8PVz84DV8flOyq93QDz7Q6Pb+/w+PY9PH59QbQAqpAVoR+mVowo/G6HWD5Iq0H4LU0g1H5uBvlQt/COP8p0OWBPCaX8A/n6dwS+3Xi/5N1g3JcURssKbxAMkjwrIKJDBLYG9LK7CnyG8AsRpsji2LacCBn+q/OXwWOHAKQPPzqw0YArcOoKIHHmQCO8EEL28wD5WdxAtBy8W0ZhHCNuWEDXZUV360gwAq8Ds69fv9pWGXxJ7/BMIPdOVI4hwYfCyOfPeQG8OPSD6ksKnCBDPv3+xyfkfyH/atWN+SBjB1vGoxFBDVeqvEVgvdYJJCuRIVkgGN3i+fsf96AM2sE2hcAqC70Q3BZDbt+SY7DgHqn3MEGbBxVB8ZD0o9+QNoB+QcIKegtWfvn8JR1YZJC0aMMSvDvxvvju+ve43+UMMSkfPoRx8oosudHe8nIIppMV7guy9JAPT0FzYVyrIaJBVlYwlXOQuiB1OrjSqr6FMM0qpITVVHrdM1KX0NSB81cbsh6ck0DIsqqvyGa6g90vi9979kAEV2dpOAT+kbj325BJ8Qnm2OSdxQuyBdCbSG4VVh4UVgludJ51zwjY9d7XQ+YWkoIWGTo+GGJ0q/Nb5qn/atr4mAgQ4Tam3AYD5EuNoxiJ/P8w0wwW8KKoCCKvCTNE2GrK6Z5uwzg2WH+f4OBI8RAzwMDHmPGOSO9Y/SWNQxiiovvHndK7Zdid5o5/dQGVUXjlxn+o9eLGN6xgngyBL4oht60v6XtTeIauh1EqB3yD5RzdbXkXODx91zSANTtcfxsQkHsKDqUBkxvJazsOHcQDwL3VQRUUQ5U9wgGTBgwVB8vCCX6wCoHcYUJA/ghUIoTZC717c90WVssQnlvqf5CHw9gFtXBrB2oLywm8IIchu2EESsQGcHYaaKAXPt1YIQmAPoYqfni4DKz8rswwIj8UtIZYZIlVge8j8HgIM3XoPlDeRxlCrpZrVdCXLQwCrLLrPbIfej5iBZVNhpK4Lfox3A9bke+71z+GUoQ6fusKcKq/JfE350D8LpLyBkmwJUclLPYEfOTpvce/3Nv0fQ740OX1T/uCn/7e1uHWePUfI/eKBFWVl6/j8b05vvfGFydLxjBHwhyU3/rkvQg/30vu83vJff6+5H6QcXfZK/L39PyBxSPBXxHsBX1Bh0fr0AFDBj8+0C3Tz5PTZ3J4+iVVwLd4P5JiADxY2nb30XfeSWDz8QvgD8T3PlQO7auFHfMGf7c+8pETj4qB6Jr6Q9Mss+8qebBpiPA9gB8wDR+lQwNwhxHQB8NGKR7UL8HTa1rH8fNTaiXg722QBlCGCQz9MuywYDHB4aoKwe3qY9AaLn7cJ97KDOKDm70O1QYbIByKn5GP+fYZed9x3LZzaQ23XL8Os/UgEpLCXx+0H5tQGzzB3V7V5YMN923UMNI9Ru0/KzEUGdTYAUOLzz6qdpD4Jybwi++D4s9M5NsXK35AR1lZQ9uE3fpR8O/p+ozAKMJChLUFIbOGC/4sBsopwKWGjdodzP3mv29mZXdb/ri5obrvRX9/eoeQ4ft9arhn0MD735nyBve+d+e3QYh1YzXMYjdv3+baN2hpOHTh7x75w0jxdk/Op1eIReD5afBpEcJhvb9tyJ/umkGTvk3EkANElc/lMFWMYW1BTrDX54M5EUTE7wQMt0P3Rj98ef3rMfq/AQ+vHsrajMM4NuYQKMoAluEwFiMID3A4iTOU7ToswdIMzpGWi2I26zGE7VpwVqMhEUlAhQZ5ifVQaIwNkYGmfLj//2rMf7rzgl0Gp2jIDLWBa6GeTTI2iQLOwj2C5DyAY4yLkS5wGcyyadIhWQ+4pEPTHEdSLEV5DsPZNgewgd9juLwr+PY+yL/H6o4YbxBvk3BQH7csh3UYyJ1jLNoBBGoTDsBwzGUIgFIc4bEsIOH6j6WPeA3hvPtgyGo4V8Kprhnk/P6I/5CpNAkpF2S55O+f6ZgzrDHO2EqwHh3R0fU6JoOaOmarrQeO5rHPTkxB8UvUOszSIgwc38BVCY+LMFHJfEIYm+10QU92uApoG4fPsmCf0kDkLYrHhdTF3ZTZbdFyvtemtL44uJIpoHnIHC7BClsdN+cIy461Ihw7/RJrlqk6tnWQg+1OuqAHsnA9r9GLTQmjYCxiOebkE0YZmphYnJEfRonDzkfWaHk9zRcXyGG1z1kD1drRMjE44xypl3PcR3LRVsrWjpft0T/vF6MzNj/gUx2cI9zb9eUIpHY7GmEXpzleuXGKZsdsa+i1inVJGSREbhjrAtSCjAqnqDSttgeZ2bgipSVFrjpnQnLn/cpqdichJFFqwUdLMVTrS+R3XrqSbfkoBsvugOELMo221+CAblFJxs7r4xQ/XkJzFh5iXTxkl1KV6HLRkOShMbriopioBzrpQhnrRhaKlaAbag535kzbLKM+PYVzPYnKqGuWE57M605oHDirLw/UQY7jilZ3fO1me7sVJq5ILC/nmdm1a7pVk/UlDojrdorqZ39sK+tlbUjGtDQICUs04oQvDcN2BJ7QF/3mXBpWa2v5ZXaoDmWhqvOtboSdvRrDB9glb1wjN6XA3/XYppgI0dY9S0al9G4r59SloiyNsTsZuLwqKEe7wjvGoNPl0bRdbN7uFPpqL1YrI7EbszdDmayXh9go9qQtil5iCGotWJNaz5Pwomzml33ct1fM2ieaXx22Rw1OYxJrsmQ957s5y7XB0uYSWd4HkyuglSC5OLCV76gCx5y+hPMzWnbyOViDZB1wJ0Mqz1deqWMt6XahXskRXjkRxsEfRnWP4zYoCjMl5WnKLOZt27PajBUWJD9tPFpQlHKdjTebNOc2KYGyo6s8y4+p6boL0e/GqC2IuKiqOcBkbxlFRltLjB6RWeiazqrzqbPIFkaokb2lLqZmZF2jJlYSPvAwIbf1peNaDbvwgMHobcLnBTFHL+W8nh5ZUVp0Z2kn5WJ0DA/bTlaXCc+s60Ort0Ks9mvpVPWTJT4LDWJHGXngep3BuQtdpuNe26hyaF3Py3p0usijU3nYJZpQsIt8roy9rZ70kpawvsc183ldH6JivXAlj92Zbr02w516aZzrBqQERqzycld15+VyIlrV1lxeyqW3EIVelEVyY9l6J1xy2z8SF/E8qrs8YmcmJ5yViUFdTr4ai1s6W8iXmQqdIDRj7xS37h5EIhEsVp1Ns9hoFM4V41y7cuFraEevrUi0uJ1FOPY1X+Xa9FId1lXkEsWqdDQNm+ZbEhdPqmwcKXnKctYx11fQERtUTDPgCXoAAmWdXWV7Swrnsa6yVlqtpAWFnlVT2hpSMg5Eyocdv/ML1dbcSYzhO9kDe/XEmGLR7a243pYgg+FyN3k/yRz/eHDWdixqDq3SqZrnBsCkxXodUZupOOp7x5wk4ys5LvILJil2OVYV7YIH1XlVN0KTsri+36VllnTZuU1LyU5HWoVyUZmYq1FPJ9Oai7kd03voeEIQlV6wPstMdHNVXrJgUhUbbMRydKvNGGI/6js9S3czCmhqabkiahjncnZN58bF8Wmf2inGrgkcMlhvWMmQ5FzxdkfS2RTHK2O2frv2VuUG3eh8xhsqD/j0cNliu8jMneN5cjidLay0s+l+LqnrY0CbOU709ijEWtbxZ1PJjV1LvqL+TJqDg0jnHOavJ/MW4ychVbK9uV9JHs4V6SyqYTGsTB/daM0+k7LqaAiMXGEdOxeduSco9LFAe2+nlZRzNNm9OpXaVizy2gu4Ixkv1hVqgGLhkAwftXpTLFHSGYumitUUda7IUqQ4zlsQNKVuN02T9ugIrBq2Fo7reObkF75qmb63HTTwzWwuY6tuT13SzVmW1IsL1gtNNacBVXIonaAxak64VrBUKzQBXxuBue11aquuV2B0lVaSnpTFKdEwUcsxVbNdMR0FnKEYor3x9HXRaFqdB11ujglLCmNmteZ1LZVobJ+oruibAh1E7vo4F6gFh9vndIVJuqJR+XkG1gpzPl8KEK9a8mhtLyUT6tzpcqjCI1PLS9717WSDOXSHnnc4I8SLhazxYBSe45ibBCvBw3NG75ZMYOTFkaPl9QHgu3mrZtYosuYZ5vauSh2ZlBAIYae2qOrBGeg62sl2uLFt5SSp8mwpRhsdczvdq/1xtk+n5fQiVkFse6etyuiC7GvkXOAwE+S5H4Voxoq2Eus22ziC4sDeYoeT7iQQTpdBoMRKj9U8sYMz7VHi5ja21bELH9nRpOFjUnQn+m4CTHu3iijPD2btBS3mq7SV2qNr7i774EqtFnshWXrhXOidiwzzm6qMyBUUoUrW/LVNr/5SyGzY442Tyka+0rXQk/sDj1IJf+TXFDTZDio/ljjQHojyiqaXIIS2Yvwat/EDtoSzT63UW4jANMlgzinAHQYX9Mx1Y909hlMNpTPY6TnNVGC6gflEk8T51FuWhFrSxbTZSE4xlemZLePqxeCLWIx8kw7pzTSzeWHB77cb/JKP8O1CXXTLVbiX+HTMmMdDb7dHgYiXlLhNzxf+oq/W9TjBHfFkRdglKdYbeibxu53m7lAO1H05L86rXO+SFu+3GxnttuTWt/IQcEBLwUmGJYUe6ASOoqXinCVsF9vrstf5LXqita2/nQM3d3Z+mfUKP+1bV9uxTKx0zcr3yBBV1/x2oQmOooCmj6jcCIr1ND8u4q4c03O53vg0qnj7jbWPC0zKIvd4uJCLgNmcZJ2O9Mb0VXpv8uvYFYUjV+lkxzDzhb6cRDuygPPUJN2f1XPgosRVWV7o1Yjcm+uwzf2gRw+uGPUyL8g2X0enKzo7bVF1Zoz1ZKREvUXQBs2bcxPnx3EPW0VTiOIpFWC4T3awATzRG3mn6mFcZZYqa1POmaMRNVuu2gzWqkAe+JoOq4vTidEEzmRra2ovtqKpkVMlXgj7fAL36+7J8+NydxHiFd5JJg6ysOX3mhXVXRBmXVEr5EpcU7EZssHhmGAU0Tl97HHqyBDnBO/l9k40AGhOM9E+kydv0cVn8xzyRQ23AteZdtW6S65qeF3lJ0Y7LUdK40f59aB4Tt1fnN7xFFlyMV2z17JCbwtbkYJiGrRRuNKZXLYmRRmLYbKqL1d9WTuxKWJ+jG7naXrUKxgSeXTZOJY+FStPS9mF5kZcC5TxpiCO6t44sJejsVWXImeII14zZDbas5FoX7SqnTZLFzvo6YytKkHrUT6OBT/tdpI+qrhzO0mAsj0fceWAZlojufomWW/jU7uQl+2kzDACb/IFb3nRTJgczQyjGsbKXOfIRtlKajb1zm0ciocDo73bm7S+XhUhhfm+qfrm5djPd+MW3ycknxswL3zWJZUzhdLeHvN5jB8ny/RMEF1fX00Bz6XNdMM2q5W5OGXrplDyLZOPco4KJzN7uSykVvN4lDDLKeOTnUSZaGl5mVfpU56ifFotqZbciCKOR8BoDThlE8opcif+gePx7XxRknymHI/W1ZqcMrNMJ0cKzad4PY5if1Jhit/wvBIQsVLp2axMxha63UgHXw3mfW95jJBR+wTzlSAIDfnkk5qEXxV9eZ1fvfF5fukYc1ztFNjptlGRG5vFfD4mHHk1wfDA5dpu2u7kfnYk1Cpa25SUoKPpfITy2KxJGhunK6axUy9mHU+qA5KTGNmzGwMb4+7x2CzNRUU52+bQXAFLzGlnRrg1YZHbbWMfgqYmT+ElumwTepqkx4u9UOcHbaL5bFJflXbXw2Z8dqGFRL6o6uDS49YpE9bSaBmtDycdu26mrReMoZfSNnf7WQKM7ajeWS0PJlh4aqUDZbV7hqx6W1ycKNfGwoDbNYyCMbOisE/4lphRXnc0qoK0hB70TVNnk3K/oFpRZOY1iXPMgecWs3QzruqmGfHNfh6KqWNyYx1C1OFAsEw+I2OHSCR3s2bLFTmnAz5ZRbLvO2vVsvayE597a7JwZqSAW+vVJPQ5vDa3xj4g1/tZ17fCaD8/LfIV44/4drUYHSaka+NjbcrkfVVPznDTFHd1n1m7bXs5dGW8OZ4YuDGJdkAkpXzru9lBOOyVsYLXI9NRWFk9e2xfjpe0Np4u7XTtS+Pw0FBjnp70XFOPfImSKZM4KPl67s0uG2DTnmsRE87vzOWaskW/Xp7L0fyC79wQW1CjmtU9zh5jPraPU/XqORMIyQeTZ5OmLeWAsXpuhvY6ICyuysDpKoxO8+pqFtbIjWnAXAsDTaOjvKDPsJ0cnLj0AJun8tTy+dkIq3Fvcly0cPsDJsLa24crTChQ3g3HabZwK29kROpsZ+83M46bk7ndxqFcUCRZ8V592YmbdUs50oyfKkmkzYhS2l+3Iw8/VaxKYa7fQAi1sOmcVCapWJ5TLlucryQ39Tf7cT0ZRdNS9AqcwpV61q1PLdvp7Urn7RG3KRe83xLtSQqv4x09Z91rNRVQF852LWzzzaQYeVW0bXrCOpxCrhFwLc1zM4xnst178RRncBM/zafGct3hzklhTG3tzVxPqSKsrsbWdsRO51LJTLjTjG8Uj8frBX8QNgvvHLbi4epMJM+9EKMRZsIg1FUtTCfOZhvg6JLYMScbKGu0chJgManZ4GTuBGlOHIxOXhfOtDEIRxhZI54/ppxYLoF/BNapXWaLduN1OepVfCdrrdOoruJGBJbOKVoWgkpjgvluOkVrwrX1xTXFx9ZuKtpV1dBFnjbEyGDFUJizuAyYAwnUyVhLgmp8YlfHI3fhytHSmg8GEvtdR18DBh8fTgFFVU3rjSkAN8OhOLZHAk5E9ZhR+E6pKEXTBZQU48BYuB6VMnmpgYsbVuKU88rAYFcE54WzdqfxMz5X55g33mlaerKWkUN4/qhj2HO/smtNlNeb0+LSUyDnk50zCqWFe93z3OzQdzxvybOJOD8Qk0nCJPNsSptsMz76aOPZXmOrjuOOFllj8OsJqezcGdOs9U3dG6Qjc8z2AtgZNRpRwqzzV8SUd464b/XjfjqVAjbbkrLFm73ZUZtNI3EVoHY1BZsmtl4dY6Js+3BN1kVzZfh8PL5m+vVgjNatx5R0Y5Yz23QnxM6FQ+p4Qa43zQgUSj9pbZ6kYocyTAc/lUale3TOX2Z0xV5R/IwSJbrY0rYzC1qBJpMZwPfV9DzT3HA+CXKM9VtjFOUb+tzNkq1Hz6/sZkFsMxD0ox6/irJ9IsF53PLUyTwDuot4nv/ll6fnp9sB8dMrhjIE9vw0HCE8DgL+3ZfHfh/mbw+uBEPiz0//795h3t8nvh8d3o4FgOW+3qS//nsK//b8VDghVO7+6rmMa//xCvO/vL39/HfeLg+cuvsZ+HDyea3eT1kqy7+9CA9TF64rurcyi+vba3AYiroc/jamfHscTDzdjE3y6vGq+Tvj4J2scAejsjfHKoOn4a9XhgM94IZWBR6X/uMI4fnJ7WBUQ6d8g5vSN1Dkg9mPA63hTe9wovX0x/8GtnEfOAsoAAA= -->
