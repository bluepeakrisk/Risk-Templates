"""Guidance Batch 4 — R-028 to R-040 (Project & Change, Third Party, Customer, Geo, Financial Crime, BCM, Conduct, Reporting, Data, Model)."""
from risk_controls import G

GUIDANCE_4 = {

"R-028": {
    "PROF": G(
        data="Programme RAG status; benefits realisation; partner/staff engagement on changes; matter impact during transformation.",
        systems="Project management; benefits tracking; financial planning.",
        stakeholders="Managing Partner; programme sponsors; Practice Group Leaders; staff; clients.",
        key_factors="Partnership decision-making; matter delivery during change; partner engagement; benefits realisation discipline."),
    "FINS": G(
        data="Programme RAG; benefits realisation; regulator commitments; customer impact assessment.",
        systems="Programme management; regulator commitment tracking; benefits framework.",
        stakeholders="ExCo; programme sponsors; CRO; APRA/PRA; customers.",
        key_factors="Multi-year programme complexity; regulator-driven changes; risk during change; benefits realisation discipline."),
    "TECH": G(
        data="OKR delivery; programme RAG; engineering capacity; release-related incidents.",
        systems="Engineering planning; programme management; observability; release management.",
        stakeholders="CTO; CPO; engineering leadership; PM/SM community; investors.",
        key_factors="Pace of change; release discipline; engineering capacity; technical debt during transformation."),
    "HCAR": G(
        data="Programme RAG; clinical engagement; patient impact during change; benefits achievement.",
        systems="Programme management; clinical change tracking; patient experience.",
        stakeholders="CMO; programme sponsors; clinicians; patients; ministerial.",
        key_factors="Clinical engagement; patient safety during change; programme size; ministerial visibility."),
    "RETL": G(
        data="Programme RAG; trading impact; supplier readiness; customer experience during change.",
        systems="Programme management; trading systems; supplier portal; customer experience.",
        stakeholders="COO; Commercial Director; suppliers; customers.",
        key_factors="Trading-period change discipline; supplier coordination; customer experience continuity."),
    "INDU": G(
        data="Project RAG; cost / schedule variance; safety during change; commissioning readiness.",
        systems="Project controls; cost management; HSE management.",
        stakeholders="Chief Projects Officer; HSE; Operations; partners; community.",
        key_factors="Project complexity; safety during change; commissioning discipline; community engagement."),
    "PUBL": G(
        data="Programme RAG; ministerial commitment progress; community engagement; outcomes during change.",
        systems="Programme management; ministerial reporting; community engagement.",
        stakeholders="CEO; programme sponsors; ministerial; community; staff.",
        key_factors="Ministerial sponsorship; community engagement; service continuity; outcomes-focused implementation."),
},

"R-029": {
    "PROF": G(
        data="Critical supplier inventory; performance against SLAs; supplier risk assessments.",
        systems="Vendor management; SLA monitoring; risk register.",
        stakeholders="CIO; Vendor Manager; partners using critical suppliers.",
        key_factors="Critical SaaS dependency; supplier financial health; substitutability; partner-level supplier choices."),
    "FINS": G(
        data="Critical service provider register; CPS 230 / DORA readiness; concentration risk; supplier performance.",
        systems="TPRM platform; CPS 230 register; risk management.",
        stakeholders="COO; Resilience Lead; CRO; APRA / DORA NCA; critical suppliers.",
        key_factors="Critical service provider concentration; CPS 230 / DORA scope; substitutability; resilience exit plans."),
    "TECH": G(
        data="Critical SaaS dependency mapping; SLA achievement; alternative readiness.",
        systems="TPRM; observability; integration platform.",
        stakeholders="CTO; SRE; procurement; critical SaaS providers.",
        key_factors="SaaS concentration; integration depth; alternatives availability; cloud provider concentration."),
    "HCAR": G(
        data="Clinical supplier reliability; pharmaceutical supply; equipment vendor performance.",
        systems="Supply chain; pharmaceutical management; biomedical engineering.",
        stakeholders="Supply Chain Director; Director of Pharmacy; Biomedical; clinical leaders.",
        key_factors="Supply chain criticality; pharmaceutical supply continuity; equipment vendor reliability; substitutability."),
    "RETL": G(
        data="Supplier concentration; supplier performance; supply chain visibility.",
        systems="Supply chain platform; supplier portal; risk register.",
        stakeholders="Chief Supply Chain Officer; Buying Director; suppliers; logistics partners.",
        key_factors="Supplier concentration; geographic concentration; alternative sourcing; supply chain visibility tier."),
    "INDU": G(
        data="Critical input supplier inventory; OEM / equipment vendor performance; logistics partner reliability.",
        systems="Supply chain; vendor management; logistics tracking.",
        stakeholders="CPO; Operations; OEM partners; logistics partners.",
        key_factors="Critical input supplier concentration; OEM dependency; logistics continuity; commodity availability."),
    "PUBL": G(
        data="Service provider performance; community partner reliability; SaaS dependency.",
        systems="Vendor management; partner portal; service tracking.",
        stakeholders="Partnerships Lead; Service Delivery; community partners; SaaS providers.",
        key_factors="Service delivery partner concentration; community partner sustainability; SaaS dependency."),
},

"R-030": {
    "PROF": G(
        data="Outsourcing arrangements; service quality; conduct / compliance issues.",
        systems="Outsourcing register; service performance; conduct surveillance.",
        stakeholders="COO; CCO; outsourcing partners; clients.",
        key_factors="Outsourced scope; quality control; conduct exposure; client-facing impact."),
    "FINS": G(
        data="Material outsourcing register; CPS 231/230 compliance; service performance; sub-contractor risk.",
        systems="TPRM; outsourcing register; service monitoring.",
        stakeholders="COO; CRO; APRA/PRA; outsourcing providers; sub-contractors.",
        key_factors="Material outsourcing scope; offshoring exposure; sub-contractor visibility; regulator approval / notification."),
    "TECH": G(
        data="Outsourced engineering / support performance; offshore quality; security / conduct.",
        systems="Outsourcing platform; engineering tooling; security.",
        stakeholders="VP Engineering; Operations; outsourcing partners; customers.",
        key_factors="Outsourced engineering scope; offshore quality; security / IP exposure; customer-facing impact."),
    "HCAR": G(
        data="Outsourced clinical / non-clinical service performance; locum agency quality.",
        systems="Outsourcing register; service performance; clinical quality.",
        stakeholders="COO; CMO; outsourcing partners; locum agencies; clinical leaders.",
        key_factors="Clinical outsourcing scope; locum agency quality; non-clinical outsourced service quality."),
    "RETL": G(
        data="3PL performance; manufacturing partner quality; outsourced customer service.",
        systems="3PL platform; supplier quality; customer service.",
        stakeholders="Supply Chain; Customer Service; manufacturing partners.",
        key_factors="3PL dependency; outsourced manufacturing quality; customer service offshoring."),
    "INDU": G(
        data="Contractor performance; subcontractor management; outsourced operations.",
        systems="Contractor management; project controls; performance monitoring.",
        stakeholders="Operations; Project Director; contractors; subcontractors.",
        key_factors="Contractor scope and concentration; subcontractor visibility; safety / quality during outsourcing."),
    "PUBL": G(
        data="Outsourced service delivery quality; partner organisation performance.",
        systems="Outsourcing register; service performance; partner quality.",
        stakeholders="Service Delivery; partner organisations; ministerial.",
        key_factors="Outsourced service scope; partner performance; ministerial accountability for outsourced services."),
},

"R-031": {
    "PROF": G(
        data="Client retention; matter pipeline; partner-client coverage; complaint patterns.",
        systems="CRM; matter management; relationship review platform.",
        stakeholders="Managing Partner; relationship partners; clients; talent (associated with departing clients).",
        key_factors="Client portability; partner movement; matter handover discipline; client communication."),
    "FINS": G(
        data="Customer attrition; switching reasons; remediation impact; complaint patterns.",
        systems="CRM; complaint management; remediation tracking; analytics.",
        stakeholders="Chief Customer Officer; product owners; affected customers; regulator.",
        key_factors="Switching ease; remediation event impact; product / pricing competitiveness; root cause closure."),
    "TECH": G(
        data="Logo retention; expansion / contraction; customer health distribution; root cause of churn.",
        systems="Customer success; product analytics; CRM.",
        stakeholders="Chief Customer Officer; CRO; product; customers (departure interviews).",
        key_factors="Customer outcome focus; switching cost; competitor activity; product roadmap delivery."),
    "HCAR": G(
        data="Patient / referrer attrition; reasons; sentiment; clinical outcomes correlation.",
        systems="Patient management; referrer CRM; experience platform.",
        stakeholders="CMO; Business Development; patients; referrers; community.",
        key_factors="Clinical outcomes; patient experience; referrer relationship; alternative provider availability."),
    "RETL": G(
        data="Customer attrition; loyalty engagement; trading partner JBP outcomes.",
        systems="Loyalty; CRM; CDP; trading partner systems.",
        stakeholders="Chief Customer Officer; Commercial Director; customers; trading partners.",
        key_factors="Loyalty programme strength; brand equity; trading partner relationship; competitive offer."),
    "INDU": G(
        data="Customer retention on long-term contracts; tender win/loss; reference customer feedback.",
        systems="CRM; contract management; tender pipeline.",
        stakeholders="Commercial Director; major customers; competitors; references.",
        key_factors="Contract length / renewal; reference customer health; competitive positioning; performance reputation."),
    "PUBL": G(
        data="Funder retention; community trust; partner organisation continuity.",
        systems="Grants management; community engagement; partnership tracking.",
        stakeholders="CEO; CFO; funders; community; partner organisations.",
        key_factors="Funder relationship strength; outcomes evidence; community trust capital; political environment."),
},

"R-032": {
    "PROF": G(
        data="Client industry exposure; geographic exposure; macroeconomic indicators; FX exposure.",
        systems="Financial planning; CRM; treasury management.",
        stakeholders="CFO; Practice Group Leaders; Treasurer; major clients.",
        key_factors="Sector / geographic concentration; macro-sensitive practice mix; FX exposure; cost flexibility."),
    "FINS": G(
        data="Macro indicators; portfolio sensitivity; geopolitical exposure; sanctions / capital flow risk.",
        systems="Risk management; portfolio analytics; treasury; regulatory tracking.",
        stakeholders="CRO; CFO; Treasurer; APRA/PRA; major counterparties.",
        key_factors="Portfolio macro sensitivity; geopolitical exposure; sanctions environment; capital flow restrictions."),
    "TECH": G(
        data="ARR by geography / segment; macro sentiment in customer base; FX exposure; regulatory developments by region.",
        systems="Financial planning; CRM; treasury; regulatory tracker.",
        stakeholders="CFO; CRO; Treasurer; investors; customers (CFO sentiment).",
        key_factors="Customer macro sensitivity; geographic concentration; FX exposure; export control / sanctions exposure."),
    "HCAR": G(
        data="Funder financial position; political environment; sector reform; capital cost.",
        systems="Financial planning; funder reporting; treasury.",
        stakeholders="CFO; CEO; funders; ministerial; banks.",
        key_factors="Funder fiscal position; political support; sector reform direction; capital cost trajectory."),
    "RETL": G(
        data="Consumer sentiment; cost of living indicators; FX / commodity exposure; trade policy.",
        systems="Financial planning; demand forecasting; treasury.",
        stakeholders="CFO; Chief Commercial Officer; Treasurer; major suppliers.",
        key_factors="Consumer macro sensitivity; FX / commodity exposure; trade policy; pricing flexibility."),
    "INDU": G(
        data="Commodity prices; demand forecasts; trade policy; sanctions environment; capital flow.",
        systems="Commodity hedging; demand forecasting; treasury; trade compliance.",
        stakeholders="CEO; Commercial Director; Treasurer; major customers; commodity hedging counterparties.",
        key_factors="Commodity cycle position; trade policy direction; sanctions exposure; capital flow restrictions."),
    "PUBL": G(
        data="Government fiscal position; election outlook; sector reform direction; international aid budget.",
        systems="Financial planning; political tracking; sector intelligence.",
        stakeholders="CEO; CFO; ministerial; sector regulator; international funders.",
        key_factors="Fiscal environment; political direction; sector reform pace; international development environment."),
},

"R-033": {
    "PROF": G(
        data="CDD completion; SMR volume; designated services coverage; matter risk assessments.",
        systems="AML platform; matter management; trust account; sanctions screening.",
        stakeholders="MLRO; Compliance Partner; AUSTRAC; partners; clients.",
        key_factors="Tranche 2 readiness; designated service complexity; trust account ML/TF risk; partner-level CDD discipline."),
    "FINS": G(
        data="CDD completion; transaction monitoring alerts; SMR / SAR filings; sanctions screening; correspondent banking risk.",
        systems="AML platform; transaction monitoring; sanctions screening; CDD/KYC.",
        stakeholders="MLRO; CCO; AUSTRAC/FCA/FinCEN; correspondent banks.",
        key_factors="Customer/product/geographic risk profile; correspondent banking exposure; transaction monitoring effectiveness; sanctions regime complexity."),
    "TECH": G(
        data="Onboarding KYC/KYB; risk scoring distribution; pattern detection; chain analytics.",
        systems="Onboarding platform; risk scoring; transaction monitoring; chain analytics.",
        stakeholders="Trust & Safety / Compliance; AUSTRAC; payment partners.",
        key_factors="Platform user/merchant risk; payment rail exposure; emerging typology coverage."),
    "HCAR": G(
        data="High-value supplier screening; patient billing pattern monitoring; cash transaction patterns.",
        systems="Supplier portal; revenue cycle; financial systems.",
        stakeholders="Procurement; Compliance; CFO.",
        key_factors="High-value supplier exposure; private patient cash payment patterns; international supplier risk."),
    "RETL": G(
        data="TTR filings; structuring detection; gift card sales patterns; high-value goods.",
        systems="POS; loyalty; gift card platform; finance system.",
        stakeholders="Finance; Loss Prevention; Compliance; AUSTRAC.",
        key_factors="Cash transaction volume; gift card / high-value goods exposure; structuring patterns."),
    "INDU": G(
        data="Trade compliance; sanctions screening; counterparty DD; export licence management.",
        systems="Trade compliance; sanctions screening; ERP; project finance.",
        stakeholders="Trade Compliance; GC; Risk; major counterparties.",
        key_factors="International trade exposure; sanctions regime; controlled goods; counterparty risk profile."),
    "PUBL": G(
        data="Charity sector ML/TF risk assessment; sanctions screening of partners and beneficiaries; international program risk.",
        systems="Compliance platform; sanctions screening; programme management.",
        stakeholders="MLRO; CFO; CEO; donors; international partners.",
        key_factors="International programme exposure; partner organisation risk; sanctions screening maturity."),
},

"R-034": {
    "PROF": G(
        data="Lateral hire DD; gift register; FCPA-relevant matter exposure; conflict declarations.",
        systems="Acceptance system; gift register; HR; matter management.",
        stakeholders="Managing Partner; Ethics Partner; lateral candidates; clients.",
        key_factors="Lateral hire integrity; foreign government matter exposure; gift culture; partner accountability."),
    "FINS": G(
        data="PEP register; hospitality compliance; inducement events; conduct breaches.",
        systems="PEP screening; hospitality system; conduct surveillance.",
        stakeholders="CCO; PEP relationship managers; FCA / regulators.",
        key_factors="PEP exposure; client entertainment culture; conduct rules compliance; relationship pressure."),
    "TECH": G(
        data="Government engagement disclosures; channel partner certification; ABC training completion.",
        systems="Compliance management; channel platform; training.",
        stakeholders="GC; Compliance; Sales; channel partners.",
        key_factors="Government contracting expansion; channel partner DD; FCPA / UKBA exposure; sales pressure."),
    "HCAR": G(
        data="Pharma / device interaction transparency; CoI declarations; clinical influence concerns; procurement integrity.",
        systems="Transparency reporting; CoI register; procurement system.",
        stakeholders="CMO; Compliance; clinical decision-makers; pharma / device suppliers.",
        key_factors="Pharma / device industry interaction culture; clinical leader CoI; procurement integrity."),
    "RETL": G(
        data="Buyer rotation; gift register; supplier DD; overseas sourcing risk.",
        systems="Procurement; gift register; supplier portal; HR.",
        stakeholders="Buying Directors; Procurement; HR; high-risk suppliers.",
        key_factors="Buyer-supplier relationship culture; overseas sourcing geography; rotation discipline; gift culture."),
    "INDU": G(
        data="Facilitation payment events; permitting interaction logs; intermediary DD; FCPA exposure.",
        systems="Compliance management; permit tracking; intermediary management.",
        stakeholders="GC; Government Relations; Compliance; intermediaries; regulator.",
        key_factors="Operating jurisdiction corruption profile; permitting interaction frequency; intermediary use; FCPA / UKBA exposure."),
    "PUBL": G(
        data="Probity engagement; CoI declarations; tender complaints; integrity reports.",
        systems="Probity advisor system; CoI register; tender management; whistleblower hotline.",
        stakeholders="Probity Officer; Procurement; Integrity Officer; ICAC; vendors.",
        key_factors="Major tender programme; CoI declaration discipline; ICAC environment; transparency expectations."),
},

"R-035": {
    "PROF": G(
        data="BEC attempts; verification compliance; trust account fraud events; recovery rate.",
        systems="Email security; payment system; trust account.",
        stakeholders="CISO; Finance; Trust Account Controller; partners; clients.",
        key_factors="BEC sophistication; trust account fraud target value; verification discipline; partner-level oversight."),
    "FINS": G(
        data="Real-time fraud detection; scam losses; identity fraud rate; first-party fraud.",
        systems="Fraud platform; identity verification; behavioural analytics; payment system.",
        stakeholders="Head of Fraud; CCO; affected customers; payment scheme; AFCA.",
        key_factors="Scam evolution pace; identity fraud sophistication; first-party fraud rise; customer protection scheme expectations."),
    "TECH": G(
        data="Account takeover incidents; abuse detection rate; pattern analytics; user reports.",
        systems="Identity / fraud platform; trust & safety; product analytics.",
        stakeholders="Trust & Safety; CISO; product; users.",
        key_factors="Platform abuse profile; ATO sophistication; bot-driven abuse; emerging fraud typologies."),
    "HCAR": G(
        data="Identity fraud at registration; prescription / billing fraud patterns; vulnerable patient targeting.",
        systems="Patient management; pharmacy; billing.",
        stakeholders="Patient Services; Pharmacy; Compliance; vulnerable patients.",
        key_factors="Identity verification at registration; prescription fraud exposure; billing fraud patterns; elder targeting."),
    "RETL": G(
        data="Return fraud; payment fraud; ORC incidents; gift card / loyalty abuse.",
        systems="POS; e-commerce; loyalty platform; CCTV.",
        stakeholders="Loss Prevention; Customer Service; payment scheme; law enforcement.",
        key_factors="Return policy generosity; ORC environment; gift card abuse; e-commerce fraud sophistication."),
    "INDU": G(
        data="BEC events; vendor master integrity; cargo theft incidents; supply chain fraud.",
        systems="Email security; ERP; logistics; warehouse management.",
        stakeholders="Finance; IT Security; Logistics; insurance.",
        key_factors="BEC exposure on payments; cargo theft environment; supply chain visibility; insurance coverage."),
    "PUBL": G(
        data="Grant fraud detection; eligibility verification; BEC events; identity-based benefit fraud.",
        systems="Grants management; identity verification; payment system.",
        stakeholders="Compliance; Programs; Finance; ministerial; affected beneficiaries.",
        key_factors="Grant programme exposure; benefit fraud environment; BEC sophistication; verification discipline."),
},

"R-036": {
    "PROF": G(
        data="BCMS audit findings; remote work test results; client commitment continuity; matter handover effectiveness.",
        systems="BCMS; remote work tools; matter management.",
        stakeholders="BCM Lead; CIO; Practice Group Leaders; clients.",
        key_factors="Remote work readiness; client deadline criticality; matter handover discipline; partner-level engagement."),
    "FINS": G(
        data="IBS coverage; impact tolerances; severe-but-plausible scenario test outcomes; recovery to tolerance.",
        systems="IBS register; resilience platform; scenario tools; third-party register.",
        stakeholders="COO; Resilience Lead; CRO; APRA/FCA/PRA; critical service providers.",
        key_factors="Important Business Service criticality; impact tolerance achievement; third-party concentration; regulator expectations."),
    "TECH": G(
        data="Multi-region availability; chaos test pass rate; failover drill outcomes; status page accuracy.",
        systems="Multi-region cloud architecture; chaos engineering; status page.",
        stakeholders="Chief Architect; SRE; CTO; customers; cloud providers.",
        key_factors="Architecture resilience maturity; chaos engineering investment; cloud provider concentration; customer transparency."),
    "HCAR": G(
        data="Surge plan readiness; PPE stockpile; downtime drill outcomes; clinical service continuity.",
        systems="BCMS; clinical downtime procedures; supply chain.",
        stakeholders="BCM; CMO; Director of Operations; clinicians; patients.",
        key_factors="Surge / pandemic readiness; clinical workforce capability; supply chain resilience; downtime procedure maturity."),
    "RETL": G(
        data="Peak readiness; supply disruption response; alternative sourcing %; OOS during disruption.",
        systems="Supply chain; trading systems; alternative supplier register.",
        stakeholders="COO; Supply Chain; Buying; suppliers; logistics.",
        key_factors="Peak season concentration; supply chain visibility; alternative sourcing readiness; brand impact during disruption."),
    "INDU": G(
        data="Emergency exercise outcomes; weather / climate event preparedness; recovery times; community drills.",
        systems="HSE management; emergency systems; site management.",
        stakeholders="HSE Director; Operations; Site Managers; community; emergency services.",
        key_factors="Process safety profile; weather / climate exposure; community proximity; emergency capability."),
    "PUBL": G(
        data="Emergency response readiness; surge capacity; vulnerable beneficiary continuity; inter-agency coordination.",
        systems="BCMS; emergency systems; partner agreements.",
        stakeholders="BCM; Emergency Coordinator; CEO; partner agencies; vulnerable beneficiaries.",
        key_factors="Vulnerable beneficiary criticality; surge capacity; partner organisation resilience; inter-agency coordination maturity."),
},

"R-037": {
    "PROF": G(
        data="Engagement letter completion; scope variation; conflicts management; declined matters.",
        systems="Engagement letter; conflicts; matter management.",
        stakeholders="Risk Partner; Conflicts Partner; Practice Group Leaders; clients.",
        key_factors="Engagement scope discipline; conflicts complexity; partner culture on conduct."),
    "FINS": G(
        data="Conduct surveillance alerts; outcome testing; vulnerable customer outcomes; complaints / remediation.",
        systems="Conduct surveillance; product governance; vulnerable customer system; complaints.",
        stakeholders="CRO; Conduct Lead; Chief Customer Officer; FCA / ASIC; vulnerable customers.",
        key_factors="Sales culture; vulnerable customer scale; product complexity; remediation programme size."),
    "TECH": G(
        data="Design ethics review outcomes; dark pattern incidents; pricing fairness; complaints.",
        systems="Design review; product analytics; pricing engine.",
        stakeholders="Chief Trust Officer; CPO; GC; users; regulators.",
        key_factors="Product design ethics maturity; pricing personalisation depth; vulnerable user protection."),
    "HCAR": G(
        data="Pathway adherence; clinical decision review; vulnerable patient consent; advocacy engagement.",
        systems="Clinical pathways; decision support; consent system.",
        stakeholders="CMO; Clinical Directors; Director of Quality; patients; advocacy groups.",
        key_factors="Clinical decision-making consistency; vulnerable patient protection; consent / capacity assessment."),
    "RETL": G(
        data="Marketing review completion; pricing accuracy; BNPL affordability; vulnerable consumer outcomes.",
        systems="Marketing approval; pricing; BNPL platform.",
        stakeholders="Compliance; CMO; Chief Customer Officer; ACCC; ASIC; consumers.",
        key_factors="Consumer regulation environment; vulnerable consumer scale; marketing claim discipline; BNPL responsible practice."),
    "INDU": G(
        data="Cartel training completion; communications monitoring; sustainability claim substantiation.",
        systems="Compliance training; communications monitoring; sustainability platform.",
        stakeholders="GC; Sustainability; Sales; ACCC; investors; regulators.",
        key_factors="Cartel exposure (bid culture); sustainability claim discipline; commercial team training; supplier conduct."),
    "PUBL": G(
        data="Safeguarding training; safeguarding incidents; complaint patterns; trauma-informed practice scores.",
        systems="Safeguarding system; training; complaints; case management.",
        stakeholders="Safeguarding Lead; Director of Quality; staff; beneficiaries; advocacy.",
        key_factors="Vulnerable beneficiary risk; safeguarding maturity; trauma-informed practice; communication accessibility."),
},

"R-038": {
    "PROF": G(
        data="Reporting calendar compliance; reconciliation completion; audit findings; tax filing status.",
        systems="Practice management financial; tax platform; reporting calendar.",
        stakeholders="CFO; Financial Controller; trust account controller; auditors; ATO.",
        key_factors="Trust account regulatory complexity; partner / firm reporting integrity; tax position complexity."),
    "FINS": G(
        data="Filing timeliness; data quality; resubmissions; certification compliance.",
        systems="Regulatory reporting; data lineage; financial reporting; tax platform.",
        stakeholders="CFO; Head of Reg Reporting; Head of Tax; auditors; APRA/PRA/ATO.",
        key_factors="Regulatory reporting volume / complexity; data quality maturity; tax position uncertainty."),
    "TECH": G(
        data="Revenue recognition findings; SaaS metric reconciliation; multi-jurisdiction tax compliance; restatements.",
        systems="ERP; revenue platform; SaaS metrics; tax platform.",
        stakeholders="CFO; Financial Controller; Head of Tax; auditors; investors.",
        key_factors="Revenue recognition complexity (ASC 606); SaaS metric integrity; international tax exposure; Pillar Two readiness."),
    "HCAR": G(
        data="Coding accuracy; activity reporting; outcomes data quality; funder findings.",
        systems="Clinical coding; activity reporting; revenue cycle.",
        stakeholders="Clinical Coding; CFO; CMO; funders; auditors.",
        key_factors="Coding regime complexity; activity-based funding integrity; outcomes measurement maturity."),
    "RETL": G(
        data="Inventory cut-off accuracy; sustainability disclosure quality; modern slavery completeness.",
        systems="Inventory; ERP; sustainability platform; supplier portal.",
        stakeholders="CFO; Financial Controller; CSO; auditors; ACCC.",
        key_factors="Inventory cycle complexity; sustainability disclosure scope; supplier data quality; assurance readiness."),
    "INDU": G(
        data="Climate / ESG disclosure quality; emissions data integrity; royalty / EPBC reporting.",
        systems="Sustainability platform; emissions monitoring; ERP; sector reporting.",
        stakeholders="CSO; CFO; HSE; auditors; environmental regulators.",
        key_factors="Mandatory climate disclosure scope; Scope 3 data; sector-specific reporting complexity; assurance readiness."),
    "PUBL": G(
        data="Acquittal accuracy; outcomes reporting; statutory filing timeliness; funder findings.",
        systems="Grants management; outcomes reporting; financial system.",
        stakeholders="CFO; Programs; Company Secretary; funders; ACNC; sector regulator.",
        key_factors="Funder reporting complexity; outcomes measurement maturity; statutory reporting breadth; ministerial accountability."),
},

"R-039": {
    "PROF": G(
        data="Master data quality; conflicts data accuracy; KM precedent currency; matter classification consistency.",
        systems="Practice management; conflicts checking; KM platform; matter system.",
        stakeholders="Practice Management Lead; Knowledge Manager; Conflicts Partner; partners.",
        key_factors="Master data discipline; conflicts data integrity; KM relevance; matter classification."),
    "FINS": G(
        data="BCBS 239 maturity; aggregation timeliness; data quality scores; golden record coverage.",
        systems="Risk data warehouse; CDPs; MDM; lineage tools.",
        stakeholders="CDO; CRO; CFO; APRA/PRA; auditors.",
        key_factors="BCBS 239 expectation; aggregation maturity; golden record completeness; risk reporting timeliness."),
    "TECH": G(
        data="Training data quality; bias metrics; provenance completeness; telemetry accuracy.",
        systems="Data engineering; ML platform; analytics platform.",
        stakeholders="CDO; ML Lead; engineering; Trust & Safety.",
        key_factors="AI/ML training data quality; bias detection maturity; telemetry pipeline integrity."),
    "HCAR": G(
        data="Patient identification match rate; duplicate rate; documentation completeness; outcomes data quality.",
        systems="Patient master index; EMR; clinical documentation; outcomes platform.",
        stakeholders="CMIO; Director of Quality; clinical leaders; CDO.",
        key_factors="Patient identification accuracy; clinical documentation discipline; outcomes data integrity; coding quality."),
    "RETL": G(
        data="Master data completeness; SKU integrity; single customer view coverage; consent integrity.",
        systems="Master data; product information management; CDP; consent system.",
        stakeholders="Master Data Lead; Buying Director; CDO; suppliers.",
        key_factors="SKU master data discipline; supplier data quality; cross-channel customer integration; consent integrity."),
    "INDU": G(
        data="Sensor health; asset master data quality; ESG data quality; assurance readiness.",
        systems="Asset management; OT historian; ESG platform; emissions monitoring.",
        stakeholders="Asset Manager; OT; CSO; Engineering.",
        key_factors="OT data quality; asset master data; ESG data lineage; sensor reliability."),
    "PUBL": G(
        data="Identification accuracy; case data completeness; consent integrity; outcomes longitudinal completeness.",
        systems="Case management; identity platform; outcomes platform.",
        stakeholders="Director of Service; CDO; Outcomes Lead; beneficiaries.",
        key_factors="Beneficiary identification quality; case continuity; outcomes measurement maturity; consent management."),
},

"R-040": {
    "PROF": G(
        data="GenAI usage; matter incident data; client disclosure; tool DD coverage.",
        systems="AI platform; matter management; KM; risk register.",
        stakeholders="Innovation; Risk Partner; partners; clients; AI vendors.",
        key_factors="GenAI adoption velocity; matter sensitivity; hallucination risk; client disclosure norms."),
    "FINS": G(
        data="Capital / credit model performance; bias testing; explainability artefacts; adverse outcomes.",
        systems="Model risk platform; model inventory; validation tooling.",
        stakeholders="Head of Model Risk; CRO; APRA/PRA; FCA; affected customers.",
        key_factors="Capital model regulatory exposure; AI/ML adoption in conduct-relevant decisions; fairness expectations."),
    "TECH": G(
        data="Red-team coverage; safety eval results; ML monitoring; deployment governance.",
        systems="MLOps platform; safety eval; observability; AI governance.",
        stakeholders="Head of ML; AI Safety; Trust; users; regulators.",
        key_factors="AI deployment scale; safety eval maturity; red-team rigour; emerging AI regulation."),
    "HCAR": G(
        data="Clinical AI evidence; override patterns; outcome correlation; consent documentation.",
        systems="Clinical decision support; AI inventory; consent system.",
        stakeholders="CMIO; Clinical Governance; CMO; TGA; patients.",
        key_factors="Clinical AI deployment; clinician oversight; patient consent maturity; regulatory pathway."),
    "RETL": G(
        data="Pricing fairness reviews; vulnerable consumer outcomes; demand forecast accuracy.",
        systems="Pricing engine; personalisation platform; ML platform.",
        stakeholders="Compliance; Data Science; Customer; ACCC.",
        key_factors="Pricing personalisation depth; vulnerable consumer protection; demand forecast importance; algorithm fairness expectations."),
    "INDU": G(
        data="Predictive maintenance accuracy; false negative tracking; safety integration; calibration currency.",
        systems="Predictive maintenance; OT historian; safety systems.",
        stakeholders="Reliability; Data Science; Process Engineering; OT Safety.",
        key_factors="Predictive maintenance criticality; OT safety integration; model drift detection; calibration discipline."),
    "PUBL": G(
        data="Algorithmic decision accountability; appeal volume; bias testing; equity outcomes.",
        systems="Algorithmic decision system; case management; appeals platform.",
        stakeholders="CDO; Director of Service; Equity Lead; beneficiaries; ombudsman.",
        key_factors="Algorithmic decision-making in beneficiary services; explainability requirements; equity outcomes; appeal mechanisms."),
},

}
