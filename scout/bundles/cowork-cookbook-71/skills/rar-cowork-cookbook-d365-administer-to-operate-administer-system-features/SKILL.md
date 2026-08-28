---
name: "rar-cowork-cookbook-d365-administer-to-operate-administer-system-features"
description: "A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate_administer_system_features", "rar_sha256": "c958d1cfb99160ecd3029d1e13c273ba3e35015aebad83f94b470118604be556", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate_administer_system_features`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_administer_system_features_agent.py` and in the RCI capsule.

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

D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_administer_system_features_agent.py` and embedded as the fenced Python below (sha256 c958d1cfb99160ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_administer_system_features_agent.py` first:

```bash
python3 d365_administer_to_operate_administer_system_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_administer_system_features_agent.py   # or on stdin
python3 d365_administer_to_operate_administer_system_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate_administer_system_features',
    "version": '2.0.0',
    "display_name": 'D365 Administer system features Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-administer-to-operate-administer-system-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '199f030de51c9810',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate-administer-system-features', 'uses_skills': {'custom': ['d365-administer-to-operate-administer-system-features'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AdministerToOperateAdministerSystemFeatures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperateAdministerSystemFeatures'
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
    print(D365AdministerToOperateAdministerSystemFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816+bPixpLuv6J3JuK5PXQftCLoG454WhFIoAUhQG5HW0tpQSvakPDz//5KwDndHvvemXtnfnjYHSCpKjPry8wvs0rntxenbaKievn8sgNOjiydNI0jUCFO7iNccS2qBH4ViQv/IV6RN1Xstk1R1S8fX3xQe1VcNnGRw+kMwg+5k8VejRAzChH/947bIKAvQdUgtVeUwEeaAmkigDB+Fudx3UAt9QC/MiQATtNWoEacCjjIBwdJQQfSTzhSt65fZE6cI0Xw/TwoCUqsnAb8iHyCdnWgqhEcRRQCKavCA3UN6ldoIuidrExB/fL5518+vsTw98vn31681KnhrRceGvpNqFmoD5Hfbu3u5olP66C81MlDOLEcIGY5vIYTgqLK4C0fBMjz6kMN0uAj8u//nlydKqx//PwlR56fLy/jf0ab34FoCgfK9xHPKR03TuNmeEWY9OoMNVIBqDKHgCA1hDwPXx8zv0kqSuSn8dmHh5LXEDQfvrw8QIEO+fLyI1JUUF/Vjr9fRynlhx9f0+IKqg8/fpMDET4DrxmFQatfvz6vn2LhwG9D4+Cu9Sco9eF6F3x5+W5x4+dh97hOOPPl9VzE+YeHYOiXDuRO7oEPP/49sV4EvCSF0P+X5P78EBwBx4drehr+48c7yL8gk+eC3mX+fbUldOs/sxI4/E3dR+QJ1N+Tfcf/P4hO4xzG+hvifynuryZMfkJ+/rtr+0cTPiLBlxcepDFME8dNwWfkt687TeB+/sH/dvOHX36Hov9TMbuirby7hK+Zk8cBqJuvX3/+ob7f/uGXn39oSxhrwMm+tlX6VzL/Cte7nj8g+Bz14Y9zof59nuTFNUfeIx35rSj/V/X7K2I5aex/u19/Rr7Pl/EzQcZFvCl9QPBdztTQ1u9w/PHld0gZOVxN690fwyz/t39DNrFXFXURNMjOK9oGgQ5u4gyMxptRXCPw/zG3KzByUgyBfY6D8T96eLQYctmv/8e7k+sn70muUx+S0VfnnXq+NsXXJ8V9f/dBmF/fCPPXV8SEyooqDuPcSRGD0bQvuROCvBkNKeEQUHWQYtyhAZ8gOX0afyCQT3/9l/R9vYt+LYdf7wUifvCYwa1GDqvbFLyOOBwikD9X7cGaAnrgtVBrWnjQxCCGfPwR4lMXaQc5cMSsTuI0Rfy4ggAV1XCXDXH9PAr79ddfXaeOvuQP0iWQR9Gpp3DAuznIp09wrUEah1HzJQdeVCA//Pb7D8j/Rf7RrLvwUYcG68HTa9DC9U7dwkoUthkcBh0KQwBSzN1rv/3+RByKyWEdgj6Ogxg8JsMoToD/Bv9OYj7h1AxxAYQdQp6VRdVAJkfi5hVZBci7vVDp+Gjk+qioG8QHJch9kHsDlOrA5bwjmRewlMJQrYPhI9LW4K71V7dy7iZmkA6c5ldkw2mwshTpWCSrZ6WBk4s8hvC/B8fjPhRS/VAj7JuIV2Q7xi1SOpVTRpXz1BE4D7/AivI2HQp3kBxcv+RjVQUjVPckesADB0FkvKdLP40+h1U6g4zh12+672Ocsf6Z9zpYfcnrZ4LANgCici/rAxK2sT+Wjb89Q6qOijb17/iNnQCU9PSC//TKPQbH2v6POg3h0Zl8aXEUI5H//5qXcQ3McmkIS8YUeETYmsbpge3YhY0+eDRusGlAYIA98uhbI/FGQ29s/CVPYxgo1fC3x8i7R55jHgwHl+BD/jDu8qHR0NBR7j1ax+irqjHOnS/5G+1/hAFw5zjoMJjayQOjN4Xj0zdLI5i/4/W3FuDu3cofEx1GJFK2bgqjJQDAdx0vgVZVY8Y9nQNDF4wQXqPYi/6wKgRKhxEC5SPQiBjmECwNd+i2BVwmTLagKrJvw+OxsYJW+K0HrYVtLnhFDjBpxsCpYabC7mgcA1H44S4KyQDEGJr4jnAdOeXDmLEzfhrojL6Anm7A9x54PvwW5ndbRvOhVMd3GojldeRiH/QPz77b+fQVNHYMn4eX/uju51qR7+vT377kdxvf6R/mezqW9u/AQWAAZvWdYEe6qiHlZOAZQDAS7lX89VGIH5X+3ZbPf9oOfPjndgz30rr/o+c+I1HTlPXn6fRRDt+q4SskiymMkbgE9b0yfvpWkz41xadn/nx/95GNn96y8Q/KHth9Rv45g/8g4hnpnxHsFX1Fx0dK7IExlJ8fiA/3iT19IsenX3IDfHP8MzpG/k0HWIrfi9HbEFiRwgqE4+BHcarHmnaFZfTOxtA1X/L34HimDiT7PBwraV18l9L3qgxd/fDke9GAj/IG6vbHbi8E49YoHc2vwcvnvE3Tjy+Q/cC/tCUaSwUMaAjPuLWCyTWSZgzuV++t1Xjxx+3iPe0gX/jF5zH7PiJjG/wRee9oPyJve4z7Pi5v4Sbr57GbHlXCofDrfez7XtQFL3Cb1wzluJTHxmls4p7N9Z+NGJPuSbmjLW9ZPGr8kxD4IwxB9Wch6v2Hkz6ppG6csZjH77Wlhnb6sDX6iEBnwsSEuQYptIUT/qwG6qnApYVV0x+X+w2/b8sqHmv5/Q5D89h9/vbyRilPHzw7TTgc5u6neqybUxi4UCG8foQYfPY/04M+hUJmhO0OlOotqLmPeYG7WGAzFHg+geILHwMY4eE04ToEICgUoxzgOv6cCBakS9Iohs1nKOkCCoqADrtH79exY4hHQ3HH8eYejZH+gnZmHiBQl/AAhmM+TQCUWhDBfA5IiNn71ATS6nP1j9WO0L63wyNKTxB+e3FnJBwpkfWKeXy46cJypgfaNSJlekQnfX/dqjBz1mZ3YS/EisKkg3dcMRkPbp542ldz0U12zcUhz2sPLWh1s+WkGavhO0ASNV0nxi5Vk4nMOBP+sMl9wq/ofItuxb1pkPMmOx7J2PRl7ObuGourOrairZMs5lbpKjG9xKMhqeaTbtORiT7HgTFUxqaabXmzwwavi3i58jtB5AorNSRr12CSSdlyHG7KTX5o6k7kT6ChnMbeUfNV3bY+wxmGcnBSfmM46xZum0R9ovWwT42dFRq76wPupaGnKTUe5HZNaUcbnQq41x2p22LTLzsvp+I53Ieltog3ppxVZys8JWJfyv3aHpRcnbH5ZJW51TW1Q+dMrBbKsKeAY+D0Wc/00q1lUY21xT5fT7wNkV55brauZDIj80S8Zody5/HsobVnxeGKCelKxxdVsjpr69Tfau2KOjDUvHKsAN0OO9qq8o0wWDJUNYjmWmOJCNxuqq+vkkvudQl3Hli9LpfDHm930p6QKbxuWt0oxL6NlRPD0BVXUbUn5025EicTcdXtqm23TRRj3/KTRphy1P5ycGJ1cayjdZpbdW9RGVWYqB7MY6EXS7aZZOHe6f3BW/enuqjsBN9NM8nd5QfMjBsldbflfu4Jno4Nm/JgSduemRHZhTiXyrbrKZJk115k52lG3ECY9niZKLCZ1Nh6cI9r+YAHpb1uvasr1wZzWLgHbIXSddxVYmw3gTJhIMG1yXXfcK7AHhf1cp3J+7ka51F523r+lGxZbrCu82u/dyaZKk93WDIXFa2w3Z1UKJlG+83WOFSXuKoXaliQJ3Wt3fz1TStW0kVQ7NNix24Xp20pDFV9OxloRVxOLe2dYppOMdW1tP4Eelw+xl1eFFIy0dYby5lgpySupsdpse7MuelNz/xUgrZ4DXBx/iKt+ajuiYHtUuVS0KJ0EuourVNDgRF/w8CQ4BuOqo9Dg3M7vo+teczpVbabWJInHnIvTD3vzN0K5hqsSbfkkpoyDq15Pq6Ug3Ti+PQqbCCq7faksQ7B9Ku4rhP5FtlbwzLlIgpvKgp0lb1QPjC4yD9G2Jw6kTjTNCnv4bHcmuoVZhNxUVhd4q4oZIWFu+oGvWFbUC6KQ+bfBNJ3gxRWHnRelniqTaZol4aWlOcb8xzRaa6K03XpHcthWO52DCbhnnmw+eNaMwZo9YAP2+7Qd1QMCkebzWSZto/qpivcmbW0Fstlxx5SlqL0myUXdDBM+hm3WHeH8uyFW0usVZsaCHZ62ZfbwfAp9MZPqMbZF5eNPMNODMbtj1lsRZ2165wE27KTClqT5PxxqRjGzi5n4bThb7NlM+CySjV82e8Nk6qO80NFFbtNL00X3T43z3vuohXEKgSGxZ7SbNu2Z5M+SLmQrC7kvDatYhVw+Cw72tG5aZeruWFsEmsntL5qV7dD5pVrwOzRdG9KeO2VkDl7m7pFu5NFanlVp87Zr4nmfNs3/LHrt4ubL5JyRqEijEw7NaKuGzzN11FhWnvEZW0T9EXdzdOJQi+D1GcPUpfbhDefcSYgItOAuxc1xpeUQuWaTqkt3t5Ebg/MhF1KhevvNuWFWyu5ItR8rLJSOQvirJ8LSivpJnqTie4YT0C9PtEcw/RhdRZwWKzc625gMH2WlNvJ3qkDPaAUgVHW8aYSb1y45pOm41NSHvCrvtkaObNao8xel5dLbEUsdyGxscliq+/SnAPCwDnx3tNW8xskiHhvHw6SeapBuDPUgjosVjG2wxbluZ4RroKi5vU2H9TdApxdaubnyjBVY24XZpXg1Bk5OceVcVENN6E6jC/2izyxOYk8LhJqXs+b3u9p3nVOuwU1azuxBoHkBJcYZo1FLBYCexMl8uIQm2tOYG4t1FGMcqqo0hEln9VKXgeXfr/Kfctuokbz+3WzttRb6PFLsrisqanGK/NAOJIkCFCSwo622J8oOdRpm2mXFZBKBctW8iqpDhUn6h7ZyKchnJWZOmyV1sT8eGrlR7/T3CIXln5tEnKosvrqdLmWOjFr8Ej3ZI9eaxkhW4Y6j5z+0CyFKdNP7LXABJifWAaldH55ZrzM3RY56Zn26hiXqNae1pgriZRK6Rt8kbQbMd6AchfjouWJQj6ZoBix7RUi2TJJT3V1YBpZoa4qd66kqmtfC/siuNduOO7iHJM3TJoeC3Fh48dpY+08dlOI595aA3wZ+9eD79ednFqtI8w3qIxzoYUdL6rESvxWtv3T9nhIRXNOpNJ8oLx6GC5yNmGECFy3V1ETho1Mkcp5bVPzXEZRjVmKO1rPPKbrfSs/FOdzKKtqtDpy7vq01ZRtgS9wFztlxVAn1+h6BEKxWV1jpZkTncQ6orJcqSvufNLp2wbjrym5naghflkdFWVoXNoQJyoqUhc8S47ijjevszRMKEknlkzP+JsyV42A7i4M75IGEK+uvjCamS/A+tqWTVGUciewfDZkaCfMt5tubR8cpYetkCqoOOvYmrqv9rqn3zrD3F5P4gEPVwIjofZ2cl7Ui8Vqip/lSAKhN9sG7SndEFLlN3TGh7nsQaoUrsCvo0VfBiW2dkXUWpLXw4BqwVSVYKHud16QKoLonRvHWyyka5fjy0ozKFQNFJpFnUlnKoVN9EMvHjRpP0mxdgFThjaLOSsxLRU0qrDVpdBTVlvHXRG85FLWsN2GYHXer88XETVDt++d9rbHL7OoWglW2JdKcVVl8WrrVVWD4qRH/Oli2Ryppvtrx3bYStZnRNrlzZJO9WyPbmaRd5EEKggLnSmObGAFwyHUMHRPniRz5seFMpNEJth4SxGfX5pzHW1yU2aFucm0CXNFM0YibfYyvZhgFdu+u1WT8Bgd6JC3PVSKFKqPAd/2gNs0K7wOF+QwIweLzeqi3LVuwSYyv1WXdXxCFdOMgy2zY4zOMmzfXCc5y9Ntw2yzABXSsjkK1pU9Co69MuOU5KlVv8ZvcoXCvSbHyE29k+yISh0LQ2/rWbZvNzPPwAOukgBBA9kWbtMDk/XXQaKj28QKsvNBuF1WhLvOKIOiZ/WQyu3RE9nDNDN3cbE702pToJRvB9CkOlUMv52QN+po5zMuCmDQF2aXc0G87xQ22fMuV/tsyMeTNaZP90vM3gVLLya49dm6irk+8wTujKE4rRjTYbdsiIsKescPIrRXl2IE29Nyo7r71NszRbTD3PONU5LZYHMhswvKVli6XKja4UVNdZj2onmJWm6Z5Rd/j7MnV2v51L2uo5xcqL2QTcg+phzzyh93enua9t7c6jcUxnexqOfJzABYn7GyS9OR2+/CUp7x81Mm5Im6wohNZJzRKlTPVlSo+oXS+kOp2p57YCSdu6S3PmCANj9da6rQYJ1gtFpbxGu85C8C7R93m4tuMWdayXYHc2+It1vl6PRsltj8ubnGdnLmlfIG9xJTftKnmV2e0KWoozlhrUKx8SeluhEsjpsP+C4QZ45MHSRxoy9DkmdDaSuK9YypWCu3cYcNVjaar9O5s88d4hDutvvBR3X5onVlTAWwK5Nphda3eulw843qbXIc8+YdG4mySuztREo6jFmeq2Iz8fdCSRnM0bWSxFZp65Y3Qa6GLoGjusV3jgdmBtwo+4fjjYvlkWT7vb+dHlUrD9ZrRyvp9ZHnEvqyYN3STJROBFrMThlSomdwa4rVmKbfJlnVLPF5u9hZGNFKMdWZ5ypfDA7a7VW/cWew23DlMEqa4VTczMKy7PK8zB3WUXY0M6cYWGEJXSkbdOrq/sHdYkC3c9GMtk5mJyXQOIY/T1F0kMhMH5qMsqxZpw03ir3ewhUj55R7WtEKe3Mx6VT65iE2MFnCamKR9miDBlKQD8d5EbfokQ+yNW76M4zHmmji8Wfby7scLDoVnM9XoBHHI0Ev+St7shqOxAKCiqbnklUyok2CyLoFRXm45jiTe8dYCIoUncVaD3xeNW5h0zqDcgw0IV+w1hoTtBaDSSxbEuMwQJ0wpsuj/JBsrq5x8sw683tPiTCTm3oDyNTYXm5mtzVxITVwnRF1Y62GaL/0j2v6xueqV5BJ36DKRpHlaWHxwSa9TGjueMMtouAX8tSYYrSICWS/Thd+GEgUviWOJ3e+Um0/q+0d58BWkyVorcVpDrs6dSPWeOod3WM3P/A6jjd7j3Cmt0OHdTTQhGwTc1S7l1DYvCcmRU4wmOJb4OOLhSFMDq3rdM3ecCLWP1kGbp8dfJriDrUjXCpkkkWHspJE+8OhXxCD7MzWw0bUCJCWW1YNYqh8vdGb9XJ1RvXGMvEVDjZBb82WGrsSFgC25F3Zrg7o2ssvJADgKs3qc38Ua63j6quUwObgOp8xyWYXhHm+1YTWO55MippxzSkCwk7pS5aeHth5oBFXMtvfPHZW8N4cY9ptffaIREcNKm5CXmbXBm2T7Bacb5vJheamksfL6Y7QEqWfDJNzQuqZqA0DcTuQkt/4cZmRpjuABJ2tWpsw3K2NDa1j3ULSkSOVxG6OOl8uHLvqWrU5HwZAHNqDcGxFfqm659YNmI6nWRwXtweChOr8M8rHsxidOgrL34yMPx2cmQc3UfRFMpviMAkyXQYukTmUtUdp3O8OqwuIbtGgoAspTS8bIiY6T4M9KUR5ckClDrXaNakL+zOlBucNqS1jWYpIjWA3l/ZS0mbWL7Vqi26bKSO1kkvvwoGj+5s7TSqu4fNDYIoYTefXha4Y8+uUCDS/yKfq6thOr06PwiDApjYJcnlhnqosWQ7qoiZksxJcn8EJRwtaQBiDvQBZGB6lrUb0uuEVM7Kgrpw7Z80TtqflqRYsF3llubVdkGLlNtHxqjnWZKMxW4bdeOk6EG9Typa9sMg3yp4SF+R8ZtKC3VYiUCjTcQ1S28+Z/a5sziJjoBs6YJhlcT0IyXXwUPXUntRIskNopsMMGNu1C1HBbqg69SNvobOKLulTCoIE97SqdKa93WxWcmBybvo5tYJJEgXstdgl18kwP1+0lTs52DpKbm4Az3ZhByza4XedbYLYqvAhX2l9mgrmoixtqiPbYauv14ENmzAvpeNs6t+Sa74nIdve6mmNDZpOt93K5btqvXGnsuzWqBQ3rRksc6HgL8ebYjpB55l5TZVYrWqMXWxRcLPSRXi6sOVGkNe5Sy9ZqTUS/qKd8Dk6zRTpevJVTyfzlce5cT+h93ztTdngEmEHX48LhmF++unl48t4YP08dv7vvYwej/3+x04fHweFby+q7ofOwPE/33V9/m/a+cvHl8qLoZWPs9g6bcPnIeV/OIn99C+98xhFPlTf37z1zdvhfuOE459AvcS539ZNNXyti7S9HxB/fHHbevzri/rr8yD85b78rGy+3t/Kw8uiiUAFv/9y3S/j30iML5WAH3+7DJ/H1h9f/Od71a8jcqAqRwye71LGg93xZcrL7/8PvXery4YmAAA= -->
