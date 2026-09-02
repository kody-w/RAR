---
name: "rar-cowork-cookbook-teams-update-review-access-policies"
description: "Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_review_access_policies", "rar_sha256": "f4f63fdb98a978d32fba2d92a7d9175a8f6bcf1de5fc270af805582391e950f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_review_access_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-review-access-policies:b42559aab8884cd25fed08647742b6fef3ff1199288f8158a2347de3eff21d18", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_review_access_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_review_access_policies_agent.py` is
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

Review access policies Teams Channel Update — Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_review_access_policies_agent.py` and embedded as the fenced Python below (sha256 f4f63fdb98a978d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_review_access_policies_agent.py` first:

```bash
python3 teams_update_review_access_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_review_access_policies_agent.py   # or on stdin
python3 teams_update_review_access_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review access policies Teams Channel Update — Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-review-access-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_review_access_policies',
    "version": '2.0.0',
    "display_name": 'Review access policies Teams Channel Update',
    "description": 'Drafts a Teams channel post on review access policies status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-review-access-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-review-access-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9c27cb19f6b7cd2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-access-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-review-access-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReviewAccessPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReviewAccessPolicies'
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
    print(TeamsUpdateReviewAccessPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZPiSJbnV9HE/FFVQ2SgWyLb2mwlBEhCgEAXqLItSvd9X4ja+u7rAiIza6q6p2ttbZUWETrc3/1+77l7/vpidW1Y1C+fXxTPyqGNlaZR6NWQlbvQshiKOgF/isQGP5BT5G0d2V1b1M3L64vrNU4dlW1U5GA6V1t+20AWpHpW1kBOaOW5l0Jl0bRQkUO110feAFmO4zUNeJtGTuQ1UNNabddAQ9SGgCUU5a1XW04b9R7EuFZ5v1latQv5RQ1VXeQkEBDBCrw3IIB3tbIy9ZqXzz//4/UlAvcvn399cVKrAa9e7nJopWu13unOnLnzlp+swfzUygMwsByBBXLwXHo1YJOBV67nQ8+nHxsv9V+h//qvZLDqoPnp85ccel5fXqZ/py6H2tCD2sJqWs+FHKu07CiN2vENYtLBGhugfNvV+WScBkifB2+Pmd8oFSX09+nbjw8mb4HX/vjlpQAiWJN5v7z8BAH9v7zU3XT/NlEpf/zpLS0Gr/7xp290ms6OPaediAGp396fz0+yYOC3oZF/5/p3QPXhSNv78vKdctP1kHvSE8x8eYuLKP/xQbisi97Lrdzxfvzpn5F1Qs9J0qhp/y26Pz8Ih57lAp2egv/0ejfyP6DZU6GvNP852xK49a9oAoZ/sHuFnob6Z7Tv9v9vpNMoB4H8YfE/JfdnE2Z/h37+p7r9qwmvkP/lhfNSkBq1ZafeZ+jXd0VeLX/+wf328od//AZI/49klKKrnTuF98zKI99r2vf3n39o7q9/+MfPP3QliDWQSO9dnf4ZzT+z653P7yz4HPXj7+cC/lqe5MWQQ18jHfq1KP+j/u0N0q00cr+9bz5D3+fLdM2gSYkPpg8TfJczDZD1Ozv+9PIbgIgcaNM5988gy//zP6Fd5NRFU/gtpDhF10LAwW2UeZPwahg1kPpM6l+UrSBJb5n7CwTeTukOIMLq0hba1FYEYK4uJo9PGhQ+9Mv/cu7Q+cl5Que8ncDovbuj0fsDC98fWPj+gYW/vEFqCDgXdRREuZVCJ0aWIQB1eTvxvEdH02Wf+oktECl6wM5pKUyQ03Sp9zfol3+Dz/ud5Fs5Tqp8yYFvLOAwF2q9rCxqq47SEbImrLLH1vsEMBbgSV2kqW0B8J1+deXbZB8j9PKn1RwA3d7Vc7rWg9LCAbL7EcDlV+D4pkgBhLeTLZskSlPIjWpgqKIe7yUG2PvzROyXX36xrSb8kj/AGIMepaWZgwFfBYY+fSprz0+jIGy/5J4TFtAPv/72A/S/oX8160584iGDunA3GQjoFBKVwx4C2dllYFgDTaEBoOfuvV9/e/hiki4HtRDkVORP1aqd/PNdKEwaPBz04R2g8ySiVz85/d5u0BACu0BRC6wF8rx5/ZJPJAowtB6ixvsw4mPyw/Qf7n7wmXzSPG0I/OTXRXYfe4/CyZlOUbtvkOBDXy0F1AV+vZfmcCrGrld6uevlzghmWu03F+ZFCzUgdxp/fIW6Bqg6Uf7FBqQn42QAoKz2F2i3lEGtK1LwazLQnT2YXeTR5PhnvD5eAyL1DyDG2A8Sb9DeA9aESqu2yrC2Gu8+zrceEQFq3Md8QNyCctAxTGXdm3x0z+p75J3+vJd4NB7LZ+PxqPzQlw6FERz6/92dTGIym81ptWHUFQet9urp8oipqYmaVHz0XaBLuE++J8i3zuEDZD7g90ueRsAP9fi3x0j/HkaPMQ9I62oQIyfmdKc/JXR9pxu1IBgm79b1pJD1Jf/A+VdgDOCKZoIskLPJhADFV4bT1w9JQ5CY0/O3mg894myKfxDBUNnZwGCQ73nuPdjbsJ5S6Wl6EBnelFYg9p3wd1pBgDrwOqA/+SAC/gG14G66PUgJ0Cc94vvr8GjqpIAUbucAaUHOeG+QMYUwCMMGsj3QDk1jgBV+uJOCMg/YGIj41cJNaJUPYabG9imgNfmiyKZo+c4Dz48gHKeCAvh9zTVA1QKxBWw5ACeAVLo+PPtVzqevgLDZFPf3Sb9391NX6PuC9Lcp34CM3xAf9OJTLf/OOACkaxC+E2iAKps0IKMz7xlAIBLuZfvtUXkfpf2rLJ//0M3/+Nca/nst1X7vuc9Q2LZl83k+f9S7j3L35hTZHMRIVHrNo/R9epSkT49E+/RItE8fifY70g9LfYb+mni/I/GM688Q8ga/wdMnKXK8KXCfF7DG8hN7+YRPXydA+ebmZyxMYAYA1h6/1pSPIaCwBLUXTIMfNaaZStMAquEd2u414msoPBNlwptgKohN8V0CTzpNjn347SsEg0/5BO7u1Mw9VjrpJH7jvXzOuzR9fcmtzPu3VjgTzoJwBeaYVkYgdUB31E6fwNPXTml6+P1a7p5UAA3c4vOUW6Cmga72FfraoL5CH0uG+zIs78Ca6eepOZ5YgqHgz9exXxeKtvcCVmntWE6iP9ZBU0/27JX/KMSUUkDiOyJP1eCZoxPHPxABN0Hg1X8kcrjfWOkTKACgT5UQFOBnejdAThe0Tq8QcB5IO5BJACA7MOGPbACf2gMoD5B2Uveb/b6pVTx0+e1uhvaxmPz15QMwpvtHI/AIHDDhr/Rrk1U/6uz7RNuaKNy7qruR7/3oO1Awmurpd5+CqTl4f4Tiy2cAON7ry2RKUKrS6HZfP788BAKafOtkAQUAHZ+aqT+Yg0wClEDVLictEgB73zGYXkfuffx08/nP299/jQGfbRwliIVl2TRN446LEr7nwjSJUxSO2qTv+ZjvI8higdK0TyMEbaEYTrke5vk+irgIDeSYvJlZTznmyOQHoMFXY//fdOUvDxKgcKAECWj4uE9ivmsvaGtB0S6G+raFugvUotwFQhEW7ZO24yOuR/gOSsGWT8MEQaPYAvEWBOxTE71nU/iQ6/2jAf/wzAMN3gGEZtEkNWpZDu1QCO4uKIt0PAy2McdDgM4U5sHEAvNp2sPB/K9Tn96ZnPdQfQpd0A+Cbqyf+Pz69PYUjiQORvJ4IzCPazlf6BZ1oex9aC8o0g+qmKbhRTkmLdK2NJHBXpokAXYsVxvFTtc7zjQUS2xcQz+tLMX2hiO7iDgizFFV7q3jTOKbTDl51FHYwa12HulenOV80xEKI5yquVbq5vkYAQrpRRPbg6inFq2dxfjqpRZR59sr7663UZP6fZ/q8w2e7vrtsktzkSc2F2NI1SW1HWZiI1q9FUWtW1/Ou9DBa92pErh0t/lWGXFmljfJbQ2XagTcpS6RjW5UhHZgK1fmMZLsbuVodrfrTGquZnuWcTW66ZV4XbGbc5CaOtqqZFZLCtkhYUKOicQfSDab6WborKlLVXh0AWOrcpwh3B7blLuFvhsuR7LySqX0JH1UGkPCjE4JrbpCGLoal7h0SGCnVk6djlcGjATRqtWNAo3N0SKGQ71t9/3J2sq50RaIryy2DpmOmeJs26TYxdHt5gpq7h6vdmTpiqXcytmmFZR9nnROpu9W7bV1bdHrHJopJUlykgxFe/yq39LdPpGCuZxuqVVzA9kWiwdj2XeAlrBAyFIr/HAmKe0JqRMdIOlu7WAs7TiNshk0W+wORiNbrTI6YmXRl72WgOBvtlxI6pV3Si/SleauiFJyxmrpnE6YCLNWn1fnOpf3eUUQMCeqztCfZanO+8XS5q3u2GbtsOBrto1Y3cwo1DPjA3+5RcISvpiX0NpcTxgRXt2ySQX67O0pzdS2rNic6nkbVDtQeMNiQVrNdR3L8xVsdGuaR7eSqjbX65bX6DgsL0SYtoJ3nJlYR5FWhOn6+nyZZaNB72S+HppTYxaBcFYCqhojrIz1HHOVFNmDH+kkVjaRmKRCzLg4nYUize3m67nPeh5Dx9gsXGmXGylT3Ir01ZonzfmgMEGBHTqXorMKXax7VkO3Z/2E6slNNLe1bqXGnksjfpEN6HKr7S7X/XjcxPuApY/hMqtFxR24w0LenuOEm7ndjMtkztMbNt5u0dFlEnE7FA1TcNa2iEyugAN61TrxITkFyU1fbolIKsTTemfoiBmH1x3Px507FLFAzp2KNPc1cZ0XkSOPUh7TMSGgNb3zL2O/1MUbcxhNf0cjti0QnFkt+kDANsh6u3EdaU7NY0fZbyLKUoSDHFFu5iv6eV318pVeMpuS8k+tmexNpJJZwFOymLMqNpYW3rzCkjNyG6kYwsO8Z9q50kkOftSVy8heHIfzl8Q+qvXeo2tOLl04wuiC3dlzP7/1sFVJu4tUI+NyprSq3aV4rxotnS1ABjFnXa+uS3OJZLeaT1BzWRlLWGtTgTBdeEzOdb8SWBoTRyaG5b4SLvnurJDNMT11y9yPRK+NtWjNzQkm3KabOD3NL6fkyG+10zFv3aKzVWLG5+ursFYWDYPkQmmiSx27mDGLZtrstHYC/qRl7sFMb7W01Qol6Rb1auvL5ZXQ9mSaDN1mX/fX+QoxKzjBiM7kD7mxQZOsBAWDFuPdZnc+BWaKZHt5dRAOMFj2DypqXT3YLuTj3uPIxWxOaX6woFeu17HXfnA8eZnEJ8k+HAPY4K9BvjlXJTcH73x0HdAZi6MXdLcG/roQAk1YrbAyDyp9PstD2AxF5mbiMSbm2W0/rtRyawrOuPGz+GbfwvUtYD0OZ9x0q7pCys/iY3zSc/osjM2K5ZIkjNSwZdoNerWLFheI2V4eWHmr6ScvTK2QGTV0FIlbRC1xR03WQhTIO1i7WYm5mR+W/WzvzQn7qAVus6CbYHNLHeOKdp18NszR9FZmnp+xGyWDHPaa2ypIPNO6bQzbm6tjGWfna+7UsplgTFB38bFBzdlM2q2jPQbzUiOtTsfwPF7kPomjGUJ3Mj6bK3uBj4601o9hkZjuua8aXBTYY7M8pLv6RAjxoV4uY8SpMvUQyMzNd097c1c0K4w5uWwlpSRTb8REQ/wEEQKYwpM6EbZWWWuCzGhLdchY3iFuqoLuK2+8KInCUyCDVbalz3M102KD8JXCSYe9U2KWFGioGuDxqtJ1UbWvo5u0pNTG0nptnrSrvGFmw8VFDpXtrEtkbVT7ypEMCylJiZ3x+FFLNmaoYF3Y4MPBuyEHnCNvm/N+sTIOly16sXOprFLuiCj4FbPqgtK9jqNn3dVkqP28WMZCqxhrwajxoORPVG2bqqM6F0dQlWp+c/H8MqzKy9Xl1G4uaCfFU09KvvR1uVs3TGSVjKraqLbca4rOMrvV7XoSPTSLLEEFTQ62sCqM3RYqw+5Vw9itjgyzFWHVWQeIe9MUEPKCzQGLjn2VkWYSKCzFmrhKcxxeYkG2S/N8dGvpiF0u6RZZmiPARLIhEc3ebZICXpG0elxfBtpAHfvW9UhkxZJyGjdhiyvOwEdLF7ONqBHFw8IQzcJQAmUuZmI5no/8wMeqJkdJrfUoAOeMB3XvpurSsmFnlEceQkNkFujuFO2E3N9bbErJ6LmhQVzvL0659VeorHaxqEiIpK83IoEG7Q4/ZzSesHOR1AE7Je2ODqygl3YR6VVlCEJ03ERyddLdROECQc6k08Vf3PalSsOidTQv8hnu5xjbJgFNhvUBdoK1imqMwbMEQjYHI2VzLW3OJ81MMvUGz9WFjPUxxTSg0V/i+pVFipRH+MjjLpZ5zHsdx7FMKvWrk2Ea2YPWZj0eUs1r+27vNMubKkYsd2tPZ+8qMBFcHLcrTi1JqkZbLcE3M/iQiM1qRHbpsJaQmXc2t5y7vqQRu+CMAVHVW7rN9yxLprmyai8FIqx53cuXBYGlIyFUOgUjcbY3qFTbnM99qjVIXSPywIXBTlB7IyUqmPOspeXEZbpjuY1arq4W7q53J0KM/EwtU0bxBZAjrLk91uvqxFV9pnqF57hSupfVeVnvhyXdeQqc0vgwZ2GtX2+NyhaKA2O6Fl7j0UzfEepu8Lp1PSbhMB4zKdZOU1j1PtvrzFU/pXDGX8jGTcTIIS+Veup2tX7NERM/hemMreF50ax3aKnOcovOUJc3w0vVbxXCTBZKdc7sg2DLZ13tTRegiItvpSW8mncBdjn4m7N3iC0OtQMWT/FxUetaWoXL8zpseH/WJEV1uKJxXe4PqR7u4l4ETYWGUWnYKpmfUQCbMOO0MR1iA3Iy2YiD5MqBwC89CeaqFC/4akys7cVCOzHSRzhnMEfQOZ8gEIQ3FtbN71teRBnu0Gc9vgXNF5XZcb8qLb7mJKlaO8VMPJ5HvdZYOViT4jUJNuiopIW8FvYzfauGc6PZinixseLVEJ1MMtUPnmEgVCC52+xabQrO0cU+dKrOSGP2CEf7TCbP8sZNHSKkmcRcEWOAtUfTUWpvRmW0JogBVrl5RrS0NYruOjZN8rIT7QqHj4WlBE55VoUzj3TsjalMh0bRXSk03KJayyXtBIctNxspmLZLEaN6y9LWm+XG48PWGStNumUZkaKFtcDIELMuq27FsqBQm2TGIjKDjYvMTIyzW9Sd2mMuezauC9FwYJPZrFEEpusAXo9lfxQSF0QpyhWD7qkB1+jWDiGH5fV4Mw+cTIytWC7mewnhWeQUyAFjhERqLHyHN+HZrZEuq5JV2NWNyFybHZ1Zo2xh0NfcdB4sVzKZDzfCJp1dzNQ4neV55l0RWOzcLl6N1la6IbJ8qKtqnFnHEwNf0sHNqaMO73X0WIKwuNLaYHI9fCQNck2IVOnH9LmHN/iiqxby+YAYdHcxa1NboOHgYJaP1n0vu4OjD4SDr9GMDW10xON+fRIUvr11On+AiTTd4DpnN3h2uMmBdDhJhEHNqLwL+LrZVGBxOxfoYYwiIdZvUSeImk7RKC1hJ04Nbs6mpvP65pw5XwcYtAwj4bCIfW3mH3Y101dWs/MIcWaTGt7s+T1z6qmM8jR74VrLYeaiekvAg57EXspfZ+tDJvUXdMAMnFjnpDRfzIJ+FuRiamxygNPzFYYQikcuKCxHrqFHiYtya5OHYU0z+B5O+YAgxfnyfPKc5U7teEuSyY2qCAKrUzPN0DBQiBz34K3CMlywBLch9kN0OM7F3DkrdAMPPebURF40bJsbZrfgT/hhdTAqVFcP66M7kr2n0cQ1Y5WbgB53TR9QY7xC6FG+DW7Q22F5KCSYp9cDhp6P0kZKzu0Q0Hxuqjod+vRizEjtqgtbV04Eyqdj0g52PAity03wM7Dkl/kiN07zzijmCHKu+nl9njs7TTTh9RlbKQOnGUc5z3GVZxYtMbOx20q9tF4HVpWXaN8sUby5Nr6HLvo9SLWyP3c7TtrMjQOO2l3e+C0dZuhSiRl1gVWezRxzPL+ZCrfaa9RKrbbnTKdWl1yV6NLdE0PAsjNrkHlYjbI20tdkl+dhx85yxttc1NMN17IDvUQbQK1YX1c5nhLR9YpiPBr4e2bQi42Ep1dvvZH96tZj534QmCu3wPnquB1NUraoS4TLQhwEN9YMEout2tG8HPZsuDsOOlLPfG2FIJuboMhzmhZk8aTLYIFmG7DsztwIN3C1Bq0TQm47M2cv7Uoee7O9sRS1PR1WyEjK9HIhrvs+PLQVMvrnQ5dv/I7lIn4NHwB4Ycw1oPgwrMkdI4s3iwudPmj5TrxhzoVemDF2htmUaTYjTpJmnbrwofNd5Nype9klPMRKjE3hYvLa4ZXZahaDXng12ANTeCtjbpFLDG1RcXXcaPGMl0+dy9cmF+OLNbXKzr6+mxfXi5vDGclb9JE71i2V4QZHjZg9V3OmX2OGT7cwQdWZadOXq+BSfb2AKz5lbHSO10fEdw7Y7FzYvUaGV8xdtjw1U5yza3NUvkZ9kKjr+cyJds7YN4bdHZDFstkLhpzwxmpbBGs51s8uZcbzm2Oz1b7kY9HqOq9bMDXZX9nZpizWgVZyZNfHZYk165WJWM6svZKCdBOlTjFm/f5SZ3uiaRmrZ6yVZV+IYbXgOgxn2GoXh9tVZifRrb3FsEDs9r6BCqa77z0kl1AMqw45f4m1QGLQeHbjMc8rVoucw2fbJd5GFq0uiJAI2AvO1CGpifaFIfpTqqbMXAc99SHYDW6aFCs59bBNyTgp5pQWV1IpV5A3jiWwBdG4tOz08nHVRbcm7djF8XbxL8ReRPp9xHfAWOtMJWS9J5aayzm7oXeS7XmfSetWyWe6IB7nWpsdOtRD5wnjzOt04A+MnW+HCXdEzbKkRBDQQ8qffObM61KueYp7refiga99yUGu6PIEd4tVnCI1X8xppsqu+1W5KhmG+fvL68v9UPflMwKTOPL6Mh0NPDf4/+LucHCLyvcnMYzC4deX/3fblo8txI8DwPt2v2e5n+/cP/8lOf/x+lI7EZDpsaUMPBI8Nyv/2/bsp39j13giMD4Op6fTymv7cUTSWsF9XzvK3a5p6/G9KdLuvqsN7N01039Rad6fxwsvd9Wycjqr+F4V8Gi5WZRHgEH93hbvjy3/6f39KDjz3OjbY/A8DXh9cUfgv8hp3jGSePfqclL5eSQ17edOZ1Ivv/0fxpLarHonAAA= -->
