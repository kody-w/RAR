---
name: "rar-cowork-cookbook-configure-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads", "rar_sha256": "31ede094fd178e13f0fe84bac8e5ef061380d0139e27c88808e5b40e1b4f4386", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_review_case_loads_and_rebalance_case_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-review-case-loads-and-rebalance-case-loads:6670296c81fc2033e66484c6c4b56c703fc7a48aad735d5a03ae6bfcfbdae3c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_review_case_loads_and_rebalance_case_loads_agent.py` is
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

Review case loads and rebalance case loads Configuration Bulk Setup — Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 31ede094fd178e13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_review_case_loads_and_rebalance_case_loads_agent.py` first:

```bash
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_review_case_loads_and_rebalance_case_loads_agent.py   # or on stdin
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review case loads and rebalance case loads Configuration Bulk Setup — Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads',
    "version": '2.0.0',
    "display_name": 'Review case loads and rebalance case loads Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to review case loads and rebalance case loads from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-review-case-loads-and-rebalance-case-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6ecb6de7afe720c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-case-loads-and-rebalance-case-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-review-case-loads-and-rebalance-case-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReviewCaseLoadsAndRebalanceCaseLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReviewCaseLoadsAndRebalanceCaseLoads'
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
    print(ConfigureReviewCaseLoadsAndRebalanceCaseLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81aWZejSHb+Kzj90NUmKyV2yDlzjpFACyCQQAihrj5Z7CD2TQja/d8dSMqsKve07Znxg6lTmUBE3P1+9waRvz1ZbRPm1dPrk+ZZGbS0kiQKvQqyMhea511exeBXHtvgP+TkWVNFdtvkVf30/OR6tVNFRRPlGVjOFkUSeTVkQXab3Ob6UdBW1jgMOaGVBR7U5FDlXSKvgxyr9qAkt9z6xqnybCuxMsf7fsCv8hSMQlFWtA3EXx0vgfwo8Z6hLmpC6GIlkXsnfyORJ4ltOTFUt0WRV80LkNC7WmmRePXT6y+/Pj9F4P7p9bcnJ7Fq8Opp/hDRU28yzQFnaWTMZq76Ls/HS0ANvAjAsqIHBsvAc+FVfl6l4JXr+dDj6VPtJf4z9G//FndWFdQ/v37JoMf15Wn8p7YZ1ISjLay68VygcGHZURI1/QvEJp3V18AaTVtloylrYO8seLmv/EYpL6C/jmOf7kxeAq/59OUpByLc7PHl6WcorwC/qh3vX0YqxaefX5K886pPP3+jU7f22XOakRiQ+uXt8fwgCyZ+mxr5N65/BVTvfre9L0/fKTded7lHPcHKp5dzHmWf7oSLKr942WjQTz//GVkn9Jw4iermf0X3lzvh0LNcoNND8J+fb0b+FYIfCn3Q/HO2BXDr36MJmP7O7hl6GOrPaN/s/19IJ1EGsuTd4n+T3N9aAP8V+uVPdfvvFjxD/pcnzkuiC4gOO/Feod/etC0//+Un99vLn379HZD+H8loeVs5NwpvqZVFvlc3b2+//FTfXv/06y8/tQWINc9K39oq+Vs0/5Zdb3x+sOBj1qcf1wL+ehZneZdBH5EO/ZYX/1L9/gIdRjD49r5+hb7Pl/GCoVGJd6Z3E3yXMzWQ9Ts7/vz0OwCMDGjTOrdhkOX/+q/QJnKqvM79BtKcHIAScHATpd4o/D6Mamj/SOqvmriWpJfU/QqBt2O6A4iw2qSBlpUVJRDIh9Hjowa5D339d+eGtJ+dB9JO3tHTe7vj5dsIi283WHwDYPf2gZffDXx9gfYhECWvoiDKrARS2e0WsgIva0YhbuFSt+nnyygHkDG645A6X48YVLeJ9xfo6z/C+O3G46XoR2W/ZMB7FnCpCzVeCoDYqqKkh6xbYegb7zPAZIA4H2g9/miLl9GCRuhlD7s6APa9q+e0zVgMHOsO/PUzCI06Ty4APUdr13GUJJAbVcCUedXfy0CbvY7Evn79alt1+CW7wzUG3WtVPQETPgSGPn8uKs9PoiBsvmSeE+bQT7/9/hP0H9B/t+pGfOSxBXXkZkMQ8gkkaIoMgfxtUzCthsbgAeB08+9vv9+dM0qXgeIKsi7yx2LZjA77LlhGDe4ee3cX0HkU0asenH60G9SFwC5Q1ABrASSon79kI4kcTK26CFTShxHvi++mf/f/nc/ok/phQ+CnW80d597idHSmk1fuC7T2oQ9LAXXHAjt6NMzrBoR24WWulzk9WGk131yY5Q1Ug+yq/f4Zamug6kj5qw1Ij8ZJAYRZzVdoM9+Capgnt/bgUR3B6jyLRsc/Avj+GhCpfgIxNnsn8QLJHrAmVFiVVYTV2DyM83zrHhGgCr6vB8QtKAOtx9gGeKOPbnl/izz1f9+UzH/oa2Zjq6MBuCqgLy06RXDo/10bNOrHLpcqv2T3PAfx8l4178E4tnOjbe4dIGhAINDA3DPrW1Pyjl/vyP4lSyLgwKr/y32mf4u/+5w7WgLwcAH2qDf6IxJUN7pRA6JoDIuqutnnS/ZeQp6BsYAP61EFkOzxCB35B8Nx9F3SEGT0+PytnYDuATqqDkIfKlo7iRzI9zz3ZoQmrMYcfPgGhJQ35iNIGif8QSsIUAfhAuhDQIgIxDYoMzfTySCXQAt298LH9Ghs0oAUbusAaUGyeS+QMcY+iN8asj3QaY1zgBV+upGCUg/YGIj4YeE6tIq7MGOL/RDQGn2Rp1bjfe+BxyCI47FWAX4fSQqoWsD3wJYdcALIwevdsx9yPnwFhE3HhLkt+tHdD12h72vdX8ZEBTJ+qx1gVzC2Cd8ZB6B7ld6jFhTwuAZQkHqPAAKRcOsIXu5F/d41fMjy+od9xae/b+txK9P6j557hcKmKerXyeReSt8r6YuTpxMQI1Hh1d+q6ud7+n0es+zzLcs+A6afP9Lvu4EfeN1N9wr9ffL+QOIR6K8Q8jJ9mY5DUuR4YyQ/LmCe+eeZ+RkfR0do+ub3R3CMsAig2u4/qtP7FFCigsoLxsn3alWPRa4DdfUGkrdq8xEbj8y5YxIoM3X+XUaPOo2evjvyA8zBUDaWCXdsHANv3GMlo/i19/SatUny/JRZqfcP7K1G/AbRDIwz7tBAZoG+rIm829NHjzY+/LjpvOUcAAs3fx1TD9RKQPkZ+miNn6H3zcptO5i1YLf2y9iWjyzBVPDrY+7Hjtb2nsBusemLUZH7DmzsBh9d+h+FGDMOSOx4YzeQf6TwyPEPRMBNEHjVH4kotxsreeBI3VhjhQWF/ZH9NZDTbUfUB64EWQkSDeBnCxb8kQ3gU3llC2q6O6r7zX7f1Mrvuvx+M0Nz38b+9vSOJ+P9vcG4hxFY8E81hqOZ3wv628jMGkne2reb1W+t8RvQOBoL93dDwdiFvN0j9ekVAJT3/DTatopA1RtuG/unu4RAtW9NNaAAoOZzPTYiE5BogBJoD4pRrRjA5HcMxteRe5s/3rz+eSf+d2DGK0lSU5QhHRrxHXSKYR5J4jTukA5uE6RDTTHfoSyctiyXwgiXsKaY5ZG27/i2a3mYQwHBRn+n1kOwCTJ6Cqj04Y7/kx3D050mKEUoQQKiGOK53pTBfRehaA/B/Knv0TgIBNojPH9KIhg9dacIxngo5dA0PQXvbXzqITbu4xhNjvQe7cdd0Lf3vcC77+5w8gZAOY1GNVALEHcoBHcZyiIdD5vamOMhKAIM400JBvNp2sPB+o+lD/+N7r3bYox20JqCxvAy8vntEQ9jBJM4mLnC6zV7v+YT5mBNUMpWQwk+TuHrdYKHLWHk8so/ror9kJtURbDrqWVwWRWFTnBANRFNKoAOvaa1pWmx26nm1zHTYfW0FfNQy/YtzFowZ2wyF3WzE+yfZZ1nNW6OGWfkkMfTqFSXp8Ra+7KezEsjdbo9cpjim0niSHChHZoqxtPUPZqNdHCNBbw9ZkdaLXRDtUzbW1va6pTrqLFJ6FxX425SY6tBb4eurHbeYXHEL9cmP6+vCBFbkW20SSssT+cCoYR00duCKTT+HIkPYR/lDseT/paicR+jSOJylRyfKgfHwPJjNBzm6qnwBbGXCitNhONy4LHCigy0lbpdbZI56uNlJ1yPblQeVmukX6lOn0nDdbbUluxUmCtlXMbtIcov+zlqXlyLEE9lW+lSn3dSUBv7lEucATnKSTnjj24pixosJEJV8TaapkrOHJZDaUy1SUmJG1Tuk0Qo9GKTuiIyw0LvSiTKddEXicL4ksOHp9MlFhJ/PmwOZHnaJkM25RXBsfFoGgQi1VkEwp0sekMVziVTCNts+umBCyaVul23By2Z1zqmIalQ12QTLQ4pEmsc2cGn+BAUJGe6zbpENCTGNf1KDJYgTCvm1OsF0uh4Ne+OCX7MynA+LzqdmiMrsQsbezhICJKkQ0LT1iyetzlWJAlCDXDYnJuBNRC0d7gknrbaBhRtrd9vdj2FmFF+kBJg9qqYyKVYHOKC6uHuImaSyi+qXTL0V8TaiYa4qLAiHVbGZkLv1cJcV1vaUZeX4nzOptomiwqTjJJm4wewxbjGFFvUZS4qBLLhG9KEV0hoJubeW+/aRJhOTctfSg23XPDM+Vw61yHsscA9ncgZlTSceeAIBe1pnmIOKr084+IKXSUiMc2dpJpwZE4shwnjXrqjNJcIW8Saib7cL/dmhAWRnUhlTom7MPLUSLfyBa+7tTyrjeUkQJOMzw1jv/NybcsLLkaxUUoGu/ZoOhtK6VYt7BGluV/oCRWSC43DdgLKnVhvhqz0cNnpkSpfFXImzbjTqWu8ebkLRUNVz4vUmy8759wQlAQyq6TZJiuxxbkS0dk69YJIAWGsTqN+ZiCzNq85DtlXSBXBRKSjw3XbaNO+NVNrN6El0UaS6tQdJtJq4k5TOHa3hGRm+GbDNEzi9qa9oqz8PNVrZSUXPGLoWMbFbrSUHWPpYtaci7vOYMgwh6u8FLaVnhEcJVgng1tJgeLqvaCWpj3IGX3J5CofsB03hTNezSYwJcKqmF/CAURpsCLCPkDcSlKyhX9ZGYnknedlA2+F9cyqySuhLPPFboKEZa/Oy0nuX2Sjqo05gJ09OpO9kKB3R5yOrOMh2rVtJ8iwsCCxUHN0bNKWC1G3nMOB4ZDLjEgP6q6q3KhNOJqNV+JGkjdIO1vAwrXASwPte5anT+fr4tRz7kk74UR2VOq6sDUnyUqlb4l5LG6OXdXu3CW1OwUB7SNbw6pU15lo6r5AI7cW+pafHGeL7dbriB2SHpbh1o0JmEzVM6wOXrng4WMo+nXQTXyJPrbldcOflWtWTKfE0izFDV0RiJJ2/SRfIHi5yuCCW+iFyrTs/OTJ4W6NKNXac/A2zqUYiH9C/Yi0nXmIcTuhPyUYVhF4jK1bcZjN8s6/RvZWTmRccOf27hiw4kmvQlnYlvxGRpcsWmdiwRZOXOB6JpNEaeDDDg+slRdWJpud9boUnFPB+Xwi1/MFTuy66Lij50m4vmSWdao1JQ1ard4obWe6LJ+6Tr9s+LCfE5OzkDpUWFB8asaZK/vCoZ8oQ8K4WShLHeeeZdA4wPt5exUVzZ4i7SGrHe4cWMdjpU3XzsQQNaLFidAlNmvPPJP7+fF6IjPyuKEOBE77gkuoE9EKBqekaRRbSDnvzM6IVvOKdRrEIUrEIqsZRE/ddeBumYvQCMl2tcQ1YS2rxiUQlleAIdUmLfg4gBmhl4T11ER0Wy+8vNO3lqlTes4eTCWXRavfkbm3mpOH5dHrJ+SV0xbHdHXc7VOnqWlC2ba8eHAmwjpUuJjVeNKctntrepAJNVS87ihWiGcHrZwbtG3lcyJuPLWBpwJsKGvW7i4HNG3d03E/QVF+bhHVIWZbbckLzMZqFz012RviFi+ZNjxJZ0XNZ9d1ojkLxajxqlg11NnfZ865drxISqR5THf8zJ+Fq03QxfqKOC/Msuplt3T11Uaal2bqLEFjxTptvo1rSVxej2ox8ZvMWGHTbcJ0QRDVGYehZwERPffAE7jvGJuFvIhVA2vzE9nFHbfsGixKNaSVeVrTO8yZIGXl6PO1sz6BFnFPtlM/mNutp1Nib7V1uc0GPen5K4Gs52WlZWznRG3g1vNjYPaLnuGFtqaNYwFHy4gzkyHnBI6py2JvO1ocHIO9c4qDYWeescmK5DKUkWexu9YwTtvAgr4jEF5ule3B6s2MrTRMxQiRgodmfxVOnH8OLwdeamLSWqzLHl7GcxqJTwUhWNzkkJjZOlpSLb0Yk2SPtZeugptUaUOJnB1DY7LUVwWmxfhi7sy0g7eO2+1im08J+pSsh6GONepa9M7aNu0iReG9e3BUgV9KeR+tybZXdh3vcnJJMttrUtgwryfrhRJipOzDZnIx95XFwAYXZKLTa9K6g22robBjtS8NHpfS45ptGJqe7GWMnHZV3KtmPmu7zTBzGbobEvQUlOehCQIs5aoF46SYORx56hQRy115MUAfHhRR5YKiMp37FWUOS365mEUiaxgTvDM2Yknsz51v7ko97ThbZ1a8dqzoybZc6E4fCrumTqeD3XNtp85bEYDFfFPnJiIujqqbabmJ1WjGL9YuRSKDUXn5+RrLSpQfrbw7ZgGf7IxFh5EGPd3NE5VNzx3p7oODNMd4f+MoxBr3dolrzJA+uCr8TqnYerW2T4Og06iPLC58sW6aZQ7vhk3RrFcXRfT7hd71+xgPK0vN8JxarUvR9UHql5koxOeUWMCL3HSKKvNioZkvs1z3A0xs2TKfkLYUu5bSG6jiKNUpnrM5FWCJMnVzP1i0Basej/amvOyxxVqfpXK1w0xDqLTikgrbwxxR7eK6OvVlw2RYuh0WWj1v9Klp7GBN8bSKvtodetotKRfBuGHVJ/rUcMpDiZHoOWN2mn484uhQtYvtGdsG6wxWL6qh+k7ntJuBQXcTAN+dGAyhfBW3WaCJge2EHR8JoN0TxVlQM2KUSks20tetu8NXdiixgrvx+mmxtSQWtNvp4It7I8SQmXd1XE9FQ5qvOP+IFrKMRFa5jnlOLxuLUemzq5kWz/lXCcWXFK9g4mLWMZKuLkmXFa7qQqA1MVmewWaFtS7nwey4S1KLPDVsdV/Ye3VhrYrrkt3CUe5SSu6RKqmKqbZHyhpfz3zpJMEGwhf72D/O0djJ9oKSRPU6Eahp3jnlMdzMduJBukbiuUVnwfqgK6hWICp+XrrxTmVA0RXV/JCeqOnhylPF3mWstRZK+nxbt6eDtcCLdXZokeURxnQDZffRNYg4+9LtG4VjPXZVn5LTdKXupyfu1O3Wk+C0qM+s2SsL+JzSXtIeTkQMOiBTCgOTnpmxqQ8NK4r1YEg7juCUmthcqtkUnWA5fz6ArRA/11nO8hTdlpqrm1C1nfPFzNOk9CwwzZGTrqZqhMuDcrpSNtPNcnI1UwcrTT1dX6CIvTmFfYztzjUXbVFxo1yLLMGnU+nEeJLWNDbJzuLVbrPSEd9VjQ61leaE7Bi2iHp5uwxgg9QJkiqOGb5epqsAcw+03LpwQ26kpt2r1UW6GIuzO1zJxq5xEp44qXZE5cw24EuNO33Ol8z0xFT76rCcFXx6MSebRZ51ohIsohITh8otLvOQJGV7TacVzPJznBGG0472eTVYglLKT5q1vEzdlVo3nVKEocXN2A5vnXXlLfId43h4w29bpzkfzmdGWSEFy80YsL+Wlr4smvTe6EBuuCnYUbpItKjiGe2GQ6NQ2PWCIOl2diWpyaSShkkwW27abjrJJ5MrO8lUDjtcvPVkVcqXukB3BcpS50O/PpRZTnN7UM0FbyEAht35Wkx2Zq/OOPowHPAM7GGWymq72RG8G3j6kHKmdI6V62k1wy62LA8NppAndB3jVbXBvDJgMDZze/SwXy52bk9fPN3Bh5qO00Udmp49w5BlbF9j4jjRNdjrW1I9an63ZxzYndV4OsBtp5zriU1V+Ry2MrUdNLlQRZzRVWfYEQV2xYJpwcqnRoHb/FwTvDaVm+q4EtALjVSMDWPnKlyJQWxTKsNuDIGH023XKgpVDc0CQ3iNAFuhckaoC229QIAmJ7QpbM+2QKHzj+mGG5aY1uJ9iFGwrMC7/Wqm7IMTSmGyEAl7en/YzrgIREq0ZnjbdJhIzs4rpnHlfRcvZ2hkZhQuXTU0lBzmeB6GlsX82ONNS2Xww5Ktz42ZbJWrv9z7AZI3W74lySEbgu1CvBK0UO2ipYvQCcaQ8up8RXmzDRh9hkryWjrbEiYT/IafnUCr2QXaxkM9NgRZesqQo+mnFOse9GbAYdpXj52RzEHhw5octjGTaqpa3WCgJR6mcXadXZON0CCZLTAwpa1CJ+epypDWk6uUuylwA4G6R5Gq0Yk500jdMYnWC/bwfucb5+wikuGlA0FsY/WJcCSbEQJ1K5NWc7Wt/YwNjoxkurZ7yd1YAe0kfvCs1qJO6uUAwj0854OkE6vD0CpYhHvOdpOyO/3IKPoOjmyWqe2OXVcrmvXONKkYvb+64hw6q0u4XEx21hWWS5deNxN22V6OCBXilwvgxexrsMN1T0x0tC+X1pT4UspWMEVMGgsm2CUTwQKmcwOJXjCN1xmrFBN3uu93x2FOlK6ztzMGpVSKHkp4Eq4Q+EjL9UXwYDICtVGKzhkrXLqFfEaOp5aoJrjTzCvmLC/njO/gIsxS2uUa4otikhibCq99n7oeeXmJyaqi7sjtdop2jcxY1fUoSoMhz62LYy1K27yObY6Cdeys3Ejabr2hNukgD7MpS2xkH6DzyZUvHrKUrgg2vajn2stnSWCr/smnlJW+UbAMh+dzqoks+swwIbEGbp8d5x1uoN2sg88iJ9qEZu/06XYIh1jb5fBBMu1EpWKGp3TnwrYMOnc8n0vci0js/cF1tEjr4avHtYRtyTJsZ1KoFENTUNlpohbxJERczxTPfiZtKmwrSiW2ipJmPxFjPt/mmH9EMpi5Kt6QZkaH07Mm0GaU0lwijt/JshnO1pSv8hJTChJ57sWLvMKVPlxxxCVYrV3Zk/xVVoWscqXoGeY3hb92xY5ln56fbufTT68IMsWo56fxbOJxwvDPfpAOhqh4e1DHKJp5fvq/+w56/yb5fkZ5O3LwLPf1xv31nxP81+enyomAkPfP2nXSBo/Pof/li/Dnf+TL9Uixvx/Nj0eu1+b9WKexgtvH9ihz27qp+rc6T9rbp3bgorYe/4SnfnscgjzdlE+L8UTlQ4jbEQBQp8nfbn/D8b44ysaDRM+NrMZ7PAaP04rnJ7cHzo6c+g0jiTevKkbtHwdo48fj8QTt6ff/BKkTTvHDKAAA -->
