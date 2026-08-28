---
name: "rar-cowork-cookbook-teams-update-update-access-to-systems"
description: "Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_access_to_systems", "rar_sha256": "be30aacb6b768b73d6108a23d64b083b63451cec612eb10a6727cc1435b8415c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_access_to_systems_agent.py` and in the RCI capsule.

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

Update access to systems Teams Channel Update — Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 be30aacb6b768b73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_access_to_systems_agent.py` first:

```bash
python3 teams_update_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_access_to_systems_agent.py   # or on stdin
python3 teams_update_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Teams Channel Update — Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_access_to_systems',
    "version": '2.0.1',
    "display_name": 'Update access to systems Teams Channel Update',
    "description": 'Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f50f30462424a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateUpdateAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateAccessToSystems'
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
    print(TeamsUpdateUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZObyLbnV2Hq/WH3k12AAAG+cSNGIIQ2hISQQLQ73CzJvu+op7/7JJKq7H59+83tiYmhymbLPPv5nZNJ/fZiNrWflS9fXk7ATBHRjOPAByVipg7CZ11WRvCURRb8h9hZWpeB1dRZWb18enFAZZdBXgdZCqcvStOtK8REVGAmFWL7ZpqCGMmzqkayFGlyx6wBYto2qCqkzpBqqGoAB1a1WTcV0gW1D5kiQVqD0rTroAXI3DHz+wVvlg7iZiVSNIEdIVAI0wOvUATQm0keg+rly8+/fHoJ4PXLl99e7Nis4KOXuyTnO+PH//M7dzU7PXhDArGZenBkPkAjpPA+ByXkk8BHDnCR593HCsTuJ+Q//zPqzNKrfvryNUWex9eX8UdpUqT2AVTLhIQdxDZz0wrioB5ekXncmUOFlKBuynS0TwXFT73Xx8zvlLIc+ef47uODyasH6o9fXzIogjla+OvLTwg0wNeXshmvX0cq+cefXuOsA+XHn77TqRorBHY9EoNSv3573j/JwoHfhwbunes/IdWHLy3w9eUH5cbjIfeoJ5z58hpmQfrxQTgvsxakZmqDjz/9FVnbB3YUB1X9b9H9+UHYB6YDdXoK/tOnu5F/QSZPhd5p/jXbHLr172gCh7+x+4Q8DfVXtO/2/y+k4yAF1bvF/yW5fzVh8k/k57/U7b+b8Alxv74sQAxzozStGHxBfvt2Ogj8zx+c7w8//PI7JP1/JHPKmtK+U/iWmGnggqr+9u3nD9X98Ydffv7Q5DDWYCZ9a8r4X9H8V3a98/mDBZ+jPv5xLuR/TqM061LkPdKR37L8f5S/vyIXMw6c78+rL8iP+TIeE2RU4o3pwwQ/5EwFZf3Bjj+9/A4xIoXaNPb9Nczy//gPRArsMqsyt0ZOdtbUCHRwHSRgFF71gwqBv2NulwDatQqgYZ/jYPyPHh4lzlzk1/9p39Hys/1ES7Qe0efbA/feTg/4+1Zn357w9+srokLiWRl4QWrGiDI/HL6mEN3SemScl6ACZQshxRpq8BmC0efxAqIk8uu/Rf/bndRrPvx6R/TggVMKvx4xqmpi8DrqqfkgfWplQwwGPbAbyCXObCiSG0CA/QT1r7IYYnE92qSKgjhGnKCEBsjK4U4b2u3LSOzXX3+1zMr/mj5AlUAeVaJC4YB3cZDPn6Fubhx4fv01BbafIR9++/0D8r+Q/27WnfjI42BWb16BEm5O8h6BWdYkcBh0GHQxhJC7V377/WlhSCaFZQ36MHAD8JgMozQCzpu5T6v55yk1QywAzQxNnORZWUOkRoL6FVm7yLu8kOn4asRyf6xuDshB6oDUHiBVE6rzbsk0q5EKhmLlDp+QpgJ3rr9apXkXMYHpbta/IhJ/gJUji8eqWD4rCZycpQE0/3swPJ5DIuWHCuHeSLwi+zEukdwszdwvzScP13z4BVaMt+mQuImkoPuajmUSjKa6J8nDPHAQtIz9dOnn0eew3CcQEZzqjfd9jDnWN/Ve58qvafVMALMcXWHDggCZek3gjGXhH8+QqvysiZ27/aCkI6WnF5ynV+4xeP6rBuHRT/DPfuI57GszxXAS+f/fdIyizkVREcS5KiwQYa8q14cJx+5oNPWjoYK1/z75ni7f+4E3NHkD1a9pHMB4KId/PEbeDf8c8wCqpoR2UubKnT70OjThSPcelGOQleUYzubX9A29P0Fz3KEKGgBmMIzwUfM3huPbN0l9mKbj/fdKfnciVBu6HQYekjdWDIPCBcCxzNEGfjkm1tP4MELBmGSdH9j+H7RCIHUYCJD+6IUAeggi/N10+wyqCXPKLbPk+/Bg7I+gFE5jQ2lh+wleEQ3mxhgfFUxI2OSMY6AVPtxJIQmANoYivlu48s38IczYsT4FNEdfZMkYAj944PnyezTfZRnFh1RNGDDQlt0IsQ7oH559l/PpKyhsMubffdIf3f3UFfmxzPzja3qX8R3VYVrHY4X+wTgIDEAYlyOOjqhUQWRJwDOAYCTci/Hro54+Cva7LF/+1KZ//Hud/L1Cnv/ouS+IX9d59QVFH1Xtrai9QkxAYYwEOageBe7zI8feTo9U+1xnn5+p9gfiD1t9Qf6egH8g8YzsLwj+ir1i46tdYIMxdJ8HtAf/mbt+Jse3X1MFfHf0MxpGWI0HWFHfa8zbEFhovBJ44+BHzanGUtXB6ngHWeiKr+l7MDxTZcQcbyyQVfZDCt+LLXTtw3PvtQC+SmvI2xmbtMcSJh7Fr8DLl7SJ408vqZmAf2/pMkI+jFhoj3HNA7MHtj11AO537y3QePPHddo9ryAgONmXMb0+IWO7+gl57zw/IW9rgfsCK23gYujnsesdWcKh8PQ+9n0RaIEXuP6qh3yU/bHAGZutZxP8ZyHGrIISv8HyW5qOHP9EBF54Hij/TES+X5jxEysgpo9FOajfMryCcjqwxfmEQO/BzIPJBDGygRP+zAbyKQEEegi2o7rf7fddreyhy+93M9SPVeJvL2+Y8fTBsyOEw2Fyfq7G+ofCSIUM4f0jpuC7/7te8UkEQh1sUyAVCxCYadrWzKJnjEUTzgzHGHMKz6SFMYQ1I0gKt4E9w6fAwjFzRk9p28ZJgrIYEqdsSO8Rnt/GSh+MggHMBQSLT22HmE0pimRxemqyjknSpulgDENjtOvAavB9agRx8qntQ7vRlO9t62iVp9K/vVgzEo5ckdV6/jh4lL2Y6JS2FH830bFJ36Ok31B6thewXbpaU/hKs/X1PFloNyKo1hec06gIRn0zH/R6K90Wh6M/yRQ2auvEyUG03cfQcd5iF3l2YlW0fKvQto2T4hRsuZrRC3M4R0ISlJx2EXQj3NLalIw2G3TRG4Pa64m7UN0WxfeoyMTrdss3cbpZUeJV62KVp4tJp5qn2MSXKphpXmLwFK4XubLJzclFFqi4U1jZ2CRb/5QuGzxLL7N1UV+GAizmpNumA31QY8bWc5tYzahmV/W4b5cbZb0Q1Sg2OLxWt3EZmky9zHOTP+9kxzYO9r5dnizdN/Gtubit2d1wpoCZJ3R4TI65Km2XclHm50L16ENy6M8NKIydOAsqreSz3e4cVLZL81pzITONxL0gqS9aRiyMwaS6pLDlpF9l2OoQW8dyUmLZzdK3hkFmZ7MUSMkb1M4h9Yq5pddgeW5iG2uXerThB0yX1e1U0MjEjCNW18DxGMV9c1IdS2fWAzVo4rDvrHSgnOBs5LjcR+lO0afqpBJAQZ0Lbdd3WK5lRX/bTq6FdLMxjrHdKuD7S8nVcuJJJg4Ge1NcmSy/RFMFrQaIq7NeXmPVkpwsqVl+9MrTUl6HdETODe2GH3AiTQbMZmgOK5qrXqZxQhATfx/UuqTfxJm7iD2inxfVbU8fpDBZXfFmxwtHy/N5sfdpKlbOZYVfJ3rDUWfK3nBGdqTQoT9rx0D1Ope1T9filk6C6/7muxwbnDCMluzTBD+sSVMD3TDEh6sq0bTD7hWxLIKyomQvI6/aRu/t1EinQrDnl1VkXwzHvRqXA3kb9Euz2IQprjhTm5IEdNnP0nM84QMQSGiooEIYroZSwC7KrEXny8ANLYK0D8zKI4UBp9szl0lpI95WLr9pzk0RVmfDGyKmjgvjigHbAFUq9keVC8VNc+I7Y88fgvN62RvbsOGtW2GcIFyGt2LVOUvKCnJfMqCzFtky2JwEkRM9S+UtXxmcm3282WrjHbHjVDuJZJYl61Mcna+4lfI8kJWEZOJps8TASr+FaUhyRBoZ8U1xwwPQFC0xUmLYczvGukbHK+vfbHTB4Kq1zmVLc8I4Q3lCMLe252IiStTCIivIhJecQ0AXXZtvdwGu6d2M41SdaanYiNgLVjbL9UIGOOfe+HY+r7B8CkggzwrZV/GewBrspsu1TWrntJHm59XKI7rGuRa4QbhxH2LN7GhNhHXqtNbygqPyZRlJOT6juIOs5/XtyKh5KTa6ixtbz4qNvD8Zc7agy5WA8v5yx5lbbZCoi4sNSRq61ZYDt53QH0/Ap1jVWJL7jaNtBpJdhyguoOK0ULR+so/0CEJTpKSXG+ZtcsE34j3XNExIbVbldns1BcbeadFak6ZBzhhGu5qKAqOk1+jSz2sHGNEtaZxcUVamGekXMKjBQToMZRPZ1epILQKgUydcLC+h1VJSzlBHjYxwYoPpVSHpR6JO8OQiCj0zx+VZcN1MjBvI4tKtF9tdrXeZTaCBFxF0veKw4zUqG1WqNsls1p3Pq/QgS+mRp4nDZogLyegl1R/E6ZlT91d1LbEmez3N1hElqYw9PczzurMDO6GgQVCQBUa5PvPhVWet1aZiMME+grV09ubYxhlCTaWW03x5hX5U4qsspNyaj1rB9Hxx2qtNnnv01t+S3MLfrcnseNsfPWNmXQXZ6WPflrcDHyvcIjVNo1LnkXvzssMirIAubNYHzT1o14WBJQcDsxPNINEkMSIXuySHNsVxuy0TdKMIXiwZBbHSbsZEHVIvIajWLld2RK+jSm4VJeFQ9OotI6cnVlYlCYodqL0BDsuYYUC7u5ADOKRMgPpJGS2x837S7rZsr6245XzrFArmh9fWEK8Xz7yA3Uo5GR1PDafZYPjbeO+p9mKZ73uuOkJC1YyEGB0c9vJkvc23YmIesW1IrvgrtvF99GLr5zqEORxJ9TI4bC9yd/BzY6Au8aFJu1Sg5vtrqts+r8i7a1EckzCNMYvcyFObOWu7/VG8XlmOS6bnWb7vrukZL6qk6Gqj1PysJQ1U4DHvxmwBG+WpqBCkk4dzX7uy1CIL/XBhpDLekUV+EpJCF0X64qSg6b2JXmOHTbrJ2Xni7s/i/rTc8dttjzmzRCSIKyHMhzVWuF0zoXhpax4lXemoVgNy0XLVOqx8YoH6tCcKhbdZak7NhhchPh5Dbs+cd7qTFynPibrSdmVsxX7GxdzK2y71rbyec+uZcZt3s2JTUDoJMHkeDbFr4Kt0z58lbh9ZzGa69pml2J8aZVDzwyUmgVSdPJc7z+YYxpaT/CwSwrnYi4osMHONXa1rQpssLNxIrsM0kvzSkuexdGI8vB6muS7FiWvtjWuk+cGOS6mU1LwdS6vB1a+O8RafMCJR9axe1KaZG5f5bmoRCr7113rjVxLnz2HPdpbanOYcNNhicsvHG530fdLBKJkD+STL/G2LaXnCV0TGd9L6EOC7mveqQU0CXeVyhq8v/E201uplPu0m1eAbnXAI54W0ojvi2qCmkEs2Nu9nLup4wDq2YmWd56t5bzPxcZl14FLTbF6eDHxjXbCzqOoTaiu4aLpkSMAcxJV7aqAH6pnTsz6WeIlc2gqFg+ZAcVGDtuEuN9L+1i9ntmzgW4ttHCpOPHA2JW87Yc0TY3Jzgbis+U7P3ENr+Zehij2XDM+bZSBqfnQwGqdVsUl2UMqt0Bzb+dLJZkGsJ4o00xb4UqvWZnwqs2aRX+zdQPvCcuuYW+KWpPaQ6dti07T6Nu9RHeNwT1ys9V5n4mLR10tJ5rA+PRbeWqjcyuaXCZl5PXqTcD7aycJVLudVtMan1JrDTzcDPYPJKRqm09l84J34Us/RuD9OvDoVN5S8ran1gB+Ny2IID6mxWW2Nwc/X1GRHdM7pkiSSKvgnK1D9K7+eyXyx2BUyiDtjdwmFvLrpx3gvWcawuhg3xfcnvENOskqWp4Y6ScXQOArk1FkZPhWbF3y4bWbJuZGmtjIFQZmCYeVsr7NO1JaZgdrcBLMnUsHYWidWhBD2SyIm9o6qmWvZ1sSedTs9vijYQTCsDYWZgzIP242ELs8EHca1mrgJvblyhKaIvk2Ja/UUiUq3ZQ/desWDHRYWMZmtZkOkGbeyIOMN7OLs0Oh8jN+ntKo5Tp/LIJk6+pGXisFyO+Nw6Yk9oZvrEybr4lS9iJQyOXllVGoZ785VTA03873vxbsjUI8WWZ6JxWS/Par9WUpjIYmGbXOe1X3QdQ2jGOV5ygG8UkPZwdbxHptW2XIlGNHgb2l6gYWRdAg2oefr59ktC/XqQreUoZ/8hTRBlcrOD+15q+66nL8c8tCjoiw0eM8oVrd94S6uYt7L3eZYtnnLXW9duEJzDHiz7Rwt0KmUhtGuU2sWrAN/J/HzSWssrSWZ31rTKJZtPcvZabDaKcJJ23sx2MAieVyiBBUYmwsRbK18x+r2FZeIUzk5SUcut+v9akPNNOqcRvONfr0ufM+Wl25EHm+RFi5B1WVnaaqGN1nZnWauczuxSseejcV1vsoOl0ub6RwMDtwapvPt8ez3Rtcf2IqUD+Jmf97T2W1zWLZNvtcVyZRoT8gp5aRbeDRlGULWjhMilS6HFZ8umgDs55q2ZPBs8LZ23Pmr2znGuAvh5epxOIDiKt10M61LZ2snzqTtGUHaLjyXuIDSKtUMlM3ZJM1DTTozVmvdgiY2tL3P3UbXDDxuryJo2iupnGFxoJ0jcQqXkp9farHDZrJSVjdSpCJVvjSeRlkFN5uxRWsk6e1wXBfkSZoKZOoLOWejYjd3g+PCXe3IomRtl0MDnw5rs1su7Hk7kWWP0bwY4pZGXCNXSU1GAyGgp9N96HbmhbmxxrWRUelWFfQ+4Ep1wZDhzg0ISQdOOQeLsF+h6JTQUUHP+XZxgqt21ELJKQQPmtAP7ZZtsAVqqOlVzSyMJ4vlUs5CRl8du8gmd1ZyDnBi0W/Q4+nkKOGMtYeiiwxyd1xsbjeRncvrA68SSr301QNZLbwZETfJUrulhq2uvDqgbvtbmR2cgS8o7bRVbsWtOeP0EK62AswGZXky/BW7MHUy9tPBOE6anAD+BgvRVasT+lnxBe1AsPMZd2PapvFKakpZ9G499YX2holKCSPJIMSbd63qJYaFtq7q7VRdHCfT8mzTJnrTWpxAgSwLdsPvSuxw5ZL1Om07dtdmlcjQe5oNN9W2sUy0lhSrn1vXizG1QnOCxjOTUgjr5s0DtsUWiZzQMbsq3Z3BeknmzVHbrFK4dGE2AalHCk/InEAHF6oF/krtVGJHkBYQjrvpTVxSk4DUauaUt8uOZZpOxrJVf+Nt2eW9juw0LBjXdoyxmXCaUTEK27PR8hZiS7MX2Y1N+4pK0IVOY7PDKpTXtMPNsoXN4OearXSbiI6YQvm1xx+4ZULvmVWQerTqFkGH1lOBr7VaxVIGlZr1VHAUxqwJnFWm7srOc/iI0Q1ZDlLYMlqqqY57ofYgo6dU5TgwvcG1xzAz6Mwqr/sqqfG29GMiOGZwibOfWuSeOV7loTNmw2SOMmQFoloXjimt1Wxbadc9R5VWN3j6XrGcmp8OzJRXPcCW+qZM2usU1tPtAja5zdCIGdPUR5ERWVKh5lvYiO3o/ChOqGkvhfMAllR8It08xlxfwcrrmGgoZrler8oFNomJ44wI5kBw2hrwnetqlsVy1+Wmmt3oukk5B6zidhIufaKZNPSpBWe1tQ+hs7iwvaVPFn7CnovVxcFozG0pv6/x+tDAZS2bttiKmOnrCb2bdFRD0jrWHjGfYjy68xVhTpFmwZa05DJ1WOJKfa2uiwt+WxLd0l1ONmjfmFy22RxBWZIFcKEnhVosfSI5uEvg9E4gETiMChv2wji5OpPHs5LXYTxXMJl2vbmYDZpQnYzmtJIJeXUMo2EJ/HZtmAFBgCGmjdnSTYYGZMdY2hWunU9SNZmv/A4lgqQuusyNaM2WvbnWCBuy2c8vCTo1hIs784ioL0CqJCXWDcxuNqzOw+zCbtlS1FtNoT153WZAbxfT4wZl2UwlFxv2vN7Rp1qLQgxr9Kur6kZgHZKei+tJHxtsh83dFcpnqSNGwaUeTDJgYn5/Rg3TUtkycdgFn2odyXBTL1XYg6bHXJDJUeKveadNjoLLCr6jzixgun19k+RD6h/sPliFIjUFjTHMiEVn9cam0LbZ9jifv3x6GXemn/vLf+/j8bjd9/9s1/GxQfj2xem+uQxM58ud15e/Kdcvn15KO4BSPfZYq7jxnpuR/2WH9fO/9bFiJDE8vsyOn8j6+m1Xvja98W+MXoLUaaq6HL5VWdzcN3o/vVhNNf61Q/XtuaH9clcvycfd8R/VgbemkwRpMH46HbV5bDKPz+/fHxPgBN9vvef+86cXZ4A+C+zqGzGjvoEyH5V+fgWBuk5fsVf85ff/DQ0svTvIJQAA -->
