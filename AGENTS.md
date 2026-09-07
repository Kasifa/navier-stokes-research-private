# Paper-source role and current rules

## Current privacy boundary (2026-09-07)

- Public overviews and ordinary website maintenance run in 48-hour batches, with no empty publication. PRIVATE_CORE archival is immediate and independent of that window. Management accepted migration/privacy QA on 2026-09-07; use only the existing publisher heartbeat automation-2, with activation recorded in publication-cadence.json; do not duplicate it. Per-channel FIFO uses one execution lock, and waiting for a public window or CI must not block private archival.

- New complete statements, proofs, constructions, estimates, code, data, parameters, certificates, manuscripts, logs and attachments are PRIVATE_CORE. Only the fixed publisher archives and pushes them to the private source repository. Research completion never authorizes full public readers or source attachments.
- Public output is PUBLIC_PROGRESS_OVERVIEW only: reviewed bilingual high-level object, direction, reliable stage and limitations, without reconstructible core method details. Semantic review is mandatory; scans, hidden links, collapsed UI and JavaScript are not privacy controls.
- The user explicitly retains already-public historical reader files, the two approved papers and previously linked frozen attachments for now. The exact 323b543a historical exception manifest is finite; it never permits exporting the entire old public repository/history or expanding exceptions without specific user approval.
- Transport authority is /Users/kasifa/Documents/Math/.workflow/publication-targets.json and scripts/ns_split_publish.py. The old full-reader publish command is disabled; source/public identity, visibility, independent public objects and allowlists must pass. Do not bypass hooks or use raw API/--no-verify to evade these checks.
- Management accepted migration/privacy QA on 2026-09-07 and now issues the user's conditional joint resume to the two existing research tasks. See /Users/kasifa/Documents/Math/.workflow/management-acceptance-20260907.md. This does not start new paper or strategy work; each role owns its scientific next_action. Any later explicit user pause takes precedence.

- This worktree preserves paper sources and historical preparations used by the current paper specialist. It is not an additional general research or publication task.
- Follow `/Users/kasifa/Documents/Math/NAVIER_STOKES_RESEARCH_PUBLISHING_WORKFLOW.md`, `NAVIER_STOKES_TASK_REGISTRY.md`, `NAVIER_STOKES_WRITING_STYLE.md` and the Math `.workflow/paper-current.md`. Do not use or refresh the forward research index.
- Preserve frozen manuscripts, v1 directories, evidence and untracked drafts. Do not stage unrelated manuscripts merely to obtain a clean worktree. Only the exact two historical paper versions are retained public exceptions; other drafts and revisions remain private.
- The fixed publisher alone edits the website and deploys. Do not push, modify remotes or migrate this worktree. Management maintenance does not resume paused research or initiate new paper work.

# Published writing style

These rules apply to reader-facing text in `public/`, page metadata, research notes, and downloadable versions.

- Write as one individual researcher. Use first-person singular (`我`) for choices, plans, progress, and uncertainty. Use a neutral voice for established mathematics.
- Keep sentences plain, short, and specific. Prefer “我目前在检查……” to slogans about a “main attack”, “breakthrough”, or “research program”.
- Avoid collective or AI-like language such as `我们`, `攻关`, `主攻`, `研究纪律`, `三重审计`, `杀死错误想法`, and unsupported claims of importance or certainty.
- State what was calculated, what is known from the literature, what remains open, and what has not been checked. Do not imply novelty or a proof unless the evidence supports it.
- Separate published results, conditional results, preprints, calculations, conjectures, and failed attempts. Link primary sources where practical.
- Keep technical notation precise. Plain language should simplify the prose, not weaken the mathematical statement.
- Follow the central writing guide and preserve AI disclosure. Do not silently rewrite historical frozen papers; new paper versions remain private by default.

# Publishing target

- The publisher stores PRIVATE_CORE in the private source repository; only reviewed PUBLIC_PROGRESS_OVERVIEW content and fixed historical exceptions reach the independent public site at `https://kasifa.github.io/`.
- Do not mirror or deploy the project to another hosting service unless the user explicitly changes this rule.
- A research release is research-complete when its analytic result, certificates, independent audit, literature boundary, required figure package, release manifest, and frozen source commit are complete. Reader-facing HTML/PDF, bilingual text, homepage entries, deployment, and online verification are publication-completion conditions owned by the fixed `发布任务`; they do not block later research.
- Each authorized research direction hands off its own frozen release once. The paper specialist follows its recorded paper handoff, with no duplicate delivery. Paused research stays paused; no paper task polls or supervises routine publication.
- Use only the existing task titled `发布任务` for all website and GitHub Pages work. Do not create a task per section, version, repair, or retry. The publisher owns the FIFO queue at `/Users/kasifa/Documents/Math/NAVIER_STOKES_PUBLICATION_QUEUE.md`, deployment waits, retries, and online verification.
- Keep the homepage's latest-version label, total public-note count, route-node counts, and recap endpoint derived from the actual published files; verify them before every GitHub Pages push.
- Recaps occur at real milestones or on explicit user request; they are not automatically required after every completed section.

# Simulation and figure archive

- Treat every numerical experiment used in a public claim as a reproducible research asset. Preserve the command, configuration, random seed, environment, git commit, raw or losslessly processed data, and checksums.
- Store paper-ready figure packages under `figures/<study>/<figure-id>/`. Each package must contain the plotting source, source data or a stable data reference, `manifest.json`, `caption.md`, and the exported figure.
- Export formal figures as vector PDF and SVG plus a 600 dpi PNG. Use 85 mm for a single-column figure and 178 mm for a double-column figure unless a journal template requires something else.
- Use neutral titles, explicit units, honest scales, restrained colors, and non-color distinctions. Inspect at final print size and in grayscale. Do not use screenshots as the archival figure when a vector or data-driven export is possible.
- Keep exploratory plots separate from formal figures. A plot becomes a formal figure only after its data, caption, manifest, and visual QA are complete.
- Complete figure/data/code provenance remains in the private archive. Future public progress summaries must not export scientific figures, source data or plotting code without a separate explicit historical-exception approval.

# Compute resources

- Local numerical work may use the workstation's available CPU cores, memory, and GPU aggressively. Keep the interactive desktop responsive, but do not default to single-core execution for independent simulations or parameter sweeps.
- Record hardware, thread/process counts, precision, solver tolerances, and wall time in each experiment manifest.
- Long simulations must expose progress rather than run as a silent process. Preserve a timestamped solver log and a resource log, report meaningful stage/step/residual/CFL/checkpoint/ETA information to the user, and record failures or restarts instead of overwriting them.
- The user grants full use of the DGX Spark and the `zck` account for suitable numerical workloads. Optimize for measured time-to-solution and throughput rather than conservative utilization; state the expected runtime, storage, software, and data/code transfer plan before each substantial run.
- In this local checkout, read `.codex/dgx.local.md` for the DGX endpoint when that ignored file exists. Never commit machine credentials or copy the password into scripts, logs, manifests, or shell history.
- Before launching a DGX job, inspect current GPU processes, memory, disk space, and load. The user has authorized simulation jobs to use the full available GPU and memory and up to 90% of the logical CPUs by default. Project-owned processes may be paused, restarted, or replaced when that improves throughput, after preserving recoverable state; do not terminate system services or another user's processes.
- Compute the DGX CPU worker limit as `max(1, floor(0.9 * nproc))`; on the verified 20-core host this is 18 workers, leaving 2 logical CPUs for the operating system and administration. Apply the same total limit across nested multiprocessing, OpenMP, BLAS, data loaders, and containers to avoid oversubscription.
- Do not impose an artificial GPU or memory percentage cap. Use all resources the run can benefit from, while sizing allocations from the current preflight state, avoiding deliberate OOM or swap thrashing, and checkpointing before memory-heavy phases.
- Choose execution mode from evidence: benchmark representative steps when useful, then select containers or native binaries, precision, batch size, compilation, CPU/GPU decomposition, asynchronous I/O, and concurrency for the best end-to-end efficiency. Preserve a deterministic validation path when using mixed precision or approximate kernels.
- Prefer a pinned GPU container over changing the DGX host Python environment. Record the image tag and digest with the run.
- Store each remote run under `~/dgx-jobs/<project>/runs/<run-id>/` with separate `config/`, `logs/`, `checkpoints/`, and `results/` directories. A run ID must be unique and stable across restarts.
- Long DGX jobs must write periodic, versioned checkpoints. Write each checkpoint to a temporary path, validate it, then atomically rename it into place. On restart, load the newest valid checkpoint and append to the existing log rather than overwriting it.
- Use a detached session or container for offline work, but keep the PID/container ID, launch command, source commit, input checksums, random seeds, and resume command in the run manifest.
