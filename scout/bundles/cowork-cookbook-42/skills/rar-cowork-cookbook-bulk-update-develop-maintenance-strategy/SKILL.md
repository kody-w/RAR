---
name: "rar-cowork-cookbook-bulk-update-develop-maintenance-strategy"
description: "Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_maintenance_strategy", "rar_sha256": "58b04c28b6d359f4bbe4bf4bfe977086e6878d376ec6261f6e31e08a35653eb2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_maintenance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-maintenance-strategy:7c7df9b159731bf7b8242e73c4a96563099930421df84e3558bf80b16c377987", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_maintenance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_maintenance_strategy_agent.py` is
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

Develop maintenance strategy Bulk Field Update — Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 58b04c28b6d359f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_maintenance_strategy_agent.py` first:

```bash
python3 bulk_update_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_maintenance_strategy_agent.py   # or on stdin
python3 bulk_update_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Bulk Field Update — Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_maintenance_strategy',
    "version": '2.0.0',
    "display_name": 'Develop maintenance strategy Bulk Field Update',
    "description": 'Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-maintenance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e5d2193b8210d84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/develop-maintenance-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-develop-maintenance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopMaintenanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMaintenanceStrategy'
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
    print(BulkUpdateDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPi2JLlX9FEf8iqJjLQvsSzZzYChIQWQAIhoLIsUvu+b4jq+u9zBURkZle9N1VtYzaEZQSSrnw57n7cr5S/PZltE+TV0+vTzjUziDeTJAzcCjIzB5rnfV7F4E8eW+AfZOdZU4VW2+RV/fT85Li1XYVFE+YZuJ0tiiR0a8iErDaJIS90EwdqC8dsXMi0q7yuIcft3CQvoNQMs8bNzMx2obqpwAp/gCrXziunhrwqT4F2KMyKtoGSsG6eoT5sAsiphs9Vm0FF5Xah20OW6+WVC4xK07B5Afa4FzMtErd+ev3l1+enEHx/ev3tyU7MGpx6mgGr9Js5i7sZyjcrdg8jgJDEzHywuhgAKhk4LtwKqEnBKcf1oMfRT7WbeM/Qf/5n3JuVX//8+iWDHp8vT+OPBuxsAhdqcrNuXAeyzcK0wiRshheITXpzqIG/TVtlI14AgjDzX+53fpMEgPrneO2nu5IX321++vKUAxPMEfIvTz9DeQX0AUzA95dRSvHTzy9J3rvVTz9/k1O3VuTazSgMWP3y9jh+iAULvy0NvZvWfwKp9+Ba7pen75wbP3e7Rz/BnU8vUR5mP90FF1Xe3fH86ed/JdYOXDseg/qX5P5yFxy4pgN8ehj+8/MN5F+hycOhD5n/Wm0Bwvp3PAHL39U9Qw+g/pXsG/7/TXQSZqAU3hH/U3F/dsPkn9Av/9K3f3fDM+R9eVq4SdiB7LAS9xX67W235ea/fHK+nfz06+9A9P9VzC5vK/sm4S01s9Bz6+bt7ZdP9e30p19/+dQWINdcM31rq+TPZP4Zrjc9PyD4WPXTj/cC/XoWZ3mfQR+ZDv2WF/+r+v0FOphJ6Hw7X79C39fL+JlAoxPvSu8QfFczNbD1Oxx/fvod8EQGvGnt22VQ5f/xH5ASjnSVew20s3PAQSDATZi6o/H7IKyh/aOov+6klSy/pM5XCJwdyx1QhNkmDcRXZpgAosrHiI8e5B709X/bNzr9bD/odDry5NudId8e1Pj2HTW+vVPj1xdoHwD1eRX6YWYmkMZut5Dpu1kzKr6lSN2mn7tRN7ArvHOPNl+NvFO3ifsP6OtfVfZ2k/tSDKNTXzIQJbAICG3ctMgrswqTATJvLD807mdAuYBZqjxJLNOOofFXW7yMSBmBmz3wswGbuxfXbkEnSHIbOOCFgKafQQrUedIBlhxRreMwSSAnBH0A9Jfh1oAA8q+jsK9fv1pmHXzJ7rSMQffGU0/Bgg+Doc+fQWvwktAPmi+Zawc59Om33z9B/wX9u7tuwkcdW9AmbriB1E4gcbdZQ6BO2xQsq6ExSQAJ3eL42+/3gIzWZaBTguoKvbHzNWOQvkuK0YN7lN5DBHweTXSrh6YfcYP6AOAChQ1AC1R8/fwlG0XkYGnVh7X7DuL95jv07zG/6xljUj8wBHG6tdJx7S0fx2COLfYFWnnQB1LAXRDXZoxokNcNSOHCzRw3swdwp9l8C2GWN1ANqqj2hmeorYGro+SvFhA9gpMCqjKbr5Ay34Kulyfg1wjQTT24O8/CMfCPpL2fBkKqTyDHZu8iXqA1yMwKKszKLILKrN3bOs+8ZwTodu/3A+EmlIEhYOzy7hijW33fMm/x76aMcQqAlrfZ5D4MQF9aFEZw6P/z+DIazvK8xvHsnltA3Hqvne5ZNg5do9P3OQ1MEBC4714y36aKdwJ6p+YvWRKCyFTDP+4rvVti3dfc6a6tQNZorHaTP5Z4dZMLTIFWY7yr6obGl+y9BzwDaEBw6pHOQBXHIyfkHwrHq++WBqBUx+Nv88ADnbEiQE5DRWsloQ15ruvc0r8JqrG4HpEAueKOhQaqwQ5+8AoC0kEeAPkQMCIESQv6xA26NSgSMEPd0f9YHo5TFrDCaW1gLagi9wUyxqQGcahBAMCoNK4BKHy6iYJSF2AMTPxAuA7M4m7MOAg/DDTHWOTpmBnfReBxESTo2GyAvo/qA1JNkEcAyx4EARTX5R7ZDzsfsQLGjql1j9KP4X74Cn3frP4xViCw8VsjALP72Oe/AwfQdpXWNyYCHTiuQY2n7iOBQCbcWvrLvSvf2/6HLa9/mP5/+nsbhFuf1X+M3CsUNE1Rv06n91743gpfQBVMQY6EhVvf2uLne+V9fpTc5+9K7vN7yf0g/w7XK/T3bPxBxCO5XyHkBX6Bx0tyaLtj9j4+AJL559npMz5e/ZJp7rdYPxJi5DjAu9bw0Wrel4B+41euPy6+t5567Fg9aJI3xru1jo98eFQLINTMH/tknX9XxaNPY3TvwftgZnApGznfGac93x33Q8lofu0+vWZtkjw/ZWbq/vV90MjBIHEBJuMmChQRmKGa0L0dfcxT48GPu8BbeQFecPLXscpAvwOz7zP0McY+Q+8bi9uOLWvBzuqXcYQeVYKl4M/H2o8tpuU+gQ1dMxSj/ffd0ji5PSbqPxoxFhew2HbHjp5/VOuo8Q9CwBffd6s/CtncvpjJgzLqxhy7JGjOj0KvgZ0OmK2eIQAjKEBQU4AqW3DDH9UAPZVbtqAvO6O73/D75lZ+9+X3GwzNfcv529M7dYzf70PCPXvADX97oBuhfW/Eb6MCcxRzG7tuSN9G1zfgZTg23O8u+eP08HZPyqdXwD/u89OIZxWCefx6228/3a0C7nwbeoEEwCSf63GAmIKaApJAWy9GV2LAgt8pGE+Hzm39+OX1Tyflv0IJr5RNOR5jIQRDYYjlURaN4qhLYTZuMiRBYjDDMBiMo4jj0biLEQRteTRsIaSNURRDU8CYMa6p+TBmiowRAW58wP4/nuKf7nJAR0EJEggCqmHcRmmLdDCC8XDLcnEL/PFchqJgmnRJmqIdjCJdm0RJxCNdDHFh2sQIksBcCx3lPebHu3Fv77P6e4zuDPF2nzCARtQ0bdqmENxhKJO0XQy2MNtFABgU5sIEg3k07eLg/o9bH3Eaw3j3f8xkMMCAwa0b9fz2iPuYnSQOVgp4vWLvn/mUOZgkSllaYE0q0j2dj9OVlR1EOLO0g2PKm5zcL5x57J+RVrf8+WbQBLhR9WBiqIdqx/t7gsuo2bZuaEKhhpVeDHFIG6F/6ORMjK9nmko2DH2W/HDeH9ZIjkj7kDrqhhkPqX2QUFlSi0PRXs5K2WnWtuHyPX1AXVzM8KnjeRc+dQukOK/0A4f3wCVmwCO2iSo9amOkzNHZTlyeunm1OioBMKAMdkXTHlaWsCO4OL0ImnMQO3GOGSHCnZdmykkiKl2PbdErs9LbZsjE3l4Zxp4SeiYzpD0VFpp8OcP7WXNQi3Oya/aksKpqrtQlFFnKgnImzzsXN+ldTNY2GYaEUKqklO4untuncrYryTA96cohOZgBdxQvbi2Ethbo9TIrV8tB55a9YZ2quZEe8HyTr/Q1WfZoqoZrj0MOhZuiJ4I3r8gRLqmcovp+zRDcNZL63V5m6aGQnF1v7EJDi6RJwA1qTK2AUVx5CpywduSruTlNWIIX5drXdXh+mFh76USJx9nEkpIai6/8zm6W2/O2DAKySnaB2MpUsuuXFc8ETKPVJktutqg2O5WIj6J7lV+b7XmDw4qtI+VgidP0vK6d+WWTw/XyNAgEnux9kAubVdrHJ2VdiXhCltj1LG08pyf1gpsNVpMg1ZUODlGD9e4VpU8zJIbbQcnq6d7QuQt1MjhTL5HipER7dDCHxjiXCN0pi2sRFuHMrEXbjj0ePqR4fe11e6K0J6rPriF5YKOAYIJ5j+F1vZ8shSWVz/lTQS2WsVd5VUkkp8Q4tGdmXVxB7nQoOXdFOlxlu5YS1cFyL4O1GfYmcxGrjHeOS+xyTVZX+siZTnjEVZEUA0IR4t4+TXRLCH35MMUV4lqft14QTH1bmAVGzlD8mo0nKbZqcom/2KQ8QeEskCXCEtUdkdt1ua3FNR1mEa/s7Vj2h5PkLS1OIuIm0bDZ9ozEhbtRdQLb4pu6Vkij55VCskQkD5fdPOn53grmvHMu+Xzva02vkBq/iJbuqkpXqR8L8eScGelG4Hq73ZyP81ZZVAw6DbLjIpWyQMGL/OhIqLCUjEWTkOyBsAmp1kCMJ1kaWmdKsg5Bxwj8CeMC7VoHk2BKX3eNY7Y7Ng72eLvYdEhxuJiVjJtsQJeSbK8rPa42rdaLq7N2VgVg7YmttXBKavGk6ra7aG9N8j2TTLk2mV8MQwx3Mk83W9KNlkZ4NK+kNE2o+QwbhDPYQpNNK2TeFB4OnD7JhG55iqS9ZJ3hRiFNrVt6UpypS+Js0p4gyonBi1ODUyuOXCf78+KM9FjnXw70Yi6vLIwUsn59OiZrUTQuA3FkoynCTXmy1OA9fVY6eeHbcLmn5ztC6AKNYAHVhgSFUcZ2s0Z32yVl8rK0P+5DrkbLPb9olYseGpMgDQt9sK9ltA/ndWguhXKGt/0QFoo2VLVi44IqLga3G+JybVQCtr2oIk2oGyRGMZE5EnDceT6lVKtSFxt8Ua+RZXNE5ilylo3ODUqhUYdth02ToN9SwXqGqK4Tz5ciqXMIY51L3yrZiRKrveIvMj9VTwZf0umhx3KUXZ7WK0+aI8YUX0hyQnE9PdGXPgdTHTpXbXVgvE6M+wBEcSN6gMWyHaVetRntz8CeT01TaZ1sY2yIvfUcCRV5Bue4yOrZKjptQq3RadLiWnq1q+G+51VTP2nnme8bKXaR94p/Pl5D2BfVeX7uk9Ja7XddR1bCIqw3W048aTq377ZsTRpCjabna7fJdLMIzTOMtDEm09TmiKBuDPu9bCjItaqYEyKKWph5aT3UzKDa8zlOMvLO3U6zM1tT7SannJnaboTukNBtFGBXcttlFUxzwoBo9kTfDmGuLL1jl6KEyLKHmt8k671KFIlS7eQVsmqXUVnr+sKzLoyj511lsJozB7yBz/alHB8PhzhZL+Dsmq8uyz5Krvpaamd4xPsud1EpZe7aC7qO5lkTb0pOmyYX0z4hQ01THJm6Hb9110ue3S8MAynLYWdVRafFxJl2duLqgKha1LK122eHZWvDpN3EK8Q4X2U7Pixm1J60hR27ZTsKNVqnyPYrFOWUhMiQWGplXhF57jxlpjxa66lroFVxbJjQCi/EmQ/w1elUc42ZxavYNLEJ4ExCOHETnuDUZrY+tl6wSOLFEskvy4vSm7PYOKTu0Q6Whu71ItOn/mJzyGeXyiX9hRQecgHxk3IpBgPGK7WwpqeEIy0P3TwMOLUYCEY/6egi3u1Q9lJvs/WSW9BWX8z0iSpJbHkqZsNiZcWzkA1wnrionTYvK3lJEK4336gHTHLUfHCTxAj359DoNk5phYqv72fD1um6ZmpX3EUy4DCWIquPq8jnrk47oZnVcBaJTN07p9SjFGQ77etLexRb/qLo1ZHQLffKe26ZFGWS6mx37hxBL7k6JXiQwdyiipoTzm0Kyl3txHmFrffJZiVu92Ui9pslrBQyra2Ys1mpzh6/quvjNY/ZqC8ke8Xky7o3d7EAh4uFnuuB7xpnvcXnrD5JuAVue81xWwj6cIJZeHC9Ft6um2AKZ6bp45ycNSs2mCyGJs4a5kxtCtka1mJOM1t4umemeNhLfEyq5VJRHVKcMRKe+egmVTUCTjfrIiQd7yg24CuyRU9tAEvVpWGoIvZ3+FlRVyFTloyuzbnLgZ31WdlsF55zCOPMn8IBF6wj3q6882zmdhE+zYdzLrFt3walRbakYxdHMYu3sk2qSbXky2xFVlx/FFqmNoqlmrkNt4Vlgz1KoW7k0a7QyiPC2z4Xsac+sxPrusd5G4FjsV0JwnINx3Ztb/h0VfuX7fVw6H1xU1reKj5d4AYX4d1Cm+rpRIsHEiudOMvOB0vdEra+zeXzJXT3YdEWvL5ZrEhHBxkpLovdJt6KC0VzJsLqcjovuMtKT7UYN9g6DfnS2ZHhtbD5HaJfJEtRN4WBMPXFQHeWgq/6gZkNnAOjC96CC2ZPsGf6BDfZEkwfZRUEu8OpU4iYDOmAP06QGCPtq3pEWzIjOYz1GmEbSZXA1c1RtvHjwuO38SCpLeFUx8UBXJVCqnBXA7qPKufc6Jc+6gid4WGLyohESqcaK+LL4XBZz1wRBQxnzzW1v7D4bjbPGFyTAO3G/JAqrYAbqRIlfZOxgiolLshEhOEDwrweK4aLdtVhaUZnehVJsIHRsysBWgUVNZzp8nwyGejSUsWdLtKJj7Cg1aW1XaxmQxyfzUU1X0wTOyayS+GGhhSe6LyGW3GpRoeudvUlFovrMhgkPI/xq3eei9f1mpLY6MJbShy3k269OgsLNsTpHK+a82HX7EQGw4uK0H106xVoq5YYcVklxAFJusr3m0aOtHlISLNhmXBBHRzyFJ8VB6yPfNrBtYhCSE/XK/akeBR/RDB9uDIXAGOxU+YK3RVisdH4o7fo9vJ2j+wpZImhrXYwtCCZzkQ7YsGccYjM4gy7pJdzja7NDMIidWbQYjg8bvfaYG7nR6mtZ2GC8ixx2lxnO2LD6dNlfPEqRVou1jHOaPEObjPMpjHdFg6SCtoquRAOFiH3TjYDNGrsZNBrjyJ3ZLe76qQcM9QPNkF4cDPqtKeM4ASfNB/GmIgr4Yr0/HCDo8OadjqjF/HymAWw08CecViz4dwoThVVblJ5bWLbFDtiZatw1DgvhNgGM0iD3AgCKcf2dt7OM5LSmWm1o5LUZ4TW3jBSdewuDqVTm82kw+SEJwesjrbHo3JclWCCdFrPyS9lxsIBGp0MW8in8Nle1EOB7Y/bym4ClnEK5lDv9wLLrjp8pwwKniXceRZNLXzGiHxxIq4zw7COk5YTVboHY/YlDFFc6guaZGaG6OlJfWXCPQNrBZhsNxR7tdAExcUj2SPLFqdqajtUPraaN5ttFNpU7RKhdXVOUe+67XQ6QckpzmqJDDYx5HZK61sCU5iEwqLthfQpSnIiyQYYIjE7aWBE8AlSus69kEwXJK7l/TS33ZV/IeWOWBaa67PFBSZwba1scXl1wsSOm122gzglYE/YKBXSS6hDyb5VH+JjqvkuE1xbtTmsBl/fOq11TQVXP0V6fFnDsiSvJMCPe0/JNhOyFtCpRLXLszidbRFmCfNMuFjSXu6xBHrAjqcjfbFLSl6hAVtdkZmM0Su3pRZar6AGOyGJVi4K1A6VszAhzGh6PBilN2k8pr+IkZQZEzwyWDMcZjg93eE41XSbqzs5hdasQtBaiDiD9nlsmToZjmYN0aUM2EMyqH+2MXJ2Fa5Oz0RMlyhov9dXc691jOtpjk84xJXVVWBlq9DRNjTWnSICn2HykbEZUVXtVNkOzBrhsJmE0ZmMDLJC71iPV0gap0uBvc48FWyE0AUAgmbr4YwnmGDY3oal9Yo79mkVCkvsOJymR78310JMZ5wHNpMcn6bdGpmkdruYs/iqvma4yEXW5rKu4WYdYD59QKqJpQsHhGSUHYh9uVlhRZOLnicnaTPZUNKVOzYUj9lgjwY2T9dUmVCqk9LhOo1UzlDodZVwHsUMQj89si61rjLH2Hs1FzjzTNpYmL+fKv4sulyRiNEwHLd3aYOxWiYfO8ZL0BNzxisZEX1BnFlMoqHwCZtfS4cxKakyMtOgwKBzXSmOS8L8imwdX2L4fa8Skc7ONA8+gPZ8YVCXny3ZyT4iUDeqy9ly8BYXfE/KdTrJl52b9c66auxVg6t8iMmU2NMykrQMraaLo9y2E4NKkGM3zY+dF/TXqXtkIn1LCvq6I62gJKdOxSz6vdoiNd+Si4mGKRvKIK8ctqGayWJKyTK2ViadNAmcBpePyEWl/ZWruyc/jVgdXR9cdJp29PmiSBXKmZvAnFChjHvdbspnuRH76WwXdyExmbSJq+o76tAwU0GuyC0HY3baMsauxxDhst4tQTLZcjy5Dn5Pco4AzxfwQZrvjBy9iDElrEuttCoXaXdDVXkOJR2bfVtM5OWK6cHeug3oa0Y6mxPrClE/kUy0mk8mqnP2SXZm4moW4vDMtfpzrB22yawTI53ZZGuQfxmur9N2fyxUOGrOA81fMWV9WdbCnmlNkKJU6+wi9nwku9nWdcok9lJkIBctmAsX7hQD6dehSrWd8PkCp86ObuVwvKvbxZE49rlaZlPxMPca+9pVJ53EBMHfwBy+IUqUyRWNhVF4xe4b5qJGk3kXV6oh5Jl99i7XiMy3rYnDqYPYSCsO5DTyvSm7I9bDpqUklWWfnp9u736fXhGYpLHnp/FVweOB///kQbF/DYu3h0SMwujnp/93zy3vzxDfXw3eHv+7pvN60/7694399fmpskNg2P0Rc520/uOR5X97Uvv5rz5FHqUM91fa4xvNS/P+BqUx/dvD7jBzWrB4eKvzpL096gbwt/X4X1zqt8eLh6ebk2nR3K59OAWOTPv2JuCtyd+csC7yejw5WlGlrhPe14yH/uMdwfOTM4BQhnb9hpHEm1sVo8+Pt1XjY93xddXT7/8HjDkSDsonAAA= -->
