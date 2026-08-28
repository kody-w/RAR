---
name: "rar-cowork-cookbook-dashboard-correct-production-processes"
description: "Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_production_processes", "rar_sha256": "e850c0e2b2cd2aa36b9e3bb0a0d289d04961ec5bc5f62b154de36a7a3f5cb7a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_production_processes`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_production_processes_agent.py` and in the RCI capsule.

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

Correct production processes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 e850c0e2b2cd2aa3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_production_processes_agent.py` first:

```bash
python3 dashboard_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_production_processes_agent.py   # or on stdin
python3 dashboard_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_production_processes',
    "version": '2.0.1',
    "display_name": 'Correct production processes Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6df2df1b57822181',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCorrectProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectProductionProcesses'
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
    print(DashboardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSNLmX2Hz/VDVL1UpxClqbMxWgIQuQOISoqutivu+L6He/u8bSMqs7umZ2em1/bAqq0wQER7uj7s/7hHkry9W14ZF/fLlRfGsHOKtNI1Cr4as3IXYYijqBPwqEhv8h5wib+vI7tqibl4+vbhe49RR2UZFDqYf68LtHK+BLKjxUv/zNNiKcs+Forz1astpo96DNqpwgFyrCe3Cql3IL2ogta49p4XKu4BJ2nQJJDVA2GeoKL28ATKARiNk18XQePUnKC8gDiMJyHKmgVDueS5YyR6hNvSgPvIGr34FKnpXKytTr3n58vMvn14icP3y5dcXJ7Ua8NUL96YH+1Dh+K7B8U0BICO18gAMLkeAUw7uS68GamfgK9fzoefdx8nmT9B//3cyWHXQ/PTlaw49P19fpn9yl991awuraYGqjlVadpRG7fgKLdPBGhuo9tquzu8AApjz4PUx84ekooT+Pj37+FjkNfDaj19fAEC1NSn99eUnCOD59aXupuvXSUr58afXtABofPzph5yms+MJ8b/fPfX67Xn/FAsG/hga+fdV/w6kPtxte19ffmfc9HnoPdkJZr68xkWUf3wIBn7svdzKHe/jT/9KrBN6TpJGTfsfyf35ITj0LBfY9FT8p093kH+B4KdB7zL/9bIlcOtfsQQMf1vuE/QE6l/JvuP/D6JTkArNO+L/VNw/mwD/Hfr5X9r27yZ8gvyvL5yXgqSrLTv1vkC/flOOK/bnD+6PLz/88hsQ/X8UoxRd7dwlfMusPPK9pv327ecPzf3rD7/8/KErQax5Vvatq9N/JvOf4Xpf5w8IPkd9/ONcsL6WJ3kx5NB7pEO/FuX/qH97hXQrjdwf3zdfoN/ny/SBocmIt0UfEPwuZxqg6+9w/OnlN0ATObDmwQMTS/zXf0FC5NRFU/gtpDhF10LAwW2UeZPyahgBdmruuV17ANcmAsA+x4H4nzw8aVz40Pf/6dwJFVDjg1Bn70T47UmC336Q4Ld3Evz+CqlAelFHQZRbKSQvj8evuRV4eTutXNYeoMT+Tn+t9xmw0efpYqLM7//ZAt/usl7L8fud9qMHU8nsdmKppku918nSc+jlT7scUCm8q+d0YJm0cIBOfgRY9hNAoClSQPPthEqTRGkKudG0blGPd9kAuS+TsO/fv9tAt6/5g1Yx6FFKmhkY8K4O9PkzMM5PoyBsv+aeExbQh19/+wD9L+jfzboLn9Y4ApZ/+gVouFMkEQJ51mVg2FRQAA1b7t0vv/72hBiIyUHtA16M/Mh7TAZxmnjuG97KZvkZJUjI9gDOAOOsLOoWcDUUta/Q1ofe9QWLTo8mNg+LpoVcD9Qx18udqURZwJx3JPOihRoQjI0/foK6xruv+t2urbuKGUh4q/0OCewR1I4iBT8mNe+DwOQijwD879Hw+B4IqT80EPMm4hUSp8iESqu2yrC2nmv41sMvoGa8TQfCLVBMh6/5VCu9Cap7mjzgAYMAMs7TpZ8nn4PqnQFOcJu3te9jrKnCqfdKV3/Nm2cKWPXkCgeUBLBo0EXuVBj+9gypJiy61L3jBzS9V/GHF9ynV+4xyP67XmH7j33Ge32HvnYoMseh//96lMmoJc/LK36prjhoJary5QH2pNvklEd/BvqEuyL3xPrRO7wxzxsBf83TCEROPf7tMfLuoueYB6l1NdBBXsrQm+31Xe49fKdwrOsp8K2v+RvTfwJg3WkN2AxyHeTCFIJvC05P3zQNAWTT/Y+qf3c3gBAECAhRqOzsFISPD4CwLScBWtVTCj6dA2LZm9JxCCMn/INVEJAOQgbIh4ASEUgqUA3u0IkFMBNkn18X2Y/h0dRLPVwFtAXdrPcKnUEWTZHUgNQFDdE0BqDw4S4KyjyAMVDxHeEmtMqHMlMD/FTQmnxRZCC4f++B58MfcX/XZVIfSLVcqwVYDhMbu9714dl3PZ++AspmU6beJ/3R3U9bod+XpL99ze86vhcAQADpVM1/Bw4Eojlr7ow78VcDOCjzngEEIuFeuF8ftfdR3N91+fKnrv/jX9sY3Kup9kfPfYHCti2bL7PZowK+FcBXwB4zECNR6TU/iuHnZ7Z9/pFtn9+z7Q/SH2B9gf6ahn8Q8QztL9D8FXlFpkeHyPGm2H1+ACDsZ+byGZ+efs1l74enn+EwMXA6Ton9Vo7ehoCaFNReMA1+lKdmqmoDKKR3Pga++Jq/R8MzVwDd58FUS5vidzl8r8vAtw/XvZcN8Chvwdru1NEF3rTlSSf1G+/lS96l6aeX3Mq8/3irMxUIELUAkmmbBDAHbVIbefe795Zpuvnj1u+eW4AU3OLLlGKfoKm9/QS9d6qfoLe9w31Plndg8/Tz1CVPS4Kh4Nf72Pd9pe29gC1bO5aT+o8N0dScPZvmPysxZdYzSiZd3lJ1WvFPQsBFEHj1n4VI9wsrffJF01pTCY/atyxvgJ4uaIg+QcCBIPtAQgGe7MCEPy8D1qm9qgO10p3M/YHfD7OKhy2/3WFoH7vKX1/eeOPpg2cHCYaDBP3cTNVyBoIVLAjuH2EFnv1f9pZPKYDvQFcDxHgLAnEQD7VRx0UtCyNt2sNsG7EQF13QLoLT5NxzCNshfBK15wTuehhpURbmE45NWXMg7xGi36bGIJo08xDfw+g5EIiRKEHg9JxCLdq1cMqyXGSxoBDKd0FJ+DE1AWT5NPdh3oTle5s7wfK0+tcXm8TByA3ebJePDzujdYs6U7Yc2nRNehfTmG3t6FyNZ5IK7Z0335wdccWqTEKg0WKrdytx3K3momMGJlJQZ0FkNyRzRBXfdmBlWSo5rxxC+8JkeOugdocdEh9YQemMvC5uUto6YaVnmS7Ok1bXEl9AeUGQrub51IsLX7YanvaPM1g6emaWK1XnzGz7QMFjil1EIl9n8oF3zKpqOuW6vnXycHHxzmBrsekbNFd3euTulkx3TNNKtzA5CnfkVaOOvN/PRnZxGbIm3W83XJee51bP2N0ZB+73uBPp+zWC97eS9PrbFb4trl532KBHlG+kJFPC+lq2ZG0rTTu3RC9CxBGL19o8Pwmz67op6/18XQ83KzpVnknCi1A0hJIN2eyyPCA2d9I6NaIv0iFCL5nmNqgzZ/imHdUo5pRZqpUhuUxEl0Wxot8a+7pmSb2boyJTI4YgOjQHsi6a743MYofzck90YnpsDrddNE+upTWcnOq2h4MV6+BlqRRrDWnRhrBNr3MW3O4wT7PTbc8y9exQlBd7a7CdU+voWM4ty453YoXLw+roumxExHQjXebIgDoJXrKYu3Q2G7phbF4MeOymndtLA1s6gqjlnmys3ayrOYteY3CBNOF22JRUrga5wnc7/JY1cFds9HE+LlyTaIBXpcDc2plIEqbr0bNCvlDusG6IdrMlG9sgeL32vUNQuYPNO3LYci7PbRE6inpu3dWxz12XDVzLmcPq2bFJfeyyj3e5uSg8WhvL6qrOGks0gtJv9rZ1anawLu2uLNc6Y6hniHSxBR++kVZDnV0dNeHzeEYvZ9O4urkVi5wshPtsndnnueTrtNDVpNka/Xkt3XoRdfxyTvjBgMXSplH8K0HHBNeZ7KlUZ8OMl3YtvICPyOEaOMYllvobzu6YFFbotBYitEabG5tulV5Pq8ba7CLsrEZW0RbXeInuZFhAw3iQTL717EQxg0NOr/d6nAidK5NcuWiVuXMNqv14dU9Eg0QtLgTbfVxukx2fKQ0johK542TWtLdUFUmXBqnJqtTPHr9CHFWcU2PscAXM93l+TgcV9pTroUlIfVRaFje928bLWLXcOjdiy92OpZXs+wRjxXqhVvP2OrS5Zc+MWUgTjCZ7XikdN8w5vBgzSQcd+UEw2Phkhc2KlPZheHJVOsDt01WytNuwvGHcFZnrCOktmmvhramrYHVndwdHcuvMeYLZMnxPeNszSS82w8Fc5MKOC+ttfpobeeQKzdXf22iqzYxzy1UzS43Ci747XDRYYsQFsjPJFatXC8s6nXfhJhXleYcYhU43pOyRwZzmbmSW7eZpvo0Fwl0m5oxkZb0xECKiI9q3iJ2zzf3KH9dlslJIpGW6dqBIcdMmyXVZEhe93S5BhM4F2zX9EuVXpOwTiX7lRNNbJyUIeyc42IbQphu/QZprsid0zOrksNBO3NGAW149FFfxBsudetTUrhJp2J2TtqBKgZuJdRVEvhvYOS03KxDpmbkmb7gQLeG9d5xJG9xHmZtf4pdxTflkEvScLXHNmuDwQY0PiRZSo1KQLKd6Kr9wQzFkjJjdjENU+0jYrsY2MWHY3ITJvNEzp2pnm9tMzGuU21eaqLeECVdNG0srIw+MU1EuOU7mSfXQ46sgUMyLYF/R85bhtGwZnRMBz2qLbK+GvzD1pbRimnO6wlaRIPK7sWoTRcilzFwO6RY5xbEQwatIydNhnodDvjmGSrO19EMtBYJ2xpJTRmBtt7HO66hyET3NsRtCSdjsSpbXVZAH5RbbnCkPVpV4V81SS7dqIcc1pkCsdX4xqEUz8Brma043NNqaXftE021gf8fAje73WI0vhLVRnDlC1leHDrNTlK54ZrPcu5WyCmPzCLJjNVi6c8iM83rLErBKouvwlkpL2VlWWEYtjctBu6CqNpdULb7ldbCPlLA8Fz2nwdyQbrhLoA6pTO71qkEvZHAMYUo+IzjXRzTe7KP9ZtcA8tsxrO6jgFJXO6zYLBusU51sTSsLXgs3YO8R0FUcwn1LGGK+x8f2nDoLo2xD3Nr7ynI8MTK8g839OtDchWE5gz6vBMrUw8s8zFvFm0lGvFvgyWCNRouK3VXNWosgA0tSCuWgtYaljjOdxDOKoeRVrJAJdj2GyUFhMqoRQN5qiFBUq6tb29l4K1fU6KEXnDWtlj3Haq5xouZsmKWW3FAZbVWVYzd5dYRtuQta/CTL6ZwbkeDibvxVPATbmKgoHPc8frEXTn3ORs4q2/tDMOKc1jSNEBTSYO6xUDWzpucGvte2i+p8Yc2+qmyDLVD2KufXlEhP+3WBpw2BYbVXr3XmjLHJXrWHJBtBTT84rbUvce4sd4RctyyW2Bs6G2E+6ImERwgWtyW0ds5Nr5C8pxBVlcZaTIcm4gJYOjuxY+1ykmq3PpgmyHs83q6u3b7SazpAaKnS8u1sha7mwCeRALP4iqe3CVuURB1b1ErJ9xLJ2ML5Fu+v5jaNTqe5Um7jbUUMq2W9KLdGj6N4N7OEUnCQZW25PowLLVXSiOq5BbHd53qzDLrDrdYHt604qbSsqip4yz8eVa4FTcjMBKlvVwvkdIi4GORk1a4caUBGQvSOxLVrfLUGZNOXN+dGLowVaSm07TuWWVg8r67YZW9F3fwahIJ4Wjpb3rCxtseRk1rYc2bR6mGmFb6/KjzfGGfbgSzijXHZCEyabGOVSivFpLgxl5KddZUjvJL2mMBcqe6wJmXtgFV20lxEA69YqY+t0izaEqGX22w5hBJsGUg/CGWxK+leKlc7J5kpu7UdItp1k2RruNjVDqg4Ky4b6p2yRXZIxBt0KeIRcUU6bU4f4aTBloeRIA5KT8/kZFtg2DruWJRwNakjt0mpSMjxuipONM2h11BLBWNVRnh2ClfsWNnkPhBLQZLnF2pn86kpwyG3MM8y551KGPSbx2slK4jKxd287NXc3GnsnI4V1Ez3iK67ZyTl66T0pG0/6OmsNEU4F5A1vdO2/qkjObfatJY8twd+RBtq417g6rAT3QWOVhvL3fvauS88xmxzQyHRZXG95P5YkrsSowFlMj58BARXn/vIHHGlUfI1vlXCG7sbEpaRKCLaM2QVi/peQZt9Kbirs8g7nDsEGpVns/0o0uPl2tHLHVwbLSl1/PaUnLE1qnL8OK+VYJ1U5xhYum9uQbEUpSA4nBzxBOhMd9PGkpNYKQxhDyK6OjuEbp9TC9uAstSuJEaJBbVp6WHLxYa05Y4ygQq3EaNrT2sShSjRE+kyZ5Hosu16l9AYJdXDKdaO/g7lrahX1PDQuSzX16dAF+voxIbI3o1SfW8KJ2TLX4RyPrNH5jK7xtwtS2DnSi4rHMa2vYVI1a2de6uxZAT2uOg8c72xRYOO9pnhRXWGhYd2ABug0xLwuSotcIGh0IXGUufIupVMS54lpg2z9Ign5qDscX5/UEuichVjv1xtzhc1DBx+WY2CsM4O/EDyV73YBSF/9SqDSUjKwNHmZHWHLFjqMuxWM45mFqRU5vN8qd12LOMq0Yxbzwt+o5LCqr8kxfG4snft4bIwKe2UpLgcGBfd6dGhAZlFzRvEu6bbDb0xNGNuqvt9EXF73SN255noiIojsBaGF9JtTXd1c1lvurW3hpcyMQu2VIzYXbWA5xJ1IjGbxBajRw340Wr8hQgqSAfMo5xOCeyDNIqc65pgf7VVD+ItpXlJm/HJiMipIc9FOvOXpBOBLgpLsY09HDcXVz80c/myXKuIvKm7i3aThajrwxlLF+o64mymXhXZAtsExljQF3x/PsbtsCGOudEz/pxW9GGG7o6YB+dMUFANJ/YXw7Iz+gD2NMeNnNmw7q6JpViGC/d660Iq2/XiPALRRBqzmV0fZgGDKNWA9MFsdl3OekdFjd5tYLjgj+ax3KmRjLJ9sGmrqFjER9l1lNHej5TWJ1l0o1h/zq0D5ALHWs8H240kYVv2srjOTkEULzJaM05OcoPrApZc0ziUekNhxvJ2sg21lBOPC2/dtpUvixA5up19y44gutelGNmFop01c3ZCeLi1brgTcFZE9ScGlmcxblOHShpG9oDjAWB/wndp2RjXo903scKLXFyyYA95ok2MvwUXoV1Hx/hkqGpDXCz0SEfzDbzoxpVP2zMqjK+HMcrgJj4vrWhkCBRO58jxoLgZvbit0I1Rt47Eb9tLYJ91QPHnOU0dIgyNuzxnGJ3yqo3jiNgRO/KkcaMYUV6uYSK1j8VgUPEa6bYLs3OUQ73bVCKpaY3c0ZdZfECiKzNctqS+g+nITXphbDp9tZhdtwxysef5Ojkt1iMGtnzelaEWSzwyEJWIbte6OzZL2GMAcQlGeLgt9jvJzwp4NruFwy2SsJNXLckMCQ++z9L9OOy33JAMazHI93SDr6LBIQ9bK7z0Rr+bK4WdiGe8c325ckxMUy86PHaJhxFUuW1RHvRf5m2uNTcxZqyDn7LoYe6j/I6TVmuSOgr72WIeNyHcFvPRwiS4531vx0YbETmacXCYJVc3HoZ5yzIbhGiYoDMQPcfglvIM4WrH2Blj1suOj0Czn9aJm/C9RRN6p4qii0uYhWiHE4VR+6DdpLeOwQLcY4/C8iSu1r4lMUZmYjvkstI4ij+OrbmpdTYu6A2FZJqvC3Rxcy55glKbMy5zQ9xSnaZxNcjjo3dYHkX07MMiYmM1eASLRXCkseuM1LlbtKY4VHR6Oi1rmmhGOrTWfBuImG+Y7th3ctfJtqGjM5miU3pmRlt/7AvfptY16Qd2vPf3krA05ABcRBIh3Ta0jaOMRikir9C+U+r4GqP9hkOO6olblspm7s6Oqtpf9ls7whw/HMl5PLR2H5+9w/FiD2d8jzDVothudQ+7BQy5cfNhyWnmhgV4YzKTU/m6kEmT7U9YIrSq7fe24kZeuEH6dXBYruTeVUn/qLHeLVwc14xznoveDl4Mi4Fp+GUd7p2DfVkRPZPK6WmmocTeWpoIsd8Jgr8PG4YQvPQoS/P8MByO7pDzBtIdep3asjOf1nbOOnf2izXtngv4yloGiNP1sRlaqvaC1IVvqUkP4lLdLKoicfkkTlu0IpOFFUqV3+8YgqZvAkOABmvwvCWmqAUIlMMYXJP8ZJ4aRsLGM9vD0alJBoW6qdT60sUclbXSheC02rNzO0akkKKZ0V7YNknvT8vly6eX6RT6eZb8F18qT+d6/8+OFx8ngW/vl+7HyJ7lfrmv9eWvKvbLp5faiYBaj+PUJu2C57HjPxymfv7P3k1MMsbHO9vpldi1fTuEb61g+hOklyh3u6atx29NkXb3Q91PL3bXTH8J0bwp+HI3MCvvJ+Fvyz4Pyr+1xdMk72X6O4XpLY/nRlb7dhs8j5jB1BF4K3KabxhJfPPqcjL2+a4D2Ii+Iq8AzP8Nrd8ouP4lAAA= -->
