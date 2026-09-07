# Reverse research ownership and resumption (2026-09-07)

This worktree is owned by the persistent task `研究任务（反向）`.
The current workspace protocol and the user's latest instructions govern this
worktree. Current state: PAUSED_BY_USER after “先暂停一下”. Do not resume research,
computations or scientific subagents until the user explicitly resumes this task.

- Scientific work and all git commands run only in `/Users/kasifa/Documents/Math/navier-stokes-reverse`, branch `codex/ns-reverse`.
- Read `/Users/kasifa/Documents/Math/NAVIER_STOKES_RESEARCH_PUBLISHING_WORKFLOW.md` and `/Users/kasifa/Documents/Math/NAVIER_STOKES_DUAL_TRACK_STRATEGY_2026-09-07.md` when first needed or changed.
- Resume from this tree's `.workflow/reverse-current.json` and its reverse-owned checkpoint. Do not use or refresh the forward `research` helper/index; do not alter forward checkpoints or the publication queue.
- After explicit resumption, new scientific outputs belong in `research/reverse/`. This task has its own user pause, separate from the forward task; preserve both tasks' historical files.
- Target: fixed positive viscosity, unforced fixed three-dimensional torus, one fixed smooth real divergence-free initial datum. A finite two-step mechanism is not singularity, uniform iteration, or a fixed-datum infinite cascade.
- Freeze completed bounded research as `ReverseNS-...`, including proof boundaries, sources, certificates, independent review, hashes, and figure inventory. Hand off each release and frozen source commit once to existing publication task `01a06480-0532-7fd0-bdf0-57571465a2d4`. Continue only while research is authorized; otherwise save the record and remain paused. Never monitor publication.
- Do not edit site/reader pages, deploy, push, alter remotes or visibility, or create publication tasks. Research completion is the research freeze, independent of website publication. Migration is conditional on verified quiescence and does not resume this task. Follow the central task registry and writing guide.

# Published writing style

These rules apply to reader-facing text in `public/`, page metadata, research notes, and downloadable versions.

- Write as one individual researcher. Use first-person singular (`我`) for choices, plans, progress, and uncertainty. Use a neutral voice for established mathematics.
- Keep sentences plain, short, and specific. Prefer “我目前在检查……” to slogans about a “main attack”, “breakthrough”, or “research program”.
- Avoid collective or AI-like language such as `我们`, `攻关`, `主攻`, `研究纪律`, `三重审计`, `杀死错误想法`, and unsupported claims of importance or certainty.
- State what was calculated, what is known from the literature, what remains open, and what has not been checked. Do not imply novelty or a proof unless the evidence supports it.
- Separate published results, conditional results, preprints, calculations, conjectures, and failed attempts. Link primary sources where practical.
- Keep technical notation precise. Plain language should simplify the prose, not weaken the mathematical statement.
- Follow `/Users/kasifa/Documents/Math/NAVIER_STOKES_WRITING_STYLE.md`; preserve mathematical scope and AI/computer-assistance disclosure. The publisher uses HTML for daily notes and HTML/PDF for individually approved Frontier Results papers; preserve historical PDFs and scientific figure archives.

# Publishing target

- Publish this project only through the GitHub repository and its GitHub Pages site at `https://kasifa.github.io/`.
- Do not mirror or deploy the project to another hosting service unless the user explicitly changes this rule.
- A research section is complete when its result, required certificates, independent review, literature boundary, necessary figure archive, manifest and source freeze are complete. Website publication is a separate responsibility and is never a research-completion condition.
- Only the fixed publisher receives the once-only frozen handoff and manages publication FIFO. Research tasks do not publish or wait for publication. The current user pause remains in force.
- Treat a cumulative recap as a milestone artifact, not a per-section requirement. Update it only after a substantial phase closure, route change, or positive theorem; an ordinary completed section publishes its own note without creating a new recap.
- Keep the latest published-research endpoint and latest recap endpoint as distinct manifest fields. Derive the homepage's latest-version label, total public-note count, published route-node count, recap-covered node count, and recap endpoint from the actual files; verify them before every GitHub Pages push.
- When a milestone recap is created, state its exact terminal release and node coverage. Later note-only releases must keep that recap byte-identical and label it as the previous milestone instead of silently implying current coverage.

# Simulation and figure archive

- Treat every numerical experiment used in a public claim as a reproducible research asset. Preserve the command, configuration, random seed, environment, git commit, raw or losslessly processed data, and checksums.
- Store paper-ready figure packages under `figures/<study>/<figure-id>/`. Each package must contain the plotting source, source data or a stable data reference, `manifest.json`, `caption.md`, and the exported figure.
- Export formal figures as vector PDF and SVG plus a 600 dpi PNG. Use 85 mm for a single-column figure and 178 mm for a double-column figure unless a journal template requires something else.
- Use neutral titles, explicit units, honest scales, restrained colors, and non-color distinctions. Inspect at final print size and in grayscale. Do not use screenshots as the archival figure when a vector or data-driven export is possible.
- Keep exploratory plots separate from formal figures. A plot becomes a formal figure only after its data, caption, manifest, and visual QA are complete.
- Website figures may be compressed copies, but they must link back to the same archived data and plotting source used for the paper-ready export.

# Compute resources

- Perform ordinary translation directly on the local workstation.  Do not
  route routine translation through DGX; reserve DGX for genuinely
  compute-intensive numerical simulation unless the user explicitly asks for
  a different translation workflow.
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
