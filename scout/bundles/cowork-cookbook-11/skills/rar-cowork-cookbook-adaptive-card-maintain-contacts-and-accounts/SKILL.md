---
name: "rar-cowork-cookbook-adaptive-card-maintain-contacts-and-accounts"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts", "rar_sha256": "a34e594093820c8d7bd24e5dfc6a88c50c3a04265ca11d171efbe2d8033c1e9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_maintain_contacts_and_accounts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-maintain-contacts-and-accounts:ac3c12227171d7e8b4daef98c6d92dbb1625a5dd34bdb30a7b5fd2372e5fb354", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_maintain_contacts_and_accounts_agent.py` is
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

Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 a34e594093820c8d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 adaptive_card_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 adaptive_card_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts',
    "version": '2.0.0',
    "display_name": 'Maintain contacts and accounts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44265f0fe26455c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMaintainContactsAndAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainContactsAndAccounts'
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
    print(AdaptiveCardMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjWLLlX2Hifaiqp8wQOyja2mwASUhiE9qhsi2K5bLviwDV1H+fi6TIrHzV1fOqZz6M0iJCwMWX4+7H/UL++mK1TZBXL28ve2BliGglSRiACrEyFxHyLq9i+CePbfiDOHnWVKHdNnlVv3x6cUHtVGHRhHkGb99Wuds6oEYspAJtbdkJQDjXgpevABGsykU2e01F6swq6iBvkNxDUivMGvhzF2w5TX3XajlO3mbwoG6spq0RL68QkNrAdcPMR+Bq16oDO4cS60/wghUm8C9ccwBWWr9Cu0BvpUUC6pe3n//x6SWE31/efn1xEquGp14+bBpNUp4GCE/9XOZyT+1QTmJlPryhGCBAGTwuQAVtSeEpF3jI8+jHGiTeJ+Q//zPurMqvf3r7kiHPz5eX8d+uzZAmAEiTW3UDXMSxCssOk7AZXhEu6ayhhng1bZWNyNUQ38x/fdz5TVJeIH8fr/34UPLqg+bHLy85NMEa0f/y8tMIwJeXqh2/v45Sih9/ek3yDlQ//vRNTt3aEXCaURi0+vX9efwUCxd+Wxp6d61/h1IfcbbBl5ffOTd+HnaPfsI7X16jPMx+fAguqvwKMitzwI8//ZlYJwBOnIR189+S+/NDcAAsF/r0NPynT3eQ/4FMng59lfnnagsY1r/iCVz+oe4T8gTqz2Tf8f8vopMwg0Xxgfg/FffPbpj8Hfn5T337Vzd8QrwvL3OQwBSvxiJ8Q359328Xws8/uN9O/vCP36Do/6OYfd5Wzl3Ce2ploQfq5v395x/q++kf/vHzD20Bcw3W3XtbJf9M5j/D9a7nOwSfq378/l6o/5jFWd5lyNdMR37Ni/9R/faKnKwkdL+dr9+Q39fL+JkgoxMfSh8Q/K5mamjr73D86eU3SBUZ9KZ17pdhlf/HfyBK6FR5nXsNsoe00CAwwE2YgtH4QxDWyOFZ1L/spbUsv6buLwg8O5Y7pAirTRpErCBBIbAexoiPHkDe++V/Ondm/ew8mXVqPUnp3YGs9P7Bi+8fvPgOefH9gxd/eUUOATQhr0I/zKwE2XHbLWL5IGtG5fc0qdv083XUD20LH/yzE9Yj99RtAv6G/PJXFL7fZb8Ww+jclwxGCy6FghuQFnllVWEyINbIXvbQgM+QfSHDVHmS2JYTI+OvtngdETsHIHvi6MBWA3rgtA1AktyBTnghZOxPMBXqPIENoxnRreMwSRA3rCB0eTXcuwOMwNso7JdffrFhH/iSPeiZQB69qJ7CBV8NRj5/LirgJaEfNF8y4AQ58sOvv/2A/C/kX911Fz7q2MKOcccOpnjyaF+wXtsUjN1pTBZIRvd4/vrbIyijdRlsnrDKQi8E95uhtG/Jce9v90h9hAn6PJoIqqem73FDugDigoQNRAtWfv3pSzaKyOHSqgtr8AHi4+YH9B9xf+gZY1I/MYRx8qo8va+95+UYTCev3Fdk7SFfkYLuwriO3RgJ8rqBqVyAzAWZM8A7reZbCDPYxmtYTbU3fELaGro6Sv7FhqJHcFJIWVbzC6IIW9j98gT+GgG6q4d351k4Bv6ZuI/TUEj1A8wx/kPEK6ICiCZSWJVVBJVVg/s6z3pkBOx6H/dD4RaSgQ4ZGz4YY3Sv83vmKf960Ng/Bo3vp5UvLY5iJPL/yVgzesGJ4m4hcofFHFmoh53xSLlRyYjAY46DY8Vd8r1+vo0aH6z0wddfsiSEYaqGvz1Wevcse6x5cGBbwRTacbuHE+GY1aPcsIG5Mga/qsb8tr5kH43hE0QIRqoeOQ6WdDwSRP5V4Xj1w9IAOjoefxsSkEcajjjBBEeK1k5CB/EAcO+10ATVWGnPiMDEASPMsDSc4DuvECgdJgWUj0AjQog1bB536FRYMSPM9/T/ujwcR6/iEWAXgSUFXpHzmOEwS2vEBnB+GtdAFH64i0JSADGGJn5FuA6s4mHMOCg/DbTGWOSp1YDfR+B5EWbr2IGgvq+lCKVCOm4glh0MAqy0/hHZr3Y+YwWNHVPrEaXvw/30Ffl9B/vbWI7Qxm+dAc729/z9Bg7k8Cp95Cdsy3ENCz4FzwSCmXDv86+PVv2YBb7a8vaH3cGPf20DcW++x+8j94YETVPUb9Ppo0F+9MdXJ0+nMEfCAtRfe+XnsXV9/ii2zx/F9hkq/vxRbN/peED2hvw1O78T8UzwNwR7RV/R8ZIcOmDM4OcHwiJ85o3P5Hj1S7YD3+L9TIqR9CAR28PX3vOxBDYgvwL+uPjRi+qxhXWwa94p8N5LvubEs2Igw2b+2Djr/HeVPPo0RvgRwK9UDS9lYxNwxzHQB+NeKRnNr8HLW9YmyaeXzErBX9ojjbwM8xfCMu6xYC3B+aoJwf3o66w1Hny/WbxXGaQHN38biw32QDgXf0K+jrifkI9Nx31Dl7Vw1/XzOF6PKuFS+Ofr2q87URu8wP1eMxSjC4+d1DjVPaftPxox1hi0GJJ7PdryUbSjxj8IgV98H1R/FKLdv1jJkzkguY+dEzbsZ73X0E4XzlyQ069jHcLSgozZwhv+qAbqqUDZwl7tju5+w++bW/nDl9/uMDSP7eivLx8MMn5/DA6PBII3/FuD3gjvR4N+H5VYo6j7OHZH+z7avkNPw7ER/+6SP04V74/cfHmDVAQ+vYyYViGc12/3LfnLwzLo0rehGEqApPK5HgeLKSwtKAm2+2J0J4aE+DsF4+nQva8fv7z96ST932GHN8shHAzHcQZjMJcBrE26FvBmrEO7M9y1bYzGKYtyXYK0XZtALcamPBcnGBxQnk1QJDRojG9qPQ2aYmNkoCtf4f+/mvRfHrJgk8EpeowlQQJqRqIzgsVRh3UZ28XhGddzaItlHQp1CAslcZpyLAxzoU/AswHusigB3QQzd5T3nC8fBr5/zPIfsXoQBrQmTcPRfNyyHNZhMNKdMRbtAAK1CQdgOESLACg1IzyWBSQYJT9vfcZrDOcDgzGr4WgJB7vrqOfXZ/zHTKVJuHJF1mvu8RGms5NFE7LdB5fJjfaMdTRbb/a7vCXMCbo8ZmEoMUy913aEZA973zG5RT0YGCevu+VGVqwb0AM231FxRmUyE+6ScOLeKh1ANzqTnYDJNNP8eKFHS2pITx459NJySqmSQtFZJIBNmW1ZJ1n1ZWPXG+203FjsUpuckuHKkMzFw9tkV2R6qNeYfExrYIrL+WwKpNUJvWVXlbNPBxEzmisTzWS83BzL1I3EdYwl19TyD1UGei53Zjtdvog2ubrtrrw6LZ25TgOPYafajRrM9sbMIrO8edmWvNS3o2Ws0R1QTtRFxC6SlXrkKWiLs7OWV3WrZK1ICPUOg7vQPbOwzGjRAKagrK44Lw45ueBXpz1mnda4l21a98RR5Rq1xeOpDpyTuAHJZt0qTTRcJFqsJKu/yce8OTnkkJz6wKXPFolHp4FJ+fi6Y45WUcWewi4OPBxceBEXwwVFnJ3B2DfBIoiypOc3mdBldXCS65BV+9a0VxWtrLjWZfe2rnMbkW7tlWAyhcV5kVyXmG0kQWklktTbR8bYFXpkRj3csNiyphrNskjpNd+W2/lew5c232hprpQ3wNYbKWfrct3X2QTu0SrUPtKV1S2jtZeVu7NQcAaTXSUpwil/duhODN1l4jR1nIGLeXOD7WeT2SHe1k1LC7h3OcSmqFZsJvXXxjRzCWv0sNrJKdaZ0Wa6KG+Rm0vLYdpdpUreKXwZLXEjIlFfIKwykspsnxDLiVKnS1LOmHmqxbLgkQc/XhvgouSmuc/QRXad5hO84tXkdKKVE5sVoRq69WWT5swOPaz11qdcIsZ1dp8o1Oz8+OkYFs9OW2djWexicoC8wPeeIkyNzuO5SadUhBIsjpVGbg+rNT2ZWhl+VuqoppY0frzwlKxc8W0ftWmcLM4JRZEx2TaY5JqLFZ9ktD031pbVR4vtZkEr6SLp0w3fwr3lufRPlhsIJ2yQV2d7yhNZuWUt4ZYsDUozbHeYX1hRWtGRtJUKMb7UqYpr+3XCbfrr4izzvu6kspHai/S4jQyxujgMeTrz2NQgUJRFqXLFaztjkK+p4jObfFPHF0/B58vbJjxNIjbMp1lcuuaqvwB9OyF7gbC5PQZZKt1OdmiLJzW23PgZZl221Wx5mlWMTDo5Hh3DDe8Wy9M5ZuRI2l1XzdFysagQTGOrpQUTkIyV08vt1jhTm+UgFXlcLG28OQmXfE2cFsFOKKjJtLZ00Gr7ldfFxx6daeCaoftQVkx5g8XCpDqWLr2zTZSNJm5rHVFRkcJUmdZRb5tEFMItcu82VhJvVuuKTZcmUPWu5YUizqy5h263ochlR+AM6CG94fx6igsQokoSVkxvn21pc1pnWn4xuW4ohV7an5i60WnbQGcqH0reSlYaoIirq2caTZpqC9y4bRazgXft2K6VW5Wez8cKU/dMWuqFG20iNLgqKCV2iSo485uKH5uixa3CmMWWT8Aav/bbgtim8YJbWUI9kN2aGVKGOBJgW6w0Oro0E2pneZv5LmCn00zeTFkp0MpLZkiHsyhJqlCVhOpx8bRekCy1yAGbCNLUxy8xel1lUZnNOVl2aFXwCUNXLZAxauuJHNkDk84x5bAfeveq+1rnbRRCF4WUTQdC5/chKoQxN/Db9ngpp1yr9pYinimuPPe4v+GOxboBK8gTlqcrnLy69RNOIQt8ia2Z5Z6bCYURg9NtXnK4LQWlIS9dk0r9NDcsYr9cs467oxm+WNMqd7uUeFOeGi8pbuzqpi23fbbau950Gs6026nfpT3PUYdzLF8I4PabHXnyaHdoXCJyhDm311Kq6GZTbB9Ubk+sZnkt7pwo6snJxKs2dM1L22vGQGyyAeXOEt7raOBGtbcEZryYq36AFu1+pSoUVejW6VAlxlAetONVOU0yByUn1XrbcsFedv3KX+K1rbVSxpc7isdwyGn7RZIcYhzkw0ErB9vCjx1Y78uzvlb13pPP3ulcpOUUH3QUqNSBM1cbK7op5L7k0hoSjRS72f5aiMssY33V9MSu3+1jwOokvkhE20Exi+w0d4dXeysQMKoh1A3XLSbVEtKtccRmG1tTTjLpnllCLFrQKXp3FtEraqzlUyGvKArghsj2DcNNVzvNb6VTcTEvuWNdxGk4oVOGJ8+xv2NTAl/3/cbpIzNdwBIc1uuDjhHDCZzmk66+XXQ+PBlccyaw3JFyMhYkTlrV6R4j1EW9j/gDdbWwVVuuA+VoFHCm66vDii26HTUEWGTIeeqJQ96mF85dBph2zCQutkn+xmWKknIlYBfDpfUgjYnzoYeRGBY3QxbkMqYTI9O2oWbXXE1Xfhnbk9lggErdiTuCjx2F7FaLIVzPfXfe4n2+PoSi0su3VRircA7JD8GiDq8mHOB6gTFbGU5vSu1XBdjv1XNpVPx0Tden+DTXibOPco22xM+1VBlbfGUdBEo2ddM5T4qjk81EPSbCc1iqgdypO8VYBrMg4tUbm+9r8hqYPLGzEx9t9vlJ6s3lIvDLMDQtU6hJAR7gzQHPKes8DfjNnte56fTgTVP5sFwzNnc5onW9PEg7PW/lwbV1JypvZzisw50vWfNsI2y9W0ORE/Jy2GAbGpM4wljxeIz7wpoBxpxobgrTz5N22p7kws6Mm4rRSrUYknpCAEdBu4ugir66A83O2UXrHN1xwq3TcS51z9hiY61Y3ZVPxqah19dAkgvSu5iSM9OMhORn10SmcnM2YBbPn1F7G2+sbhcepWMCUi6nieS2W5dHBsWitLEYci8eCSY5ohiKtx53XnEGF3lze3LmVvxCsJyoSNTzWqI3k5neXZbJnp9nuYKds6BebJyUt9d8Vux9u4gX1W1v9/NDUzlFVAtxkhlzcNgureO0Jo2eEg7h3HXEDactzNsBFml6PammvuXAYNL0NpBMxc+4RLClQ2AIk3KbbqK1uTvmdO3Gm9rpVHUq75W8C+X1YjKLojkr5sFsX1daJKRuVvY6BwFGC7w4r68Dns33TkHcbstyoU430jCtJ3BnWS7Z9VbW9MleBLLMsnaPG13ap/xtrZvtlNns2Z4ociLXrpC/jOyozC5np3RlhWcjKtxnS3M1MxTzmFUps+kP1zqUOzNUdgG2VoyiZIua5/0kpHQ8B9YmEvfLJVQcb/Rma1ccXi/aqAgnDLm7StAEotS83nLBHr3x4jJsSXJYG0RhdTlvCknuZ5l0LrC4OaV0eWk6IVrb5UKKB1TNFvsq5rJkrmfYujy3TVOa8yMz3QQLrT9H68NVmnVKcFr0sSGsRINzwKl1xb3mdMzG1QLU9Wwt3C5MhZoMcHjKabmNq9Vmt9JOXUpok12P5rqWnYI1r5fL7W1fpmqpVvn8KB5xRllCoiT7hLoJl62Lch23taqrdcNKu+xMFC/43SW10/m8Hop4ObHoosnytmjIgFleFtOBC84oXUwy3l8BIqISC6XOIN80Jw91AmWqVJqjznm+sYtV4pRhu5v0mxhm5/Kqq5G+YzRu0y5LhxL5dW7WmZiy1TG1PXAL9WUyGN0Z3R570s+JbMEThy2YzQ9ckjO5nnalx5xvvSPGR+PC7VJdZTtUt86z7pBicphhi3nTEPv1zRHsK1nS7j7oTIXdXpaGo27wk+uU/jDvGPFGZJE5uxEmWobqxA4m6LXhnTrA6tsGEwm49SDJydG59fSFAhPGO3Ue5l2y+aqRu1mL2xXhm96sB6fOnMz2ti309c12TLqM9LVcEu1pVaOUmkgkSC5LSlHxzN9quy11nk2YpBmmByNKMhXd6Zsi98N9ImG5FIJFO19eUaLPoo3XxmgXMjfgJWUPDfV0f3MImja8Dp52PWJwPNzay6lBemfa01aQV/WF3VItgalDq+4MoFXajaVJdeCrOKa1bjkh8dm14kG0GybbYUsQ0/m84y9BQVhTr5iyrrqxWxcLmPJqRxxDH+n9ggpn+pWYg7m+WQl4mqDzNNglERc1dXqcGGtq4/vq/gpO5sE35odNYVLCdr058/QOkFtfEnbTZaFFRGRRcHC/gIESWYuQCYnWeH/GnM51BLhyda5wh+KJ4LBA0w50kmAr0jSXRU+86iw4+0CYXqfzQZ9GRyOramkqmIfBdAlhNdwYi6xiuTkBc5LUJ11Ieypy57PYu7ScfFTos0CLVCgNJL49T8TIc7L95CZee2J63p7225g/YdgB58xa2DDiVmJIMcg19Oopu+2pqpjLPAhldC32iZMpfeNpA9vMciynmU5e2bPdrsdkfGaLmbc+RZxfdUemYRb7m3ma9MPywOMCSdR0rw7x+dyvZCyb4PVUJWWe21Xzw4xeMhtDT1qlKjqm8g9NeV0sLovekfjrJGxkcbUyzkF4Sa5mSPTb7IILE8AH1VG6BIrgWIPm0aS3XUWoxPXzCbmidaFTWY3QesmY1RrHKUxVrNsIJ3xdhkRZB/QypDQ2TbRZq+OHkBbYecdRu5NmYVceyzWGZsxFg6c3uHeh0GNNHXiniWFWmc2NJyU4Gi9O/WzVbpx4mGLdyjs1TnO11QkpLGk4s0xq3r/UB18+R74tivNrTxrzrdFyhYZj3oTyzQi9hPV1j3OOsvRxWncTs1YzkFIysanSq5FW+Gx5JA16hlnpakngXIWZW36eXn1uSU31RlhVGHEuFUHi2flqdlIKFu4yaW0XzNbJCjtcrfllBX3Ce7Vd6Oya8cxmGRw8GKgpWwsh7pqz9nK4bq8TlZtb6/m0Yb1Jo7P5HGBmQKgarOTptBEzzdbzbZ20DHvjagMwWwxbd6xns6vpZEVslXVw7ae+WmmXa7PlwXpgc6oULIU/FMcTo04sOEksuvJqVDt/e2G0E+Dc2YXZsmLhL/1jIdDXa5QkRK0udpp97Y6UK2NU3BBddjFT9GzVagJ4VQuoZVkZfbdw5yLRc5ylLANpkdp5cFNvPMqbyuTCVJ0FzZgRdQE0bXrozmG39FkjaqnZLSnPF6N01BU/i7EtWM6nHBnxlL5Eh4VzEX3rBklEkAq2UDsR427+bSECU+PnttvaM0HIZrR09pnK8Ynlubt4DXM27YncXLLQbweipnBpZsuGhQ2WXQE58ajCJs4zyLWzSFocB7E/iNOhTGmVX8l2cumLXuLogmVjPGMuAiuqlmfPg0601uncPNdXYS7uXWEpBCY+AfpuugM2oyerOBOtSXxbUfiytfMZl7nZ1q+PcCSdiVMO9gbDyVJJ57iXTy/398MvbxjK4PSnl/HtwfMdwL/74Ni/hcX7UyrBkNinl/93zy8fzxI/3hreXwkAy327a3/79wz+x6eXygmhcY/HzjCN/efjy//y5PbzX3myPEoaHq/Ax5eeffPxgqWx/PtD8DBz27qphvc6T9r7I3AYirYe/2tM/f58KfFydzYtxjcc3zn3uAAz2Gnem/y9bPMGvIz/fWV8mwfc0Pp66D9fIHx6cQcY19Cp3wmaegdVMTr+fJs1PucdX2e9/Pa/AbfMZygOKAAA -->
