---
name: "rar-cowork-cookbook-teams-update-allocate-service-parts-inventory"
description: "Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_service_parts_inventory", "rar_sha256": "cf43000fc6cd4539a569b9f93021a58ca29e1622bfbfef6f4fa7d84df6e111cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_service_parts_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_service_parts_inventory_agent.py` and in the RCI capsule.

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

Allocate service parts inventory Teams Channel Update — Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 cf43000fc6cd4539…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_service_parts_inventory_agent.py` first:

```bash
python3 teams_update_allocate_service_parts_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_service_parts_inventory_agent.py   # or on stdin
python3 teams_update_allocate_service_parts_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate service parts inventory Teams Channel Update — Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_service_parts_inventory',
    "version": '2.0.1',
    "display_name": 'Allocate service parts inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-service-parts-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b34e68f098d8b3f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/allocate-service-parts-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-allocate-service-parts-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateServicePartsInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateServicePartsInventory'
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
    print(TeamsUpdateAllocateServicePartsInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+5Oi2Jbuv8LN+aGqh6pU3lAnTsQACooogqBgV0c17/dDHiL07f/9btTMqp4+Z+b2zESMFVkpsvd6fGutb62N+duL3bVRWb98eTn4dgGJdpbFkV9DduFBfNmXdQp+lakDfiC3LNo6drq2rJuXTy+e37h1XLVxWYDti9oO2gayId238wZyI7so/AyqyqaFygICckvXbn2o8etr7PpQZddgeVxc/QLIG6Cmtduugfq4jYBycKP1a9tt46sPsZ5d3d/wdu1BQVlDly52UwgYY4f+KzDFv9l5lfnNy5eff/n0EoP3L19+e3EzuwEfvdwtMioPqGefZhweVuwnI9ZvNgBBmV2EYEc1AFAKcF35NdCXg488P4CeVx8bPws+Qf/6r2lv12Hz05evBfR8fX2Z/mldAbWRD7Wl3bS+B7l2ZTtxFrfDK8RmvT00UO23XV1MeDXAjSJ8fez8LqmsoL9P9z4+lLyGfvvx60sJTLAnxL++/AQBIL6+1N30/nWSUn386TUre7/++NN3OU3nJL7bTsKA1a/fntdPsWDh96VxcNf6dyD1EVvH//ryg3PT62H35CfY+fKalHHx8SG4qkuAo124/sef/plYN/LdNIub9v9L7s8PwZFve8Cnp+E/fbqD/AsEPx16l/nP1VYgrH/FE7D8Td0n6AnUP5N9x//fic7iwm/eEf+H4v7RBvjv0M//1Lf/aMMnKPj6svAzUCO17WT+F+i3b4f9kv/5g/f9ww+//A5E/6diDmVXu3cJ33K7iAO/ab99+/lDc//4wy8/f+gqkGugor51dfaPZP4jXO96/oDgc9XHP+4F+o0iLcq+gN4zHfqtrP5P/fsrdLSz2Pv+efMF+rFephcMTU68KX1A8EPNNMDWH3D86eV3wBUF8KZz77dBlf/Lv0Db2K3Lpgxa6OCWXQuBALdx7k/G61EMKKu513btA1ybGAD7XAfyf4rwZHEZQL/+m3tnz8/ukz1n7cRC37o7DX17o8NvTzr8dqfDb+90+OsrpAMlZR2HcWFnkMbu918LwHZFOxlQ1f60EVCLM7T+Z0BKn6c3gDWhX/+Snm93ka/V8Oud8eMHb2n8euKspsv818nvU+QXTy9dwM3+zXc7oG0SnUFBDIj3E8CjKTPA0e2EUZPGWQZ5cQ0Amch9kg1w/DIJ+/XXXx27ib4WD5LFoEcXaWZgwbs50OfPwMcgi8Oo/Vr4blRCH377/QP0f6H/aNdd+KRjD4j/GSVgoXRQdhCoui4Hy6aeA0jZ9u5R+u33J9JATAHaHohpHMT+YzPI2tT33mA/rNjPKEFCjg/gBlDnVVm3gLmhuH2F1gH0bi9QOt2auD2aup/nV37h+YU7AKk2cOcdyaJsoQakZhMMn6Cu8e9af3Vq+25iDsrfbn+FtvwedJIyA/9NZt4Xgc1lEQP435Pi8TkQUn9oIO5NxCu0m/J06rZ2FdX2U0dgP+ICOsjbdiDchgq//1pM7dOfoLoXzQMesAgg4z5D+nmKORgHcsAQXvOm+77Gnvqdfu979deieRaEXU+hcEGDAErDLvamNvG3Z0o1Udll3h0/YOkk6RkF7xmVew6y/9kA8Zg7+Ofc8Wj30NcOnSM49L83nNxNF0VtKbL6cgEtd7pmPSCdpqkJ+scABmaD++Z7+XyfF97Y5o10vxZZDPKjHv72WHkPxHPNg8i6GuCmsdpdPsgCAOkk956kU9LV9ZTe9tfijd0/AVjuVAaAADCAjJ8S7U3hdPfN0giU7XT9vdPfgwrcBmkAEhGqOicDSRL4vufYEwZRPRXaMwggY/2p6PoodqM/eAUB6QBlIH+KRgygBx3gDt2uBG6CGgvqMv++PJ7mJ2CF17nAWjCu+q/QCdTKlC8NKFAwBE1rAAof7qKg3AcYAxPfEW4iu3oYM024TwPtKRZlPiXCDxF43vye3XdbJvOBVBtkGcCyn6jX82+PyL7b+YwVMDaf6vG+6Y/hfvoK/diG/va1uNv4zvagzLOpg/8ADgQSECTyxKsTSzWAaXL/mUAgE+7N+vXRbx8N/d2WL38a6z/+tcn/3kGNP0buCxS1bdV8mc0eXe+t6b0CjpiBHIkrv3k0wM+PxvT5reQ+P0vu873kPr+X3B+UPDD7Av01Q/8g4pnhXyDkdf46n27JQOuUws8XwIX/zFmf8enu10Lzvwf8mRUT3WYD6LjvvedtCWhAYe2H0+JHL2qmFtaDrnknXxCSr8V7UjxLZuKgcGqcTflDKd+bMAjxI4LvPQLcKlqg25uGuceRJ5vMb/yXL0WXZZ9eCjv3/9pRZ2oJIIMBLtNZCVQTGJPa2L9fvY9M08Ufz3n3OgME4ZVfpnL7BE3j7SfofVL9BL2dHe4Hs6IDh6efpyl5UgmWgl/va98PkY7/As5t7VBNPjwORNNw9hya/2zEVGXAYtef2nz5XraTxj8JAW/C0K//LES5v7GzJ3cAjr+TfvtW8Q2w0wMj0CfIn1CbmiXgzA5s+LMaoKf2AfED8p3c/Y7fd7fKhy+/32FoH6fK317eOOQZg+cECZaDYv3cTP1xBjIWKATXj9wC9/57s+VTGKBAMM4AaW6AY/P5PHBJ18MJjLEJknGYgMHmKGITtGujjI+QKOoETuAHZIAHNuXRuBeQPoIgrgPkPdL12zQRxJOB/jzwMQZBXQ8jUYLAGYRCbcazccq2vTlNU3Mq8ECX+L41Bfz59Prh5QTp+5g7ofN0/rcXh8TByhXerNnHi58xR9s5zRwtkuE6g283jFQxo5rDhSToSRqQSaXIKa9zxZnU/OWGkiT3cGx1abvNKD/csrO5NrNMRgqCLcUTkmHVo5uErng57HSXUsaGkrc03AiszpG8LsepfjpE0dH022V8lE6ttiSvyJkwj6pDG7XUamKxIYpiE21nGZ9Ks9nKoWDpJmm+mi3x2NWkzDpVGrHcwAdKrM7e3HLtfZ2dWcJsD5c0zduaMPDDyZT2xLjZRCe5jDZXkUBcQOMH91Lwcz9JSW8/NqRb1DTux9TWrGlixjenOtMkidUQQj5peo1XG+TW+qcLPa8lJUtWR3Gccc7CF/PdyhCGuX9O4vbsaMS5t0wl43xOlfaGbh8PrkkMY3fJxswU7MLw4txFBME/HovFwuaR8Xrk86JhM4QsBzElWZ4k+y6mbMqP2xbbZqNVwTLZ8Hq1JArhUFVbXjufSYWWB2lLoOvoKFWyUuAbNFqjQUakh1aTt/ruEPt1HWzX9vqMlecuLpXVgMf2akBwQxFgWFh3l9Mq4BUxz5rVzJZkbqwO5TGOGLOJzsf01mgXcsDXWuoG9LC5CTXXwnnp2bfz4Em2kWmmI4G6uXk1X2B7cqblF5+l90u4XZ5UBFlmacaNXq+0xKWlrIPsoJ2/YIfF0XVoZVgdCUy9DChuyc5obzUUP7vh2SXgLM2t/oDSeMS2sVDjp6RJj/S5OdSnoTPkdUbPj8ZGkhpVmDGhvY2UgtNmSMvHnXXti0WMG/OrW7Xtol+hjRtnC3Zzwxby2SCiLR60+RZZkh0pN1hD8kkUWZkjDI4Ah+G5NNosyS+XJi8WjB4gN/0IfswMry7ozTODnqpqKaG2o4yLwIyRNgt8vRrYHcNEB7o6Mb0LK2cEhpn9fEP1bmE33cjj2m6fzdaobASCXDXJeWXGh8OAnkAPVl3X0bYnkVSRVbzTD6lRjtbRFFN1jIdjfuDEq3XJcIRLHZ9V6UV/tfNVv7nAN08t+4saEmy68Dfriq4NW1M4G1uP1dKS1sc0HqzY5g9nPctcnOjxnIsx2BvqgENn6/lu3mqrwbDyphKlQFRjgcjX65uCpFpKOS5ZVHtW9vfHcTaOx6oZU+m6oQJNhVv6YnhO4pB7eIXu8DDH23TAvaxEmGAgTY5smluzkTgz72MDVXfFiaaXvoJvLa6whjV7KqUZqWWwKbnIzFP3yxnWsYhqGnY5HCKOHECGXRCV2gQVEx815ESqDre0CulaDyTFiJe4Xrmoe1ZOuCQxq7Oft/aA0FhasP2lNmOaVObIHFUkhAyNK2dVxpDSeUPi9bCz7JRNVjkvp/t9iNLl3mJi29Riezj3ZQWvM3Se8K5xrZt2eTFsApHhUM9YDBQr13VzheTreum53qUJq9N8aw75UG+Qs+eelBWpqVmK3LjWO5wRLcWUtKlyT9oANlWPmmVK1oBlJ2ssDwi9XzHH3ak+XJ39kBpkW1L2xXH6mpi3WbrkALU2lzUtUHPZng37pthm+VitjIDbCtTOwZxwDfMwhVCMxouu01wzTmRFuEEWoEdg1Va5egvKqg6xe9iXwu5wy3onvSSCUVy351N1WVwXKSN4M1iSWemIVYdKuu1GAmb4KjvDPqUsRM4mdlkeJf0Si9SSX/GeXWIxrLt2fHHleumchIjpD8tKJzbEXm93KOw444mhYpDSa/3SbfDNreyVw8ZNt8vBOLMnhWezsJIK2z9v4yUXLuh6nRSdZq4lycC2S11j24uxaC97vVbD4HZMtRUjnBOKoLyiRvFusz2uN6xgnPXVglE2uOIEwj69mdWqJ/BtOd+Czlr0x34XdqDNeFGDbpb7WKaYgzky7n6fOP1Mi2aKGZdGY7RDVJbnyLxeUkKyOJvmleOOvBHrREn4xYhYF1GXwn05mra2q/blbaSidRYiy2HGulchxzzVQNZhQ5FpbZxt+yZURhFujhWub4RrXHFz7Wh4Wq4vsIUwZzzwOxyxjkeEq78ufZWwFnZ7HdfVPLjK25K4EfZhE8iepd/Y1FwWRs5s5IrsLOd0NLcVqdkzVNzb3JYVM67E58exlkmZx/D+cNsw58RJonghzARqvdNRAj9gNDi67UsPy5I9rHIuVuLZFqUV7rI2Si9PSVFF2rEn0QC7dVW39hGt3F4zhIlxz0XDM9ofBi/1T43Mzg0NDghi1iesaB8tpay3KEzb+alct2EJb6Q67Rn9zLteFuGYHV1UPBzYA0UcoxTLWYFTVzt+Ye/yNi9iqp9Hun12+7m5mCNqZYha169KPgjRblORkr44E00hkwZXCnAWV1tiYcVUJXkHUdkvl+QyciWav1idstov7Aa7DJtEttVoU7mUbvSAyHZYj3aNJO3ZkwAGnkqVqGZcopFsOaTj72y1Ozlph10vMu9Fo27LQhk5fYB29e4srOceUu7W8kG0mQxZmfQ19dxIIE3teJIduNB4fX6+6L60ya+3FburqoQf9nHOXk/eMVJFcedlrMe2uWzymR0vY1rsd0bBhEf5zIZLdivFmLrC7IFZe0u1klluuZhRMtEotHbbkbaiJWeCDKUyOnPYEiZCVza6nYGcz4XKqNyKpM90UTN9y6I7Bc3UDXm1twiKK5opNYnn61ioeg61mOdkE2PG7Zok8SZ1TpVbU57oLAUtH1N+nTgxjJNqxMV9r5Yi0y/ordZl8ppUODyWtXWjEtutxqyEgdrpYkWJTbiWGSXJNAy+HA/2SsjkvSFZ8z0ZH5JLq0fuwrncLsaRZ6icGH2RylTRxej2MEec+rZXF0G43ejXQ0bU9CI/aDtem5NpmXp+GrjrjYBYxkGliFqMDseC58UsNjdLm8yXS6KSqhmoBzWlbJS0bdYRzijrHkfVB1wt7qxiOdCpZRHbMSK0bN+lTSQ72jxzbxyDm9VmWLBSbxk5l9I+G50SPU+ivCdWZtJErV6MwoIerKGhztSxiBTFXO9ZXekGw/QLJVaXSi1qi/PNE/Rdss/Lm08km3FVie3Vqy/XhsnJUMno61aO1NnpFPBHX7taC5FKYisCwhMwG7I1w+86eWNLAXKUdNdLWtm0yUO9JfrkSiwJwWpnY8mXYGDaCrTi3BrKPsfLecUNHm/obnLKnXZxyYhynQ8pubFOaC+oJ8JGwgBdKsm1oUkqS9T2PMOIJCXYpDYHAo/mmLN3ndKnZSW5hNSNNODcjkMJuTDlsuh5Ju0HdQE6wDAXIkOBLxs5g0+1LRGXpX6J1YEQsk1wIm+4aiprFKmo7dU2pDFVyPwgoGhnifLy3AyeTVHVPEndfSwUQ6xVSIqI0brGgpi8ZjxvebB5RmInaJaREzn4xdTXWs1wa/FQinZG33YapYfbXupWsrAbPTwRXUNFPCWhhbHfN6aCmSChvZwhKtXA187SF4+jUqnmnm31+qoy+hXhCuW2Ntb8ggHzMqMwks91krOLD0ePiXPCxYy5mDjmfNObi7S3HcfUh46/dEeF4GJVEdlZyd7KMi7WwnFDn+tdKQxRMbhCUBzmYoaR82bOg9lfptnFlt3WO+oaUlwya28Om1kbdZ0723G0Tnp2i7RzVB8Vy8Ipfn6rLOmm9t0sypHzrpnBAbUyI5OASUMG3TkwmjlD4/qtFLt5XTSi6i8Q1LJg+9hFTrBeyiY5rDB9kfKzgLk6FzOfdQxs3uBbSa5qtHUZpmPM4yz2vG7bZvDeiRgSoQ0zJ2cFy5hOhiILzUGxEDO3p/Ul2yTnLmIqDNkllX6VwnLr6ysrW64IwxDRa4TiFMlRjmKPXl5suFA7EmlkjQOg1fS0oK+9OY8Drh+7vKFzh7FUjKV7Tl7eYrub271Fk0xyEkyDcWsv0RhHmVkNs/JWEUwNVG7IMGcveniBHlsCGY4pOxMXPcbWGIp1ziGocTe6MQkDz3pkBsaJoV7oHTLOBAwhkI4MKakgkBArNszm4vIKflxybDKfr8LzYqVxi/LqO4Dz2YW4R0X0sF5zPgWfTsZ2Hdqsd1KM6MbCIV0teLE/rNbuadwvEvd0sUyvOzYSfWAx0tlQ3lXDleXJ2aCGzgmqPxCF79K4lhsDmP8j6+ZwGCPaDgFGkJ4KfYwqzrg+X9FCj83NUBjF0wjDKiyPTZ3DaoediZwMbpdQCvauzV7pGeWFW1kdbGvEnW5drxKLWYn2zhtbeaaIs9MssWhGiyO5C+ezUPTD+DpyeBFwuMdhx5oqpGbTUXbSuppzY2fW8Yhajn0LMtgm9Prc70Nvi5ERtjpMigH0omNJm62wp/zqvOX8IHZbYb1VW73RuDJkhMKqCZLHZHNWnZdhjQ4yCweavznBkqVfYF+RrRXlcjgRuSs5Olmsurdvis+w8DadrUHHdHUnqbdysWpsJJbwgzYuL3oNd2bR4+vm2if8fI+wQbw46tiMdEcF4bhVZ+Tahl52elurxmmRD9YCUQTKp81MYToVrWOChxcprnWbIFz44zVlcgnb+E68KwRYL8rsHJ8WsDMEmTJf7ZJmflleVLNt6L5AlW3L7BBGRHWUxJASowBBqATMkWuFhTcNT/W4OEahQAfoejzJ4Vqvmys749vbZdidVuDAqih872wWTnHrhJmakzmqK4w3b7GrY+aqRbZIttVunhMfSRiT9tNhnm+oCr6t5rkZYVausshpj9vkagwRR8L9VbmyTgNJVgWzyNclo6ERck1ZZEPBNCtzDHNurygSZjlV72e3OYXVM8EVbjw7o/Z7rzL2MuCpPhpnS/zQXSl/5tHsXE4cqe7CINXRpHE8N1kVFxS/UXTG0CxvBeQ1DSyfRxh0vl+Lq+MqX0tNv9vzF4WExxWGWShzog6SeGCCJjrCEroLYn2+19UFWx2OSDDb63ph2evUxYIQHig6GSWn00VFdq3VZST8is33NhxvVh6hrpnFaSRZ1lYSThROGMcVVCGUB/JMX2dmOr8GTnA1D17jwavyegxlDteu3kh1tbHpxohWBN87IXtf8uGZ23PNlvX6VhTaZtVg+FAOxdUebS1XxQAlY3VFoVcHuxzB2Qgwit8zwzh3z7clTeU4rcCLq4lveVNxMLvmgptU7ho3P5HgOMNj+xEesTVcdLAbrlcqttjWmMRn4zm5nRBtdjH4MriY40q397o/sr4zR/FVwkpIv1VmNHfYiXlOLHlAo5t5vhZuyIFAVmnYnAN0jHAK0FnPcKZXX5PGRm89I8xYcbTxXkc3Ksu+fHqZnlg/nzv/1750nh7//Y89hXw8MHz7Zur+0Nm3vS93XV/+i/b98umldmNg3eMZbJN14fMh5b97Avv5L325MYkaHt/wTl+t3dq3p/itHU5/w/QSF17XtMCSpsy6+wPhTy9O10x/RdF8ez74frm7m1fTU/Qf3ZuEP/1qy2/PPwB5mf7SYfrOyPfix5rpMnw+pP704g0gkLHbfMNI4ptfV5Pnz69MgMPo6/wVefn9/wHL25SHLSYAAA== -->
