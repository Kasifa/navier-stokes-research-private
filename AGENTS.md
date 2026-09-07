# Forward research role and current rules

- This worktree belongs to `研究任务` (forward regularity), not the reverse task or publisher.
- Current state: PAUSED_BY_USER. The user's latest “先等一下吧” overrides earlier resume instructions. Management maintenance and migration do not resume mathematical research, computation or new research subagents.
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
- Follow the central writing guide rather than mechanical word replacement. Preserve mathematical scope and AI/computer-assistance disclosure. The publisher uses HTML for daily notes and HTML/PDF only for individually approved Frontier Results papers; existing PDFs and scientific vector figures are preserved.

# Publishing target

- Publish this project only through the GitHub repository and its GitHub Pages site at `https://kasifa.github.io/`.
- Do not mirror or deploy the project to another hosting service unless the user explicitly changes this rule.
- A research section counts as research-complete when its analytic proof or explicitly stated negative result, required certificates, independent audit, literature boundary, figure package when scientifically needed, release manifest, and frozen source commit are complete. Reader-facing HTML/PDF, bilingual text, homepage entries, deployment, and online verification are publication-completion conditions owned by the fixed `发布任务`; they are not research-completion conditions.
- Each research direction sends its own frozen `release_id + source commit` once to the fixed `发布任务`. It continues only when the user has authorized research to run; a paused task records the handoff and remains paused. Neither direction polls, waits for, supervises or reports publication.
- Use only the existing task titled `发布任务` for all website and GitHub Pages work. Do not create a task per section, version, repair, or retry. The publisher owns FIFO ordering, retries, deployment waits, online verification, and `/Users/kasifa/Documents/Math/NAVIER_STOKES_PUBLICATION_QUEUE.md`.
- Publish each research-complete section asynchronously through that one FIFO queue. At most one release may be `active`; later releases remain `queued` until the predecessor is online-verified.
- Treat a cumulative recap as a milestone artifact, not a per-section requirement. Update it only after a substantial phase closure, route change, or positive theorem; an ordinary completed section publishes its own note without creating a new recap.
- Keep the latest published-research endpoint and latest recap endpoint as distinct manifest fields. Derive the homepage's latest-version label, total public-note count, published route-node count, recap-covered node count, and recap endpoint from the actual files; verify them before every GitHub Pages push.
- When a milestone recap is created, state its exact terminal release and node coverage. Later note-only releases must keep that recap byte-identical and label it as the previous milestone instead of silently implying current coverage.

# Figures, computation and resumption

- Before preparing scientific figures, read the figure-archive section of `/Users/kasifa/Documents/Math/.workflow/research-operations.md`. Before launching or changing numerical work, read its compute-resource section as well. These complete requirements are unchanged; pure analytic work need not reload them.
- On resume use `python3 /Users/kasifa/Documents/Math/scripts/ns_workflow_context.py research`. The index is a source locator, not mathematical evidence. Keep proofs, literature verification, independent audits and certificates complete; read original dependencies whenever needed.
- At a natural checkpoint, update `/Users/kasifa/Documents/Math/.workflow/research-current.json` only if the current problem, source pointers or next action changed, and run the same command with `--refresh` after reviewing those fields. Do not update the index per tool call. Never read or maintain the publication index or queue.
