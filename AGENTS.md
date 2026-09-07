# Paper-specialist role and current rules

## Current privacy boundary (2026-09-07)

- Public overviews and ordinary website maintenance run in 48-hour batches, with no empty publication. PRIVATE_CORE archival is immediate and independent of that window. Management accepted migration/privacy QA on 2026-09-07; use only the existing publisher heartbeat automation-2, with activation recorded in publication-cadence.json; do not duplicate it. Per-channel FIFO uses one execution lock, and waiting for a public window or CI must not block private archival.

- New complete statements, proofs, constructions, estimates, code, data, parameters, certificates, manuscripts, logs and attachments are PRIVATE_CORE. Only the fixed publisher archives and pushes them to the private source repository. Research completion never authorizes full public readers or source attachments.
- Public output is PUBLIC_PROGRESS_OVERVIEW only: reviewed bilingual high-level object, direction, reliable stage and limitations, without reconstructible core method details. Semantic review is mandatory; scans, hidden links, collapsed UI and JavaScript are not privacy controls.
- The user explicitly retains already-public historical reader files, the two approved papers and previously linked frozen attachments for now. The exact 323b543a historical exception manifest is finite; it never permits exporting the entire old public repository/history or expanding exceptions without specific user approval.
- Transport authority is /Users/kasifa/Documents/Math/.workflow/publication-targets.json and scripts/ns_split_publish.py. The old full-reader publish command is disabled; source/public identity, visibility, independent public objects and allowlists must pass. Do not bypass hooks or use raw API/--no-verify to evade these checks.
- Management accepted migration/privacy QA on 2026-09-07 and now issues the user's conditional joint resume to the two existing research tasks. See /Users/kasifa/Documents/Math/.workflow/management-acceptance-20260907.md. This does not start new paper or strategy work; each role owns its scientific next_action. Any later explicit user pause takes precedence.

- This worktree belongs to the single-paper task `论文修订与补充研究`, ID `01a0747d-db37-7063-b9e0-06466ca89cbf`; it is not another general research line or a publishing task.
- Read `/Users/kasifa/Documents/Math/NAVIER_STOKES_RESEARCH_PUBLISHING_WORKFLOW.md`, `NAVIER_STOKES_TASK_REGISTRY.md`, `NAVIER_STOKES_WRITING_STYLE.md` and `.workflow/paper-current.md` in the Math workspace. Do not run or refresh the forward research index.
- Continue only the user's current paper/editorial scope. A completed manuscript freeze is a research checkpoint, not permission to submit or publicly list another paper. The two previously confirmed papers are retained historical exceptions only; a new revision is not automatically public.
- The fixed publisher owns website editing, deployment and its queue. Do not push, alter remotes, implement migration or supervise routine publication. Preserve v1, frozen sources, audits and historical PDFs.
- Save current editorial inputs and outstanding issues at a safe checkpoint for the conditional migration check. This management request does not resume either paused research direction or authorize new mathematical work.

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
- The research freeze completes the paper stage. Website publication, bilingual reader pages, permitted PDFs and online checks belong to the fixed publisher and do not block research completion.
- Publication requires the user's specific authority and the single FIFO queue; paper preparation, audit success and arXiv formatting do not automatically authorize publication or submission.
- Keep the homepage's latest-version label, total public-note count, route-node counts, and recap endpoint derived from the actual published files; verify them before every GitHub Pages push.
- Recaps are milestone artifacts or explicit user requests, not a mandatory next task after every paper or section; the publisher maintains their coverage accurately.

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
