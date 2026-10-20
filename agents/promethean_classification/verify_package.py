#!/usr/bin/env python3
"""Standard-library contract and package checks; not an LLM runtime or truth test."""
from pathlib import Path
import json, subprocess, sys
A=Path(__file__).resolve().parent
R=A.parents[1]
def load(p): return json.loads(p.read_text())
def contract(value,schema,path='$'):
 t=schema.get('type')
 types={'object':dict,'array':list,'string':str}
 if t in types: assert isinstance(value,types[t]),f'{path}: expected {t}'
 if t=='object':
  for k in schema.get('required',[]): assert k in value,f'{path}: missing {k}'
  if schema.get('additionalProperties') is False: assert not (set(value)-set(schema.get('properties',{}))),f'{path}: extra field'
  for k,v in value.items():
   if k in schema.get('properties',{}):contract(v,schema['properties'][k],path+'.'+k)
 if t=='array':
  for i,v in enumerate(value):contract(v,schema['items'],f'{path}[{i}]')
# All validation keywords in these frozen schemas are handled here; $schema/title are metadata.
def supported(s):
 assert not set(s)-{'$schema','title','type','required','properties','items','additionalProperties'},'Unknown schema keyword'
 for v in s.get('properties',{}).values():supported(v)
 if 'items' in s:supported(s['items'])
checks=[]
for kind in ['input','output']:supported(load(R/f'core/{kind}_schema.json'))
checks.append('PASS frozen schema keyword coverage for this bounded validator')
outs={}
for p in sorted((A/'cases').glob('*.json')):
 contract(load(p),load(R/'core/input_schema.json'))
 o=load(A/'responses'/f'{p.stem}_response.json');contract(o,load(R/'core/output_schema.json'));outs[p.stem]=o
 assert o['agent']==load(A/'agent_metadata.json')
 checks.append(f'PASS {p.stem}: full frozen input/output contract and version')
criteria=['order of magnitude','widespread impact','paradigm shift','catalytic effect','democratizing effect','irreversibility']
gates=['system:','barrier statement:','suppression test:','tiers:','prospective','critical mass']
def missing(o):
 s=o['general_et_finding'].lower();return [x for x in criteria+gates if x not in s]
prior=load(A/'records/v1_before_course_verification/responses/primary_response.json')
assert missing(prior),'Expected preserved v1 framework-completeness failure'
checks.append('EXPECTED FAILURE preserved v1: missing '+', '.join(missing(prior)))
for k in ['primary','contrast_1','contrast_2','hype']:assert not missing(outs[k]),(k,missing(outs[k]))
checks.append('PASS v1.1: course gates and all six named criteria present in four general findings; manual semantic review still required')
assert len({outs[k]['general_et_finding'] for k in ['primary','contrast_1','contrast_2','hype']})==1
assert len({outs[k]['recommendation_management_implication'] for k in ['primary','contrast_1','contrast_2']})==3
checks.append('PASS general finding invariant; three context-specific recommendations differ')
p,c=load(A/'cases/primary.json'),load(A/'cases/contrast_2.json')
assert {k for k in p if p[k]!=c[k]}=={'adoption_posture'}
assert outs['insufficient']['evidence']==[] and 'abstain' in outs['insufficient']['general_et_finding'].lower()
assert 'funding' in ' '.join(outs['hype']['contrary_evidence_or_limitations']).lower()
assert 'defer' in outs['contrast_1']['recommendation_management_implication'].lower()
checks.append('PASS posture-only control, insufficient-evidence abstention, hype rejection and hospital deferral')
for p in sorted((A/'cases').glob('*.json')):
 subprocess.run([sys.executable,str(R/'tools/build_prompt.py'),'--agent',str(A),'--case',str(p)],check=True,capture_output=True)
 packet=(R/'work'/f'promethean_classification_{p.stem}_prompt.txt').read_text()
 assert (A/'specialist_instructions.md').read_text() in packet
 assert json.dumps(load(p),indent=2) in packet
 subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(A/'responses'/f'{p.stem}_response.json')],check=True,capture_output=True)
checks.append('PASS five regenerated packets include current instructions and exact cases; five common validators pass')
core=subprocess.run([sys.executable,str(R/'tools/check_frozen_core.py')],check=True,capture_output=True,text=True).stdout.strip()
checks.append(core)
print('\n'.join(checks))
