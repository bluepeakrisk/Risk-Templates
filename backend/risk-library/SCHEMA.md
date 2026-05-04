# Risk Library Schema

## Universal fields (same for all industries)
- id              : R-001 to R-032
- domain          : one of 13 categories
- theme           : universal risk title (e.g. "Cyber attack / security breach")
- treatment       : default strategy (Avoid / Reduce / Transfer / Accept)
- impact_category : primary impact category (one of 7)

## Industry-tailored fields (7 archetypes × 32 themes = 224 variants)
- title           : industry-specific risk title
- description     : 1-2 sentences describing the risk in industry context
- causes_people   : 1-3 bullets
- causes_process  : 1-3 bullets
- causes_systems  : 1-3 bullets
- causes_external : 1-3 bullets
- consequence     : 1-2 sentences on industry-specific impact
- inh_likelihood  : 1-5
- inh_impact      : 1-5
- impact_rationale: which 7-category impact drives the score
- owner_suggested : suggested role title

## Industry archetypes (7)
1. PROF - Professional Services
2. FINS - Financial Services
3. TECH - Technology / SaaS
4. HCAR - Healthcare
5. RETL - Retail / Hospitality
6. INDU - Industrial / Physical
7. PUBL - Public / NFP
