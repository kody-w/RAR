---
name: "rar-cowork-cookbook-dashboard-identify-strategic-initiatives"
description: "Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_strategic_initiatives", "rar_sha256": "1879d9a5d2aa2f702d6f06df68a82d70885214928866005d734a6dd06f3ce0a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 1879d9a5d2aa2f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_strategic_initiatives_agent.py` first:

```bash
python3 dashboard_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_strategic_initiatives_agent.py   # or on stdin
python3 dashboard_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_strategic_initiatives',
    "version": '2.0.0',
    "display_name": 'Identify strategic initiatives Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad51f0be9fc19d9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyStrategicInitiatives'
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
    print(DashboardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJLtX+HFfMiqUWYgEAIp+9Q5I4FAIFaJTVTWyWJxFolNbBLUq//+HEkRmdXV3a9rznwY5ckIAe5m5tfMrpk78duL2zZxUb18fjkAN0c4N02TGFSImwcIXVyL6gx/FWcP/kf8Im+qxGuboqpfPr4EoParpGySIofT1aoIWh/UiIvUIA0/jYPdJAcBkuQNqFy/STqAbHVJRAK3jr3CrQIkLCokCUDeJGGP1E3lNiBKfDgjaRJ3nFAjn5CiBHkN70GbesSrimsNqo9IXiDMjJwjrg+V1kgOQAB1eT3SxADpEnAF1Ss0EtzcrExB/fL5518+viTw+8vn31781K3hrRfmzRL+acThzQb+mwlQSurmERxe9hCrHF6XoIKmZ/BWAELkefXDuO6PyH/+5/nqVlH94+cvOfL8fHkZ/+3b/G5dU7h1A4313dL1kjRp+ldklV7dvkYq0LRVfgcRQp1Hr4+Z3yQVJfLT+OyHh5LXCDQ/fHmBEEG7oSO+vPyIQEy/vFTt+P11lFL+8ONrWkA8fvjxm5y69U7Ab0Zh0OrXr8/rp1g48NvQJLxr/QlKfbjcA19evlvc+HnYPa4Tznx5PRVJ/sNDcFkVHcjd3Ac//PjPxPox8M9pUjf/ltyfH4Jj4AZwTU/Df/x4B/kXZPJc0LvMf662hG79KyuBw9/UfUSeQP0z2Xf8/050CtOhfkf8H4r7RxMmPyE//9O1/asJH5HwywsDUhjEleul4DPy29eDuqF//hB8u/nhl9+h6P+vmEPRVv5dwtfMzZMQ1M3Xrz9/qO+3P/zy84e2hLEG3OxrW6X/SOY/wvWu5w8IPkf98Me5UL+Rn/PimiPvkY78VpT/p/r9FTHdNAm+3a8/I9/ny/iZIOMi3pQ+IPguZ2po63c4/vjyOySKHK6m9e+PYZb/x38gUuJXRV2EDXLwi7ZBoIObJAOj8XqcQH6q77ldAYhrnUBgn+Ng/I8eHi0uQuTX//LvpArp8UGq6DsZfn0jwq/vRPj1OyL89RXRofyiSqIkd1Nkv1LVL7kbwTmj7rICkBa7OwU24BPko0/jl5E2f/13VXy9S3st+1/v9J882GpP8yNT1W0KXsfVWjHIn2vzYcUAN+C3UFFa+NCqMIFc+xGiUBcppPtmRKY+J2mKBEkFYSiq/i4bovd5FPbrr7960Lov+YNaZ8ijpNQoHPBuDvLpE1xemCZR3HzJgR8XyIfffv+A/F/kX826Cx91qJDrn76BFgoHRUZgrrUZHDaWFUjFbnD3zW+/P0GGYnJYA6EnkzABj8kwVs8geEP8sF19wuck4gGINEQ5K4uqgXyNJM0rwofIu71Q6fhoZPS4qBskALCaQS/4Y6Fy4XLekcyLBqmhI+qw/4i0Nbhr/dWr3LuJGUx6t/kVkWgV1o8ihT9GM++D4OQiTyD87/HwuA+FVB9qZP0m4hWRx+hESrdyy7hynzpC9+EXWDfepkPhLiyp1y/5WDHBCNU9VR7wwEEQGf/p0k+jz2FvkEFeCOo33fcx7ljl9Hu1q77k9TMN3Gp0hQ/LAlQatUkwFoe/PUOqjos2De74QUvvtfzhheDplXsM8v+6Z+D/vuN4r/PIlxafYgTyv7FbGRe24rj9hlvpGwbZyPr++AB8tG50zKNXg/3C3ZR7cn3rId4Y6I2Iv+RpAqOn6v/2GHl303PMg9zaCtqwX+2Rt9VXjyWOITyGZFWNwe9+yd8Y/yOE605v0Isw32E+jGH4pnB8+mZpDEEbr79V/7vLIYgwSGCYImXrpRC7EALhuf4ZWlWNafh0D4xnMKbkNU78+A+rQqB0GDZQPgKNSGBiwapwh04u4DJhBoZVkX0bnow9VfnwdoDAzha8IhbMpDGaapi+sDEax0AUPtxFIRmAGEMT3xGuY7d8GDM2w08D3dEXRQYj4HsPPB9+i/27LaP5UKobuA3E8jpycgBuD8++2/n0FTQ2G7P1PumP7n6uFfm+NP3tS3638b0MQBJIx6r+HTgIjOesvrPuyGE15KEMPAMIRsK9gL8+avCjyL/b8vlPO4Af/tom4V5VjT967jMSN01Zf0bRRyV8K4SvkEFQGCNJCepvRfHTW759es+3T9/l2x/kP+D6jPw1G/8g4hncnxHsdfo6HR+JiQ/G6H1+ICT0p/XxEzE+/ZLvwTdfPwNi5OG0H1P7rSi9DYGVKapANA5+FKl6rG1XWE7vrAy98SV/j4dntkDSz6OxotbFd1l8r87Quw/nvRcP+ChvoO5g7O0iMG5/0tH8Grx8zts0/fiSuxn4C9uesVDAyIWgjJsmmEWwZWoScL96b5/Giz9uBe/5BYkhKD6PafYRGVvdj8h71/oRedtH3HdoeQs3Uj+PHfOoEg6Fv97Hvu8zPfACN3BNX44LeGyOxkbt2UD/2Ygxu6DFd7ody9kzXUeNfxICv0QRqP4sRLl/cdMnZ9SNO5bypHnL9BraGcDG6CMCXQgzECYV5MoWTvizGqinApcW1sxgXO43/L4tq3is5fc7DM1jh/nbyxt3PH3w7CbhcJikn+qxaqIwXKFCeP0ILPjsv91nPuVA1oP9DRSELahlsHTnAe66eEhN8YAMp2QQkgt3gQfUdLGY4xixxBcLkpxO5wE1I1wyCKZkOPPB1J1BeY8w/Tq2CMloG5TkL3wKI4Il5ZI+mE09OBbDMTgZTOfLWbhYAALC9D71DCnzueDHAkc031veEZjnun978UgCjtwSNb96fGh0abqURXn72FtWJDg6Nsp7iXEhLcK+iIKDbS0f29D6OnfwZMGbOL2Zny9upkhXyTWCilNiZrnKKWHbtaGwMko9LtlrV6+z88m3vHYmnsP5nKDM9Z4tUNlPRdP3yqyUXZQ9ZI6UVjurE46za8UMEFbXQQ9sGKrZ3AtrTg8rc8sF9XI5mTjWEkvKTqqH08DHieJjhmXLThLf6HXUDUHLHtzDMZzl3s6kzV2EAynFWsvNzSoWyKtRsXmIUhVL3HJcPlyNIvIBaXrmZcG2821itjEhM+V8AcSEkmwho+ScUgYzI+rw2B25K6l5cmYtLkGw62dlxbq5Pa1oyRx6c63PGHkumia7lhYSXpx3eQa6bqObw04rtDKT1+fAVeIrlLvWmi02mS8Cf1Dc68mySmG+jxvQX4zrUjtkbbx1D6zVa5ltWyxeBafaZexLe9QZ0s5SjJ+WwCmE8nw4H89COKelidfwjJNW63VfyRW50oQhwdNdZOqHmUulTUrOh6t07izLYaSC57qFj3W0s1sYQwpanN1Vuu47wtJK/BOl4GZZbDy1w6hb1hbsYKRcYc0vDEFMGl487mtuOnEjrMKqW58l8dIz7ZOznWCRj1LmBezTI3NbMLfZoWSsjRQMdqfuRfcG5u0uWOCHKp/5SioPq6VENO2EwoTF/jLvyeNMvzpWMCOSy63uzIWh8uZJIerrWkG584677Wdpg7NlE/MLG7AEpsTKlcsUe5kpVS/0wS7vDIO0WgMdtqeEYMXlWfRoNlb75qbwhl9lxq7G44ERchRXbTPfzar2JA74oR/oQUHFmjKcwuXPgnGtB5cqE24oMyzT7dbB9mEnMmbeTVGmi7Sw36q4siUMdSHyzcDr7O40YRa3m9LNyHiShhKTkBsB34bajZc63Fo0wdlKXSw7GiVtTpqGPe3nkkb2tW6yHScdrdvOjhPMAPTAp93gJ7a0VqhSONRBPB8u4coJU9K6ZD6rWZZabTfefodG/Sp2lXNyOLvO7lpObu2eB7wuOly4MQc2S4FpKtUQXfNT4rSdonlRsL2ZCwKdTuhoSFLB31QHJbFLxbLrtZ0O58ug9i4Tg8NcNsN1szl55HV+CuhYV2Y5OaBTw2DIC8nTRhNik2PcGZh9y+ouLhj1dinoPSiKC6ef+qDOmSM3H7Rs5Sd7sdOk7RCYuoP2QzavT6qyO9FS75b2ipu5c9lfcnMmudLy0q75g51naCw5mbPmAzneURxNLo197RzAuduSF6xMbcrzeZEtBY/exrjTZWmEc/ixkGxvn5XxJt2CqXK2KkuOfSZKtSUXz5eszYq7IYXLylczv9+gy5i7zKq+vk0WZzs/HOzDbksKE02BxdXmmqphz4fQM5a1mOyGTlzJDr3FguJypmIeKNM+P+zUmrvs5qIwSI3Asvol8Vwqq4/zZSOnXAzJasJetYZTmDm3xPmDHmbzRGXyHYtLOb1Qe/Q8pdc4U9/qYLPRt1cmRC9ClC80YzhWVni4Jtub3hMehoroKpztjluFX1IRJ+Wspqe35nyJ1GTtO3ycojvNmQmGRyWuzZyV+spNjlG/ZzFvmbZ1ZJ3nKh74qMTdEmNo9PaIx+kk6I7nttOKbCZz9KXPeGqPamsg0Fa0plN5mjjhleVWGbge81OzWnHbUllvbryryRxeeosW5fvJOjwyabMTWsE4ulMmNb3jOVWANMS3g1bE251jEvwGU92YUukEKGCD+dr0oltAc7SmE3j51AU+IGrR1MiCUpXuNEVVu8GAcUyu/s4466dqWSwFYX/GQjLYNUGm+zRNkDI9SAw6wTVGofJWmWmGmMQ0CFGWmBwi0+7J4YahmY0fJ4baJxfJBC0qBJ4h0dbG4pPLgZPr5fyo7ddlem2d4GhEYjVXK8KKxUVMrIVCtkCnbY1bnaUXPyvprIPZZcTcIZBdUSDohASbm0aVdKjplblvbql2XtWx6g4Wxotoobvywc8ZS1z55c7UMAYYZ4ghviy4s82eQuO0SouDK80JlSYWYeVZxlD2jertS7tjKX0qzsH2CqOZcyI1l5qE4BWghwrBcBgXdMm1dq8GV6loVzk+DhGTs6oduFknF1CAtGkOsuoy7eW407ErQRI5tdruN6cDmc1u/P4sHtYZ1UtxLWq2TuTmieIGOZ0ZPLFZ1uvrtsJExrrFt8spK5R9dKJ7Zw7vyFnCVDZd3ZpYJg7mmmZpx+i8gIk3ppQozDqhsiJCG+IQr3Uam6KGOD2Xq82GQ3mHDeJ4mgr4EJ2CtOm8fqNKO8fNDmv7dHGC2RnWaqdgiiEoz+tktxO8CbbYzS6UGZnN1eFKXFqLdWcBd6va2cWF8vXBuFD7W0kPqJMJg2Vrs2nPuEbsN53Dtp5llybfCQZm9vNin1xbUoktgVj26j6R+DxoMfZMLGOA3jb0cZYGPCzRBcgDWj/biZ24ZSZOWY4mOG4pnumLMC9Pe4o95DuFXHuSNdV3N4dP03STw4zbW0zEBzZ14Lv4Js/DyVQ4HOGCztMBpaJ+NlUnuDuVt/zamDRnTr6CAKBMUx4cTIQFwVwP+nJOqk2nNxShXDVRmGWnta8FrjBfpkQOuS4DAjWbKDKWkGZo75ql4uGhlRC5frA7jzrZGrOaTo+RtqBYc4b7KxjrGzpe4WQotyrXcz6j1Gp6qaUeY5ZEyvaTsKpT9XKSAj8KNM7RMlltrcs8P6uiRGppoCVJ0Up0oqyJ4MYxqVKyHqYeWoUVDXO9tanGqG82ptjRhuG9qx1KHm2XnDRhpzgpGwnXHtRqQ6c4cYniYaCX9tmsV4KfrXV+n5d4ZJfnTUcdvBujV5Vf5vVqmmbEGuiq4BqoT7i36TRnLZyo15rHipdkb+831cXBY7DKwZD384TGpGO7O9SMf6IJ9mQcz/pat4KASXo8ygTxMF3T5vTWJCIX6VfZIfTY7JtLbjNHSEep2oOKVU5cWlOKyVctWTs7KRfMRS04sRiShySkeGcqkEm9x2O231L7gVAad5u151XmDsyRanhMjXeRaIeKfInx/JBPTWuKbmr8VJWBvDGPtd7ON0t2SpHDcIg6VJ0ermxn72XWFzhBT+qNoM0xlqDX61wmbqy2MA5cexZECzNwJRGtk7JuCW0nz4Ywl7lJyTszELEoW82WW53eHK0ddRL5uApcrNTonhX3sBBtLGFqrrjoqqWFIhRizV4uPR7sDvtS22XmFpxZoSGnhIiqubdnIqMYNtQu9OnVFZsmq34KlifJaBl3llbCpnWDs5Jr9gl4ZbIGjhpMenfB8hgz64M4K6ppTxyoXIsocsqzurbndxxawrTmLxJ5XAu4dJ0HJbiB1S0vt9tQ5RcrmNShibYOpE3Myz13yqc0527UJVhcOBnuipYpXliTtkhnAd+szBt9rTddrjKL40IludpcVW111INtd3F5poHNQqUcZG29DrxAFYwL3uzXUdIztbSOrjK0iWg1noTJCqpVbUi4F2tzv9LcEAyJbl4DY8Nc1LI48man2ZCvFYKi8fVuXyWaVWhdE0G2Xhepu1luCC8PJWHLnToI4xluCvpqVaUX3BwW8YImGHToOlJe7k1MXhbHPtmt4qGxu4N5wuzhmrLaeTHZbftbZxSUJTiU48VhVPthCUxiKRK70Av0bgGbI7FjnG1A+EJndahC4THmM2zY2kIts53HxW1dS1FxLpfZHMtO28uROSzdXU8VRDYZ1Agoe4Wy5hh1uvDbquEuDe4W9Yre0fzZnCk7cpXt7bBH14AQaGrdrLDMGIA3W9l4sSQIxVqd2tV2qeaaL15F8lwlXn0ILycZiKt95289ZeiwrUB5S8cFykma1RUlJitPZxbkKQf0zLeBV63AabjO0MnMttGV7ey6FSQRFE3RBeVa+JIq85kMZqTQSOLCEnqWYCbLlbs1zIl4utgHwTU9a5Ng+MnRJ1FcZ6fVNFsS0/1qceXSrZ4nEmn4GjCG9uSKp0y9Odv9rBMFWWxmu8kc51ceKYvyULiqPKwr0Y6U/XAZWgOj+jRfOJHh98p5YESSI6o+t2zOvKqR3fRbO2FQMOh+cMvY/d5jWdTnQ7Gru8tEgzvQeU4at1JixZwUbBXfLxuCY/i91MzP8jD1DrmO5VUxm4nTkOw9aY9iA9pyDNeRa5GiBXe9E3fb3CbCrbZs5hNvNmz0YwNabLU4Jk62bhxdGZaePVtkYnjh5sDnOVueFMFtMfPVI+rNdbneYBzcjVfmAj+t1Uy2eyK5KfOBV4oUeDasfUuWSquFoh6kzVaIT3M/pzJ5uod9UT/39UHdRNtb2mQ+2DNXWwi1dUPNmPqqQ50nPRU7ZUFMFut5wa2aYhlu1KovygFqu82XaH72bxOCwY6sYTWiRxFBAyxmv7K4bHWRNp7ddFFtMNu9xxjillzepIsp+rGIboeK3OknjoD9RzPDFgMebkOWba/tYuYpIMkz5+yKe31R4Khfg9uNd64JJE0qhmjUy1rGGq6FxIphxDC/8b42b+NUWmzDJcfUgOO64sovcrlQYKFLpnDfD7sONKt8QGZXvmCvuLW1zcav2ggb8u7S9E5ZdSxOWUnsbkHuWGxBtrAsLrYMsZ+vdkwR5VSq7Saz9iadVkkUEvOJKfJLl/fDbXFdnPuKLIc2ZeM21L3Cp24rmW5njRof1U4MuqXv0ws7cNAg1KO2Y6z8Okuuwyy0h8pQd7uZFB6bkzhz8W6GnURMKA4OrqHBchlbYrs0yWPTBra33KKTbacou7hT0EiuWius1DXgLwt+elvLCl1Klx3FogpKMNHRDFt+CnubgGLta+hjE2oSuwf6yO4OEzGnSNKcr/cw6bzzSrEtHLBisHCpm0Nxi82MMaLGTtfxroJdJq1qQz2JVu6puO5vhUUKEqzQDS3rRUBwfpxfPH1JuV6bF/uleDvS1/XGmx0n+YCt8poImZtms40eJlonqdLKW0c74pDTOL5WvKtjOJaKye0hi7hAOSQ6s+0LbwX0balP7cbpF/RV9YVbuoTUhoN+1c3QgLbXjkqf1qhzu6i1lqUkdbrplCTuSbwQ7LCeW6HPaJsbuiOF7b7k515wAaXKFfolp3oNhKE/rMBx2i+2eSRPz6TMQk2F5AjTrSGu9GrRRhVanEVB2rSL6QRvxYKYULWeKRp2meEDhtH2cTE5+USgMAzWn1er1U8/vXx8GU+ln2fLf/ll83jK9z922Pg4F3x753Q/VgZu8Pmu6/NfN+2Xjy+Vn4yG3Q9Y67SNnseQf3e8+unffWMxSukf73PHV2W35u1ovnGj8Y+UXhLYqsOZ0LQibe8HvR9fvLYe/1Ki/vo80H65LzIr76fjb4pHNxQV8N26+doUX58H6ffXmRkIoHrwvIye585wbg+dlvj11xk5/wqqclzv8xXIeEw7vgN5+f3/AYYmw7QjJgAA -->
