---
name: "rar-cowork-cookbook-bulk-update-define-accounts-receivable-strategy"
description: "Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_accounts_receivable_strategy", "rar_sha256": "89e06ba8d1bead9cfad73b4ba70e2e39fa9ec444e4e8dc80fb1f22692795c626", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 89e06ba8d1bead9c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 bulk_update_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 bulk_update_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_accounts_receivable_strategy',
    "version": '2.0.1',
    "display_name": 'Define accounts receivable strategy Bulk Field Update',
    "description": 'Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6f2abe196e1d0a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineAccountsReceivableStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineAccountsReceivableStrategy'
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
    print(BulkUpdateDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejxprmX2GyP9huZaUAgUB1zz1nWCWQWIQkhHDdk2bfF7Ejj//7BJIyy27f29PumQ+jqqwSEPHGuz7PG0H++mK1TVhUL19fDp6VQ2srTaPQqyArdyGm6IsqAf8ViQ1+IKfImyqy26ao6pfXF9ernSoqm6jIwXSqLNPIqyELsts0gfzIS12oLV2r8SDLqYq6hlzPj/LpyinavKmhynO8qLPs1IPqpgIDg3G6V1RuDflVkQEloCgv2wZKo7p5hfqoCSG3Gr9UbQ6VlddFXg/Znl9UHtAty6LmDajlDVZWpl798vXnf7y+ROD7y9dfX5zUqsGtFxood7prxd61oZ7KaJ+6HJ6qAFGplQdgTjkCF+XguvQqsFgGbgFToOfVj7WX+q/Qv/970ltVUP/09VsOPT/fXqY/GtC2CT2oKay68VzIsUrLjtKoGd8gKu2tcfJE01b55DzgiCgP3h4zv0sqSujv07MfH4u8BV7z47eXAqhgTf7/9vITVFRgPeAZ8P1tklL++NNbWvRe9eNP3+XUrR17TjMJA1q/vT+vn2LBwO9DI/++6t+B1Eekbe/by++Mmz4PvSc7wcyXt7iI8h8fgsuq6Lzcyh3vx5/+lVgn9JxkCu1/Se7PD8GhZ7nApqfiP73enfwPaPY06FPmv162BGH9K5aA4R/LvUJPR/0r2Xf//wfRKUiz+tPj/1TcP5sw+zv087+07T+b8Ar5315YL406kB0gob9Cv74fVI75+Qf3+80f/vEbEP1/FHMo2sq5S3jPrDzyvbp5f//5h/p++4d//PxDW4Jc86zsva3Sfybzn/n1vs4fPPgc9eMf54L1T3mSF30OfWY69GtR/o/qtzdIt9LI/X6//gr9vl6mzwyajPhY9OGC39VMDXT9nR9/evkNoEUOrGmd+2NQ5f/2b5AUTdhV+A10AEDRQCDATZR5k/LHMKoh8HeqbQBGXlVHE5Q9xoH8nyI8aVz40C//07lj6RfniaXzCSTfH/D4/sDF9w9cfP+Oi+8fuPjLG3QEyxRVFES5lUIaparfcivw8mZSAYBh7VUdABd7bLwvAJa+TF8AekK//MWV3u9C38rxlzsHRA/s0hhhwq26Tb23yfZz6OVPSx2A0t7gOS1YLy0coJwfAfh9BT6pi7QDuDf5qU6iNIXcCKwI6GO8ywa+/DoJ++WXX2yrDr/lD6BdQA9eqedgwKc60JcvwEo/jYKw+ZZ7TlhAP/z62w/Q/4L+s1l34dMaKoD/Z6SAhuJBkSFQeW3mTUQ0hR3Ayj1Sv/729DUQkwMiBHGN/InYpskgcxPP/XD8YUN9QfHlBwUBqimqBqA3BIgIEnzoU1+w6PRowvewqBtAhKWXu17ujECqBcz59GReNFAN0rP2x1eorb37qr/YlXVXMQMQYDW/QBKjAjYpUvDPpOZ9EJhc5BFw/2daPO4DIdUPNUR/iHiD5ClXodKqrDKsrOcavvWIC2CRj+lAuAXlXv8tn0jUm1x1L5yHe8Ag4BnnGdIvU8zvJAwCW3+sfR9jTZx3vHNf9S2vn0VhVd6d64EqIxS0kTtRxd+eKVWHRQu6h8l/QNNJ0jMK7jMq9xxk/wvtxET3EH/vRR6sD31rURjBoP8/2pXJDGq91rg1deRYiJOP2uXh3qnXmsLwaM9ArwCBeY9S+t4/fKDPBwh/y9MI5Eo1/u0x8h6U55gHsLUV8KFGaXf5ICOAeye594SdErCq7k75ln+g/Svw0B3aQMxAdYPsn5LuY8Hp6YemISjh6fo78z+9M9U6SEqobO0UJIzvea5tOQnQqpqK7hkQkL3eVIB9GDnhH6yCgHSQJEA+BJSIQCQAI9xdJxfATFBvd+9/Do+mUAEt3NYB2oJm1nuDzqBuptypQQBAUzSNAV744S4KyjzgY6Dip4fr0Cofykz971NBa4pFkU0J8rsIPB9+z/S7LpP6QKoF0gn4sp+A2PWGR2Q/9XzGCiibTbV5n/THcD9thX5PS3/7lt91/MR+UPLpPSm/OwcCpZbVd4ydEKsGqJN5zwQCmXAn77cH/z4I/lOXr39q+n/8a/uCO6Oe/hi5r1DYNGX9dT5/sOAHCb6BKpiDHIlKr74T4pdHAX55VN6Xj8r78r3yvnxU3h+WeXjtK/TXVP2DiGeOf4WQN/gNnh7tIsebkvj5AZ5hvtCXL9j09Fuued9D/syLCXzTETDwJxN9DAF0FFReMA1+MFM9EVoPOPQOxSAo3/LPtHgWDUD6PJhotC5+V8x3SgZBfsTwkzHAo7wBa7tTexd40zYondSvvZeveZumry+5lXl/dfszUQTIYuCZaQcFKgq0Tk3k3a8+26jp4o87wXutAZBwi69Tyb1CU8v7Cn12r6/Qx37ivl3LW7Ch+nnqnKclwVDw3+fYz22m7b2A3VwzlpMVj03S1LA9G+k/KzFVGtDY8SbaLz5Ld1rxT0LAlyDwqj8LUe5frPSJH3VjTSQeNR9VXwM9XdASvUIgjqAaQYEB3GzBhD8vA9apvGsL2NKdzP3uv+9mFQ9bfru7oXnsNH99+cCRZwyeXSUYDgr2Sz3x5RzkLFgQXD+yCzz7v+03n+IAEIIGB8gjVx68tC3SRWyA2SvHt1xiYWO2RcAe6i1WvrXyHAzDPMwjXYeEfRvxUXS5QokV7izRJZD3SNn3B/MBkR7sg4kI6riLJYrj2AohUGvlWhhhWS5MkgRM+C7giu9TE4CiT7sfdk5O/Wx9J/88zf/1xV5iYOQGqwXq8WHmK91aooSthfasWnoX05gLdq6LcIYsdATulnGoyAlzpHNrqXnclhAp56DLx41osueGs+iu2PuOMBsNIr+pVHTIuTbqz+jeLYVcTG4mSaTKijS3QcT0moLAYnKQClxOTf3MM+V5lpjrq7ZFd+tDmabd0HLXbtCVBk40Mh1dTMyJ+eroDlnrlXpqCpy7wQKQjPJIxH0aVEnn7OPMyw7b4cKvL43JmHCaeulhd2o0dBuPuC5ELYpd2a3Gz8r1FUMFRBJOh1rLOtdOTZbCfN+use5mLr3uJs52JO61u81oR6vLdV0jYlqatN4et/yucpgrfMDh1Oak0tOObWJ25fliKPpeI3NEkHVNuHSNjhLRPpE1tT8dr1VUAzOFaCXt+Gg1NMWO3wfzoROOQZExO1a+jHDf8BrORlqonzN4TMSKWC8bAUZXPGiK3C0a6qtb39yK29YcnNKmY1Ok89DTrEwZTttSFHeDbByYUNi7iZZfUObGmVcjRhwcp5m9ccaFphCYNU32WUCm3rrsu/Ptasu4hCj7mBCRk6Tq3vVEq8P8dD1TjbWQNs1VjvebYZiNwo4/12t4tKih0m/iIivjKEvPR3Mzu5UlW5xFZA1Cse7nKrc98dYeH7iVFNN0aqtcZ6w9e6fdbvXmcMVDr/XOhu8vOXSLOIMv2RVp1Wt8POhmRiydUkPpitPX10u2EGE5iFvCjEzX3g59TdrLItIrxuJEn6x1PhFrTNrMDSlTamGOZfEBO+394tLIym3Ddc1xVNZ8nDHnPsRZPPeIrryKup5nbmy5Q9X3q7bOItUphWSXjwlWYs6lRcDPQJpIXCzsDd0Zimu7g5bWYoxLsIVxG5K8kQY7XlSBElbz4syvyVk868cmx8j9PFZRuXe2vKXNmz2sHOjqEqF9bfG3pCYqy+OcKgEpJWThrO8UMlsw61q6IPI4XCmRLkmHPJXZAdU3JC/k5izBcL7LlSogQZKUO8EaubTO1+327KwTiqJH7mKizeUQKoOCUmy4uXjCqWfQS7RdH7wYydztCXNiecDExtkWpNLlZrduzPlFXm5uRy8kuZU1Y/TOD3d6F6ZLrxmvok8dCPU6+uKqyq7uuF4ZmB+6niwpukTE/nIOs/05TozMOhohqWedvTwdsE7XQcC03kibK4dYJz3fXAhO2hY1m4kNIzA78kCueoCVRlVpQ5bDvONqmh5ZEnW5wr3icqdDoam1uNqgIrbowlGzW9jmZHU+HyOE0mcG27qXStxf7Qt8TZbWcHX9ZZIIZ/Fi1adcxOXT2iROXF8hh+VpZ54UfeGyIV7AudOfhdt6h8U4tjEQ5XKM5BL0nqM4p4/qsO6yUhi54xz3QilbZ+lxHhxyYTHbdjKbLMyFhbm3Je85fl0nuzMsneEMzdXQbJJM2ZBaVHLIim3kQ5kMqb4uOb7n4G13YmU3zNfjPk8Nx8LX64CipJXP4yerOcutfw2O5jJyK7prb8v6WIbOkkbNs3YqjgS5cYnrzlKvvHwdz80Mpno1iqvFoSRFde8vtiiAjlu4OCVlYKdIem3CuURho0tRMSXPDim7xoxwJHaMx/qhvsciEuMluKS8wVlcsk1HBjUFNo3n/hBfA+OGrNRs7euNSeC9HCZLw1qfqSNKcVSdcbNBC3arNXlOxYCstfKibAxaYFKDswc0aK45zu5X/W5rZYJFEfEhYHa9VEQwOhPtKvEZyrE5ehs4rJKkR5O58JSv25jTxAOuicy1CFeWwFeHflXBhORu4FmMcNpRaTs4m7k5PpLdDU6SpRgN68x3/XI4JelmK4+X2/IGizS6ldgYbXB4NWsCZtFieOwu12w9Z3fDQTKvF3c+Q4TVkSaE2wINZpxOUyAZyWQhCvtNEoRwOVgb+YSnlrZnrnxfu/qYUTZhqc015WwLY3eFdpbm3CGnnXi5LJISs5KZS2+EnHIzKy31QJUuPXvLBNYsjpge7Ki+rDR2GwbSaqYeYjpvcRzGdV5FS7g/kuLmhK+lCvOHwW7pJaaysO+Lwy1bpgpVVVjMOrTJh8pSdfCyR22LvzpxZOCAk9zQIC6bA6VRHYGeW7fMjwcU5aQUz5FkXcuDWI+XQHE6LNWX2XA8z/2rG0XmhVBS7MLt16NV6MzZkOXdys98J3YOHiPNnDMV1rMIEx0yuLSgYlv7wJylbKzjkUiEdoxbWm1Fh0oPFa26NnoSm9OhpBmHw/cluT1jQxji+JUxxlK3pbQXRlox9lHMVLBnMba2zlRAHzo3l+F9eD1uU0Q5STCMUxyPUrfLkWQBEBhBe0rTlHSq3X5F2fo2dcolc03Rs24xSib7azNKGqzeg6Ktc4BhaWbqO2sfiXp9WRuDcvazjWqXnLlN69tN3ASGsmr9zCwcM69iNN4nu5TA183iEmG5zsDI8WYJp3ozi6+Iom2luXthGQqmQXtwvu1rP1B2Gr/MzTbihXkJH5LV+hBxerrc8mhAnjDjvGLySD4mHVPty52U4EUK99ZIicKBYE6CBDY0a033EoZNdubmBjiquSnlkYTNk3DrVbXM5wua7hoVzU1Y2rD0aagCjr95brVd0c3ZRHjL00tl03XzfHlu5hnJXJL0wAdVwNr2sZMHzlHQBXyVpVJD6nruV5Yod4NZlx4rIkpo+40Bdg0wV8Rawu6MyjbYYtuvmZI6b+c+ThLOttWTml1xl0yo9/PMZqXdTge1hzCCbO7Xir6UjwtPPFbxDrQVNB5XB04+XXV4wSNFS2PueGZTpeR2Q8G2cbtncP2wQ9ZLXVEOs1DjqMBkZ1siifemXeCJggxbTVji4qwI+F0znGg2z8qluT1LVClrCZ6UXHsRKSXyTHUZICPcntDFPtrf6qIRNmS7VVFe6gdVHE6LpKx9irTcUzQjRL48KIkqsqzmzcRiuJgsNwinzE+wsxez+HJw58Xhmp/aglwaYdIg0iFnuc1Vb2JburgJOiiMK3V7UNuu3A/rleLrG9ZE3V0ZXrJ6mw9GWXrmUURkc6sMbrXrYLyi1NRFfFhQAAUrfmacW9FaKi2OtaIipdtaqEsa9E5IzftojZVg4iKuSllJ9QFOO1Ga86cFkTaNlvlXQqzpxUkTdw6xFo6HZKv1gs4DPOM3/PK4DLGCG8fE2QoWGtGR3vc5tXAEnaXNJYJsDrx1y6vV+oZGJg8a1FrKhUQhVprf+26CR27tJeeqGAul7pgUPpwz5sib8ijMKHzBbTnKbUrlHGxhijKNnXIVTLMoRxAIZnEQupzRz6vBvBgeVSOjIRRx5EeyXO8AwcL1RVI4sx6OI4HHSZM7EiPEVHM+bdEqlYIjMUcYI2roXiGPTZ2euzTTdtG8UlWDpm3PWEc8tzxx/M4SDyZT7+V+c6y6eE0X8yHe3K7crBczCsbmmdDVswbOq2ylpYfswpmYzxhHJxLamW9lZy+ois2VVZsgupIxs2vPR3xNb2dqJyDMrUySuWZYbcw0tzWcuqOWwLGhHrXRUhlj29ZhlKJrCr8oN/qAK9yJ5YshqKQtz8oJttKSA9zmC4dcUKdrdhoKSoJZ9boY/aBS4oW7MgUlWdNOoDmaLjQ9HvjbLQgff1rGaaSuzus4bHiWtRFprA7ddcvsdhUhGF7pKlcTS3SWZ8jV8TZco+Wsu3LcHqFF0NeTCG6vZ3RWEjN9yecqg6DkZrmwcmOhFyt/s9JDTFkgvmrn59I3ZhSCYgMaLrqF3SC7/tq5oDWb4w6WntFVaC7HeZzyJ+G0aG4lIkgwkaYtYJ1jPVsrC3VPBUEElwvRONp9l+9X+kJGwr3K7iwhdY7SFkCZJiyGeW8n2nK79ii8THWjYsd6Kx+B1cImbCNY8WaVcx5vqGgbyAWeH4aVdaSGzt3YzNDh9G4mb5vaYAE+o7qLgiavDGcuezMjIzBAx0578a0/qsRisSB4AwSPZ8DGfn7dzOROtGcr5EbOOnkWjTbjq5FvelRvaAca5v2IWOYC3SVexlpkh3G3q6Io4TALW1Mv9pojXzXuRtArRhFUxl7Q9WYI1dHcDItuJ0u7BjRYOAo2u7ye2Plx7xEBazB1Chsd4SxyWSGLQSrlyC4Op/Nem2uLbGZq+Aq5qP0MdJ3K4Thn1IrYFeKS81R8Ti3pG9m1bVDhFm4tzlrJ0npcM8eK2K/MxfoWXOqaJ5HYMY7HGucuqLqKkM1s1tanbmXPiTA+rjVFntGbmhq45IhgsxTpFzvPzVbkwKEbo2ocZS3UGNW0W4lQh8b3R1+eFXZKNFS06mA2UzIiJTaVvzNXQVZQ1NxZNnmvD6R4xc6BxiwUmiMifSl64ebW6+25WxbEkQowSfDTpd2KLXP2cM+4JmeXTKilZGL4gHMKfT4ywfEINnl0kGOmW95CEexvsJlDY8VZ6ALe5/a7WZUMs4oOYE8VS0WcwTTYM4uST3SuhDsbTuv3Zi73h4HBmtG+lFuf7WjyWm3IReFVVyRycr/DdYrZRmQp+gjRgcZYIbY3zmiI9cJZDaJ0dG6ZNCP2bkaWMqCb5CyRcpVyPuGORj83KI+Qq9w9H/2aC10m3yr2IjjOrYCOhxsSr7QFNq8PWbOgtHx3mtMeQ8RpHtdTbjkF3531ja2r7k6JYdSur83SLIn5gFZO0CO7PLzE0RINctjsaCqTHYrnb/tqVAvfCIlLsqdwT03MpXIrYFsg/U2wuWSjvazylUywCXpd9OMioqyN27VHpve9M+Evi4t8qZegLW9z150fJRq+1OoKlJ6lz28BT3gkV9tdENtz9yQviGavEG2GwvxMmKltvyOiIfMNguTnM79VD/rcA7bZ1dLwvSAwBY8UTgMle+trbWVzbc6QczYBFmYC7EqIS83s3j/kM4ndy7SoMIjs88fb3N1iYYG2VyLhJKOw/FLLlo2MdSleFh0LMOkKny++CDYxbARjvVxIfLmVuFwO4/AWwhIhpYaB4qWDdGc0I1B4ccrdGD5fNSS8ap0b4516YrxbQKo87ZwQ2RM9sid7upYovW8UvqwpZwFYbMy76806ZBrqKGO0ZzdjZTenRD3kRWXdUizNa+wWiRjcLJmmZv1OK/hWunWpR8/C2KguuLxDZjy5mdnZCmn3uOHW+MFxVg43tCQmGOZV4G0nmyMSve9OXeZdE/+M56pzK9NAVSm3Ent7RHh8f7F2xVE4M3k+qrSx0IT8cg7doZrrilpQM7yNIxexY5fIq6BWBoKkx8JebQNmC7aFL68v00n28zz6v/tyejoU/H92Nvk4Rvx4a3U/jAaCvt7X+vrf1vAfry+VEwH9HqezddoGz8PL/3A2++UvvvqYhI2Pt8HTq7eh+Tjjb6xg+q2nlyh3WzB4fK+LtL0fFr8CR9fTb13U789D8Ze7yVnZ3J99mgiuisr1qvemeHesOnyZfidiepvkudHj8XQZPI+uX1/cEQQycur3xRJ/96pysvr5KgUYi77Bb8jLb/8b+YeEzWUmAAA= -->
