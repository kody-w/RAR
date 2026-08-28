---
name: "rar-cowork-cookbook-scheduled-brief-report-on-and-analyze-trends"
description: "Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends", "rar_sha256": "7fd71e70637888e061bc35bc8ee641eeaa95ee4cc288ba09b1dd7b17f1833e0f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_on_and_analyze_trends_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Report on and analyze trends Scheduled Email Brief — Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 7fd71e70637888e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_on_and_analyze_trends_agent.py` first:

```bash
python3 scheduled_brief_report_on_and_analyze_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_on_and_analyze_trends_agent.py   # or on stdin
python3 scheduled_brief_report_on_and_analyze_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on and analyze trends Scheduled Email Brief — Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends',
    "version": '2.0.1',
    "display_name": 'Report on and analyze trends Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-report-on-and-analyze-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d4675d0d7a2fcd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/report-on-and-analyze-trends'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-report-on-and-analyze-trends', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefReportOnAndAnalyzeTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportOnAndAnalyzeTrends'
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
    print(ScheduledBriefReportOnAndAnalyzeTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOj1pbtX+Flf7DdVCUgRtUNRzQSEhqYhYSQy5FmOCAk5lHg9n9/B0mZZV/fe99zd39o2RUl4LDnvdY+R/Xri9PU56x8+fKyA06KiE4cR2dQIk7qI/Osy8or/Cu7uvAP4mVpXUZuU2dl9fLpxQeVV0Z5HWXp+Lp3Bn4TO24MkCQr0ygNP7tlBAIEJE4UI1WTJE4ZDfA+UoI8K2skS+9qnNSJ+wEgdQlSv0KCrETqM4CLqjxLq2gUmHUpKP+GQI1RmAIfqTOkbFLEh4J7BK7vALjG/Ss0CtycJI9B9fLlp58/vUTw+8uXX1+82Kmqb0YCfzZaZtzNUFM+9fmHDebdBCgmdtIQrs97GJwUXueghHYl8JYPPXpefV+BOPiE/Pu/XzunDKsfvnxNkefn68v4nwFtHF2pM6eqodmekztuFEd1/4rwcef0FfSybsq0QhykgrFNw9fHm98kZTny4/js+4eS1xDU3399yaAJzhj5ry8/jAH4+gLjAb+/jlLy7394jbMOlN//8E1O1bgX4NWjMGj169vz+ikWLvy2NAruWn+EUh85dsHXl985N34edo9+wjdfXi9ZlH7/EJyXWQtSJ/XA9z/8M7EwDd41jqr6/0vuTw/BZ+D40Ken4T98ugf5ZwR9OvQh85+rzWFa/4oncPm7uk/IM1D/TPY9/n8nOo5SUH1E/B+K+0cvoD8iP/1T3/7VC5+Q4OuLAOKohdUB++YL8uvbTlvMf/rO/3bzu59/g6L/n2J2WVN6dwlviZNGAajqt7efvqvut7/7+afvmhzWGnCSt6aM/5HMfxTXu54/RPC56vs/vgv179NrCtse+ah05Ncs/z/lb6/IwYkj/9v96gvy+34ZPygyOvGu9BGC3/VMBW39XRx/ePkNIkUKvWm8+2PY5f/2b4gceWVWZUGN7LysqUfAqaMEjMab56hC4P8PmIJxfaDUYx2s/zHDo8VZgPzyH94dRT97TxTFqncMervD49sDDN+y9A2C4dsTDN8eYPjLK2JCHVkZhRF8gBi8pn1NnRCk9ag/hxgJyhYii9vX4DPEpM/jFyRKkV/+ipq3u8TXvP/lDsjRA7WM+XpErAoKeR29ts4gffroQaoAN+A1UFmcedCyIIKg+2kE7SxuIeKNEaquURwjflTCcGRlf5cNo/hlFPbLL7+4TnX+mj4glkQeXFJhcMGHOcjnz9DFII7Cc/01Bd45Q7779bfvkP9E/tVbd+GjDg2C/jNH0MLNTlUQ2HNNApfB9MGEQ0C55+jX356BhmIg0SAwo1EQgcfLsGavwH+P+m7Ff57QDOICGG0Y6WSM6shpUf2KrAPkw94nyY3Ifs6qGnJXDkMNUq+HUh3ozkck06xGKliYVdB/QpoK3LX+4pbO3cQENr9T/4LIcw3ySBa/c9+4CL6cpREM/0dNPO5DIeV3FTJ7F/GKKGOVIrlTOvm5dJ46AueRF8gf769D4Q6Sgu5rOlInGEN1b5lHeOAiGBnvmdLPY87hUAB5feTtp+77GmdkO/POeuXXtHq2g1OOqfAgPUClYRP5I0n87VlS1TlrYv8eP/AYAJ5Z8J9Zudeg8a8mhw92Rxb3keNO8sjXZoITFPK/YT4ZPeBF0ViIvLkQkIViGvYjsuNoNWbgMY3BAeGpBnbRt6HhHXLekfdrGkewTMr+b4+V93w81zzQrCmhMQZv3OXDYoCRHeXea3WsvbIcq9z5mr5D/CeY/jueQd9hY18fvrwrHJ++W3qG3Ttef6P7e27LMV5jtyB548awVgIAfNfxrtCqcuy3Zzpg4YKx97pz5J3/4BUCpcP6gPLHBESwg2B076FTMugmTE9QZsm35dE4REEr/MaD1sLZFbwiFmyZMQMV7FM4CY1rYBS+u4tCEgBjDE38iHB1dvKHMeO4+zTQGXORJbCSf5+B58NvRX63ZTQfSnV8p4ax7EYA9sHtkdkPO5+5gsYmY1veX/pjup++Ir/nor99Te82fmA+7PZHEX8LDgK7LKnutTqCVQUBJwEfdfpg7NcH6T5Y/cOWL3+a8b//a9uAO43u/5i5L8i5rvPqC4Y9qO+d+V4hVGCwRqIcVN9Y8NGEnx8t9zlLP0OVn58t9/nRcn/Q8QjZF+Sv2fkHEc8C/4IQr/grPj6SIg+MFfz8wLDMP8/sz9T4dASdb/l+FsUIurC13f6Dgd6XQBoKSxCOix+MVI1E1kHuvEMwzMjX9KMmnh0DET4NR/qsst918p2KYYYfCfxgCvgoraFufxzoQjBueuLR/Aq8fEmbOP70kjoJ+CubnZEWYPnCqIx7JdhKcFCqI3C/+hiaxos/7vjuTQbRwc++jL32CRkH3E/Ix6z6CXnfPdw3ZmkDt08/jXPyqBIuhX99rP3YTrrgBe7b6j4fPXhsicbx7Dk2/9mIscWgxR4YqT776NlR45+EwC9hCMo/C1HvX5z4CRxV7YzEHdXv7f5erJ8QmEPYhrCzIGA28IU/q4F6SlA0kCH90d1v8fvmVvbw5bd7GOrHvvLXl3cAeebgOUPC5bBTP1cjR2KwXqFCeP2oLPjsvzVdPmVB+IMTDRTGBj5LABZnSJbjOIAzhOuRtOtxADAUAYDjTGkAKM+bcJzr4FOX8H3WJdiA4EgS4AGU96jVt3EoiEb74F1ATomJ55PMhKapKcFOnKnvUKzj+DjHsThUChni26tXiJ1Ppx9OjhH9GHTH4Dx9//XFZSi4ckVVa/7xmWPTg+PamKucJZSNsdl+mFI1e4ynGhkeedZ3SzDlRcLZSFeIuqa+NzZ11TdSEZ1jqqcsZo1lEtq1jQXEfG5KQ+nmlD0rr4LD4ilPpRs/TYuFb/ira+HkMqmfzXmcJuiCs1Aa3TtifqBjm+tZu3C75hAxjU+sj1StnArpyE7RU9AZhbNcXGozZktvWCpoQVx2EO79UjtoYM4WKHuyEyLDrW5/tuh058SbzL3mB+22o6s0N+1WEyMpqw2dXYJuRYuM1UQkziWHG8d5R7PouSaNp9NNwQBthTHHXQ904pD0V+dwOc3qarAItz2hiwmx3ETNicm2gDIDp2bwStqI7M5ZmVbtsmec7kpLXC2pJZ8Mh1rYN+B4ucXTgyTosVMmRMi5xZy6NUl93ai+pB2ciWUn+SrKnaK+sdXmSqCUZ5s1I6KDtyubmGRap13uYknQeiM5FVy8R7tAnkhHPSGuZVx4fWMbMk7PehHPjY4gSs9dWRPNjLRQPTEmW26g0hu9tCh2nc5QY773LWLSmjM1ii6HTcINEyk+1Ha5rIn2dFXQerc8nN1rKN5otF+XS5MTcZQxbmXNbvo4vzDJdWLSK3S4UrgDchK4MwicKKBlaludL8Wpx0+q2wiEHIP2ONdZlLx19nzXF6RxVvW+1fql1ZDCjA3c81mcmCK27g122ol+zRrCriDjWB0W2yNBnKphTxM7K1asibc9nrVIDDBbdNf7mHI0kKSyb5fYTbkOm317m7muzs2m5Wpd653Y+F00ITQ7UIMbKzpRMjEP2om2tgbnSXJJVUNFVOGa3MWsvBWvqRkrabBUzCBeCa0aHFfK8bhQalIAVpaRFbnNul0w7MvO1agwoOTJUY3VfalR2nG1pjFsx6K6T80PlzxDh0HfaOy0l/w53R6apKzWWXj1SjUnbGex6Bjr4lRT71y01S5e2vUmDgtUduetdHHXw1k869VK9+ZFL4noxo8L21gW2HYWt6nYZJNI9BbUprrudjB/M1G7qZOFcBaNgPR6KyuyON4TJ1K21NUC99Cp1BwUSsXIxc0KQVjrq02z4jdzqot2V9PaHKlurjfyUm0HqdlPJXyVs5SbNoFzyI7eZiIOShfkZq70Q+uwmIDx/kVQTjvDne5tWvRt0kvUG1rt96GyiFTM2Sj7g7ShSfUmGLVkCs4k3GVxswxAZgc+cRA0ajI37Gm3zg+bzUK5LC5REINoRy1WsVhcT0HNhTaGA9SgZngeK2SLZR1uHoijGZteFbbDikhDirQU9YQlcjnXJ6YR1ROezzmCPlGL0CimllpSfr2Id1h+2VZNOjt6FyYXSmaV4juwz+16b+UTGs8Sjlm2UcIw/k2Vgrb2rs3ePSjaVGycGccUBXTRn+KzwNZ7CltulGOdyTCk9cxlBlasPJUbYi6JCUEBUu1vnVpKN9tMGiymdyczzyHmQPE7N94zahYMNHYsTyXB0jcuS7W0WKtRcmOl82l9Ovn8pnftZqfxYJjhzbylN66ybBxl4vLacmO46BS7YTNso7jCcS52xyo7zOZbCwVDqHApmctqC7eI63x3ATvtulQ2+ZV3myK6Xpa3yTkbynVS1RIHYpLP6y6zvIQmBoZpV0OixAdGE2Q+FRZ2OV0ss62QmV2NLpipjqbcbKVvYlk871Et5G1w3SyOybne4UcnaJsSu0jZkgtVAy8SCidLI/QY11G785W5EY0lb7t6Tg56ndj9BfWWtugJ4ZYOT+sJrc8cXmlFalpGXCTwEat3jC2pTXvpOXA8XCf+Md+sI2c4wnvTi3WNV2sCPeFNryqb21oWSnxdXVYaceEnNR5WaxB2B7zA0PnlMmDyCtWDHgssK2BQ87bDtmqhJ0uAOpcwDpfJopyfG0tTaWnbRYxilrXHOnw+JzXZPYWQvzazm7MVdyBU02hw6Hq7DTeWSesHZpEpdkwkQrfaVNzmeiObfVevnUR2VMayFt4MJfOQDjGiWC8chXbM/To3HGfODrv6UO6uCc+qEiji282bJ+615r288kK5mcRJSi5nvkmWW8bZTuOK8S0DWKi4mM4yag9Z0G7mQ1qxg8FzFV337W1pqvM6VoZ5vdZiiWDsnuRuls4BrNkQ21ONe7OFnup2u8FdznFTA0/a9uILnjllLvpJTbSbheXWYiURc0uthu2t3wRWleo1gZNrlvWpNhOOYlYEmrlnFGPjLQ7GPtjSpSrEwr7MZ5QHWeVYz6/ntNsK5rpeH6XOpCU9bCBJ0Qeq4ZT1vj8Hm3qZTJX9+jC7uvhssk4pJYsyEOHbycl1CTTmd7N6UuLh3mYlNRncvRFxc2kZzabdNs7o0MM05gLcBTGz8IuUy0Rpxzl/lrLguJRj2+b2hdNBvuPnqCCbpVeHLY2vCHrOuGrN+qjX0jEROMaaYHCXx+hJPVx3kZ4Cs9eNbcz2Fu47Jtot/cWxXEmaYoLUmJm9WxwcpzDSW7zd7G9lSjehFB8h/OVn06J1TZfiMxHSYH7bOZtZDgemYZtHF30+E6qOCQWsPYGrFnn6lQ9yDbv1GCuUQkbSi3R/87iLLtY20KdTrXbEMyGVh/pgHHBlzxtoawdLDpsKunoxfdaaN7l6URxg72RauLrlxJoxZuvbaJUQfRAMSXdYyUc4rfgMaaAysRVCkeQ3OLuPseVusS6sxTxekw2/grM7ntEro9Oup0rup7xH4WnPbppyRxdeXq5FLjQX80TGiF1u6iFIDv1ZAlvFWBrEke6KmT/18O02nk2TTZRp1aI52MshaJTtcGiaDSecUb7L1anV1hATdrtNBlFVCYVluSLFee2ry8VVRb0tru4aSufJanvWL0evCFcrSdGY+Fgs4uOENCRdsMuaEqLGcfslR92kBZWQ14tkzmI5ndtts1vt8Mt51RsSfmzPzeKiyHo6r+H2yDzf2EXA7NWCzxwDjTta2kv7uOq1Lh3k0o70bM0IFlhQAwhZU2bYzc1nPC7fhvKkKsAwpxXn4E6vprlb996GNlbuxCkCVsurDRZVh/xsb1fMbaDUKlmTpx3vBreVbAinIvcMek6QUozadYvP6D3hCzfRYoBPV1t9zfYmbLxN4E3MIho41tD4ZsKsIVfIU5WoN7Uh7c7dPpJkNodkdKtiFU6CTSnsF413pVfsWcgkuQUox1SlcRIKj1HDBU1UV8xwdm4IDo1K5wnjM0K7yk2GcrZ8apVNuAt4dzLwOa/Mr6mkHwid5fL9UeD8HjcHfBYfFue0V7ceWk/ZgW9Qo7wY6smC825VXA7zWIn7OuPqSFaPmlATPXOWlZRe9KcTmDSSfV5zPh30VhXP1dMUHB2i970Sjw/nYlEEJn8eMrj4wA/7Nt6i88l5RoWG14BDKQ6DKFPFWWICrYNVO536K9/otz6aTpJ4aYbnyqAcvErikKP6xnOLVeuj2SFPRGkbrbWmkzSOlmNK5K5zVj07A72smYkqany3Y6c7md/knhKLG3xaegy55ReZJ8+6bibMDkt1MXeX2e1YyptY0K4Ut92LeJNqDtXiO2k/c3Fe4IRrgQ1yWCoXRpja/NLb6lmxl0/TxhzOwtFaxIno76lDGjXSLrmESSzM2bPoHq7EgLJWr6JSuj6aS/S4nBxQyrpE3sTZnMiJO3XxISq24eAeB8v31ke7Sm0+NbFteLylQ+uXG1MYyqGa11pAQw7k0rJp3Vrfc1pNBv6y1ASCUVhI2gplt0LMtLc+g9f1at657U29nqRzsMVngxeRx7ooUv3kmJcQBzebL5arqWk2ehNNzugkT9gJA0lKE5c7Y83Gp/2V1SJeuGC3iT3gOx6WX3xwHVbpNKzjF55hzWw2b/mrmZJKdriYx0mgKhJuYK0Y2WRjthf7yAVxoB4tcAy9QV5tm4E6W1QUpJ63mgC6Z4fZaegBKDGM6TmMmncby4bbgBajciykiwke+BUmlCJ32/mxcDFEpg2PlB1zVCRRdb6Bc/TNUhR6bbdYGA+G4SiJVkuWu1sI3cVJDjLQsU7eVlzeLpf4Kpa5gtWGcHJg2IPdXPC1zIhkiZcT/zKjQKicrN7oZj4I+jhEZRvXk27auXJi+5hO1OjJPXFZZfhbrOnSXscG3GHZRu0iSeT8vb/I0SOp4woXe3WJyfixPoZFxnU4jfVt3fLdaa4cqubW4JcK32nGDVxsj91hUtwSLTXRVNyutmyJaZmSZuuS68CGxIPU9nEapebuvKzULD3ylqdrk+XBT5aTKqB96wa3TN58vToqt6t3w68grcaJmplEu8tMmpLFydV3LBUeGTxaW3S/DnE9OKfZAW4uyzjlTPoaZup8JaCt4UsiszmSyRQ0zmlV6gJFx26qxXtbsyVnprVCyMhXjE8djzLLoVXl4xw4y0vJzNpoRbCHDMXcWYcB0KOqjXmwY5Z7GcX9obp4q6uB63lSd/N4Ri5p19ZW63MNW8e/oPZeXLIXO9nELGocd3AhvgwIoZ3Vtxm7ZNaxe1HaDTro9pXurYgQo1M8va2UhZ4UMmMe1zbWpXRfXWqF8JrInFAKgffL29rTaQAJn5txGqWQdL9ML7xGozYk1GZNNWgPn6xJscpqOyArnmIkoyoV1FcpS9i6uU4rLIHpJKB8cJqFDinKt5WEUzvNbGj7igsdv9ecI4zcfEUFk81VX+4v2EIzcj9NT9LAcXG7lItbcWPN0w0Fe6ny3Xyh7VQSXfeUh4mXE+V7m7ie9NTOV6cMJZG3hZ5ht26g0OMlmmgML3tYMxdLtlLbCSbUfYXfGjYTch6LjwvyqE9pSkhkgBlB0MqXVdOyYrK61IFeC/3SJGbEeV6uZyZFHLDD5IRx7Kp3OsbIerUsU6kNi5vL7YJz4dKXfsodyYFlHVWM1ouaXIte0zDcVmSvZFqQcPQoUKvQ6bIPu9hcaaLAZwYedGvB2FNbShaCRaJ73iQXc1zkhEYfpn4cTWtlcpHXaOxcDYg9Gtu2BsGcddXTLlwuFc0G6+HMoMm8K/ArTzLPDjtLFUYu5LKFxLgZ7IuawkFUuLCHOlMkc5IzklXR4HRiVZli0ALOV6CfBWS4nKezE+m0s0BflqpnJ7DbTcJcySVgybVaBaicQUgmZ5XbNfPDhLnMLDJvc0nYS4REpFm7mjZxr8miawtDt2QgZh/QrhZNwfTPt3mHk8BYzDkmnzPmjQdKy5xv00vbujJ72SuBH2Rwq38iNCxUxCMaBVx/5Xn+xx9fPr2Mx9bPw+f/0s/P4yng/9hh5OPc8P3HqfvRM3D8L3ddX/5r5v386aX0Imjc4yC2ipvweVT5d8ewn//KzxujpP7xS+/429qtfj/Hr51w/HdML1HqN1Vd9m9VFjf3Q+FPL25Tjf+Wonp7Hn6/3J1N8vEk/e+cGxOTlcBzqvqtzt6eR+9ROv5qBPzIqcHzMnyeVH968XuYxsir3kiGfgNlPnr+/NUEOjx5xV+Jl9/+L4l88sU8JgAA -->
