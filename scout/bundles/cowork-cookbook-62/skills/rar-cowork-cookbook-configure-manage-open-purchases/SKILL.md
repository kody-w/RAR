---
name: "rar-cowork-cookbook-configure-manage-open-purchases"
description: "Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_open_purchases", "rar_sha256": "6513ccf1fe74b5ca8284badd9ca3798f4d9ba8405dcfabe748106d918b557221", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_open_purchases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-open-purchases:26c70d89d02bf9a71418fb2dd45635d8ee435ab82df6790643ce1da1934d4274", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_open_purchases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_open_purchases_agent.py` is
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

Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 6513ccf1fe74b5ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_open_purchases_agent.py` first:

```bash
python3 configure_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_open_purchases_agent.py   # or on stdin
python3 configure_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_open_purchases',
    "version": '2.0.0',
    "display_name": 'Manage open purchases Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e07eb8ed54ccbdff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureManageOpenPurchases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageOpenPurchases'
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
    print(ConfigureManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1pLvV2Fq/rA9VLfYQXXjRjw2IZAALQghuR1lVoHYd5Cfv/s7SFXV3WN77nXERDw52s1yTu75y8xD//Zkt02YV08vT3vfziDJTpIo9CvIzjyIz/u8isFfeeyAP5CbZ00VOW2TV/XT85Pn124VFU2UZ2A7WxRJ5NeQDTltcl8bRJe2sqfXkBva2cWHmhxK7cwGV3nhZ1DRVuBFDTYFVZ4CllCUFW0DiYPrJ1AQJf4z1EdNCHV2EnkPSpNcVZ4kju3GUN0WRV41n4Ew/mCnReLXTy8///L8FIHrp5ffntzErsGjJ/5NGl+9s9cB9807c7A5AdKBVcUITJGB+8KvgrxKwSPPD6C3ux9rPwmeof/6r7i3q0v908uXDHr7fXma/tu1GdSEk5Z23fge5NqF7URJ1IyfITbp7bGGKr9pq2wyUg0smV0+P3Z+pZQX0D+ndz8+mHy++M2PX56AtR6G/PL0E5RXgF/VTtefJyrFjz99TvLer3786SudunWuvttMxIDUn1/f7t/IgoVfl0bBnes/AdWHRx3/y9M3yk2/h9yTnmDn0+drHmU/PggXVd75mZ25/o8//RVZN/TdOInq5t+i+/ODcOjbHtDpTfCfnu9G/gWC3xT6oPnXbAvg1r+jCVj+zu4ZejPUX9G+2/+/kU6iDITyu8X/lNyfbYD/Cf38l7r9TxueoeDLk+AnUQeiw0n8F+i31/1G5H/+wfv68Idffgek/yWZfQ7S4U7hFWRoFPh18/r68w/1/fEPv/z8Q1uAWPPt9LWtkj+j+Wd2vfP5zoJvq378fi/gf8jiLO8z6CPSod/y4j+q3z9D5pT7X5/XL9C3+TL9YGhS4p3pwwTf5EwNZP3Gjj89/Q7wIQPatO79Ncjy//xPSI3cKq/zoIH2bg4wCDi4iVJ/Et4Ioxoy3pL61/1KXq8/p96vEHg6pTuACLtNGkiq7CiBQD5MHp80yAPo1//j3jH0k/uGobN3XPRfH0j4OiHh6wcS/voZMkLANa+iS5TZCbRjNxsIrMuaid89Muo2/dRNLIE40QNydrw8wU3dJv4/oF//BY/XO7nPxTip8CUDPrGBozyo8VOApnYVJSNk34F8bPxPAFgBjnxA7vS/tvg82eUYAgx/WMsF2O0Pvts2PpTkrv1A7/oZOLzOkw5g4mTDOo6SBPKiChgor8YHlrfZy0Ts119/dew6/JI9QBiHHrWlnoEFHwJDnz4VlR8k0SVsvmS+G+bQD7/9/gP0f6H/aded+MRjA4rB3VwgkBNI2esaBLKyTcGyGppCAkDO3Wu//f7wwyRdBoohyKUomIpbM/nmmxCYNHg4590zQOdJRL964/S93aA+BHaBogZYC+R3/fwlm0jkYGnVR7X/bsTH5ofp31394DP5pH6zIfDTvXBOa+/RNznTzSvvMyQH0IelgLpTlZw8GuZ1AwIWhIPnZ+4IdtrNVxdmeQPVIGfqYHyG2hqoOlH+1QGkJ+OkAJjs5ldI5TegxuXJVM6rt5oHdudZNDn+LVYfjwGR6gcQY9w7ic+Q5gNrQoVd2UVYgXC8rwvsR0SA2va+HxC3oczvoamW+5OP7tl8jzz1T5sI/ruWg5u6kD3AmwL60mIISkD/PzuUSWpWknaixBqiAImasTs9QmxqqiaNH30YaBYg0Gw88uVrA/GONe8o/CVLIuCWavzHY2Vwj6rHmgeygez3AHjs7vSn/K7udKMGxMbk7Kq6m+JL9g73z8AuwDP1pAJI4XgChPyD4fT2XVJgkHC6/1r6oUfYTaqDgAZWc5LIhQLf9+5GaMJqyqw3N4BA8acsA6nght9pBQHqIAgAfQgIEYGIBSXhbjoNZAholx5e+FgeTQ0VkMJrXSAtSCH/M3ScIhpEZQ05PuiKpjXACj/cSUGpD2wMRPywcB3axUOYqdF9E9CefJGnduN/64G3lyA6p7oC+H2kHqBqA98DW/bACSCzhodnP+R88xUQNp3S4L7pe3e/6Qp9W5f+MaUfkPEr+IPefCrp3xgHYHaV1veQA8U2rkGCp/5bAIFIuFfvz48C/KjwH7K8/KG7//HvDQD3knr43nMvUNg0Rf0ymz3K3nvV++zm6QzESFT49dcK+OmRaZ+mTPv0kWnfkX1Y6QX6e6J9R+Itpl8g9DPyGZlerSPXn4L27QcswX/iTp+I6e2XbOd/dfFbHEy4BrDWGT/Ky/sSUGMulX+ZFj/KTT1VqR4UxjvK3cvFRxi8JckDaUCdqPNvknfSaXLqw2cfaAxeZRPOe1M/d/GnSSeZxK/9p5esTZLnp8xO/X894Ux4C+IU2GIai0DOgO6oifz73UenNN18P9TdswnAgJe/TEkFahvoap+hjwb1GXofGe4zWNaCmennqTmeWIKl4K+PtR8To+M/gRGtGYtJ7sccNPVkb73yH4WYcglI7PpT9c4/knPi+Aci4OJy8as/EtHvF3byhhB1Y08VERTit7yugZxeO+E58BzIN5BCIDxbsOGPbACfyi9bUIO9Sd2v9vuqVv7Q5fe7GZrHMPnb0ztSTNePhuARNWDDv9uzTRZ9r7WvE1172n3vrO4Gvveir0C5aKqp37y6TA3C6yMGn14AyvjPT5MZqwiUrtt9cH56CAO0+NrFAgoALz7VU48wAykEKIHKXUwaxADrvmEwPY68+/rp4uWvW98/T/wXjHJpxGPmHoI5wdymUQJlAgfzPIKkcNJjfJ/ASdthMC+g6DlCEbjro56NznHCIzCaADJMXkztNxlm6GR/IP2Hkf9uN/702A6qBEZSYD9ForjrBmjg04RDujaDMYRje97ctXF6zgSEN3dshkBIzw1sByxiUITy5ijjkCSNYehE760zeMj0+t58v3vkkf6vAC/TaJIYs22XcYEpvDltU66PI86kNYZ6NO4j5BwPGMYnwP6PrW9emZz2UHsKV9ALgk6sm/j89ublKQQpAqxcErXMPn78bG7aznF2HcIlXCXwcDZo2eh24/6sY4hmLgKZ7vxYaN2K74StsjwpQbxvyhNxVVzkSpuqwgaxCZ+suZKdM7eImjVp5WU0qpJy9uma1kdmc9UOC/EoLOjVdj+aarktdlpypOLkfHaP9io0CSyxR3Tl7g2lYo4JVbT7bumsaXiF0GtVO0XxXrqEuC0uLv2asaPNkbvF3apSj3XIUyulsbP1XDH3xFFP3Ktrd1XiRLvWJVwFTeL8qpBZfUWOYL5bi6hp9LaAYMFmXVNB5hDwDLHdDh/mjKuJ3YIoxFI57vZofKDmauG32lEJVyjfNLt9sU79yM1aqZPqnWb7zWoMDhcUiZOSQa87JIw4Tt5qUuaZfG4sKNe6Lehym1iq2bgG4/QSQRXRZjv0poNum5DklJtf1tEOdhqlouVT1GcSIrV7UU0cxEPTs4Raspwco0OZFmpVYawKO4rmF0c+MpkArxZGGFcbml9oQrltxtZbV3Z7YlgSK4SOPYiIYML47rzFDq0AD+a6mLVHSfCbhUpv0nA3Vsk+Udo1ndjDAt3tjgqf4w2yF6gePsfmpaKEk9PIJbpCY2p/GNCbrShINT+PaIE2B6La91ZCWFka8nzRH2geXSo9TyFWalXXtZatSAIRZM/bdsZmXWXZXHCWTrptyoZglmuuZgS0SCnYJw1JOFWHs1jZJXoOZivPWjSDW9ZJ4FpHjWbN4Ygo9TYJsH6R7sUaXhXZkPQZLDKutS8J5qq6uS3OyOaSySfN0vOFvcpqNetmp8Yz1UovqWa9KTT9qJUeg+9dlOLz2bZw1oYoLUpaUkpDEFEn1ctxfihs/gQba7blYHimzpYkqS1j0bRh1I6j2cyY5fLxxpzVYEjmkWvxYZM7aNH4MXNCZa1epcmerPQeiWuzb1f0ISaKa3Mag4RLKfW8G1ZjCCNDF3DEeqUsXbHMdlFCkWwDCtaFKOW+cbjTKs3d7Jj2R2YlisHakWVS8FR70LkFztKFeNZUE+dLO7Kj/dlIUte2CdfYjRRhuiuq1zv8nEpbn3YkZKejnXiWW6JxrS0982yFOwcxRwsMcnNAkDv6RpjVG8Nxk4XezChxhnm8EMnkMGrFpr6hfUfa6wjFrB7b8WFO9HsbU9JZjusLWVA2ktw1tjRqQRGE2m3GDZbnIKVzUGa+5MolqVlqrm08djE43Urj+m62RpGxFGd1j9a5qTqz2WJjMcdylXu3NSqu4PJYaNk+uxXkkSgYZ+/HTVVZkT9qEYpgnEJIl8OVwdtExsz6oFlH3D9emOPIcUbNxfMrTaRLsk+RtjpwByfeG8yumleUyi1nTH243q67KO8I68YaazM9LCjrtE57OBiGweU5a+OwqB+tjt4p8Rp5uGRX1Zej2dauVpa+dOEYsRIJM/RqzsoLTD5sVkPGtzg3LhtO0khqVoU5ipUkmcNXdXXMs0J2aI8XKT8nb5f1qnAjhQGJjWm9NR+Ec5fE1IG7barewbtNJ8+Z2ZmjC1xkrDhzDW5nFNlJrzFxuQTCWNc8NMg47Ht0QZySvkcEzVplUr5OuEPnyaFBDE169jcroedFd7AzBZM0f7Nk5ieTPfBX1aJpsWBqRO0uTn7WBeTCZ6Z0WY4OupcOenq+2oNH6/qelKv+BvNsE+Fbx1tgMa9duJQ3kvCQKIQuJudi3M6vEmWORMGy7WI34uNSSZTBiAmb6nGHu7bj8aSxmXPjlWpt4fu0oBtsubdJ3j4jCZbhN2Km43PSPxD15YypqHOtyFYnxHxud1dpcfTng65zhqcnRa7MmLMiMfS1lfADopH8skTOc5MJfTMIzCSNnPOpFb3hCK+wq7HW57MDza1lQ2OvocHH/r64lWPIUbXJFwimD4Lj3Cib3EmiJoSeUBYJwZ/4VWKZRowurnF2yze7xVkipSyyC62T1Bi/iolVBMbKwZeJIaFLUybdpQhXNXZCupTZIqp5Iufxvq4PbtxcVSDrQGBNmZKX4FbPl7J506IzaQzDfpYJx9VYwJ1HHZZ85SDNRnL2WbXY4w3fbXSBZXWYwx2bxDNPaenTtrylm+OWIg6n7YVRLFJe13QzQ3TBxE12pCSz2db1wMcrMD1pt+NeOS9Rh5gdrnV9vK6uK9ZW5wu974KMZce5l3N5dcpTtDLtoN8KJVZh+5TXpA1/hfeXoloPO9VCKXROkN4F9ljKcwlJXXcYUh9QbzycXAImDEekeDxtrvaWRK31SaTZY7c4oPjZL/pIX4wBY+nX8oImDbccT9F1uT9tMPEQYflqSFC3N8/dzT2UzjrZz8rVqrTl8KjSPLI1XYDCazxq3TA5UNvq1sOhbbLVnkQEwZwdDdvWUtbptd3RWgVKom2UeQ7Pbw7qpsWox+eTkOmGKMsWD9NWbSjHRkrXCn9FjJZq52pgqivYRwDkOqdi324Wi2KuOiGdn7LDWsq5meOPeigqvoZsuIvaZ8HCD5HBy+cst0NWHW+lK2Vm5CAZ1IW8ulbqYT1fr8htFdAoL+AZ6pp6tExJdhxwg6tEzE8X0UrXjpyz5ObnZD+/yDK/OZhNfq18ZC7PZSXec2auwPQexhZ+EWOwqHM1Sdq5VvNnrUthzb/BzWHfRDZroGdq084ymsbYvtIDLh157+JR6jDn+y7D9EzdkXiqz5MLNQ8spWlVh/Lqwbsq5jLz6MzK2AYhA9a4MLqJxZGUn2JWVPVWE9fXc4Pk5DLtN/E5PmAoHyvEhmAai5QsM9wS8aEUZVgwVYHrVHG7QKMN4p22YYuu2pTSE7XvlG6UV1sKb+pDI9HJtj0g6zL0yuUyDPqSYAmLC8xg3EUqLo5HVShm+o5NZ0pLXM9V2BdLbkR0Px3PV251VC7WXj61Z3fc2Q4Z46WQLveDcVClOElJ4WhsuNNx5spF6IbrwUwqiXSFue5Y632vbBpTP6w1TuUXs7NS3NLW2m0ThLXZcB/vy2G0U7xwyz16wBRHFYlVZ/g6AWpXk/kiUXi5GJ8RzJAqpJkbCWuDdkPDF6MdSnXqVgviqGauHdsYg2U+KzChOtjFIT+4EYOIVIIPCbLLsXBeEhQs61oitXmdrKoER2sEH2OkqNqQzI4MGEqb4CLj474bjrvA9Zpavc0ZtlJaKlf2RrEZVsv4AqLSqcNB5DmdvsSmcN6hZrJyXfXYbdUoGdqMtbZyfpo7laTHO847RRrt1hsqMw/mjL1l5tLJ3FOnrbecbCJ+0oarSI7F9bH0fGbnZr4tY6IwagrG8qHY3uRkh8BrzxQpTyyG3UJmblQorW820/vtVTgNwuZa7wrm6OfDPp3vDKQQIjW2Ok2+Kd5WQ66H0lTBpOeRrJHBem8xCdCnk2Fd62RSlDRPEE+nZkWL+eDat4sabmWzIozVNUVYZWseWljmRI6+Sma25eYq3i/wXA/P9GE38B7s6FKyUC5hEeKkpVJESpDSYtvOF5Y+O0iYuo3C+Cqsq/FGSywLLxepU5wQGd0iZXbse3UuKVx93bJOZuPGrRDWVnm5FNEWk/j+JCh5Xmfsxlgx9BEAEinoMaEx1h5JcTxHQCFdmjqPsBy1Xpk0OfQeijdOzpacD6YHQYO7bKkMsmdeV+SK3NHc/KJV1JLb9mWcbFY6T4N+NhXjQqPXlFAUzMISasSxETjLzztzeSEOFVHyKHzyeSTbBQjVwCKJn5YlrmdS5lZMwIbEyRaauZW1JF4uj2d47W92dKZ0nuZ7K5RuQKGgdTyQPAfTMseCNzW15stF7o2nhjZK0xiKULqeW00rs4sS71bOwdE0tBFnxtazugY57m5GMetD5qaOy/mSW1rD7HZurshOxtoRYzfXSkC6W+7ltKqyiq907ZzZkeoG79x5cQwFVF+idSiEAxIgwjKoR4vZRx1qCUGqYGBsbpeOyMGecDsz1jLz6U73r7d+3Iy4hc84geKO1wI/zmYpDeuJ2Kx9aph3VgNHtsP7I++efXmuh6pRrjY8TiX5JUM3BteYGcPvUFHqDqAp9lVeYk60exkyQmB4HlB3hp0n9KFPnpfDrXPm6rrJdOwsSSlWboGF28scFxNzNR5ukmZ4I9L54om6rfssNePotAt2VqKz9FCbVmds510Pe9uNDZwwa+VLCQIz2NDwkuh0DF6RbEBXg4agUXkRQS5rFhNvHI/dExp2vMAU1a5HkdR3UnsNXBwMhkWObmbHTUvYIprtrQ0ipxexQi6+gSPBMvAQEs4pe7UMmmOLsfXlsqxXBKEmDahc3WZOWiUly8pmPefIW6m7nQvThbFxxUEUMjr1ajhqg1C1eCSSfbKXb6d9Z1joWgexhA2zhVFIqhCy/eyGzA6GK56dMdhYcn4r+h1BZsvlMrZO0m6drBx4PdxO3ijiNEMazq3Ru1ZhEIE7xvuOlxrCjNyZljN+ECwXZ0EZltRFV5Q8dCrXITv5kl82qsMCXykChl54Zy7tT3MUW5A+I5mrsA2Ma0TZcISQu1QMBgmnj+PSa7zISYk9jfkIQsm6W+SblqHOQVee+xll8gCUB28JC+7I4Ci+9G8lKZEZTrNri79elxqO8Jt+zdu9NycNU4MFmiU7f4hNpOkwMG8z7bnEF02m8jwXoE2INim8w7aU1+GhSZZk1QjS3IrIUQKRVxmxZ+kE7a9DsmdIns0vHcVejvNtAyYhjmQZ40qO/jUqJXMMhIHYUUJdwjnZHfFBBZOpy3ozfrHpT6o/d5wu0EkwdNFl1+xod0GTZ3lZwcSZ7hwYXS8bsZJx0hxkvcH3s5ThxsWxOaFG0BGbM+/YBp6SqWPRzWIG7467/ZkJmm3LJDShy+meb1e6C0ote8A2phdVaTcMI2hpMBU5rdH5cALY29gzib4cYzbV93EXkTDcJv72sHcW7ckLe9spZmmDL6JuUdeaxjJc6dTrtTiS116lJK0KWWN7OiKXfnSR5uSf9DA7X1aN4bA8KXQ+Kq0HFBe7cthtDuwe4ZDNAObuEBeMkAD4FLXVNusIUKf0Pdu4stW7K7FRZXcjU9cxy2QQ0RmXnlRm70rLMTtvqcNCd5BDw8GzkVXP5502B51T5Qwa43nRirxxs5hYU4Xmd5kS+m0/S+C0qGeVuEzxuWQqt2upMEHUlgB/s7JuhU2yHAGQZ7M9itnYDcbqBNcp0uWuFx4dNG1W8oisaiLKrdZLQyPDy5ou43W7PkkENmOXa4RY3lKfW0WtgSeDapmMz86WlV6I7KlkWfafT89P94+8Ty8oQpPM89P0feDtlP9vnBJfblHx+kYIp0ny+el/7xjzcaT4/vXvfuTv297LnfvLvy3jL89PlRsBeR7HynXSXt4OLv/bMe2nf3FyPG0eHx+op0+UQ/P+baSxL/dz7Sjz2rqpxtc6T9r7qTawcVtP/zylfn37tPB0Vyktpu8UH/y+Hqs2+WthT3aNsumbm+9FduO/3V7ejv+fn7wROCpy61ecIl/9qph0fPsANR3mTl+gnn7/f5s6Bc10JwAA -->
