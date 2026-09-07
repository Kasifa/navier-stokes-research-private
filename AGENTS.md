# Forward research role and current rules

## Current privacy boundary (2026-09-07)

- Public overviews and ordinary website maintenance run in 48-hour batches, with no empty publication. PRIVATE_CORE archival is immediate and independent of that window. Management accepted migration/privacy QA on 2026-09-07; use only the existing publisher heartbeat automation-2, with activation recorded in publication-cadence.json; do not duplicate it. Per-channel FIFO uses one execution lock, and waiting for a public window or CI must not block private archival.

- New complete statements, proofs, constructions, estimates, code, data, parameters, certificates, manuscripts, logs and attachments are PRIVATE_CORE. Only the fixed publisher archives and pushes them to the private source repository. Research completion never authorizes full public readers or source attachments.
- Public output is PUBLIC_PROGRESS_OVERVIEW only: reviewed bilingual high-level object, direction, reliable stage and limitations, without reconstructible core method details. Semantic review is mandatory; scans, hidden links, collapsed UI and JavaScript are not privacy controls.
- The user explicitly retains already-public historical reader files, the two approved papers and previously linked frozen attachments for now. The exact 323b543a historical exception manifest is finite; it never permits exporting the entire old public repository/history or expanding exceptions without specific user approval.
- Transport authority is /Users/kasifa/Documents/Math/.workflow/publication-targets.json and scripts/ns_split_publish.py. The old full-reader publish command is disabled; source/public identity, visibility, independent public objects and allowlists must pass. Do not bypass hooks or use raw API/--no-verify to evade these checks.
- Management accepted migration/privacy QA on 2026-09-07 and now issues the user's conditional joint resume to the two existing research tasks. See /Users/kasifa/Documents/Math/.workflow/management-acceptance-20260907.md. This does not start new paper or strategy work; each role owns its scientific next_action. Any later explicit user pause takes precedence.

- This worktree belongs to `研究任务` (forward regularity), not the reverse task or publisher.
- Current authority: RESUME_AUTHORIZED_BY_MANAGEMENT, implementing the user's later conditional joint resume after independent acceptance. Resume from the actual paused checkpoint when management dispatches; a newer explicit user pause overrides this authority.
- Follow `/Users/kasifa/Documents/Math/NAVIER_STOKES_RESEARCH_PUBLISHING_WORKFLOW.md`, `NAVIER_STOKES_TASK_REGISTRY.md` and `NAVIER_STOKES_WRITING_STYLE.md` before using older local instructions. Historical freezes remain unchanged.
- Do not alter remotes or repository visibility. The fixed publisher may migrate only after the management quiescence check passes.

# Published writing style

These rules apply to reader-facing text in `public/`, page metadata, research notes, and downloadable versions.

- Write as one individual researcher. Use first-person singular (`我`) for choices, plans, progress, and uncertainty. Use a neutral voice for established mathematics.
- Keep sentences plain, short, and specific. Prefer “我目前在检查……” to slogans about a “main attack”, “breakthrough”, or “research program”.
- Avoid collective or AI-like language such as `我们`, `攻关`, `主攻`, `研究纪律`, `三重审计`, `杀死错误想法`, and unsupported claims of importance or certainty.
- State what was calculated, what is known from the literature, what remains open, and what has not been checked. Do not imply novelty or a proof unless the evidence supports it.
- Separate published results, conditional results, preprints, calculations, conjectures, and failed attempts. Link primary sources where practical.
- Keep technical notation precise. Plain language should simplify the prose, not weaken the mathematical statement.
- Follow the central writing guide; preserve mathematical scope and AI disclosure. Historic paper HTML/PDF/source remain aligned. New complete manuscripts are private unless the user explicitly expands the finite exception list.

# Publishing target

- The publisher stores PRIVATE_CORE in the private source repository; only reviewed PUBLIC_PROGRESS_OVERVIEW content and fixed historical exceptions reach the independent public site at `https://kasifa.github.io/`.
- Do not mirror or deploy the project to another hosting service unless the user explicitly changes this rule.
- A research section counts as research-complete when its analytic proof or explicitly stated negative result, required certificates, independent audit, literature boundary, figure package when scientifically needed, release manifest, and frozen source commit are complete. Reader-facing HTML/PDF, bilingual text, homepage entries, deployment, and online verification are publication-completion conditions owned by the fixed `发布任务`; they are not research-completion conditions.
- Each research direction sends its own frozen `release_id + source commit` once to the fixed `发布任务`. It continues only when the user has authorized research to run; a paused task records the handoff and remains paused. Neither direction polls, waits for, supervises or reports publication.
- Use only the existing task titled `发布任务` for all website and GitHub Pages work. Do not create a task per section, version, repair, or retry. The publisher owns FIFO ordering, retries, deployment waits, online verification, and `/Users/kasifa/Documents/Math/NAVIER_STOKES_PUBLICATION_QUEUE.md`.
- Hand off each completed PRIVATE_CORE freeze once for private archival in the single FIFO. Public summaries have distinct approval and verification; a private-only release does not wait for a webpage.
- Recaps are private milestone records, not a per-section public obligation. Future public summaries require separate semantic/privacy approval and never automatically expose a completed section.
- Keep the latest published-research endpoint and latest recap endpoint as distinct manifest fields. Derive the homepage's latest-version label, total public-note count, published route-node count, recap-covered node count, and recap endpoint from the actual files; verify them before every GitHub Pages push.
- When a milestone recap is created, state its exact terminal release and node coverage. Later note-only releases must keep that recap byte-identical and label it as the previous milestone instead of silently implying current coverage.

# Figures, computation and resumption

- Before preparing scientific figures, read the figure-archive section of `/Users/kasifa/Documents/Math/.workflow/research-operations.md`. Before launching or changing numerical work, read its compute-resource section as well. These complete requirements are unchanged; pure analytic work need not reload them.
- On resume use `python3 /Users/kasifa/Documents/Math/scripts/ns_workflow_context.py research`. The index is a source locator, not mathematical evidence. Keep proofs, literature verification, independent audits and certificates complete; read original dependencies whenever needed.
- At a natural checkpoint, update `/Users/kasifa/Documents/Math/.workflow/research-current.json` only if the current problem, source pointers or next action changed, and run the same command with `--refresh` after reviewing those fields. Do not update the index per tool call. Never read or maintain the publication index or queue.
