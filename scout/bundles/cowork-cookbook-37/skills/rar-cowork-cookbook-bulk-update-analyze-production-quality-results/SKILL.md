---
name: "rar-cowork-cookbook-bulk-update-analyze-production-quality-results"
description: "Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_production_quality_results", "rar_sha256": "3697538499196f7b27af7666ba7033a96732ab0f793bc670e0525a4476f9d0c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_production_quality_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_production_quality_results_agent.py` and in the RCI capsule.

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

Analyze production quality results Bulk Field Update — Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 3697538499196f7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_production_quality_results_agent.py` first:

```bash
python3 bulk_update_analyze_production_quality_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_production_quality_results_agent.py   # or on stdin
python3 bulk_update_analyze_production_quality_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production quality results Bulk Field Update — Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_production_quality_results',
    "version": '2.0.0',
    "display_name": 'Analyze production quality results Bulk Field Update',
    "description": 'Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-production-quality-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07d3aaa9f1ad24c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-quality-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-analyze-production-quality-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAnalyzeProductionQualityResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductionQualityResults'
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
    print(BulkUpdateAnalyzeProductionQualityResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WbejVpbmX6FvPdguRYRAiCly5VoNQggxSwg0OHKFmQcxz+D2f++DpLhhVzqr2tX90Iq4V0Lss+f97X0O99c3q23CvHr7/KZ7VgbtrCSJQq+CrMyFNnmfV3fwlt9t8AM5edZUkd02eVW/fXhzvdqpoqKJ8gwsp4siibwasiC7Te6QH3mJC7WFazUeZDlVXoNbmZWMkwcVVe62zrwOKlsriZoRqry6TZoavDt55daQX+UpoIeirGgbKInq5gPUR00IudX4sWozwMPrIq+HbM/PKw+olqZR8wlo5Q1WWiRe/fb55398eIvA57fPv745iVWDr94YoJvxUIp+KqO963J4qnJ8agI4JVYWgCXFCByUgevCq4CsFHzlej70uvqx9hL/A/Tv/37vrSqof/r8JYNery9v878jULYJPajJrbrxXMixCsuOZkmfIDrprXE2ummrbHZdDfybBZ+eK79zygvo7/O9H59CPgVe8+OXtxyoYM2af3n7CcorIA84Bnz+NHMpfvzpU5L3XvXjT9/51K0de04zMwNaf/r6un6xBYTfSSP/IfXvgOszzrb35e13xs2vp96znWDl26c4j7Ifn4xBhDsvszLH+/Gnf8XWCT3nPkf2/4jvz0/GoWe5wKaX4j99eDj5H9DiZdA7z38ttgBh/SuWAPJv4j5AL0f9K94P//8H1kmUgar45vE/ZfdnCxZ/h37+l7b9Zws+QP6XN9ZLog5kh514n6Ffv+radvPzD+73L3/4x2+A9X/JRs/bynlw+JpaWeR7dfP1688/1I+vf/jHzz+0Bcg1z0q/tlXyZzz/zK8POX/w4Ivqxz+uBfKN7J7lfQa9Zzr0a178j+q3T5AJatX9/n39Gfp9vcyvBTQb8U3o0wW/q5ka6Po7P/709hsAiwxY8wSDGSv+7d8gOZqRK/cbSHdyAEQgwE2UerPypzCqIfB/rm2ARV5VR8CxLzqQ/3OEZ41zH/rlfzoPJP3ovJB0OUPk1yc4fn2h4tfvqPj1hYpfX6j4yyfoBKTkVRREgBg60pr2JbMCL2tmDQAU1l7VAWyxx8b7CFDp4/wBYCf0y18T9PXB81Mx/vLA/+iJXMfNfkYtQOF9mi0/h172stMBEO0NntMCcUnuAN38CGDvhxnP86QDqDd7qb5HSQK5EQB30DrGB2/gyc8zs19++cW26vBL9oRZFHr2lHoJCN7VgT5+BEb6SRSEzZfMc8Ic+uHX336A/hf0n616MJ9laAD7X3ECGgq6qkCg7toUkIEQgqADUHnE6dffXq4GbDLQBEFUI39uavNikLd3z/3md52nP64w/Fv/AX0mrxqA3RDoQtDeh971BULnWzO6h3ndQK5XeJnrZc4IuFrAnHdPZnkD1SA5a3/8ALW195D6i11ZDxVTAABW8wskbzTQS/IE/JrVfBCBxXkWAfe/Z8Xze8Ck+qGGmG8sPkHKnKlQYVVWEVbWS4ZvPeMCesi35YC5BWVe/yWbO6g3u+pRNk/3ACLgGecV0o9zzB8dGAS2/ib7QWPNHe/06HzVl6x+lYRVeY9GD1QZoaCN3LlR/O2VUnWYt2BymP0HNJ05vaLgvqLyyEH6vx4l5lYPcY8x5NnxoS/tCkbW0P8Xk8rDiN3uuN3Rpy0LbZXT8fp07jxlzUF4DmazSLDuWUjfZ4dvyPMNgL9kSQQypRr/9qR8hORF8wS1tgIePNLHB3+QD8C5M99Hus7pV1UPn3zJviH9B+CgB6wB40Ftg9yfU+6bwPnuN01DUMDz9feu//LOXOkgJaGitROQLr7nubbl3IFW1Vxyr3iA3PXm8uvDyAn/YBUEuIMUAfwhoEQEvA66wcN1Sg7MBNX28P47eTSH5RkzoC0YY71P0BlUzZw5NQgAGIhmGuCFHx6soNQDPgYqvnu4Dq3iqcw8+b4UtOZY5OmcH7+LwOvm9zx/6DKrD7haIJuAL/sZhV1veEb2Xc9XrICy6VyZj0V/DPfLVuj3LelvX7KHju/ADwo+mbv575wDgUJL6wfCznhVA8xJvVcCgUx4NO5Pz977bO7vunz+p3H/x7+2I3h0U+OPkfsMhU1T1J+Xy2cH/NYAP4EqWIIciQqvfjTDj8/6+/gqvI/fC+/jq/A+vgrvD1KeTvsM/TVN/8DileKfIeQT/Ameb0mR4805/HoBx2w+MteP6/nul+zofY/4Ky1m5E1G0H3f29A3EtCLgsoLZuJnW6rnbtaDBvrAYRCTL9l7VrxqBsB8Fsw9tM5/V8uPfgxi/Azhe7sAt7IGyHbnyS7w5g1QMqtfe2+fszZJPrxlVur9xY3P3B5ADgPHzFsnEAowNDWR97h6H6Dmiz/uAB+VBiDCzT/PBfcBmofdD9D73PoB+raTeOzTshZspX6eZ+ZZJCAFb++079tL23sD27hmLGYjntujeVR7jdD/rMRcZ0Bjx5tbfv5euLPEf2ICPgSBV/0zE/XxwUpe6FE31tzAo+ZbzddATxeMQx8gEEZQi6C8AGoCN/6JGCCn8soWdEp3Nve7/76blT9t+e3hhua5x/z17RuKvGLwmicBOSjXj/XcK5cgZYFAcP1MLnDv/3LSfHEDKAhmG8AOxSkCQ8k1RSEU7hP2irB8Asdx2yJgFLUonEBXlg37BIXaDk7AHoytMGu9JnCfcmEHA/yeCfv12fYAy5VlOaRDIGuXIizc8VDYRh0PWSEugYLlFOqTpLcGznpfegcQ+jL7aebs0/ehd3bPy/pf32x8DSj5db2nn6/NkjIt4iLZSmhTFe7TdUzdm0E0CxVZmVRWI/zOtXeWpajtfbVI17sI2x9CoYxSWoBzoiSN3gduvApUMkkkrRnX8uTuXIDE9+x+yIJ1Kywyvm7LDb0/Rh42SdeliOwMoVyd9KJxltxJOnGubeiFfcMMM150tRFPR/HecQ1slOJoLhYL8+KYeyM1b2ed4U8LQeKtyWnvlHBlJcR2y7tu4LeztG2n/jKGJC62R/HWKEf+0ial1CiDOk4lz/LnBLHPe8QVDT06pjXFmSpTuhqP4H5nw5h2uZkLqR68biJgbfDuKOtZl1GvI/xctLpSH0rDWiHc9V7fxOG28Yfz9SK4K7EwnFgTXW4Sna47nMypPLHmSaa3fLltzahTT85w7VwLE7mgpgZJFoO61dmTZI1c33FHhImixjzHxfpWCFIlYnI7rBQlK9vCRE8EwRqJUyRZFHY7N7jzHofxZwffGm0CJ0GaULSwTaTVYYWNgjPoF5FC6maNxWv27tzbkTmeDrVkYVO6A+LsbER8FWuR+8nB+iwXPQs5lwY/oklxpikdlbMiqdJci2MkPaw28VUJV0hYmdX5FConPhPKezp2VHI4anp9iuSK8bTQ80pjL8LhKRLWmBpYZk2dKOeG1c1FU3tXtFMGx7CbSy3z07UyJ44cWn6NXRXiHomEhtbwtHN2Q7Y1d4Vz15g0FbWlIoqNe8/5cdl3YiYdZa48VFMU43DkoFy5EKNsSKbdYtOqlyjdkpxS5+ftMokj5xCsO/cwTol2vcrV0qVc06nEtqw17SapOy4yycu+wbKIDl2RbWNfaPGT0OGc0KzEk408flzbH5SkkmJMnoj1liexyTktSI4i2FFxcOOot8tgITtxQS01FJb7UZ2SS3YbSCENx57zuTNgZhzPZjbdjvsqsZJzw98jBUn6lSiV8rVXItOPleJKSumx2p0XRnbdCEtTT3KMrbKzF5D+hHKnzTWKupo/l/vzmov7G90hW0Nx7tbRE48tkx33B9GuGC7pzX5b6KMoWvXUr1M2OnYaZtxCVxsTkhJh56gSQia2kT2ASX6N3C+ugnHwRLUiaRjAHZNQkdNkNnV8V9JytZiQK+oU+tQyi2xJStQOg50VJ1gZcr2ydiUS6Xjm4YFJCWMjcM1ti5zvpB1Hx5hvDqZxhltV1+il5mj8yQSL3VusCaygiaXsDvkSju9MuC2RDBaX1bAZLtmIh5cGvpaKtlwOWCEXUacxlnCLlnJ7Pk+NacOrymW2asLdFm7MSZmnCLKomFpztYo9Zvqwvz1Xei0xV1beThFAIdc3ipN6TRNknewzkpOX22hpB6Eo+sum3OKGdTY1aodg/KI4chsAtyLOocRWUbVRP3GExUi7k33KjLodJp5t5EIGWBbuokIenamKzc2G3J2SrBSiFtZjXj6NVbt1EP6AxQuvG7FK8bIdqg37gsQOKnxH0WJ5EeQ+8GhCruRWFhqcaTuEiy9wlFJGde7c0OCHAyLVyIJfrX10M/GN5BAj2AqR+X60VtN5rYUMeRPC4ObxGqNH4V5tMMUeSKS+iqR1WBwwHt8n2j5yYEQbFnzLnE6xtsWUUWORJRUX97i5GJ533RiYkq2me7Q1epneSYxX50rc1ZN4b1iem4u8x9cCbZT72BPioTkvKJtt6etpqzAH3rSMw9Fjks053QmSKafYgY2vgXDQr7dVltr78GAwk1mFI8pryeYulSmH5MG5rthVO8EDfJkWkjywMo4vpuqGu5mE4O7dCA/yWUamqqJ8UxCO0cVPlaGmooOzYbc4JY43fonl9HmFao7f0oHLjRLcwfdFkvCUixZ+EZALfTFhh6UoBsxZ8BZge3Knmba/4sZaYdPIGet9FxsjbqpbibXJS+9bkyr0Tb+90HqDtXtuscF2SmZypxzZk8ROO+6lzivNwgw6ySDZMdmxt/y0NgMxgJkuYZirFvhJebMOGhpR67qMSl6oYRUT1kWy9dHVpblj+d49MVtTMUB7oOt0vcJ2jQ6vA7vUkfNt2ls1wvawseQ2QbANJIMqpOxswpjQDHS7uE23SIrDmL2wnL1uByWPhayQ7QM3ufF4lm44z+xCsdTz9GhelGa/sDvKieujN+7JYLUPRV7q7tWGjqWddM91asvdt8cVgrlRejGPmsyjnERfFDPfbG0PD+0yOu33dpDp3LEoV+lmw+tUbywQsXK2u0GlT4h8XA95wy+CVD4OMeJO5rEbnC023MfGNRHWVPADw1BhtRVaJpQ5bTjt9HECg0ay9tfKGF5CB6PPJmW6VqmkrOFYm5snHDbJVRUIzV3Yl5JSjkmzv23gFSmIV2bYsERWmWc5FXc3csuclWwxKaeKVB2bKq9hfUgsZFGf0XoYUDDKWcXNDKSVjZqIGEpoe1wpx5DGMeKs7th8hS7k7JCSooHYkXyC8Vx34tClS7HbOsYtL1wx1FiaXVWb6VhV9B1bh21vD1yBHJrj8VjIopOr1b48kwJTaosTV6+0lsjgELe2Cq2Q2ZKw+dUk9aLaiqC/XzTGYAp6m6COAiBGc3ULaXT/iol8t8z4cZWQpSxFd9e6B8SdRgm3URnZVZUJLRRnGrh7u+zYU+FmOXUdqd2p9PUVanX5YOcls43XO6drm5o/2LTM6UwNa7cpWOGmE0tXftwjm5sVbnMrxpULQBmlTBxrZEC/W4tZQW2SS3qQcYId2HO9txK9ylu2MB1pJFKDEylrf9EOgrt3omQsI6rkxtK5mBR9XzPByJHIUhADwj6e2MCVb7C43mBSRrB0cWvFveyTk3IoNlMU+qVCy8leCtDjXrlQuo1tTlLlF9ecgc10zSwuioC7y843Ys5aJDifsF3MVxZ32hljmIhYzpjra8OPm40QGWDkE+Da3SzJcQEwXwZUl3PgsuO46u/CVKSqsoFHpdVS3bayUE0uVzU/qS1uxF6iiUHOktUugfv6dEZMr9b1ylwz1G3QblY5uoTUwkLFdPpwB60hR3yTr85p1bfaJcxiaXUz1bPTqmWIozGPmDroQ1cbQ+C2a8o8P6Jk6UWWS/XXMZ/8hbFdbNbVPu1brtoWR4/blpta5C19D0/tfZ1v8dGwxGuER4J+G/sLvXL2Li3eKBTJLo7FGr7CS3AkCE16Syot3N5WJbwMF4sKvWcOlYfGAXH8m3qpjMQzhDq8I1ebZPjIu9HMIG9Di22vG4bbpOv9UOq6LUbGOm/gSLqNidl55zOHBlLjJKO4x1jnJnWhgbWrJmTKdQzqU7j4yjlxpjA41Japm2B4yoc1py6pC7cuDw7bbQlbMSssvOvrLp0mpD+cUXPIw6MKMBKgnM/WNBu5wSq++KhKD1nBaT7YSTDnnG2rpTMu+jQDG8mqT03xFhz5ZClVdMWJBMFZRx/flLGXb3arcVOO9bbDFHZ1BW+WHMtV2zYnV72UJS2h9fJQqZYabnWwN1OPg6VjJlrThtr3vM30V3Ep9EwsNjuZuzHX/FZnXEoW5wReEFmKxyGe97ueng7LTeXXLVvjWoNy9wg/0dw4cD1XlzC7E6h86+Y3UDW6uh2R2lN28lVRyPUoNuIiX++rtqhjX6qQeu8t/DjyPBUr1ohiehdkw+53wbYN86VlNbEz8gbl6ywdZiPhdgzZwBWyRHTtgnUnx4sb5DKlGGKhyBQ3diO7ucMjqyVVkqKEOjznqBf15jbB9UzV7X49mBtOIBzC1NlGHW63VjisCO0W1xNM0/u9U7qTAsNrHluxZkC4V4M9jEgknIxpk44CrMvkmZTIo3ak2Z5v5Kqarp4Z7q+2qlb0VVmZYYwgRNSbC0zE8Wqb4b57vveyjR7xvrYXF32ZtZV96WEhpRLbdQ+KdfWzg0MEOhkRqHtlYc87EssVvliuaX8ryYqIo0vqsJxguGkI1NamcdXBZ8m6YPcjLq13jCWqKh2Tl4tB0AiZwf3JTJZ0Rh3DvbzTVua0KzcbNm5G+q7JPrzf50uhM7ieF/bLCNdi0Etx3LRVCgHzjkhI6H6lMgGFOru2udEl32YKNl06Udbx0zXFtwl33/mwMnTp9uyftjQpmw08eXe/X+wWI87ewh2Y9PbnwFlKdleLC789N8jdOozGmthoMHX1amK69fJOZ4fLkEtFtcIFLvftY6e6hY8RF2ByxfO6ajDmCuw1tuN2e1mt1RTtff7gpthigsftxW48dUXX1yCsRZKQkcb3xnVD5USBxYeW7Di+U3dESmSZIxVUkK7BHl/RmyxwJPKars/0bYOqzJbYAD8uCk7a3rqzj4+4ToZrmXaS0u0OKMdKcichR02jRtrdyaS8JiOezpTgILRrdKr7Uy12iNAnaGY5vkeThrQ590YT7U3CyIdl6S0dT6NjFuZXgRoylVAtKbTIpKAP1I0kc+nmkq+Q+iQxU14z0W7Tdv4Jj9I2WGHRjVpub/3dBUMtsRjcNdVN6NW8RkK3XU1ZUdwie6f356XF1Ch1qUmLHg+XuCGDeLlJzwOP4/Hl1jmE2NvU+i7tHeKInDcbH/bo2lOZ+npVfZ6KZCRagzGSIHqtB3VFUmaIlj2bBPVuzHE8sUMfbtvBTU7dyWXdRYvc7ju1cu1p61y8fgsqcb2Xe5umKxXXa53iLFKdtlGg7YelwudLMTCdrCe9uxcRQlfubJgmb5NFXDast2Vyd7HAHW1D3ezOl4QIHZd5l7WYg6DD7UBPUT+h/mWqDE0EIdOmVVguGbei8J5wWkQeWnyHHy7kar0jNjyq2fUiRtcSQW63AZH4BxUlzQrvc+8g+6Iq05djIPq7sl2r02VJrVeMQejKTqd8RzjTDIr4EQtrpwNo0TqPuEuw/e+u4j4rV6AjJzB7KfWL0zbU2RpQrpoSfYd4Obw3FtMUMDjvZj3NGjd+40jyhVEyIuPyI25ZXtMeRtz2qEq9NFlnUDt12IWbc9jw1F2rSfcgECo/kAY32FtqnRATM9GboQ99Bs51uA8nJy470fNitdi5m1swSUK/90U31fQAk7wxydWsNdS4kuWurdoD2wUEspDppD+7cNGj5NliCV4ovGZdH6gpIupm1ASi6fanOLeDlFum4QZrhn1uG8uxYEQeT8gBXsUrlOz5lJJbButZF9uxx9WhEWP26EbHTQ9jnr7ekHgh4/HItkpHcAOlrVGFdMM7VTVJTjn3cKUtA9XflkbMbHKapv/+97cPb/N59evU+b/5+Hk++/t/dgT5PC389mTqceTsWe7nh6zP/10F//HhrXIioN7zCLZO2uB1RPkfDmA//rWnGzOv8fm0d364NjTfjvEbK5j/pOktyty2bqrxa50n7eNA+APwcj3/TUX99XXw/fYwOC2ax713A1/H7F+b/GXi/E2UzU+MPDd6EsyXweuA+sObO4I4Rk79FcWxr15VzGa/npfMJ7nzA5O33/433qiGdEMmAAA= -->
