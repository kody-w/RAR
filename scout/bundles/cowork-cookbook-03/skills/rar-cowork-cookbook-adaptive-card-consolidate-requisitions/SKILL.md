---
name: "rar-cowork-cookbook-adaptive-card-consolidate-requisitions"
description: "Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_consolidate_requisitions", "rar_sha256": "88c1347cd1d0cc467fe355430134edd9840d97f7b8b60aebcbb83b0ed31d7eef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_consolidate_requisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-consolidate-requisitions:5b015b03fca040a9ded63d2dd0ff3248b7f2b44de14dd3c5a7ec8dca95cd7ff8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_consolidate_requisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_consolidate_requisitions_agent.py` is
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

Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 88c1347cd1d0cc46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_consolidate_requisitions_agent.py` first:

```bash
python3 adaptive_card_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_consolidate_requisitions_agent.py   # or on stdin
python3 adaptive_card_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_consolidate_requisitions',
    "version": '2.0.0',
    "display_name": 'Consolidate requisitions Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd39bbfe80f8d0c24',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardConsolidateRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConsolidateRequisitions'
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
    print(AdaptiveCardConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aXOjyJb2X2E8H6p75LIQiM03bsQgNi0gJCQkRFeHiyVZxL4JQb/9399Ekl1V07fv3J6YiFGFbQGZT571OSeT+u3JauogK59en3bAShHJiuMwACVipS7CZW1WRvBPFtnwB3GytC5Du6mzsnp6fnJB5ZRhXodZCqdvysxtHFAhFlKCprLsGCCsa8HHF4BwVukiy526RqrUyqsgq5HMG/CqLA5dqwZwTtGEVTiAVUhVW3VTIV5WIiCxgeuGqY+EKeJaVWBnEKt6hg+sMIZ/4Zg9sJLqBUoErlaSx6B6ev3l1+enEH5/ev3tyYmtCt56epdmEIb7trT23coQI7ZSHw7OO2iWFF7noIRyJPCWCzzkcfVTBWLvGfmP/4haq/Srn1+/pMjj8+Vp+Kc1KVIHAKkzq6qBizhWbtlhHNbdC8LGrdVVUOO6KdPBXhW0auq/3Gd+Q8py5O/Ds5/ui7z4oP7py1MGRbAGYb88/Two/+WpbIbvLwNK/tPPL3HWgvKnn7/hVI19Bk49gEGpX94e1w9YOPDb0NC7rfp3iHr3rg2+PH2n3PC5yz3oCWc+vZyzMP3pDpyX2QWkVuqAn37+M1gnAE4Uh1X9L+H+cgcOgOVCnR6C//x8M/KvyOih0Afmny+bQ7f+FU3g8PflnpGHof4M+2b//wIdhylMhXeL/0O4fzRh9Hfklz/V7Z9NeEa8L088iGF4l0PqvSK/ve02AvfLJ/fbzU+//g6h/1uYXdaUzg3hLbHS0ANV/fb2y6fqdvvTr798anIYazDn3poy/keY/8iut3V+sOBj1E8/zoXr62mUZm2KfEQ68luW/1v5+wtysGDKfrtfvSLf58vwGSGDEu+L3k3wXc5UUNbv7Pjz0++QJlKoTePc8//16d//HVFCp8yqzKuRnZM1NQIdXIcJGITfB2GF7B9J/XW3WsjyS+J+ReDdId0hRVhNXCNSCckJgfkweHzQALLd1/90bnz62Xnw6dh6ENKbAxnp7Ts2fPueDb++IPsALp6VoR+mVoxo7GaDWD5I62HZW4BUTfL5MqwMpQrvzKNxi4F1qiYGf0O+/mtLvd1QX/JuUOhLCj1kQbe5SA2SPCutMow7xBoYy+5q8BmyLWSVMotj23IiZPjV5C+DlY4BSB+2c2BRAVfgNJDj48yB4nshZOhn6H4oAiwN9WDRKgrjGHHDEporK7tb9YFWfx3Avn79akPe/5LeKRlH7lWnGsMBHwIjnz/nJfDi0A/qLylwggz59Nvvn5D/h/yzWTfwYY0NrBA3q8Gwju+FCuZok8BhFTIECCSgmw9/+/3ujkG6FJZJmFmhF4LbZIj2LSAGDe4+encQ1HkQEZSPlX60G9IG0C5IWENrwWyvnr+kA0QGh5ZtWIF3I94n303/7vH7OoNPqocNoZ+8MktuY2+xODjTyUr3BVl4yIeloLrQr/Xg0SCrahi+OUhdkDodnGnV31yYwoJdwQyqvO4ZaSqo6oD81YbQg3ESSFNW/RVRuA2seFkMfw0Gui0PZ2dpODj+EbL32xCk/ARjbPYO8YKsAbQmklullQelVYHbOM+6RwSsdO/zIbiFpKBFhgIPBh/dcvsWedyftRS7e0vxY0fypcHQyRT5P29dBslZSdIEid0LPCKs99rpHmZDyzVofe/SYPtwQ77lzLeW4p193nn5SxqH0DVl97f7SO8WWfcxd65rShg2Gqvd8IccL2+4YQ3jY3B4WQ4xbX1J3wvAM7QN9E41cBlM42gghexjweHpu6QBVHS4/tYMIPfQG1ICBjWSN3YcOogHgHuL/zooh+x6+AIGCxgMDNPBCX7QCoHoMBAgPgKFCGHUwiJxM90aZslg5lvIfwwPhxYrv7vWRWAagRfkOEQ1jMwKsQHsk4Yx0AqfblBIAqCNoYgfFq4CK78LM7TBDwGtwRdZMjj+Ow88HsIIHSoNXO8j/SAqJN8a2rKFToDZdb179kPOh6+gsMmQCrdJP7r7oSvyfaX625CCUMZvdQB27rfI/WYcyNtlUt2oCJbfqIJJnoBHAMFIuNXzl3tJvtf8D1le/9D7//TXtge3Iqv/6LlXJKjrvHodj++F8L0OvjhZMoYxEuag+qiJn4dC9fm7NPv8fZr9gH431ivy1yT8AeIR2q/I5AV9QYdHcuiAIXYfH2gQ7vPs9Hk6PP2SauCbpx/hMFAcpF27+6g070NgufFL4A+D75WnGgpWC2vkjfBuleMjGh65Avk09YcyWWXf5fCg0+Dbu+s+iBk+SgfKd4dGzwfDTigexK/A02vaxPHzU2ol4F/eAQ0MDKMWmmTYPcEMgt1THYLb1UcnNVz8uAG85RYkBTd7HVIMVjvY9T4jHw3sM/K+pbht1dIG7ql+GZrnYUk4FP75GPuxu7TBE9zJ1V0+iH/fJw0926OX/qMQQ2ZBiSGZV4Ms76k6rPgHEPjF90H5RxD19sWKH3wBKX2okbA0P7K8gnK6sK+CTH4Zsg8mFOTJBk744zJwnVvgQsId1P1mv29qZXddfr+Zob5vNn97eueN4fu9RbgHD5zwF5u5wbDvRfhtgLcGkFvLdbPzrWV9gzqGQ7H97pE/dA5v94h8eoXUA56fBmuWIezD+9s2++kuE1TmW7MLESCJfK6G5mEMEwoiwZKeD4pEkAC/W2C4Hbq38cOX1z/tkP85G7wSNjqBP7jnWOgUtRgXuCTuYq6Leh6OTWmb8jB7OnXBZOq6uENYFHBo17EYwnEpz6OhKINPE+shyngyeAMq8WHy/2Hv/nRHgYUEI0gIQ9POBJ9SjjtxUceZkpQHcIKY4ii8C3sFhp6iLkN5lE3bJGoB27FtGrdR4OITlwLAG/AefeNdtLf3Hv3dP3dqgAIlSTgIjlmWQzsUVJyhLNIBOGrjDphgEA8HKMHgHk0DuPbTx9SHjwYX3rUfYhi2jLBhuwzr/Pbw+RCX5BSOnE+rBXv/cGPmYFHHqb2+2kxJev4+ZRZ2cdCS9GQYxyNTqBVpaeZaqs+mvM2NZL5MVot0YvG+6TTXjN+umZAnghTbb5b7xItyLArpY+gfLvJ2LHd0CnXoiPlW45R9fGwOO3Nv+9vyatYrK4mitBTkFsViTE9XXKdeZvtLbDr5aDQ6GEyR65apL/q9fzwsy3minZVR5YluNzL7NAnWdNbWR3npmXVW0/Eq1q/ViZASJab7xFZ1EsWqhVBvFGcWB/XoRE/KttwS84xYpz1NbdIcozeXxkrtCe15BN+JxGWmTkJNmp5K+irFrlyVYtdHJtz4qNy1V31zfF6djJlhxTMW7xLNoVMZvwoTZ2f20p6WhNVZPKwOS8xLl83VUM2QWa3inRn1LSrEpB4dpx22WcLtqoPqbhkdc8cmjitrtyJbrKgTVUsqZt370fiA6WRcRhthvFAXCccaCThfODo8q2a11LeW0+1XI1/gnOm8cTJR8sxkQazXVN8qUVW53dHcbmcl3VRxUOXOipiurwfSsOp8fUXjhd4XQo5Ng12g9hS/B1Wpcu5R2hdBY/sjSSlDCRXtZaNK1abgdyNnWRR0VeTXqhxbUVFRhwJo9Ym/0vx1ssv5o6A4mmhcUZa8pIVxLjfrNCMIlF9qgtAYaxmn8FEgnmtcOATMUYtcsC6rUp54uW0qElq3MF1rIlPOe7xb0ShmhTV9Ufi+CLM9a1VXNxHG6yyrsFXSaf3kQIal5GHXbmGc1TQRZM6rzdBRcmIz213PM7k40T5NMIzR4adrHnDyyO6vHKGM5azV3YpYRIvjthoRPcWai5B0XW1ZTCIsK9NZmrcGpWwwUkjbk8yE6dTatIJujeJT4isbY3yCEYkdnHHPU/OpGjj1hpoIO35J89WRIgJ1F0enjTVKtXnHyNXRWkbecb/PKjcLEl5a7+lKysKt5Al0IhFYNZuvuSIic3Q+X+X01adTANj5AgtwiS/F2amcjGcRu/Jt7SC5uTgXznVah+xUI6UdT7LZUeYCQne6Sk1VR12GJG1eLzPdnht9eemlEl9z5LLjDtq1O2iT7nCW6ZMddVtmmW6O/UTNw2l/ydLC5ls50rKgFS8ne7ymg6a25euOyxlJ1I4rGvdW2HWULhRn5W95qlrsYivC5ufVNZVi33EtDWXbVLT3Ct47YnYaMe6V5yedogmmOHPHGktEey4L9GnNT3CsEfIr8KiG3cPIzipqTKvaMlYOBFlqsmKQdaeNvKKUEtSL11e2xBc7ab45n3twOCdgMlMrX2+CBSF66Fg6nrVKZrW9IhBbHQQEvdsJxJlKjqHT7FthzIRK0ZbXLBjRiRFz4WE3m/cCvuCbw+K4tPdl3DfeXmeqMhT7i8zWpiKOL9ryVPvJen489bkQdzN3Hllh1ZfJ7igUVpIfOhOVwH69X+kuk8ZZMVu65+vYOJghBqM/p8+6ZBXGCWwYcMSOzEJOW6UreukcsgxvGYe9vWSWZm2ZE2oK8Bl6pMHI2bDjI5/ge59YK2q6DpaSI6FuahWsV7KqkmxXeLpYdWmh1FfFDnqjaqXq5HcaMbGJoNJ9PSI2Q3wq0jWk+1wrTpgn0owXEKfpxDFs8RKaXblx2VyYn0RxwR4408lqdLT3VlqFSuUsaOaz0o9mu1O4PpHz+WF/XV44KgmW/e7CGtdcW18XZ/EUWqvUEgyFQntFEpbVblX0/XomCUeLnq7E6ZSS4yu/mx3sCZb62LrksU0Hi1hOpKt4Ch3veuMLzah9fNWS5Uxmdg6396cXd7nUEukyORJYQyzV2cxy1YDY7Mf0cbtZUedCpbaKqOlnEjuMz4A7joC8Jxcppm82lDOb5p7IQ9qYgNF6f4p8UW0XnY7W83SldOhCbg7F0lQKlm5rphQmUxISgDMTB82NTBZOiWZLxrLQljl+nR0WmpDupaAD7MlNA0VRCT+9ZpNFntGuvjj0Vj/tLMHOLiquZqF63SSu0nabSVUedoXZhgSEi9fbJduPxuvr6jBZCYftYQZmtMZW1wZ1qq6uulITCyf1/Lxa895hAmKG9Tl2HY2iMjke0Lqur2w4yinXPwq9JR2OS4oQqYM7zvCgxOg55NhkhWknD12Yu7W4368wsJw3/PgS2FUGBE5ctnvPbLBttTgaFQsFNfdad1Y2qnxJV5PNnIqO6Lpd6kqjBMf5KCd51jNZwo322DHvd9cZyifqmDztiBO5PfkFXZxqYKzEyW6ayi3PWLLYEy1Nrxe6n3hqLJDmSmc1LrLpmcueKyWvElBNrwaAtEIHfMcFxzyaRdnkdMz1Ij1dVifCwS2NXQCuAGPTWzBENRFM25G0Yn1md9QqToPgiuEbyQ8uodMLF9QcbfExZoamH6PieGPV6raR9mcSF88y2pyNKLSK2JJaj1yXESFmZxfPGGGxDVys1A/7np5S4mK/tC1x1VJkqHUeanJ7sCwWLcUeTmZnb609cWjXu76K9tRppxMatZVFH/XzoyxmUcjNBUPTFnU124LgKtA2yzMFwSzGSSDv+M0MH5X6GOP4sePW7jk6NWDRclw1j+2jQpI8cHfG4SDO4gkDdgFF0QQA6GXWdX6usErIX7aid8EEZ66R0yJNnROOJ/M8njgF7kwaorbkyFVzRrZdctqaarIROO586sano68Ju22rLyRqf6nr+XF79s1JQFeHbXLMvFDMRudw4kZ5vSfOMO43Ey/Q3VGnF4SdqHZLbyclJ0Un3RU7kzufAW6zfr4vteNIR8tLvDLXu0Ii3KIu2NHshLGtxo0kfFr7ho4KKDHfr0C1Fbs9s4oOzXy5F8DulJJRUW+XasRubLaKF0wXLwJG4xaz9SUylaYm09mSwMQjyo8McU4qmHNSiYl+UedWFY9acnolJ/xRExpFuRrrrducZC0JAiFYG1HpT49bXw+7wulWoZcrqjbRiYUtUYTG4O0Jdvlz2GGMsrYdz3LdE4p5eoj3o1Tt2JoDlHqu9spBB0Ubya5D9MRVBCv14soLD83j7eU6myxRufHxk+rNU6DyFo8dr5fT9SId5XDVChVq25ZCcuXouNtJ58TTJlGSSmRLas1VHcdbFLrCdj1Y367t7CLUPK9MxMXZiiVhJwMBm/mtdgWZq29ENilNKcREW4O61bYBLbFwWfpAoKNe3sEWN9OqcXBgNhraxnORK8g8ZG083+90NvN3qL7v47XvmstDnR9jYseGnUQGXF7V/NEVCpNdEls0Z/ZdXJS2hW2N0VhAw/mi1KIlHoEpzLnu1KFqHCh0w55tTI3OqaJ2xh4W17yOD1KtnJvxaelxuuVTuXrtdI2S6KXb1zpBCsp8f9Z3rL4K9rRe5OfVeTVhu1m8bigOleeNYgKnTXvG8+UjfykoDPLlejL1LEv3o8JW1PHUjJbY6cg4x+g4arIEL1beRN+OT5Jk9ElMKirPTI5SMkm33nIEd/4yMY2WKRMRV01vt8YR33eNqBmLgg46PlNmZOtK7KVzWLORuZY8XvXMrM5S4pRGEpFUCvcLflH1UsQftBFdeCzgKnJdUx3GrrQ02Cattqkrgt7McnElUIIZp76yFqTzBQiTKitMRmMN+1AlZqOtW9JF5XSuTafWrilkYj0T1rvQUI9gfTY2B2PDRXJmzokdg65Jbb7rV+lOdmSHPzPM7LqRi4tajzErdZnetRfp2JrPGDfCrYbuxpTvlGHn9g52XPumRJJ9wYXbRM7xhJEUfSwNVB4b2kRhMI8lHd+edkRvx/V0XlYA7jOsRcVxS3JxPmybFRFGmuF1YxagedHN7Vk5XxQjbO4bV5e8oodqw9v+BQOqP+LGFBnVAVXtvIJhwJzVUmduq90FjZeU4ZonoJ6VviqodciW+yXtBPZk61JzA5aHcwS8+DLGSQ4n2JpfVZMNtdnQ2mZJScykx+1Lmc96cktx+jRi/GIaUGYmXEKCFDMu0QDmbWMnwvRxZjAL3xf5y8g0NcCyOYo59IzfL68zQlOna79Qt2MxVs5pKRNKURtqR0irmR3bkT3fooAJZuUC91cBlffAQakujqplZTgcl/TchZRgeS+P3jxm5Z3h4roXbaaMpJIU1+SiWEmG2wZ0M+qaguDGSplu0MAvWj3ZoPbCq0rKbhVpy+eWnNlxhl2Eq4V3qN2nljGyDqP1mLxe0TPBGq6hM7508kPAnHOXnmvo3Gy8ylUCccKUV7QVS4GzusZOTtjlYgJjhJoTGssMME/OfTp3+g1B4BzpnZYNy156vTxMhR1MyGbSiuc1Hmoq4XJyuggPoUrF6ahopsYC8Oycqzd4ZlRxHh7irknTZj1TzzyAEbzkW0MGrVhT643qG8JuRJfyEaxG01HLE1OJq7c5ELxNm2XEuJxNGXBpp7ywwX2QszKHB5Rnc/W5a6cLtjVOs7Vfym6C8cF24cWKuKvGNSYUxcWOlsZ0ZHqznb7ABc90m6SOVIqkTKHGEtynlgSqO73KE/bCjhW8jPeodOBOi7InN7REM/HlEqhNaROyhdt1G8vZdhqNLrPZfLw+U9LZtyWJT6/j03l9athcxcYeyjRmiBphddkdWacSfczS6sisxNQiiRJflsnlJJUYI3KoCstgJmsEYLYSLfFTjeB1fqYak4nvElbdudJMZEfBmS4TnbYWujvPcCfqSjJPa4XilVGCb0k8XHikVabYlCG7cXAZa7ZajWgqaw1j0uEtFrJj3JuPc32jska1P4k9LCfFZRxrARWiizW1tJtR09uiAc6Ms8PUFBvPxuM47jdcZveXKW9RcUkuWiNULtxa2e73fuGuwou26Q26mkqiQYXr+XZtgPxA83hwmQTWLFss/WNeTivPo66GsJbqie14ATmd7KmFfak3QF4XGDo+raJlQR+zbQG3NmyAKtQmY6WM1IWTZTYhv8ZVeXvW8SNTOnFsHEcUpl/suesxR66VgtUhcflxsolGbstO1fkV1SfMTnDpiOpnLctRJgfkcisuz3xyFQ9AHzGyFZnoMuGVKmUDOsdsd8VHDRHLW29D+zxsYA5eTQFL9mZ42WczuarmS/t82XGYhKn7nWv3TkClcXu1UPrcYHQAN0s4r0DfcnEH92QWWozjHadvMNnsl3U6uojsXCUJZ9b7c7OrpL6e7Q5SFBI8tz7nO3TTitfJjojnUXq0xiYvEinTWBk1U8nE6k+ECzRyM2aFA10lobzasuzT89Ptve7T6wQlceL5aXgP8DjN/+vHwH4f5m8PPJyaUM9P/3snk/dTwvd3frejfWC5r7fVX/+qqL8+P5VOCMW6Hx9XceM/jiT/yzns53/thHjA6O4vqofXlNf6/cVIbfm3Y+wwdZuqLrs3OL25HWJDwzfV8J9WqrfHC4Wnm4JJPryd+EGhb2endfaWW4Olw3R49wbcEEryuPQfB//PT24HPRg61RtOEm+gzAd1H2+ghhPb4RXU0+//H4b+41uaJwAA -->
