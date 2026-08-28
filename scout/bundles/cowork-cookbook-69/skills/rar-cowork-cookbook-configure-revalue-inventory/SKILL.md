---
name: "rar-cowork-cookbook-configure-revalue-inventory"
description: "Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_revalue_inventory", "rar_sha256": "b1decf0e7c6e25eb36c7d2a737a14e00b559deebde4ff1a57b7a05b80a88cf18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `configure_revalue_inventory_agent.py` and in the RCI capsule.

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

Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 b1decf0e7c6e25eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_revalue_inventory_agent.py` first:

```bash
python3 configure_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_revalue_inventory_agent.py   # or on stdin
python3 configure_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Configuration Bulk Setup — Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_revalue_inventory',
    "version": '2.0.0',
    "display_name": 'Revalue inventory Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to revalue inventory from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e68eea6889435eca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureRevalueInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRevalueInventory'
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
    print(ConfigureRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V655LjRpbuq3Brf0hadDcJD/TERFwYEiQIQ8LRqCdaMAnvCEeQunr3myDZ1dJqZnYmYiMuqyoKQGYef75zMsFf39y+i6vm7fObCdxyJrl5nsSgmbllMBOqa9Vk8F+VefBv5ldl1yRe31VN+/bhLQCt3yR1l1QlXM7VdZ6AdubOvD5/zA2TqG/caXjmx24ZgVlXzRowuHkPZkk5gBISus3CpiogO/ik7rvZcvRBPguTHHyYXZMunsHpSfCkMsnUVHnuuX42a/u6rpruExQEjG5R56B9+/zz3z68JfD67fOvb37utvDRm/CSBBhP1ptvnOHKHIoFp9Q3aIMS3tegCaumgI8CEM5edz+2IA8/zP7rv7Kr20TtT5+/lLPX58vb9GP05ayLJ/XctgPBzHdr10vypLt9mnH51b21UO2ub8rJOi00YRl9eq78TqmqZ3+dxn58MvkUge7HL28VFOGh+5e3n2ZVA/k1/XT9aaJS//jTp7y6gubHn77TaXsvBX43EYNSf/r6un+RhRO/T03CB9e/QqpPV3rgy9vvlJs+T7knPeHKt09plZQ/PgnXTQXt6JY++PGnf0TWj4Gf5Unb/Ut0f34SjoEbQJ1egv/04WHkv82Ql0LvNP8x2xq69d/RBE7/xu7D7GWof0T7Yf//RjpPShj43yz+d8n9vQXIX2c//0Pd/tmCD7Pwy5sI8mSA0eHl4PPs16/mbin8/EPw/eEPf/sNkv4fyZhV3/gPCl8Lt0xC0HZfv/78Q/t4/MPffv6hr2GsAbf42jf536P59+z64PMHC75m/fjHtZC/XWZldS1n75E++7Wq/6P57dPMmRL/+/P28+z3+TJ9kNmkxDemTxP8LmdaKOvv7PjT228QHEqoTe8/hmGW/+d/ztTEb6q2CruZ6VcQgKCDu6QAk/BWnLQz+DvlNsQt0LQJNOxrHoz/ycOTxFU4++X/+A+w/Oi/wHL+DQDB1xfkfX2HvF8+zSxIsmqSKCndfGZwu92X0o3g6MSubkALmgECiXfrwEcIQR+nCwiQs1/+CdWvDwKf6tsvD6BMnphkCJsJj9o+B58mnQ4xKF8a+BB0wQj8HtLOK999wm77AeraVvkA8WzSv82SPJ8FSQOVneD6AcJ9+Xki9ssvv3huG38pnwCKz54FoZ3DCe/izD5+hBqFeRLF3ZcS+HE1++HX336Y/d/ZP1v1ID7x2EEUf3kASiibujaDGdUXcBp0DnQnhIuHB3797WVXSKaEFQz6KwmnijQthhGZgeCbkc019xEjqZkHoHGhYYupkkBUniXdp9kmnL3LC5lOQxNux1XbzQJQgzIApX+DVF2ozrsly6qbtTDs2vD2Yda34MH1F69xHyIWMLXd7peZKuxglajyRyV8VQ24uCoTaP73EHg+h0SaH9oZ/43Ep5k2xeCsdhu3jhv3xSN0n36B1eHbckjcnZXg+qWcaiGYTPVIiKd54CRoGf/l0o+Tz2G1LmD2B+033o857lTLrEdNa76U7SvY3WZyhQ/BHzKNelibYQn4yyuk2rjq8+BhPyjpROnlheDllUcMGn/qAYQ/dAv81ECYEDHq2ZceW6DE7P9XczFJy0mSsZQ4aynOlpplnJ5WnHqhydrP9gmW+hkMpWfGfC//38DjG4Z+KfMEhkRz+8tz5sP2rzlPXIKZHUA8MB70oeOhFSe6j7ic4qxpHmb4Un4D6w/QJg9kgirAJIZBPhniG8Np9JukMczU6f574X74sQkm1WHszerey2FchAAEDyN0cTPl1ssFMEjBlGfXOPHjP2g1g9ShqSH9GRQigdkCAf1hOq2CasK0enjhfXoytUNQiqD3obSw2QSfZgeYHlOItDAnYU8zzYFW+OFBalYAaGMo4ruF29itn8JM/elLQHfyRVXAqP29B16D3wP6IcskPqTqQt9DW16niAnA+PTsu5wvX0FhiykFH4v+6O6XrrPfV5W/fCkfMr7DOczsfCrIvzPODGZU0T5CbgKmFoJLAV4BBCPhUXs/Pcvnsz6/y/L5T035j/9e3/4oiPYfPfd5Fndd3X6ez59F7FsN+wRhYQ5jJKlB+72efXxl2cf3LPsDyaeFPs/+PbH+QOIVz59n6KfFp8U0pCQ+mAL29YFWED7yp4/ENDrhyXf3vmJgwtP8Bgvoe3H5NgVWmKgB0TT5WWzaqUZdYVl8oCt0wJfyPQReCfJEGFgZ2+p3ifuostChT3+9FwE4VHaQdzB1YhGYNij5JH4L3j6XfZ5/eCvdAvwPG5MJ5GGAQkNMWxmYLLCp6RLwuHtvcKabP27CHmkE8z+oPk/Z9GE2NaMfZu995YfZt07/sW8qe7jV+XnqaSeWcCr89z73fYfngTe4repu9ST0c/sytVKvFvfPQkxJBCX2wVS4q/esnDj+iQi8iCLQ/JmI/rhw8xc0tJ07leGk+5bQLZQz6CcgB5PVpvIHIbGHC/7MBvJpwKWH9S6Y1P1uv+9qVU9dfnuYoXvuAX99+wYRLx+8+j04Hebix3aqeHMYopAhvH8GExz7dzrB11KIZ7AdgWs9NAB+uAC0TwGMBB5O+XSAuTROuygBFguPJNkAAC8ARBiiLkl7tLsgPWbhMowfogyk94zGr1NFTyZxMNf1GZ9GiYClXcoH+MLDfYBiaEDjYEGyeMgwgICWeV+aQTB86fjUaTLge1M62eKl6q9vHkXAmWui3XDPjzBnHZfCCE8bPaShwsgq5xuvdOQGiS7Uwg5QJpNcbRPdDqTRq1u7uCwz9LKLAzUZq7utssKaiteYOfeJmKS2Br26HpKFLXakuyb1ddwf76U+jivbMoiLS2ZOUsTMrXd0VOvHcynneO3kgVxnRLd2jqf6mOTHFdjucJw41ouD4R4OqxXXuubaK+SiPzekcTVqg7ZrkGP75EwsckM/rhE5l84HvVZT30SDoucpq0HtwgRJJ2eYvSlyRj4Yh9VWGzPVqqEJjyVC7iwU8cJkviub/M7qo96jm8j2g1i4+UVnuRXQLKH0D3lv3JabPlh6O0YORXJ7uTa5cVOZdFHVVs5epNCUGtu+C7GZj84lN5ndGpeJy1F3fFjWzv2mvlLCjZQ7VUs3RwFxAnN3IhYXJ++snbXeyqjFC4OBaWh56WsHt/CFU5/44ixfL5iZ3c6LZrkGK6JTa2xTO5u6ZJFuY67yBeIXDrNpx9BxZaQPmGu8iassPiw4ng7FRq9CuYx7X0FZErsDyw9k8xQiC/MilofauWxK8mTewu22CZLKku/WUbvOhaWyjNsVRrni2PCYsu+HxMyGg+XIbOp7lGMdqdS82SkHyksAhGDjEonhK/vwuOKRGvQqi4HoWHJqrt0FNmD6HjCq3AYXWsBcXLyCtkBvRh6U9ME8HX1pbJZgZffe0j+Spa5Q6KkgFltmr+wKqlZX22sxCgOCCdFtv2iuto+ovXOPdvh6YSaSXWKcIob9OO4I2y+TenXnFffExAyJ0EN9kbujviptrBRMVr02tXxKz5ax2fe5jB8w9yhtznPJskhUPjbpXbXobXBwlpKMyykV7OSIuaoxrudLu0CWobLmsHCwUoRrVS5dufXVxV1awZzkhl0TN1fqW4DmWtI7F8fNDtZp7mqlYXixKEitmZ3DjiN2iSkY45KOMp9C7HK9sVhKYyQWHCi/5dPt2jvrmm92hEJsCtHdEPfqTqCJn8gtvza3t5tRxSsfXTrqJZEUlbLJKyEN5XiUCNuowhDIQHVJZBFWibhGFElk9KuWJ/u8ZCXtcgtrtjoUwV3qwIjHbCdFwwYTA2V+vPL+BdHF1DLIARca9N6TbR6zqm1dHFxktOZUXLA0JOxIXZH2CssrjyMZc749l4gS1es1epkv+TkiJXJ5WlnmUqPqUtv6Z+cyrgaWZRovHki1wwXRKu4MzIJwvFRtPOiRs1HI7ZjIaeecF7eUdW+2vDhsy5XBBKZ3qf30VsukdUEXl+OtPV0GSrHuxlCu9tU+vwVXycJ2w2W9L25Uhp7KXXyL1bmdMO6yEYzd1aeyg+9eTAEZCxAVO6WqDKyn7fasouI9yTOTF7DIvGWLJclu2WE57ulUDTZxfzKqi6UOPrquFeEItxU9a6g4evBVmUccdjVkkStv3DuKHHPjgp5wEmlW2nCRUVXq6d1l1NPVvV2f83NuxLvh6uN91VVI62OX3AlzK+XYXqc7jF6IFo/YuCptrXt3up7VG5fTjeLIIl2txuwiHZFaZG3SOOry3tcuY8ndGifTpLUm0RtBUhJ6eWWQfBUtF3Q0bvf+1kfAUBPXOZU3qhbWrV/c6f115OtzttTHSNZtKQlXw2qzpS6KeqKOd5cgOTuqUkUf+NYmeg/p72fDXuz2S9W1T4bC54lTSLKiqZ53wCMmkvcmd+7LwttYZk9TzU70Wl3HVyfDFubukT8IHZeT2h33GN1Bs3Mq5e2CmgO8xubD3elP4HTNYy0crteLaYk3yy80smWFfZgke4KFPcAubJZcE/T6CffjyJSXYXhA7WHbNPQcoUYQhlRmSvtNrmwqN9YPjjfe1jzPycHFsmPL3Z0PJ4dzNaCUjnneCwvMorbnWEY7jiKkVaONa+1qn8Z2mwV6apf30ylecuLpZnV6y5fimtOuI+dSa3+hYL1oSZi5criKjU5YKHF+WZaH3FautF5Up/V+eY7q2jtjsn3rWMW6ghzZtiS7sLnNaB2BiIW0cTpKuOdFoZQrFqkz8dFopK6GCAQzi+MUnc2V8uAsSrmLuQ6c7me+iY1UWEUtIgdB7hGim8Q+vseZqkuidg12m6150QhSXl46cmC13sB4zViZxaiOroANBrLMhLNGr/jzqcW3FzahA6vgrsaJtCCmWk6idcnaldZ5fmrqBTsc7s2KojYqQYANODBGfz7m2PYM+ntz2PV8y7tHNUNj8tLJ1yW6N63ViUXdYEHsTwrR9crRrB1v39hGqyz78dRucVPZuAt6cw6O6go7Mkd+557Nyg54w7aCbLsPT24sNMkp5H3GMbK2vVjBWVizolllxFHfb/iwNxs4MjZ0ajvNKEfndL/1DnLlUvOjfFG7WnKQ1W0/cuYSwRuXFG52kC26c5UcEp9Dyzo91VFIYke5l0bh2Fz5jQvuEg6oc33JM4oLW7wvKyc5WoEYnURBxsdDxqrhYb7f2GfBuyXDKGhUsKx3fNTItpWO4hZt6k70d6nHzef6zdjtxKy5plh0uPPpaHXGfjwonbTH+czx3GW04Bgjw0b9QJeLFHHVy/JM8XSFzsnIphwdq86YuhN54nrdL2/kAJAVSJBOMzvT7a2RpDbBvFQInR2XamgWe17f6Jq+jU8L50qLVlItqGEI4oSywFHuMB32dO0YpI3DeR6dHlOuXRCnyFoy65z2TalyM24l6EMgrfnBI483tYvCTWrL+WW1t67eeBnD8swahHiAz/JSdI+ofF3dwG0brNlSz2T3HjtLiPxuIRBzLBfz7WVJo47Vawcld6TuutPrsTrOGRDtRO50Lf2uuVvEpsWWi3FtXcxoD1sBduS2xzC5COudercpuyX4PdkKxT7VRqmw7s58WbB7m6bw7YnmA/mM7I/Z/XbIh7kgEaDIiOawuKu5kd2VS7YKlpV8xXP1bpibeI8lJ5VBr9hlqUYCsdTt1DlIx8M9EGHRTgr5fs4aFCywrt8WlnUuY311dHleCrRoLO5b3x730l2KlfMYFCfHIcfztj329o0ZXSP1CErbiDi1vK8uOY+GjLnq/YpF1AvjH65Si6/Xo483+6HYyllPMsFx51Rd6OhKBTY37JhWaFMeVGZJx45odQChuLPh9ZdIBLWpYpSpGgW6UdPKTLJssBd6y1bulj+0qJTEgc8sO5VcKakHuB13rkYKPyjsJjJdsji7rBve9bocCDM82sEwjEWy6IRcCMpFnxmOsawiF7UtPNGigNzw7XJVuFa+WSkyVHR7rxGJ3vILqrKuiXKmCmerHw8osae1ZTZepFN5Sq1QYPd+py2FoTY81WvxUNKkXWJFiBOZdZahrrdNNGXE23lWG5slkyzJgrln/VjWPi3ChOG3vrIRJaDZlb5FK0VOtywvc4HeIz6xTueSuuMTk3KGvVLuwY1etE2u4eTgu7ZdCBJYh51/9w3lniAkW0AUwagIIxLb1rOTw4JLWF/3+01HgvMhkJxqCyHDZpRrd9icpdDO1fVaqlHGPtdKHgAIHrTIHdq1EhukzumDQ9wPDaesRC0j1Hm5XRQl3i462187EodxPKXwDiWT1yDHe6Xiah6sl1G8nGN4dRUOmVPRmnkwhevc37sgphYnKalLdMWz3eE+VKRJuN7FtdEkZS+UVNX5anlAuRUyNxZ4frkhHlb1wnGQPEbEg2ugwJp+DNT0xtj0Lia29DZUNKtDWmXIIJ01IAI0PA62yWA85rNo2OPaGl2VnoT07WlpHMyFTvsw/1JHTOuh214P1M6YR7B/FEu4Dzqa1n7Q9uy80Zze6saMWO6LunDWWVqlGTEw2mnDLsXA99utiBVzX0SURgdjwy20VpifCYq9KvPhYmKrfpSRTnR9SUixq4qJdUBvnXmkwdjWaf3ONCftxjVWShClfl33J4zBDxtmHZ13cybsBoRby7dGNON0Pl+JSBBwJBAXd5qJGzbrsUwz1icT4/zDZZtu1XE1jsqIWgbLcItDuIDmWO7ZoKeGLptX5wAzVneaZwV9sxM83OjWY7wbz2seHxRNUwZ8i5HYhvNWxyIsrT2gE9HG2ty+w27g1lV4Lun+2beZm57dRYWSiGYQrV2SjCR3x+bNOhFZwFphMJZOMiYdSfubcEViGGpXRx33z4dMzYGQyoichG0Kd9nqbn933fu8KaoiK2VKGRcenbtrJHCQek6N7DzdZC0leqwgu/xW2awtGtHSoceYuUqfE6XFhqPLHVSDw3jPP5ywISJB2TMe6iPN0RAz0WrWjKXhd0TDkb3lGbwVnXEaVeSLYjHWSo2VhE+CRGbhxvrGJ7smTpFTTzmEyXG4diobKkj4DqaR1K8jG+GRkgPSaQ83wnahqwLWmmW536Xy7na7O0PS9LuWQwAsiwf1GIuKsJX18FKB3S5tWybPiJTdr524kpsw2NWpEhGRLijqqhB2FXZeyFpf1qqOrIV+CC03ofrhQJpyPF+eF0XADXwDk3vJDiN+OpwSss0wsaxraE7Jx0vc5dvjkLbMmbjtj2nHVOl1XbjImqLE43nw6e3VC6pM2fi04RxYAfAY3wIdtGGlh+sgWaA9kaq021yP18Y/tIwTwzZZzKuOulX0ifXi80Lvz0HuDFanBHiPnjNJb3zHgvtVcF2CVCM2KkyCTQ0WqZ9Ta5QEmLzk9GNK8iBlKE267dYjIWByWyCXem728pGvBkbViEiKcQ9We2aN5z2KXA/iQYHQt1Bq/BguUK6TFHHOMiGWhwwRA2knKZuGNrFhIYkdEtmKTlXHFgkjiAC0Cvy8v1PzsBrm1/623Q80DnULQpO9U8ujIA7CSt2Lx/jSSM1wZbb4niMl1CITbW1pRyRyGGVhwU2Zy1eyvDeaC9H6IT06S1ZKUcsH8ZbBLXpV954lKGTgnps5UnVutyqkbcjje6LTfdEVeddMRfkuOiMZUWu2MC9N46O9e288K6Bdr7f6mPUuPBlfjDKw8HJj35BrxOzWPGOjGlh1TETceYYTHCLmVmQl+Hh0r5JmuIjAKmIq0M3EEte3ytP8YmemtdWdb4xwx315zFkJpSs2E8I5cJcIdxtQIMwXzaHZsNoux9YMjp0Klh32Zy9sncPJ1/brcX69ybhRb3LPL/TNIO9TZ0BSWu3Ru450sdX4Ps/Re6uii8bDonEpWqt9xOs4GgghleyRikmrnYVIbWjgYXjnxx2VG32XpqN5tBmEYwvH2vKkkHEc99e/vn14mw6lX0fL/8pr4unA73/t3PF5RPjtxdLjUBm4wecHr8//kjR/+/DW+AmU5Xmi2uZ99DqE/G/nqR//yZuIaeHt+b51eus1dt+O3Ds3mr4e9JaUQd92kG9b5f3jMPfDm9e30/cV2q+vQ+u3hypFPZ2Av/OaTmofLwO+dtXX51vht+nrBNObHBAkbgdet9HrbPnDW3CD3kj89itOkV9BU08qvl5tTOey07uNt9/+H6akkyiBJQAA -->
