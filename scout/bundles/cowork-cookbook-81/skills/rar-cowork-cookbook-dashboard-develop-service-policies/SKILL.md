---
name: "rar-cowork-cookbook-dashboard-develop-service-policies"
description: "Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_service_policies", "rar_sha256": "ecfc750ef31aac30fff2fe352eda8d833e3745292f5539797cf454b66e30d557", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_service_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_service_policies_agent.py` and in the RCI capsule.

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

Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 ecfc750ef31aac30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_service_policies_agent.py` first:

```bash
python3 dashboard_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_service_policies_agent.py   # or on stdin
python3 dashboard_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_service_policies',
    "version": '2.0.0',
    "display_name": 'Develop service policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop service policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55ec86ed89e4face',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopServicePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopServicePolicies'
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
    print(DashboardDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOi2LruX+Hm+VDVh6oUEARqR0dcGURRERmFro5qhoVMAjKqffq/34WaWd27d599+sb9cM3ITJF3vcPzjmvhry9e18Zl/fLlRQdegUhenicxqBGvCBG+HMo6g//KzIe/SFAWbZ34XVvWzcunlxA0QZ1UbVIWcLlal2EXgAbxkAbk0eeR2EsKECJJ0YLaC9qkB8jS2G6Q0Gtiv/TqEInKGglBD/KygqvqPgkAUpV5EiSQ0WekrEDRwPVQmyvi1+UAaT4hRYkI0xmFeAEU1yAFACGU4l+RNgZIn4AB1K9QPXDxTlUOmpcvP/386SWB71++/PoS5F4DP3oR3nQQHuL1h3T1KRyuz73iCAmrK8SngNcVqKG6J/hRCCLkefVxtPUT8p//mQ1efWx++PK1QJ6vry/jj9YVd73a0mtaqGbgVZ6f5El7fUXm+eBdG6QGbVcXd+AgvMXx9bHyOycIzo/jvY8PIa9H0H78+gLBqb0R/K8vPyAQx68vdTe+fx25VB9/eM1LiMTHH77zaTo/BUE7MoNav357Xj/ZQsLvpEl0l/oj5Ppwsw++vvzOuPH10Hu0E658eU3LpPj4YFzVZQ8KrwjAxx/+im0QgyDLk6b9H/H96cE4Bl4IbXoq/sOnO8g/I+jToHeefy22gm79O5ZA8jdxn5AnUH/F+47/P7HOYQo074j/S3b/agH6I/LTX9r23y34hERfXwSQw2SrPT8HX5Bfv+mqyP/0Ifz+4Yeff4Os/y0bvezq4M7h28krkgg07bdvP31o7h9/+PmnD10FYw14p29dnf8rnv8K17ucPyD4pPr4x7VQvllkRTkUyHukI7+W1f+qf3tFLC9Pwu+fN1+Q3+fL+EKR0Yg3oQ8IfpczDdT1dzj+8PIbLBEFtKYL7rdhlv/HfyDbJKjLpoxaRA/KrkWgg9vkBEbljTiBlam553YNS0jdJBDYJx2M/9HDo8ZlhPzyv4N7IYUl8VFIJ+8F8Nuz+H17Fr9vb8Xvl1fEgJzLOjkmhZcj2lxVvxbeERTtKLWqwbjiXvZa8BlWos/jm7FU/vLvmX+783mtrr/cy3zyqFAavxqrU9Pl4HW00I5B8bQngJ0BXEDQQRF5GUB9ogRW1k/Q8qbMYVlvRzSaLMlzJExqaHpZX++8IWJfRma//PKLD/X6WjzK6RR5tI5mAgne1UE+f4aGRXlyjNuvBQjiEvnw628fkP9C/rtVd+ajDBVW9qc/oIayvlMQmF/dCZKNTQSWXy+8++PX357wQjYF7HXQe0k0dpxxMYzPDIRvWOvL+WeCmiE+gBhDfE9VWbewRiNJ+4qsIuRdXyh0vDVW8bhsWtjVYO8KQRGMbcmD5rwjWZQt0sAgbKLrJ6RrwF3qL37t3VU8wUT32l+QLa/CnlHm8M+o5p0ILi6LBML/HgmPzyGT+kODcG8sXhFljEik8mqvimvvKSPyHn6BveJtOWTuwQY6fC3G/ghGqO7p8YAHEkFkgqdLP48+hzPACdaCsHmTfafxxs5m3Dtc/bVonqHv1aMrAtgKoNBjl4RjQ/jHM6SauOzy8I4f1PTeuR9eCJ9euceg8FezweqfZ4r3fo587QgMJ5H/v+aR0Zi5JGmiNDdEAREVQ3MeII96jc54zGFwLrgrcU+o77PCW6V5K7hfizyBEVNf//GgvLvmSfMoYl0NddDmGvJmd33new/bMQzrejTJ+1q8VfZPEKh7GYOegzkOc2AMvTeB4903TWMI13j9vcvf3Qzhg4EBQxOpOh9ChkQQCN8LMqhVPabe0zEwhsGYhkOcBPEfrEIgdxgqkD8ClUhgMsHqf4dOKaGZMOuiujx9J0/G2al6+DlE4NQKXhEbZs8YQQ1MWTgAjTQQhQ93VsgJQIyhiu8IN7FXPZQZB92ngt7oi/IEg/r3Hnje/B7vd11G9SFXL/RaiOUwVuAQXB6efdfz6Suo7GnM0PuiP7r7aSvy+xb0j6/FXcf3og8TPx+79+/AQWAkn5p7pR3rVgNrzwk8AwhGwr1Rvz567aOZv+vy5U/T/ce/twG4d0/zj577gsRtWzVfJpNHx3treK+wakxgjCQVaL43v8/PTPv8zLTPb5n2B84PoL4gf0+7P7B4hvUXBH/FXrHx1gaKG+P2+YJg8J855zM53v1aaOC7l5+hMFbd/Dom9VsLeiOBfehYg+NI/GhJzdjJBtg87zUY+uFr8R4JzzyBJb44jv2zKX+Xv/deDP36cNt7q4C3ihbKDsfp7QjGrU0+qt+Aly9Fl+efXgrvBP5HW5qxIcBohXCMWyGYOXAcasdb8Op9NBov/ri1u+cULAZh+WVMrU/IOMZ+Qt4n0k/I2x7hvu8qOrhJ+mmchkeRkBT+e6d93zf64AVuy9prNar+2PiMQ9hzOP6zEmNGQY3vJXZsW88UHSX+iQl8czyC+s9Mdvc3Xv6sE03rjS07ad+yu4F6hnAA+oRACGHWwUSC9bGDC/4sBsqpwbmDvTEczf2O33ezyoctv91haB+7x19f3urF0wfPSRGSw8T83IzdcQIDFQqE14+Qgvf+L2bIJwdY4+AEA1mAIApoCgPRFPe8YIpFUUREYEoRIPSYkJlOwZQmKYIlIoqasjRLBxFJkf5sBqZYSFE05PcIzW/jEJCMWhGQERPQOBmytDcLIKE/DQBO4CE9BRjFTiOGASQE6H1pBgvk09SHaSOO7+PsCMnT4l9f/BkJKZdks5o/XvyEtTzapn0t9tl6Bhz3MFn5iX2mfXdhsVkzS6uddObk+a2jNSCuaXke6JZiLCVPatdbXFD3MVpqbJbiUzVL1llFYMlgE0dXXRVyRocovexAsFuYB222OpGL0j6fuOXMPnm85Z33J02XVJ2ty0NuX4me64uCJfOeiOUWP9fpjrDRyWRbAc81pxJwLxuesDHsaikuyK9yFmyamx+bXW4f6CjOd6d1Lnq1BJjpRjbPl3578jm90cPJBMi3S6o0Ln6stBUVYglR46Qc6lMxDYXBK4wLHRY0Qe8MnNAUgu03OLpnLoDEYyw7mwpQlN5yPTzv6n1N2PHJZsgzxIfL0RWeK65dtqjkmteFdusP00xOqHwVrExDSq5du9iT6i0rVpbgXVsbTxf0IdsNeLEHalsPZjJbnPVgwOrDXjuf9YV+poeu8tqw1zyFuwmWqtGUZeOzTSaDa6p57nGX06fV7dKbebLZ2JKQS+EBm2d6ISpra38+5d3ltPFV/FZkjrxr2qvt7veKT9IzT7xa5LlYs0HjWfaJIK/GuVpQ/tVv6MN+dfKjeloo4VwtKlUIhWDKMUFoi0qzIgQnah0H93CSMlwdbc7VpaknHrOosdok0/WwTMkDLKA8364cuuh3XirhCXvbWj7F5LaKMsF6c+JmLu6H7bQ2yNS65djQTTOsqevLwipcUDMlmNfLMHZjXumUlamk6WSzbjYHj+eYntlcziHvHpXA6ehtaGdGRluRV1ZYFVZRukkTUtyw2c3nF7F6bS+7lRnUJ3PdEPFNkIvJVD1YxXpad+nmRujXG3/bTTYNbbqlt8pkc2huXl+ls+L+m0gFWq7DFPgNixZ2jnIC2JJoYqA7lfFXLZts9q0xOeqLXYXDMFWx7XGm3LCosAGO6pgPzE73jeZcKxvxIqPSOb845Ulm3YV8nhGJtN86+O46maV4z6BLfzvd5Mbc2K29Q1Xsg+Ac3Rb1JcjP1YnLlDz18Jsjy2BwGi2TUFPmF1xG7lm3DtJdpmVNaiZr6nzT1R0MgAp30/iiLJepHDKrdDWbBNXM5doQo7OE2V02fZropINeFkDc6bk4kfPdgtpkuMVImN72R4FQrmuxoaWo6icber/T6/NeVnH0gPMSa1iR5F3R5XxbSKWxVFLp7O3SLTlkfkVOOd7B5bnkZfxtKlww3MJmgGkuR5/DIouvyXotpuXZOChat9cDLUcP10XQRxeGv03kG78n/UTGFIsiW2OzPVxPbOWoOF5r557IyLnN6Tohqil1Awpvg3iee710yhaJo1GGHfqsOFvovpod5GEuEGp/Xu0L7xBct7fcAHoRZQJOWGB/UqfZFet0faZtJ5py5fwTjOFpG2ZddJtRS6UHe92iHa5e7720z81lIKcxcTJnmhIeD9qBc3duW69WScjcfCvA66W6qTrHVKj8NHSC0heXycbqLuu9H0y2xsloBdo2ArBkwVW+cCx3dQiQ8HJKzpsJvhiMmbx2S6s+NFM2poJJR4XTyyQQCHp/pFwVtFwiX0wRZ3xXHgT8eJD0lRtdMyG84pJH5uwwFeot10irLdxs2IzryytR3hlscVBvXOPE25lJn5TTJVIPDLDVlcn7Zc9Y8mERlrPVnLF0fjk9Jgp5NCJSYebJdljVcetsuaW84kVYW4eWx2J/aOly5nESyQntbt1VouOZgm1tzFzojO0tHtD9qpJQ2aVW5mV71ugd3wMFoJS/NxPDrgN3rqRrko2acAvahtb2M+e22/U9gYLCvZLNTTyedpVzE20/nBh8LZ/V3Le8WinKveCY9rIoDxQTMJK49A8BOnT7BS9G6oy6bmhm32nRJMOZttNdZrVMFpjZku3Z8onGF5t5QciiLoUlQzmmxsnKtXM11xwEQPWdYxecOb1wA+/rXkMFxyZOXUUwKUVfQv1XZ3nNZ54+RY1SmpiMHMUoI7JObp9TN10fMTgYlLgQ8uhMJDKx2Ki9kg3MgQP73m9pZbY9LNKlmezzcp9sKVLxSCaqfftgVOd25e+pQ7+gDYyXrOlxa622xdzv3PXiaIf0wQsGyzpvac+KV3h8avcADW2jYkh78PRDSyjdzJeNrnNkPrN369zwg8z0VPTKdUNO71f7rA5Jk6bWl6OsX3iy2C4aWlxxK88hwro/XwRqSR2lYTtUcbV17e2ONQacYzHhRGhqZfi4Iu7IneNPqngx0y8xl/K22fkaR2KemSyFebLJaqAm1AoMZcyj9nrh6U6M8sLuuE3QYeh4l77ByT5XCu+K7YY1qx/12DmWWohnWL9wy6V7U+IFd9TXck2lzGV6ulml1c6tZXJaCRsms0N0Ix4C4PI5aRRYR2lFyN96t5Dbs70/MDfBc+IgLDwLFexD5VC9O8csfawc+3a2q0xZlG/K5aysllqH42XARldGu52d6UJb4+ilBoXGG5ifQPefTzU2n10HEW2uBX+KZ1VqeiLfyztP9rcSGq+5cJMnez3kYzktk3rIxHJWbe2uROku0pdVs8fmwxVM2ibyheUkCEM/zZwOSOVislpuOtrFMAmbZdT5dD5WcDOixzTNUADAQSi5rqkVZotLcJQnvrIi5bS6AsAqcDhedfkBJ6pI6NiTlfVyRha0TdD4JbixW3slunyXs1gI03cbH8u9coIdzG3beDm/1gLr1Omq2bOnjcYUizOtGF5BS4eVynHWfj0x6vycWISQGGome4OWYOfdmd5ycKyhc7A362npm6WnTIeKP9WmR4XnttqjnCPNB41HvSnZDoFVytWlO1HiOjCnuoz7RyzDF5mkoCVsVnwac8JpOMu8GlbJPAxO2STxo5XuRjDIZsatWbWrJdOtI8LdktfQGA/LJJXa9DG2t6bnpItX9P620CkOo86t6EuiLlJAJ4TQ5Xf62qs6wTXKwAYE7LqeDRzdXuCNhps8iFOVZ9aNFZolSSu6h1UTg7Vcf5e2xhpIs9w2snOnL5oh7lnX2rHZdiay2mHV7wElUCXF8Id8hqc8lSohHE8dOPGdhzhgSKJeeq4cXVwXVvibt+sybIJbCSfR2Y2xjKjfhRXBMEoozSU2FG/hLXNiZb13CkE1N0dnKwaHemkJl/1yTWhZa9iGQ8CwnlMSHQultFFRCnNmZnsK12rBSH2IsVtZu+zP3fl4lFiqtK3teiW2C4khDWdp2fM1x3F2Rq3nydWepWs36zeLXDybkq5BmE2Gup6JVsbbnmZ8fRUkreQUrkYfnQW6M/cSSNvGrfPe19HUnRc3o4mx2drzDWu7X/ky3aPc4RhLJUpozZZdgnjKwyYrLiOQzs++JR4XQmnSi/U5uDrcSd8OrlYDBuUv01ha9qrMDFrD+Re2cwG+sg6Ff2bkXOcdMaICZraG4NpsQGQHtCtP03adz0MMH7arrohUxtkKdMIofA2OhNHy+Xm95dqjlB+YzIXlgyTWa6PCqzAx5Hm2NB0hPganeX0N5gt7ww8z+2KWbpNKsV4d4mxGFxjRHL1mI2WCpdFw8tqhXDNTtCmezc3bho/DfRJtFji5WxprcRGtjrWKkp6sLD1Gpq29WFHa/OBbTT1NmTDkFyRN9dFGpGdJXdWUqOWiedkkZ9Uu6sLrs5hDY1abmb2SgozDmusG46c8ipLTqFTgVsSirD4kKqKTuNo1WSIewMFV8U2/7UOYXwMVzEJC4mKfuJK38zrei2uvOHSbsLqu5RY7rLs+8TaryZyhpL41OqLziCNqX2YU3CcGxW2R7rWFf/LMi6YmOyGZXrxGvl7m7R4HpuH50yHqysCh+RMXt4NKqQcTcCrO6hYWErKKaWjPH51pJ7Spc6DqnD2tmzYS9iefsEIcnytVjIbcrY83p00f4kdVoyi1p/2anhy5Qa8HsU6jCW5MVDjKFX3YoNdammjrqooCbTHrj8uwjEkyUS9RyOf15Fo7bWZ3Hc1HmGBlmLPzD710XEk7HltdA+bS79NEGE4s5muBeUPr1WwXUr5cWQ01nW4vw8bXKq0JBY3uSsXyGG7YhSC6nnpgNpd4m9SZZp4cd6IRC1TxrmTQcDY/6eb9RJ1cRIXFcclxFwu6McN5y3Qd2tQUz8p0vcXiVCdnkopRJGjomztsJT25HC7lpqoJVFjUka+NyR/l5ZScTurlUldPixDXl4x4FcUD0ShqX3a7mA5vTFFlq27qsWHDOZe519T25dTWNHHI6UZiDwp/pQcm81iSTtwODS/d9CrC3F0zi90UxGRLiFETxNklLBvD1iPNxsreSaWZO4HdjA/5YSVSVjVjEjZrt3rZWxjJtKSCOZtLLmIBuuBvEefrF2NaLi9Z0VyvVJFE3a4Z0IAbantbVIt0u9uA/pIyk+WymJLehV7S+6V5zF2/ZIv2aF8oJxR55xzMk3146AyfI8utkkh8ZU+mFB+DknB5DZ2cLCxrRSVeEgId107RMR3hbEK3pXe2PllAt5UNOC7dqElcZ8LO5re4DZp0onbK5TAj08Jtg7q7+e1QbMo9qbFA4CMqWRLqck5slWWUohfJGwLuFIanSUHDLt+rlhPemjnlbbjmvOsUmzywmzo/uCaNTffTkG7tVhDMbgauwVKnRDRtyZU4CMPcLEI4vnUxGx7CRJsLuTO53rLO0taoQQJV32lKNsUPysxDJbdV+njRS3NsRwFttzwCpiWmE1UliAOrYHu1PnY9E2ZHtb3dJp4l3HRlxtpy1IVpXStYP7SpLxJVoEyNpQs3n53cNRrtL4jIotkFi8r6Flz7ZufXSj0DzSFdR6sdszK1+Q6sk92suwkT17kKpm+rEo+HARVSi8Mlam6MYuxVruIFPIyWgjAJ1qv0jAe79jIT6lu1SWMbVRWnZubkmkbPW3GzynX8NiizpVJf5sbeWer2ip9aQrEplqUGXdmbRLZt9/6kd3W2YYUed9ZHT5QNfrbEuqjCqKMAERLIqvaYNU1x+EkoYSG+iszBPm5uu6WSrM9Mxc5sfH4rb6LkujsO9vDOYeG8DfBiM/hbZlhKNuZC59dbYdKTlsxwOePNRZYhSlTj/cPmvFtMmqGdpg4MRvSGu+jQivvltqsz2CNSKybOs/PE4/hzNFnwVIvfthf2aNRMAOb03nBIu/CJ40VMdW1/5HZTPOTVWbJnyqvu3wxaCaq0pXB9ug1iUuuUad2YXUuyHLsg9wSd8dl8Pv/xx5dPL+Pp8/MM+W88PB7P9P6fHS0+TgHfnifdj4+BF365y/ryd5T6+dNLHSRQpccRapN3x+dx4z8doH7+988hxvXXxzPZ8dHXpX07cG+94/i1opekCLumra/fmjLv7oe4n178rhm/4dB8ex5Wv9wNO1X3k+83kSPnpwlt+e35zYyX8SsI4wMdECZeC56Xx+epMlx9hU5KgubbdEZ9A3U12vp8tDEexY7PNl5++z9KcFXk0SUAAA== -->
