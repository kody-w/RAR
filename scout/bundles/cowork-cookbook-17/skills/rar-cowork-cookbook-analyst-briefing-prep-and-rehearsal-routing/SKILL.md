---
name: "rar-cowork-cookbook-analyst-briefing-prep-and-rehearsal-routing"
description: "Prep the [Analyst Firm] briefing package and get the team rehearsed before the room."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing", "rar_sha256": "8413801950006c8334bc6c08e142f18cac6ff0402eb0858fc3d65ab1ec33d313", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "advanced", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing`. The original RAPP
agent is preserved byte-for-byte in `analyst_briefing_prep_and_rehearsal_routing_agent.py` and in the RCI capsule.

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

Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyst_briefing_prep_and_rehearsal_routing_agent.py` and embedded as the fenced Python below (sha256 8413801950006c83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyst_briefing_prep_and_rehearsal_routing_agent.py` first:

```bash
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyst_briefing_prep_and_rehearsal_routing_agent.py   # or on stdin
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing',
    "version": '2.0.0',
    "display_name": 'Analyst briefing prep and rehearsal routing',
    "description": 'Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'advanced', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'analyst-briefing-prep-and-rehearsal-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '033e08f333f9f0e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/analyst-briefing-prep-and-rehearsal-routing', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AnalystBriefingPrepAndRehearsalRouting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalystBriefingPrepAndRehearsalRouting'
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
    print(AnalystBriefingPrepAndRehearsalRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6+ZfayJLuv8Kr+cHuwS60S/iee84IBFoAIQRCSO0+tpaU0L6jpaf/95cCqtw9fe+817NglwtJmRGRX0R8EZnyry9WU1+z8uXLyxFY6YS34ji4gnJipe5kmbVZGcFfWWTDn4mTpXUZ2E2dldXLpxcXVE4Z5HWQpXC6UoJ8Ul/B5Gc2teK+qifroEx+mdhlALwg9Se55USWD+6SfVDfx9bASiYluAKrrIA7sYGXleD+pMyy5BUqAZ2V5DGoXr78/MunlwB+f/ny64sTWxW89fJUtXjqGG1gU1d9CLRiNWtqeBuKiS3468tL3sPFpvA6ByVUlcBbLvAmz6uPFYi9T5N//deotUq/+unL13Ty/Hx9Gf+oTfowO7OqGtrrWLllB3FQ968TNm6tvoKLqZsyrSbWpIJYpf7rY+YPSVk++fv47ONDySuE4uPXlwyaYI1Ifn35aZKVUF/ZjN9fRyn5x59e46wF5ceffsipGjsETj0Kg1a/fnteP8XCgT+GBt5d69+h1IfPbPD15XeLGz8Pu8d1wpkvr2EWpB8fgvMyu4HUSh3w8ad/Jta5AieKg6r+/5L780MwdJIL1/Q0/KdPd5B/mUyfC3qX+c/V5tCtf2UlcPibuk+TJ1D/TPYd//8gOg5SUL0j/g/F/aMJ079Pfv6na/vPJnyaeF9fOBAHNxgddgy+TH79dlRWy58/uD9ufvjlNyj6/ynmmDWlc5fwLbHSwANV/e3bzx+q++0Pv/z8oclhrMF8/NaU8T+S+Y9wvev5A4LPUR//OBfq19Iozdp08h7pk1+z/P+Uv71OzlYcuD/uV18mv8+X8TOdjIt4U/qA4Hc5U0Fbf4fjTy+/QaZI4Woa5/4YZvm//MtkFzhlVmVePTk6kBcm0MF1kIDR+NM1qCbw7514AMS1CiCwz3Ew/kcPjxZn3uT7vzl3VvzsPFlxZj046Nsb0cGEAfk3yHLfyjce+lY+iOj76+QEVWRl4Adw1kRlFeVrCkkxrUf1cGIFyttIhH0NPkNK+jx+mQTp5Ptf0PLtLvA177/fuTZ4cJa6FEe+qpoYvI5r1q8gfa7QgcQPOuA0UFecOdAwL4CU+wliUWXxbSRkaF0VBXE8cYMSgpGV/V02xPDLKOz79++2VV2/pg+CxSePylDN4IB3cyafP0OjvTjwr/XXFDjXbPLh198+TP598p/NugsfdSiQ8p8eghZKx708gRnXJHAYdB50N6STu4d+/e2JMxSTwlIG/Rl4AXhMhhEbAfcN9KPAfsZI6q3wwPKSlSOEk6B+nYje5N1eqHR8NPL6NYO1zQU5SF2QOj2UasHlvCOZZvWkgmFZef2nSVM9qtl3u7TuJiYw9a36+2S3VGAVyWL4z2jmfRCcnKUBhP89JB73oZDyQzVZvIl4nchjjMKCWlr5tbSeOjzr4RdYPd6mQ+HWJAXt13QsnGCE6p4wD3jgIIiM83Tp59HnsMQnkB3c6k33fYw11rrTveaVX9PqmQxWObrCgcUBKvWbwB1LxN+eIVVdsyZ27/hBS0dJTy+4T6/cY/CtU/jRI4xNxD2w3oJ68gzqydcGQ1Bi8r/RZtxN4Xl1xbOnFTdZySfVeEA0djwjlI8mCdb5CZz5SIcftf+NOd4I9GsaB9DfZf+3x8g7sM8xD1JqSmiFyqp3+dCrEKJR7j3oxiAqyzFcra/pG1N/gn680xLEHWYojOAxcN4Ujk/fLL3CNByvf1Ttu5NKdwQEBtYkb+wYOt0DwLUhVNCqckycJ7wwAsGYRO01cK5/WNUESoeOhvIn0IgApgJk8zt0cgaXCZH3yiz5MTwYeyFohds40FrYUoLXiQ5jf/R/BV0AG5pxDEThw13UJAEQY2jiO8LV1cofxoxd6NNAa/RFlsCQ/L0Hng9/ROvdltF8KNVyrRpi2Y5E6oLu4dl3O5++gsYmY37dJ/3R3c+1Tn5fUv72Nb3b+M7dMG3jsRr/DhwYdmVS3QNxZJ0KMkcCngEEI+FeeF8ftfNRnN9t+fKn1vvjX+vO79VQ+6PnvkyudZ1XX2azRwV7K2CvMOdnMEaCHFRvxezzWzqNjJ1/huo+v2fk52dG/kHFA7Evk79m5h9EPOP7ywR9RV6R8dE2cMAYwM8PRGX5eWF8JsanX1MV/HD3MyZG8ox7WD3fK8nbEFhO/BL44+BHZanGgtTCGninUuiQr+l7SDwTBjJ16o9lsMp+l8j3kgod/PDfO+PDR2kNdbtjW+aDcesSj+ZX4OVL2sTxp5fUSsBf2bKM9A6jF6Iy7nhgJsF2pw7A/eq99Rkv/rgPu+cYJAc3+zKm2qfJ2KZ+mrx3nJ8mb3uA+/YqbeAm6Oex2x1VwqHw1/vY902eDV7g7qvu83EFj43N2GQ9m98/GzFmGLTYAWPJzt5TdtT4JyHwi++D8s9C9vcvVvzkjaq2xgIc1G/ZXkE7XdjOfJpAH8IshIkF+bKBE/6sBuopQdHASueOy/2B349lZY+1/HaHoX7sDn99eeOPpw+enSAcDhP1czXWuhmMV6gQXj8iCz777/SIT1GQ/GBjAmUxBIozCDonEQShHAbHCduhHIQBKIF5KONYDuV5CIFgwEYYkvEc3KVIy0aBg+MujuJQ3iNUv421PRjNwyzLYRwaJdw5bVEOwBEbdwCKoS6NA4Sc4x7DAAIi9T41gsz5XPNjjSOg7+3qiM1z6b++2BQBRwpEJbKPz3I2P1v0ZWvLV3teUh5bhfOo7jauVFZ0w+RUTtClySmnfBGlDYntC2y9WOXSQWvVbSRYiFDNENErVp4pzuftxt/Ah9GURtRBbraqwnbOZb5XXEdbr7TQITe63lXiXLIKQmtialOcj+coMWD0mMeqPHYr2y34a0qTlO51QQZJW5UuBjifLtYsvXla35Dmtjtu9KLhydDcluJqFouxttX6ChQGanaUomK2nMadpww16XjLqLmUFDnjDN0elkZiS6p5lCOM6nal2cgtl1UIakZVvsm3jW/OAkmydd3mb81umeN6VROMe91dmnhxXQYWoruKru2Fnpa26yOKFUl1KaSrrfBt0DiqWJK8Xx9p9FDnkbjRSc22tVzV+d6iuua0ddzwYMzP801D7aeFHIIi5nWeodIdykWmQZxS+1xmp2Wv9bFsLCHqh4pMthqWX9eJiJGX/Tm8pStz4dhIgPnshmqtmb0KTNq6sFNMqNVkdsZ2EbFZzLXEHpSsOW/QoNLwzTwRmwCpufXU0MmCI4i5Ga39EuMMzzUsdING5Enr5oOVS1U5N3vERkuNCI/tJSQukCSXy1rU6KTK+VBHg/kgn22SiffKlHE224SnTNR2a7w8EeF5iJG2wRHGqJHDuWR7QDOZyZaCHWBLfnO7xMW+QfY6uj42wzkkASGkJzRPlqihEoPK0KpuB7iyUAcCI0833tsLRW0uE2AcKnlKCytCVXuwQU/JRsc6kiNpFPUG51hYx4zeD6kEeCFBGd3UTcYX02NMizFCnXZycNrHnVQHNZZcwHrvAQVx0+06IZq9Rq9ubXVqTynjKITvGFMth3359jwj5PVQuMotx6e8sQ+P9BmtfIY7ubYXCIfQXttlUa5SQ8uCmKmtrR73bUn1jn1eHPmdkZBiqMaIP92dxHMpOZuwWVzxkjxCgrwNBd66aGyp+XV3PmAYV15WW7Da9zsWW16lQ2Ekwck/u/2OUvnjsNbEKsmSLL5eqmNTOMTupHYidnEKpN3f6GWj+5a3ODGRf5xJ++Nlscji9MwcaRJ08VSrj40IogjnGHSwi3xpS/sBXZ1DOzhz+35NMzTBT41jddHt07Zjzrouz8TcuRTFIPS3TL/IRISqWmOFvRukW0PX+Koe+Kifbcx0ug0a/pav8Kq02VTgJGotYEvpdDZ3yOJG1WV3UaJZJLd6vk/biF6hO53v6LYyUpmMKY8TeEJWdP7UHIKaDYpZfd2wJR8hRqaE286pex1c2QSdlsK5tjfSJpllJ0XZC6a2LHLNPPqHeUhTPsXlUu7q5nKWiqcZsopPkuafrwyN1KsoqVdgtp+LPMibIkOj5HChYzRQ9hZyUCXC0G/iIbereKtSCXkzjFOx5my5DCRIxNz2dL46pKGrgEK005Q5+am47bcx71CQKTtvh7tWlWDDClfmPLmbq/sqG3CSOBsCctr5ZlxfXG41Rxaxh/LtCdts3SgtFV+ccUxJzgE6Y1HRwzeRwJEznBBX6do4ztE4qrI9tXDMzXU9Kw4eLmkXLnAELttXBK9bfq/GeL8Mc8Y3K1rpTPm2ONnXekfuhlxAiFtiJ8tY3exqpykAnKusRNE/rXb7ZS6rpbQjZ+xxcx3KnYGd/LZdrnJ1wePiaVGfSYqOGkRUMXZnLC23WDdypBrasD7YbSil3nR9YGOpWAhHc82UfKwI11LhwmbvCZJxRDbeTWErSxeqM0xLjwGkqEshdq1Ikpl7A0NAZl4SThbbK8uc44xcRFFGrm8nPdVBJ+67heNOg9MuxKdtu6HpNJFx0dgF5I4P1Wm5wDtLEULUmgl4d+BwxAfiRVXxhqkKnDOc1YqtsVw+8nI0jw1V1wblHGT2HmP3nOxGPBotr3PRDdjyep0t9WITXS52tNqdkDJLi0ikrDzDJL8sNRNhhehylAVzt3DW3NQ+dFo7i5k5wRTXRshJPCJYbF14vRcLGSEwArWIZFE96fNI08tIWvIK8Py066TI3K+WEWe56jnBYs1QqJt5ltoKw6AanYiT+ZmQfDKbx7zBipEel8qlCcKsELyQE4meGtaXdcjz2XmDtawWVAVHkp2kSSRAgcjLcVLI+w0nbDvVbk8lvXBqbwCzLsdlqwu1tvIW5yPayAyaNcl1cUkH1lz0bn5gBX0eLz1E89tNx+Li1SAuhMU6m4HqUPvMM6W/vLB+vNGRzksXqFZutKJOyoi7kqTRN+hy2mx4whLz3XK7wbPFQeUIRQ8ACCIeM0u7ZeLVnktiAbbUw811lQTLglPLkftuX+2kDElu0a2/uHjdX4/IVTssjcPuFhhVhzjzOiadYnnBouPyknHDjUvJhLqyA4VhUcsZ6fZckoF7M+GPvETQ42DtjuFtRsXIXM+P8hB64cE6gGCHDtsNOJaO2MbLsq9P8lSUlFMRSr2CxoG0u3Gslu/DOr3mPq6dXX/aDNIeiLQhmYvuJC6kVcTfDvHRoKrN1WxXYtnmrKITU9SZRu7JyLNFBSlx7ju0ytHuPN2H0aEBnc9eCUWqN0OYMVIn2ef6vPAuKrlZ32bpBetKL0yVA6mnS3E/XwrTzJBbWzhdEZIqdYtqXfFWRtg0cSlQLZxTjiq1bd8uQVsiWear0eZ4wWjSXa2k5eLg2/JucLC4jHllY82O6z7CVqYWMECy5t7F7E7pwOvyiY2zlZdFZkKtrushEaxFLR5Qvl5gx6xzWk9oTv4uR40bqAu123SgyPYWAbdV/BUQ+Y5d8YdZ0JAiwrvUxuRuZK8d+eYI+8HFkXbO7IEkryAZzinLXyT/clyZ1MHgKJMdNLZE12GaO3ltWbVkNodLNLR6fMOXPAGSiCgwZFjNFl5bF0vJXa3j/uSrxC5f54QmMmZ2WnSZEdURcWY9WJEKcWPJQ+boANtBdHdL2tilWcQy4dFZGabnB51CbRcnudBmOeXv9N2SHyCTWPF53pKb6uJv3FQ7Rzk1x6p6mu6Qdafqa95t6UpJQkGysIMJPINNDJtB+UzWmjOLyWZPXzi3bhKFCqoM7DosLHOXdzQjU3GmAIF1ng9e72w9VOOYDWEbEdGsUvya+L52aA/7VXXKBWN2a4ygi0yYUmgvB25n7dWGOFAcO6Q2JbYDFyR0u0rIGiQZhR2uy00aV21dWzJ5WBzX27Pq7VaahJxb3mvldbHHsll0LuzA3CeZsCzWQ3CtjxsPRteZ3w5Ws7lcBHq29TUx5IlicALidnRFfrHKUjmRfMxTpuERveKH3DrprtVghGgsp7P5ISbKgxk2Dr3eqluSjJZ0fPBhwyOuFR5BanCu+1IrxkNjLDQRVeybKeIsQmW5F6buQK6KwzIXii6mD1cNc5uyjc+i5Kt0PEhZlq4tmnapBdynFDbIGh45LpK+2t0ShWMMekY1ZbiAbfri5LKzXGc5PJgd0v1x1y4WruUqG0SuQcGx4Yqrdgu/lU+qSjSHdXT2h3154NacHBC7hg1cN5yaKltf1sORzbJZot1SnuW9yxwQy2QtHrabw47ZXXjD8BSYXrLfZ4yi3hLEDdU0P6oS14fTptnkNgMpTsz5GnNT6UKaYJHGBAUEHS2LYKpp6mFtWSR2oouCnGZkpl2zhAXr7dQoC0OOmzPgp/2ZmPHrIoy826Ze4/tWYy58h0Kmxa6ti2s3fFtRN7f14pZ0yDPKL6421hNhsVbFE14PxZmTEeIc7+mc4yomaQZFFIpbJN42rh25ajZ3/blcny4CuxQzo3ewnZHCBnDhzWhyQYu+1Dh9UFYxOhPkjeA3M4LllXZ9E3BUiG8LN7jUS2QDSGlqkSuikoU5q95onpo6Nq1Ry3bqYueavLW4uK73CmwAXEsAXd01VdfLypDOyOnRY3weOet8Ok/xqZiiZAOoOd2n6DxgbGmebpxk36IIO50jZyEiKQk9mC5wDsyp0aitQvFSvxEXJ+Dt100k5x1CEic+ERAh2tkRHmRkyCQu6m774bScOX2dgKDl5/YZoxBX8IkDmbGXa7+Xj26P3YBGEGqiqoMINwbiLYMNruhq033JXk4KjeyGSGEGvqHoYCcG3U0glcPGi+c4vva2OA+mvSyaxUqWT/JuI5R7BnO4RZTN4spaUpabZsX+Oqt1gsZQTC+9eDZreGVVFXB/GMjGotiKQjjMlTADWEXLNJlIFX+7WC3YqW7P2o5uYl5qATyZ2ugB39Ih23c3NGzkhM5pgfZEs86irN3NXCqOkDU5lQpEi7oFuu9WVIASKuiEAQkb/XaodyJ78JKK6+Zw308TsQvKnCRy38tbIUzWkTNdS+GcrcsVSSMc0cP9QxWbRIwL2MHbs+25XMHN5qxZr9MLfVHSsGX4ldNNCQ411tpuitcyozpCpCIHKajbZbzAZco0lDV7nUXteR3OvGizpkIjklJ6er4cdeSirW6MhOH6oECPBduG6O0pqGJMaszw6M2JfQ/apleJbcHtebTvFaYnUtIrg72boH1Nyw2+dJordxVkYifNfAIYjMMZLeJO98LKLBftykRvF2I2zB29YuYhVvjcRoX5ps6raXO+HSwSxc8uZZlpI9dYvb4WAsjVC4e4530mAG7BiAy7XiBHl4E7EG+FdbuQDXyP6Ka7bcZQouMJGTqXYgE9KZZz4STy0HR4s2IZkQaoLS06xp6nTTAzzZoaZucGzClmWzoDL3Izl/Gm8YEhQhDdOHtl0zZ2Q2CbPo21Rb2d05cGNQCNpuWOc6YNTikzZqhU5swBFGftkrrclDYwxYYRtXlnG7xynifbndfBdml9qkXEFFC4Q7/4Fw/2N8phLrO7ZSx6Z5yZy/u5nwX81u0Xwra0lWXdkI5JVei1gYwBIqVgxJ2kTYfe76iVKyBLrrK0laOvm+Ck4PvtIdQoAbKcaFIJMgNYQiPzpZLrOauzm3BK0QgA2WqecsR0syTKwGaScuAGlm/bxWWJEHrTLgYQbsLNYlrKOW+yZktvJHbnberbImed+GbuUYEbtmAI9+It7wGtkwuPnnpHjzU9EiwBVR7t3VUuY0RwZrihw2d+088kqp6Jx1A8BTra69djBzqiIjWPyheFQoRLEr2l85vJCgpFOovB3+ORtaXQNXkwLDtTRH2ZltOUveCqeDlaktvls/V0m0FKqiCnHdA5Os17moM8PWOn9RCDQd+wLPvy6WU8fX6eIf9XXgaPh3n/Y2eKj+O/tzdM9wNkYLlf7rq+/Jes++XTS+kE0LbHaWoVN/7zwPE/nKV+/guvKEZB/eOt6/h6rKvfzuJryx//R9FLkLpNVZf9tyqLm/vB7qcXu6nG/9VQfXseYL/cl5rk42n425Gz+1jceFaeQQDy+ludfUusMgLjKMu9jbCM56cjLN+yNB7hf3tJ8Th1fr7uGI9jx/cdL7/9XxxaVmaLJQAA -->
