---
name: "rar-cowork-cookbook-configure-analyze-product-quality-data"
description: "Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_product_quality_data", "rar_sha256": "ce9f39200f499a440b52464ad7e2cba750dbdb4351502f21714205078df64d5a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Configuration Bulk Setup — Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 ce9f39200f499a44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_product_quality_data_agent.py` first:

```bash
python3 configure_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_product_quality_data_agent.py   # or on stdin
python3 configure_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Configuration Bulk Setup — Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_product_quality_data',
    "version": '2.0.1',
    "display_name": 'Analyze product quality data Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze product quality data from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2470117fb16a38e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAnalyzeProductQualityData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeProductQualityData'
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
    print(ConfigureAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZebWLbmX+HGfbDzyg7EDK5VazVIDEIgkISERDqXk1mIeRZk53/vg6QIO29l1a3s1Q8tO2wB++x5f3ufQ/z2YrfNJa9evrzsfTuDRDtJootfQXbmQYu8z6sY/JfHDviB3Dxrqshpm7yqXz69eH7tVlHRRHkGlrNFkUR+DdmQ0yZ32iAK28qeHkPuxc5CH2pywNdOhtGHiir3WreBytZOomaAPLuxoaDKU0ABRVnRNhB/c/0ECqLE/wT1UXOBOkDqPRhO6lV5kji2G0N1WxR51bwCnfybnRaJX798+fmXTy8R+P7y5bcXN7FrcOtl8VTKZx9a6A8ltg8dlkAFwCIBqgLaYgB+ycB14VdBXqXglucH0PPqY+0nwSfov/4r7u0qrH/68jWDnp+vL9OfXZtBzWUy2a4b34Ncu7CdaBLzCrFJbw81VPlNW2WTx2rg1ix8faz8zikvoL9Pzz4+hLyGfvPx60sOVLg74evLT1BeAXlVO31/nbgUH396TfLerz7+9J1P3TpXH/gaMANav357Xj/ZAsLvpFFwl/p3wPURXsf/+vKDcdPnofdkJ1j58nrNo+zjgzEIaudndub6H3/6Z2zdi+/GSVQ3/xbfnx+ML77tAZueiv/06e7kX6DZ06B3nv9cbAHC+lcsAeRv4j5BT0f9M953//831kmUgWJ48/ifsvuzBbO/Qz//U9v+1YJPUPD1ZeknUQeyw0n8L9Bv3/Y6v/j5g/f95odffges/0c2+7yt3DuHb6mdRYFfN9++/fyhvt/+8MvPH9oC5Jpvp9/aKvkznn/m17ucP3jwSfXxj2uB/EMWZ3mfQe+ZDv2WF/9R/f4KHScE+H6//gL9WC/TZwZNRrwJfbjgh5qpga4/+PGnl98BSmTAGgAD02NQ5f/5n5AauVVe50ED7d0cIBEIcBOl/qS8cYlqCPydarvygV/rCDj2SQfyf4rwpHEeQL/+L/cOoJ/dJ4DCb6Dof3vC4LcnDH57wuC3CQZ/fYUMwD2vojACZNCO1fWvmR36WTNJLiq/9qsOYIozNP5ngEafpy8ANKFf/z0B3+68Xovh1zuORg+k2i1WE0rVbeK/TpaaFz972uUCTPZvvtsCMUnu2g9Urj8BD9R50gGUm7xSx1GSQF5UARfk1fDA6Db7MjH79ddfHbu+fM0esIpBj9ZRw4DgXR3o82dgXJBE4aX5mvnuJYc+/Pb7B+h/Q/9q1Z35JEMHIP+MC9BQ3msbCNRZmwIyEDIQZAAi97j89vvTxYBNBnodiGIUTL1rWgzyNPa9N3/vJfYzSpCQ4wM/Ax+nU6MBWA1FzSu0CqB3fYHQ6dGE5pe8biDPL/zM8zN3AFxtYM67J7O8gWqQjHUwfILa2r9L/dWp7LuKKSh4u/kVUhc66B15MvXM6tlLwOI8i4D737PhcR8wqT7UEPfG4hXaTJkJFXZlF5fKfsoI7EdcQM94Wz41ZCjz+6/Z1Cr9yVX3Mnm4BxABz7jPkH6eYg76egowwavfZN9p7KnDGfdOV33N6mcJ2NUUChe0BCA0bEHrBo3hb8+Uqi95m3h3/wFNJ07PKHjPqNxzkP1X08LiDyMGN00dewApBfS1RecIDv1/MJHcbRDFHS+yBr+E+I2xOz98O81SUwwe49ckDyTYo46+jwpvQPOGt1+zJAKJUg1/e1DeI/KkeWAYKH0PAMbuzh+kA/DtxPeerVP2VdXdI1+zN2D/BNxzRzFgAihtkPqTT94ETk/fNL2A+p2uvzf5e3QrbzIdZCRUtE4CsiXwfe/uhOZSTRX3jAZIXX+qvv4SuZc/WAUB7iBDAH8IKBGBGgLgf3fdJgdmgmK7R+GdPJpGp0e0gLZgWPVfIRMUzZQ4NahUMP9MNMALH+6soNQHPgYqvnu4vtjFQ5lpvn0qaE+xyFOQyz9G4Pnwe5rfdZnUB1ztKUe+Zv0Evp5/e0T2Xc9nrICy6VSY90V/DPfTVujHDvS3r9ldx3e8B/WeTM37B+dAoM7S+p5yE1zVAHJS/5lAIBPuffr10Wofvfxdly//MNR//Gtz/715Hv4YuS/QpWmK+gsMPxreW797BWABgxyJCr/+3vs+Pwvu87PgPj8L7vPDmT9wfzjrC/TXNPwDi2dqf4GQ1/nrfHqkRK4/5e7zAxyy+MydP+PT06/Zzv8e6Wc6TICbDKDZvnefNxLQgsLKDyfiRzeqpybWg755h18Qi6/ZezY8a+WBO6B11vkPNXxvwyC2j9C9dwnwKGuAbG8a4EJ/2uAkk/q1//Ila5Pk00tmp/6/u7GZ2gFIWuCRaU8EvA+Goiby71fvA9J08ceN3b20ACZ4+Zepwj5B0zD7CXqfSz9BbzuF+wYsa8FW6edpJp5EAlLw3zvt+67R8V/A/qwZikn7x/ZnGsWeI/I/KjEVFtDY9acWn79X6iTxH5iAL2HoV//IRLt/sZMnXNSNPTXsqHkr8hro6bUTuIP4geID9QRgEvjwT8QAOZVftqAzepO53/333az8Ycvvdzc0jz3kby9vsPGMwXNeBOSgPj/XU2+EQa4CgeD6kVXg2f/lJPnkAuAOzDCAjeszAcag83mAM4yN43OHQHEStz3KR13Hpoi553gOjhEIMUcDFKEQHJ0Tc4r2AhL3iInfI0O/TWNANGnmzwMfYxDU9TASJQicQSjUZjwbp2zbm9M0NacCD3SE70tjgJVPcx/mTb58H2ontzyt/u3FIXFAKeH1in18FjBztB0TdgZOmlXJ7GYZ8IqKk4NbobOtmK5pOHU3KpsYFjq/ufwRXZhE3Fmqe8rcYod6Z5uF82rWd6Shjwu8iJK1m5AyK8JXTc081MssP7vFZVQqO3OfKtSBWR+Vk5zSgyzdGstW3GN72u0zuRnKo7dRrDlaBFG6tilBnJn2vhsrCaYPFnI82qIpCIu4saR2jh5Lcz2YLh+sLyxhI+iZW5CKXGbKBU/IZKFI5kVuZbOlTJw1s1Z080GgDkC/XYrQK/RoHksBZ0SLngUnBKd1rKFoG8V9/YTSXXPuhHkV12YxDzOrVcyCdPZJeT469lADqcmh7g18wEW8tIcq8QZ1UWBm3eAz+ryNd3G9YEEiIov8lKD+aRSo8tCc1GMF+EpceNr49bURxCQri0pu2I3hl020m50duaJW5xnagj5tHUfFR204tzUn2RbDfJDN1EzHNrNX462bx3J2LpPD2HmYjS1X6LZM1tah32MihTQJSY34ItPqht6dt9tlR7cReqkTV2SG5nTqXE81CXuN0tdBSczmXAknJthHTl5Uh8vxbJIy17iBOmi3g8c1epsfbMYf6GJ9nhWFEJM7uCYEjXGO2nqoBcIXCCo/hKUraHHcqk4pIWoSdN3iQM3O8m2lbcWy81LU8Lp2IaA+tuGowJEj0TTWzGowKTq32GpJXbdRts6xpEOruWYigtmOB1cIzlJmIHK6QPId3t9oauvbq2VFla0hndYBbsgofTjpMXFtllsJU924WHI2gSwU58BwLg1TTFMqjaMdT+dZipq0uu0ovL7VVseuTvuYsvvNxjhs8vefY6rrvuUbmH6zAwXRtlssyzuJtnWcP9qzORFHmx6D89U4kkYQGBS8wNvLnvJ7B2yPDbxyI2xbOohTDF5j72VpjZSNuY44FY1xtFKc3hrG6OAsl2WwWPIXlW68ULky/PpYxWrK7Oxl4XZ7TRRvx2XuZmbbm7S45y3FX/Mg/vx8Tx8N9+qH+9jFTHpN5Eop28fGPNys7HJrJL4ivCGnWBJuCsdiSttC/b0sh/Fib4F/471ax3jNZmuZJ4JtgerozCea5HBp5gk1in5C5KRFF7nGwXNd1hpTbWcbebPPZqZGYXR6vPlkpXoyz9LwWW7Oh6U1p7L8ckOTS2ylncxektl83NCYsNf0zBTz6yxcVfOSB3qY16zJZul+nkvrzW4Y4FOXIO7Oaa4LbUzHYUBgeJ0IyOaI87mhbKv5wBRmhzDZbtFgVNho62pFsphxjjPlIDZB2ofhHDn4Bw0zsR1accb+bGWc321pkK+0S1jrclQDVeBD2ElwzDJ1U+8ZRD7HCB4eGcw7L652W96qPeX5DC9YuqaF220uWVzVb89Yi9QbQtjE5Nm48B1qHM97BMGzNL1GxLC3EaqS/XJcDq22Z69dT/fUdhcgvk6iTrOLm5lT8ARC7XxUQLtoW4XoKfRpNzfHMgzDYFAkxrCRGZ/U8/UAr2+D4edDPwv0dWYF/vUCG8OiDAo9EbiZV5C6Y1qzOiRpj1MCty+1bT4f+VsqKcFhULhyKdsnReola8YWxAyA6YwWlq3Yj/GowZ0+3Lz2zB93zs3J9sYcsRwt6HWNrcMbyxZljLVao5cc3Sgii867JA75dn+mZcfE/PnJOHXrapTkAWNZeVmYgoiq9SVM7RTlVnuazE8633L7HseUTmDRouA6qs+Na1anp5Ugx5RSKBvlvE73NzRIfdv0irO3srDTCcXO3RghXqfkYRLK9k3MAi+4ECe8lWIN0exxK0orkhASgkQYndeFMqu7NDjDB4M7+mmFjTcS1kNsgI1bNTt0AdnZ7OWA7o6YT1hYJyk1T1+M+Z7lN7ZFyX1UrBOsJBAhMVYqtllim2p1FGYm7imrzdHt2LV9c8vUNXeH02gu5WG9WfU4cjgdC3+Vz/X1YU7JKk0EbbypHUv1DlLGzLIxvi2DBJ4P62gtrU176WvtoTP3EicXXmCFxoI6N9pO2R9r7dZtuHGbVU7S3HCtLw+3QEhOu6prN9sqhzdLjUtyo6Gqc7uoshAbU7atb8l43AlXchEkKaYKzLwoNqcG2RC2mgnxouab7QZUhqwGQkTuZii3xHhMYvMyGdisUjnhVM/HaEtetKVYXOrjJo7RMttY46IfKhFji23cL8D1PLkQZ2RNbjSJicjen/WehqrnWLjiLqpZbWEpCO0EI5VJrH8Zb5uzbzMzlxNzYc05uidi3obXtzPRSW5z52jSxZyfGUqTRtnyVGxxbbGvi+ToIrMZfdooosNt82B/ZcRyfV4uhgbnfH5PL9W8PuUFt0nt+VLH9/X2YDYey4Mt0BlpDStCyvU8PUXG6syIMcPRl9QhvHS+1mLZ3uVrjp+rx7AD09g1Oc6vfJQYB1s5KSdX9MruqqwcEoyQ+cVrQgLPG/WU04tTGl83oPfnHaEfo/m1pyR8LuZSkekeudA658qRPJ8VS1440lsc1kg1Wa2MsJQRPOrDUki61NoeULwUu/nBHWURXWNnD08QoW92lpyHSh1rjliaqsyGi8iowoVHpddCIiR+txLEiwSSMLOP5CxtjR256XQVD4d+Hc9okuKlKyUc1yu5d1hF2Z5gpmeulqoZoUfEYXmW/LjbMowq364VhQbMssK9VduckJkTLFsmc/gjPzCge+6oubZSGv3a84fl6kg1t2jNrdmLxDrLhYSvUu7oVuNZaleYaJwv7cq7EiusGmCtPLvOcCvwRkVryo+4gwFzRxlulNvCnK8sQzgiJ6IvRYZUo4tg6D7R7pEScctcTpc1KYmhtrBwjjtwV9cbkG4js2DoVHJaS9xcCHumj8eTVOy1ZZYvGB0gF6uqzqLgV6PrEzFoETe5O2zUWROl++1JrvRerFt/31dwM+CRu1OGY9LwVJtri7SdH8N9lQn7o3JkD7shwVTbwquFftgXa0GizRnBDWWu2o4Se44WiZg8W2cNJvGHBvOHdlAP3XxVqbakGEl6xC0yUmNOMamSUtfJkdkiY37N0wVJ71A3rbZkh4fq7VAtqqOXyLEeX7OYpGuNVs2D0OQEs7wVpaQOSNEGujkaQbkcLjfvSmkNQVOe07E7PcrcqL7OBhEdFXXFL9WU8vJt3+2D6KArXHRkMWIZrvgFgxkgeJxFHpP1zp2h9dYts5vWLU6svj8v4WLtx3uu2Y+q4ja63Z0OCbUYSTprlvjmJBYlHPNEZyM74cLuo2N2avWD1I4h2BixnIuGRHgxL6eiVXLSYPt9HmjrFbGKLi6B+NckuYIR/LTnXPeWnTHBlK6XtW0U+tb31/3tutMIciR3SpkVbGlZZyQlz2GqellHGKd9stgvacna7W3dt/d6b5zTcOi4gaeW5314KKUoOUpWzeJhkW9y5IrDvajCqzASz114WGxHf9BX12iTGRlc9nKy3+d8YHkDrQh4iOpxVW5yryw8mk2Fq8CLnXPJfE9ih6W6Y9sxj8VrnqXdpT9eooViiQskphVC3MyZyiWx9SYyb/1pySH5oliF9anXy3U9msp2SSy1iFBbR56jtJ7zIaKePHZxYDnS3R3IdUijzGixyVkZdmpudcyVtDhlsY5FrDiXrHX2uU1wxtfa6TC/ktewHSpr7JaHVNozXpE1I0Noet3sa5DX9UIsL4lwcDtZgGX52CvOzNu1YFbKw6ukwzllkgKxoZrgSp89QVrB/pHsOiYqCG3EapSH0aQPjA4meTotYNeQ3BYkHEirutpimHsmDgu+pTZEVyBlCvRZHuq1eB32vGCsyNw94dMeVkFSPeBPlhTDcyJxV5h7VbMTgW8p9QS3t+2MN+cL6+aK6Iahzbro1hQtccWgemQGb+Ve2tP8pUAQRNOW89Y7RQMvYTts63K5SixhmlxuZxvUa4gO01dcu80KWPQLrAtQLDDniMCSAUwSI9yzDNifrN1NABMBrBuRloTMWYMrMPdtm0sQcGLaxcFpK8sIH+7OjKHurk5QheZAzS4iHkW9hWdBI12Wvuq1a+s2sDDrNoaa0ofMteJxVsWeOHNOXenRvWqsZgfU80FHxjXJ75OqMrdaCBcU5yZUn/GpXEv0IkzHq0RKbjZKop6UsbI6MShyinV6JhYkdd0UoB3TJwbjaCxzAmEI1XBDZvZ+PG7XF/0G/JHqDsMa+AY1w5tElsog4zPBQjfL61EiZu1wCBhvBl+qm7KO9kEvb9iNWbB02uGMdqGqkVlOAzBlN0y+s3Z8ehaQmyXZ6DKxfAng0Jw6pAv9JnZ+gw8dRs0EbdYv+Z0WRAQ2orrQrhTXMdWLcl1evcuK4XK0FiIVq3TG82omrPmd2NoZhW5uOyos6Y1phPqSlYzUV92j7LJHsQPbBzyTur4K5Y7OxjS7Bt4WNwhCXDTnm8/P8FUlU7PqlM1Jte7w8YpKZKgVcnVxKnokulWYR7rqsId64S5RLFwo3LiqLyW1oDt3WZZIu0XYPbmeRTU+pnzXH1kPNpn0hsk7J1LChhzBJoSI0uvNVrpkg4FRUgWaeX2FzV3eoy4KS3mes+9iqmUCX525a1F1sdW4YsNOcThUS5agf7HBEu1FkQh2M5+quHGUUsk1UXquroR+jkr2YBMRtXTmvp/AcWYWKE3dGOW0sskY7TQO8SgjIRvsyo9ezQsCtt+MSm4FY3vrWDaqA5wjdSXGKZn0s5zFhaFc5yeGB/gnJnB/wWjWJhmfScXoxtQoTEc9NTpIRi+ZdjFjrvX63LIB3GUXpJRi3kFMvPFkXTNsmDzrIwJQ2sO2xAoOhCAjkMum9XSnkTpUAgOkfIHH2ULRb6eumEUWW+A5MSyqnjNw5Nj2iTVTHPlg0+TIhd5JV69dWKLeTIG50haQobwoHRUJvSvwLmJrcI1v2i29RqkECW3EFMnU33Mr/UgpfbKXtPVCyo25v11pt7Df3c4mLquw2zesZzgO0vTm0XHgbrenXcYJ2tuRnbN7vMvhxBY1/aD6WIYzi4iqIouONsyNWC3mPXeI+hXYFHM9fF0v1zu62uTimbVwapDZQ7Bm2mafM4MfMaV2Kk/cuNTUrkA3M92VA2qGc7psBXzIwfCxguN+AycTQGlzZozO2/kAE2TL1pKsLlMTAWNEQhPXm4UWQXJeHnRU6NJ29FEqC4nRUHqXY2fDKqeP2unGRYUYm9s89bqwFsBOMvGsOO7NK51YonElrsdMtRpD8jI9OO08oyI38+yiMF61Dln25dPLdHj9PIL+i6+ep/PA/2fHko8TxLfXUvfjZ9/2vtxlffmriv3y6aVyI6DW4xi2TtrweVz53w5hP/97rzQmHsPjze70Ju3WvJ3dN3Y4/Z7SS5R5bd1Uw7c6T9r7YfCnF6etp9+XqL89D71f7gamxXSC/i72cZoehdm3Jv9W+U10vxVl09sh34vs5u0yfJ5NA/oBhCty628YSXzzq2Ky9vmOBBiJvs5fkZff/w9vPNcwFSYAAA== -->
