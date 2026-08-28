---
name: "rar-cowork-cookbook-configure-analyze-costs"
description: "Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_costs", "rar_sha256": "b3d8795e657ade0abd0f9047a7edcce847e9d4f28acafe0c06f5e31a06f06682", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_costs`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_costs_agent.py` and in the RCI capsule.

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

Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 b3d8795e657ade0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_costs_agent.py` first:

```bash
python3 configure_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_costs_agent.py   # or on stdin
python3 configure_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Configuration Bulk Setup — Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_costs',
    "version": '2.0.0',
    "display_name": 'Analyze costs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze costs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b14bd69f16ad29d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeCosts'
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
    print(ConfigureAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjSJLtX9Hc+VBVQ2ayI8i2NnuAxCIhgUCIpbIti1WA2MQiBPXqv79AUt6smu7qnjYbs6fMa1dAhIf7cffjHsH99c3ru6Rq3j6/GZFXLkQvz9MkahZeGS74aqiaC/hVXXzwswiqsmtSv++qpn378BZGbdCkdZdWJZjO1nWeRu3CW/h9/hgbp+e+8ebHiyDxynO06Cog18vHKQLP265dxE1VgFuLtKz7brG+B1G+iNM8+rAY0i5Z3Lw8DZ8SZn2aKs99L7gs2r6uq6b7BJSI7l5R51H79vnnv314S8H3t8+/vgW514Jbb/xLi4h9LsvPq4JZOVAHPK5HYHsJruuoiaumALfCKF68rn5sozz+sPiv/7oMXnNuf/r8pVy8Pl/e5n96Xy66ZDbLa7soXARe7flpnnbjpwWbD97YLpqo65tyRqUF0JXnT8+Z3yVV9eKv87Mfn4t8Okfdj1/eKqDCw+4vbz8tqgas1/Tz90+zlPrHnz7l1RA1P/70XU7b+1kUdLMwoPWnr6/rl1gw8PvQNH6s+lcg9elCP/ry9jvj5s9T79lOMPPtU1al5Y9PwXVT3aLSK4Pox5/+TGyQRMElT9vufyT356fgJPJCYNNL8Z8+PED+2wJ6GfQu88+XrYFb/x1LwPBvy31YvID6M9kP/P+b6DwtQcB/Q/wfivtHE6C/Ln7+U9v+2YQPi/jL2yrK0xuIDj+PPi9+/Wpoa/7nH8LvN3/4229A9L8UY1R9EzwkfC28Mo2jtvv69ecf2sftH/728w99DWIt8oqvfZP/I5n/CNfHOn9A8DXqxz/OBeub5aWshnLxHumLX6v6P5rfPi1Oc9J/v99+Xvw+X+YPtJiN+LboE4Lf5UwLdP0djj+9/QaIoQTW9MHjMcjy//zPxS4Nmqqt4m5hBBUgH+DgLi2iWfljkrYL8H/O7SYCuLYpAPY1DsT/7OFZ4ype/PJ/ggdJfgxeJAl/I77o64vqvj6o7pdPiyMQVzXpOQX3FzqraV9K7xyV3bxU3URt1NwAifhjF30E9PNx/gKIcfHLn0j8+pj8qR5/eZBj+uQinZdnHmr7PPo022IlUfnSPABEG92joAdy8yrwnlTbfgA2tlV+Azw2291e0jxfhGkDjKya8Um8ffl5FvbLL7/4Xpt8KZ/EiS+eBaCFwYB3dRYfPwJr4jw9J92XMgqSavHDr7/9sPi/i3826yF8XkMDzP1CHmi4MdT9AmRSX4BhwCnAjYAmHsj/+tsLUyCmBBUL+CmN5wo0TwaReInCbwAbEvsRI6mFHwFgAajFXD0AGy/S7tNCjhfv+oJF50czXycA40UY1VEZRmUwAqkeMOcdybLqFi0ItzYePyz6Nnqs+ovfeA8VC5DSXvfLYsdroDpU+Vz5mle1AJOrMgXwv7v/eR8IaX5oF9w3EZ8W+zn2FrXXeHXSeK81Yu/pF1AVvk2fy+qijIYv5Vz/ohmqRyI84QGDADLBy6UfZ5+D6luArA/bb2s/xnhzDTs+alnzpWxfQe41sysCQPpg0XMP6jGg/r+8QqpNqj4PH/gBTWdJLy+EL688YpD9Q83n/9AZcHOzYACWqBdfegxBicX/j0bioaUo6muRPa5Xi/X+qDtP9OaeZ0b52SaB0r4AIfTMlO/l/htZfOPML2WeglBoxr88Rz4wf4158hDI5hBwgP6QDxwO0JvlPuJxjq+meUDwpfxGzh8AHg8mAiaA5AXBPYPwbcH56TdNE5Ch8/X3Qv3wXxPOpoOYW9S9n4N4iKMofIDQJc2cUy/4QXBGc34NSRokf7BqAaSDGADyF0CJFKAOCPwB3b4CZoJ0enjhfXg6tz9Ai7APgLagqYw+LSyQFnNotCAXQQ8zjwEo/PAQtSgigDFQ8R3hNvHqpzJzH/pS0Jt9URUgWn/vgdfD74H80GVWH0j1gO8BlsPMp2F0f3r2Xc+Xr4CyxZx6j0l/dPfL1sXvq8hfvpQPHd8pHGR0Phfg34GzAJlUtI+QmwmpBaRSRK8AApHwqLWfnuXyWY/fdfn8d833j/9ef/4ogOYfPfd5kXRd3X6G4WfR+lazPgE6gEGMpHXUfq9fH18Z9vGRYX8Q90Tn8+LfU+kPIl6x/HmBfkI+IfMjJQ2iOVhfH4AA/5FzPhLz0y+lHn137cv/M4fmIyiY7wXl2xBQVc5NdJ4HPwtMO9elAZTCB6MC8L+U7+5/JceTWUA1bKvfJe2jsgJnPn31TvzgUdmBtcO56zpH80Ykn9Vvo7fPZZ/nH95Kr4j+yQZkJnUQmACEebsCkgQ0L10aPa7eG5n54o+brEf6gLwPq89zFn1YzE3nh8V7//hh8a2jf+yNyh5saX6ee9d5STAU/Hof+76D86M3sHXqxnpW+LlNmVumVyv790rMyQM0DqK5UFfv2Tiv+HdCwJfzOWr+Xoj6+OLlL0poO28uu2n3LZFboGfYzwQOXAYSDOQMoMIeTPj7ZcA6TXTtQX0LZ3O/4/fdrOppy28PGLrnXu/Xt2/U8PLBq68Dw0EOfmznCgeD8AQLgutnIIFn/9OO7zUNcBhoPcA8Hw/pJUNGFLkEGx3E80MkZhBi6S2jMAgimlhGTEjEGO0FXhwhAULFZISjHviNUBSNAXnPKPw6V+90VgXzvIAOligRMkuPCiIc8fEgQjE0XOIRQjJ4TNMRAVB5n3oBBPiy72nPDN578znj8DLz1zefIsBIiWhl9vnhYebkwcTS3ycKhCMwZ8Lw4Bc3xfBI297gSuXeuk0SnQ1HC3HOFtCO09cFNm2J/rpVcdE2pkMCnY/MBQTmuM6N5XbybJmQuOslMzBjgCQaUh1/vKwP2ZocCwuFT6l87xolRVVduXm1YlnFMaVCNEzN/iSYNtGEcZyYpe4KteuY5u6AXG5+ubF6p9kYVeau4bTNDr7GyZQC1dtSQfcn3rPUfHcMPLXp/NQqTCrkNkVZZUBKe7sYXUpt13c38TR9jLWSxGLtyFBBbOCq3SAkPBGmzzgXbcuY9jl3T1h3pIqqya+OiZ5q/xIk/D27Zi6cWI69CbFtbQaZtg2FaRvcbs7ROKBFWjgmH55srzbLDRS0eFoHqDVaAiYQF1MYLHtD3pnO3VL2mDtHTN14ueubE3Ifk9AcDsouzI4u1VxPIQJH6X4fXHO8SPXtxTApF1lyYoTiYrFeCua2tyego2zsy7YPitNu3d1bxt/0gG7ZoMzz4qBst1zi2+pxwIzbakfZDTl1GH0hPK8YYrQqEUntjMTaLhlvXBdWaN3FZtpPB4m7w5OsrPVWxCjvjDYCrgxFno5pZx1dhZlM17oWHSrml1pkYc2kgrV3QO/rK2VV987RTPhkQfHmlME3iU/Jc1SEFtgZMEa89vqgL/YIJDVCH1xOltszZeFMCbZBBX1rb7PIJsZSh9zA9vyNoQl4FqGilTorM1FuSXalzwEVcJJ2tItt68JEn/Cya8TO0O6hpbQmdH2MtnlWbC3kTq7IaUndyGITnhwrnDBnoyAT3Wfsvbhf0kMSb6e62Zm5GhuoptYegbhkSkIrXuiTDY3vlsIAcxzEshkOJWvzNFHalDFUfKwZRtN2xzN1mnopqsOmvenWXeiSCyrbuYug5rglrfp01d1dxlTtPh1xXqA1J5cHyKvx/kLzSULirEjiQa2qhxWJKcS+ovekNYi7qvE36DUVblx4EAaf04XjyRUv9jn1LyGS7tjCI/Tjjgu5rdOlY9/sAnVzJlp36k9rR7LhHF8JHaxI0yHSmbWy1u4lFXZ3oovNI+aRVIklnouvvT2+p6UGQq+kNdWbmIZZJdTvB9PxYiGRQ69toOPWudm5uM2jgSn9cXNt6xKX1pOoekOHdEeHl1KbyMllQlBeRQn7JoKbVE6N65E9IufKR45qZCJpc0oVqYDoxk18qrDIJN5MPkXfQzg96W7GhdH1cJxOlB8gzZry0GseU1UunxLTC06Sjm56KrlrxbnIoWtp1f5WH69wHco3KwBZV6vmBl/b2pmiK1z07t2qvqv6iri6kIxiyIbfWXBsY7JZ4UMDE/sjLdbuSeB7fNnRdTkW2k62IlHwDVbxQrVxIbO3fGkVypVpbImzBTAenXtTeub6IoItGZXelXxHjB5Pj/fB5kQkJeDCb3PviLupL0GlKXpXW4s0JjJRfiUq5bAbqUnMUu2YuXZ4dDbLjXuzt1eJPWpn7BbdmNNSBhaiLIFp6v3MIvCWF42uRQ6rZohFw3Ej6rLHjqggEmYyokrqrgA+DnGmXQz1kUpw1BVyOi5pYOnhuJ/WtU5nioAxPJnlwDEnSludyK5Gsq7lxZUsB9NWC2RegLj+jN/dmzDurrk6kJvKCQmfVdQus/AmUFX9eEBYycgE80S4MqenRoHpQhQ0jr1izXO99hKySC++mcu4S9jaPcHixuAvWZfbwoVH6eyMqhBOBolbbuqlbllxfFudmQg/3ckrn+8EP2v2vXZBqnF7Ky1S9KYNJLDKXkxcGqfpdaC0StOoiqNx+iFZQVuppONaQOlewokEQcK4zsgDvN2e9ZMbQb6fXljWGBzKbLtVUQRjK19W5kidVOp8Z/cdI03ImLqZwwmI2PT2WZiqQj+eMN0cNSNWh2xt8vvjfodcB9vbOhxmXFaNsxkOmnHdH2zywNkree/hO5TXiCpT91R75Cx/VyAHfsOuQbuAFcmYWsJmy03oBV4lRmvyG6ga4uweK9ABkVJUOSZ22IMCGN75U9F6WK7lZVhod93H2lNAjdDZ6aDdWslEfxcG4s5x9k5GhCgm4PTOpfJlmI36aCmHi6JPSZ22tREcLuk+onGmQ9dLuahS8uCIbMcpcTXw1jEYt7yh6/0JJcUeVZ2ME5JTYBq8ddHPInySPEvKO6epEPhmKQ1HLWUZJyw5sgK99e0c27rh6YKpcaAEXJB7uiX11cWrLhR/dK5lWhhot1+PxpyF0DW3yM3R8FlO9ZHkZlOsy5nSnle2t6I5Z9lywBJ769KsGXCoa+RrUb8dtiwvnT1bMJj1pm9py+5IY92v+jyrVvwRr6710Q+MljhVU+Cu2S2hbvxhz2D4ddonOSiK+KQa0IY/hPdljvji2Lk7VzQ3pyri8xB2i+tq3Se3mkBrQxhH5jqeOz2cejfy6rrON9YKPoHdgFyLbc8IFbcVJrvv5auqwZIhXxjZHY1szEEjgbhb4yCtzdy+yuikGx6KBWIvMVZeJIO12Ux3ccndWBv0J6ggiPmh489Um9b+cFmfxVrFRm66kZ0cF4lirKSDzOxgyBH6sOwHD+0kmTOZ/LzRQdFY2pJvDNNVX9dugV+ICILoeCPicDxseJu9mOflhc+Wx87g1tENFDIk6nMipU6x7eaIusTcVg+yGtVq37/ZPtsiGHHW1zvB7ol2cwhNfntZOcTaYyM8avKNxsEJXwPP7bhjFeh6dJsQqu71Rllfx/EcKsW64kmVFPYJlJTGunMqVBakU1TyFYnnkytfzSWCZsXeWuamaIOiZLaocmu0g3Q67+TjzcrJhl6rHu8BvXKVC9qVsQFkSnlOOq7W8A63t+yFOrBky4/BubvQ+XFyYdNCMGadRc6pWaljipzjkahhx5xWa7oULOjiHijVrHVdWA4pkR/IA30JMkcbNgZ6KdTIOOgIZ0UJBwnRdUivWVabqo46S9lfkwFlFHXgWvj2uGGqYYDZaj84B1XFTkeoVLdDxeo+2BQOrW7lYdCOUXXa1saUihOK+sukR8Jym3uCd6sSpU3QZcvZ5BXNdmS6V8d7fxK1fFtXLRm4Jw29SRp1vVT97o5lTQ3WpERVDOFtXmFNHCyDZocjJnfb9Vtrayi6eN+CnkOn6ornhjJlWKr2tpzakmJayB2TOnng1cMedBqsAnmrZc1GpiV3O1xbQfXexaP7BCnllVIR7IAevD45JwVDmVe5lnnL6Lx2v2T7u7o7s5jBDx2H53yXdsdA8xCNi/LDGJk6dRRSUr8ykqLwy4HB2gMhKGqi7kqcTU3c94wzTOvFtK+a223N+159Vt3E2FwK5npU06CZcAMvck4W6SNNYDu4hHS/CnxJMZL7NrBlcRUY9YF2rvVyf/b2gsJ2Yg+htJBp/E6DCoBRfVCkIBwVovfRDba8Ga55KTgRkoKuHStTwCcJGUHsmRTDHaP7yItju77d9ivMYTUS22W7pr9tjqGmXT1ZhPlaajPZGXshzS50lPenDckiZbvjxiGw+Hbc7VxIuaed6Jy2oi/f63JzIl21J5mwqrxmd69YHuGkxp7sRNGatqHZOjHW62mdxY2LOqpy3F42Un3caHYVbfa2Q29Ft/JcUj/Y/qld5pR5I0WqPsjLvdjXt5oXDzrXMtlpecl9xr0qdYjlw3Y1JPaghUu2Del66AZDW2EVKjVYI3cwRpWnKQrDbakZEoeHd/xw40d4eXaadAwHGrf2Z1ekyGwj6LLW9UsdK6WrtTJsT0/CwTvCej4o0jYLulDupk6WwP6x6TDvthtZ0CzLkzuk4UW5CDfmdrarVKyz4sBaOY4PTruKUdw9wUk3hIMK1cEIn5fIzUMdljF0xl8PZBtKMXu/EYYCWUrf+fwBC7FTt+zYRhGZrZa1HCgpN58a7Iqm84nuUAYeTtDhOgxNE8NUAme+Ydm3MICGBlseNkyuGsn+DgoGVukmxd/uQchXnI1IR44JHdqIkdX6MjiqHWyMLUP4h2wzTWuGV2WN93GuFe6GRrRZRS5H+Gg07nTr9Yy16ogU78heujmDd0UvfBVRAV7uVbq64/Um9SvDtA4ufGBExjVcGnTvxf2Er+BQhTl6z+SIOKWCQAVOzJLYCbcdmwalfKnIWLLOJiT1k0BSthBGr7gLi1g0JZLe/nrcUAqK+Mvck6AQhWqYujN4JrBWKHYQt+tYYV+saoYW7ojm9/El3N1BZ+ej2CAkJhTmVrkpumaJ2QLciWG88wQ8ISuavOO7CYrCoS8x0T+zCo1usYgbbvcC6MFdlIC4HNuN1HSUabZ6zzhw09RrQzoP3GjVEMMH5q0dg9tpTcOZzCHORE/JKAd8gHZsgWeOeuTUIYWNkrej0L0zxOp+aDc+52GybXfGUYIqaXUnGL7VDrHHUmuxLboQh3K6X/EsIbeD6chY5qr3XSup6SDKzpZimP1161Eru5BLnHZLXkcgmr+RILmxmxTWp1TG6KOvRsWl2LSuwvlhJd7jpXq/l9mGi7QTmUhw3HZnDUWleNNETBjt+sCQ1qpfRUeNv0kTh2mrlYUADiiZ805IqRXC4E3cUF2hBBHGILuDkp9b9V6hdw/np2sY5HBeWjnW4S6zneRdGFGVKBN9REjRKiFkevDYc6lR3MFgeAYKRU5gIT2DPEmHULYitYRiNqiEHWOLx68oAfd3rF+btKzouEK7A62gOazT6rTvctwNbYYimziVz9xNSsqevklWFSFsm8aZtD6hJWMz/jAdLuhV7ykcUnGtJyywycB3OAZzMJz708RXPsi6oxsZS7hcr0DLkIiFzDUDKqRoP8TTDSIIUbCX6V4y9nakn+gVnsfZClkd4ag92neThnGjl6kd5IkECXYQlxJz8MAqaGsckcmGO91iInm3M6EVlAzeLpAQcdVu16JT6Ld04kD7ESSmidF+0JUmhi0xpHS1oiTa01njkYynJHwb1wh55ohIWxF149HKkuTQYlWxQpPwkdIcBPLGFbpwgmqG3HlnFyGv3G5345O2wxxmy1/C5dY6YxGZQLv2TDH4nrwsCZWJ/GETCLdwG6wgtDhD99GzmwjsiQPitlSCbFSX/rgmKJHYJDHpHHrQW24tVKOvBwO0NjGjFD6O7wip2O86jiRWS96RUhJjqp0uI7AJtm83RmBLqLpoV02+0giclZIZST5mqMPo7S1Y0Oy1HGYwsSK9nFsqbM2y7F/fPrzNB9KvY+V/9Up4PvD7Xzt3fB4RfnuZ9DhQjrzw82Otz/9Sk799eGuCFOjxPElt8/78OoD8b+eoH//kzcM8aXy+U53fcN27b0fsnXee/+znLS3Dvu2a8Wtb5f3jAPfDm9+3898itF9fB9VvDxOKej71fl9nPqF9HP5/7aqvzze/b/OfCsxvbaIw9brodXl+nSd/eAtH4IE0aL/iFPk1aurZvNerjPk8dn6X8fbb/wNkkgBVVSUAAA== -->
