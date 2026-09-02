---
name: "rar-cowork-cookbook-scheduled-brief-manage-opportunity-process"
description: "Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_opportunity_process", "rar_sha256": "12149c0d6b8f2a8c63e24f63f910c569516c18ace47ddd6fff00767697670a97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_opportunity_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-opportunity-process:d8c582e393124d66e46e9d39477f83236dc7e542eb86c4f115fc64b88d8fa4a3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_opportunity_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_opportunity_process_agent.py` is
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

Manage opportunity process Scheduled Email Brief — Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 12149c0d6b8f2a8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_opportunity_process_agent.py` first:

```bash
python3 scheduled_brief_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_opportunity_process_agent.py   # or on stdin
python3 scheduled_brief_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Scheduled Email Brief — Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_opportunity_process',
    "version": '2.0.0',
    "display_name": 'Manage opportunity process Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage opportunity process for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3af66bf7564c6f08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageOpportunityProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOpportunityProcess'
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
    print(ScheduledBriefManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjSJLvV+Hl/lHdo6yUuCHHxmx1cEgIhARCgq62LI7gEKe4JOjt7/4CSZlVtT29O73vma3KKhOBh9/+c48gf3uymzrMy6fXJw3YGSLYSRKFoETszEPm+SUvY/grjx34H3HzrC4jp6nzsnp6fvJA5ZZRUUd5Nix3Q+A1ie0kAEnzMouy4LNTRsBHQGpHCVI1aWqXUQ/vI6md2QFA8qLIy7rJorpDijJ3QVUhfl4idQiQElRFnlXRwC6/ZKD8OwLlRUEGPKTOkbLJEA+y7RBIfwEgTroXqBK42mmRgOrp9Zdfn58ieP30+tuTm9hV9U1F4M0GveSbEptvOqh3FSCbxM4CSF900DUZ/F6AEuqVwlsetOfx7acKJP4z8re/xRe7DKqfX79kyOPz5Wn4t4M6DqbUuV3VUG3XLmwnSqCkF2SaXOyuglbWTZlViI1U0LNZ8HJf+Y1TXiD/GJ79dBfyEoD6py9POVTBHvz+5ennwQFfnqA/4PXLwKX46eeXJL+A8qefv/GpGucE3HpgBrV+eXt8f7CFhN9II/8m9R+Q6z3CDvjy9J1xw+eu92AnXPn0csqj7Kc7YxjHFmR25oKffv4ztjAMbpxEVf0v8f3lzjgEtgdteij+8/PNyb8io4dBHzz/XGwBw/pXLIHk7+KekYej/oz3zf//iXUSZaD68Pg/ZffPFoz+gfzyp7b9VwueEf/L0wIkUQuzA9bNK/Lbm6Zy818+ed9ufvr1d8j6v2Wj5U3p3ji8wWKNfFDVb2+/fKputz/9+sunpoC5Buz0rSmTf8bzn/n1JucHDz6ofvpxLZS/z+IMlj3ykenIb3nxf8rfXxDDTiLv2/3qFfm+XobPCBmMeBd6d8F3NVNBXb/z489Pv0OkyKA1jXt7DKv83/4NkSO3zKvcrxHNzZt6AJw6SsGgvB5GFaI/ivqrJi3X65fU+4rAu0O5Q4iwm6RGhHKAPVgPQ8QHC3If+frv7g1TP7sPTB1X75j0dgPLtzs0vn0HjW8PaPz6gughVCAvoyDK7ATZTVUVgcRZPYi+JQkE2c/tIB1qFt3RZzdfDshTQRl/R77+6+Lebpxfim4w7EsGI2VHN/AFKaSFSA6x1x6Qy+lq8BkCL0SXMk8Sx3ZjZPjRFC+Dtw4hyB4+dGGDAVfgNjVAktyFJvgRBOvnAezzpIVIOXi2iqMkQbyohG7Ly+7WiaD3XwdmX79+dewq/JLdoRlH7h2oGkOCD4WRz5+LEvhJFIT1lwy4YY58+u33T8h/IP/VqhvzQYYKm8WjBUENV9pGQWCtNikkq5AhUSAQ3WL52+/3kAzawQaFwAqL/AjcFkNu3xJjsOAep/cgQZsHFUH5kPSj35BLCP2CRDX0Fqz66vlLNrDIIWl5iSrw7sT74rvr36N+lzPEpHr4EMbJL/P0RnvLySGYbl56L8jSRz48Bc0dcmCIaJhXNUzjAmQeyNwOrrTrbyHM8hqpYCVVfveMNBU0deD81YGsB+ekEK7s+isiz1XY+fLkvVsPRHB1nkVD4B9pe78NmZSfYI7N3lm8IAqA3kQKu7SLsLQrcKPz7XtGwI73vh4yt5EMXJCh14MhRrcav2We/OdTxsckgHC34eQ2ECBfGmyCEsj//iQzaD8VhB0nTHVugXCKvjPvqTaMYIPl96ltEHcXMwDAx3jxjkTvGP0lSyIYnrL7+53Sv2XXneaOe00JldlNdzf+Q52XN75RDXNkCHpZDnltf8nem8EzdDuMUDXgGizl+G7Lu8Dh6bumIazX4fu3wQC5p99QFjCxkaJxkshFfAC8Ww3UYTlU2CMYMGHAUG2wJNzwB6sQyB0mA+SPQCUimLnQuzfXKbBShuDc0v6DPBrGLaiF17hQW1hK4AU5DJkNI1AhDoAz00ADvfDpxgpJAfQxVPHDw1VoF3dlhrH4oaA9xCJP7Rp8H4HHQ5ilQ9eB8j5KEHK1PbuGvrzAIMAKu94j+6HnI1ZQ2XQoh9uiH8P9sBX5vmv9fShDqOO3fgAn+VsKf3MOxO4yrW5wBFtxXMFCT8FHnt57+8u9Pd/7/4cur3/YC/z017YLt4a7/zFyr0hY10X1Oh7fm+J7T3xx83QMcyQqQPWtP95L8PO94D5/V3CfHwX3g4S7w16Rv6blDywe6f2KoC+Tl8nwaB25YMjfxwc6Zf55Zn4mhqdfsh34Fu1HSgxQBwvb6T46zjsJbDtBCYKB+N6BqqFxXWCvvAHfrYN8ZMSjXiCuZsHQLqv8uzoebBriew/fB0DDR9kA/d4w+AVg2Bwlg/oVeHrNmiR5fsrsFPyVTdEAxjB5oVeGPRV0Ohyo6gjcvn0MV8OXH/eFtxKD2ODlr0OlwcYHB+Fn5GOmfUbedxm3DVzWwG3WL8M8PYiEpPDXB+3HptMBT3B/V3fFYMF96zSMcY/x+o9KDAX2jstDy3hU7CDxD0zgRRCA8o9MNrcLO3nARlXbQ7uEXfpR7O+p+ozAGMIihHUFs7WBC/4oBsopwbmBDdobzP3mv29m5Xdbfr+5ob7vP397eoeP4fo+LdzzZ+D912e7wbnvPfltEGHfGA0T2M3Xt0n2DdoZDb33u0fBMEi83RPz6RWiEHh+GjxaRnA8728b8Ke7XtCgbzMw5ADx5HM1zBJjWFeQE+zwxWBMDLHwOwHD7ci70Q8Xr38+OP+3wPDqMS7JYABncRQjPIoCBAVYD2cJmvYZHMMpz6UBSWDAYSiX8FGU9F2KcBjGY3ybsHGoziAttR/qjNEhKtCQD9f/P4z1T3dOsLdgJAVZoRhKsO7EoxzGx2zGpXCAET6F+yw6cUmKJVHKRRnbBQTteR7l+/5kQlM0xcIfE5ulB36PcfKu3tv76P4epztSvEGUTaNBecy2XcalUcJjaZtyAT5xcBdAPTwaBxOSxX2GAQRc/7H0EashlHcPDPkMJ0k4x7WDnN8esR9ylCIgpUhUy+n9Mx+zhu0cxs4uXI/KZHS94tQW3xf7UWHS0sZbHD1/NTuctIuceHsnmDfd7jipzX0yEjQv0RdbkeV8jB93+qRv8Muu0MPVgvAW0w7sGmfTV2OV6vnZjFt2oDO6JlnMeNM9n/vsgPJ7o+DSQw1WaWUYRSaFx0yg4p45HgrUWDPjpm578yzL3R4rqivaFqXQSmdzUtvOSevRNR40SsqMTSGR9jZmSKt9rQsEWuky3mi5Hxk7q3WLqycY3AF2sJnX1FMVU/aJbylhp+gFwzR6OHbb8jye1ddx2xvX7SgEU+MQuXGZGN4crY92ImrmZrJzYjecX0/nkzWOlP48WR9IQ3Ji2zrFteWEDHk5HwRxRXAz0dBQbR83esSaqqVtJ6v0TNVbVcKnjax7pTU94fy+TexJus2LEtpeu4VgkXLp5X26McKKRFmpoY4gJ/kykWN2KRBxse/E3lvqmWf1xW7eGVq6sY4cl7rcyZqvs1VuU0nDZ6W1RnvxIm5IyyLmlyiQoMNC9wwE9qKukvRg1fKOoOzk0iZFtl9saq0wpDXpd0Q5ceJDJWfKQlmfRuksXZ3MVTNBhfKwbg6hpXIJ71ZppLMpgVUGPy7r9UrbzyhQTIhlHJaVNc/LjXOeoa2yb4/Cwdkc+2subBkJd9PD8diqlIBtcHnmHJ1dtzksbEJcOyoqj0Cb7S2ucM/Kan88ndReisqjdVbMorSz9Y7jy23ZxydqErg4n46kIrsmPT+aN5tjdLaiziW2sTLuRX65DczW23Zoopqmqo5Qm2rIA+8ZJgD9wV06HM20unxNZ/l4GzrLHrto8Zy2izmFFmtaS9VSp2Z96PXuQey8U0bwKLk+EYpIbNVKlWo91MhzyyxC66q0YzIcBfvD7grOFS3i0xiXcKIgJOyqUWepqwgzjs+1cTYsTlwLhcOHFeHx5vXMxyEqlrOeaOLyKBtMsTGlGWiUFdpJ/cYuZ1hW1NJh3ie8SW4UL6pNeTKVDsx+t8eCXcERnOOemng3xWp8ac6p+T50+EQ+WITrzK4SnrnnzWXT0tLhcLJTKeg1ZpdG1tXKC9JapqNDdfATfl+6arQxlIrVHbOWnbOanqes0kcTn9zpdT8+jYtRLcgbsF4rsggOm74ll2XEYkez0yQho64nu1/BTUkG5mvBPWC7lMJrdI4Lo3VQSG0+kVeKXy8N6XwOuglobWOZA6rouyA+o7RI+hcjY5cgPqC1sDrp5HgkHOIulRhmvUxyfmTBvopTI7SwjqynTc6Lvb037Mt81x44XrloCUjQUlp42kg3PLfm7QpdLCM8nS9jVQ2o8XJ7ANd6UVz3O4WY5GMuou1NuFlmR0yLjLkSnAtmK5mRC7eBIX4gZuxaRKO5rLpAsxx3ug4cS+flqmlFce5Nz8kq8YKFKdNZJtQVqXUOX56t3ZHCNtIlVKcNWlzaWhJUkhpLhxijlL3rU962sOFm7drWE925yMdNMLUMNN2JoVo1aGu3Wx2zr2Di0HjPTEXM6Wl2yqrs1lWp6GDqeLUK87jTavpA2fUKu/iHyPQAFasHzRCu5oHoSDoK+yihLqo0X7OLSMBPMmZlxCgAs21/kjhyAxEEpUdREWvKYe9pNLsnlQzrY4aTF+vlbDt1q1y5NOaxWJnCqp86BydzA67RAmZVCjRU75i0Gk0s1lM8mq5XxcFD81LRpq7kmPvW6qnQbWwjlExR8Aoy7ZamMXJRYLrepScuhUwVJ8UiRcM4wQxwSaxfNGv5qqqURPUOOQKZzo7BnqgCp5NR51SyOXtd7SjDF5SuYrOTK89ZSpH68EQzmCYluL+XG7K6dJw8SphGXIzU5EizzIg7dq6aBQ5L7saSHejuhmEmOL/OeWamo5rJbexrL/VRLaXHiET3qbf0xiorruoVulkLhLZaKjtfnR5G1+ocl3JacHHrm/w2XOqHXa0WRCROmEKkG0Y/c7vEtfZe3KN5lU3gbfloWz67ifJydknTq4HaoB4Rc27Vj6jVNdg7iXPJ7aCcgwV7PS2as53UF0LU+HOOR9vEKtte28LYatNraEvKDFBadzqw1IZjT7IjW65Zbc1NXpJMcIkjlZZhF+dQiuWP7OhYY+pqvqrRBaVw53leaInD1+akcWkWpogTiaFtr0TMa81WnCa90CcjN1kJfMpqh/O+IcvZGR/nIT035+d5EybmZYRq1p6TA/3CL1nUtutimrAT3RXLQ2E4WjTVC0lIV5WJ8lOqSo2NVgllc46UkRNFV0sujkayxXSTm+1aU5jO/cByZxpj7OKqovQaAFFbTPPDElYF7/lGdoBNNkAPQiCkS3/Cc1cmHgFnUjRoB4Jl5J/4qUXoy4sw71FMF6JqBWxtaZmpEIb9FCfT4Dhdk7Sz2y0cfo2WpFuPi6hUDZmjEssI1pSDGegyXFPNrlF26ZQiacy1Ftie7rh9rvtx2qxKkO0kfeKcdVuStNOlJ+Uw13eMUyhlX8Vaeyk62E1yhekttdjPm72th2TCTyz+gIVLAU5XVn08jRt7E6uxueOmzkwdjyZtHRzDQqjFXadm6sqYufkaNlkSm0hTKvHOlLRY2lNyzrftOKO0aqyDKaHDLh142Eypzyf7dBL1sGKp41FidpbT0nlHHS1KxuRyF1PppKmxktwLNGf26UUIVTAWFvlSU7jttJoI457ESMMtr6bYLNG5boZFbp7O0nHN0OqZY+zuuiKLSWLqZq3CzUE+kY5b2F2TmheK4EyV+8tx0ZCcvD2XWQsCzRbNIOnOJ7wku9y1UPYkdtxsK7AovrYvOOxV20tzhulKzHxu7K5k9ELtTwFJLYYRrA/4hXCRdnNZWc5mG0mzVSrGIy4+Yv12t1ylBjZZYEd+Tcwp11xF7s6hYLlN+4vuYIfjjD+crS6ypiSH4ztxaXsrbk6g2+NR41bTI69Txt5XVkm3qbPd2skEfjW54idJXoaRoqanZMHM45DdFsCropJV90Y45STME73QPLeSPbK43vLljLNiiWKxdjPSU281zq1CCN2LSBl9lxyTEptezwRrixhTmuiEtLocK1ewz/gTi4Tbq2vdHtlluHKITmHikjHiIy62diaPpe2qc5pqvg5IfazzjrbeK3q8mVb6SjTW162Cxqv9/sqzphbyfZxNaXdlLFSSRDFxb9m93yiigk35TZuvsUVxjgC5IQjqsCq6mLdaLUF3+/msMUAbcJjerjhVmmVSTO+nVSR6yTynfD7pIrCJuGUec8AqtMyoG2CqR21W2SF9wXjJJ7NzGxft3qiXJnGS+O66k+tsr4YcKqX6akUFNDVm2hOaOlctqCVmwTCYkqXmMpnslUQssm2SlqedG+bSrEt8eXxkFHpuB91pr9r+1OyZSFCLbjR1trOeHzfXI6e3ooKjuSZx9XY5p9jEyI/RastWWI6N8HOM28tpnefBhJ4uGX07EoIVM7JSi1/2KB+je3GxDseFMV4JUzR3FVJQCHbtUsduFaVXmMKzaz6/LoM6myqCxPSH9XZBLjYVKbflaoKNcYI7GXLmcXN3OrePwHB47+L5Pr2ZnUNtL9nLDfD163LLonC/EC4swdoRq0WslPQKtls5TcDeTDDvqHoxzU27Jb5Xz01AxK0ob05l1VNYGHOwvSsJzM/DJfQi2+cmJ/0SoLnJFHptSkcYN2tk7KhxRp5OE685sw260Q9s6oHJLmbx5GJ1tXoZMTiPugvRb3TFFAS8Li845q53x/lkRMhbr0Clcz4Bp13FCPNOv4j6Es/PymVD0d4aw9aGS3tiPCOve0LbFKmlqFCLKcEyWLpnuZgprcQwgNMT1Uh3zQvHcXpVe5wX6CRLRZU8Ks5Xhc5UMsf18DJRJjPRr1ZHGRqROIstpmJeTaKLJF2MNwGBqzxG4g3dZznDZCcWfkbXLTM9wOJF2zFVjE/F1bHxJvZDo/fz4nBpr0HmHiORzo0JNT9d6qZIpuTlgCsmX7ZtoI/gPl+YL3CbzIxkxgb1XBXVqU5yRgBiPF0QiyAGV0u89q3DKus624wsQUrxdbbBN2HO4Fxi252hC4rudZMWcATRy0GWGnFkWv4MTzaGs6uaY8BqbCO0VDDe+hd/4VrerCJO3ahZqieGtuk2no0u7RLTD5sC7nTZ7Z4da2rbTFdAcNZzc8EavDV3s7w87trGyf0VfqQythRxoOxn5oQ5UXOrmkusLMYeI173Iti0ZzftEow2Tk2wlpdCCfc8veIc8Oq89u091VQml9Wj3LuiYnOsfI/Js83cDGY92zcjf7bNLtG6ADNuDQhu16yO2ZXi83Z3oO2xrRZLeRFOL+N+ctTCZm6wZJuVUbyjiCXj9vXp1JXVIuepRPGVMy0L9BxOXu6qJrHMxzlgz4K1KR9DWPBnUvapi6uqbVUtOBUPQDEtZxnGZnW8DphoI8/lWTrlcIWwzQ0/DavjFg6CIz+eouhhstQXPWsd5/Zkqc2PzJmelV7WTJor1HuF4qo273lR0C4H3/YqnCmrwJ52wbGtieA0rlLtSlPU6WjhLt1cHJbg1pbVnaiLMPO7ZlqDzazKTcEX2UBmI2IhUxQ/JpiJFeF806Sz67QRhAtNJWXmxZs2ZQmjMRRFYTMH1aQs9wg3YtUdaVKnmqhEfH1dbWWO97dgfsxQaJIp7hedoF4bT6QN+ZSzIn2J9r6xZwvDBWIypzmMDhf4oqbPk8O6pHDHB+V0rGCHMYNOaJxOU4aLlhD8Nj59IIA2g50/rCFSrsOSpSsUlk2oZNZCnsxGApDTozkiCC9FwXjm+1V1EtU1vUidU+tryiLiT1eYtrwYLLLwXDZJao1xWtzCkPfXoD6K6qINJKxkNH92NmfmStJHZUkwrkfPdpxy6OXFRtcbVUYbUrGo2gibcxZPNBEFF2a5H/Vws0RxEDXmi8lemMsLGQ9XCS0o59nZdoDSzLuz47OUdDzpRTFa8+bioiyDJmR7kQIbU2NU8crGKGtz3pijT7Nuy5fhHKxPW744LcIrvwf7ESl4W5mQr7PsrAdb7EDvQTLTU5Zfb/3WDcbCYev4nqJu1q2I76jZcp3X9MYJ2gODiY2b8hQeXbOReWCxZjvyvQm5TTdhFV9bJi8aegskjFQYy9WCTenLtVKwbL+Z9Wl2vBDMrImWweSQrS/BdXLaqrm72+B9N29BpG1yJnJ6feRUzg4wZHWq5LSs215POk40x6MpLWhu2zvSdjp9en66vQJ+eoVhRsnnp+FVwePA/392TBz0UfH24InTOPb89P/vxPJ+evj+evB2/A9s7/Um/fV/ou6vz0+lGw2q3Y6Yq6QJHseV/+mc9vO/foo88Onu77eHN5vX+v09Sm0Ht+PuKPOaqi67typPmtthNwxCUw1/81J9d9gLr9Kifhwpf2fY/VFVALd+q/O3c5PX4Gn4y5ThpR2Anfrja/B4VfD85HUwppFbveEU+QbKYjD88dpqONcd3ls9/f5/AcKND1DjJwAA -->
