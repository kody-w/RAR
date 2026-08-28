---
name: "rar-cowork-cookbook-dashboard-create-marketing-material"
description: "Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_marketing_material", "rar_sha256": "dc8d49775c8ed4ea79a25490fd3ad5926690a21d86dee16548dc4b122a166a91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_marketing_material_agent.py` and in the RCI capsule.

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

Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 dc8d49775c8ed4ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_marketing_material_agent.py` first:

```bash
python3 dashboard_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_marketing_material_agent.py   # or on stdin
python3 dashboard_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_marketing_material',
    "version": '2.0.0',
    "display_name": 'Create marketing material Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create marketing material - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c4ddf7ad9d21a31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCreateMarketingMaterial(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateMarketingMaterial'
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
    print(DashboardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVpb2X2FyPlR5VJViB1VHRwygDYlNgBDI5Sizg9g3AfLr//5eJGWW3W7PtCfmw6iiMgWce/bznHMv+cuL3bVRUb98edF8O4c2dprGkV9Ddu5BXNEXdQJ+FYkD/kNukbd17HRtUTcvn148v3HruGzjIgfLlbrwOtdvIBtq/DT4PBHbce57UJy3fm27bXz1oa0uCpBnN5FT2LUHBUUNubVvtz6U2XXit3Eegm+APrZT6DNUlH7eAAZAnRFy6qJv/PoTlBfQEiMJyHaBvAbKfd8DYpwRaiMfusZ+79evQD9/sLMy9ZuXLz/+9OklBt9fvvzy4qZ2A269LN+U4O7yxTfx4lM6YJDaeQgoyxF4KAfXpV8DhTNwy/MD6Hn1cbL2E/Qf/5H0dh02P3z5mkPPz9eX6Z/a5XfF2sJuWqCna5e2E6dxO75CTNrbYwPVftvV+d11wMF5+PpY+Z1TUUJ/n559fAh5Df3249cX4J3antz/9eUHCHjy60vdTd9fJy7lxx9e0wK44uMP3/k0nXPx3XZiBrR+/fa8frIFhN9J4+Au9e+A6yPQjv/15TfGTZ+H3pOdYOXL66WI848PxmVdXP3czl3/4w9/xtaNfDdJ46b9l/j++GAc+bYHbHoq/sOnu5N/gmZPg955/rnYEoT1r1gCyN/EfYKejvoz3nf//wPrFBRB8+7xf8runy2Y/R368U9t+68WfIKCry9LPwXlVttO6n+BfvmmKSvuxw/e95sffvoVsP5v2WhFV7t3Dt8yO48Dv2m/ffvxQ3O//eGnHz90Jcg1386+dXX6z3j+M7/e5fzOg0+qj79fC+Qf8yQv+hx6z3Tol6L8t/rXV8iw09j7fr/5Av22XqbPDJqMeBP6cMFvaqYBuv7Gjz+8/AowIgfWdO79Majyf/93SIzdumiKoIU0t+haCAS4jTN/Ul6PYgBNzb22ax/4tYmBY590IP+nCE8aFwH083+6dygFoPiA0vk7BH57wN+3d/j79gZ/P79COmBd1HEY5wANVUZRvuZ26OftJLasfQCG1zvwtf5nAEWfpy8TWP78L3D/dmf0Wo4/36E+fmCUyvETPjVd6r9ONp4iP39a5ILu4A++2wEZaeEChYIYgOsnYHtTpADa28kfTRKnKeTFNTC+qMc7b+CzLxOzn3/+2QGKfc0fgIpBj/bRzAHBuzrQ58/AsiCNw6j9mvtuVEAffvn1A/T/oP9q1Z35JEMB4P6MCNBwp8kSBCqsywDZ1EcAANvePSK//Pr0L2CTg34H4hcHsf9YDDI08b03Z2tb5jNKkJDjAycDB2dlUd8bVdy+QnwAvesLhE6PJhyPiqaFPB+0L8/P3akz2cCcd0/mRQs1IA2bYPwEdY1/l/qzU9t3FTNQ6nb7MyRyCugaRQp+TGreicDiIo+B+99T4XEfMKk/NBD7xuIVkqachEq7tsuotp8yAvsRF9At3pYD5jboof3XfGqR/uSqe4E83AOIgGfcZ0g/TzEHc0AG0MBr3mTfaeypt+n3Hld/zZtn8tv1FAoXNAMgNOxib2oJf3umVBMVXerd/Qc0vTfvRxS8Z1TuOcj96XzA/+Ng8d7Toa8dCiM49H9sKJnMYTYbdbVh9NUSWkm6aj3cPCk2heMxjYHZ4K7FvaS+zwtvaPMGul/zNAY5U49/e1Deg/OkeQBZVwMdVEaF3gyv73zviTslYl1PKW9/zd/Q/RPw1B3KQOxAlYMqmJLvTeD09E3TCPhruv7e6e+BBv4DqQGSEyo7JwWJEwBHOLabAK3qqfiekQFZ7E+F2EexG/3OKghwB8kC+ENAiRiUE+gAd9dJBTATxCKoi+w7eTzNT+Uj0B4EZlf/FTqB+plyqAFFC4agiQZ44cOdFZT5wMdAxXcPN5FdPpSZxt2ngvYUi2IK+28j8Hz4PePvukzqA662Z7fAl/0Ewp4/PCL7ruczVkDZbKrR+6Lfh/tpK/TbNvS3r/ldx3fcB6WfTh38N86BQGpmzR1rJ+RqAPpk/jOBQCbcm/Xro98+Gvq7Ll/+MON//GvbgHsHPf4+cl+gqG3L5st8/uh6b03vFeDGHORIXPrN9wb4+VFqn99L7fNbqf2O9cNTX6C/pt7vWDzz+guEvMKv8PRIiF1/StznB3iD+8xan/Hp6ddc9b+H+ZkLE/Cm41TVb13ojQS0orD2w4n40ZWaqZn1oH/eYRgE4mv+ngrPQgEon4dTC22K3xTwvR2DwD7i9t4twKO8BbK9aYQL/WmDk07qN/7Ll7xL008vuZ35/9rGZmoKIF+BP6YdEagdMBS1sX+/eh+Qpovfb/HuVQXgwCu+TMX1CZqG2U/Q+1z6CXrbKdy3X3kHtko/TjPxJBKQgl/vtO/7R8d/Abuzdiwn3R/bn2kUe47If1Riqimg8R1kp9b1LNJJ4h+YgC9h6Nd/ZCLfv9jpEyma1p7adty+1XcD9PTAEPQJAtEDdQdKCSBkBxb8UQyQU/tVB/qjN5n73X/fzSoetvx6d0P72EP+8vKGGM8YPOdFQA5K83Mzdcg5yFQgEFw/cgo8+59Mkk8WAObAGDPtXl3awxcURbi07+G+TS3AA3wBBx5me8QCJckFbKOIR5Oe7yMkgdOeizsIitoISdoLBPB7JOe3aRKIJ7VQ23Zpl0Jwb0HZpOtjsIO5PgKYUJgPEwssoGkfBx56X5oAjHza+rBtcuT7UDv55GnyLy8OiQPKLd7wzOPDzReGTZ0oR42cRU361tmc8058qjSndWphd0a2J1dacTqbEGhM80a3ksbdCpHcc3iGC+okStyWZBVUCxx3pjGlltuaEDkWm+CxizodJiQBQeCUwarrAhFbn8OsqGuFo9uO0XGGwDvepLbZbnkba+JshBhFELSKUH0Dk4ZxyynBC4LsdG3FytHZyyZTt2u3rMBgbY/rZab3uEF0GFdK4rXDttu9wRl7pt+IKdKd7Nxoox3ZH+tVbs5v6Q0fclSc9ccidFFSdYyKXneEEJ+6CJeWJbHobjQl5buMEnNKvqXZXAysubXpSe2031w3GVa17X7EjMIjhQMm+KKhnzzmNl/ZY9bUR3iD3/aZVnUePnMj2WwiNuJiCz55SLHfsjO3objKORr7WWcpNh2dNu0ujVLgk8zs24N+ktO9zUnGeKgM87RDaq9u7aVedJbdkoq3r8ZWpS+8rvOt2Js2fVt5OFZp65sUalISEV6Yeby4Jsq1llqbele37niaAVXgzYiVu4YNjeQSzDqNuDSlKxA4v0mNsu3EhKxU33QzSkZgbpcp5EDczMOSILX4KLkwS7vBCV43PLp0AulgI9VAELqqztp9NTT5LI5uXnurpJrRxGjmE0d8D0eX2KeJSqmzLSJGwTXnPGfuDLdCPmzK3OtQ83RVxvVJxgKWkh11lOuNgaopOUdjnEtcFMlW/AHHonCUFLcU+sW54rGR7hW5gs8Zg6gR5egzNG5u58rZbRXDrMTGCLyratM7ftEPlraoRS1CFB43qkzkG3QglsQFQYKbl5E1WJjT8NjdljdythOdk81z62Qnoo1uzyrNBmCI6IfEMGajuNi7wXkYg0Myi7qgOQQDMV+mm2spnwv2ggQot4NnCabA5HyQl4W51eWFT5pn5diWNrVr90Ml9q2+qgnbdjbxaOVIYmW1cOTP/SI+bpdsxdBMrgpORhwri9Nv+oiI5PKa692h7YSkNURcjprGOckGu6tnyw0nM5hW7g/FMee2teysVDgW28QuVFM62SphHNFWvsiuvKtw+ry7sitna96ups5LVzmnk1u02JE4ncw2SnM2IyEp4+1ZvPbKzs/21xDlzCu9zYfufEjzszNX5kMasyPiGbs9tx180zIxyejtWqAdJg4ttUlQcR8V5GJ74YYsvbgr9bIKGZs8Cgq9XetIcCgp+LYZIs6P7VK2O3OhhrPW1q04vUXjbIuuQ8WM6RF2d7qs44K2gyUDxx1zL25n6WLnyIhx1e0riuKWxmoaulb0q+a38tFn+cxWNmhiVJa6U01PGNYkolrKKtAKVzjQs6jm2t15LDDRlM+roCtyYy8tVlZ+vmLjWjP3u3Kfz6PTwC66aH+grh7ZBTeS2EpKp2lrymYFTnf0xDyaVnmJZskxPkve4aKZ0Vk+S7XAc6fdTTh7CKUoQhnbR2+eZ0XFSsFtmBdDM5Cu485XenZLGUrWAz9f+Nkto/rt7nImeT7DChmeH01WKZIyi07trF/iinOZzb12xopMgO03WyFckOSGz9cH/TykSREqJ9Y981E63x8UjD/ay9jaLkO56TejFY4qgTi3tMFDNSEUVHfnYjbE4q3UOwt11/Q8GHZnNtLKbj9HjqlroJcyXN4Qng9CbofFrDoPMZgTdCbuNkjfr9wk4TVXLTjY0Y3rHusvJb0Kw1UM4xWZRlHZS9Gx1YzQxc75MmZCVZOZkeoPu+qcLFF/PaetxZyEw3KVtVjfHxz5yDpbm8QX3vlURbCa+QDsA3oBsJe8iRpn79OLqJ5baqHsm6yY6a1RNagfMdKgWr4fBflw663Qa9sbxRGrI6/SqYmeCbq7+gplzuXVct4cl9sxmh09latTjKhrK2IsjdtqmVG4iG5GEXsA+KsRCcIe2O5azCr26K6X4cY87BvC7xM0JtbSkZD01WJP70iC45LKRmKhXzMhvTuoKLNaWDkap/ZFztCOGwKjqHOYZ8gM99PzcgmjFq41BqLMV+O1ynBzZ2Re7slCNdT7s60dmcuGhjcE7StIW+938HBKpaKpzWq+Bb5kqn7OscdwbHYjka4MdqCa8xnjTmgxtNJpfdlwPlJiFELsk5t6W1aDi1qnhdOke4IIs71aDILRZpo6XAMK3zocFa0ize6wIWgTgWNTiufjhj7eRCteD+3lnMXzeiV0AargTLtPNqdFZh1IRLkdt2TP5ecjmQJMhg8uTxWgHFdYtNuvNsmu1IgWFmhV0PhE3AhdHBGzOkwWXLcSdmF1KuV4yzPSph95aik6u7yWOQk9oYsrf6DCEql2/LqSL3XXZKlVS4yTOY13sMQ4tmduIEvE1bDXzmGtEruYGee7dR7FQ4pdMo1nYklOubWU5T6mUPvYETPL1ldK3NSna1+hC2Gbkvwpq06tLfrr6wGxUx7ANyqxJUtKY9ceL9XJrBR/yRHVWetQPYBJXvMv4oECAIUyzXhbbUIsH+uQPOcneyU3O9nnnWZDs7bkCusMAAUX75ZJfA2LbeGwyunKzKjO0bZEocH9rfeVEkSAXc9dz4tvid35XLlWGV7oZiQMb3XyOFRZVVSVcMyXc6yn3MQJYCkMNfXa8hzOkOhAjSt1u+xa2tbNuX12BAUjj53pkIEp+pf1IGfpFaUwNNuvFmoxMr6ANXXEW4UOMkhg2SU6oxxNXiXodtGbe8NS0wM/4GmNzLzc4AVJtmyBI8NjdnEEnc7czuvpcCi50/VYVMJlTG8M7ZM2q+VGvCCzcrtdpuQ+DGoErU62QBrSgWNDEXeumTHs6MvG4UjHiip1ae62SMxqlGcwB4KI/Gq0QenMdKZM+BGujns43piLUsIjYoC7I+IpXdJgjDAShKDlt3yJylmCX45YepW54xAcK5LkE0mXj0K/Op782VE8nHbAB3srA+OnwdRkTMaWQGqXwj356GrY2Scf1zdrpFHRI+dHF4Wj940hHRuckjQbLme6cShFC27z81iuFcxId2p+3K5xPJ6zJ3OWJhjp3g4mnB6uC5YqJHSZDwSqV2gopYCp7AyphscNg2DUxbbONXwmtoa3HIU2wUnzJK83woqaGYrayouWoBMhwJoVLVlIo4tm7MVHK19ysERf3B0T6t3MikN/X9wMLWkrstK3qgeGNLbDD3upvgUXbzMr+TPmh8R8XWOLrc6tLOOokbBUU6dmfzgdSpuXiD7rZaAUzHHLlu0TVgIDxeZ0K/2TsGePY0H1UXmmckM6neo6RwiU1nGDE4duTDCmEcG0GYntMrB0RQiyltqNhpBtPa5MpCV2Gu0wjlUsaNbXQRMPEpxbRLdbpPaqI3pB9qMlC5NtZWY5vPfi1NifxQNWbHixROY2ylrz4bK8ZcnM3aFMZc0w/mrDcnVrEX81lqzIKXTnn9dbRzEXYNto+nGdYRFI3jOM9YzQYbpM4yJLzWiFo06xdktZj5Rltg2zdIun517b45u9oJdE5Wn5nlltT5Yehe6GqUZRXPsCGO83g1Hswmgz+JXJJiRl4mhzsDshCxlDpb1qvvRYmpTPOZIzx9uOYz0tni/XSLEBRSuucispFJl2dq1g0WfqeEhSXA1Ny3CvaN4E3tKBeUSerc8YsTX1HJH0/b6Il9vUR3anOevuNZfhAgyMAM56UQmNtTI7w2dnCxWd6/R2IPckGQiS3rrS+jS2dHNp6I671ubs7FEM3kVxizmNteGw9tJjx9OyN2TLPHfCohz2ZQs7ZNwkpLKbhyO+GVK9ozsn60lrIImbXbsZhlwtdQ0AKSEGhdvsY2zhdGDfxEgWGqzMs7PEZSyRDW/UGSajtzR2rTDmSs2IPanVTE4G3ikKRQdTyb5xaHKcYchpc40KXaL2AG/CTd/P/RDHivS2xjqqNwuaLm50iyzm/YEujGJjDNc5Gc0v5dkxsa4LzukiKNKkv3Z4NjNDYYBZxlNNvJtFJ3hOGK3JCabZpgrJjqMtLqUau6irpcCAyQug8q1UB5bQZVIqOtmarxNv69NNAneYW1O51bBtATeYHBU0xm/q1meIrVzLhG5e9ydPzVj1xpO6KF4LR7tuJMIVTYaKfIy3ZF5ZUJI0YBvLWK/rxmz7iO5mI1oT3Hwv5ALY+GjWXlZgexU0NeX04uYQq86tcNIC7ZRtrZjqtTOKAElQPJ/XW8wXs7UHGxi8GmHmiLqSfMVROaLONxprM7672QuvYK0B8BPAPtPLSTRviea0OErjDO/FxllY1OXckf4ww8aNY+/2Iqtgfkm0Gy5orDYdpFDSM81T93R9tS5rkqfSGt7nHCgGIo0IGrR8idbK67oHM0gvw8UWjJe0OzO4/sIGhyGi4GUx6ujO82/RDtueQDdm6GO9MeH4Em/XcxMvZ87tNtCzi6xYgc2QyaoEO/fWazhYEZZFeFvrYaKxtTeeLUViI/HQGxVGz4vjDtkgvKbM6Vhu8mLZ7Gda7raOuMDW6I11LrsrQY6mlRFZu77AIbVb5GC/F2DahpbqdBXg7YDyc3PlU1Kdn0960K0Gj8v3ct0f1HlnzQYcZH0UUrS74W8nIRb1+mouFEe2WoKshSYIt4JqSamKDCPGYfWCrqh9fsrIjmq9PVJYZIscT3pMokwOe1eWyRiXiRuqzPorjNUFJWp7hr5sZyc3HyvWGIPlQOqk0GSzgrg6eW9IYCfOS/hhE2E1KfW0gKTdOKeJGTrOsy72F/4amafNip13s4DSCt9SryY51AjWRJ7TSajQzA8ZUkcdSTjK1ZAGD4kVh5BvpBIU1yvRqMuZsVhSwbkNDouleNYJFom4imd14qhiJ9SaI86mty+2io8TxtdXpprViySIKpu11vvDrK5x0vYoVt20p/qCyVst8o2dS5PYcK7XAYNxZrDQI/C8QjuXVQ5UO2MY+8Lj2sCfyF1DufiCk3XeIDd0lFZCsKD2ZrstvJnAHpc9mEGw4yy9IWLe8MBDfbBuwfQdBLws9gETVvAhj0mY9Z3+nKiGkrJXDS02nmyH+lLoC4f39G15gEsUDOXsmepW+DiLdh4xPzPmfJ5ESggGHTO8dntkO/K6RngD3i6y9dV14FV9Rd1ama0LDuT++ZgXcGI1HbI18tuBR/QFwQdK150TRdx7wfLSb0nuvI1pwj9u+ITU7FW4Q2dSqM5hbZ1mmu7bwVlYH4Pr1XaJSyJt2luz8OoUUZRCOdELLCD6kmGYv798epnOop8nyn/ldfJ0wPe/ds74OBJ8e790P0z2be/LXdaXv6TVT59eajcGOj1OVJu0C5+Hj/9wnvr5X3gxMTEYH+9pp5dhQ/t2At/a4fTXRi9x7nVNW4/fmiLt7oe6n16crpn+7qH59jy8frmblpX3k/A3mdMJeQFMLdtvbfE06GX6u4TpDY/vxUCB52X4PGQGi0cQpthtvmEk8c2vy8nW56uO6WB2etfx8uv/B3/3B5/oJQAA -->
