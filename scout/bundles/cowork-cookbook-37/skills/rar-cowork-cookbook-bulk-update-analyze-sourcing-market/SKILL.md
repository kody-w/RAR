---
name: "rar-cowork-cookbook-bulk-update-analyze-sourcing-market"
description: "Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_sourcing_market", "rar_sha256": "2901fe3860393c0e9eb779962d9a3ffea7f079930145ebf3c2019887687b646d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 2901fe3860393c0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_sourcing_market_agent.py` first:

```bash
python3 bulk_update_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_sourcing_market_agent.py   # or on stdin
python3 bulk_update_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_sourcing_market',
    "version": '2.0.0',
    "display_name": 'Analyze sourcing market Bulk Field Update',
    "description": 'Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5555bf89a931efa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeSourcingMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSourcingMarket'
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
    print(BulkUpdateAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRrrmX2HO/WD7qqokdqiOjhhACCGJVQgkuTrKLMm+L5KQx/99Ekmnyr7uvtOemIihlgNk5rs875rJ+fXNHfq4at8+v+2BWyKSm+dJDFrELQNEqK5Vm8EfVebBf4hflX2beENftd3bh7cAdH6b1H1SlXA5V9d5AjrERbwhz5AwAXmADHXg9gBx/bbq4FDp5uMdIF01tH5SRkjhthnokRb4VRt0SNhWBZyEJGU99EiedP0H5Jr0MRK048d2KJG6BZcEXBEPhFULoDxFkfSfoCjg5hZ1Drq3zz//48NbAu/fPv/65uduB1+98VCgw0MS7inB/iWA8uAP1+duGcGJ9QixKOFzDVrIoYCvAhAir6cfO5CHH5D//M/s6rZR99PnLyXyur68TX9MKGIfA6Sv3K4HAeK7tesledKPnxAuv7pjB1Xth7acUOoglGX06bnyO6WqRv4+jf34ZPIpAv2PX94qKII7Af3l7SekaiE/CAe8/zRRqX/86VNeXUH740/f6XSDlwK/n4hBqT99fT2/yMKJ36cm4YPr3yHVp0k98OXtd8pN11PuSU+48u1TWiXlj0/CdVtdQOmWPvjxp39F1o+Bn032/Lfo/vwkHAM3gDq9BP/pwwPkfyCzl0LfaP5rtjU061/RBE5/Z/cBeQH1r2g/8P8vpPOkhAHwjvg/JffPFsz+jvz8L3X77xZ8QMIvb0uQJxfoHV4OPiO/ft3rovDzD8H3lz/84zdI+v9I5hESDwpfC7dMQtD1X7/+/MMjVCGNn38YauhrwC2+Dm3+z2j+M1wffP6A4GvWj39cC/kfyqysriXyzdORX6v6f7S/fUJsN0+C7++7z8jv42W6ZsikxDvTJwS/i5kOyvo7HH96+w2miBJqM/iPYRjl//EfiJJMSaoKe2TvVzD9QAP3SQEm4a046RD4d4ptmIFA2yUQ2Nc86P+ThSeJqxD55X/6j6T50X8lzfmUDb8+8+DXVwL8+p4Avz4T4C+fEAuSrtokSuAMxOR0/UvpRqDsJ7Yw63WgvcCE4o09+AhT0cfpBqZJ5Jd/g/rXB6FP9fjLI6knzxxlCvKUn7ohB58mHZ0YlC+NfJiCwQ34A+SRVz4UKExgbv0Ade+q/ALz24RHlyV5jgQJTN6wHowP2hCzzxOxX375xXO7+Ev5TKg48iwU3RxO+CYO8vEj1CzMkyjuv5TAjyvkh19/+wH5X8h/t+pBfOKhw9z+sgiUcLPXVARG2FDAadBY0LwwfTws8utvL3whmRJWNmi/JJwq1bQYemgGgnew92vuI0ZS7/UF1pGq7adCBasMIofIN3kh02loyuNx1fVIAGpQBqD0R0jVhep8Q7KseqSDbtiF4wdk6MCD6y9e6z5ELGCou/0viCLosGpUOfxvEvMxCS6uygTC/80Vnu8hkfaHDuHfSXxC1Mknkdpt3Tpu3ReP0H3aBVaL9+WQuIuU4PqlnCokmKB6BMgTHjgJIuO/TPpxsvmjwkLDdu+8H3PcqbZZjxrXfim7l/O7LXgUcijKiERDEkwl4W8vl+riaoDtwIQflHSi9LJC8LLKwwe5f9EfTPUbWT0aimcZR74M2AIlkP9/PcdDXEkyRYmzxCUiqpZ5esI4NUkT3M++CtZ+BK57hsz3fuA9m7wn1S9lnkCfaMe/PWc+wH/NeSaqoYVYmZz5oA8tD2Gc6D4cc3K0tn0A8aV8z94fICqPVAVtA6MYevnkXO8Mp9F3SWMYqtPz90r+QmeKaeh8SD14OXSMEIDAc/0MStVOwfUyAvRSMAXaNU78+A9aIZA6dAZIH4FCJDBcYIZ/QKdWUE1ojAf636YnU38EpQgGH0oLu1DwCXFgfEw+0kEDwCZnmgNR+OFBCikAxBiK+A3hLnbrpzBT4/oS0J1sURWTU/zOAq/B7x79kGUSH1J1oQtBLK9Tkg3A7WnZb3K+bAWFLaYYfCz6o7lfuiK/LzN/+1I+ZPyW12Fo51OF/h04CAyponvk0ikzdTC7FODlQC8ffqZrBHkW7G+yfP5Tt/7jX2voHxXy8EfLfUbivq+7z/P5s6q9F7VPMArm0EeSGnSPAvfxGXQfX9H28T3aPj6j7Q+kn0h9Rv6aeH8g8fLrzwj6afFpMQ3tEh9Mjvu6IBrCR/70kZhGv5Qm+G7mly9MiTUfYUX9VmXep8BSE7UgmiY/q043FasrrI+PNAsN8aX85gqvQIFZvIymEtlVvwvgR7mFhn3a7Vs1gENlD3kHU4sWgWn/kk/id+Dtcznk+Ye30i3Av7VvmXI+dFcIx7TfgaEDe54+AY+nb/3P9PDHvdojqGA2CKrPU2x9QKZe9QPyre38gLxvBB6bq3KAO6Gfp5Z3Ygmnwh/f5n7bCHrgDe69+rGeRH/ubqZO69UB/1mIKaSgxD6Y6nj1LUYnjn8iAm+iCLR/JqI9btz8lSi63p2qctK/h3cH5Qxgj/MBgcaDYQcjCSbIAS74MxvIpwXNAMtfMKn7Hb/valVPXX57wNA/t4i/vr0njJcNXu0gnA4j82M3FcA5dFTIED4/XQqO/d80ii8SMMvBLgXSwNgFGgKcoRY4i/sLwAKPplmWwgLWxcMQuHS4gM84RIIEXoj7EBOWYWiKoT2KoAJI7+mbX59lbSLpuj7j0ygRsLRL+QBfeLgPUAwNaBwsSBYPGQYQ4HdLM5giX7o+dZuA/NazTpi8VP71DTKFM9dEJ3PPS5iztks7tGfGHttS4HQ+zmUvOTSuB+jW2wB07QSezBVLcFskjGxjgkhmjVvsN+elk4sqh2OyXkjhWZmxynw80IIZ7PiTiq/aAt9ld/8+1/SjX93nqlRTuRK0THXytk2y3lNi3J+P234frrIcnW1rO8u6S4emzr69zajZPAkUxqKN0aga41b7zLHPb5LpnK8BxwpRZ58Pdnfb7WQ15vZah7WHxHJzXruhwHZvij04+b4euR6tWNuJpea8OtQi5rjpHmcWWoljtLZjMFC2DDUXZ/7luGLnNHFx3LhX97XrGLZXakKOD7zkbvwGUxPJGAwSN5T5zTbadGvZWTWYWa4lt6w79gl/9qmDd5D5bVO1XGUnxMUS0NMlcKutXfVsovn5ivdXDiYtMjcH27QRVkvQKMt6Z543K5SMg3OHjuqqvfgjrhYXWktmN6m2tmq+UxSP3+rM7roVb9imtje37VZtaS5zT+l5VjT29iwOtyPoK9wa9Eg7JyZdrdSG383VplDUcrfUwFJg0yK1eM1Jkm6N+ibb5k4c7lYB1kEBnDoKCssTu1HTqdPqVKhRgacHRz11pEvih9w56rqzUbM5hnKnYHvT5LFbEbMV6S0DfiBOVHJKzGrEurLzmjS0s+4+L9fSbeRY1evnVkAtKBkLzoGy60ll2LKjaZ8LDws3y614QoddspJtiWgNSRoydAG3GAQ6MkAW7G7VGPl9vGGn1Mclh7HXejdcqdt6nlArOY43bCwYON35biwsC2YhrJVDHaeUPmI0NZDOJsi9wb07vmHJ91A36bsu8iJlY2dpb7koZdkosJyeweqGoZoWM+sainjx0YW6q7ySaNfzcT0TM5dFayGWcIs9EcWdIsPQumCba7BdueS9xV16R1mVQZ/cjUBSzhndb/njdgG9fBdHazSbr8f1QTldV8lhnW4qzucys3Uc6lCchDtujblMLuetNUT1xVKFYXW1efc05CeDXWy9i8F5jRI1S2UhKPvNwOOmbF2t1ly5eH4jYv9+3zpsGccqLd4HMFa4QOnRjiLrmjYvmIktWdGK5/zuMOeGQe8CPd6JeaMnZw/t2NQLNyJdbaj0GEr4wuW75oyOF3aerG6XUTwFNDiyREOBI9PYVzC2iidERmR1J3WbVRdN3WCyb0fe1V1cuavcXguSjonxdKGdNBX11rplpnHOxCGYm1xNWuO2P2uRTgLZHAOmjNbqLJX5zZyhA5VbhTlBhKeDcaTsldVRthNo3QyE20Umr0jTZfxys1k52w1tc9WRGiD+SqXKntaPCWNTA7fOa0jL9GfMTuhW562Mad6KJKyLsWTcqhY9mlgEji6rZzkJN2uNb8gDMFZBDy6eT/XWPcEzIdcww6UysWFBDhbC6WrXuZaZR0NFbbm0i+DkHgyLWxoDy8soJp106VZ4PZtnJ4rfeOltfrTNZlERZD1LT1LTHA9AZQeruvHN6m7s5EaMNwwnAjrDWpoX3NpOrcvaX6KEPuK7eQeYNXqNDRLTNTLir13OK6nkNIlERHpai8pyydGEvPDI+KRvIqC6Uiw0t5wnr1Z/Gbk6IbWbEuoFexW2/h0VHX+2Z4BOu2ecPKBYMhCs0lnH8/3G304reSlEO/EgjdZ2N0ZGEKxK1YPOK/PLQxYl1tBzqoj13tDgZ5NBQ4NXXdsw95LDtUK6CwizRQdauEbaYsWlkSpSB2ZfnilaF8KZps3Rs3Gojp161RknLYmixtH5stpl4+gv7Lw83pm5hrMkOBCN4SrQfdcObs6tfVpvZ/vzroPZOo7Um3kCAA13M+t6ioI+uHk8k2hqN7t57HUWlCVzUfV1A/e78jrZlJlK6DtFHZ01z3PboDEPt4ICY2dUXNawR62p9hBZBkcP1t5q3Bt65Y4ndDXOeduSxuZQj27G0Wu6l/k1kXJ3e6MaHMMbvC6cuH6IdYNfOE7unJXYXxcz2lLqyGoTglDQE8lmdqZY9SqbnS3R0A54x1V7RaKsJeUXsTpX6eyy44/D8ZoUlctIRHorU7vZ+eT5yno22hzS4kieG2l26ekNJnCrSLcKZwg2a0vGcFH0MMdTzr6lnM6kkdL07NzLm+DU9Y508Tqwdy3Rk/yTfhDYZLXV9s0NuicmznERF8uoXoeraDP2oacKY3TCxlQedo1kRqKB2aehXu66iAZLMp1FN8eueB+GRnLf7g/Eeh+l0moVj0UhJjuFmU8RaA1CYpRc3ZDo6XTElsJoFmJfoOrN0cNbJ1jEntxXxbZ2C0b2k+5qx8wxOsUrmVkRRbco0p4V1kC57ZOjEERFHeQr0Ct3qR6Um3YUD0u5oJPZXXdMDHecBS/vnVO1KgV3YESTwWhitHebbJac+TZIz3R3P+R3gS9Yt5CPRxOrj/Etp5XSJiuxw5z6tGQLGnd35rYdzEE1c44i6cJhVtkeL0RgFPOx5ZZoLYKSlfaZuKrJrU1F9uJ6GLqilIwlehFS4+xxBUXE2LW98RUa9abJV/5WjrSl3Dj+hm+00eJbTHfQkjJHebY/CcWCmrNXw8MsttL8dD9ebbWIBIG4SIsZf8dy1S3q9aorljiOt6x+pKMtR+wN6ZAtg8inj/0pktOcLrVZtuhnonagZ8R92AXBsk931zNmEc6dtml8yy5ZOfO4y4rC1KsjnPjYi3YbPmFotV+tt1TBz5MltCCHnYjTTBjRsDyzVpxKB17K/fTQY/aBIsaBVitwohbx0t7mgXoL3HsE1sMuqq3GFGaETh9pv8n2bhfsCqz2rfNMMBg+EtQZelHX3K7eiovb2ur8yEQpk71GzdGOTX55ybIG2zi+WLOmTGb1srNqEab6s0pF5LgYDqiqa+gZM8rsPjr5hRak03HtEjmssO0iQo0CrZI+2WwPaC7eeVQ+tKs7tdxw+2ORRIQDEnPOFmVI+UJ92zRrLSfOu8A61Ndx7ka0M94l67zqrKi0WmbJb3DL35oXq7StTPJTKc2IS9cLFVGdUMlbCGg+eKPkrbGhnrmqL7Jt0Tg3fpTX55KwQZE6Q+0DrYjji3hQi63MDWQXHJe2ttK3SVsDecTt9BIcWNu8JgN5INcnlb3lY2cGy6s0S0hZLip0tRNrU+PFqo+ioJbToF/MVxzlmKm5F49Lfyesd3y3dK/xYnkr29Dp7VulmrOFq+/lrMDOUKWZaJbuvZ1xNHPR9uA+Jupe8ZK7PPa9kJNGMUqWHetXEfBEzq3Fq1lXWh3J4mFValLgGPvasKzQOaWhzNRNg+O6KJ4psXAMetXtWW1B48beU4qg58RTKhWjYIf7WXZY1onhO4eDfe4aOaBFl54Z6KIymN0get7W3i1cuDHoKAtFr1eA5WYUmyDneYHKDoXR+JYvLFyavF4dhZHJGcXr3dbjvEXYFkfseKDuM9QVx9pSBIW51OcNdep3l/JWb9pq20C3Qa2jvG23VyvMCL2O9nRU3Ub7vNhRYQV6c88D8kAdYOuZLVJPt8zRV5IBPddLW+8UfrwGhVCNirIZd2rCa35/UEYjPSvd0cwo+kjNEqMZrCLi7hzft0e5FzpKS1sCNwI5F85cSgqNQQt3bhCNHWRa3fS1cHIbdQddS3LusKvaZ8fDYWV41lEfoILq9na9BcqymrvJcNk2WkD2Zu1h+0C13PESsBUIbc4JPaLR0GShLRzKoZZrjy1DsDZD0qN7NDxSdYObOsj05UjvhjYg7TnO3458QZPnTtmJd7W+r8G2MLLtGb8GknLApDxhNOUIbiqbHCNPM3cuYHEvv0Tr/lI0eeHqyuyaNInc3fMVczJlRafDq56LqLTUru5l717UGbOa3zmxs6RN6imtgJdGuLu2VNHnu84NmzQHOmeU/trTbgOKbWeG03X62izOs3MgkZx9k2fa3KZOGJu2/OxyG9drDMfn9MpiopORF9IlLMvZtsxYS4O75s0Rm5sWmWt+rPMXwwOVc6CY+tppcaO3hFVHGM7NeJVKmMjrdN8rbENcrpduZh8HY36Vt9V8czmTOL1R5gylp3i6Z/ulXoKRkLDVeeVmwToifLZfVa3kazGb3waSxFUFGuw2XGXP8eq5oa1mm9OZYQ9cywd4cGKMOat4bXtZUFmh4HJH80tSH2b9MKpYjktBveSPUTOGFWGwZ3wko5MfE8m8NI6CifmJ7K5nqJf23tF1j7N+Tt1ucz63+vBs0pxib0TW0e+adqPde1fjd9E6oWHoco5iShjv+c4Ju5RncByuHuq39q5cUmaNp45SzgC4NmtMPKfXHXNXKPh4uWVe7IJs5xOZ1W3WdUjZRmdeAiVEj3iW81dD9uCeqA9xfpv6ZYve1iLtcqGkkB3hN2su5ENjE5P4shotZtVdXKKk01bRS87fov2GNk/3ZWO1ZHVsF5Sm6WEww9dUpMWbZuO1gU5e5OjC6VuLIxzY9mIesSOj+6KLm7UwmzGFvcKDuLqLo82S9W0dHC4C3BZcsqC84RvTS9Ryg6VpVZ8Th725spcrCy+/49hhYcjtndJ9gRVWl0usDa1H7k44bA3zXWUQ5t1fcsdwntLrNPIkaQnpnVLtNOiWhl3CRbjtbt797uAJH/ksGWH52tNT39JiFA2ZoXeD1rt4hC2dTlSAZoqJAtaQGGlJmOTysAT8EUUjm/T7MZD4FTebpWyupWgDIQ1Tltpv9aEAsKaot9Hqk4svx3Szn4Vuil+sWTFnSAZb0PWQ8bPQpuc6bMnpjplj9ZVEaVZ2JZy5X3M7nG/vK+a62KpbFtMw1h/Y1msFzydCj6XnM+eozMf4UswjtSZ3R8YwlMwConuKpAu3UKiG3eFqON6jkx0O8iLgUDCTjtc5yGeqbqg8rwj55ri6zxl/y0RVrrXefaEdjwXY5AOpMEQX9311iamMb1gnA0da3y6X1X4RGrJuHiJ5PnqeWMBqj9Xbeuhph9xth57FuxrYGlUSnc3pwiHVqDW6PdboOeYJoC+punW7ncfyaLGsuFUbC9ouNVbkhU/M1RH4Aau40XlBNrymXIS4yzGP3QoFQMvd1VOY61py8DzsQ8ffzVV0d5CXOyITVTbt98woYtjRCHbzc+xdpCtv5/MbetYICfZRQ47uh3RvbkfiHm7nK4E/zEl3k/YwolKaKyWC9PkxWoUnp/Wwa3KWiuTGCcGlBaJ+W8WsWYvLpGRCf0h7Etvjeodey2C3NpPDrCdYnq28k4SGQsZx3N///vbhbTqefh0y/5UvyNOh3/+zs8fnMeH7J6fHATNwg88PXp//klT/+PAGB6BMz1PWLh+i14Hkfzlj/fhvfKuYCIzPT7PT97Fb/34o37vR9PtFb0kZDF3fjlCefHgc9H6AIHbTrzp0X18H2m8P1Yq6f4x9U+X7oWlffa3dCc+knD75gCB5Dk+P0evY+cNbMEIjJX73FafIr6CtJ01f3z4mC0wfP95++9/R+AvNwyUAAA== -->
