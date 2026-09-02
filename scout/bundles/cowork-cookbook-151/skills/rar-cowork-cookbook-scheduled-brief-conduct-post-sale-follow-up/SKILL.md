---
name: "rar-cowork-cookbook-scheduled-brief-conduct-post-sale-follow-up"
description: "Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up", "rar_sha256": "7466e508077be2e328998c793196fff8c6516b0ad30a190f57ae490bd0c32297", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_conduct_post_sale_follow_up_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-conduct-post-sale-follow-up:9ea37c0efd260b94ea587ccc6645fa4b0febec36278a30f277ef412fc55ef67f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_conduct_post_sale_follow_up_agent.py` is
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

Conduct post-sale follow-up Scheduled Email Brief — Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_post_sale_follow_up_agent.py` and embedded as the fenced Python below (sha256 7466e508077be2e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_post_sale_follow_up_agent.py` first:

```bash
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_post_sale_follow_up_agent.py   # or on stdin
python3 scheduled_brief_conduct_post_sale_follow_up_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct post-sale follow-up Scheduled Email Brief — Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_post_sale_follow_up',
    "version": '2.0.0',
    "display_name": 'Conduct post-sale follow-up Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct post-sale follow-up for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-post-sale-follow-up',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-post-sale-follow-up',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '022a9b25a213c7c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-conduct-post-sale-follow-up', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConductPostSaleFollowUp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductPostSaleFollowUp'
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
    print(ScheduledBriefConductPostSaleFollowUp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZejVrbmX6HjPti+ikyBEFPWqrUaTUiISUyScNYKMxwGMU8C5PZ/74OkiExfl+u2q/uhlSsjEJyz5/3tvTnx64vdNmFevXx50YCdIZydJFEIKsTOPGSZd3kVw1957MD/iJtnTRU5bZNX9cvriwdqt4qKJsqzcbsbAq9NbCcBSJpXWZQFn5wqAj4CUjtKkLpNU7uKbvD+SMhr3QYp8rr5VNtwh58nSd59agt4VSFNCJAK1EWe1dFIL+8yUP0NgQyjIAMe0uRI1WaIB+kOCFzfARAnw2coE+jttEhA/fLl53+8vkTw+uXLry9uYtf1NxmBtxgFWz6kUKAQGpRhcxfBKCCVxM4CuLwYoGky+L0AFRQrhbc8qM/z2481SPxX5D//M+7sKqh/+vI1Q56fry/jPxWKOGrS5HbdQKldu7CdKIma4TPCJp091FDJpq2yGrGRGlo2Cz4/dn6jlBfI38dnPz6YfA5A8+PXlxyKYI92//ry06j/1xdoDnj9eaRS/PjTZ6gIqH786RudunUuAFocEoNSf357fn+ShQu/LY38O9e/Q6oPDzvg68t3yo2fh9yjnnDny+dLHmU/PggXVX4FmZ254Mef/ows9IIbJ1Hd/B/R/flBOAS2B3V6Cv7T693I/0AmT4U+aP452wK69a9oApe/s3tFnob6M9p3+/8X0kmUgfrD4v+U3D/bMPk78vOf6vavNrwi/teXFUiiK4wOmDZfkF/fNGW9/PkH79vNH/7xGyT935LR8rZy7xTeUjuLfFA3b28//1Dfb//wj59/aAsYa8BO39oq+Wc0/5ld73x+Z8Hnqh9/vxfyN7I4g1mPfEQ68mte/I/qt8+IaSeR9+1+/QX5Pl/GzwQZlXhn+jDBdzlTQ1m/s+NPL79BoMigNhALxscwy//jPxAxcqu8zv0G0dy8bUa8aaIUjMLrYVQj+jOpf9H2O0H4nHq/IPDumO4QIuw2aRCuGmEP5sPo8VGD3Ed++Z/uHVM/uU9MndbvkPR2B8u3JzS+jdD4NkLj2wMa39ril8+IHkIJ8ioKosxOEJVVFMQOQNaMvO9RAlH203VkD0WLHvCjLncj9NSQyd+QX/4Cv7c76c/FMKr2NYO+sqM7+oK0yCuI5RB87RG7nKEBnyDyQnyp4GbHdmNk/NEWn0d7HUOQPa3owhIDeuC2DUCS3IU6+BFE69cR7fPkCrFytG0dR0mCeFEFDZdXw70WQft/GYn98ssvjl2HX7MHOOPIowbVU7jgQ2Dk06eiAn4SBWHzNQNumCM//PrbD8j/Qv7VrjvxkYcCq8WzBkEJeU2WEJitbQqX1cgYKhCK7t789beHT0bpYIVCYI5FfgTumyG1b6ExavBw1LuXoM6jiKB6cvq93ZAuhHZBogZaC+Z9/fo1G0nkcGnVRTV4N+Jj88P0725/8Bl9Uj9tCP3kV3l6X3uPytGZbl55n5Gdj3xYCqoL/dqMHg1hNMBALkDmgcwd4E67+ebCLG+QGuZS7Q+vSFtDVUfKvziQ9GicFAKW3fyCiEsF1r48eS/X4yK4O8+i0fHPuH3chkSqH2CMLd5JfEYkAK2JFHZlF2Fl1+C+zrcfEQFr3vt+SNxGMtAhY7EHo4/uWX6PvOW/6DM+egFkfe9P7i0B8rWdodgc+f+gmRnlZzlOXXOsvl4ha0lXz49gG9uwUfdH5wbbiSebEQM+Wox3NHrH6a9ZEkEHVcPfHiv9e3w91jywr62gMCqr3umPmV7d6UYNjJLR7VU1Rrb9NXsvCK/Q8NBH9YhtMJnjhy7vDMen75KGMGPH79+aA+QRgGNiwNBGitZJIhfxAfDuWdCE1ZhjT2/AkAFjvsGkcMPfaYVA6jAcIH0EChHB2IXWvZtOgrkyeuce+B/Lo7HlglJAh0FpYTKBz8hxjG3ogRpxAHTbuAZa4Yc7KSQF0MZQxA8L16FdPIQZW+OngPboizy1G/C9B54PYZyOlQfy+0hCSNX27AbasoNOgDnWPzz7IefTV1DYdEyI+6bfu/upK/J95frbmIhQxm8lAXbz9xj+ZhyI3lVa3wEJluO4hqmego84fdT3z48S/egBPmT58od54Me/NjLci67xe899QcKmKeov0+mjML7Xxc9unk5hjEQFqL/VyEcOfnpm3KePjPv0kXG/Y/Gw2Bfkr4n5OxLP+P6CYJ/Rz+j4SIhcMAbw8wOtsvy0OH+aj0+/Zir45u5nTIxoBzPbGT6KzvsSWHmCCgTj4kcRqsfa1cFyece+exH5CIlnwkBozYKxYtb5d4k86jQ6+OG/D4yGj7IR/b2x+wvAOCAlo/g1ePmStUny+pLZKfgLg9EIxzB4oVHGsQomEmyqmgjcv300WOOX38+G9xSD2ODlX8ZMg6UPNsOvyEdf+4q8Txr3GS5r4aj189hTjyzhUvjrY+3H4OmAFzjiNUMxKvAYn8ZW7tli/1GIMcGgxC4Yi3v+kbEjxz8QgRdBAKo/EpHvF3byhI26sceCCev0M9nfQ/UVgS6ESQjzCsJlCzf8kQ3kU4GyhSXaG9X9Zr9vauUPXX67m6F5zKC/vrzDx3j96Bce4TPS/jfau9G672X5beRh3ymNTdjd2Pd29g0qGo3l97tHwdhLvD0C8+ULhCHw+jKatIpgj367D+EvD8GgRt8aYUgBAsqnemwnpjCvICVY5ItRmxiC4XcMxtuRd18/Xnz58+75v0eGLwywccpFge/NSNRh5sAmaMp1XZKcE749d1AfOMDFyRlF2zjqzygK+HNs5rsEAXyS8qE8I7vUfsozxUa/QE0+jP9/09y/PEjB8jIjSEiLmpMkIFAapSgHzAA+oxmGdikGxxjS933aJQmMdFDbw1EbY1CfoGwwZ1DHQ118NmOokd6zp3zI9/bev7976oEVUKY0jUbpZ7btQg7Y3GMom3QBjjq4C7AZ5lE4QAkG92kazOH+j61Pb43OfJhgDGnYTsJm7jry+fXp/TFMyTlcuZ3XO/bxWU4Z03aOU0cNhUmVTPoeJw+4URhxQl1VJ3bJKpSFeKkvYoJUwXpP8byrmY1+2lnCLFlL7BRVp+cTw/u+SCn8JpF3saL23crq10RNybeaqkRU3Bx0lpROic0TRn7Zz1IztfbCenaESVSczuFpMMvEsy3NdWxVDmVFI2fHeeX5foodLfZGXrTkltmTVLTpsqh0zIokYarLIJpo8pqw041k2pEpWF2rHtc3Bq69DrkRmZhduxbmccnWaI3ryls2C3+PHy3HVVRS1gt0Kt+KAVxv1FyzBgZkOO1HjReEQCwT01tizclOhMqexDK6Oce1te9uIHd8UhrIenMsCM42SCcyYOyGO6wvB3nDH9hVQfZ7LeMnroi3xU7jbphp5FliBidZGMz6oqqtRZbHDlubvFt6fBnPryLP++22xvpGqnatZc10hz4VTqK1bqejsRUNib5TFngIVCyTw41QePyZL8BhqfZaE/OtW4bV3qZOcpJd8TVgXSpO8GC3JMVSM0tu2HQOHqCzY+ElaC+ERXliJzf2ACO4MHI/bAXtqrX9sQ8qbrdoXF8c5N7wFo2c5qbNgMHl92e64DcxqU5rgjPJtPXM5LwfauWGscnCyGVP54xEZfwDKMiyoUmtOt2AvGC1W2FQ9WSASUIfWmJG5FuHckVtGFSzSO2ZL5/9RlruSvM4r/dqkRG8d6xEjGsMotBNNF0muT4PzanDHq0IU1bmDcWIi8Cd8C2q1YmriIbKXYvLJRY1MYuKMxkljegHEzCDHbUVnczjJnOZdHlkxKkw70SrtpT17jTURL0m1u2sPE+a0mqcNe7M5NKf8wds09OZxU9WzORItIspWE6YkDi23l7hzWnn2rKFTqYZRVrDIN8SM7NkmksrbbrxN8fZXjfUo5mtjDg2yUarzsH8nFytWrosC4cTD3R8yJmz6nNsbBPpNeFx9lBh8wK0h5OFW2d5TkvEsTuKebXlsbLeXBdwEBnwKNqncSTtrpsdvrvl64ArvEFetYdwf1RVfZMCjutcvSEo4eIK5WTdZHmaXHJ63q69OqEzmx+Wc3WmmYOXZ+W57QlwRrW2AzE6sYgynanDETcy5aQunSIp+KGcatvpYkip2B2IXXfFjANlUftpPKQC3qsXPs+tyllKFRyuWrkgd67ZOwTnVbuZhi6UqS7iN3ezMBkuuewFplh2ZmlGHmUUiYAaMjA4TCst36eWV6pcoSle7xjZUXTiRJE7c5OKG4ycLZRDZcyowqtQpgL91Y7TQtyX6DlAg/biYZfIlQ52BrBFtb+Y6kS1PLeRz/Vmy1+ycnVAFSXQpoJ61IZGT27BgqfQ9ZQbKu0YTqT1KY0uZsRnpdodhKB0ay2O8GOnMmCFx/O1mIPj2aHX+5pSda7Omy5bLb1DmfG8eVnNd0R2kuu6MAYnyQor1ElaXu3CK1vjRNc0jKwQJMUf4xkloYZLeufKXjpZryToSdTr1tstB+EiRtelEjIXF5vkSW2WTI6jXjw/SzSeTWmKvuALdFryVkZdNX2lLpLElWsUa/WWnVzXh2GK7fw2LqW6kxcJim9W2WbFBMCd4/ZmLfuyg5qr2+TUsofLVVkXcs/fiAmzCpOz5B491l0ZhJTMViG9nq52u0W89NxcYSdqxhfGWritraNwuQZxq0W0dOXEI+YQ0nVJzRZCcGtZByuOWJ9X0nnp7h3bYHl8Ehq1kyT8+SR7RZH2u86bupvT2WUmw5wtRNK6NhYhHE191t7QHqdurSD2K5kkJ7fKIr1MwEhvbVwDYSZiVFUxvjnw6nDy06avmUvg0ssJyeyHcIVPBo0rccVV2iK4DfG2VrZ1NO27ySRmpy2syrTkp47Xa9P9MdBFwNBHaiPsOGlx6XU7lm3+th+ifp+eNAI3OFUA/moqWKGA1Rk3X24EqT+07Gnf12ReilyxjZXTeXNIdvrRatWCvuwMutoJlaQvzuH+PORUkVcqoRSFZZ9bbGBIb6OeV4Ui5awnudvzvsJlRVaomtqTh5OwSAbrGBURKTJTZdvu5bIJzK2OgessYVtLOM20TlGVqOCDvbzh2llyu+xJkkbnAThBKBsSNR/C0grNbhctyTXjhUZBb80r2pyIXiRssWnipbiercliH3kb051PgpnXXwsvEtrzfsOjF9+a4EHdcaf6Klo8Z8ZzbTaz2kIXymzb6lR0ZYWhDLjdjElWgrlOWZVbHGhDOxkbennBD1JXNHZiNvtdL8Y5eZ71FwNdNZFlkGVnt2TJb8l272DxkHhncxVK88OGY8KC5SeLZLfRe53ThlshY8Tcm4vL0A3dOXsyGdOzSyldHc82a9PhcDD17W1F9FeDpE48yUb8XjwvslC8sLGgnVzR3ncJUezCJAI2txVXfqotPPaaNc1mLdXG9XhNB3ySCiJjdnppJkf2WlytkxGtg5LcnjHuvKqyq9WXil1dd+oRCmoU+yl33hb4ISY2ZEpG0bqmJaALNrZ0uaUPakHiZuLSyyKOWl1F7LjXFvWGS4JyGZB1VDhdvGBhzM/ansEbRdtq633EymQ2hc3TjBK6kmskdVAyWFoWUS7wLUnM0H1HJl5J7lc7e2ktN9fr9TQc6+kRLMSYsRO2qleCY24xfClnlkWibWvPh9nMz5ICbXEU1Nbxwvdi4fnNKamlyQ7npEDSAMNJO1ZL7HPAWrkCMqpBS0K/dP75UBop7N2Mfrs+Xk8F6Rl1jSaRoemE3KeZ7Z+Lk5qv29jqQsHeS9rCxE4FlN6biFa40RXArBt00S+ExOT8E5Uc8llFqUq80wKRqtqj2efsJQpDbz3z1ICb8u1ct6oQLbaLAeVAqhfZYnnkA2Ngz7YargZze+OnxlEESZSS5xUvSANHR0Driulc1VfEUo8a5yDGwXZZglTbo7s6MWXjttvCJp6Od7bHr5dz7HBytLXCnhJ9Yhoqs08GucnUlZOJMPaHy2W/3l0iSUkvyYpe5iFzKIBXRxWjeJzPnouaBNSy39imSQ98ella8hnfmQnVAIlORPI0PVwMaUnEClpl8X6qHOtFZvQRemAI0FfkckgWzUmfQQSc66Qq+RdHbucGOj1P2MgnOGZjSUwXD/lNwc0lHc2rIJ3KaxzD0i7E1DO5YrebIcRguq1CSzO3YuIY653u0Xrgt+vyUtIoSa2itCGuM+6SEmyUnVCCWqCYpbhbA3gCi9LaHrrUnuf7xRIvs1O3dHg8jjYJe5tqXssee6EeFq6nLG8bVdmqy9jQlsq6LW7RDL+Km6pgZ9IBmztRIdGwoR3Qab4/xge3z5fEvE2Pt3LbLbVE5+OUKXVpaZxuMxdPi8XeJLYE0TgK76pwInP2gib3inji0vmKNVaJPTkTHYut+YHdNy5d0ZuLshSdSbYil00AE29CbGhPokXKO6qwmU3YiyAMx6N63Ju3gbJ1nwSlD/KQm0VLQavZayet0DObzbXUis2L7xq6GXuizE6SbJ6cb1rQnWIH17v2Zp/2KamvF7W44TqFi6LBZY28ujUuJBOLpB7cJm6lOb5/0ZhD5xlnoWM3OSjM63G7wBmlpjhysT9YcUQUvRL3ysxYeOe1lVvJKc5ldmhqGBqiBk5EmJrWxp3O5mtVn1e0Lcewhu+qTjxkl8V+KpxJct82gtWz65UunW6a12xPBzO78nuUdhUt3e5oyl6FTnFKlWYD/B723MSWIitLutXmVc3sRvNEr3C3NOVMzsoi8vB1jwvx7bxoYK1BJQbnWpMN5fYm7m0PFIW0E9FqSQR0PFkcBmW2z1xejlKNKS4YbmMqIZ7cdbkJSTXVwzmz8yPBZxpDCTfSLvW2ZpYyE+di4APLLnp2vj+5yXk9cWUUdjMlaOFA0U8qzJzTi0XTeSgle93endrHAFUuXubALCMsFh/yidT1TOpRE5Qkp9tdPj35/hXdKPOFz50sezqp/XnpnmYNVW5zyT+Vsl5X6IGfhVTkDVurjXNa0HPrsPc2zM1Y7OEIHcMAhSUzkNqrtbF0kK/US3i7rWV1e94mIhHMlnNiVR/VzqNmN12jvNs19SJeIsmbhJe2suj4GWgSow+NrXsV8ESRRWrL86GzO3LHTmcOCUef9xgtrq9wbGzhkJjRXIfLp4Mj8/X0Em1ySpnNKArGUjFQNXqxDU1TDFW+FqtZ5m7blRoHtEmXy3kEpuquWTk21g9eNZXs6XHazMm5OuQ7Dkf9w2oTqUpxoaVLAEjYiTKMum4hTMPx3lDdiPXcozrzKvuIp32FqVs4ILF0f8WqVsy9yfSiw3juOz2e772WufXnSJyue313mAdn/Bwp6h5bKefLhuyn9klXXX4ReHnKTyYr15By7aqYKE3fAgkntiG3iX2wUS/UrjryEwoV5oNDszVWzBP8NDMm7qKrjmIW8qQo38BVXflgCoLOCzkhV0zWi272EseHzQ2oqwV7PKPTQTgz9Zxddu4g7Oy2g9ZmybJwYsmdt/E1KOCYHyo0aEisueHO6Rxt2nVKZ4UEolW2PwvbXJ6dKCc9Kyxh8DhXn9RpeOLzhvF6vCFbNbWYyXyFdfm8773V4UKnHVdvDxND0vUg7GSnc63ElUpm0npEXw3YceVSwXa1OEuNit0inMNLhtlTu+xYkq1HtptLLDG2dc5289YLB+ak3wIiRpfLmipm/QpdVQMl6gM7v2zpAVzokjMHf9WTOrmqy0luXX2nA1Lpuaw0DbgGpyirox2saTE6SgXfmbQTm2puJ39lsivltlK8qS8XBzrfuvhUJLkQm1E4JYSzQ47Vamuzyk7gdD8D9aW5lZQXTKfDpKfCGI4Q4uJ6LQAzWy7iCxVFWbe4dtjmYupuRUs3VAaNOenTS5iGV2zjLBjehzMyi7IxcTMw2lQUBq0i+XJKg2yXH7eZdjrDwcau+hMv3M7Swr6K9qZ0zn23ZlYy3rGLUlyF+zUpxztx6nYNC60Mdes4U3emV1WjXca+lv0R8tDmSu7XIZOtSu6q97TPL7xjr4B+QnduvLDnbBXODd45s3NfTVYJOzFTYyWzYucRcb5TEoBxxcElrqqMbYWbsFXDjDvdzJteUr1E+8FyTwgyFc8FYiap05QPQTunzUmaXN3K2KY4I5v8LbD52qfF0q/RrKzb1XaToTlbZlNB3/uee6t9gu8nMuwG8qUob4rZZCeqO/QWrdeXhlkcslkeX0tlB0uxHzhc7PpStSZWRds5OUMRrFAD5eDj2RmmxLlgWfbvL68v9/Phly8YSs3I15fxEOF5FPBvvkEOblHx9iSKU3Pm9eX/3avMx2vF96PD+9EAsL0vd+5f/i15//H6UrkRlO3x+rlO2uD5IvO/vML99BfeMI+Ehsf593ju2TfvhyyNHdzfhUdwa91Uw1udJ+39TTj0Q1uPfxVTvz2PJl7uqqZF83zd/J1qj0d1AaB2Tf5WtnkDXsa/XRmP9IAX2R9fg+dBwuuLN0C3Rm79hpPEG6iKUfPnmdb4ync81Hr57X8DRk1j3gUoAAA= -->
