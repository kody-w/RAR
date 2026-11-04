# PII Scout

Scan a folder for what must not be published — secrets, credential files, captured sessions, emails, home paths and any names you supply. Reports file and count, never the value.

Skipped directories (including standard exclusions and symlinks), unreadable files, invalid UTF-8, and traversal errors make the verdict **not safe to publish: scan incomplete**. The report lists skipped paths and covered patterns; no matches is not proof of no PII. `max_findings` caps report rows, not scan coverage.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#pii_scout
