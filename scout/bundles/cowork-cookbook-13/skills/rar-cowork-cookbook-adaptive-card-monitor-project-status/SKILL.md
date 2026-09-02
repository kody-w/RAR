---
name: "rar-cowork-cookbook-adaptive-card-monitor-project-status"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_project_status", "rar_sha256": "45dc6addb2033428583c6fbc49cc036835e2d702b75fb8e6acee03e71ad6b886", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_monitor_project_status_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-monitor-project-status:00b189c61fcd063ad25fe7b8aadd6a1528ba775eda5ead1f88b005ecacd3380e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_monitor_project_status`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_monitor_project_status_agent.py` is
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

Monitor project status Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 45dc6addb2033428…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_project_status_agent.py` first:

```bash
python3 adaptive_card_monitor_project_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_project_status_agent.py   # or on stdin
python3 adaptive_card_monitor_project_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project status Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_project_status',
    "version": '2.0.0',
    "display_name": 'Monitor project status Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-monitor-project-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf473351ed6cc839',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-status'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-monitor-project-status', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardMonitorProjectStatus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorProjectStatus'
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
    print(AdaptiveCardMonitorProjectStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSNLmX2Hz/VDdr7JSHOLKsTFbhBDikJBACKGutiyO4JC4xCFAvf3fN5CUWVXT3bPTa2u2KstMAREe7o+7P+4R1G9PTlNHefn0+mQAJ0NEJ0niCJSIk/kIn7d5eYJ/8pMLfxAvz+oydps6L6un5ycfVF4ZF3WcZ3D6usz9xgMV4iAlaCrHTQDC+Q58fAEI75Q+IhvaCqkyp6iivEbyAEnzLIaykKLMj8Crkap26qZ6/xPAJyB1ge/HWYjEGeI7VeTmUFL1DB84cQL/wjFb4KTVC9QHdE5aJKB6ev3l1+enGH5/ev3tyUucCt56etdlUGV5X3h9X9e4rQcFJE4WwpFFDxHJ4HUBSqhECm/5IEAeVz9VIAmekf/+71PrlGH18+uXDHl8vjwN//QmQ+oIIHXuVDXwEc8pHDdO4rp/QbikdfoKAlQ3ZTZAVUFAs/DlPvObpLxA/jk8++m+yEsI6p++POVQBWeA+8vTz4PlX57KZvj+Mkgpfvr5JclbUP708zc5VePekIXCoNYvb4/rh1g48NvQOLit+k8o9e5YF3x5+s644XPXe7ATznx6OeZx9tNdMHThBWRO5oGffv4rsV4EvFMSV/V/JPeXu+AIOD606aH4z883kH9FRg+DPmT+9bIFdOvfsQQOf1/uGXkA9Veyb/j/i+gkzmAWvCP+p+L+bMLon8gvf2nbv5vwjARfnmYggbFdDln3ivz2ZqwF/pdP/rebn379HYr+P4ox8qb0bhLeUieLA1DVb2+/fKputz/9+sunpoCxBhPurSmTP5P5Z7je1vkBwceon36cC9c3s1OWtxnyEenIb3nxP8rfX5Cdk8T+t/vVK/J9vgyfETIY8b7oHYLvcqaCun6H489Pv0OOyKA1jXd7DLP8v/4LWcZemVd5UCOGlzc1Ah1cxykYlN9GcYVsH0n91VAkVX1J/a8IvDukO6QIp0lqRCwhM71T2mABJLqv/9O7Ueln70GlY+fBRm8epKO3BxG+PWa93Rnw6wuyjeDSeRmHceYkiM6t14gTgqweFr2FR9Wkny/DulCn+M47Oi8NnFM1CfgH8vU/WejtJvOl6AdjvmTQOw50mY/UIC3y0injpEecga3cvgafIc1CRinzJHEd74QMv5riZUDIikD2wM2DtQR0wGtqgCS5B5UPYkjNz9D1VZ7AilAPaFanOEkQPy6hLnnZ34oORPx1EPb161cXEv6X7E7HBHIvNtUYDvhQGPn8uShBkMRhVH/JgBflyKfffv+E/C/k3826CR/WWMPScMMMhnRyr08wP5sUDquQITgg+dz899vvd2cM2mWwOsKsioMY3CZDad+CYbDg7qF390CbBxVB+VjpR9yQNoK4IHEN0YKZXj1/yQYRORxatnEF3kG8T75D/+7v+zqDT6oHhtBPQZmnt7G3OByc6eWl/4JIAfKBFDQX+rUePBrlVQ1DtwCZDzKvhzOd+psLM1inK5g9VdA/I00FTR0kf3Wh6AGcFFKUU39FlvwaVrs8gb8GgG7Lw9kw1gbHPwL2fhsKKT/BGJu+i3hBVgCiiRRO6RRR6VTgNi5w7hEBq9z7fCjcQTLQIkNlB4OPbnl9i7zln3cS98r+L23IlwZHsQny/7lfGbTmRFEXRG4rzBBhtdXte4gNXdZg8b0xg23DTfItX761Eu+s887HX7Ikhm4p+3/cRwa3qLqPuXNcU8KQ0Tn9Jn/I7/ImN65hbAzOLsshnp0v2TvxP0NkoGeqgcNgCp8GQsg/FhyevmsaQUOH629NAHIPuyEdYEAjReMmsYcEAPi32K+jcsishydgoIABXpgKXvSDVQiUDoMAykegEjGMWFgcbtCtYIYMMN/C/WN4PLRWxd2xPgJTCLwg1hDRMCorxAWwPxrGQBQ+3UQhKYAYQxU/EK4ip7grM3S+DwWdwRd56tTgew88HsLoHCoMXO8j9aBUSLs1xLKFToCZ1d09+6Hnw1dQ2XRIg9ukH939sBX5vkL9Y0g/qOO3CgCb9VvcfgMHcnaZVjcagmX3VMEET8EjgGAk3Or4y70U32v9hy6vf2j3f/p7O4JbcTV/9NwrEtV1Ub2Ox/cC+F7/Xrw8HcMYiQtQfdTCz0OJ+vxIss+PJPt8z64fZN+hekX+nn4/iHgE9iuCvaAv6PBIjT0wRO7jA+HgP0/tz5Ph6ZdMB9/8/AiGgdwg4br9R415HwILTViCcBh8rznVUKpaWB1vVHerGR+x8MgUyKRZOBTIKv8ugwebBs/eHfdByfBRNpC9P7R3IRg2P8mgfgWeXrMmSZ6fMicF/9mmZyBeGLAQj2G3BFGHDVMdg9vVR/M0XPy43bulFeQDP38dsgsWOdjoPiMfPesz8r6LuG3NsgZuo34Z+uVhSTgU/vkY+7GXdMET3LnVfTHoft8aDW3ao33+oxJDUkGNIYtXgy7vWTqs+Ach8EsYgvKPQrTbFyd5UAWMt6E0wor8SPAK6unDZgqS+GVIPJhLkCIbOOGPy8B1SnBuYDH2B3O/4ffNrPxuy+83GOr7/vK3p3fKGL7fO4N75MAJf6uDG2B9r7xvg3BnEHHrs24o33rUN2hhPFTY7x6FQ7vwdg/Gp1fIOeD5acCyjGHjfb1tqp/uGkFTvnW3UAJkj8/V0DGMYS5BSbCOF4MZJ8h83y0w3I792/jhy+tftsT/jgZeUdTFGNajsMDzUYpwfJwMAO0yjuP7lIOROOM6NE0C3yFhhcEChnFRlASe4/kEwaAAKjL4M3UeioyxwRPQhA+4/69a9ae7DFg9cJKCQiak71FQJRdHCWKCMyRDeFTgehPW81CCYggS4D6N4i5NBi4DKMcDACUAjTk+5TIMNch7NIp3xd7em/J339wZ4Q3yaBoPauOO4zEejU18lnYoDxCoS3gAwzGfJgBKsgSEAkzg/I+pD/8M7rvbPkQv7BFhh3YZ1vnt4e8hIqkJHLmYVBJ3//BjdufQe8mtuz17pXxudWUlGWyNY6GhhVNrc2GHE/bJP442+AkTJuKobQxedtTaVktRF3PyxOjypN2y8pUDbeb4iVawmqxP0ny6n3bedqyt9UCVuEi8YmZzNIqD6ZwDXVTsVd2ZaYJP9r1XqJOemTe9mfQZTR/8AIfMVuzMeKVp1Vzep55hi9WYJBmAqkW2ApSE9luFsNkLZ41rT5FwyY2vxm50KOVM2XkuLs2N/VnhjMl1vHS83US++NvQybYdCzIaZ7XtDveDil5aJTNiZ2yaHy1F7iVCnQHRxM+Fnh5GlnP0N9VkY60Pprtm5GBKKuWmyI2JabjHUwHoDqdjo5GqIMzTnZQWRiH2DLm6KiSt7mXdKmebCOB22PBtYlkKSrqJx1t4Wi3PmKLuTM2rTS/f7/Tj3kWtuCZbZ1GobHTCG525tvpSBLE9o0DRL5lyJC/ltE30aXkluZza2Op1o5D9xnJY3ItO6LVahyO912npMJc58YKTfar18/aShMTcKuoGO2Xqxoz2q6w/OvGcX9ButVwpVO1VWHSicjedrKOjMonqqdW7x6icUSF6yXjnfFGVs+cqYzyTjg2k/ZNrcUzAMb553mDRbGHi9ITiDtYVW3ddlvaox9BTNI/5hZolJUmPN2mHlyf1UIO1jtnEJbZLa8Rm6YYwsFhdxgul7P2ZLdFjw1U0vK08da2MzstIbMV0uWdT7dhLiq9kF9OkrMa+XBdyBHhy1BZ1wbcZaU4yQdJU3FxW5JbiZ+oYC4JdmOJLJdDj9WlctZVx4TsNy4xlfOAXaLa+MGm8iNEiWRfk8JOpOUXmB8qcj66zuolkRuDHdjueTkccdySYSDDlGRVcZ3MK9CWNg8DeT1E1gYl2YdXlpdG6bZOeMMnS4U5V0edBiTZdUaW6f5C0uMNi0VvbyaxtnVjlDqjRT4LE4TgLpeLNeWF7HnVp5+uRR06Ew1GZBbaWW2x/3DMiNzvpydws8NCsrBWuUfJsOisPkurw002t7KPN9cxMPLmlUvd4zazJQmcOgbai145mYzMpkyVyihrA9oVrPD+qjOGeYIgZlVNllG/MuyzQAzNdtDPhuIGe1y7zMTmKGt9VdJ0pWHHR7SDfBQrejTJpaSrhhndr6Uz18WZCZe6024vHuFrtTu6B3aOz6YiInPl67QUTCVTbHD9Ojbo4LGNPEJREmK8O47ITvSCv0Sk5lnQBrC+XkBFSs9tn5UqouuBMyIvDCG7ptvp4vxf4yzKSbG+0XqxIa7nmmyzhFYw0q8gmheCELfYzR1O5zWYpsJttE5EMb87J2TW1YrsxWmnMGstzq5JxpHWLPUR8x8vTqzSWZqKuWIftpkzG54CfsHWRipf1gq8Lbr4YuwoMvnRJOPb1wJ16fSec6Ka+qrFhmcUkLQ79wVQC42qvcveqqronb53yOHKaXqhX+HWJrw9avsS85sIEFKOdKpHb6+Eh2aWrtQAsDW3ODbqlnM5B6ZJo/fOMqymWngTcyBNqLZn1FbdM/EQWOQX3j1aRr49TbdnoyuIiS3GWL+fkUu3Gu2qj5PZmZJA7F4vUSWyg2BqH9XWZsjGzTfSzPQrICgORbHYY6jrzwHF7V/U5jJvb86UUzBXXk5LdSK/E3LK5XTvBZlzXG2Gk6FYOYjcvCJPl/IWTkdNFpEqjQrTPG36zW8+PxUwVDxMyXfGCtRB3BXkKr6K6ssCC8zwwddq4sJtqMtM7F3Sxm41tT5sw17k3Lsr16pIVOLi44UQiF+HOPG93BBhv+1JervtVX+/wLaNMW0WeXUcXcmIyznLh7j2rDWQ+4if1LgsIGqXW2kK6oLER0D2lMCNz3cc5NwfNWFlVhjA9SpKvHNLoqmvAMecbWCbKdLc5SCLVHanqoNN4zfUUvwsvONdsdhJ7UU7z5REt22N54gyjKC17zS3FWXucLQ72Ng+DxMwPa8dWTACW5lZb09VFW/P5KaKCFfCoK+GNYsMt+IRvFMOZncc8KjeuPipMXqGOebto1HkjY0c/h6Ss2vjKSjzIfN0G1TAirA6SUM78S6EcopPPLByvnWNnjbZ3kY1FGWzvG9gaEZuTw2NjcCyT5LqCvYagCXghxstp4rbmkR51WL/C90Qs86eJdqn2W8U6zWRcOKi2lZy3Mln4TGEV3Ph0xLuGW06z/nSlTTYKtUvoUf2BlsyiPoRNdJXXLCZ7ub/xbLOdr/aXMuJp0jbO9pysd/FEzONAnCjGdn2k4iBPFN0MjdWI6zgdF0V421oeyrF8mozMiI32ihkL16VSqSa1M6p9tvJHbiWFQjjdrYN6fUoZ3Dku6zMv4VoXHvwTdcX1SekWR84kdK2O92d5KrljetmtZgbFj7PaSqX9Qu6iIOkSytpe8f1qbtUzac2KGO7Hld7RJ+co2JuGnufqmaRCnwilE1vziX1gdZvVqGUiXYREsP3oelqyy3y1Y/KQbw64Jc8qXfFyMp/3rXMQynl8snRd1heoaaguZy5yj1yL/WbsNIGxJnMDDbsNWJ+xNRuboabhF71f7decPd3GfM9eNH81bbVifT7HYe80F3nDjtnJyNhdOrw9y7JV2PyEw/GO7hh9oeI4WJVFoC39JCOh11SfFg/NRQ/JzCwuOE1YqSJget5zEY3lZQet3MpmqE6nY3xCuwYunPAF2+6UnT1Nz/YsVtSEAtlOJZYjOzHm+Mpc7NVtmZybw2R23Won2ekiXVgsEiflJiy64zHlLNDYbttoTonq4sUturNll1S3bnk9XE7cS4R1KnoUXZ6yj0XCzfsyMIq5G/Vmtzil8qhQSpPfFtwMb1XZmHpnQ/JN/DSOZ3vVILcHbKQYV4+7SFlfK8HIXtoU2MZHH6Z7vowLTE/pPPVT6IZ9qBEVyWCbsN6KkJAjKZLbZupgYiF0KZYsNpOqzuXYQ2vBSeh92s2vHCweBaNHyWh2RMdFNVuVRsZqu3ioergP9492PFYdo5b7o6ee1KXkBo61DQ5jLVqf5+dVpXvRCPVGM5VhHFjBulTsru6KcfndRgd51lwPpr5f6qajFeTc6oFflrOzqAr0aLfWa5GtGeZ0DYilwPCTlbk197Efm3bEs5OjOZ9FqkDpmMGYfASVVuykXhhoj9YecWinKD/fX3XXI6X9VTmKVxzWMWyx7T3PdI55kcsVmK+UTZ9y6nS30oTRFDMTCz9QVpJruqQ2cyXt8ZW20QtTSpMZOGGqZp7r4nzoAsjGQPb4SNwQjkG3O7EsSmmjNour0e5WF3tkNHZLk/qyI7UTDpOFMTSaJVYjWY+nzWksytG6jjYRoe2CLIetobbaSVMunq8jq0yX52UJwRaFnoQI1kDqMnImBuv5aNbYM7EcO319oneRX5dGbOWVTIyj1EsP0wBHz7sDpTQukLR0F63ZUNr52jkoWntG+BNwsOA2JVOmNBrk4iZ18S0hi1t97rmrhTzBZD92e1HSqnahTnGbv0ptl0hVOcvduRWmvOAe+iJwrmUdHJ2OP9Oaw013ixavGAWVrjkN65LHFakh8PR8PhKvWbvUMtPe4LplAIpDtw7oJlu8j4oFKU79aNeTZ1LYL65zdHlZbGqURcVtXVwpMToJG4NYJAArzPHUUwyPO/uXbuOhKq1D/9qld/ZmPnWsR8lEPaL+5cyk+MWpfcKViNbZsxNPuFgXD9A0xzRRX9MJrs2iAw4VOKtRKxXnfbMXPXSSmDiksa3Ve3M0aF3vaLcdHdNZHe7TymqOKWyu2M7GBR0UVsJ520kWTy7Mai+wh5lv44GwA+6WWRJNdabRmJv6E4u8BGajBzjbW1hiTddoM6pnnIc3xzq0idE2qUu3qlx+g/v4rqYwbpdEo2aTwz0WGdPYqJpSqzW/HtO+HzCcpiSWmLDZeCTtJ5QFcJbOMhzb4JTsE7J7Vi47lGNWgrFtl+z80qnSReVXxmjmKONKzsylMVOP5MpjzpvQnrhAESIyHIVeePRSZrOQ9qcrLvfYvEp3OJ3Y1XgerprzdUXkzppvp5jntrslDA9CdVhSv56lVgEH0ZCTHTMD5iS5qFHPLDwVZ87XhmM16LAVuzP5UY/De5vRzD3sfT8K+rr3q+roCIa73tjXII8oulotuGthqyc7zZt0oY+u3Smgk/OaPewoeUxhY2I25/f1bMduDCs04j4isdG8a1cuCFKf6QR8tSfwcH4U9FFbl8oBh8EJiJR0sQ1REs40uQbnxTJY0fJ4QQeSXIenvBXGPnWy2oM8antsz+E8ppFzanGSGi/W9rnq1QFWoPF02tv2aC835MwXzkHvNXuzutbSlDm46+Oiyy3uoFL8ag1aT+RBR9ONJ/skni2IcD3n2101VydRB7C1sMbs5SIjJk50XtCbhRkmhXv2yzq0OtL2BN5WK+648V2QprNoIwXJcm5U4xoXzueLe5LVyegQTA1TJoS1jTVpHWk0RR+EGk+JkJZJ1PSu2ox0JTdZEm6yJSizt6XySq0ZnmGTyyXSmtIlVYdw6zZR883kNLpMp4vx9kiLx9AVxVnWje3jym64QoPNMMpWZIzu4+qijzivmoe4o9fHoppne4osCblML25TpuycRzU/7XNVJwG7ERlxNtHJmTmbanusDHfkATpdnM65UXRkihT2o5LpL3LCO/UlVWT1vJwJo4TYUETMAcG/1DgfBoHFHsa4y+ZJtgvEGqfLjNpeW7ebHOiL2mHnRc3T4rrSuoTMWZdZ2SN2fV7sfTTGg8BbxHQpAbx3MnochJdxB/RjbLI94R3qwPCvnH0k50TEp9L02O2s0iDsYOKKG3B0IqYTyzItL0tltKLaddutmJ6JgznBjDSNDXNI0C5NaAsjAgfVZ2QCP9QifnKdfcBuI8yQzcpjZlp0dZiNgIo8mvCzFbYhe7KlBD91ytI10YYiSve6ox26PDYdLnUS32L5uIpYIjtPF4d2pMVho9jpRbgAG9icpcI9BuTuouI8Iu/zPrucXTNbwS7CS4STuE4M3CGXIFnrFpaprbr222y+b/19E+AbecyS0naiKsxuotKg1uNYQJu9F6jBIXKJlJ0qNHtUrmy0DLeLMZ9nvniKkxo/T05Mwq+sMTDcLVsmYDbjM6udMFM8zKbMxdon01jWTmkk8f7lKAgBK0QHHYKbZrALdbY+S28X0g7Tjx69cC+eFpXsFDWJSSePlQ3HPT0/3V7mPr1iKIUTz0/DK4DHQf7fPQQOr3Hx9pBG0Dj6/PT/7mzyfk74/qrvdqwPHP/1tvrr31P01+en0ouhUvej4yppwseR5L+cwn7+T06HBwn9/b308Gayq9/fhtROeDvAjjO/qeqyf6vypLkdX0PIm2r4/ynV2+NFwtPNuLQY3kr8YMzTx7n3W50Po4N4GBNnwys34MdODR6X4ePQ//nJ76H/Yq96IyjyDZTFYPDj1dNwZju8e3r6/X8Dk7UQdYQnAAA= -->
