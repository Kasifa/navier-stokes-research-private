# Fixed publication role and current rules

- This is the current source checkout used by the fixed `发布任务`, ID `01a06480-0532-7fd0-bdf0-57571465a2d4`. It shares a Git common directory with scientific worktrees; it is not yet the isolated public-artifact repository.
- Follow `/Users/kasifa/Documents/Math/NAVIER_STOKES_RESEARCH_PUBLISHING_WORKFLOW.md`, `NAVIER_STOKES_TASK_REGISTRY.md` and `NAVIER_STOKES_WRITING_STYLE.md`. Two research directions exist and are currently paused; publication does not resume them.
- The private-research/public-artifact migration is conditionally approved, not yet cleared to run. Do not change repository visibility, name, remotes or hosting until management has recorded verified stage checkpoints and quiescence. After clearance, execute the existing migration plan with independent public Git history and an approved artifact list.
- Only this fixed task edits website content, the FIFO queue and deployment. Management may maintain role and writing rules; scientific tasks provide frozen sources and bounded editorial input without duplicate publication supervision.

# Published writing style

These rules apply to reader-facing text in `public/`, page metadata, research notes, and downloadable versions.

- Write as one individual researcher. Use first-person singular (`我`) for choices, plans, progress, and uncertainty. Use a neutral voice for established mathematics.
- Keep sentences plain, short, and specific. Prefer “我目前在检查……” to slogans about a “main attack”, “breakthrough”, or “research program”.
- Avoid collective or AI-like language such as `我们`, `攻关`, `主攻`, `研究纪律`, `三重审计`, `杀死错误想法`, and unsupported claims of importance or certainty.
- State what was calculated, what is known from the literature, what remains open, and what has not been checked. Do not imply novelty or a proof unless the evidence supports it.
- Separate published results, conditional results, preprints, calculations, conjectures, and failed attempts. Link primary sources where practical.
- Keep technical notation precise. Plain language should simplify the prose, not weaken the mathematical statement.
- Before publishing, follow the central writing guide and read the actual prose in both languages. Daily reader notes use HTML only; individually approved Frontier Results papers use HTML and PDF. Preserve historical frozen PDFs. If a paper is explicitly revised, issue a traceable new version instead of silently overwriting old HTML/PDF/source evidence.

# Publishing target

- Publish this project only through the GitHub repository and its GitHub Pages site at `https://kasifa.github.io/`.
- Do not mirror or deploy the project to another hosting service unless the user explicitly changes this rule.
- A research section is complete when its result, required certificates, independent audit, literature boundary, necessary figure package, manifest and source freeze are complete. Reader pages, approved PDFs, homepage entries, deployment and online checks are separate publication conditions.
- Each of the two research tasks sends its frozen `release_id + source commit` once. It continues only if research is authorized to run; paused tasks remain paused. Neither research task waits for or monitors publication.
- Use only the existing task titled `发布任务` for all website and GitHub Pages work. Do not create a task per section, version, repair, or retry. The publisher owns FIFO ordering, retries, deployment waits, online verification, and `/Users/kasifa/Documents/Math/NAVIER_STOKES_PUBLICATION_QUEUE.md`.
- Process authorized frozen research handoffs and explicitly approved maintenance through one FIFO queue, with at most one active release. Frontier Results inclusion requires the user's per-paper confirmation; research completion or arXiv preparation alone does not authorize it.
- For a compact read-only resume check, run `python3 /Users/kasifa/Documents/Math/scripts/ns_workflow_context.py publication`. At a natural checkpoint review and update the actual release, source pointers, status, outstanding items and next action first; only then use `--refresh` to bind hashes. Hash refresh alone is not review or verification.
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
