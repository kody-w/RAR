---
name: "rar-cowork-cookbook-teams-update-contract-suppliers-for-services"
description: "Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_contract_suppliers_for_services", "rar_sha256": "71d6de08d6a594efe8d5d86af08620ddc6a49c7e2a35aca9ee18853d790bc714", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `teams_update_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

Contract suppliers for services Teams Channel Update — Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 71d6de08d6a594ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_contract_suppliers_for_services_agent.py` first:

```bash
python3 teams_update_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_contract_suppliers_for_services_agent.py   # or on stdin
python3 teams_update_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Teams Channel Update — Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_contract_suppliers_for_services',
    "version": '2.0.0',
    "display_name": 'Contract suppliers for services Teams Channel Update',
    "description": 'Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02b5f64d501879b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateContractSuppliersForServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateContractSuppliersForServices'
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
    print(TeamsUpdateContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66ZKjyJbmqzDRPzKryQwhJLa8VmYDCNAGSCAQUmVZFvu+b4KaevdxJEVkVte93VM9YzbkEoC7n/1857gTv7+YbRPk1cuXF9U1M0gwkyQM3AoyMwdi8z6vYvAjjy3wD7LzrKlCq23yqn759OK4tV2FRRPmGVi+qkyvqSETOrlmWkN2YGaZm0BFXjdQnj3WmnYD1W1RJKFb1ZCXV1DtVl1ouzVUN2bT1lAfNgHgDYVZ407Tw86FaMcs7jesWTn3VWUb2jEEZDF99xVI4t7MtEjc+uXLL79+egnB/cuX31/sxKzBq5e7QFrhmI3LPqVQ34Tg80p9igDoJGbmgwXFAEySgefCrQC7FLxyXA96Pn2s3cT7BP37v8e9Wfn1T1++ZtDz+voy/VHaDGoCF2pys25cB7LNwrTCJGyGV4hOenOoocpt2iqbrFUDLTL/9bHyO6W8gH6exj4+mLz6bvPx60sORDAne399+QkCdvj6UrXT/etEpfj402uS92718afvdOrWilxgdUAMSP367fn8JAsmfp8aeneuPwOqD89a7teXH5Sbrofck55g5ctrlIfZxwfhoso7NzMz2/34078iaweuHSdh3fwf0f3lQThwTQfo9BT8p093I/8KwU+F3mn+a7YFcOvf0QRMf2P3CXoa6l/Rvtv/P5BOwgwE9JvF/ym5f7YA/hn65V/q9p8t+AR5X19WbgJSpDKtxP0C/f5NPXDsLx+c7y8//PoHIP1fklHztrLvFL6lZhZ6bt18+/bLh/r++sOvv3xoCxBrIKG+tVXyz2j+M7ve+fzJgs9ZH/+8FvDXsjjL+wx6j3To97z4H9Ufr5BuJqHz/X39BfoxX6YLhiYl3pg+TPBDztRA1h/s+NPLHwAqMqBNa9+HQZb/279BYmhXeZ17DaTaedtAwMFNmLqT8KcgrCHwd8rtygV2rUNg2Oc8EP+ThyeJcw/67X/ad+z8bD+xc9ZMIPStvaPQtzcw/PYOht8Asnx7A8PfXqET4JFXoR9mZgIp9OHwNQNYlzUT/6Jyp5kAWayhcT+DlZ+nG4CZ0G9/h823O8XXYvjtjvbhA7UUdjMhVt0m7uuk9Tlws6eONgBm9+baLWCW5DaQzAsB6n4C1qjzBAB0M1mojsMkgZywAubIq+FOG1jxy0Tst99+s8w6+Jo9IHYBPSpIPQMT3sWBPn8GKnpJ6AfN18y1gxz68PsfH6D/Bf1nq+7EJx4HgPpPHwEJt6osQSDn2hRMA+4DDgeAcvfR7388DQ3IZKDkAY+GXug+FoOYjV3nzerqmv6MYjhkucCAwNJpkVcNwG0obF6hjQe9ywuYTkMTsgdT5XPcws0cN7MHQNUE6rxbMstBLQSBWXvDJ6it3TvX36zKvIuYguQ3m98gkT2AOpIn4L9JzPsksDjPQmD+95h4vAdEqg81xLyReIWkKUqhwqzMIqjMJw/PfPgF1I+35YC4CWVu/zWbaqc7meqeMg/zgEnAMvbTpZ8nn4NyngJ8cOo33vc55lTtTveqV33N6mc6mNXkChuUB8DUb0NnKhL/eIZUHeRt4tztBySdKD294Dy9co9B9r9oHh4tB/tsOR6lHvraosh8Cf1/60smwWlBUDiBPnEriJNOyuVh0InnZPhH6wX6gvvie/J87xXekOYNcL9mSQiioxr+8Zh5d8NzzgPE2gpYTaGVO30QA8CgE917iE4hV1VTcJtfszdk/wSscocxYAeQzyDepzB7YziNvkkagKSdnr9X+btLgdogCEAYQkVrJSBEPNd1LHOyQVBNafb0AYhXd0q5Pgjt4E9aQYA6CAtAf3JGCBwF0P9uOikHaoIM86o8/T49nHonIIXT2kBa0Ki6r9AZZMoULTVIT9AATXOAFT7cSUGpC2wMRHy3cB2YxUOYqbd9CmhOvsjTKWx+8MBz8Hts32WZxAdUTRBkwJb9hLuOe3t49l3Op6+AsOmUjfdFf3b3U1foxxL0j6/ZXcZ3qAdJnkzV+wfjQCAAQRxPqDphVA1wJnWfAQQi4V6oXx+19lHM32X58peG/uPf6/nv1VP7s+e+QEHTFPWX2exR8d4K3itAiBmIkbBw60fx+/yoSp/fMu7ze8bdS9hbxv2Jx8NkX6C/J+efSDwD/As0f0VekWloD9hMEfy8gFnYz8zl83Ia/Zop7nd/P4NiwtpkANX2vfC8TQHVx69cf5r8KET1VL96UDLvyAs88jV7j4lnxkwI5E9Vs85/yOR7BQYefjjwvUCAoawBvJ2pj3tsdpJJ/Np9+ZK1SfLpJTNT929tcqZyAOIXvJ82SSCXQIPUhO796b1Zmh7+vL+7ZxmAByf/MiXbJ2hqbD9B7z3qJ+ht13DfkWUt2Db9MvXHE0swFfx4n/u+ebTcF7Bha4ZiUuGxFZrasme7/FchphwDEgNF6kmWt6SdOP6FCLjxfbf6KxH5fmMmT+QACD8V7LB5y/cayOmA9ucTBJwI8hCkFkDMFiz4KxvAp3IB7APondT9br/vauUPXf64m6F57Cd/f3lDkKcPnr0jmA5S9XM91cYZCFjAEDw/QguM/V91lU9aAP9AJwOIEXMHd1yEdHATo5ag/pIO5pC46SEkjiKOY+PmkrIJFzUXmGmblOvOSRJbOASFWDYxXwJ6j2D9NjUD4SQfapo2OY05FGHitrtArIXtztG5QyxcBKMWHkm6S2Cq96UxAM+n0g8lJ4u+N7iTcZ66//5i4Uswc72sN/TjYmeUbuIoYSmBBVe4e7ka1MYKtXKwLKeyCne+PtvWhk5X7g0JyY3ectKw5eaSrfiyqTmVIAcris6I7aF1Wo9Ob1YMcqUWzHN5upK4LV+9zhPceEMHQjGUnVpg2kly+FhLFLO6qltHDrutuUXkQV/ynXSKbHJEDMELA9XwMxTG4Vlt24kxP5u26iryJmHxS1lkrNEhu7oymrO5sIOyX0TylV9uucIz/AKNuxU9yw6bQQJenY877JJoBayXXE6ttwjuZVeEOhgFQl1TuzOKxYzfbw0B5VF+nfEuP290Nq0yHRQOVRWX/flw1awDydf80qqO+jFbKVgqqnOi7SqT3WHxdt/vGLnMSq081TP5ZJeyPfC4ruzw9ngwW79l++RUS+szRuwTZ6XzDI7d0jjxtmyB0WW1o/RaQWEqU9pWmimEZhZV7IkkZ/ZaaO8U94rL5H6QRSztE4UpRjlbCmiwiVxqTI5tqre3dINJEjH2YlrXICAvvkorm4Wr9Oix5UlYBwhV6U1gCKrWMjNHxP0rYmmX8jizooBXu8rYS5erXArX9Yqs9TXX+Dv4pLnSZXYWeOqi6vryiowRZqBIoY6FW4xORbte4J5LabNrgyiUA1j2BaOmTqR9FepqfWCOjmC1PC5gV9iVkG3tlAKLEoaxhEXL9nVXSrgD2SwjkUXX6XojhcdmvUEoMuwkKc2BTEufLPOWQ3LkFhJitEQCdmGWI88fEqvckQpsGXQYE3Op3rjcLF9w+SUumFvG7MsL7JNLB66Ya63Nz7xRj1mop5d2rYOKeB2vm2MdbDFDF9QRLU7eKHnnapc2gjZ4sFOVVipQzZn2rqlu+EiXMkZ9Ofi+txTnC3Qjq3MPZVQEyxazJQLf+k6B3TCy9nsaydoFwS9vC0Udyr1qD6RKemecF2o1iofe4aM6lqRlpCEFV4opN78lnFjWwXUZKluULVzpeBEWNieTpN7TbifmlbVFWBXJ2chnltIyDw28UG4b4kpcfJlzg9i/9Xs+7HNXX4vRKhmzVXhBOxtb9CW5NqjoMp7Go7VjwvPN3wTwpaQTMRAZ7hAxUUEOWHI4UpvSwzE80xT7uoidWX0hWAxRz3VLIfBsdBGqsy4Kq5wOYa/PvHJXjfrZWOIMN57VS+AUiaMj3UHQIlcyaaycA1nTmvdO4mxY7tUKL5U6gptFqupqUco04aYrub6dC4feA/vlBV6pmYwo3DaqcBJzPGW3qW9xk+n0HmvUYuHsRjmtrXw+ahm8qUt3q8SatLbk2j7t5/RO3tWaHOwx6TpvUU3tOHG1OnD8mLseI2HqmcSCKnUCk72O+Ra+JchIsVQ4M4zdVsvjAWjPwRpLJZq9w71WGnnvPC9PjhbNZTRQcU3HyWuSzpXL0ruudmfV4Lh5gmW64NiDOqQSkuzasmH0ZM0N0d7Wr4Xs7wyf9ObG+dKUsI0ISmnoWkVWArzYNpGnDNiSicFo7NKzjRM42Aw54iXlIkQsHymcDR14NhNVZmbvarlejTW9qZXBD9HGO18ZuF8RSLo2xGTFaZVSKfzAttlF7aX8pvjlSCKKkOKrahVTV2cG3/bsdufxXKGaRhZRBK/kOKa3oFzVY3J2CcbaHI876bgK6SWmmAmJwghnk0rEFO75vKI3arKNrRiWDOOEFg1qkenuemt86YKUfcTrPoEXQJN6oE36bKt0EmyKzHSvCCvo3UhWdJS1DEjxraHXdOkz5rldm4fDychXmQ02DPJ1Pp816IgQosGjbsyVt715SUciwuQS4eaz2EpM0A0tNZZFzHVmRASpHA9nIioZ4iIKVztcKTPOKAdydiKoJXlgO28Wl7M6T8Kk1iQmqPUKL05cTtcws96l2IVcKtk5YJCh0XfbTBMGvquX6CggF53q43Nv1rzrS1U4Wma72/nK2cEUHafz7SWep6t+ta3JTTwsQm4WrAt9p68TeawZui8pVYzXxDU2ebgOycEhyGBO5azBtrrZHTY8NSMN+4xJKyEtNgUZ3fxDLZzsMFGJPlAUlBDMMMSWjckbnlrPVmzon2pZh+MiFa4LzCl6301zQvLRdeQKDbqPwvnezG4r+ya1y7mzaOutrxoNKrXs3t4y8EbLnTTGBVU3jQQpujpyIieh8PB4PewrgkfwpKGHJkxi4rKs9XGtKuuCLDIqVPyuL/vKRd1ipc0P/FEBsN7Ep7NblElIU8Rl7NvASqKISdj0NFSnXSt6JePKJifM89qSDtzi1rFpPCyDvBW2eHLOucjzDzSHRdpyl3WCmBDZYFvFEeA3tefZa8h2/PzsqLWRZkEnoZrG3ugytdrrKMKVpKRnhNGc7aWXs0GhuWWzb0Ym31tt4I1cJ0rYcUvUNw5l9pcK9QAiHVvU8ttFBzJzN8vi+KSX6b73ULmSrvwGcea5tNmrgZ5UtuTdYB+7XYytVe634YLaRdwiH7iUVDUdeMG1jieBUT1zR3epAzYTa97c7xiTsWuhDXa3S8HHRzUJy92Wb+Idfdzc0tX16FGnHRKQKqvF7Lidwc0MHnBlvSaMIy40WVwqp54N+Y6hOqYTCgdvq6PSRmsPG0i7sPdMVqltoBwdlC2dVgQLxIWukYS/kMme2nZVouIptRBPyjEy54fC29eL80kS57WvcHvbIFSE25CDwOo0KhxmUr7D+XpViAc+LLnwtkr72xqxjX09F0FLbJIM3SGtrGVeWejHftnUBR7sZUFSAwUxtvGOkQgX2bGx3CQWNlNcEjM2pqR21i69zruaC2hRPs6KFt5rHFNsYj/H7VOSMh1rNRou9VftrGDb1UHfIiajurl/RplLoaBDnCawlpJHbWGi5WVPV9srSmvaeDvrB0KWRXcbL/2FEUTyKkZtZGHi2y45nbVTv0bObttcjsI2FJZxffIHTfQv1HGvaOZpx6Byt76yZnZY6Ychj3aLOpTONnfBPJ9kDrhFj0ukWJzyW7tkNUKOmpN4ESjEPCVy616pY9ARW/1MLRBUu5F5sKW83Xrox3zTjVhHXzPWSi+R6DDxHr3xy9C4xkLegmykOK1Z31ZSYQJfr7DswBGyIivnvZfeBP0KEyHrMo5enxILRL5GVsxOORjJys85oVmoIrIiHHG5uxSSPSCBuS3P1IWjGKki8+7cFtqiUgwXzm/y8YIvSBl01Y46LNCB63h9jsW806lJAkzAtMr14Gs4s4h9YTiqoEJpvognaN43yqEfPeUgKGyiqcKBa4sRn6PXfD2qvGgGxAa9sh5mlFVc1rF+2oyXcb/KhuTWDwpIQmwzute9ho55pKYG6tV4x7DyxYGN63xnYmdXQNlsrrepwqZsu012fJgfLroGHxTJ9W1/qBdYfRGimSBe2miHn7jLqohmZgnLnse1BI+dzLjoN8OOXOqxXvvN6FJi7RzmcifydrVJj70oo710QC50uhzIQKzcVDhRDF8SHZfvhbNX6r4rbf16OZfXhVeq7dFNuJG2Odrr+eAYrA69ma57tAhoWRPhMVHheXYyZ14RStrOQY5dT4sj3cdIJ686YUYtgSYbRauPAknITqBIxpnhUgHjsCry68rik2PFMfwMFs/VvslgK73Nlyp8aROWJC8ZHg19t+ZVp8kMTxT9mq3q2ZxEM4VFYXF79kBRQEMht5JRpsJSxlEMxaw1gWaZe1DRLltYOFzBeElcL1QxO1gBgs+XB6O7evvcrty5U/vLs+OQ0pwJSZ5NTgsrdk2KUs64elXTK71GFsiWYWZzjcr2uVOfW9FBV2mLFnHf15u8Vp0zW2fFjmeimZTR8FUhxNNpt+8kDBYON4JPma3vr9PGX9SpIXVnKjLma3N30BAPHWPZWiuLXvRaM1zO5ygsBUuPIXYDad7kIeiieCcPSUuilFdt3Ei5RbMZujBADefZvsJlQp915RqW6sIKnPmNlDsrYiRcwxWOQCm6w4LLNudOgTWe2NXY+z3qK+hs5ODLfrv1ewntXP1yOrJMzuE1GRx8bpeDlOH4nuc3ZEgmioUlNno97zuFXnlyPTQotfaXNjWX8k0W7nwKmJ7MsRtTHLbioRUiPuY9RIq6SCdhY0Mv6po4DELs9bAA40u2I30f9jZyeIbPC0OT7MZurZmIGIXul6R9IXoKW6CYf9H89UAaR0NVUE8cTEGeE1FnGq66AHVBuN36ADsaXsAtfKGsfU/p+lZmKnysi8WCO13ml9nUZCnyyMJiYVxvUsG7VtbpbJcd4RUSnap1fd1TJBU4h1pEadVYljpKsVurFhcmxgYhcbskYiyHJxDaoWxUe7Jw4DhXWXrcChnR71EVue13jnEKFoa/uPqdwBkcZu+CjmTRJlqNOX8DpfaWdgaHLvFxhfVrobmULheLt12Mz6oEJuWVko+0SBxnGoNui1CgFmpkNf5RA61SzFbMXiNMhOd9rD7T2OnmRN5ejbzFxRJvYuIxob1d6MLlBGdNKLXbhapbddNx8Ckrkm2or7bW3ko26Jry6tqkh6NRzd3LieCFM5bheNTFVOvCnWC4WzZcydjaD5dRX/VEGvmVwNELbHZZMWCD3hxQoV+lp/SgKLuBOiyZW39eXQsGddP+7LhW0dlta1Ip3hGItjpiqLWnpXVCzDlrvnTVtXg4ihzmqSl78JPutOzFfJ2L3pwbslHZRTkmEEOoebpN5SQFmk8Zlak+XM/GebOZRYtqDzug4RytfVsgs0XVSR4nsKvZfnWgMFveH2d5fxvHzQXHSLmYobZlVxTtt7huHQ/iNrIWFdyU4uGALpnZLJmPBJtbAPhO5phURNgbodiGkng8WX7p7MJOnY/GzF+mvEGE0vooGZ2jDyuU97oVsjoeT2CXML/Zs5mhdpvzNiQJ2w+GJXkiNlbXHOS9U4pz9zrE9IWqkI0Oj4Pf41yzJlka0XesyIuL2zYm1lKp7hyqO1gZMrOuVmednPo6W18izt9vCWV2HQi50nbyGJAOzzjI7eAWLtnbPV2nNBHg3P50obFOSU7JwUXQQrjS154ot7TtmU3nFkd73l3P8/Vq3B+UW8afbi0xNtZSplzf39pJ55S1BMNnf7gNV6ty9/HBJjvicI4QZzEmDHtd2eLQ2fHO2KaHa6VWsL7ZHmdXKRNT1MNJjbaJqgGRTetRcGk6nOVUacsPG444KPxWVPerMBt36y0jzmdmuh+7yp4rON0SqLe6JE2k4CsyWLjGFWdjmqZ//vnl08t0Xv08df5vfW6eTv/+nx1CPs4L375K3Y+cXdP5cuf15b8n3q+fXio7BMI9DmDrpPWfR5T/4fj189/5rjFRGh5fdqeParfm7QC/Mf3pF5dewsxp66YavoEdX3s/DP70YrX19LsT9bfnoffLXdm0mE7Qf1Tu+4Fqk38rzMnE9y+VqeuEj+Hp0X+eTX96cQbgwNCuvy1w7JtbFZPOzw8l0zHu9KXk5Y//DUlMS+McJgAA -->
