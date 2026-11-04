# WildhavenCEO

A CEO prompt wrapper for supplied context, inspired by kody-w/wildhaven-ceo. Paste the relevant strategy,
legal, budget, pitch or playbook **text** into `workspace_context` on each call, then ask a question in one of
five workflows: `ask`, `decide`, `respond_to`, `daily_brief`, or `quarterly_review`.

**No retrieval:** it does not read files, fetch URLs, index a vault, discover your organization or retain
documents between calls. A folder path or link does not provide its contents. Without supplied text, the
prompt tells the model to disclose in the first line that it is making generic operator-style inferences.
Grounding is a prompt instruction, not independently verified evidence.

Requires the host-provided `utils.llm.call_llm` shim and a working model provider. Context is sent to that
provider; this wrapper does not add privacy routing or a local-only guarantee.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#wildhaven_ceo
