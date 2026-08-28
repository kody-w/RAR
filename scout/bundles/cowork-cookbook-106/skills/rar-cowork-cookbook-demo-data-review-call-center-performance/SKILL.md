---
name: "rar-cowork-cookbook-demo-data-review-call-center-performance"
description: "Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_call_center_performance", "rar_sha256": "099c1a69fdc6803cbbc81ee95eabf2f28ae23cb5d2f4640e2156d284a59b8be3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_call_center_performance_agent.py` and in the RCI capsule.

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

Review call center performance Demo Data Generator — Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 099c1a69fdc6803c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_call_center_performance_agent.py` first:

```bash
python3 demo_data_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_call_center_performance_agent.py   # or on stdin
python3 demo_data_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Demo Data Generator — Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_call_center_performance',
    "version": '2.0.1',
    "display_name": 'Review call center performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for review call center performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '106101c3cb43cd0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReviewCallCenterPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewCallCenterPerformance'
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
    print(DemoDataReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2LbtX/HG/VBVl8yQRhrzjBrjgSKiIIh0WnlGFD1I34P16r+/jRqRWbfOOffUG+/DM5sQ2Xs1c60119oYv71YbRPm1cuXl5NnZTPOSpIo9KqZlbmzVd7nVQx+5LEN/s2cPGuqyG6bvKpfPr24Xu1UUdFEeQa2c17mVVbj1fetTuXd34MfSVQ3kTNzvTQHl05eufXMzyvwvou8fuYAjTPHyxqgtPAqcCe1MsebRdnMmtVAlp0Ps8bLrKy5b2sqK8qiLLirKaIkb2Y12G5VUV6/Aqu8wUqLxKtfvvzy908vEXj/8uW3FyexavDRyxpYsbYaS7krXwHdq7tq+ZtmICOxsgAsLkYATQaun3aBj1zPf7fyx9pL/E+z//qvuLeqoP7py9ds9nx9fZn+KG02a0Jv1uRW3XgAE6uw7CiJmvF1Rie9NU7wNG2V1ZOnANkseH3s/CYpL2Y/T/d+fCh5Dbzmx68veTFBDXD/+vLTDGDy9aVqp/evk5Tix59ek7z3qh9/+ianbu2r5zSTMGD169vz+ikWLPy2NPLvWn8GUh8Rtr2vL985N70edk9+gp0vr9c8yn58CC6qvJuC5Xg//vTPxDqh58RTWvxbcn95CA49ywU+PQ3/6dMd5L/PoKdDHzL/udoChPWveAKWv6v7NHsC9c9k3/H/b6KTKAMV8I74PxT3jzZAP89++ae+/asNn2b+V5DgSdSB7LAT78vst7eTzK5++cH99uEPf/8diP4fxZzytnLuEt5AUUS+Vzdvb7/8UN8//uHvv/zQFiDXPCt9a6vkH8n8R7je9fwBweeqH/+4F+jXsjjL+2z2kemz3/LiP6rfX2c6IBT32+f1l9n39TK9oNnkxLvSBwTf1UwNbP0Ox59efgc0kQFvWud+G1T5f/7nTIycKq9zv5mdnLxtZiDATZR6k/FqGNUz8HeqbUBiXlVHANjnOpD/U4Qni3N/9uv/cu4c+tl5cuh8osE3FzDQ24P/3ib+e3vw39t3/Pfr60wF8vMqCqLMSmYKLctfMysACyfdReXVXtUBVrHHxvsMdn2e3kys+eu/q+LtLu21GH+9c2n0YCtlxU9MVbeJ9zp5a4Re9vTNAQ3CGzynBYqSHEid+RFg2k8AhTpPOsB0EzJ1HAFGdyPA9aBRjHfZAL0vk7Bff/3Vturwa/agVmz26CD1HCz4MGf2+TNwz0+iIGy+Zp4T5rMffvv9h9n/nv2rXXfhkw4ZMP0zNsDC3Uk6zECttSlYBsIGAg2I5B6b335/ggzEgN41A5GM/Mh7bAa5GnvuO+KnLf0ZxYmZ7QHwAMppkVfN1ISi5nXG+7MPe4HS6dbE6GFeN6DrFV7mepkzAqkWcOcDyWxqXCAha3/8NGtr7671V3vqbsDEFBS91fw6E1cy6B95Av6bzLwvApvzLALwf+TD43MgpPqhnjHvIl5nhyk7Z4VVWUVYWU8dvvWIC+gb79uBcGuWef3XbOqX3gTVvVQe8ARTZ586+D2kn6eYg1EgBTnk1u+6g2f3d2fqvdtVX7P6WQZW5d37PjBlnAVt5E6597dnStVh3ibuHT9g6STpGQX3GZV7Dir/elSYmvps6uqz5xAytcQWhZHF7P+LqWRygeY4heVolV3P2IOqnB/QThPVFILHEAYmg4ewqYy+TQvvXPNOuV+zJAJ5Uo1/e6y8B+S55kFjbQXwU2jlLh8YBpyY5N6TdUq+qprS3PqavXP7J+DVnchAvEBlg8yfEu5d4XT33dIQlO90/a3PP+GbPAcJOStaOwHA+p7n2pYTA6uqqeCe8QCZ603F14eRE/7BqxmQDhIEyJ8BIyJQQoD/79AdcuAmgNav8vTb8mgKI7DCbR1gLRhZvdeZAWpmypsaFCoYgaY1AIUf7qJmqQcwBiZ+IFyHVvEwZppynwZaUyzyFKTJ9xF43vyW5XdbJvOBVGvi2q9ZP2WH6w2PyH7Y+YwVMDad6vK+6Y/hfvo6+74J/e1rdrfxg/CnhJz693fggPyr0kdiT2xVA8ZJvWcCgUy4t+rXR7d9tPMPW778abT/8a9N//f+qf0xcl9mYdMU9Zf5/NHz3lveK+CKOciRqPDqe/v7POH1+VFonye/Pj8K7fN3hfYH+Q+4vsz+mo1/EPFM7i8z5BV+hadbQgS0AkyeLwDJ6jNz/ryY7k6M8y3Wz4SYGDcZQb/9aD/vS0APCiovmBY/2lE9dbEeNM47/4JofM0+8uFZLYDes2DqnXX+XRXf+zCI7iN4H20C3MoaoNudprjAm445yWR+7b18ydok+fSSWan3bx9vpoYA8hZAMh2NQA0B4JvIu199jEnTxR9PePfqArTg5l+mIvs0m0baT7OP6fTT7P28cD+HZS04MP0yTcaTSrAU/PhY+3F8tL0XcExrxmIy/3EImgay56D8ZyOm2gIWO97U5POPYp00/kkIeBMEXvVnIdL9jZU8GaNurKllR817ndfAThcMQJ9mIICg/kBJAexasOHPaoCeyitb0Bvdyd1v+H1zK3/48vsdhuZxkvzt5Z05njF4To1gOSjRz/XUHecgWYFCcP1IK3Dv/3qefMoBnAfmGCAIXi4dxCKWvusQFIw5tu1QiOctcc+yfdRHKctDwae4i/oLYgF7KIITLkotLHxpU7aHAXmPJH2bRoFoss2DfQ9bIqjjYgSK44slQqLW0rUWpGW5MEWRMOm7oC182xoDwnw6/HBwQvNjtJ2Aefr924tNLMDK7aLm6cdrNV/qFmmQthLay4rwzhdzztuRubfsbnNM4o64FtIhXqlMnKARxevoisXj0kql1bht9qLFdPnRd3hovODkZR6Ep8xShdA+M+micVC7xYTYB16QOkOz+dIvjbK2Yyeo2UW23yPG/ljogobicRZdB4VDRW/FV/sLUZg7YxRLc0FeXD8lIW2j7mRF58t5PvipbelqrOwJuNTT9R6hG6GHnM3SXRFxvaP1FPMircrEPYIbiS5kUjIfDrkpqSutTurmxA2tpKS+nFUo5G1tdNnud+32ii87HcvNiNQjfohpiqlL0igaVUfyxLIW3XI1ZNV1R4ZVX6oEtTPgbX0bM8UZM4FEWcQh4h7RbqtQLUtC3ycL37esQROrjF+zRJRrt7Hmhbg54OE1PG7Lwl6bTGThumWbO8WwTntibFWhdq/qhahK3QXZtbEssiCE1VYcUNfL1cy93JgibhM4CVJ9Se/YRECPKD7unOGE7Qekbhb4dbGOnbgdGUU9bkzSxdfry2kh33prLcDpSIyX0gnnmCrlnGchRqltRzIptJxYjnuDM9OwtQOIE43d+rxvYmRbGdvGCC8Sixy82ihPJEehK36EECOJ8bOYuVp5REI60xbAcP4S8brZZSvXntvDLZeOXJG5LWoanTxuDAnzGVK2h2hrqHuSH73bXLjQt60bXph6p9kbyrjcSqg2du2B6tjVDW8JlTnVu/poz5ugFEM/C/MlYdeDfpXnLKzUiTNnRQO9nq+jJhXA2dOArYW9tgzrYU76RSk0F113r7i9s/u+PnWrQbqlJzZy99v6ut5Vp9Ky2uJkwSWXCqWRdhe1jDDPSPNahkm664/+aK77vUrx6nU7NvXJrBf+nNlKvlqRhO3nOHNmq+ysUOu0Uh0wwwrLFYJobnIRR+NUIkahX4/4OfYv9QGcRK+cqDqxkN/Oe39zji087ZIdRss2EheedNRwTF5INbUjVVrb4CGBKGuMLqE1zxD5GJbw9bQf9uli67IhXbQ1q88Zkz4lAp8X5U1eR2dpx1HzREk38Hxv3m6kMrDrOuFLl71FsbJV3VHNE0INE/LoEs5OalROVhTqdtOb+hof0hyFMga2I624oNF8nFMb8+oRrUnHjQrIY9chiT5cKmHh0GNShuIZrSOrIqzrNVKu2+aoLYyhZm6hQBWpv2hXcQk1ChF1OF9sdOXireAuYA7FEs118cDdXKriREoukGahjA4KtaPQwVYpiGehQqwVdGpUu02CTjUa9DrX44juy0qN+lGqDpgh7SiU1TpEs6DgVPqjdavc3Nfj/MztvVxcHymIEVb18iLsEckUF6zfFttFottHWBiCkeo1q1SERpNHRo5VPdVgjsCgbWbKkEUdhwt+Vjr+WFTNRjyNJ5SsxR0cXS58Fe3OhHMTrkbqFLwxWESq6VB9iwpeHYXm4HDCaXeF3G5EikN7ZTF5uS/EpSI1OYbhNxMX88ijb3IlltJu3TONj2yuGRWmy3NldKc5sQ3VEcKa+V4MfGx/3oKEMeZafOntC9KkOQ1R9GJ0GcF3gtv+lCMmi7bbtXejbaW8bZkNUXkU02xGPyIgKMYDduGQu1Y7e92Wsp1QK6MMOLnPdjWEOvDRX+1chsvXzmJ3uszDJCkkdiuwF2Md7voTXUiKNJah7aWV4CVYyOlhmtKwfYrsqwLmSRrT0H5XF7chdMT9aRUrIzgZ7Y98C18WuhresEyIVvG6SHEkpVGnuKLeQA1kepPW8nAVFwQ0r3DIMYXD4MRsfhMMHr3ZHXTWdztlNJ30gNfL1dFbRf1iaUHWVkYqGtUxubaboHc3N6o2rjHs7y5wRkGGu/MqAQ483mROGEHVBbY5O2xNF2ixP3GHeJlcQp0pkkXr6rssECpcrvCUTYzFyg54o8Y2pyVjXblbGRW3kjoUW76mndYKCz3oNhq8HpL9+nxU0dBPjpa2jAf9mKwgA+B2RTVzfky1q4FflriIXwV7Xo6pfFCFdpl1hWSsOq0LN2tdP7vD9oqxmJnCwq1AW0UwdqYYlqombjfbZh7wNLUaZGuPI4krkrZz3Hepg55Xi/7cw/2wnc8j0+JB+824fudhZyoR00LLvFY6032hFfqWMzl0iQ0IFt0a0dnjh5YJuU1INIJDtYAUS76jr0XXBXKoF3awRMRCY/2jSG7YJWJZTRFUzGBLVgZYzB47bcfuxcI0uYMb9QkAbm1cdUw59vPD4sikPr9haZ3X+mEdCzDDHJMFdxgUmfEulXyISU8LLRoro1KEbSInEM0Wueo8sih14tm4p0z0TA5Nh0TWVTgpp7XSLE762EfeAfWNo5hDfM0X58QLyDFZUzfNylkInJjOQ35KiGGpG1gzGLc8tKziksQ7VJjriJXwO0lvD0zBELsbgBcnuga+svGuWyUHYxE1hMteZCUoBk1XI8as1up+Q/pcSUehm0Rna7VTk61Ld6lgnWIrSqPVtj/u5I4v037HEJujiuS83JIpfIUstuFFcSsQjTo/nzu3QG6cpET4Yh+ITuC05CWTj8dbqaJVnottpY2a7M87ua6M+YI74qeDHANaXqvLExwGqZTBOAanTbKICN03iwSWSPRSK861QOTCtjuTPBZwuwgUdp+amIPS/GrcrEIatcQU9+zLXlKyeo1zFiM2x67eKUvJ1gc1RkT0cAkKDekPO3ihDYvI6vFGaGij5q3kVOUtU9JaGGLWYq8Rsd5lrrRItFbX/MZtdfUad4Gm0DR3nEcgjzSuI/YXZ11EUqm3gaXLhrQ+qZpxPGN4ShTHTbZit4fAOMUezsc0UeDxvNyawglXzwhpnW5O0PEZ3Ox9iBX75WE3KE2ROtKKR33NtQheT1RJW/NbSjl7ZHzgJHZwrFTQLntOpbi5w3GqxrtCOIKJY7e+ZEzDwfUh2u9peWzW8XUtUKv8Qh7PllufsqWkKdc+PKGuebmey25v7fR0eYw3w6bgmq6pdn4cZn2brA4+zLbHuSX5K93zmjPR6s4VlpYmdNtrq43QmlvahrqFguuaux44Y/RcuzQsTuLc+T7J0avvHMVKNPsz04ntXtpZgsINe1ENFOJwVCQ2OBaYs+hamRhia3+O8CWg4BH0W9ThXZq4wHILclThU+Qm9gcCXqauffB7aqmrKIRxlnDSWHd/qODC1bQisAbdNkM5OCA7pqa5wZKTnLF5N9X2t4IwGGsHE6BHRYKyyJL9xgDnjMB2tymYys7Xs3aZJ14undKrosL2MhIlA9vo8IIIyTi7sOVlJxvpLb/m1GHR4TvtxMg8JLmdiMu1RJj7ftRi/5QxY6GwfUIXWsfxpUSeuVHhe/JSdZpPn29UtJaL1Av4FX0d51hdhTvMzmwL5pOVYbH+0hlL0J/DdqmhuQGhZYIRG75x8qAmDzypHqk0ECjvJo57suk104QJo2YOYDTZ3dIgDxY1ImWJk0atfsDXYPwRGa73ueg6OoEHl0raGIGx5+zdePE5s2jk7rIzyoVUigAyBi7ECtusAzLtOJdRV4BARp7zuVt1FNUMOStQgOreKcfU/TgsYHY4wt3tSpdjieNwrMmYJBEQPgyK7+AamZhbnCeIVdsJl5Bmr6fQHE9uszZVPQOyLZvdXtR1bJCrtWIXZiLXG8/vPSnHt0vErFAcsbBkjBufz1pKWlvkGrq4WEK2TNRuhQxN275eO6gpOnlp0laLHbbwGVdFSyePjtSuI5sUIQbGWSypwHQvkYHXEkSOXfIoEFkNvnCWpJm3kA+6eQOtIPYIsyLOVPKOoFAuwJYKpPTw+XrtegyRs97Y9wKRVmusPc3TaCkJawU7sjbUt2OymjNGUMuZm9ie62wuPFYolA/ORBGJHuoDAo5eOJTO534u+PGKEssRntfUfNCorrYxU/ZbqI1Z+WLWOxVQ5KqKtoc2zqmtrAzWChHIyF3pN3W4zI/qqDKBsPFHok8dfq1ei1vPHiSZl/dnjKnZYdzi9S0gsCRNE5RMfHG+oQ8ocTtguSUzPUNuwXB+6ct1ayLkmG05cdh7F+60SxJq62j4pklHwGjwhnQOJsJA+TJoJWq0mPMQRPOWlSOK3BNdLFBs68xP3KpiNG2uuAw0dk1H9xf6sOmksDWuFmEluW8rneQWPk6aBDavttuTpDEuAgiNHVnWRBdSgvX+9uimOHSDR9a0G09C6foc6PWeIkWk8b1x0SxzssCvx5bqNttO4siUzDJHKJZBugDn+cPYZIEjUOd0YdKXFSbtWHKlQBi0YQXWxoTtXF/y1NHhaGlcAiDsILm0ZkLkWebtaOnKuYbjKevAjLuchSkihM87iDONenFaDki2vQXyZj8kFF+ew8FFoAxZOp1QFCh7boOlxqDCIRR8n8MOOCuyzNk+02mvJO3NZ/qclSKUA6cqchlyZYniKx2SU7PXAccOMiXXOdJcMd88l5sWDATZ5eBFVXrpDUFZUxVaOLFHj7kaHpz2Ol93YmiTC7WyGidrblUxZGRwXACj1qO9iLBW3B4h8WCqATRIdu/sEudALCPIs6/brKo90qDFfAPKeGs6nSO0IQLbdekSdmF3Clo5QY8I7fx8jQiMzmC3Y+h07dAbYUyr0T96UNYOfECPtd8rhHzLEZun/G3uDrsEQ1SZsFD2sjwAqR1Lw3vSg1I2gKgGxdBKRiFz6VJr2Y5aT4c7ptuGoLC7rZF78L7W/dIEp8eRNLEuNAa9PK9deEn53WnZHxD00Lqmvdx2o2lSNB/O91DgNgvBxC7HOjh7mncO0iutoQfdhf20w4pB3Fcoa0mJBRGnarHu9nMuy40M6hvSHM7UHItanjhYFrpYrhF8yNAz5hgpZYwQDJt9coqXHhhoNGgNhYMlOluYY+BktRZvNDKA0+nWTU9laTuH1riVtrokLbtTixASkPOqP/C3FlreslKRzz20vQaQYKUdQ1LB4sZQ9ErvQ3mzzFcOFtzyqOpK1VPTgHOlU6Sut2Nur51UPl0Ls7mM1KqXnR3Ivf2JxL2R7rA5sjKZi7y6Mv5xWcr1MU0I8jqopCgoBMqLXQfOGbLElKszRugsWcLsqWlVQPhsrpbYTVAt33dugXeGR2qbBQc4Xhw2QFMuujuY0wRaTSghqOZ5vC5lvqXgeVuxsN85SDhuVX2PpThKLNe5Nz+6yyNdX71VTNP0zz+/fHqZnkU/nyj/5S+Tp6d7/88eMj6eB75/03R/nOxZ7pe7ri9/3bS/f3qpnAgY9niwWidt8Hz8+N8eq37+d7+nmKSMj+9rpy/Ihub9gXxjBdOvIL1EmdvWTTW+1XnS3h/wfnqx23r6TYj67fkg++XuZFo8noo/nZqellu199bkb/ev1983R5MJqedGVuM9L4PnE2ewewRhi5z6DSPwN68qJo+fX30AR9FX+BV5+f3/ALGNHJn0JQAA -->
