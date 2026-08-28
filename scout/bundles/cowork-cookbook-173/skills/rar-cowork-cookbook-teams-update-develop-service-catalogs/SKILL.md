---
name: "rar-cowork-cookbook-teams-update-develop-service-catalogs"
description: "Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_service_catalogs", "rar_sha256": "4cca61b74b8e150822448d800b42fba02b40748304ad63a0bdbfa3bb72ac4a0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_service_catalogs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_service_catalogs_agent.py` and in the RCI capsule.

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

Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 4cca61b74b8e1508…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_service_catalogs_agent.py` first:

```bash
python3 teams_update_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_service_catalogs_agent.py   # or on stdin
python3 teams_update_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_service_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop service catalogs Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '868d68191755aec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopServiceCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopServiceCatalogs'
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
    print(TeamsUpdateDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+7eiyLLmv8Ls+0NVX6u28oY666w1goqAqKAI2tWrmkfykPdb6On/fRJ176q+ffrO6Vmzxqq9t0hmROQXEV9EJv72YjV1kJUvX14OwEoRwYrjMAAlYqUuwmddVkbwTxbZ8AdxsrQuQ7ups7J6+fTigsopw7wOsxROX5SWV1eIhRyBlVSIE1hpCmIkz6oayVLEBS2IsxypQNmGDkAcq7bizK+QqrbqpkK6sA6gUiRMa1BaTh22AJm7Vn5/w1uli3hZiRRN6EQINMLywSs0AdysJI9B9fLl518+vYTw/cuX316c2KrgRy93S/TctWqweKg/PLTzT+VQQmylPhya9xCFFF7noISKEviRCzzkefWxArH3CfnP/4w6q/Srn758TZHn6+vL+E9rUqQOAFJnVlUDF64ut+wwDuv+FZnHndVXSAnqpkxHgCpof+q/PmZ+lwTB+ed47+NDyasP6o9fXzJogjVC/PXlJwQi8PWlbMb3r6OU/ONPr3HWgfLjT9/lVI19BU49CoNWv357Xj/FwoHfh4beXes/odSHM23w9eWHxY2vh93jOuHMl9drFqYfH4LzMmtBaqUO+PjTX4l1AuBEcVjV/5bcnx+CA2C5cE1Pw3/6dAf5F2TyXNC7zL9Wm0O3/p2VwOFv6j4hT6D+SvYd//8iOg5TUL0j/i/F/asJk38iP//l2v67CZ8Q7+vLAsQwOUrLjsEX5Ldvh/2S//mD+/3DD7/8DkX/H8UcsqZ07hK+JVYaeqCqv337+UN1//jDLz9/aHIYazCVvjVl/K9k/itc73r+gOBz1Mc/zoX69TRKsy5F3iMd+S3L/0f5+ytysuLQ/f559QX5MV/G1wQZF/Gm9AHBDzlTQVt/wPGnl98hSaRwNY1zvw2z/D/+A1FCp8yqzKuRg5M1NQIdXIcJGI0/BmGFwP9jbpeQQsoqhMA+x8H4Hz08Wpx5yK//07nT5WfnSZfTeqSfb82df749+e/bk/++vfHfr6/IEQrPytAPUytGtPl+/zWF9JbWo+K8BOMMSCl2X4PPkIw+j28gTSK//lvyv91Fveb9r3dKDx88pfHiyFFVE4PXcZ1GANLnqhxIwuAGnAZqiTMHmuSFkGE/wfVXWQzJuB4xqaIwjhE3LCEAWdnfZUPcvozCfv31V9uqgq/pg1Rx5FEmqikc8G4O8vkzXJsXh35Qf02BE2TIh99+/4D8L+S/m3UXPurYQ4Z/egVaKB12WwRmWZPAYdBh0MWQQu5e+e33J8JQTArrGvRh6IXgMRlGaQTcN7gP6/lnjKQQG0CYIcRJnpU1ZGokrF8R0UPe7YVKx1sjlwdjeXNBDlIXpE4PpVpwOe9IplmNVDAUK6//hDQVuGv91S6tu4kJTHer/hVR+D2sHFkMf41m3gfByVkaQvjfg+HxORRSfqgQ7k3EK7Id4xLJrdLKg9J66vCsh19gxXibDoVbSAq6r+lYJ8EI1T1JHvDAQRAZ5+nSz6PPYb1PICO41Zvu+xhrrG/He50rv6bVMwGscnSFAwsCVOo3oTuWhX88Q6oKsiZ27/hBS0dJTy+4T6/cY3DxVx3Co6Hgnw3Fo54jXxtshhLI//+uYzR1LgjaUpgflwtkuT1q5weEY3s0Qv3oqGDtv0++p8v3fuCNTd5I9WsahzAeyv4fj5F34J9jHkTVlBAnba7d5UOvQwhHufegHIOsLMdwtr6mb+z9CcJxpyoIAMxgGOFjYL0pHO++WRrANB2vv1fyuxPhsqHbYeAheWPHMCg8AFzbGjEIyjGxnuDDCAVjknVB6AR/WBUCpcNAgPJHL4TQQ5Dh79BtM7hMmFNemSXfh4djfwStcBsHWgv7T/CKGDA3xvioYELCJmccA1H4cBeFJABiDE18R7gKrPxhzNiyPg20Rl9kyRgvP3jgefN7NN9tGc2HUi0YXRDLbqRYF9wenn238+kraGwy5t990h/d/Vwr8mOZ+cfX9G7jO6vDtI7HCv0DOAgMQBjAI4+OrFRBZknAM4BgJNyL8eujnj4K9rstX/7Up3/8e638vULqf/TcFySo67z6Mp0+qtpbUXuFnDCFMRLmoHoUuM+PAvT5mWqfn6n2+S3V/iD8gdUX5O8Z+AcRz8j+gqCvs9fZeGsD1Y2h+3xBPPjP3PkzMd79mmrgu6Of0TDSatzDivpeY96GwELjl8AfBz9qTjWWqg5WxzvJQld8Td+D4ZkqI+f4Y4Gssh9S+F5soWsfnnuvBfBWWkPd7tikPfYw8Wh+BV6+pE0cf3pJrQT8m3uXkfNhyEJAxl0PTB/Y99QhuF+990DjxR93avfEgozgZl/G/PqEjP3qJ+S99fyEvG0G7lustIG7oZ/HtndUCYfCP+9j37eBNniBO7C6z0fjHzucsdt6dsF/NmJMK2ixA8Y6nr3n6ajxT0LgG98H5Z+F7O5vrPhJFpDUx6oc1m8pXkE7XdjjfEIghDD1YDZBkmzghD+rgXpKAJkesu243O/4fV9W9ljL73cY6sc28beXN9J4+uDZEsLhMDs/V2MBnMJQhQrh9SOo4L3/u2bxKQRyHexToBTCcSwKtWnCZgBKzhgMIwjGZWYzm8A825phNjGjCQafEZZL4dbMdm3Pwm2bxiyHsGYAynvE57ex1IejYZhlOYxDo4TL0hblAHxm4w5AMdSlcTAjWdxjGEBAjN6nRpAon6t9rG6E8r1vHVF5Lvq3F5si4Mg1UYnzx4ufsieLwmhbC+xJSYHzxWRFOzQKyqBo0zDYYlcRmMpthfqarzK9rJbbXlqiW0fzd5bulsIuWLDzlJb2jdt48wTTEwqb61Yuotsh70h0wjIXSvX55WV/25jiSRFmsszGYnzlZZLKa8NqOZct3LIMwIHo2RjTmKjocJwm4+Msn1jl4bqpTuGp1uTV7Bbb+9k+EygiNmrsjFXbbEiPO+skr+NDb7TcMZZAwrE7cEn6+FBeEjRLTlRXSKfJxlmoFPDsarobLj1oBmkyVCRoh/VsgwF/r/HXTR+2AoUVweF0bYbazUVL0TfrqlHSRsD5rC3V2Im3HBkrIUk2Zl2tKDKS2u6wkcNjEZKrviL3Q4YSm3SrCaXQ83U68Nlmo/vFec+WvSlTy7K4dDdbz+rz8ZboRVNt6sNgrmdo05CEmS/aG4ib4EwOE8HVQ1WWWoVZgxW5Npz+fKiCWR4eJ1otHkT86JD6Jo/t6hLujkeHAVyVxtfkcGR7Pcwwsm92feynOJkUqFwbM7NjpQOx72fHYpFquRpetmwLFFPe1U6lNVpjzXFlfas5m299DD/qu9WlBcIS1YFx0s/YccoaxqzYX12zGFbpHKSFa/CuaBFXvw/PbEPsdWZlsLXEtay55n2Sg8yCrfOAdS/hdobBz2jv2vVNuDIJQT9OD8NVUTc2yNQAI/naWRx3vczMMCqsnX3C93JDHfmrJmyqbj9Y8mYb5kphATnVT8TAYI3GiTjmEGolTbVG6njVYOLF2tGb7Nrv+2ZNVSsM1U6Z5g3AEDEpIb1EvtZrLgp4ap2uTqZZLi7oFt+utib88bYr9HKqcVvz19QFnIjNhvBP9GpNWF6W4fhkXvXxBudogkhNnO0mXQsWEQWVEKYqiUzb7G7HJolQ0YgvNC1pK6+cNbe8MrTwIu7CG3YQLPYmiycflQ9zuUv52DZVnTkkOhVHi8jUOb/nhnR7Us6oCc7GVSc48XD2tfk2F3SglVuxPCt25UaawB2vF7FMFpyfi+bN6TOF8Fade5gM09ggdjgh3xonOU92Vz2IxJtMhku1EXNh328DybGJSL1MtO0UH067LCToVkynEjfZVuLStTk6W0z3vURrxrCLVMKL09PEY0xTKKv2xvC80K497ZTHWzdC01K6mUI7L9mzNudbrp2qyh6jNmFKF0G2nbCkkK1E+agfNqqO7fVTcTyU1sZDZ4Hkzg6U2nNRVihTb7oiJSUP2/XB6vQ4LJ3MxVz7MsOuk7yxlg66jAN76eWwM3GG4cbPMu5Knnitl6dSsDOPoJPnYLFZ4qoGApLRjIi40okRWti243E23KCFEJmil0qutMzivthQvGfMJ2G4WdYluiP7MlNA0sbz+lj7RhVzu9YizToylCV2HuLlpefclXOJL4mpVNVWj/U+1k+Nn/U31Ytt3bwcBV9eK6wX08a5bqbVJAoTNBbYIijbcrqLFT30531bKsVutaC43CX3+JE6DCDCadyvw8UsJ1hm6XE7ZT1MfL+XlZ2fBytBFYY6pvtoPfh7J1FlPMqkMLKUs6So2kCjZ+6gnG3Roba0ijaqRIGU3lWeMCdu8QXLUOG4DyegVZmd7m0cbG1iCZP0uLolOPOmyvNtH+OydJ7CkYTbTJeOUoad00WQahpQHPWj6zaTNIozlxD9NYTeDycrEU2kqIDBSJSQdTk1F+XLegkumbQ+bTiAVlpnLlM/qcTCUI47dRYZQ+Un5BQTr81euZn73rXJLcPuB5QEqbQSl3wRS8bgTo9UzlUDYZBGSV+o5ZyMV1o1ZSctly4OPE11B2xx2+niiZ0whkndLmA/be2sJNnpEJl9zxsydlNnM6HG2gJVDj4fE0unuGDXIRZca7m6yqieJa5qqcaku1qMrV1wnNdcruhOFF+DzbYuiKzgVjkerMxs3sUbo1bB/KynwVI2qHk6iKycHzI2D+igoC4HpZt2PUPyVGjipVTt+W6KLUu6JVvXILfiMr6KOVOg/l7kFcduIiwwEgduVFBJu3VWtW2PhY+adTgntBwsWa8/dFcem655VU7qZH88uf55kRVbwgIY1xsTnV7dSgK1s1vRmiy1a6z1XvJFYqNL64MrNHK9N3tZXvu4il/UiRjJxz6Z3Fwlt1SlvFzOU2O34atbAdlssjtO+nknE0vihCmBsSYLTvbphsNKKa3yw4lWloIRXaYk7IYWDR8d0nm/9xaNcva5wbosUS2rbN5dmmzLr4iesLOiyYuIyea+p26LJXk1RYmudk5NpAfHlropmm35is8TLjqRunvITgleGVvBMXl9XiSbTBoizNnemtNMWzqnc7dI+eNinvl+fdvCqhoEYLFsFQtVpWtoh5csnq2m+1aoRXMj3Uq7vMXY6rLp1fpkNXLnTbZlfFmdrySesUtRDdykJFaWxp5pWjxKtrWWwxTdXmd0Bssnc9Q1rdLAWb7uuMbb5fOGB/HBSJaHvcQVG7cSrqoc6OUq0g8tn8hSnEdyp4q4ObWyfa01pD2ZSbJ6yha72TClN2QDFzPskmKnHS+kPLdElUkvylrvPbQwqA0kwEvay7O9N92v4fbLz5SZrMEysWg6caiCKIo0jBXS1BaIdbguT6xbmCrekIktLy9Gzm5IN2F3F9gfRIetf+mn9q47Ccp8dhKFrhuk5mZ0dXC5BES1UmNMtHeCSIUh6qb5ACE0I6loXK1npu1JboT5KXP2+vbSBc1JVgLIONkSryk8k1UKO7Upu6KH2AkyR2ar4hI3k5vqzDtyMUloola1PCN1cZeK1EU1+6TQ9leHP5nnLLpNcwW1Is0RRQvjzplW5q56TKJZ20V4ISa2gR+bJUPxMPSIMgmZxDMU40wW5nVRH9aCuCUuV+tWnsP+5GrHfQesi9UfAl+PKnOZhBRQA4ZnC+9mYf3x2mN+Ig3qjGQ8pb2WmwVE5LreMMKBnByq4/56SJw0v27VSMMvQ6wpmcBElp3ugHFmu6Bmc9gURwqtc10ZBJAn1/RhIJR2kMr5BRdsYX3dzm+VhHErKlyQqZA1LXEhV/pFIjmjb1y63DJX6JN0ZczoVTUE3kYxDwrXKo1MSe1W427y7hjElkCKa+4goscmIrN1Yl06/WZZaBwHWZLbqH/U+aOJa6B2+twzwh1z0DignZsp4UQWQSV1e40kINPXtVgMIC5lP9M3IDx483y2aKX5NvWvtOq2cxPdxFpAFSBIBB8oxUoWIwPk7DEd+97OTCL5jC4MrekjvGtP5uZEzktBDW4Jv97GZVFHi8zd95eIOYC8TmF3piRgSqwAv3R6mkluxQztTWfVrNowd5VwrcT6UdYXK3VCFDkDN/gLkeZirR4W5/0aLM83d2fOuH0nXNYT9MSACeA8rOQjVLJ9benSXTkvL4GdHKyjRXmhB87t9aQtr/751PqWWXTcdjiJga/iriM11wuK3vRZw8rtan7bC0mPReB0KyxySUdriZt3wsRfCH4oO76ebXzWFTgnuzCpkDClnlhTrwxZXXT1c9vNlY6aZ3ilcNiwD9mFOY9F6iAuwCXddVValvNwsVBCZ3a7Gav82hNaOO/piWCfImyYbskzxXK4bGoBMOScoPJrkO+oW5nMlipYClg0m9jrJKR3mCCnbLW2jzBZMX+d4IdUNh2baUNXyMg1OzUL2GKmLO52V0/Lp1PTXxYoPeDexaMjh24GN53PMLcmtuwtUVZ8ION2i1lb8ihTeqkZJr9eDvipX/iFlMp4Wzp1MmfrZms4g7bCZ/NcCbcnnikj2V2B6WbCMXw6zAXiYOyOKFspPo67k0PXKcLGU1vK2/kU6sNIstfeOZq6ZOMA3m86ZeKmblPYsWkNHbMQLimJYna0MIwjQfNmsbHxXZVS7FqsvKPntbOVNxNopRl0unamty27M+wm201I1j0r0iH15KS/1qvjfK+yYuQI1a3r1H7DdN2SDbV+2i+tgyhx6cAmiYOq6o7flrBc9r2n7lQtODriNZLly7AkqQQ7ynQ9VJobzgXSJVu7tmCFDlDH7k4K3NWW8XbHZBecP6822/YgxSdm7cwItF1EB2btbzCGQbfcJGN9sCMKRqoUEE7baB8kGIqaogloJ5+kjJUt1QEXDuupOJme5/xMoQyeEuhCim8MqKBHJ+QkYBIXRvKt8qyZLfJ0GaXVfFguzYmitK1f7AJ6MlDXvBKbaa7t4L7j7B+FE3XuEzSkZX6Kp0ZpTrQ5AazdbmdeYvxG0n3oEFIxX+5pg15BivMcsTl1q2tNL0ROjCaw2wvjYkvX5bSf9cpyvQqupJLQ0XZ2KHCpJ93jbTfz17egFhRTyM8Lv83EGUsFvnJghvTsno8smQwLslsL9bkAS6PqiIialusJu93v9367mO3JuXfgjaC5YRK2P67joFMlGBq8xqEToq7gvrDD5bMc2VM7WpP01Y4kgWYvJn+AW/Hl5DK419JwsRXWS3a9TaXJ8Zill9hZ9ZiOy2S6O+898ihFYbvP2G5NMBXLblF070m2MfWaZe3AYE9QQlnRAeTZRWXthOrc7Z10m+22xYSfTdXBwwWlSjJY/bqLCluJKqHVhUPvAmW2x08G6c5YOmVtNDvLwQAw06c2skkp+GaOpc384BM5xaCzpWeVjinO5XLNCE7MzKIruQsyViR5zPROzrQgOnyVA0asGV/IcZPacc4er1tjurC5rE71qWnmXTqdRGmH991Ae/hQ6nt5sbeVW7oF1qGYsqhg7lK12pdxAqNi7tzYlC4rLR4m6XI/rSrY9WoL4DKhLZxbT08WjBagGhnytsIdc/1EqxNrUqXLrpietYxalWxWtOqug39BYB34cywfmg1OM8yJXNzkIbEHYmeaMrgsXCYnUbvmkng46/7VDEDAlxjQ+bWKVhN/LlxzmGZ5QokK7hA1fzq2NUs5TUrbtktRdnDdE9PVOeLOe3lPK6aLWv4Jc/bXLNuEiUTfNniyTuYrv1s7Gy2wbG69oJRCyWkqQcXhvNitJU1aXGkdbs82i1lBxbTu1Dudu5aKnJYanvJ45/bMZH6gN1xvnukZUwd1EPW4weAiIElHAdu9SLepuJGibTfIbK/mcFvMJrXckrofL9gQc3r7Mi1vKjc0DT53zhzm2Fw1VfVYy+VG9a9nSqtXIedcZE/JnAiSKWOd232TkOF1Bjexjmv0Gwq7ztZYNiNzypDV+fzl08t4HP08VP57T4zHI77/ZyeNj0PBt8dM9wNlYLlf7rq+/E27fvn0UjohtOpxrlrFjf88gPwvp6qf/60nFKOI/vE4dnwudqvfjuJryx+/WfQSwoJS1WX/rcri5n64++nFbqrxKw7Vt+ch9st9eUk+noj/uJxR+HMhdfbt+e2Ml/FrCOMDH+CGjzHjpf88cP704vbQYaFTfcMp8hso83HFz+ce4xHt+ODj5ff/DcC11d67JQAA -->
