---
name: "rar-cowork-cookbook-bulk-update-create-solution-blueprint"
description: "Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_solution_blueprint", "rar_sha256": "076af6ba95ef7515cdbe368e7fe6b125c105ff1e1748263aa9ee91c863f7ed9c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_create_solution_blueprint_agent.py` and in the RCI capsule.

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

Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 076af6ba95ef7515…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_solution_blueprint_agent.py` first:

```bash
python3 bulk_update_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_solution_blueprint_agent.py   # or on stdin
python3 bulk_update_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Bulk Field Update — Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_solution_blueprint',
    "version": '2.0.1',
    "display_name": 'Create solution blueprint Bulk Field Update',
    "description": 'Applies a bulk field update across create solution blueprint records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b2fb15dd02960',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCreateSolutionBlueprint(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateSolutionBlueprint'
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
    print(BulkUpdateCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+bObyLLmv8Kc94PdT/YBBAjhGzdiWLUgISQEEmp32CzFvm8S9PT/PoWkc9z9+vab2xMTMbKPLaAqK/PLzC+zivPri9U2QV69fHnRgJUhCytJwgBUiJW5CJ9f8yqG/+WxDX8QJ8+aKrTbJq/ql08vLqidKiyaMM/gdLYokhDUiIXYbRIjXggSF2kL12oAYjlVXteIU4Hxqs6TdpyE2EkLiirMGqQCTl65NeJVeQqXRsKsaBskCevmE3INmwBxq/5z1WZIUYEuBFfEBl5eAahRmobNK1QG3Ky0SED98uXnXz69hPD7y5dfX5zEquGtFw6qpN914e86aE8VuDcNoITEynw4tOghHhm8LkAF10jhLRd4yPPqYw0S7xPyn/8ZX63Kr3/68jVDnp+vL+OfA1SyCQDS5FbdABdxrMKywyRs+leETa5WX0Njm7bKRqRqCGfmvz5m/pCUF8g/x2cfH4u8+qD5+PUlhypYo9JfX35C8gquBwGB319HKcXHn16T/Aqqjz/9kFO3dgScZhQGtX799rx+ioUDfwwNvfuq/4RSH261wdeX3xk3fh56j3bCmS+vUR5mHx+CiyrvQGZlDvj401+JdQLgxKNH/y25Pz8EB8ByoU1PxX/6dAf5F2TyNOhd5l8vW0C3/h1L4PC35T4hT6D+SvYd//8iOgkzmARviP9Lcf9qwuSfyM9/adt/N+ET4n19EUASdjA67AR8QX79pqki//MH98fND7/8BkX/H8VoeVs5dwnfUisLPVA33779/KG+3/7wy88f2gLGGrDSb22V/CuZ/wrX+zp/QPA56uMf58L19SzO8muGvEc68mte/I/qt1fEsJLQ/XG//oL8Pl/GzwQZjXhb9AHB73Kmhrr+DsefXn6DJJFBa1rn/hhm+X/8B7INR6LKvQbRnBwSEHRwE6ZgVP4YhDUC/465DTkIVHUIgX2Og/E/enjUOPeQ7//TuRPnZ+dJnOjIiN8eXPjtQYLf3kjw2zsJfn9FjlB4XoV+mFkJcmBV9Wtm+QDyI1wYMl8Nqg5Sit034DMko8/jF0iVyPd/S/63u6jXov9+J/fwwVMHfjVyVN0m4HW08xSA7GmVA4kY3IDTwlWS3IEqeSFk2E/Qfii9gxw3YlLHYZIgbggpHNaF/i4b4vZlFPb9+3fbqoOv2YNUCeRRMGoUDnhXB/n8GdrmJaEfNF8z4AQ58uHX3z4g/wv572bdhY9rqJDhn16BGq61nYLALGtTOAw6DLoYUsjdK7/+9kQYislghYM+DL2xYo2TYZTGwH2DW1uyn6fU7K3KwGqSVw1kagTWGmTlIe/6wkXHRyOXB3ndIC4oQOaCzOmhVAua845kljdIDUOx9vpPSFuD+6rf7cq6q5jCdLea78iWV2HlyBP4z6jmfRCcnGchhP89GB73oZDqQ41wbyJeEWWMS6SwKqsIKuu5hmc9/AIrxtt0KNxCMnD9mo11EoxQ3ZPkAQ8cBJFxni79PPr8XmehY+u3te9jrLG+He91rvqa1c8EsCpwL+dQlR7x29Ady8I/niFVB3kL24IRP6jpKOnpBffplXsM8n/ZJ4x1HJHurcWjnCNf2ymGk8j/z+5jVJldLA7igj2KAiIqx4P5gHJsmEbIHz0W7AEQOO+RNj/6gjdWeSPXr1kSwrio+n88Rt4d8BzzIKy2gngd2MNdPvQ+hHKUew/OMdiq6g7F1+yNxT9BXO6UBc2GmQwjfQywtwXHp2+aBjBdx+sfFf2JzpjXMACRorUTGBweAK5tOTHUqhoT7OkGGKlgTLZrEDrBH6xCoHQYEFA+ApUIYcpApr9Dp+TQTJhbd/Tfh4djnwS1cFsHags7UvCKnGCOjHFSQwfAZmccA1H4cBeFpABiDFV8R7gOrOKhzNjEPhW0Rl/k6RgIv/PA8+GPqL7rMqoPpVowiCCW15FqXXB7ePZdz6evoLLpmIf3SX9099NW5Pfl5h9fs7uO7+wO0zsZK/XvwEFgWqX1nU9Hdqohw6TgGUBjGI9F+fVRVx+F+12XL3/q3D/+veb+Xin1P3ruCxI0TVF/QdFHdXsrbq8wC1AYI2EB6nuh+/xIu8+PfPv8lm+f3/PtD8IfWH1B/p6CfxDxjOwvCP6KvWLjo03ogDF0nx+IB/+ZMz+T49Ov2QH8cPQzGkZ6TXpYWd9rzdsQWHD8Cvjj4EftqceSdYVV8k620BVfs/dgeKYK5PLMHwtlnf8uhe9FF7r24bn3mgAfZQ1c2x2bNR+Me5lkVL8GL1+yNkk+vWRWCv7NPczI/TBkISDj7gemD+x/mhDcr957ofHij3u3e2JBRnDzL2N+fULGvvUT8t6CfkLeNgX3rVbWwl3Rz2P7Oy4Jh8L/3se+bwxt8AJ3Yk1fjMo/djpj1/Xshv+sxJhWUGMHjPU8f8/TccU/CYFffB9Ufxayu3+xkidZ1I01VueweUvxGurpwl7nEwLdB1MPZhMkyRZO+PMycJ0KlC0sg+5o7g/8fpiVP2z57Q5D89gu/vryRhpPHzxbQzgcZufneiyEKAxVuCC8fgQVfPZ/1zQ+hUCug/0KlILRM8ub2RZDAY+mcMpxbUDM5oD2wMzGp5SDY5Tn4QCnyfl0RlgWAwCDO/MZ4dHAZRwo7xGf3x7FDYoEmAcIBp86LjGbUhTJ4PTUYlyLpC3LxeZzGqM9F5aDH1NjSJRPax/WjVC+968jKk+jf32xZyQcuSTrFfv48ChjWDNiYyuBPalmHltHTNzQeTw9TYlydiNmVbBTIkVJq+WRPh8cYd9q8UqzVknIN/IGB7KpYppXx5MbIdT8RlaSoq12A0be7P56uDpLtiXQeFfy7IpLgRSXuoaXB6PUsTSvDpCHFoMe9RWWdrezXGOii8a8TswY4Hq3RQoKvLisdEMkr9AcpicjtokqM+okI82nnLaWzI6vVudtsKX7MtCKpjVW9lKjxDi9LQ+use7WPHEKcfEiWakor6fycG6L65Yrne6c9E43BAxAZ8luiTJMK9PhOaTzdlEbHNuVxDrhE7zlDGvtlKcgnN+SQlJmQcXIR5nqT9iGYzTB0LXFhja2hGNJR0NHuYDP2xJbJWS7wfza2EBG4W/6Sp3bskjKa393HU7bZrs56GBPxqaR5DMn7XyrxLqjLYKouZCVZXiYi8/MBXVebyQbbCtuva2FQY4LfMNd5PVlsa1m4nHNH2q0vsVaEUpT+YZ1Sk5FpBCbcdtzh+N+faaabRHVjbOk6vI0gOP2su4JX1or+tY7OKW+Vm4bp+IhVql5vuj0Ltgdo0nMntaNuW5iTIpOm1ZrXVWUFFCn4ZFOhxPVpQq+SOJywaKqOHNEa4/fxEiMuFtjqnqn7ybe+hCh3ZIPqaBN3RNhuzNsssIdyt1uGmaXCi61lutBoVT9lnG1hUsHOZUbzRBMEq2neWmctNrb3LTBOIjVSZyuNJQ2ZWF1vJCWClJ765pH9KYskr0folfOtJh0t0a1LJ6L6+VWbIKoXw4pjnuDo5Wb5ZZOMSo6BxHtHlRxctsf8jMMVuqQmpTrw58LOZTDLcahsjq9nRNiMMvOCeAjwJvgeKOUZbqMIcRVmGxQgTbJxYDSdnc9CyzZGrsGLK+8RW9IAzNss1U4yrI8PJHYNiENC2u1fXfaZ5ODzUULqdZC0lT4pa/3a9Cf+oJmw8nstC+XJmSH4Lo4TMFFNs+SLl3CGXYQCE7eCSx38we+dob99mam5NJlAzZoO1EauCOrSYO6vZWDKoXm7rCYo/EplSDixjBU0VTI6tjlyHWme/w0VAKSWgTJZN1opgyu61KdTcC6yeKymS6Y/ur5Dq/wO0+ZzT1GvciU4VTScprdTEY5VxpE8rTEcI6/6OFKaUwmCzS2j3pfXlR7jDsL0gQblPl5B5LFlHD2GSpfZGyYyRO5FrSgP2YTixWW3F7LD0tvck43e5ta1+Rh5U5RQc0IzCrDlTdUeLsFJkyKRYIR55OyqVBDTPhuI+hhiLNFGfeqHGfSrsy0wJODsKRzXd1Bv6R8wJs3jwXqfjLJV7xzaDbldGGsSdmdrBUSW5+2odcJ+Fq8YmJ5nLMatSyCY40puEUxBJ0IWwWAnVRp4ia0jSNK5tPMXgpgdY1Dax6c2krvzWsZ2QE/5zXpXLJpiw+hsjr2m8p1NoJWRK3bhVipTCORUBltvWUOO88nCGow1nXQ8Nz0cjro+XE5Fwy63FhqKSllf2omGO4DXOAngzdZiSzais5Su4WXllI0P42qStKEOSnd4lLkhL07j0s2vs6z+LYQmcWML4OAo652TnDs5eZkZpplWFazWeamVy0qqPOGGdNPNdxLU02YIJ6drUXL7gY2Dcx6HYTR6UgpWLE47g9mxF/dVcvvpbW1wo+5aRs7NKWqdiEmiqxz7iIRxRNrX6VLM9eY4/JkkGS54nU2XjhrK+1FrCIn5XAlN0J01U6iwUn04G82SUDLRerQWYEvSjNNXcUujB5Vh4TxskJZ6XwTKc5shp5xTdPNgqCybaU68XLl17tOw7IIpbD9ZkVH5Y4w9XVYCOoymwPVSMRoYJQ4dlW0u1yWWjDRXZ7dzJi5QaxXrGz4B6zILFVxisQ8nHaVtK9dgy94m9aUSk6k24xkN7lrbDv2gt6ccCbXabE6xRNmLa42onOyisrwVdZcCddUXF5WxxnrSbWlu3Eg5fmZdE7ZQnGO6o7YFVlzRV2rOgOrOtXi9OifLzMPq3ZTe6trqeTypEWnglRfqKOdCbus0hll0YL+rCz35gWfrIYbm+U6R0Pg9aEK6SO/GOa3Wb8yJGGxiEORmaAhdSqPigwZtprOpPha92ngN7yxIsWLlcWT+GSpk15pqaUpTsS1uG+41bn1AiGJBQmvb9JtuSfbfckPKqT6sBJVcjUlt9e1IYurGa66xyHh1o6A77WNnF6pY7AghHSB4rskDKfcbR/udRwwpbiJuO4Cq/HFVM4qLgxzmy0kfeKW62mpF7wmrOyYg5xFLrDDvjtoZbWRKAqc+eVez2R3ny9AkpzC4yU8VTu3tMMtq5+5funWXa06lXiTT1gUy5F9javoJPZSu5uTK9bh9WO+rmtbZVIriUxjRVQxLpCtbGzmodJdAqVzVxiu3WTWq4k2yo3QRWEvYwr8mridYodbHrPO4XjuIojSjPeZXalnLHne93F3gz0AJEYuUyPA4t4u3KseFxfXaOqfBq7Yas2BC8Kdv1wNk15OCHZvRbf8agsR01LMapIeF/5iJnTMNGDqqzqJaQ1bsjdnXuzF/RUYzYmpKqXA1zbQL8oyy6fEBHSdcWav11Qz9DwUur2IdqnoLG7YbafuUrxrtmdtM6OUOsC7oh0kbJfoQOlaxtF57yiFHDfU7rldrthwm+9lkbkUhF3tGj0mFxNsG69rs8c36Hq1uc0dglpkDrOHszDlaBvosUrkbjsPqHOmiY2Z43tqaTgZn1ME0zerUqexPGj98MpTOh/js9LYKNasGOZiDBEVaQz2zxI7pH6arWbmkbW4aKZtT+2SO4pAMzMqL839IsOlmM02ibI/5nEaTQp3HqwTptOJQt31IeZ7PZmjpj4I4jyTjp627TCp02fFwcC0TZ+6+Wm/GEJqXl/8K2zBwn0Ae5trzaTZMJkZk2KQU30R57NlA7d87CE7ipsyCoDtXOo4xVWeEdvr/CC67nxYMLxjtPtlMlU2RWCmtZxSZtycN0fZ3q2rzeEkdBdhmijmdoL7VH1wQh5zULaq5xaOb4sbmCuKOTluCn6Ip4munjAdLaswJocl2LUJ5uPGkgdofMTOx661d/rMnpB+dD1fDiKGX2sz2cnXQmJh77PfmznZaa6uSmw81YPgxp2wq7hvF1tyQQdsTtjqqc3Jw+YEmEuOAd1eNXqlBiKs6YSXbyYbus62hyaCq7prhTMaUm/LPbbXrGrdHpZXdUtyZigozLqfc7rvCyvqgh+EjSHtXLGnYHc+P8pRubGt+VVqc+1yEZzj9VAwCZgttDQ8TDGfCbfhebOWcHPmX5XFRbpebsxppuUxM3dnHbXRNU69TsxLU1P7+jjz5H5Itt55ydHlQeITjtIxflUebJN3btsrbead2bHmMA8ztV5MOHnO9QZaX86WO0Q7AicjWdpeV9GMiU8xLa4NVFbYhuGMY4epB+vCGZepbMzj4LblzxMqXecJ4fpFGwW4sZJooyuPmbQ88pzLuKqcbxWnhA2BvDRNAfdnW2kZQ0yMU7Tja7bWt5Cp8am70SzPG47G4erquWCyl9xZG52x5KaMatJ8f4AllaVWJcnPXJOLxAkmitOtFuECLXsWtlxE4XaRevFFmiaurosHQgKHNtJIRoW0g813UdPas32Qi3uNWOHe5aDfzpVMTabnydy4+YmXB1g9pbCe0IgDrCTljhscg8Y7d1rQ3r47axzaCB1oMVjvPQPQPgqZHqZ6zdD8kATo8rRL98nGykC7uxS9LONYucguw1YpPdZ0ogtWEFNCtf3O2zdGpuDtgQmSi3hI16m0jaNVvSG9q1qscFHY+eDalxUeUCc29WuyrAWfWFu8etbBhiXouCnKWvMKBrdU9ta5S5u/ddNmMxFmTX0WvPQyNdwpzhpFMHGF4cKf92dAdxyIhmunEuczQS8EMjDD4nxC0XQ52aVxA3fSl4l6XqAHvSlUcFjKnX9O8pQkefXmukeHPd+8I6eclnPew6WlujdRqOws3DGkvY/WRM/PdGcP9KEVzE3Ee/GgDhU4WebZbo16mOssIVcrYhf6DMEuKxzurSDT7Sjv3MlbhxzYgoovq1Q/X93bMTpNbcUYCDZrUMPTN30041G6l3NpkGbDZL6fbIa6Ktt9h5+ogVmZcs1djoywXNLyZDoXuJgl0pqeUZZSrcNTMG8Wc2qaMFniVd6kdlyzXw9tc534qe6H7cBhkwlP0nRDqD10ZEi7FT69SpHIK8EpW6dKRU/PFNosXE8pJSKg/Dl1I7aDO6cDV4UNB7s/k6lRM/zEDkVigfMrjbyZmal5+ylGtqYwoS5oabfrfulfuf5UTOYpWVzM5AKqAwVD7JhfsyCT4v1coqqeVboF6Ux5J1Amq53eOS51Y0jhtq85m1tMV+65Oa4Z5hQdsAk48uaRIZflXtYu9PJCXzRSXUW+P+wuflxycDtvm4XsCR03L6vlnMhBVeKtE3sd3G9w1fG4P6HWGSh27RLGdNXaqdJRdHg0UyrdrhnCp9cUSm+WHpmbpH3erNBbFXvJpGWpqX2W6XpKm2ttJu5Eh+jg1uu4FxZR1i1mUXdtbjubqNeSo1iTGwB2ZGRR7Zkn1sml7mQs7X3nbnYBhtt12cwuhY0G08rxr/gmU80onE39DLt0HJsqDitJw166dXlxvtBmvGcpoMaH2W7IMXs195a+aqa9PSvPzLoSnGlKXHsiZK2l21Uof/XAiT6TnqmY9YymDJBxLmpRHrPbCKrLeNPGmedLB0dXs0VF49NuEISmH3DBTmgWKG23pvqUVitmwqPorloUPNpZdKjgzOasrLRtvASibPoLVTBOzdlN0bi2uZlSLgfRaluzRc9roaJRdCvsFW6943HFk6IBBTIZ5Tgo7QhTz1npFYd01ihklxhF2fFyJpXYyfTW86UrhBh5VfKtVMhbMVOCKBgCbEtvk/N5ShUO3p2mKT3FCD1zI+xUHvCgPHQuQ3WqzoPBn6sS5+i4AtaT+XV+5eota1ybnVTUrEPkfd6nqJ5iiRLNSScR44WaaFOL2oJkue+sISETH6ZouCHrihjs1QIFN1F21jEqbyXGn1anW2+dq1ql1HpQlrTp9xPU7OM5OcuVyC0wSMb7gzylFLR0+GBXeNvGWE+YYQeK6LjZA8DS2tEnkmrT+zdsuTdgoO+IPuW7Sbjf+Y1ADwdUQFUA90SRdiG0wTCzTZXuOHTONbPp4VayBcuy/3z59DIeSz8Pl//eG+TxqO//2Ynj43Dw7XXT/WAZWO6X+1pf/qZev3x6qZwQavU4X62T1n8eRP6X09XP/9abilFE/3g9O74fuzVvR/KN5Y+/afQSZm5bN1X/rhScYbf1+CsP9bfnYfbL3by0aO7P3s2BV5abhlk4vj791uTfHufL4324MqhS4IY/Lv3n0fOnF7eHLgud+hsxo76Bqhhtfr4BgaZOX7FX/OW3/w3r7cR21yUAAA== -->
