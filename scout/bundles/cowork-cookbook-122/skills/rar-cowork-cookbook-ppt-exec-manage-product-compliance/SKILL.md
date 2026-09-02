---
name: "rar-cowork-cookbook-ppt-exec-manage-product-compliance"
description: "Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_product_compliance", "rar_sha256": "303f7170bf374ac16e46c10fa3bb2efbdf6f42c024979b5da4fa14c98df592eb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_product_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-product-compliance:8a83c0e7575254343d79dfd468096eb5d1c4ed7e911ee446698b4f33793bc1e8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_product_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_product_compliance_agent.py` is
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

Manage product compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 303f7170bf374ac1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_product_compliance_agent.py` first:

```bash
python3 ppt_exec_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_product_compliance_agent.py   # or on stdin
python3 ppt_exec_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_product_compliance',
    "version": '2.0.0',
    "display_name": 'Manage product compliance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage product compliance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e75bbfa794280dab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecManageProductCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProductCompliance'
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
    print(PptExecManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpruX+HWfGj7qLoEYq8TjhhAEgKBFkBocTuqWZJFrGIVePzfbyKpqttje87xjRsxqugqAZlvvuvzPpn0r09WXQVZ8fT6pAMrRUQrjsMAFIiVuoiQtVkRwT9ZZMN/iJOlVRHadZUV5dPzkwtKpwjzKsxSOF0EKSisCpRwKgKuwKmrsAGfC2C5HbLJWlBssjCtEBc4EZKlSGKllg+QvMjc2qmg7CSPQyt1AFJWVlWXz/dboAJIG1YB4gRWUZU3vSorjsLU/5zfBKYZXPQF6gOu1jChfHr9+ZfnpxB+f3r99cmJrRLeetrk1Qxqpd6W3dxXFT4WhdNjK/XhuLyD/kjhdQ4KLysSeMsFHvK4+qEEsfeM/OMfUWsVfvnj65cUeXy+PA0/Wp0iVQCQKrPKCriIY+WWHcZh1b0gXNxaXYkUoKqLFJoCLS2gHS/3md8kZTny0/Dsh/siLz6ofvjylOWDf6Gzvzz9iGQFXK+oh+8vg5T8hx9f4sHJP/z4TU5Z22cAfQuFQa1f3h7XD7Fw4LehoXdb9Sco9R5WG3x5+s644XPXe7ATznx6OUPv/3AXDIPYgHTw4w8//pVYJ4CBj8Oy+rfk/nwXHMDsgTY9FP/x+ebkX5DRw6APmX+9bA7D+ncsgcPfl3tGHo76K9k3//830XGYwhJ49/ifivuzCaOfkJ//0rb/acIz4n15moIY1lph2TF4RX590zcz4edP7rebn375DYr+l2L0rC6cm4Q3WJ2hB8rq7e3nT+Xt9qdffv5U5zDXgJW81UX8ZzL/zK+3dX7nwceoH34/F66/S6M0a1PkI9ORX7P8/xS/vSCmFYfut/vlK/J9vQyfETIY8b7o3QXf1UwJdf3Ojz8+/QYRIoXWQBQYHsMq/4//QNTQKbIy8ypEd7K6QmCAqzABg/JGEJaI8Sjqr/pSUpSXxP2KwLtDuUOIsOq4QsTCCuMB1IaIDxZkHvL1P50bkH52HkA6zvPqbYDItzsIvj1A8O0bCH59QYwALpwVoR+mVoxo3GaDwLEQ8OCSt+Qo6+RzM6wKNQrvqKMJ0oA4ZR2DfyJf//UybzeJL3k3GPIlhZGxYLggwoIkzwqrCOMOsQaksrsKfIYAC9GkyOLYtiCID7/q/GXwzj4A6cNnzgf8AyTOHKi6F0JQfoZhL7O4gcg4eLKMwjhG3LCAbsqK7gbr0Nuvg7CvX7/aVhl8Se9QjCP3NlOO4YAPhZHPn/MCeHHoB9WXFDhBhnz69bdPyH8h/9Osm/BhjQ1sCjePwXSOEVlfrxBYm3UCh5XIkBgQeG6x+/W3eygG7WCDQ2BFhV4IbpOhtG+JMFhwj897cKDNg4qgeKz0e78hbQD9goQV9Bas8vL5SzqIyODQog1L8O7E++S769+jfV9niEn58CGMk1dkyW3sLQeHYDpZ4b4gkod8eAqaC+M6tFEkyMqhGecgdUHqdHCmVX0LIWyqSAkrp/S6Z6QuoamD5K82FD04J4HwZFVfEVXYwE6XxfDX4KDb8nB2loZD4B/per8NhRSfYI7x7yJekBWA3kRyq7DyoLBKcBvnWfeMgB3ufT4UbiEpaJGhp4MhRreavmWe+pc0YvbOQb5nH9OBfXypJyhGIP/LjGXQnhNFbSZyxmyKzFaGdryn2sCzBsvv1AxSBwRSj3vdfKMT78jzjslf0jiE4Sm6f95Herfsuo+541xdwNTROO0mf6jz4iY3rGCODEEviiGvrS/pO/g/Q7fDCJUDjsFSjgZgyD4WHJ6+axrAeh2uvxEB5J5+g/UwsZG8tuPQQTwA3FsNVMHg5vdIwIQBQ7XBknCC31mFQOkwGaD8IQIhdCdsEDfXrWClQJfe0/5jeDjQq3uEoLawlMALsh8yG2ZnidgAcqRhDPTCp5soJAHQx1DFDw+XgZXflRm470NBa4hFlsBk+T4Cj4f+I4/cbyUIpVquVUFftjAIsMKu98h+6PmIFVQ2GcrhNun34X7Yinzfpf45lCHU8VsfgHR9aPDfOQdid5Hcsw623qiEhZ6ARwLBTLj18pd7O773+w9dXv9A+H/4e3uCW4Pd/T5yr0hQVXn5Oh7fm+B7D3yBtTKGORLmoBz64eehAD/fS+zzo8Q+fyux30m+O+oV+Xva/U7EI61fEewFfUGHR0rogCFvHx/oDOEzf/xMDE+/pBr4FuVHKgwQB2HX7j46zfsQ2G78AvjD4HvnKYeG1cIeeQO8W+f4yIRHnUCwSP2hTZbZd/U72DTE9R62D2CGj9IB8t2B4Plg2PzEg/oleHpN6zh+fkqtBPw7m54BfGGyQm8MeyXod0iYqhDcrj7I03Dx+83eraQgFrjZ61BZsNFBovuMfHDWZ+R9F3HbmKU13Eb9PPDlYUk4FP75GPuxk7TBE9y3VV0+aH7fGg007UGf/6jEUFBQYwcMrTz7qNBhxT8IgV98HxR/FLK+fbHiB0xAJB8wG3blR3GXUE8X0qlnBMYOFh2sI5ikNZzwx2XgOgW41LAhu4O53/z3zazsbstvNzdU9/3lr0/vcDF8v7ODe94M29F/n8MNTn3vvW+DaGsQcGNaNx/fGOobtC8ceux3j/yBMLzdE/HpFaINeH4aPFmEkHb3tw31010faMg3bgslQNz4XA6cYQzrCEqCnTwfjIDNzv1ugeF26N7GD19e/4wQ/wsAeGUsBndQQJM0OSEJnMBdmnU9l6AYlKWATbqYQwCXBiyGAUAQFMUyNuHhOM3itoMBBqoxxDKxHmqMsSEK0IAPV/8/0PSnuwTYMyYkBUXgKO7RGI3aHk4TloNRgKAcDPUs3LYnwLNdj/KIiYNOCJZmoc4W4VkY4bCM65HsBNiDvAdNvKv19k7J3+NyR4JBhSQclJ5YlsM4NEa4LG1RDsBRG3cANsFcGgcoyeIewwDomKePqY/YDKG7Wz7kLWSIkJ81wzq/PmI95CJFwJELopS4+0cYs6ZFHyS7uh7YnnK5Vc9kMjB057ROclCt5/N4stFUWqziSr6s2qoK3Gimo4dlyxeits/IiNFkojVYuedAu4hJ3clXm/wqbGyMWxK14nskSSknTZtnMGqk0PDLC96tC7XckfUlUnqVn1a0QitWlzR8X+1X6NpdxvmRnbGRORqni5T1ld22WBWGoMZoi+4o12IWvX0gpwYX77vexmlRrSpbt0eRLQj4LqRPVWJZaCM4kxPp6AcFs7WOi+q5ATYatTbmIVH3885tepK6lqzbKDSlTNwa8+WpLpR9WJlooYDJXjmZiRuiqw4/z3dYulXH10S1k/osHYQEmwU7BsfYLPFqWZ9by5PPVXpVOefT1UnmM4aJjZqe6UHdx72vYNhFl3ZHIp+3y2MH1HJSB2fH4AXSdI+2adKHIzqpQ5JMTquGUWuMklG24sJdf0kjYtw2M0JJbDGeLdLlcZfQsl/SU1K/zGdtNXEw61TXLtPzEhbXunGyDupyTS33Yoe1RbrE3PLi7pOE6AyrXrDcGT9ss/ro2U0S1wm1ElozsC/B2jiPJlwciu3CJi+bfSnaqyU1ktEzQaxXsWdrHMSdxuiEy8wAlCkt0eBcew5TzVbFnE6IAsdPy8pzOGqHq1MUDyc07aPpVSwaJT+7Gz4icY3vS0XpvXjRziW6UtRlifKld8x2ZdFe7QuBSsxW2VywPOXi05mWcHoiZN2J8pYLz9xdrHLnsakmErMSSLNKXvepzFFppK4xQ5zt7SMRMNcR3eSXvrL3ZuKwSWLWx+Cwu5bJUgxlwVSV9aWMV0tI5Dd5Ekt5khyMBc7j0aln6wql0FKSjGuaMtaGiJzjyMwTP5LQsTQLjIvreYbHTqX1WWAX5CoNvKgScWWFdtEkPu2NVZGHGlO5cqidVIPsJMPEqpmaWdelG4+xTTYmOZXLzFYmJE1rDD0mSI5ubM8nNYVouU6EVK5yJoJ+KEVlZvF1LGgrPzzKgMlrDdelTtQKbX5ET+QiMaF0qry2RHIOr2g9mmm+640iVp1gznZESh0/kV3U0XF5jtKBv5g54lZe766JLZNpVBnzQ2ev5g3Dn/la28YNQU9XMM2BSGHMVJaFpiOWyXi/h7HZHwiCn04P4fFUHk1XQ7uNOINRtTipXklOlY7kEUSndVLWpOFwLBukh+gSdaVe6O3Oryg+mWjjbnlQ55t+1GYTgVF6xW5DldwwzG7kyah8INDDdulsmNiV7XVsNobV9DWZGbhg7oXU7USRNGL8rBuraXjYoq4hKEurLyA3NAP5yI9Px1O4LUdnpYv8UxfharM6zbJ9vqAXfRXTM3o+ChJBJzVJOXrdrI+EhEIrvq5YYX5YFKHqY+SM0CqJKwEexqM6qlJ6KrhSlHRL4pyUDdehWLZfH811UR/0aygeDnwugBNrb3zbMlWvr+hsH01otUfZiPYnWISNz+NDvEr9q0AyU3UfOCiznW9pnb3Q8vqYxbRW+8yZdhbxgqWxGN2Q7Rajths5n6JnJ5cUbnI40yuFZ47yNeqWO4aUUCfWzrXsgVXCJrt+spaahbCs6HY+O8hUV9DUOZkZMTM5dTHuNIsC5uppd9HTQ3HRNqYZlyThE60UCxSnJix3ypmE2YWUPVr3Cwf4PSfpkT+z9sW8TKyymuydiJ2J4ZG/VsullF31FZgfK/0gEgy+3kwDLoxsIk7TIJIu2Ik40Nczjhe6EBk5bk9XfDF3+MItijMG9zmXhSaeSIwdewpKb/a2epVk7bJXr/MEb1D00tlTptEL8xSNBd8Wwi0zskbebMMH/ATDN6US8dtA8ptNNDZkbxwqJMOOm/U5XTrBTl2GF8m0q/GSdfUZ70mSuzyJQX9YAXE2a5cnV0nc3ZwQJ6MzFc01CoNIS/FmupmIxdaUyMaKYtVAizYtIknQ82JP1DBDp2U83hx84wxJ1xLCo7lyGZUbVfvM8he4lqC2SYyEcu/4VFokF1FWNv2a3FyzQ7/cmhpaT8e15BjEhD7aYQ3rAA2sYo0TqV2dz6cdSQKfA9vjRK2czlr6O3ayVulAsh2r9gvuashLqsVtM9Ust3HYGWHherKxO7dsXf1gUe2GkIXIWluJ5k50hV2M7Rl+3LLSbKnH9Wg5ZeLjVi2OAWonAsSL5GjZhZfqq2DBRPty0cpqedmk4mKdowrnyRzhRj21m6h8I/Tp2nDpw3bPLJeCJhqSQFWoRfGr3JrxqK16YDHtWywQpuEab1dzHZPWW1ngNTONgnLWTnbVnlEKFYtmQFli27DLT/7iMioPu3p+KjFWtEU80bgs8fVRYWxNlirN3dx2ltsLBD/9IM9SueoxyN78q7I6duc9IU6jcSqnVMz1VDKJz2KwPBQ7NbZrPKZWaqGbGxM9K8eGPZgX9DwjEwIVo0WGLyGt5PMjOLKMqkD6p9jlEs/RbcSKXDk3995xiZqZ5MreZm5OYV+p0cWO0l1Ux48rUoBFsldmUWTNRX3Bx5qynvnzjSsLo8UCN3tqi63CxF8AoxlXU9o+jmmjWM6c86K/7rmj5zMX4rTw9CN+0ZMi5+s2bbIJPfIaDj1wPgTDOFPCabMVjmAP8fqKtvEGlFhdlwddodhdk+Ogl9vDjBoZ08J2KeJ4qpPFTFDPB2pEJz4/22/bnSTSRlkU0WSb+qc+YErzmuwzr59nI2M1cqO8Mq7nolxEYna91KmxNHdeu5l3QNKxYKqXl/WFVnmtb2xsL9Gpp+1JB7WbQJ+vdLAn2Utx2Y54UuRaTRhZOFG1TpzJebdOVPIU2H5CaWrqrJNUKv1rg/EY7evOikMXuDXzFwcl32Qp3s0Sb8Iau4ihBaXjx0qYsklniXm+Xq7YlsD9ChxMvqlD2ToWkwBwSddHSzbkMfUIidfML1Ohnyw3uOdu0Tkr85N1sTgJx6hZbOVcnGM1WWUhfiKMwOymwawvSkyOulRemUJ6PesTN12eTeHQV7LJzwlCx4U9Ponj8WTb+wYb7wNqtpC8arPxO6bZl1tYtkEWVFKcX+SVwxCTRrZOa+8qnHKgktXmoEOKegk1Ed/1vml4jcieLowgu3NOZC+CumgPghbuiIIXdur4zPC8n4bsscvAUj6s9Vl6CS9nUVsBGmgNsaX4ST8uXRHEyqnRz/OxUNAgzQNdXc7tfXlSVVvRJzGnyLtqPWM485TyW86KZWHvE5lfE/vLQbHQghfjbWLtVpSx68juMkmVYp4ZfUXE7XJ2OruxUvM7K5+UAXcmvNWCAxPaz5fxedpApy1KqgcYt8f9UzgiYiDMrHBxEtsedSeCI7O9saVEVJobxU7nduvAKHeXvJd9K5d6PhYrvCaUBZgdgcCk/XTVzseLCRnT5upS0uwhUC9bgzuPlTQJjvhJxD0DDQkV200YrXMLSjkK88bO07Wz4HrSmV9PF+3gtv6FFDZbrD3rZ1YvyWwpLTeKkZOXam8u+VJyfHrKaeUizyTmIHGuQHhrw98vRVu+Zs7FzNxNfbquCwJcBD6eYqi9X6LSikgKq+eWpyjg6nw7DkKKmZ3zuSiMo+3O3+7Ws0lagt34ki01UvMPR5Np+q6S4zPNLNeNu3WromuX6zqRjktxZ2oSszvQu9im0zaQx0G2bnj+emzcyj3zoOqKZoxba5w8Nt4ia/KcqbH1NUFrzGy0yMWDVnWtca00zsJsVXNEO36L7tnSEqlruxcu+nliJ6ylgvy0ktzsAIlpaNPqiL+cpAaLe4Av9HDjgfHOjrCRSwpyop7NVJSJbbPdj+nTdrOfrXZKs53v9+zocNjisUYYLedQi+O2oby1TwpjhUoKLq11L6nMtTLV8O3MDqi6x+eTTaUdwRr2MYhrsIQL40zQ51Q/46Xt2IUKzq16Go/reDGWeDA3g7y9jMYhyQLDBw1PkKx7XK07T+sS6lzMXW7du7w2X1uhScTR3k4S2VtWsVfPilBU+KJnksDBCMgS3VqfX8lgxMsLSMSJbJ3RcsoeNMYhutrbFiRe1nxl7GtYNxmzmC5s3hJIepp5pLP11gC2aV43ZuNtmZUZPQqnK4ZS0pb018X84GxGDM3OW3xy2NkbifDscJotmrjCsfk2P8ieexIj1TI227xuYJNoHBvwfofupdGKd1dgfNlVBm1V175SmMoai2OWIBiNIYr6krG+ePRDQJ9zl11c0cVp5JWsGswn9OFc+cpaEvr4WKtY5fEQdNgMv5D9rhY2stiADZHYTcrYFeMnaAi31EaDZ0Bx/ZReSCf1YCmQ1aboqZElUbrWiUcCV423pcCvdxRopOakeGIuzd01V6ynrigwxFVeSNrWmbR7tNyxNM+cZJwra5tI6XOhblLOWWJniZJpQtOmONukNEptFue1RLM8lU0vkIhXLMPXY4XL/I1gQAQQLHliE8qcu6L7FuOvo8YxLpe43qKSTsasKF9Td0OfD6ZCsrSX1lGIH23NLtONqffqSJ1n1WinWM1ubEtnhtgeipKRij7er7sFNTkf5MKhKebEEtFScvAtm/BCzfYwGafTPSqJ43Tlq/OQOqMjatUodZMoDqBGhJjNYfEs7N3KsSs/pppmWXUnsqjxhD6EPiWCwt1NM6J22yW7MNot6aOcpnmovDUpjZ24Ij/nRtp5nIkaiXEZuQlIVpovJoa31/EYnUk1htezHSMpOo1hM2K0ojr84NEMfjqNe1zzR7Vljt1yxo9HI4/WM3DUGkipFYx2Tq5dx9gYmpNghVZTxGHVmF7LYsHmQKx7auNlTUMctenIZDkakJWnmwJzMkge8q6LxBvkTsN32HHEKWJrnS2N6PZFkxSbDdONUneKoly73AXTg9cTBNxVhzOrqj2VcOWY3FV9W2zjRLUo2Q3cMbZiMCnWsb5dUYtV0XPG9rjQ95KAX0x0qYrTU3yhEmyq5BU1YVgwqckcJUbxMeKPYmTjnpZ2GNeUhDe9bg/zyvDCbaNuVM6e+stI94XJhF/b7Wl3Mr2L4pxXW5VyMC4RvWA72ZMqiKd6Y/UxMY8AMT0r1DzGYzbivfFImI2EDswFYdzbO08KVpsYX4T45Ljvr+VWB+MTVbbE3pfOtWnq4KxrYUeb7s5bcWdzg0cBM6LIZMu0OcasOd/L5AgofUxuj6GRLzKdS20i5BdjTdrvT7I6z+moNLXriMj6ZJ3g15rF04s6qgiWH21DqrdcIeI47qefnp6fbq9xn14xlMImz0/Dsf/j8P7vHf36fZi/PWThNEY+P/3/O5W8nxC+v9q7HeUDy329rf76d9T85fmpcEKo0v24uIxr/3EU+d/OXj//6xPhYX53fxc9vIW8Vu/vPirLvx1Zh6lbl7CvvpVZXN8OrKGz63L4/yjl2+PFwdPNsCQf3kK8G3J/IRH66VuVDeevYTGsFabDizXghlb1fuk/jvfh+A7GLHTKN5wi30CRD4Y+XjENZ7TDO6an3/4vsewMpGwnAAA= -->
