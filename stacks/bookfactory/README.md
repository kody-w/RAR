# BookFactory

Five-persona content pipeline (Writer → Editor → CEO → Publisher → Reviewer). One call, one chapter back.

Requires the host's `utils.llm.call_llm` shim and a working model provider. A failed dispatch, empty/non-text
response, or recognized LLM error response aborts immediately, including failures inside Editor and CEO.
`perform()` returns an explicit incomplete report naming the stage; error text is never a final chapter.
The final chapter is saved only after the Reviewer succeeds.

`run-status.json` marks the current run `incomplete` until all stages and artifact writes succeed. Intermediate
and older artifacts are preserved for diagnosis; an old final chapter in a reused workspace is not evidence
that a failed rerun completed. Filesystem failures are reported explicitly, including inability to save status.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#bookfactory
