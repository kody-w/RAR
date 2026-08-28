---
name: "rar-cowork-cookbook-adaptive-card-track-employee-learning"
description: "Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_employee_learning", "rar_sha256": "212de49b8e5a5792c3f4cc02919d09330c1462961bd7a2f6aed1cb62bf60e645", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_employee_learning`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_employee_learning_agent.py` and in the RCI capsule.

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

Track employee learning Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 212de49b8e5a5792…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_employee_learning_agent.py` first:

```bash
python3 adaptive_card_track_employee_learning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_employee_learning_agent.py   # or on stdin
python3 adaptive_card_track_employee_learning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track employee learning Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_employee_learning',
    "version": '2.0.1',
    "display_name": 'Track employee learning Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-employee-learning',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d65807175166c7f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/track-employee-learning'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-track-employee-learning', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardTrackEmployeeLearning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackEmployeeLearning'
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
    print(AdaptiveCardTrackEmployeeLearning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV9HU+8P2o7vEvvQNRwxCLJIQSIBAyH2jzb6KfRHy+LtPolJ1u5+v31xPTMSou0pAZp79/M7JpH57cfouLpuXTy964BQL0cnzJA6ahVP4C64cyyYDX2Xmgp+FVxZdk7h9Vzbty4cXP2i9Jqm6pCzA8kNT+r0XtAtn0QR967h5sGB9BwwPwYJzGn+x1VVl0RZO1cZltyjDRdc4XrYIrlVeTkGwyAOnKZIiWrSd0/XtIiwbMOgGvj8/TIqF77SxWwJS7Qcw4CQ5+AZzjMC5tq9AoODmAFpB+/Lpl39+eEnA9cun31683GnBo5d3YWZZjJkz/2QsP/kCCrkDvj69VBOwSQHuq6ABUlzBIz8IF8+7H9sgDz8s/vM/s9FpovanT5+LxfPz+WX+p/XFoouDRVc6bRf4C8+pHDfJk256XbD56EwtMFHXN8VsrBaYtIhe31Z+o1RWi5/nsR/fmLxGQffj55cSiODMBv/88tOs+ueXpp+vX2cq1Y8/veblGDQ//vSNTtu7aeB1MzEg9euX5/2TLJj4bWoSPrj+DKi+udYNPr/8Qbn58yb3rCdY+fKalknx4xvhqimHoHAKL/jxp78i68WBl+VJ2/1bdH95IxwHjg90egr+04eHkf+5gJ4KfaX512wr4Na/owmY/s7uw+JpqL+i/bD/fyGdJwXIg3eL/0ty/2oB9PPil7/U7b9b8GERfn5ZBzkI7mbOu0+L377oB5775Qf/28Mf/vk7IP1/JKOXfeM9KHy5OkUSBm335csvP7SPxz/885cf+grEGsi4L32T/yua/8quDz7fWfA568fv1wL+pyIryrFYfI30xW9l9T+a318XppMn/rfn7afFH/Nl/kCLWYl3pm8m+EPOtEDWP9jxp5ffAUgUQJveewyDLP+P/1jsE68p2zLsFrpX9t0COLhLrsEsvBEn7QL8n3O7CYBd22RGubd5IP5nD88SA2j79X96D/D86D3Bc+k84eeLB/DnywP6vrxD35d36Pv1dWEA4mWTREnh5AuNPRw+F04UFN3MuGqCNmgGACnu1AUfARh9nC9mbPz136L/5UHqtZp+fQB88oZTGreZMart8+B11tOKg+KplQdqQnALvB5wyUsPiBQmAGE/AP3bMgfI3s02abMkzxd+0gADlM30oA3s9mkm9uuvv7oAtz8Xb6CKLd6KRrsEE76Ks/j4EegW5kkUd5+LwIvLxQ+//f7D4n8t/rtVD+IzjwNA+KdXgISPOgOyrL+CacBhwMUAQh5e+e33p4UBmQJUOeDDJEyCt8UgSrPAfze3LrEfUYJcuAEwMzDxtSqb7lGIutfFJlx8lRcwnYdmLI/Ltlv4QRUUflB4E6DqAHW+WrIAZa8FodiG04dF3wYPrr+6jfMQ8QrS3el+Xey5A6gcZQ5+zWI+JoHFZZEA838NhrfngEjzQ7tYvZN4XShzXC4qp3GquHGePELnzS+gYrwvB8SdRRGMn4u5TgazqR5J8mYeMAlYxnu69OPsc1D9rwAR/Pad92OOM9c341Hnms9F+0wAp5ld4YGCAJhGfeLPZeEfz5AC1b/P/Yf9gKQzpacX/KdXHjFo/EVvoL/1Bt93Fp97FEbwxf/vFmSWmxVFjRdZg18veMXQ7Dd7zp3TbPe3Zgs0Ag/Kj9z51hy8Q8s7wn4u8gQERzP9423mwwvPOW+o1TfAaBqrPeiDEAD2nOk+InSOuKaZY9v5XLxD+QdgmgduASeBdAbhPkfZO8N59F3SGCg6338r6w+PAhuCGABRuKh6NwcREgaB78427OJmzrKnK0C4BrN9xzjx4u+0WgDqICoA/QUQIgF5A+D+YTqlBGoCM4dNef02PZmbperNs/4CtKbB68ICiTIHSwuyE3Q88xxghR8epBbXANgYiPjVwm3sVG/CzN3sU0Bn9kV5BfH7Rw88B7+F9kOWWXxAFSBsB2w5znjrB7c3z36V8+krIOx1TsbHou/d/dR18cea84/PxUPGrxAPcjx/BO434yxAbl3bB6jOENUCmLkGzwACkfCozK9vxfWten+V5dOfWvgf/16X/yiXp+8992kRd13Vflou30rce4V7BQCxBDGSVEH7tdp9nKvRx0eWfXzPso/vWfYd8TdbfVr8PQG/I/GM7E8L5BV+hechOfGCOXSfH2AP7uPK/ojPo58LLfjm6Gc0zBibT6C8fi0471NA1YmaIJonvxWgdq5bIyiVD8QFrvhcfA2GZ6oAQC+iuVq25R9S+FF5gWvfPPe1MIChogO8/blji4J5Q5PP4rfBy6eiz/MPL4VzDf7NjcxcAEDIAoPMWyCQPqAJ6pLgcfe1IZpvvt/EPRILIIJffprz68Nibl4/LL72oR8W7zuDx36r6MHW6Je5B55Zgqng6+vcrztEN3gB27Fuqmbh37Y7c+v1bIn/LMScVkBiAOTtLMt7ns4c/0QEXERR0PyZiPq4cPInWAA8n0t00r2neAvk9EHDA2B8mFMPZBMAyR4s+DMbwKcJ6h7UQn9W95v9vqlVvuny+8MM3due8beXd9B4+uDZH4LpIDs/tnM1XIJQBQzB/VtQgbH/u87xSQRgHWhaABUUQf0AZ1w6IByCYlAPC3HPg1EGYXyYwTDYQ3ASZUjE9SkHDUkn8BHPJVE3JOGAxAlA7y0+v8x1P5kFC+AwwBgE9XyMRAkCZxAKdRjfwSnH8WGapmAq9EE5+LY0A0D51PZNu9mUX5vY2SpPpX97cUkczJTwdsO+fbglYzrUWXaV2GUaMmTblMm62870lQ7WmKJFJMt3JcdRVkrRMcpNMadjzBknYc8fyxVm4kQGaVtoNCi5wEs12yl51TfqHcZv7jRqo3fml/cUPpsrTSjvHnKfyAsq6AIaNSuulZpTZTf+lcQd40hN5zwntmZUUXcVdejlkt4GiF4N+5q/XCizVHha3l9SJF0qw/m+9emsHnJLqCdv9AM0wW6IbIr8TSg6ZW25O4/ErHrDV4f9fpVHPmTTsDumNiGVhFLcETI8GB3hLW1ExQaCGM7Y/tzfheRmVJqY2+54cxBTbilzuptVnQ/irqJ20WWZyra0NRxTWWO75Oh4WENZe8zT85u4pgWeaPaKfN6gQW8giE3npFU2ZlzZg+sdpZWv32XBATN6zXAMkbN2iNDUp8qq1VGvcaTuyINWqp4Tk/qyRio/uezOV5tl9uOZoo1NiJ+vhpBuU32Spnx/K5BqHZ0FDpBY+Q3jTRYEeTEsTIN+vqzZahMhy/P2dEdPvUDvVXIyq67fZ4ST0A2xR/3mZPd26IbXuDOV2sxqrjAVD1vTrXbmlWiH3k9BZ4eWY8K4YZqMgxjp5YyiOH9GG5iOd6MU40Xa5rrYb/B7hoXSUamJgAhUj0aDpiiO+5w/6rlH932whLetXxMc6p5T2LcUCk92yDAIuKXALZ7cNzFZ0sUR3ak0Ik6d0soSd5+Ga1oa7apKieUlrenEK/SKQgQ1l/MDfcMpdaUvL3t0jG2DbjwjESSBkgXRqRhDyJbF4WxiKqrUrk4zWduO7X2YKBURHTHZcia8PvQ8Ou2SfV8oFXTdXOafJdlW6IXo72tE7WTgVfoyLtPVkl+n0pjuYUEjh+VKqEOjocgwLN0VbA1a73tSxOmUi1zJi1E3F+sMy/xtC4mVmdxMxainsy/cOt4b7VvtZlHOu2yK5216GsxxM5bCaThBGU4IUrFfJ6TM8riYqfno28RacAZ8H23Utb/LKi7VvV3QbltN0mUd1ZqV4CEX86DW17xCLml8UyQpBRmySTfk0t+Tl1UPwVJWbDZ4geirDZ1F+iGV4ZMLtzrDXVvIYOk7afVcQyhjggMgcLq1KrUkdF4OEE/U6onL1gbZrtg9OSKh40yQyO5tMTLWSifWjpqc8DFzKxwWhWvvszIyWjx2oCXBEMMawEFHtlsH0Te3nXOVxuRCbbJkxRKrrSYeiGBjJMxSGuWcjvdbjIEYKUvIa03TYpVfZUZnLraK5INRDyD4bA1PLhInxcR2EPPdgc0MZxDR6IiTfHAyC2up9Q2vR3t2Ot7RmGDEs7Dl7rnYX3p92i4V/VCzBpXF4j1cdmTWH3XOkqHUu7FVp5nrAEEdAjtUnofCBIudu0hs+zVbhNXZh657ybkYWz5HOV/KnKm9u5au8eT62pmTg6qBbpz2JYXJcnwSXbJIoepK8dWqu9M39aLCh45QfDxEiE2WSbC0TS8IayoD658hvOdCbesrXOcwxMAyNccz6JI+2ivI29BBnscZldE1t9shLbJhifGQbvl9T+hiSHDp1ltvCE+7XVnEEERuG1oM4rLlHlcNJD9j2KHd5AoJ33OlqIKDRBsWjZ9IUGQpUzGFriXwiMTLimXttYSs2mLi4UrcsFtrvfbUtbTacNnAO1EsYr47dLVNafGmXDmxvIMqx66PKw05mHm5lq0LTuQKy1tibhDlKZpEubMCaeV50Ho3xtWpb4m1FruBprtFQOB+ZVu7CtMsKwwPa5oJsBzSku2queiWqg4oA2e5aDvLE3l2KD7DeSGHSeFqS0uoZC0dO3hhP0aaMAEzlHPZ6Dk5Rhh6Oay1Eprk6kifhimuPT/oQ9FvdZbLbd7fXdD0nq98hxfSHWFur8ZRPF4hOnVoQfNOB3brr+p7TnIDus3gWzw52c5haM3UeWULI+WpiHZChRvcuj9t6a3i7JyDZHLsBtv5omGguIzVRr2JvOsa+EmH0ANeVH1FJLt0RZeojxHBmuurbbIdi+hwI7mbnLg25ZjGxenFxrpYmHjvMtzbHQ5uyXKcsplyGTU1eCf0t7igy/sltWDDFg+XDWXmWN0gKBNF18GNLgBv9eacx8xo5JvM6/bNpcwCCgugFTr2uLY5FauOPlMXbowuwY3bNId8jwmnkSZ7yN/x0wHbMJEa6aydXXb7Q2fUYgTtVkd3BzZWF9CsSJ4kC0sUB5XqFt1YsMauPJRU/Gkzg+TtcjeX7ujBmH06xuE+F6ft/gSt1LzJtu5mXSph2wctzqOXxoXpldxxW6fKWL1C3KrydqktL0VXvKf76LQ2bumlGuTd8lzXbKcKm5OIxduuPRprCHfupjYe72NPGJbDDzvqcN/f2uhOkmg2ru1CRhpc7ZbOtFSvQrXLa0dLWwxqapPTHO/eOqm+gt3Od6SD5Q28x1yV26lO3XaHVfAxY0Q8h6+7VgkiEbbYHstP4wk+OF2jrBArKxS+Q9fBMef7PLltt3ysZfGtOun3eLM1UP04+DcG8aDMN+yqXCEZuWQi371LS7276Gl2bIMSZ5eeVJzTIwl6Al/HTM08OjAdBAk1EBBNGx4nZMVUxfbRJ1mTSeE0uqqFcKHgvkPghDTDc13RKoUGlk5fjTp0UMwZJOtSxjc+LQV86MkWpFy0F/RVC8sHl8rrdS+0FySmW/N2tVgjTE5nGSL76SRW+K2hpZRNSUGpkAnxN9SK0Aqd7+wRlOw06e7sVpiQqdrUJgUriaU4FH5ahefiVluO7JiHo76K9htjuObMdr/eOZzjpVWhWBuH2ELtcXeW64qT5L2M6IY18sXESlExrbJSMjZVCGdYwhdnizBMmCY5KmCX8hV4IlT3kk3W51TpLIuxlZPgO3ZTJgdRtOtzqTZ7E2/sMTle5cS8efLmOK3OppILRwG+Shuy9zMl1ffl8khcN00ZNxsYW4mihAtcSsYjTHa7ECYs58zuqQvs1xddDspmBxeyENRaO8YDczFVpoBJHqrOm+IYEWuiJGjunJNIyhGpwqQ6ejrdmDjQTow4XuATBnqaaC95UNJcFBX0hLHW39RlfoQpc3DdUOawm70axG6N7W/CJnVykdeGgLdW0ajdgtY/HQT22lxEHRFcTYyVjoYuLc6SqzrFBgZVM5kotNQlxTOMHIzJ805OWnrltg0ERD5OV1ZemZ3KQyxiFhq6Iq28VLmN3Av1dUI7cdSq0/aar4MMOahe3VWTcwtxmgq2HheLNnbRqcgUa7/ZHDeBdNfvmBLaql7ZI4Vr+xultqhxFHh9RzFjB+20ZNVnS1GJD510jDFV8yd446mFWGZsqXEFXpn61RSVaZWudxcPpVrzsLfvdBUfinq5sui1m2PdRUS2CDU4zom91u4uWBKltUXdK3NBszPUl1esFg/I6bi0RfF8L3Jor66Z0BJjszhut1DUK8qIT3sZ0j18I+wlQahguvGtfMfuecsOQSaIq1pnDwK6FsZ6dzdtIYmvN6+WdjnpGhTqHZ1eriPW1Bhmd+eYG6lWKtxGXHbBT9uadylbHdajc9Ej+SYKF3y91lag7FegDrAF6C84yomvtnjjseBmwsS1iBQCB53dGUFW4Xa3qbmNEGBbFBM8yvJ4TofxjZoITEe19j7vzYCDIBNbCrgCWFO74aAYHawKaN8x+6Kn1dW1kRjCp3iqXyU9JmcHcbq36RE7W6fjSedrxsMPWpof4krquIsPe0Z4KUZV2ojBvvdEnHRWJHWvC//a3IZIU7XMaQkt3PE6R0HYKKMxa+FdxLfT1b3bRzYkmylltQupkuvwBIGNrwKdEcXiDqfrsrvbHqqmaLTBGMbM+4aOHW6EfNTsCHQ0swjKpdtSUEt5sNERs3BCKgh5CaqtAh3lza5RDOh+X/LGBHWD7zEwRdJaA2UBlCurg61fN4FFcunkMeKtPKCDq7Z6f3TlMJOHjD+t/YISEtyJ2BNOee02BYWBm0CUubejf4OMA9nH+IXIvb463w+at/a2Penv1HT09v4glHLRqjGV3wKaICah9Ld7w+emZEoHcmNjSCyGa56l9mZHstI0wOd1ePE1SzS0ABPlUQ5ld2h3kN3r/TQppVbRDFs4zOlg+bcWFxVZs1McFmCEoksdOXQ1JqnwMMEu7S6xNI2le9KTTYqyl4TbUqh6xWCwkfKvBHSHJ/7sdoGKsq0dGZaZ2ncLYSh5WqJp0FxXmo8HziHw/PseC1X8bFArJeYFaJe7B5u2wB3a2qPd0+IWY9ujV/FGq6V+G95McnWK8T3r7eBlcOsn0dpa590UBBjMk3sFn5JkH3KVe2c7gKkMufI0mcpA8cdrKqXYQxHZOyQVcI1cckkx3I8HKR1Jx79JcnswWV93vLwfRgglbEFY4UbFZaPuq5i62rSSmkxiackINfmnWiTWRi8XZ/hYiD7CoduwaMqigwKSk/1YIXrUY0x5f7dHK8GIY1czJ2YAeKGLtF9c+ZBRbyi7PMMOobiFa6XhAKrwuiDFchzNZW9DN9zeTTGL0VSrZe2ZdwrM7ogAbW/uHbMwbcX2VjJSu7hJmVYYbIIwobOqKFiHObgpH+8IVZetJGDtSiqpgFvv2XElNNCV4gY96NP2tinX0z4ktCnclcJ5Sx+k6lD2k0umV6YPVx7aI2OExawjBUMlrcfBsqhmmRaUK0MJuaUQ/Hxm0PEoQRSx7HYxEYtM2IjDOZhMpCcwWx0VLrUGkWqKFmJOmIhZNjNcqUPJQAm0TDX+QIDtZsdcEWYPy7f8kEkWvysj4ZBrrh9e0qXUuqtaqcDG0On7Y89wDY5RLLOGYXbcnWLmHN5xnEK5RMA7TBq9vtvQO4cizKK/O0q3Q6F2CfZZHCecOxpngxi70CyLiNpYJMccNi4QcXP44HpsYIVYyycUo1C4uByOKWQlkRBz9r2PGbmotYM9QlIaQbJzHVgosIMLi65XZhQfBKbkPCy6l0m9PFmM7EQXmKhX+/3AxW2M7IN8rRfOPceFoseNVCbVodea/Xo54MiWXuWeQ/MMaZWQxrmgx1CFZTt2VBpG+QW6Ixdo7PijtB/krOPy1IzRkiyXYEN8WkI74S4PRQAiu5Bwgl5N0fU2dmrRrZKLmNU3lvOH2uEPNyEmtDwrkgLVGUuSsWXV2/g6KcCu6Mxv/fBGrpeCshfbgMtYlv3555cPL/OR9PNg+e+9Qp6P+f6fnTa+HQy+v2p6HCoHjv/pwevT35Trnx9eGi8BUr2drbZ5Hz0PIf/LyerHf+stxUxiens/O78bu3Xvx/GdE81/avQC7Nu3XTN9acu8fxzwfnhx+3b+m4f2y/Mg++Wh3rWaT8W/Uwfcx0kTfOnKL03QgauX+Y8S5jc+gZ843ftt9Dxx/vDiT8Bbidd+wUjiS9BUs7rPFx+zI17hV+Tl9/8NLbMuxNclAAA= -->
