---
name: "rar-cowork-cookbook-bulk-update-process-allocations"
description: "Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_allocations", "rar_sha256": "4a3d5f7582e2438744bc64632f9b21985b91037ddf11dab9b8b566d9fb45df36", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Bulk Field Update — Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_allocations_agent.py` and embedded as the fenced Python below (sha256 4a3d5f7582e24387…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_allocations_agent.py` first:

```bash
python3 bulk_update_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_process_allocations_agent.py   # or on stdin
python3 bulk_update_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Bulk Field Update — Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_process_allocations',
    "version": '2.0.1',
    "display_name": 'Process allocations Bulk Field Update',
    "description": 'Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34f883f5cc672caf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateProcessAllocations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProcessAllocations'
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
    print(BulkUpdateProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRpruX2HOfLA9nDpiEQiqoyMuSAgQWhEgwOUos4PYd5Cv//tNJJ1T5bF7ujtiIq5qkRCZb77r87yZ6LcXq23CvHr5/HL2rAzirSSJQq+CrMyFlnmfVzF4y2Mb/IOcPGuqyG6bvKpfXl9cr3aqqGiiPAPTmaJIIq+GLMhukxjyIy9xobZwrcaDLKfK6xoqqtzxwDtYI3esaV4NVZ6TV24N+VWegkWhKCvaBkqiunmF+qgJIbcaP1VtBiZ7XeT1kO35eeUBXdI0at6AGt5gpUXi1S+ff/7l9SUCn18+//biJFYNvnphgTLqXYvjY3Xm2+JgcmJlARhVjMAJGbguvAqIT8FXrudDz6sfay/xX6H/+q+4t6qg/unzlwx6vr68TH9koF8TelCTW3XjuZBjFZYdJVEzvkFM0lvjZGfTVtnknhr4MAveHjO/ScoL6O/TvR8fi7wFXvPjl5ccqHBX9svLT1BegfWAL8Dnt0lK8eNPb0nee9WPP32TU7f21XOaSRjQ+u3r8/opFgz8NjTy76v+HUh9xNL2vrx8Z9z0eug92Qlmvrxd8yj78SEYRLPzMitzvB9/+kdindBz4imY/5Lcnx+CQ89ygU1PxX96vTv5Fwh+GvQh8x8vW4Cw/juWgOHvy71CT0f9I9l3//830UmUgcx/9/hfivurCfDfoZ//oW3/04RXyP/ysvKSqAPZYSfeZ+i3r+cjt/z5B/fblz/88jsQ/U/FnPO2cu4SvqZWFvle3Xz9+vMP9f3rH375+Ye2ALnmWenXtkr+SuZf+fW+zh88+Bz14x/ngvXVLM7yPoM+Mh36LS/+o/r9DdKsJHK/fV9/hr6vl+kFQ5MR74s+XPBdzdRA1+/8+NPL7wAfMmBN6zzq//PLf/4ntIsmdMr9Bjo7OcAeEOAmSr1JeSWMagj8nWobwI9X1RFw7HMcyP8pwpPGuQ/9+n+cO1p+cp5oOZtg8OsDAL8+ke/rd8j36xukALF5FQVRZiWQzByPXzIr8LJmWhLAXe1VHQATe2y8TwCGPk0fAD5Cv/4TyV/vQt6K8dc7ikcPbJKX4oRLdZt4b5Ntl9DLnpY4AHe9wXNaIH+SkgD0BoD6Cmyu86QDuDb5oY6jJIHcCCA2IIDxLhv46vMk7Ndff7WtOvySPYAUhx7MUM/AgA91oE+fgFV+EgVh8yXznDCHfvjt9x+g/wv9T7Puwqc1jgDQn5EAGm7Ohz0EKqtNwTAQJBBWABv3SPz2+9O3QEwGqAzELfInapomg8yMPffd0WeB+YQR5DupAPLIqwagMwSoBRJ96ENfsOh0a8LvMK8byPUKL3O9zBmBVAuY8+HJLG+gGgSi9sdXqK29+6q/2pV1VzEFJW41v0K75RGwRZ6A/yY174PA5DyLgPs/0uDxPRBS/VBD7LuIN2g/5SJUWJVVhJX1XMO3HnEBLPE+HQi3oMzrv2QTLXqTq+4p8nAPGAQ84zxD+mmK+Z1WQWDr97XvY6yJ05Q7t1VfsvqZ9Fbl3dkbqDJCQRu5ExX87ZlSdZi3gP8n/wFNJ0nPKLjPqNxz8PgXDcFE2ND63j08eBv60mIIOof+/zQYk5oMz8sczyjcCuL2imw83Dd1Q5ObHw0U4HoIzHuUyjf+f0ePdxD9kiURyIVq/Ntj5N3pzzEPYGor4COZke/yQcSB+ya594ScEqyq7k74kr2j9SvwyB2aQEyA2SC7p6R6X3C6+65pCEp0uv7G3E/vTLUMkg4qWjsBCeF7nmtbTgy0qqaiegYAZKc3FVgfRk74B6sgIB0kAZAPASUiUCYA0e+u2+fATFBPd+9/DI+msAAt3NYB2oJ203uDLqAuptyoQQBAUzONAV744S4KSj3gY6Dih4fr0Coeykwd6lNBa4pFnk4J8V0Enje/ZfJdl0l9INUC6QN82U/A6nrDI7Ifej5jBZRNp9q7T/pjuJ+2Qt/Tyt++ZHcdP7AclHQyMfJ3zoFAKaX1HUMnRKoBqqTeM4FAJtzJ9+3Bnw+C/tDl85/a8h//vc79zojqHyP3GQqbpqg/z2YPFnsnsTdQBTOQI1Hh1XdC+/QouE/PSvv0XaX9QezDS5+hf0+1P4h45vRnCH1D3pDp1jZyvClpny/gieUn1vg0n+5+yWTvW4ifeTCBaTICBv1glvchgF6CygumwQ+mqSeC6gEn3qEVBOFL9pEGzyIByJ0FEy3W+XfFe6dYENRHzD4YANzKGrC2O7VjgTdtVJJJ/dp7+Zy1SfL6klmp9883KBPIgzwFvph2NcDtoLlpIu9+9dHoTBd/3I3dqwnAgJt/norqFZqa0lfoo798hd47/vsWKmvBlufnqbedlgRDwdvH2I+tnu29gB1WMxaT3o9tzNRSPVvdPysx1dI7JE9U9CzOacU/CQEfgsCr/izkcP9gJU+EqBtrouGoea/rGujpgqbmFQKRA/UGSgggYwsm/HkZsE7llS3gO3cy95v/vpmVP2z5/e6G5rEX/O3lHSmeMXj2fWA4KMlP9cR4M5ClYEFw/cgncO/f7Qif0wG0gZYEzJ9buEv4C4LCPGyOU4v53HbIOYljPm1jKE0RNo0i+MJ1fRR1LZu2KZsgSZf27Tnh+jgJ5D2S8uuDy4BID/E9nEYxx8VJjCDmNLrALNq15gvLchGKWiAL3wXo/21qDHDxaefDrsmJH83p5I+nub+92OQcjBTmtcg8XssZrVnkfGHvQxtekH5QXikKmVXnonCabIdFMRzHPMluAiQlZYVDm43MYfBNzKNCmuOBwMxOIZzLdNzhB1G/oDskXVyWvVWISBPnDtXANBXi4omVDnpopFqjSmlpJEmpoung7cpONo8NlyuUhnnjWtrg+ILQzFviWblm5qU4JA6lV8nAyw5/6sRrH+RaOkqDkVyMylyayDrxkvNWa4pRzM5zXIwyDCG3Ur2+utZWVWKtNE95Zthbj8xElDcR2NeTOXXUG5qyL3PvKJBU7pneFgvn1qBezkmsXYhd7rR0vyxkuzpptTMkxXpPhimVbBKP2J7qpCH3qjxXazqYucNGO2gKsubIcl4xpRbt2tt5MDrXMqR13twi3klY1llfsCWSmIknaRs2ChvtwgdlfhRRrfBSzCB4Et+3xR4/ucQ1l1N1jIgLvuLH8/W4pKJEdCNCO5/PytUi+g0XipjPG+PGGaTFyiDxTkE4k3UWXIr1zBqJdBrj1RvWx8uZfUBrPL5dCOZWZ+hpuFWJHJrlZnEDLt8u4dBNlJrcEaow2wW1fOlte1Ou+Bp3rk7mnFQU75Gzb+CXvmSvjVaYEhocV8MRXwo5yjIZd0bHRjxqNXKmHZOob63nBsi+NfQqSypi0RmmsXCHNeOb/cB7irUQR+9G782TIjShIRfnEkuCcX+0N5V0M9MSH6n+eEilVFyXfTZEVwpj0VR0qEOZhc1N8LiZ428k0QBaBfUeXgjcXJZHT+KuqXTpC2JF6C6tLxdcMdJ9S3QHY02ZMH66DcfY5cj1zTycdQOVQMIefLXZ7BXdyg4nphvgfnFJvNXVHTk41REKHoIrDoeGqt/I42K1hH1lWNHH424VkZqEXjuvRi963+UV1juWcEPqRSVZa6fqW7So4xCm/AN1xZf87mgkYj+zilsXj4I38mOzYGSP9E55qR5gVyKX0eK4S3abSFq2g2uJoR0gOhssEVW+XjA55ecFPxdM7hwYCL6UmkA0NkuiS9Xr7SAMtcBdL+5Y3hhyVpeEqVWLUEfkQwJzeOiGw+BeO5qwY/VEBSwyK00qw1qrwEUPnR39JYZZgxPZaNBRs+W694dYtTLviA9aSXeFXEW0phuwDLPWrDth3TnK5/MsDwdtnTHby63aW2wGb6/78823DiIPH3J8ieQnZr8+9usNKidlw8G3DPE1XLxk5Bj2LmLv9sduFlAap8J6V1x7tShtI6cl1zSR4bYgkPxcipdEK3vqYukSJZ09VYp8CUVynqzqsJPtfb3YrjWmjWBu9EKCkk0Ov5KKVqut0HMz+rQd6rLe7Ga7Vr+uVvIoKqM+Y25quRWXxNjqFEmZAz2eozXbbZnGXPIrL7q01nF3OSBjNor2nC+lRCnwXbkXxU3KpmobaGNJbPl6jgv7eRKf2tWm9IeZoMmlGi+I1hIOGc+TkX6GBdbL5MOKXMVjPRbnNAuOrmDoqG9sbK0EnIUsqKOSY5nbwSaR+5pMsuPccKtWUeuNT46DIsKw7JhSGJzWwmyzDJBaGohtOBzlViwd4+Q5aWZnwcZoj5S+usGnC6MorW5s2H64ETCdXTmtrOshgcdidLc0U3F8H5x39ZLJBtnYUOlMDRYlXA+heQiWTByepWhHkQyPKknRnBdGyN9khTmzhRxyFG+xF9vn4N3QJM6BPzMJI7HpeCnq616ikkKH+YVDuYh1KkvRvxisfmmP+vF4y+JZpl7K6ODF5Ay2Tdi5bLXBOVjZ5rrXFXd244uNdFBtZEibwDlf65MqKVhHUDRcB8uunRNXmGYZzt8WJll33WxAaD12/Jmgs4u1A6urIZqLvIVnSUpsVkwdcAdUlOY3+WjyucZYslfpslOclthw5sHOfJs0DDnnJNeKWC8o5KupRSqxtwDI4kjMVKXsmUW6d5gF67OHpR64tbBzt0ZfLMywDOLDaF3SVGh4Pbsk6sFYHNKuFk5cGBSEXTTLITZL7Rp2++tohwhx2rPrvS0e4fl12Eau6hG3W5Fi3ErdZLtmPCE7QcbzjI+XoPjxulEJRW0bTNjt1+a1S7FI4Gsu47CEpCJNL1frtU3BBbbYyNeR2kaiJh9VIZG2yRrBj+3evzkyO4pUe+HCcq13cbXkrltuy1quYrEcm3i6GWqj5joy3B9P3kJyuMy9WgaBbiVHsAEesn5Q2Ep64FLvWBxRr8TYHaaITO9e+K1Uyb4hbjlNHLQl6keU4Arphiv1gZCzq7I+MoopnEKp3+2CqyeZZ/6iDXLdrZB1qwramBmbfReVlczWQ7XIdvp2lALlxg5H1+3imWOrg3RBonhztfu4ihxukTQwZYqjKRVpcNaM1F2APXJnbEWsUtHVvJX21SLdd2ZQHV0HQa1BYvwaN3FN2DDFbT+AChYU1hpw1kHOi9PtwOHJJo5qHyEBJV1ZeSmNs7UzOy9LVcLh3YmRz7DEFAh3xqWDxTo1H4QSypVcfjLYZb1TSlrUBPE0HtM4gBdn94zT+ZgPaSBWynHurVauMbOuHYc4wVrBUuaAswSG9qAEzExNGsKMew/u5r5J0nRAzYiEXBbhIrhmFtoxMud0DoEhaeLlN+ziZ1oTdyiyx5wubIldaPvNSXcqZI9Ecry86dUJZwypXyMeU3Pc9lZjo+ZUG0OAxWEnG2Em4vz80ukJ6aiDc0sCdX7pUdF13X3rFOqtFa6sK57RKNSUFiT/ThgWhQHK47LRM5a2Wj85l7pqF06L2hF3DNZDsONOXdgQOcXD1tJyrkV4kEVyvmljZV2FozoIcbqBLSnlWJM+4QQX8m24Zw/R2TqSMT5yqY7R5xghUu2CrGB9LZBLzDGymBBwLtPbfmWqWI6jiLw6p6BLNvgLSuOHK8edOdSz4JVpLqWzZBWFVCpqTDhhaY4nzKBMmSYXRpTUAeYFYk/SbDN6MaiVPemranviZ9jm2PaxfFkrTj16BbpJ9hnnpo5260yawMx8aiNsnyUsXBKOV6kSuLq5ZE6HMxW/TPQVdgobksCwZUWeHTUpHTcH5Dtj1rUrLkYFnZep73R0wd1o4jRj2jHaxItEHCRDDYYDuw4xNujlgSAImVSXqDEe1pzs75nwQOirwD4stVPFeo0r4/TlTPG4HNB5ItvFxRb4gg9xv9h620VtHSRMJnqrLXaBBFOSrklnUaQ1bsYouZA6TL1huTQmRiYbdSJ1KDIL43OQHkp7lyc76kxe08q3qH7d5mdTu6pKr5h0wpL8OY1kHPHoaHfRhU2CLILNWauX3lE6SCSmqYUa+S68LWFN3F9x0q1iKaHp88bTXBPsNcStfSYYRwnmpTkAmEhatghSw633upRFOxOWlQwl/IAqGcSiDlRVHIhcty1ks16mFjfcnHF78aO1Bnd7pqFn2r5D9pplspqJLTUqDof9UqfZdJOjuJ0XbTcgssjbaldItzLchGINI9e+vG11kB+g5UYEFst5WQzgbL5rJcpsj6fVerWPiX1TWfHiwsPRqWyVNGY6hnGr48Zd6rJAgb5JPCQSuwtk54SKdE94viStyXWoknEW7vY6fw2T9Wplo7uxkruCXPJVvhUyauvu7bEvDhh2zCU+kNmts9NoNVFWbWtnW0MXUIXjXZgTLFzP/MqpHPwK96CvqLDGaGYYmSV0RBti1p0FlnBD3GzJcrYIwPZ7dIcddtkHJk8S12Iti7LbLobLlS+t1bmw2BCkhNIPSb+7SYm7cebNiMZXFMnQy7A/pi4jK31sxsJwGIUxmlH4aTWX98Zww6Syxro5PJdmVUfuhNUO0CQI4q1C1nONPV/G3WFzxOU0W8f5ArB+Z+oWk/jxTb0I1/JWz6R25QQSgtAHc4EY7kLQV7StxJ5fdjOcXM7IpS9phuXjOuhYfCU2FxVe836FrgRMXaQqztFhIYaoXWyO7A1xYs4/alsBvV0Hc3ZSKYUNtro/bk+RJq4Upbj1vGX5p8OpaBVHVFKgyuwWN1t3V9E3sFnkt4y912I7kxGPDVdkjp0jsy/3x222GAALmP6hCOzcOdRBBYfsnhrVxdzqj8pYtfN9XFFCj6P6ycbEnd4QIbXKTN13mVm6jReuyce7tXfIr/RhIVQHCnNWLCADLbKWpEW3kWwJA2KtMkvHPA1uZuRAxkN8y9yLOWN2Ibum21XhUkKBCGbr1+4uXKN0NSDDuuOYJtQyswW0ButJrglut8/XekPm+Zy0MdcXFr4oN0Gc97uZS8aXfs3CmxIF8LJEECPyZQ8JOuOakONM0t0TtWFUP61XA70fDjhgV9Av4kPFLM6BL+xEhKCk1Uph7fNGueXSadjDOazWlGKiq1y4nXdriz3DGwsPZVDt9bFbzHvjaNoHA1ZZTAS9vmNnM7CR5Dh5Drj/2MubA9YsFcPOeI5YsSrs37yQbHOsWO7hWaL16+bYsFvq6lJoM+CuDgC7NbBZ1m72kZ1avS5YqzpLGydm6Si8hqjnyLMUF6gr68g4ZuNH+3K1Oy6UVxnBG32vzTADHhBDGkOGhn2M6S+gFG90hyxwzKj5HEb3vTPXV6zhNhJ2c7ClAkDsiG+qtDMvFUavw1I4CLK9QjS1QzYdK2Jrj0HZ/qzQm3zjnyvHEpldBVKV5s3R28f7o4Io9ZlwWfUGh/uw9GU7d+2B2S9bHGlYRz0mne4TS9gyXVSXO68tAZpFyJpqD55wnjvZCg7R1Rbm51bbzmLahXlrfQEIgPuz4TCY+Di7nFKihfH5cUbFjl6TPGXDHKbH9axmmfHUzOUiYixqLxuoSyqwSduCiJUnSs7JTbkgd10Io1vKugTWcmmsSwveCjgxV9mVXDQ6Ljhee6hn58wdbHuwtytF9pfoBtfmdQ+fuSMpsPnQ+ydje1aNjWUJupCuchczpbJtbheiOjTNHm+KFnHR42AVzAUwlIsdU4dWNovlqiddYVBUdK7h4/W6E3pmoy85Sk+Dzc1fHSKpBSAbGShzK27a0jDh9dWsYpTU9hv74jSy7i3Cg9QF5MxK616HF52a9bxGVL2CY6S/5jaN0+akHt6WeLeHl9stfZVus9BkogOmazy533DVNkBhjZI4qZiNySlb6IcFz7OHZhjmq4Y9rAqr6fSlGFumzTEbDI6R04zTJDLqd517nA+DmtH04pjtFqXNE5jnKSOZKYhAzToTOEs6MczL68t05vw8Of5XHwNPh3n/a2eKj+O/9+dH90Njz3I/39f6/C9r9MvrS+VEQJ/HqWmdtMHzkPG/nZl++icPHabJ4+O56vSQa2jeT9cbK5h+EfQSZW5bN9X4tc6T9n5o+wocV0+/T6jfdXy5m5QWzf3ehwnTeez95P9rk399PP99mX5AMD268dzoMWK6DJ6nyK8v7ghiEzn1V5wkvnpVMRn6fI4B7MPekDf05ff/B5c02XB0JQAA -->
