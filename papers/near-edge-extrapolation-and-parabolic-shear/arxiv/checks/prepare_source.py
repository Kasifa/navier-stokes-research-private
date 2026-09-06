#!/usr/bin/env python3
"""Prepare a self-contained submission copy without editing frozen v2."""
from pathlib import Path
import shutil, json, difflib, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
V2=ROOT.parent/'v2'; V1=ROOT.parent/'v1'; SRC=ROOT/'source'
SRC.mkdir(exist_ok=True)
for name in ('main.tex','references.bib'):
    shutil.copy2(V2/name,SRC/name)
shutil.copytree(V2/'sections',SRC/'sections',dirs_exist_ok=True)
changes={}
def replace(name,old,new):
    p=SRC/name;t=p.read_text()
    if t.count(old)!=1: raise ValueError((name,'replacement count',t.count(old)))
    p.write_text(t.replace(old,new))
    changes.setdefault(name,[]).append({'old':old,'new':new})
replace('main.tex',
'''One explicit sequence of consecutive-integer-frequency shears transfers
the first-kind profile from a single initial datum over the full time
interval. Its signed collar-flux quotient retains an''',
'''An explicit sequence of consecutive-integer-frequency shears transfers
the first-kind profile over the full time interval, using one initial
datum for each member of the sequence. Its signed collar-flux quotient retains an''')
replace('main.tex',r'\paragraph{What is being added.}',r'\paragraph{Main results.}')
replace('main.tex',r'\setlength{\bibsep}{4pt}',r'''\setlength{\bibsep}{4pt}
\interlinepenalty=10000''')
replace('main.tex',
r'\usepackage[colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}',
r'''\usepackage[colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\providecommand{\doi}[1]{\href{https://doi.org/#1}{doi:\nolinkurl{#1}}}''')
replace('main.tex',
'''In the regime $A\\to\\infty$, $\\mu\\to\\infty$, $\\epsilon\\to0$, the''',
'''Here $D=d/dx$. In the regime $A\\to\\infty$, $\\mu\\to\\infty$,
$\\epsilon\\to0$, the''')
replace('sections/upper-bound.tex',
'''The theorem cited here is a preprint result. The longer reconstruction
in the frozen first version followed the same half-line basis argument
with exponent $5\\sqrt2$; it is not an additional contribution and is
omitted here. The required range in this section is only $d\\le1$.''',
'''The theorem cited here is a preprint result and is used as an
attributed input. The required range in this section is only $d\\le1$.''')
replace('sections/upper-bound.tex',r'$\gamma=2/3969$ used in the research notes, the rate is $-2/11907$.',r'$\gamma=2/3969$, the rate is $-2/11907$.')
replace('sections/consequences.tex',
'''The estimates above can be read without the particular exponential
normalization used in the original scale experiment. This section states
the dependence on that normalization explicitly.''',
'''This appendix records the dependence of the estimates on an external
exponential normalization and compares the static and parabolic scales.''')
replace('sections/consequences.tex',
'''a change in the actual flux. The numerical constants come from the cited extrapolation input;
replacing the older $5\\sqrt2$ input by $3\\sqrt2$ enlarges this
sufficient $\\kappa$ threshold by $5/3$. This is a literature substitution,
not a new dynamical conclusion. The spatial witnesses in''',
'''a change in the actual flux. The numerical constants come from the cited
extrapolation input. The spatial witnesses in''')
replace('sections/sharpness.tex',
'''The longer growing-degree slice estimates of the first version are
not needed for the separate dynamic confluence proof used here.\n''','')
replace('sections/literature-context.tex',
'''are verified directly. The source audit records a normalization
inconsistency in Khan's printed operational identity.''',
'''are verified directly.''')
replace('sections/discussion.tex',
'''more general terminating hypergeometric results may exist. Independent
review by a human specialist in asymptotic analysis or approximation
theory remains a sensible step before submission. No such review or
journal endorsement is claimed here.''',
'''more general terminating hypergeometric results may exist. No priority
claim is made beyond the explicit comparisons in
Section~\\ref{sec:literature}.''')
old='''\\paragraph{Version and reproducibility.}
This independent second version retains the historical first version.
The source package contains a Chinese research summary, a response to
the novelty assessment, proof and literature ledgers, reproducible
checks, a scientific-figure inventory, and file hashes. No new reader
PDF is generated. The retained vector scientific figure and its data
are identified as historical assets. This local research revision is
not a journal or arXiv submission and has not been publicly deployed.'''
new=r'''\paragraph{Data and code availability.}
The ancillary files contain exact finite-algebra checks and the code,
parameters, data, and reference SVG for Figure~\ref{fig:edge-diagnostic}.
The file \texttt{anc/README.md} gives the commands and dependencies.
These reproducibility materials complement the proofs; finite checks
and quadrature diagnostics do not certify continuum limits.'''
replace('sections/discussion.tex',old,new)
replace('sections/diagnostic.tex',
'''Figure~\\ref{fig:edge-diagnostic}, retained unchanged from the first version, checks the three constants in the''',
'''Figure~\\ref{fig:edge-diagnostic} illustrates the three constants in the''')
replace('sections/diagnostic.tex','../v1/figures/heat-edge/figure.pdf','figures/heat-edge.pdf')
replace('sections/diagnostic.tex','The letter \\(p\\) in the archived legend','The letter \\(p\\) in the figure legend')
replace('sections/diagnostic.tex','The archived calculation uses deterministic IEEE-754 binary64','The calculation uses deterministic IEEE-754 binary64')
replace('sections/diagnostic.tex',
'''integration interval. The plotting source, parameters, all 16 data
rows, and the numerical comparison report accompany the source
delivery.''',
'''integration interval. The ancillary directory \\texttt{anc/heat-edge/}
contains the plotting source, parameters, and all 16 data rows;
\\texttt{plot.py --check} reproduces the numerical comparison report.''')
replace('sections/diagnostic.tex','This retained figure illustrates the qualitative limits, not the new','This figure illustrates the qualitative limits, not the')
replace('sections/diagnostic.tex','New exact algebra\nchecks are supplied separately; neither is a continuum certificate.','Exact algebra\nchecks are included in \\texttt{anc/checks/}; neither is a continuum certificate.')
# Preserve bibliographic identities and add explicit identifiers that plainnat prints.
replace('references.bib','% Metadata and statement audit: literature/source-audit.md, 2026-09-05.\n% Only entries cited in the completed manuscript are included.\n','% References used in the manuscript.\n')
replace('references.bib','% Primary-source metadata checked 2026-09-06.\n% These are candidate additions, not a mandate to cite every entry.\n','')
replace('references.bib',
'''  doi = {10.1070/SM8670},
  eprint''',
'''  doi = {10.1070/SM8670},
  url = {https://arxiv.org/abs/1602.02315v1},
  note = {Theorem numbers refer to arXiv version 1},
  eprint''')
replace('references.bib','  doi = {10.1007/s11005-025-01946-9}\n',
'''  doi = {10.1007/s11005-025-01946-9},
  note = {Article 60}
''')
replace('references.bib','  pages = {60},\n','')
(SRC/'figures').mkdir(exist_ok=True)
shutil.copy2(V1/'figures/heat-edge/figure.pdf',SRC/'figures/heat-edge.pdf')
anc=SRC/'anc';(anc/'checks').mkdir(parents=True,exist_ok=True);(anc/'heat-edge').mkdir(exist_ok=True)
shutil.copy2(V1/'checks/verify_algebra.py',anc/'checks/verify_algebra.py')
t=(V2/'checks/verify_revision.py').read_text()
old="ROOT = Path(__file__).resolve().parents[1]\nLEGACY = ROOT.parent / 'v1/checks/verify_algebra.py'"
assert t.count(old)==1
t=t.replace(old,"LEGACY = Path(__file__).resolve().with_name('verify_algebra.py')")
(anc/'checks/verify_revision.py').write_text(t)
for name in ('plot.py','config.json','data.csv','figure.svg'):
    shutil.copy2(V1/'figures/heat-edge'/name,anc/'heat-edge'/name)
plot=anc/'heat-edge/plot.py'
pt=plot.read_text()
old_doc='difference.  The separate render.cjs converts the SVG to PDF and 600 dpi PNG.'
assert pt.count(old_doc)==1
plot.write_text(pt.replace(old_doc,"difference. The paper's vector PDF is supplied in figures/heat-edge.pdf."))
# A neutral ASCII metadata version of the same abstract.
main=(SRC/'main.tex').read_text()
abstract=re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',main,re.S).group(1)
abstract=' '.join(abstract.split()).replace("Erd\\'elyi",'Erdelyi')
assert abstract.isascii() and len(abstract)<=1920
metadata={'title':'Heat-evolved Chebyshev edges and localized fluxes of sparse Fourier shears','authors':'C. K. Zeng','affiliation':'Independent Researcher','orcid':'0009-0002-5402-3374','abstract':abstract,'abstract_characters':len(abstract),'primary_category_recommendation':'math.CA','cross_list_recommendation':['math.AP'],'msc_class':'41A60, 41A17, 35K05, 35Q30','comments':'25 pages, 1 figure; ancillary code and data','journal_ref':'','doi':'','report_no':'','license_selection':None,'submission_status':'LOCAL_PREPARATION_ONLY','compiler':'pdflatex','texlive':'2025','main_file':'main.tex'}
(ROOT/'metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
(ROOT/'abstract.txt').write_text(abstract+'\n')
fields=[('Title',metadata['title']),('Authors',metadata['authors']),('Abstract',abstract),('Comments',metadata['comments']),('Primary category (recommended)',metadata['primary_category_recommendation']),('Cross-list (recommended)',', '.join(metadata['cross_list_recommendation'])),('MSC-class',metadata['msc_class']),('Journal-ref',''),('DOI',''),('Report-no','')]
form='\n\n'.join(k+':\n'+v for k,v in fields)+'\n\nSubmission settings (not metadata):\nMain file: main.tex\nProcessor: pdflatex\nTeX Live: 2025\nORCID: '+metadata['orcid']+'\nLicense: to be selected by the author during submission.\nStatus: prepared locally; not uploaded or submitted.\n'
assert form.isascii()
(ROOT/'metadata.txt').write_text(form)
(ROOT/'audits/editorial-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
diff=''.join(''.join(difflib.unified_diff((V2/name).read_text().splitlines(True),(SRC/name).read_text().splitlines(True),fromfile='frozen-v2/'+name,tofile='arxiv/'+name,n=0)) for name in sorted(changes))
(ROOT/'audits/editorial.diff').write_text(diff)
print(json.dumps({'status':'PREPARED','editorially_changed_files':list(changes),'abstract_characters':len(abstract),'frozen_v2_unchanged':True}))
