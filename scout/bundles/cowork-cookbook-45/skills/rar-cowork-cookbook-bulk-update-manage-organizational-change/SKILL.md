---
name: "rar-cowork-cookbook-bulk-update-manage-organizational-change"
description: "Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_organizational_change", "rar_sha256": "756f67467d9cba3ba95b6d04fb09e6d5664d32671189a2593ebfd27a6164a48f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_organizational_change`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_organizational_change_agent.py` and in the RCI capsule.

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

Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 756f67467d9cba3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_organizational_change_agent.py` first:

```bash
python3 bulk_update_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_organizational_change_agent.py   # or on stdin
python3 bulk_update_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_organizational_change',
    "version": '2.0.1',
    "display_name": 'Manage organizational change Bulk Field Update',
    "description": 'Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b72ff409516ba61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageOrganizationalChange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOrganizationalChange'
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
    print(BulkUpdateManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOjSLLmv8LL90N3P2WlQFyixsZsAV2IUwIhoa62am4Q93309v++gaTM6no9M296bc1WVVkpIMLD/XP3zz2C+u3FbOogK18+v6iumUJbM47DwC0hM3UgNuuyMgK/ssgCP5CdpXUZWk2dldXL64vjVnYZ5nWYpWA6nedx6FaQCVlNHEFe6MYO1OSOWbuQaZdZVUGJmZq+C2Wlb6bhaE4TzRiyAzMFd0vXzkqngrwyS8DqUJjmTQ3FYVW/Ql1YB5BTDp/KJoXy0m1Dt4Ms18tKFyiVJGH9BvRxezPJY7d6+fzzL68vIfj+8vm3Fzs2K3DrhQFane7qiHc15O+0YO9KACEx+A1G5wNAJQXXuVuCZRJwy3E96Hn1Y+XG3iv0X/8VdWbpVz99/pJCz8+Xl+nPEehZBy5UZ2ZVuw5km7lphXFYD28QHXfmUAF766ZMJ7wqAGrqvz1mfpOU5dDfp2c/PhZ58936xy8vGVDhrvOXl58AkmA9gAn4/jZJyX/86S3OOrf88advcqrGurl2PQkDWr99fV4/xYKB34aG3n3VvwOpD+da7peXPxg3fR56T3aCmS9vtyxMf3wIzsusdVMztd0ff/pnYu3AtaPJqf+W3J8fggPXdIBNT8V/er2D/As0exr0IfOfL5sDt/4VS8Dw9+VeoSdQ/0z2Hf//JjoOU5AK74j/Q3H/aMLs79DP/9S2fzXhFfK+vKzcOGxBdFix+xn67auqrNmff3C+3fzhl9+B6P9RjJo1pX2X8BUkbOi5Vf31688/VPfbP/zy8w9NDmLNNZOvTRn/I5n/CNf7Ot8h+Bz14/dzwfqnNEqzLoU+Ih36Lcv/o/z9DdLNOHS+3a8+Q3/Ml+kzgyYj3hd9QPCHnKmArn/A8aeX3wFPpMCaxr4/Bln+n/8JieFEV5lXQ6qdAQ4CDq7DxJ2U14KwgsDfKbcBDbllFQJgn+NA/E8enjTOPOjX/2Xf6fOT/aTP+cSLXx+M+PVBhV+/p8KvDyr89Q3SgokmQz+cCPJIK8qXaXhaT2sD/qvcsgWsYg21+wnw0afpCyBM6Nd/d4mvd2lv+fDrnejDB1sdWW5iqqqJ3bfJ2nPgpk/bbMDIbu/aDVgozmyglRcCqn0FKFRZ3AKmm5CpojCOIScEXA5qxHCXDdD7PAn79ddfLbMKvqQPakWhR/Go5mDAhzrQp0/APC8O/aD+krp2kEE//Pb7D9D/hv7VrLvwaQ0FUP3TN0DDvSpLEMi1JgHDgNuAowGR3H3z2+9PkIGYFFQ74MnQm6rXNBnEauQ674irO/rTAifeyw0oK1lZA76GQNGBOA/60BcsOj2aGD3Iqhpy3NxNHTe1ByDVBOZ8IJlmNVQBh1Te8Ao1lXtf9VerNO8qJpOP6l8hkVVA/chi8M+k5n0QmJylIYD/Ix4e94GQ8ocKYt5FvEHSFJ1QbpZmHpTmcw3PfPgF1I336UC4CaVu9yWdCqY7QXUPlQc8YBBAxn669NPk83vBBY6t3te+jzGnKqfdq135Ja2eaWCWj7oOVBkgvwmdqTj87RlSVZA1oEWY8AOaTpKeXnCeXrnHoPiveoappkObe6fxKO3Ql2YBIxj0/7kZmRSnt9vjektr6xW0lrSj8QB0aqEm4B9dF+gHIDDvkTzfeoR3hnkn2i9pHILoKIe/PUbe3fAc8yCvpgSoHenjXT6IAQDoJPceolPIleUdjS/pO6O/Amju9AW8BPIZxPsUZu8LTk/fNQ1A0k7X36r7E50pu0EYQnljxSBEPNd1LNOOgFbllGZPT4B4daeU64LQDr6zCgLSQVgA+RBQIgSJA1j/Dp2UATNBht3R/xgeTj0T0MJpbKAt6FHdN+gMMmWKlgo4ADQ+0xiAwg93UVDiAoyBih8IV4GZP5SZ2tqngubkiyyZIuMPHng+/Bbbd10m9YFUE8QRwLKbONdx+4dnP/R8+goom0zZeJ/0vbuftkJ/LD1/+5LedfygeZDk8VS1/wAOBJIrqe6sOnFUBXgmcZ8BBCLhXqDfHjX2UcQ/dPn8p17+x7/W7t+r5ul7z32GgrrOq8/z+aPSvRe6N5AFcxAjYe5W96L36ZF5nx4p9+n7lPv0SLnv5D/g+gz9NR2/E/EM7s8Q8ga/wdMjIbTdKXqfHwAJ+4kxPmHT0y/p0f3m62dATDwbD6DKfhSd9yGg8vil60+DH0WommpXB8rlnXWBN76kH/HwzJaHmaBiVtkfsvhefYF3H877KA7gUVqDtZ2pd/PdaXcTT+pX7svntInj15fUTNx/f1cz1QEQuACTaUsEkgh0RHXo3q8+uqPp4vs93T29AC842ecpy16hqZN9hT6a0lfofZtw33+lDdgn/Tw1xNOSYCj49TH2Y8NouS9ge1YP+aT/Y+8z9WHP/vjPSkzJBTS23am2Zx/ZOq34JyHgi++75Z+FyPkDkSdlVLU5Veqwfk/0CujpgL7nFQIeBAkIcgpEawMm/HkZsE7pFg0oic5k7jf8vpmVPWz5/Q5D/dhA/vbyTh1PHzybRTAc5OinaiqKcxCtYEFw/Ygr8Oz/uo18ygGkB9oXIIjECY8gMYJ0KNsyUcukcItwYMyzYMolHJwgMAddECSCLCkwhUJdy3MWpEkgBGZiSw/Ie0Tp10eVAyJd2HNRClnYDkoscByjEHJhUo6JkabpwMslCZOeA+rCt6kRYMynwQ8DJzQ/OtoJmKfdv71YBAZG7rCKox8fdk7pJrHALKm3ZiXh+Vo656xU31cJfCmI7uLocLolmD09eE6Wshv+7G5B7ClBrQQ3BtVFid0RjLJQPYMM8KHcsF5ulJsMk6whWnVLZe+1HufeODrYjotTgsCFYYTwODeqqrbjiG94aVRW8DAU1DqawWqg9NaV5E5Z6nlzRErlK17kJ/0UHeC2EfohQ4VmtTqHDUKd/EpPBr434rNRXtkrvIndWBX0Oh+4LYI0x41Q5dFZD63+gCClE67DWuM3a0u4Whcb32aUnGrDXE5xYqa0FJ8KFOZ5O0oTRhfeMeei6E6A8NC8XsVawur8yjPD+JaINZcrtuTt1eulUWFhb7k3fe1uhJ2poLaqa/GJYo5y0fAdHxuhAHfVWUDPCRsYgmKr4zrjBT+C+y5LEbVeH3MhOAf2eX88lyFPdI1mic7NuRJWoTmwROGGiev7UsZqv6+ibOxaLld3RgMwiSJsaDOGjvbuQI9bYyDXN9vanSkC77eHi9xzdUazTaW2Sdcl7mLTtclYWxIu9lEkBN5C4zPT3SLnLPGChoMrhkAaQ9FOqER7ux0pAoTPnaXti9W2QsUUcK/M8/pVijxSjs9yYKQn68xW1mq5POQHPV+la80YpLVU7rGYyNDxysue0xEnVBTgMUQoap5pRqmPm2Xf7DDKkLqDX4qjqyHitbO29fGk5mEBx4eFrJBiwd+cqNgN867lE/4sbopDOYY3DA5ZdJPM+CDt434zWy/tVuc4zPSMQyXNhN0aC469S9BBwrtdf92RFkXprCVmQ421uCKbm0pfogdyVNbHNaGjVznRrogMfgbtUu8p77TXnUsrKKdDOhhBDO+VnL5gza7q3I45luS5Mvc05VH+rVTymKIUZXnxiTWP7Fqjz8QUlvtdHXCwkF6dxSVa7vFL7hQrXVrV8dHJrXYtLo2+sKJAX2uMhpUovasZmcz3bOUE+Fh49NW74lEe2PpBT4TyuFbsbYmJ/u58E/lRk+hxE1q+A6trdrtYHi7LDctwF3E5JKW4dPc+Flnj7Hg2Ltoy8BSl3hkHedBhzU+c05KfnWA+XVK+sGyM6GxQPsx5yBLWLGV/JiuJzLqRxSOTtyMPlucL91SW+nA4+byn+wbS1EJjXQ1Pi7ZKfODCDZJpenEsGnm/Xbs6ox6tbSesjXZIrvMQG08VumjD3TzX9nriHS69HpgnXrOHleqLGLeK1VBGZy2LxG3UjP6WQS2gouf1ZsEFy7Y9Yz1eUFJlKprjGHDTUrZ64ueVpPLCiU0KjVsWqn0iGoffLIstXzbJYcAsfWbw9v62sVmaWpGEP+z7HdyURn5q/RzFosvNio3hOqOEU6ytDkPudcdLBiocOdBOuyAAX5PJRpRZV91Y6lrYOmYZnM4WQgUBWzDH5VFfqzhMJPo2XusZjRDagaeOaYyo9g1ZuftrIgSqlS69HjmZ8V6eWUkw5n3QZPEiDeaXHC78niZEQSxOeY6tltfFhros2DNilufUmXVCe1B3LdrWq6WH+lKA2Ia5arQo21fmYtQNVGeW133gX7c7hRH9kJN0XCz7uV4ZfGceZodNQVGHbaQJi2uKLdOG0bTbysClbrVC5lRabgW+aPDNCCjzKjhdvd6R/jkDJiP90crFri1YGpHOdF+lKuavJdVm9yGBs7B20tuiHG/86rKn93F+ZDbV1mAMS+GcSN2knrymaYTjgx1/zsVS5mW0rJb8HsMwDelBhLjdkoWPlguzVjo/2zJGqeslmpeK3Kb4wmnRANHCPVNnoy7LbXODo3hr6ktj5Ef0KnWccMtgRSLmTZeyY0gSY7hY9caJu1JbD23gc4oSmDzzFK9bRvn8woAdMxtkHJ7rrepje4O5VOo6kqZag7AFqwmISVgBT1/Ognfppf0h73YXOqg3BbdZsPBWis97LUL2IrpTAp4hxGADeNoEFrFhYa/7A9myXrnq8pt6K+JTvabngr2AmTaPrwOux5ajpG5dp0VWWyu5DrGFg+KNrqJGc9QlY4Pp/W4ct6TRDzGqDDV3Lgb3aMdBZcrFeJ5h4vq4KQxYJ3OJP6/QDL+5Il71SB/1TJiE7W2JL6gw1koNWZuzlkGEfb2v7JUfHhl9f+L3fJmco7kCz5prwynHrbu31oeNoKOqHrB9HWxUsU/ZAWYzkls2OFtWPhndyCCgd1Vx0IgFFdOtvs4OB4URIt5i41o0YNc15suZzqfGensUaQ2BGdBcSTvVj5fH/IbYgn5oR3u9V6Ohdo7IaiMVB4ah/Cu8b5igWs97jVeHAfQBMeYZ0hAozQlnVGSm6yYvJZInAvzc/sBGhsyRskPhaNKLalxzV7ZbLPc8RgaSYN3aoyom6vaKrZfnfTobJW2/FG0LKayg0jZbZGZv0aqv0KIxzfwaH4SFhR4RPhAuzbGRjgFLYMJZXt3KLdqsbzQo9GG8X6oGJRN2zHGWNpxu/c7Bo4LaU8pKXCEteztEJR3hWLDozD2TR2p9ZPyQPq20G9HzOkofiHYRHTzh5oQklQ3RmPgbWSPnCwavVFsSFikvH1mcVGmO9Jfl1dld1GAs1MUyU00F0F0L495sqFZBrkZ8oK13bqh7urzH5Bsy5JIs92NdKarA40qV35yRSoTMYYul5XnE1djMttqaVVozbPXqwIjxgba5raYtUBQx8j2mUNyR04w+KbBtd2rTHPciq4Y3/pnb2Ygi6ZQinwp7JHaJ7HAqEt70VeTog83fUg8VojDXWjUUCVqgy1jltUuXnyqkLHqlYx1f5LT2GOMlvFJN1rRveSAy5VbJ172J2bF4xPehl4R5QJve6XpgQ/YYZbujIKXUwcJ5TbDOJamevXiT03Md12ZdkGxzXOYlihs2B0vXiri9HEWSvy6CK23NhHTcJ6sNZzR7fj2uUxbblIB3Nd47G84qHBZhsh+vIYes4a5u+K2qXdNA3l0w+aTJzXDS3FThL9xqUW5vVVdpZ123q0EtQUij1353JfjGIZUa3he3FKs2NWtFyuKWdrGe3s7bsmikXbC6CUOuc2e7qYuAWIQpcrThdm1YVwRuarcwsCO6LNzQdOZRGa5wYlBpB1mr+kU+hms4Z0KbbTWMZbo0pPb4kTix+pWVN+urd6ADGb+sfKtZy77HUiYx5ud6g4mL25U48slCrWApxXyRdK5ep0gxPhwbd6nmmV1JVbuXslPNrxu1N/39jL6pygmmsYYVa2bhMPOw0ewRQyhG2BxF93Q2tU2FHQs0KXcsOWyS+IBvxNNoX8s6OOFJUgeMgd2khB0uHreIxTHwD5Wp23pfF/jB2Mhz6rLB8oO1amHystctfBWpWEkMI9IdzmjcZ8FRjBlcHcJDciirlc3ACxKzfFMBndGSqJWS72lrraD6JSYvg9V3LrzIVHErLpVgmze62Mp7MknMoETnxcrJvZDoQpZs1hrOr3h32+428pin1fLouPktDDoKzufRTSrWzTa8wZi7ca/8VdO5ypa6TiqYSOWUnFgdw3Zr6SZrcMcm3ce1JTfIrM0ivozwnBY6ujTJYTyU8i0k5jUIbuZQHLgZZ0YyZrdKsGapHVdIR63fbovbEbS9QVARoO3KUphiTg5MwUKzaRJrF62XBopjCHN1LnCyAtUyblxuZtp5CDY/mtTMVsPtdivI88qxai0nK8Rtu5ma4TuLaP2aRIlLPFekYy3OKnk1kJdm4zKxh9L4RUrIE1NVJNdJyLgZ+EJNSB2ZS7J0MuRkAVvs6C/T2UrwnUSXwVZzbm0qYVc2m6IGWzSDYzYee0wO3nrJabw4Hz0amIaUO9EoiNH0Yj8olITOukqEzwiz2Cgp6vO9QCT1FuyK5okvydbqiB7W1oxs0ECeX7Z+paROfHUde3vlLvlx6Y6XYiAXcrUj5jvOnnvA7EpXBuYGNhnmfOZ6WOFqC4cs03zjoSbbVjks7ok9ybjHFYEeTiDpM4vmZzJvKGWwu2kzv8eSFY0VVHwO1kS3jXda64swtvSX+c3edtpOnO9TL9XsM3G9WI0ejsszjZolh8pBthTo3flYxevxdkrtukTjrQxf/ZM9yNHIlhgDl4OgKenQAbRm8+IS7vDruLKd/nIK+9sqRm3O2+ALBLlwKDFbjg5n8BVjadRK2JH8bLFcMRG9OIfEFjfBLik8B8t6C0p3TKWxV3qzynZATzo2TTfzk5MfNiMDz2YsRuxq0BbIySEkZzFGGqDpYc5dOVbjFqFIYUAXtyZNEJCry5NrY1ZizZUtcdFIRjrQmxkeG61fXLDjZmjocNPY6n6xLtGcYvlzRtqVh6RozDCdQZMCjNqjfWrtoQLlfjkfOAY2RnIMB85mRYSiE/RmyBojd8WcT9mL6+Q9ha36Q7WxGHXGuZda26+o84rBgIPPxkhhu+LAq9dlapFXFVO4m++PsuVHA1Nb8KJbnNgdrjGns0I1h/qiW6dAmCujgK3UZNHlM3Y2M1GDbIUKtEui5Y7pOu2dUTSEtGKSy6gkpkIHp74rWoWb92XU6LOGIwmpTOvyWKPhoQrGeocY3H4O2rUew7Z94ONLb8GNZ8HnxzpD57uBrM7+Eqmx6CDEfiUPmWXKFnNF5aagBhMvF3FBtUfDBC08fO6oTSxQrNUdpODiSwd7vfHcgkVRd7FfH7anGyl7N5GQt+Fu1xMSuheLWXElj2xHKTkFyzXm74KdRSp+tUOR9jwnSDqL07Nn6zBJloTaMeGamTczj1Qz12Ba6xLUo76knMtc9FGvlo4o7uL6TWgRtwLNTj1vu8scrw3yepIw1GaaNjepjmWigOxA40AjmFn0BblEl5sxk4/1aWZM5KSjS9xjKN7DYImG1xEmnJDlWVEorAy3twvRNsoBcb18lkjoJm43VSVJ+lI75c4lHFe44s8ze3vbMRTj1/ujH+eZhVWds2pQTt8grYnurwhVN1S9X+zR03xTRIxhRlf0MLuOiJhWnLLqO28jaZcAFBJZ7Dyajm1O612TTiVMJLiCJCI0wjMmBRufqOvBDm+87G9wRpiLCneZK6B8rJixJdWYI+ORjaPe6OslaRnFq4vqdEiQgbjlHikK7hLFuKpdiKUy22QsR171k5XBkVo1qwt+6bJDkc4FnfVqm6wMY02gu50vw2tMjosFlYlHDl7AHK3V1OJwm2WRUgj0QMHzwNqevNbRqVHhm7Gp07qXL5el68+X11uzsE85TdN/f3l9mQ6on8fMf/m98nTi9//s4PFxRvj++ul+xOyazuf7Wp//umq/vL6UdggUexy2VnHjP48k/9tR66d/9+XFJGV4vLqd3pr19fspfW36039HeglTp6nqcvhaZXFzP/R9BZhW03+KqL4+D7df7kYmeX1/9mEUuDKdJEzD6dXq1zr7+jhvnu6H6fRCyHXCb5f+8yj69cUZgO9Cu/qKEvhXt8wns58vRYC1izf4DXn5/f8A+JMaRv8lAAA= -->
