---
name: "rar-cowork-cookbook-configure-analyze-supply-purchase-plan"
description: "Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_supply_purchase_plan", "rar_sha256": "51e1d224aac770737b7d1f1a4ecc7c18ce9d3ed488076da7377df65431b66ae4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_supply_purchase_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-supply-purchase-plan:248caac090c2633c411871098b5b4d554d91a6d474e74458f68fbc120e3f8d7b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_supply_purchase_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_supply_purchase_plan_agent.py` is
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

Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 51e1d224aac77073…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_supply_purchase_plan_agent.py` first:

```bash
python3 configure_analyze_supply_purchase_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_supply_purchase_plan_agent.py   # or on stdin
python3 configure_analyze_supply_purchase_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze supply purchase plan Configuration Bulk Setup — Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_supply_purchase_plan',
    "version": '2.0.0',
    "display_name": 'Analyze supply purchase plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze supply purchase plan from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-supply-purchase-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-supply-purchase-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa9f366ed2966660',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/analyze-supply-purchase-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-supply-purchase-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeSupplyPurchasePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSupplyPurchasePlan'
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
    print(ConfigureAnalyzeSupplyPurchasePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjyJbmX6GjH7KqFRliB8W1MhvQCpIACQGSKssiWZxFYt+hpv77OJIiMrPr1u1bY/MwSotIAcfPfr5zHI/fn8yq9JP86fVJBWaMLM0wDHyQI2bsINOkSfIr/C+5WvAHsZO4zAOrKpO8eHp+ckBh50FaBkkMl3NpGgagQEzEqsIbrRt4VW4OjxHbN2MPIGUC+Zph1wOkqCB9h6RVDp8VAElDKN3NkwhSIEGcViUyb20QIm4QgmekCUofqc0wcO4MB/XyJAwt077eeCV5+QJ1Aq0ZpSEonl5//e35KYDfn15/f7JDs4C3nqYPpQB310K9KaE8dFCgCpAF/O1B2rSDfhmuU5C7SR7BWw5wkcfVTwUI3Wfkv/7r2pi5V/z8+iVGHp8vT8O/fRUjpT+YbBYlcBDbTE0rCIOye0G4sDG7AslBWeXx4LECujX2Xu4rv3FKUuSX4dlPdyEvHih/+vKUQBVuTvjy9DOS5FBeXg3fXwYu6U8/v4RJA/Kffv7Gp6isC7DLgRnU+uXtcf1gCwm/kQbuTeovkOs9vBb48vSdccPnrvdgJ1z59HJJgvinO+M0T2oQm7ENfvr5r9jaPrCvYVCU/xbfX++MfWA60KaH4j8/35z8GzJ6GPTB86/FDvn1dyyB5O/inpGHo/6K983//411GMSwGN49/k/Z/bMFo1+QX//Stn+14BlxvzzNQBjUMDusELwiv7+pynz66yfn281Pv/0BWf+PbNQEVsSNw1tkxoELivLt7ddPxe32p99+/VSlMNeAGb1VefjPeP4zv97k/ODBB9VPP66F8rX4GidNjHxkOvJ7kv5H/scLog8I8O1+8Yp8Xy/DZ4QMRrwLvbvgu5opoK7f+fHnpz8gSsTQmsq+PYZV/p//iWwDO0+KxC0R1U4gEsEAl0EEBuUPflAgh0dRf1XXwmbzEjlfEXh3KHcIEWYVlsgyN4MQgfUwRHywIHGRr//LvgHqZ/sBqON3kARvD1h8u8Pi2zss3hLn6wty8KHwJA+8ANIhe05RENMDcTmIvSVIUUWf60Ey1Cq4I89+KgyoU1Qh+Afy9d8T9Xbj+pJ2g0FfYhghE4bNQUoQQYQ18wBCtnnD+K4EnyHYQlT5gOHhV5W+DF4yfBA/fGdDPActsKsSIGFim3dEL55h+IskrCFCDh4trkEYIk6QQ3cleXfH9yp+HZh9/frVMgv/S3yHZAK5t51iDAk+FEY+f05z4IaB55dfYmD7CfLp9z8+If8b+VerbswHGQpsEDevwbQOEVGVJQTWaBVBsgIZEgQC0C2Gv/9xD8egXQz7JKyswB36XjmE6LuEGCy4x+g9QNDmQUWQPyT96Dek8aFfkKCE3oLVXjx/iQcWCSTNmwB2yIcT74vvrn+P+F3OEJPi4UMYp1szHWhvuTgE005y5wURXOTDU9DcoXMOEfWTooTpm4LYAbHdwZVm+S2EcVIiBaygwu2ekaqApg6cv1qQ9eCcCMKUWX5FtlMFdrwkHDp9/uiAcHUSB0PgHyl7vw2Z5J9gjvHvLF4QCUBvIqmZm6mfD0PBQOea94yAne59/TBGIDFokKG/gyFGt9q+ZR73r+aL6Q9DCT/MKSoEoRT5UuEoRiL/H8wwNxuWy/18yR3mM2QuHfane8IN09dg/31gg4MEAgeRe/V8Gy7ecegdob/EYQCDlHf/uFO6txy709xRD0KCAxFlf+M/VHt+4xuUMFOG0Of5zSNf4vdW8AzdA+NUDCbAgr4O8JB8CByevmsKneIP19/GAuSehIPpML2h56wwsBEXAOfmhNLPhzp7RAOmDRhqDhaG7f9gFQK5w5SA/BGoRADzF7aLm+skWC9wlLpH4YM8GIYtqIVT2VBbWFDgBTGG/IY5WiAWgBPTQAO98OnGCokA9DFU8cPDhW+md2WGifihoDnEIonMEnwfgcdDmKtDz4HyPgoRcjVh7KEvGxgEWGftPbIfej5iBZWNhqK4Lfox3A9bke971j+GYoQ6fusIcIgf2v13zoEInkfFLeVgI74WsNwj8EggmAm3zv5yb8737v+hy+uftgE//b2dwq3daj9G7hXxyzItXsfje0t874gvdhKNYY4EKSi+dcfPj4L7fC+4z+8F9/k21H3P/e6sV+TvafgDi0dqvyLYC/qCDo82gQ2G3H18oEOmn/nTZ3J4+iXeg2+RfqTDAHYQF6zuo+e8k8DG4+XAG4jvPagYWlcDu+UN+m495CMbHrVyxx3YPIrkuxoebBpiew/dB0TDR/EA/s4w8nlg2BKFg/oFeHqNqzB8forNCPy7W6EBimHSQo8MuyhYQHCMKgNwu/oYqYaLH7eCt9KCmOAkr0OFPd+A8Rn5mGSfkfe9xW3LFldwc/XrMEUPIu+SP2g/9pkWeII7urJLB+3vG6ZheHsM1X9WYigsqLENhsaefFTqIPFPTOAXzwP5n5nIty9m+ICLojSHZgl79KPIC6inUw3gDuMHiw/WE4TJCi74sxgoJwdZBduzM5j7zX/fzErutvxxc0N533X+/vQOG8P3+6xwzx244G9OdYNj37vx28DeHJjcZq+bn2+z6xu0MRi67nePvGGEeLsn5NMrRB7w/DR4Mw9gO+tv2+2nu07QmG9TL+QAMeRzMUwRY1hPkBPs7elgyBXi33cChtuBc6Mfvrz+9aj8L8HgFSdZ2zRtdILaOE0QNolhLIOhE9aiLNKhKNKZYCbtkAwJGJKkWJdmXcvGcBQQLuswFlRliGlkPlQZY0M0oBEfLv+/HOKf7lxgH8EpGrKhMIA5OE5CZRkGZQjGYhzMxUwS2DZjY6wNJg4BHJJlUYZ2TEjAOC5NkQRm0bQJyIHfY3a4q/b2Pqy/x+eODG8QUaNgUByHolibwaALGJO2AYFahA0wHHMYAqDUBDqABSRc/7H0EaMhhHfrhxyGsyOc3OpBzu+PmA95SZOQckUWAnf/TMcT3bSMsbX3N6M8HLUtQe8ILdWikgk1We8yuaCrHS8ty4BaN+mRXBNCaO2w1jColCf0rcS5qD4+HYmN0suUulhr5Ia0Z3kyn3WT/ow7IeUa1nwtJEuRPG4lhk1O56rrZyCw1ikqmqh6VsmNbWRrXyfx0OywtX04Ho5kuAkPTihviCPBHsRJ4IV7Xe2XV58w54srvk73S3xeyyNubxyNhJ/Sa7E04w0m6ippyKF9sU0lD63AqGzS3mHhNbmIlJK66cLddvoeVfjAVeIUd5VDSbmuKcmrmhrV3crYtGB9Xof6VSvPC7k+rI/5RQ9OarnLLU3L1D4+ygdiduwNIZpsjPC8yXcmE4dmg19a1A/2C2EnTa+OLqcHsXPjmcRku1Lf6qXTjkRqZp/1FiSnfGn4CzY3BPoSGaFhtNuJBJKjg85t8hKas3gxE4KarNaEXE7D6KqGu0zS9SXWMh44KIqjJoYa6eyYSBYzP7SSw3Qxj06+FZ7oIyDsPcn3pboCnLdJlvmkmmaXIrVXkyA7Hlyt2kbYaU3hjjS9hMcsXLejFRma2Bzz93ofngsrKVaYz7ZCzuto1GBm62T6RkSvaZ4GqHpICboNcys1U8oIvXrTKCtotLT3RHyRyVbAY0m5rY9Lw5KPfZssdyZ9AZFxPNYKvcRlYstbR6ttZOOgUmKH9xNFdPrlysznOtwLRcS5JkTnuIjabVSH451hSGP+yJuoaNtz10CXUcDRIzq7tjqhsAvUPk4zhp3NnYQWWGpyjQVSNMCuw3VlZynuiDHNIDUcnTBpQ1XZwtIYsjwUFMMJhJoy09088nMG5bPhZ4Xy6cFcGWe5x6T25IrY6OgRRy9TEtZtuVHDZpi8sKJ03DhhLNDjcbRiz10j9+XRqEtyJk3DkTA6WSdHWoeM4fCiON+kQDd8sW0is7OtiJfw7dmnBInPUGUk+k1lG/JJbOVMErFufZBPOY9qZ980po0unRhZkrzyZF8F1RjtxOlCuKI7dm7Zs+q6v6Ktwa6pbJ2JYigb51bM/VZabXJfb/Kco8d2eTrzY6k4nEXy2h1kcX5tVE2IlscEP6bxnFaX6bbvlZI7nkUvXrmLfWal1zTFwzGqTPjCo1XZYK/JgdmuWGVkBGTphKx8VU8m2J6iQj3XtNT7KtfHF02PysuZ31zrNqIYn2SygtalfK3kM6ClakSr2pLIvCmbLNal0rT1jECrSBgXDV4IrWy5m0XCsNcsyFbbbrKf1lmYHc5oytJAr9buEo3SDR1hZFxcotKRPBXwyUIYS0yqSuFqIelYiflZq2+DxX6XH1BXSdbEBhZ9a8ZWmgSHPhVHom70ZcAaE9cQxa2AzTKXlbbbFa/rKV+VowsVrfLt/OTCXtUbpKBxeBfNsYNZ2LZIXpa8mLO8SZd9G89suu+C/pzqIJkFTLQUwh3hHU8sOcPT2YqdOHqCWpZksFp8CBeMfTjbIlu181yxd9ROCnXZV+wrLtNRIo7nVEGogSuMDNf2AgK44+UyHQPOj81DB1SQbhcLuYNprpw01DWmDpCDhRKp+kzSzufg1M+8LYZmhelVGjWdTILl8bKmzZgceYDf9UGkUXI7ZlpyfEmjEb9fy6JLFWrc9XvoSIoP55zASZJmkq6wCa4ux2/bJRaQB1LcXCNlBn1B4xugl+DoeuKa2yRiYCxMLfPGqh7F4my9DdJj7mmcSurE5iLYkX6Z1mGjU36Dz1b+/NqZ8rmWhcQu3V1mxTJ9ci6wfxzbqUNh7Gjco4x8XCyt+by7iAZJ09ZlJK2VZU61/j6qbdf3lvU+heoqNSMK6dFxdh0TdRdhRx9Yu14tEtTOwPgSCuNmc6kEYm8QKnXGajM+idQ0Tq47wUQvnV7phrap9SBxttGeyiymco3jeoPzibMRJF2rOVVr7YzO7CiZatfRRKSFlUCS2Pygp9W8RevpCc1nG1Y8FFc2O+EencqbIFlNnOiwDSdYtvRH+ULZZoswyLtwew4X46V+yeg0x6WJzHjEculUWjz1RMfgSEbXzBqjajWhT9YByxoGaJNTZjiRDgelhtv7J7PAYL6Nwqpkt9r+sskFx1a3p71BxW24KVN5iS7dkHFmnTE9O7vKETvPWKrpvleNzX5DueOjfSlsEKwPytQpmnkJ6pnM8UzeyjM44Ra6M79WoZVfcN7TbXQ09TuVExN01RmL0LGzRBvX+KWeMdmipyh14+Ibvz1hIX1NKtrnsZjgLY5R9FY6Abr0s6nJrVfTDtBFbpCt6pN1dojbUrfUYHw5c+GOjoCEewx3RDddtDAOOrFvC1aiLMwendaKlxWpVawEwuPLvdVsQ8grwBp8b+XdmJ8mfGyg2Cz2WPTonKVMUHd8NCeWeyEul8JkUo9qhjxHeidfRZOPR2DebLVdrVhuHFXnLerpixMXwa3VuGA0izZ2BEnPzMR3qlpIklI7cgx7jK4XKfGtndtV+ZxacLiDeVtudlgDGGIIOAuf8ERFNbV1TEY+7aCizO/iqVYeA3518Y+0CHErVKcFnU5pVrXj6RJf0udyWRDaLlBFPttvroGcs5625ZdcZxa1zJ5NY+wvxAN/SBRwOY4j0copqpBHCt/MQsU6cwxsTaU2IfLwjK1lXdtRgb1x3ZFynTijYrugtnNJ5axitrKw2gVzW26JSSbJaN+7p1Fp6N3BukRNaG2P806HKQYnzcluYSurZtG4m8jxOAjCLcf3q+zCt6RqrDV7xpirbt6tLfVyZtUpBVY6rkaEpU0FKUt5o2FU3jvQvEa5Ud9ODXRulmqeVb2/2zL0eTZdR/KkPy1yvaK0WSQtjeRoeg2M4IbdLRcNQRksdr3s91x0aWi71+x1HbiVsFRJe31u7MkmTLfRufF8/xQ2/tLKne3ViEepRHpiiBUoMZ2eF+eKm4T9DszreLk+xXOVvZ5PrUxk01jJc1FbpngQrheRh/rrSb81HSoPZtruPF2uClVZ1bi+zpV1tq8imlqBQ+K3jeWlpVyQl1VB4w6pZuEo8PeXvQN3r4fV5KDtMy/lCOeYehSm9dFZ0VTRrtP95qSaE9Ylgi0GN4yqv6PXM+6SHpUUS0+MHs6llhClNoLDQ55ZoppRzthSpPEU6Fi8m/Q5kGUGkMS1JsUVmwt1JQPcOI+Y+RGNHX3OiGid+LNuV652IX6gO34eS00Lm5DmYGd1W7nqkVzuApI4eFYx17YAxdCxKjRZCVGjMlaUmtHbkU/DObfsq60ShIk539CuGu1CbK5N+UoHtSfgh1qau2s+n4bMjteClRNCnHIXdRXAHqQJSXQFIrUPdaoAgnKERWz6TIMvAncRZ1strTXNWTfkRVywvb3FjtrMEbB1eJCkiAC7OTO+FIuxuJ5qea9ceguXD+dLvN8v1xu1atfb47IgZ5w2C02WWuwZi1sk62xlLbbdlm0vcpdwo9hqZhwqaMWkEkheHsN+awSJt8OanMwjB7SVPKM0q95jfY3x1WUuJGeh6RiuGLUep/i8uaQNaYFpkrzHmi2vHIKdJZDcksJLlCXCMA93+6svWDPe3vJpkxcxJ1/WLHlktgI1k6/kpNFUtCKIE1uh9kyTVZTjaW6lM/ShKTGstAo+81VNHMFt3liW1M4e5byIGmpOaJuTa8zllS+btlEI/bqIKjex+NDdXPJduSzXLJus8IUwG5th6LsSvU2maWuv9yNsf+C2qXXq4R7Kuaxiz2H4tUOnXdkJCtERga1McTPGGY2tZ92GD5VJ6jAJwVaRInYTYmEcx3Efd3XJLHusHK9kXfA3MiEf1mcnxcX1HJvN/IRajtpdI5vryAnkFMfxbpWncjHDTWY7Shcbeh+pMcUm3ipQlX1aT/dTLrKPe79xx5i/Pow117MlmQ9rbTwCsgIML8ZkfJQ17Si8ZKzBeyNSpiVP4WdbMMo1k/GrvhhLFU1xUieMZLLFFIehCZruVxw5PrjjcamPGw7Ix5Pp4q5LBu4hbJmMqFH3aMxWRYqTackxe6Nbldk1YS+HJKlEIJ6lFdYf2vN4d6D3+xmz6HkybvxyKa+U7YmaOx6ANXwxN5dIbs8rn6gtabspCZk+4+srsT5lhJx5E4KLTyau9Ut+53RsDTSb7IvdNVoU/mlv7QlsKlvtNTyOz+qkaqoJnK8JWhlVpyKx5A2rWNWMHMv4YKBbz3rpil2ynbh0VaE6kwBlGqoxbX9Z4KF71A44JYSJZam1fEjdBUnQxCRfHeFkLmqEd6G5czEVJ1sldBypP8amUmdC2GE0o8+CYLPlVnkQwC2KZRBs1LrZiayi7axfEmpFdj7BjCR5tOtXe/ngpThDSGIm9uwhhJkQLC5OIEwWRE4xC0uZGow5mY4bb8njwSlm6E2rEv66mBwvfT/lCPcK9wTafkLqS0ULylOsyK27PLiXXKaBCMsgVog5WC+CDc0f/VkxzrrTWPIa2HfYc8vMqN3q7Od+XjtEetl4pCdvN9uwmO44HCtmG5kRt3LFTIvanZn+jnAzr5Ukdx/Y6UG1yHo3O+Krc+F0YUReLAxcSUYApySZRAVNHcoQ3TPc2l+TOs3IW3Hs9IrlTFw+v1KVMz5JFTtdbAtm75zGnItFfAlkUNTJ0l1NPHRSkcGcJpi2b8SlYhpRw0gnvtGMsYVa59C6OGhV+c7VAhmuMaiTHwXT9Pp6JKLOJr7QMhFwB1iNKhwUJ3ZD8zXJnAif26sKq02WcB9bXkfKpTkU07M+0ftRZC25UUTsIoIV7EbYTXBCqvDR2JqWEmGMgZUTMeG3u8OebcYE1DE/jtdCfWWCnFqQ/ebIAG+i6KY/OTpKcWHYi+3LVTvpE0ZKJqNg4kpCzIw39Aw/enWt7wKKb9t9f10QyTRus7y8bLvxKd7ssvGp33v1kRCntS9jOXsCvLmbnqi1OtrAJKB1it9vtsbZH63atIlHJ8I21qzRsSh6adS0bYrisIkUrk9OeDXnJd63VH4WU8mpsRtnJvecTkcoF9Ir4GTy8RIX6ihfUrS3NDzZH21WnS0npqOsWva6wKz5hFkwPd/tFrk3rVb+Liy9mT9ZarI2oYzzDiW3PU9EqueNdMacqR7VA9jZZKLSwGUjC3UZy/IGiHVfk/vV+kzYNV8DFmOAHS1oBvqDNqMJXu+A5aJnDRIncTtaZ4ncqyDrSAkY7tqbZu5kvpHKOnbKfCM7WEfOVlx4CUzL1RbCzjTPwVLD5etiLQWbTRZtRGWxJDFncSmpix5vbZ+CIEfkQVKVJAs36YSAn0/ThOO4X355en66HRg/vWIoS7LPT8OxwuNw4O+/Vvb6IH178CMYhnp++n/3pvP+1vH9CPF2VABM5/Um/fXvqvrb81NuB1Ct++voIqy8xyvO//Ze9/O/98Z54NHdT8CHU8+2fD9nKU3v9lo8iJ2qKPPurUjgxiq4/UmZVRXDX8MUb48DiqebgVE6nHZ8iP32HrZM3lJz8HIQD8d4wAnMEjwuvcchwvOT08HoBXbxRtDUG8jTwdTHYdbw9nc4zXr64/8ArPBYkvAnAAA= -->
