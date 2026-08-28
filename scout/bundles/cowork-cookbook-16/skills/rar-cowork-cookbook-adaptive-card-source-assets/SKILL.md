---
name: "rar-cowork-cookbook-adaptive-card-source-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_source_assets", "rar_sha256": "d69021989a09bdf77d51d4613d576a0db15d1e39862469aa49391feab20541e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_source_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_source_assets_agent.py` and in the RCI capsule.

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

Source assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_source_assets_agent.py` and embedded as the fenced Python below (sha256 d69021989a09bdf7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_source_assets_agent.py` first:

```bash
python3 adaptive_card_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_source_assets_agent.py   # or on stdin
python3 adaptive_card_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_source_assets',
    "version": '2.0.0',
    "display_name": 'Source assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ff8e8a850edced1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardSourceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSourceAssets'
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
    print(AdaptiveCardSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6Z7PbSJLtX+He/SD18uqC8IQmJuLBECBI0MHRtDrUMAXvCA/29n/fAskrtbZn+s1EvIhHGRJEVVbmycyTWQX+9mI1dZCXL59fNGBlE8lKkjAA5cTK3Amfd3kZw7c8tuG/iZNndRnaTZ2X1cvriwsqpwyLOswzOH1f5m7jgGpiTUrQVJadgAnrWvB2Cya8VbqTlbbbTqrMKqogrye5N6nypnTAxKoqUFeTqrbqppp4eTkBqQ1cN8z8SZhNXKsK7BwKqF7hDStM4DscowMrrd6gGqC30iIB1cvnn395fQnh55fPv704CRQL1XpXYdRAu6/H3peDExMr8+GIYoAAZPC6ACVcPIVfucCbPK8+ViDxXif/9V9xZ5V+9dPnL9nk+fryMv5Rm2xSB2BS51ZVA3fiWIVlh0lYD28TNumsoYJ41E2ZjchUEL/Mf3vM/C4pLyZ/H+99fCzy5oP645eXHKpgjeh+eflptPjLS9mMn99GKcXHn96SvAPlx5++y6kaOwJOPQqDWr99fV4/xcKB34eG3n3Vv0OpDz/a4MvLH4wbXw+9RzvhzJe3KA+zjw/BRZm3ILMyB3z86Z+JdQLgxElY1f+S3J8fggNgudCmp+I/vd5B/mUyfRr0TeY/X7aAbv13LIHD35d7nTyB+mey7/j/L9FJmMGgf0f8H4r7RxOmf5/8/E9t+6sJrxPvy4sAEhjT5Zhknye/fdX2C/7nD+73Lz/88jsU/X8V80iIUcLX1MpCD1T1168/f3jk5Ydffv7QFDDWYKJ9bcrkH8n8R7je1/kBweeojz/OhesbWZzlXTb5FumT3/LiP8rf3yamlYTu9++rz5M/5sv4mk5GI94XfUDwh5ypoK5/wPGnl98hN2TQmsa534ZZ/p//OdmETplXuVdPNCdv6gl0cB2mYFReD8JqAv+OuV0CiGsVjpT2GAfjf/TwqDHksV//j3Nnyk/OkykR68k6Xx1IO18feH598NyvbxMdiszL0A8zK5mo7H7/JbN8kNXjckUJKlC2kEjsoQafIAV9Gj+MRPjrX0j9ehfwVgy/3pk7fHCSyssjH1VNAt5Gm44ByJ4WOJDsQQ+cBspOcgcq4oWQRF+hrVWeQMquR/urOEySiRuW0Ni8HO6yIUafR2G//vqrDan5S/YgUHzyqAYVAgd8U2fy6RO0yEtCP6i/ZMAJ8smH337/MPnvyV/Nugsf19hD654egBreCwjMqCaFw6BzoDshXdw98NvvT1yhmAyWL+iv0AvBYzKMyBi47yBrS/YTRlITG0BwIbBpkZf1vdbUbxPZm3zTFy463hp5O8ireuKCAmQuyJwBSrWgOd+QzGA9q2DYVd7wOmkqcF/1V7u07iqmMLWt+tfJht/DKpEn8L9RzfsgODnPQgj/txB4fA+FlB+qCfcu4m2yHWNwUlilVQSl9VzDsx5+gdXhfToUbk0y0H3JxlIIRqjuCfGABw6CyDhPl34afQ7Legqz363e176PscZapt9rWvklq57BbpWjKxxI/nBRvwndsQT87RlSsKw3iXvHD2o6Snp6wX165R6D2g9FX3sU/R8bhS8NNkOJyf+fjmLUkZUkdSGx+kKYLLa6en5gN7Y/I8aPjgkW+Lvke558L/rvlPHOnF+yJISBUA5/e4y8I/4c82CjpoQAqax6lw/dDbEb5d6jcYyushzj2PqSvVP0KwTkzkfQITB1YWiPEfW+4Hj3XdMAGjpefy/Xd+9B5KC/YcRNisZOYDR4ALi25cRQq3LMqKcDYGiCEdUuCJ3gB6smUDqMACh/ApUIIdaQxu/QbXNoJoTZK/P0+/BwbIKKhz/dCewvwdvkCJNiDIwKZiLsZMYxEIUPd1GTFECMoYrfEK4Cq3goM7akTwWt0Rd5CmP1jx543vwexnddRvWhVMihNcSyGxnVBf3Ds9/0fPoKKpuOiXef9KO7n7ZO/lhL/vYlu+v4jcRhPif3cP0OzgTmUVrdCXSkowpSSgqeAQSecfv2KJrPDHnX5fOf+vCP/16rfi+Dxo+e+zwJ6rqoPiPIo3S9V643SAYIjJGwANW3KvZprDefHjp+euTWDyIfCH2e/Htq/SDiGc+fJ+jb7G023lJCB4wB+3xBFPhP3PkTMd79kqngu3ufMTCyaDLAsvmtpLwPgXXFL4E/Dn6UmGqsTB0shndOhQ74kn0LgWeCQMrO/LEeVvkfEvdeW0dmebjonfrhrayGa7tj/+WDcVeSjOpX4OVz1iTJ60tmpeCvdyMjs8P4hDiM2xeYK7CTqUNwv/rW1YwXP2677lkE09/NP4/J9DoZO9DXybdm8nXy3t7f90pZA/c3P4+N7LgkHArfvo39tqezwQvcStVDMer82LOM/dOzr/2zEmMOQY0hV1ejLu9JOa74JyHwg++D8s9CdvcPVvJkBkjeY+0N6/d8rqCeLuxkIGe3Y57B1IGM2MAJf14GrlOCawOLnDua+x2/72blD1t+v8NQPzZ+v728M8TTB88mDw6HqfipGsscAiMULgivH7EE7/077d9zKqQz2IOMW02KmWEoM2esGWO7Hk27JOoSFIq7JE1ZM9dGSRcFODOnMIJiLItgcAb1gGVjM5JAwajKU/5YxsNRHcyynLlDo4TL0BblAHxm4w5AMdSlcTAjGdybzwEBkfk2NYZc+LTxYdMI4LdOdMTiaepvLzZFwJFLopLZx4tHGNOicMXug9P0RnnnPGLklabmDW6kBxS4a7msmmBDL+OkXl233Yw9divB4SudPcab/rpd7ZYDt0817+q2gJO0mNaokx46R3mFCShd1gh5K1bcQu4aU5ylfibVqnW6qM6xPJY7PeGA2XLLKlk5xRTJlhkT0sbVROVIj0pOQ8lskXLXduq1y+2RutxOTbi9FoG1cTG9XONxol0v2OYc6sfj9BKtsrUL7COs/lkji0mfTftLoXS2Qy1ldHcqZ9Qer1EnyzBRr2mAZ9OT4zdbQk7WV2ZxikRg9rU5pEVGimf7amY839NKtKKDursq1Gx1WjnadhOkp3Y7MBVbnxahRazM4LBCTTcsNDcjO3tu3tI8UsOLehzQ3lgklBFzxIDtV3C/YlVFtlxEWoiat2htnqQtXlzKiFrjJ6fbRJQHQlNwQvKWOUZeLLpjNddnLnGqwEXfButQ0NNBN2e+r5dT8Zb4ZU825HJVpM7en6qDSssXcSV0lV1uCXuN863NNVat2W4rVsrBCM5oOERWKPJL2q02pVlb5KWE6PBY7XtJJBNBzZ0GOwrKJeXP2pK3rq1gXR1vjWDtau0q6M5mzvyt2t9QvuBgEDg6nokq7XWgoNbCzdKiE9HsRFbTLoJd7XWBGm4LO6iaRsQQicvc6eo6t9dr76Kd8SMx7bRCtfUzLUleil6CBhU10gsWtQbkWW92CYgPBm06tmFQx+aM3JarAPDktDOjQugyckGcFjKnYMamJnWKFxRkdkZMP8Wu15pXpnrXS/0OV2Y3w82pTSyfDs6UXlu5tdEw99hd0jq/kguK7MQpbq5d7UjgItYVU0mfsxnw+Jl+sLMCqVihoDdtS7aMpDFLkpK3V7+hVxLSHpU+2sGtlgFS8tQrPWPnhoXmTupGebX1g8BbWAGpROoM90/aIpZIquXOhXeF6RxHsaESTsI7zM2XW+lK3/iZljnmmlBbn5O3eR6eyETtZfqCn8MNv9SGg5GLfG8ZLR+kajEjFZZKmQzf1d2q7VHkDPNyrq9yQuW05SDlB0wPN7hJZwe3nEbLW55Rrib2maeaNNbPJAzT0kohcQPpkAqkZhUGseAlR23qzcwT1lZtcI0IqVmAzmkv0emyLajBMfvyvL4dFya7WqUFFQRTXDUMhLH7dhnqrYWm66soq43pFgeDSfTGqI08ceb0tI3PShMtteViEyxUHKEgucRDup676zw5KsyRPFMbatoX5pLxnNn6dl0p/I7lVVjlijQKzS4NI5lcerGcKauMElmlTHgzF/eH6TRfD3aP3pR+deGJlT2NT9cr1Z2DKemWos1uTVNg+Gm6d8JQWVQlipF+mXIgzUTW0Wv/WAWCcEqrEiNLkbc3l3UokUHqr2tycUFvUBGt1o8iEOGkDRuL5HHGYguyoPp2r8B9ic4UWCks0rbPN6HUTNv5zei1NSusp9WQE8f9QbrgMeLuC2VL6V4FOlcSpjdyivMMS8k7bXcT+prd6JdElNJ1U6u3m7XMfG960B0Gn65v+ZU1KkHyIhOGQRfM6z7H9+yB3OjF2muHHXERdM7I1tHxMm9s9HIM8wibIkV82psruhYrv+/kgK/y3SYRW6O3EZXFO2SLrYjLsfLURF7LIcMQTZoKOqgxVVZu3Y09cIVa96vWStjaBJ0MQwBJD4aoe76B4qnFG3KO1uG6kWe0Y9aCxmE2kFIfra8c2g4zcc6Q2Toh9NLetTjJgNbGiLxf+OGiUI7Lki7d1UqNTYTihhpyu8Pz3rALYT4h01wWLwyJs0y45C4b5srYGZEtkSkiJ/IB7EATq31KyNKlwncCaa54jdWQRZjwGArmcad08ZE8Vml8u5YuUBb7PEiWPGKsxNmihJmzz7IZBpDVnGk6snSjo3gwcNmvqLPfGFmkK3tP2LEKBCEhFDrXb4YVG3x+ovxqPztaZrqsd6fsfDL2PXneImBvb7PtdHYktooUk3I8n8nTZShwDYpqdJeoCoZj1ixEiVoXbQGLOokt2EC+IIxy2mxKJbCLzt9KOb0tMT4CEo+toiM1vRznc0sxcYdA6cMwDwNnaS3KQvLJ5Jhsi/0pghXBq2J3oYlK53nnXjJq2fFm7caYDdVVDXEJUxiaKhZWvGSojN0pNjVTes3RYQwvIIMWFpWGpryt2h3OgBDnRF6XF7f2iovbs9UknK/4173YRWcCUWYJuQkXFkHmeiEPS0KZKWqwPouUoJTKSdlt0SwdnP1aow7VvLiwFuaKS/NqqhVdZZtMnMXdivGp67ne9jiwE1VScdZYs2QXx91thZa2njc9wZlqfQlPKd/lzIZM82S+YrbOje5zLcF6p8fw+cWJNGmWKKhVhPxCiq7oUZ1uWsYSNH4mny4WKhgG6HbDkRuOVDicE0TL+y21CWRvkYgGzc5kWIs6mSaNbru+VdVhc9b0y0E52KI/OxRHRczjKF2UPZXHR+yQC4d+7Wwdbopa03ivHJKCM3wCsfdIFS/nBH5uYEWt5slhDXP6UA/75CyuZ0ptosbxMIvQ3aJtcXuwDJvqUKzgokQGNLvfVdJ+UJc2SblubB+BDOoTOpSuAOjsUuUq7PhnbYLZ1CVJpVSVB+5iMy2Z9Qv+0Bmy1N3AJdaPh8S/rAKiMg8ploNUzKdRiLtxcdOY6JSve3AShupmmddBHMSg3Buy0qmhsd4kIGVzCXeHTX41aAyNUgbFu2QTXIc1TOSikKbcEmM7kp9KOBH5x91sEYtL/Qqqg0jpzDpWG2WlxEA9Z1RMbQ+rncHubbaCMTUs8gDVrGx+WKJrrbbVcqsd3WCLsnMT1ac3oZQU3jFtOsYQzp7vrC3nzNC4UNY7IoqJ3WnHyLoqh2ej1I6DvWfVq3pBtxfhYMTZMq7VjZb2LSAs97hcmAsWP13tsx6hg2AbtxV2SW4FLWkiW7XnGKCb3rwa25mlJU3jXJhz1G7F07FO95RxY0+dj1iJQOQrXDyRBO47uL+NdvNUjDs3wtSkj7Y676muN8AIy4cbxdeJQeL6jVzeFtlunZRYpMY5AFbjyYJ3MU6bm3QOhavh9DxHHIhUYEuRCpgDMuN325hSYBKwMFhRurpRnXrl9gp9FcRpotil2t76Jaxiu0w8Q58u9dNBoObK0RRXZ/YqGjNKJ5amZlq2fzli6/mw5lfsVVeM2YmT6kN4MWClMSjyYGFYkW2jiE5nMpGsN8FunuGLcHvSjxc/qbZB0CZHMlytyExoE/G2jCkdoEGmyss9Bv1dS7JEredWuqgwkysdlMTaQ3Gg+GMcx/zamG6t5ozlQ3NwjPNJiXtzMIlIcoyN6cxPhDTzlWPLXMtjMi35LDomYqKdqxMtVEMRi1PbKrZZ3hQt4cuJueh2XAB3ScU044IlOHlwnzebYVbO1luPnvkbZFNyzu7GrWr7skyca9qooPMH9rzj9jnf52yQERudz5Wt6p/WkrcaCm+Nr7AWvZ4jk8/cheIu0U0xX22XJeuqawxnLTIO2KY/eEF1mS+FxJQWV0ONo5bY8lhSXQ2myjcHJO8uVUMZmT3XXZrD9yEQkZi2tk1NnDl56cGcRGspmdW5ocOu/AIYoTxkO9q1Wd29FW09bXZLdFXtl9dcYBC0KTVEPDYLvW1arncd/NLgV4RWyBOX0cSqrJTlzS6jPbFiWB6U4Gbot6zO45MnFwtG9ZtyzhPGUTT3l5C8EiJRSjDbr9HaPUurYrG8msUBj6nVrFEQQe/36cHNYooISxogQkUyJu1u8Y6r+WlNU1G3niONdmx0L0ZUezeXOH9K7KfbwA2pU0pd234u8OfsguO2oRyPAkHyWUvap12bUf1Snnush9CFinRi4Vw7g649r3eRHXOC21WSYDyjLsK9ez1ewyvjsju2Z+M5X/engTfseefPCr8fsttisMQVF3RztQHo+SDz23LB+9PeY9eq2utAFvz1+kKL5DrEdQumTWWCkJVa95LZNbXnup7c2Ad1v4CRmjC7eU723MlUNm0oJmYlerNl2Qr7KSNVwm1eEzek1drOExwTsLhk9QAP9/3NtukyVhqjOQT6dGvy3oWM9tk83ns1q1qSq3COsEXFgaD2R3UXeQ6iTvV123tzbF9bm5hzZ8IN4y4Dv0Yk6Yh37vLAIBcGbgQWJxvNcZs9ujoSWczmolu9m4iAjlqzbDeBs19Jy9O+GkqCYQp17xg9y5/IqztM+ZXXGCdrxvcN6cceWvmzVaxq/VLAeoQcXIEXwq6vQp0ZJFruaFinr8UZ3x2EvMMRaRka1aI7LVgbMHkvrayzToXVqieGSz8nhJtWmR6/28ln3fV6BgH6qsLcQNrm3pVFFrNEsOlaLTF/owh+pHMnPxq2qcCp550r+jtjfsrxYZbjDCaZG61uu2IHu5TbZsXgGCmhC7oq61TFQ297m4Vx39xWZ6WsV9ipN2DvQg++XqDAUelgtyFPFBW1+bQBbS3hYMUPyx0pWV0n4jHB4GonZgK7J4dztD83bLHD5oh2U3Exz5Mz6OcseVa4Oo5pQXBg07ntT9PTcQtQ9+ROFS4/U1t0A5sFkgpdar5fCeky53kHKSj2hMu4eN0Ia44SlswBksTskFM7NZgXyRI9tdZlv1YHsQ49R1anB6xBl7rOzW20RQwkESsKpw2Xj6ZIn9HYcFgiNonUcAvoiwwqydNztDgd91hbXiJ6ERRmjWvl5UYg1ck9KfP+MCMYei4yU1+TnaGtpLO+pSmn0qINyHdz2biwOwDD3sIGBEfPqXC0j3uJRd2KcXHuuPIqd77VD3uu4FXU8yRdR86WHJ9n3pzpKVaBu5g22U1xJ69w3+Zp2lKUm5xo/a3bUMttObCH7qxohgw3jUqmZEKuYZd5ix/jWevZdGtqc8ed4nEl+nueCDKXodPSGJrOn2+X3NxA90CM5j5x4+Y8T6n8TokOW7LlAlU0p7lLSSh7y28L6ULuOMF2G5pZ8zGHZsrBrAChhyWxbjGklEWkoZJVxSVTy1/spvM2qIN4wI9zXAYkCTZgu5fpNpOVVbztbmvmdiic9Myk7rolD34iMDHmDPYFKfsDd2sanHXOHObYXIUcjEQtVs2Bjc6UXk1DzrmsvU3uxIvbiQzP+6XfOr1OaSm52yln1NV1SoBulsFstz6w7Mvry3ie/DwV/lee646Hdf/Pzgwfx3vvz4TuB8LAcj/f1/r8L2nzy+tL6YRQl8dpaJU0/vMA8X+dhX76i4cI48Th8YB0fGDV1++n5bXljz/neQkzt6nqcoBaJM39IPb1xW6q8QcG1dfngfPL3ZS0GE+vf1B9vHbuZ8Bf6/yrC3f+eQVexl8BjI9igBta9ful/zwdfn1xB+iT0Km+4hT5FZTFaOjz2cR4sjo+nHj5/X8AOVJ6SzUlAAA= -->
