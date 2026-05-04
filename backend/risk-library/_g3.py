"""Guidance Batch 3 — R-015 to R-027 (Tech & Cyber, Legal, Reputational, Env, H&S)."""
from risk_controls import G

GUIDANCE_3 = {

"R-015": {
    "PROF": G(
        data="Threat intelligence; phishing simulation results; vulnerability scan trends; SOC alert volumes; incident history.",
        systems="ISMS; IAM; vulnerability scanner; SIEM; DLP; document management.",
        stakeholders="CISO; Privacy Officer; Risk Partner; partners (high-value targets); IT vendors; cyber insurer.",
        key_factors="Sensitivity of client data; partner-level adoption of controls; phishing susceptibility; cyber insurance coverage."),
    "FINS": G(
        data="Threat intelligence; SOC metrics; vulnerability and patch posture; pen test results; APRA CPS 234 compliance data.",
        systems="ISMS; PAM; SIEM; identity / fraud platform; core banking; cloud platforms.",
        stakeholders="CISO; CIO; CRO; APRA; cyber insurer; payment scheme partners.",
        key_factors="Critical asset criticality; APRA expectations; payment scheme compliance; ransomware preparedness; OT/IT scope."),
    "TECH": G(
        data="Code security findings; dependency CVE exposure; CSPM findings; bug bounty reports; pen test results; incident metrics.",
        systems="SSDLC tooling; CI/CD; CSPM; cloud platforms; secrets management; identity provider.",
        stakeholders="CISO; CTO; engineering leadership; customers (security questionnaires); investors.",
        key_factors="Customer trust; multi-tenant isolation; cloud configuration discipline; SDLC maturity; security culture."),
    "HCAR": G(
        data="Medical device security posture; PHI access logs; phishing results; patch posture; cyber insurance claims data.",
        systems="ISMS; medical device asset register; EMR; PACS; IAM; SIEM.",
        stakeholders="CISO; CMIO; Director of Biomedical Engineering; medical device vendors; cyber insurer; TGA.",
        key_factors="Medical device connectivity; EMR criticality; clinical workforce awareness; legacy system footprint; ransomware exposure."),
    "RETL": G(
        data="PCI scope; e-commerce attack data; POS security posture; payment fraud trends; supply chain cyber posture.",
        systems="POS; e-commerce platform; payment infrastructure; loyalty / CRM; supplier portals.",
        stakeholders="CISO; Head of Payments; e-commerce lead; payment scheme; suppliers.",
        key_factors="PCI scope size; e-commerce platform security; supply chain exposure; peak-period DDoS exposure; payment scheme compliance."),
    "INDU": G(
        data="OT incident data; IT-OT segmentation; remote access logs; threat intelligence on critical infrastructure.",
        systems="OT/ICS; IT-OT firewalls; remote access; SCADA; SIEM with OT integration.",
        stakeholders="CISO; Head of OT Security; Operations; OT vendors; critical infrastructure regulator.",
        key_factors="OT criticality; segmentation maturity; remote access discipline; threat actor targeting of critical infrastructure."),
    "PUBL": G(
        data="Citizen-facing service attack data; legacy system exposure; staff phishing; threat intelligence; incident history.",
        systems="Citizen services; legacy systems; identity platform; SIEM; cloud platforms.",
        stakeholders="CISO; CIO; ministerial office; citizens; service partners; ASD/ACSC.",
        key_factors="Citizen service criticality; legacy footprint; staff awareness; nation-state threat targeting."),
},

"R-016": {
    "PROF": G(
        data="DLP events; misdirected email incidents; data classification coverage; privacy complaints; audit findings.",
        systems="Email; document management; DLP; matter system; conflicts checking.",
        stakeholders="Privacy Officer; CISO; Conflicts Partner; partners; clients (privacy concerns).",
        key_factors="Client privilege protection; ethical wall integrity; DLP tuning; partner-level email discipline."),
    "FINS": G(
        data="Tokenisation coverage; data lineage; retention compliance; privacy complaints; data subject request volumes.",
        systems="Customer database; tokenisation; data warehouse; CRM; complaints management.",
        stakeholders="Privacy Officer; CISO; CDO; OAIC/ICO; customers.",
        key_factors="Production data exposure; lineage maturity; retention compliance; PII inventory completeness."),
    "TECH": G(
        data="Secret leakage events; tenant isolation findings; pen test on data isolation; privacy complaints.",
        systems="Multi-tenant platform; secrets management; cloud data services; CRM.",
        stakeholders="CISO; Chief Architect; Privacy / DPO; customers (DPAs); regulators.",
        key_factors="Multi-tenant architecture maturity; secrets discipline; customer DPA obligations; cross-region data flow."),
    "HCAR": G(
        data="PHI access logs; anomaly investigations; privacy complaints; clinical workforce training metrics.",
        systems="EMR; clinical applications; PHI access logging; privacy training.",
        stakeholders="Privacy Officer; CISO; CMO; Director of Nursing; OAIC; patients.",
        key_factors="PHI volume; clinical workforce discipline; legacy clinical system access; celebrity/VIP record protection."),
    "RETL": G(
        data="Loyalty data quality; consent integrity; DSR volumes; privacy complaints; supplier data sharing.",
        systems="Loyalty platform; CRM; e-commerce; marketing automation; CDP.",
        stakeholders="Privacy Officer; CMO; Loyalty Lead; OAIC; customers; suppliers (data sharing).",
        key_factors="Loyalty programme PII volume; consent maturity; cross-border data flows; supplier data sharing discipline."),
    "INDU": G(
        data="IP exfiltration alerts; contractor access reviews; classification coverage; incident history.",
        systems="Engineering systems; document management; contractor access; DLP.",
        stakeholders="CISO; Chief Engineer; CPO; JV partners; legal.",
        key_factors="IP value; contractor / JV access volumes; classification discipline; cross-border IP flows."),
    "PUBL": G(
        data="DSR volumes; legacy access audits; privacy complaints; data sharing agreements.",
        systems="Citizen records; legacy systems; case management; integration platforms.",
        stakeholders="Privacy Officer; CIO; OAIC; citizens; sector partners.",
        key_factors="Legacy access creep; sensitive citizen data volume; data sharing agreements; legislative basis for data use."),
},

"R-017": {
    "PROF": G(
        data="Service availability metrics; SaaS vendor SLA achievement; remote work tests; incident history.",
        systems="Practice management; document management; e-billing; remote work tools.",
        stakeholders="CIO; Vendor Manager; partners; clients on critical deadlines; SaaS vendors.",
        key_factors="SaaS dependency depth; remote work readiness; deadline-critical client commitments."),
    "FINS": G(
        data="IBS availability vs tolerances; stress test results; payment infrastructure availability; incident history.",
        systems="Core banking; payment systems; market infrastructure connections; trading platforms.",
        stakeholders="COO; Resilience Lead; Operations; APRA/PRA; payment schemes; market infrastructure.",
        key_factors="IBS criticality; impact tolerance achievement; third-party dependency; regulator expectations."),
    "TECH": G(
        data="SLO / error budget consumption; failover test results; customer-reported incidents; status page accuracy.",
        systems="Cloud platforms; observability; status page; CDN; multi-region architecture.",
        stakeholders="CTO; SRE; customers (SLAs); enterprise customers (DR commitments).",
        key_factors="Multi-region maturity; cloud provider concentration; SLO achievement; chaos engineering maturity."),
    "HCAR": G(
        data="Clinical system availability; downtime drill outcomes; clinical impact during outage; failover testing.",
        systems="EMR; PACS; pharmacy; lab; clinical decision support; patient management.",
        stakeholders="CMIO; CMO; Director of Operations; clinicians; patients.",
        key_factors="Clinical workflow dependency; downtime procedure maturity; redundancy investment; patient safety during outage."),
    "RETL": G(
        data="POS / e-commerce uptime; peak load test results; payment processor availability; incident history.",
        systems="POS; e-commerce platform; payment processors; inventory; loyalty.",
        stakeholders="CIO; Head of Trading Systems; Head of Payments; customers; payment schemes.",
        key_factors="Peak trading concentration; processor concentration; alternative payment options; offline POS capability."),
    "INDU": G(
        data="OT availability; manual mode activation; ERP availability; supply chain visibility.",
        systems="OT/ICS; ERP; supply chain; quality systems; CMMS.",
        stakeholders="Head of OT; CIO; Operations; supply chain partners; customers.",
        key_factors="OT redundancy; manual operation readiness; ERP criticality; supply chain visibility maturity."),
    "PUBL": G(
        data="Citizen service availability; peak handling; cross-agency dependency availability; incident history.",
        systems="Citizen services; identity platform; payment platform; case management.",
        stakeholders="CIO; Head of Digital Services; ministerial office; citizens; cross-agency partners.",
        key_factors="Peak demand events; cross-agency dependency; legacy system reliability; ministerial expectations."),
},

"R-018": {
    "PROF": G(
        data="App portfolio TIME quadrant; tech debt register; legal-tech adoption; AI productivity metrics.",
        systems="Practice management; KM; document management; legal-tech tools; financial systems.",
        stakeholders="CIO; Innovation Officer; Practice Group Leaders; partners; AI vendors.",
        key_factors="Legacy system burden; legal-tech / AI adoption pace; partner appetite for change; vendor roadmap."),
    "FINS": G(
        data="Core platform age; modernisation milestones; legacy risk acceptance; debt register.",
        systems="Core banking / claims / trading; data warehouse; risk systems; supporting infrastructure.",
        stakeholders="Chief Transformation Officer; CIO; CRO; APRA/PRA; major vendors.",
        key_factors="Core platform criticality; modernisation programme size; regulatory pressure; vendor roadmap."),
    "TECH": G(
        data="DORA metrics; technical debt ratio; platform adoption; refactor velocity.",
        systems="CI/CD; observability; platform tooling; cloud infrastructure.",
        stakeholders="VP Engineering; CTO; CFO; investors; engineering teams.",
        key_factors="Engineering productivity; debt accumulation pace; platform engineering investment; cloud infrastructure flexibility."),
    "HCAR": G(
        data="Clinical system age; biomedical device profile; refresh plan execution; clinical adoption metrics.",
        systems="EMR; biomedical devices; PACS; clinical decision support.",
        stakeholders="CMIO; CIO; CMO; Director of Biomedical Engineering; clinicians.",
        key_factors="Clinical system age and vendor support; capital programme alignment; clinical change capacity."),
    "RETL": G(
        data="Channel integration maturity; POS age profile; data unification metrics; customer experience.",
        systems="POS; e-commerce; inventory; CRM; OMS; integration platforms.",
        stakeholders="CIO; CDO; Operations; customers; suppliers.",
        key_factors="Omnichannel pace; POS lifecycle; data unification investment; customer experience expectations."),
    "INDU": G(
        data="OT age profile; IT-OT integration; digital twin coverage; predictive maintenance adoption.",
        systems="OT/ICS; ERP; CMMS; analytics platform; digital twin.",
        stakeholders="Chief Engineer; CIO; Asset Manager; reliability engineers.",
        key_factors="OT obsolescence; IT-OT convergence pace; digital twin investment; asset criticality."),
    "PUBL": G(
        data="Legacy system inventory; modernisation milestones; cross-government platform adoption.",
        systems="Citizen-facing services; back-office systems; identity / payment / notification platforms.",
        stakeholders="CIO; Chief Transformation Officer; ministerial office; citizens; cross-agency.",
        key_factors="Legacy debt size; modernisation budget; cross-government platform readiness; ministerial sponsorship."),
},

"R-019": {
    "PROF": G(
        data="Obligation register; monitoring findings; AML SMR volumes; conflicts events; breach reports.",
        systems="Compliance management; AML system; conflicts checking; matter management.",
        stakeholders="CCO; MLRO; Conflicts Partner; AUSTRAC / regulators; clients.",
        key_factors="Tranche 2 readiness; conflicts complexity; monitoring maturity; partner-level engagement."),
    "FINS": G(
        data="Prudential ratios; CPS compliance; conduct breach data; SMR/BEAR coverage; breach register.",
        systems="Prudential reporting; conduct surveillance; regulatory reporting; risk systems.",
        stakeholders="CRO; CCO; CHRO; APRA/PRA/FCA; Board.",
        key_factors="Prudential standard breadth; CPS 230 readiness; SMR/BEAR maturity; regulator expectations."),
    "TECH": G(
        data="Privacy maturity; DSR response; breach notifications; AI inventory; readiness for emerging regulation.",
        systems="Privacy management; DSR handling; AI governance; consent platform.",
        stakeholders="DPO; Chief AI Officer; CCO; OAIC/ICO; customers; regulators.",
        key_factors="Multi-jurisdiction privacy scope; AI governance maturity; emerging regulation pace; product compliance integration."),
    "HCAR": G(
        data="Accreditation outcomes; clinical indicator performance; credentialing currency; ministerial inquiries.",
        systems="Clinical governance; credentialing; quality management; accreditation tracking.",
        stakeholders="Director of Clinical Governance; CMO; Director of Medical Workforce; AHPRA; accreditors.",
        key_factors="Accreditation cycle; clinical indicator trajectory; credentialing volume; sector reform pace."),
    "RETL": G(
        data="Consumer protection findings; product safety incidents; modern slavery DD; supplier compliance.",
        systems="Compliance management; supplier portal; product safety; modern slavery system.",
        stakeholders="GC; Quality Director; CSO; ACCC; suppliers; consumers.",
        key_factors="Consumer regulation pace; supply chain visibility; product safety regime; class action environment."),
    "INDU": G(
        data="Permit compliance; reportable HSE incidents; ESG disclosure readiness; emissions data quality.",
        systems="HSE management; permit tracking; ESG reporting; emissions monitoring.",
        stakeholders="Chief HSE Officer; CSO; CFO; environmental regulator; ASIC.",
        key_factors="Permit complexity; HSE incident profile; mandatory disclosure readiness; sector regulator scrutiny."),
    "PUBL": G(
        data="Funding agreement compliance; sector findings; ministerial reporting; statutory compliance.",
        systems="Compliance management; funding agreement tracking; statutory reporting; sector portal.",
        stakeholders="CCO; CFO; Company Secretary; sector regulator; funders; ministerial office.",
        key_factors="Funding agreement complexity; sector regulation tightening; ministerial accountability; multi-funder coordination."),
},

"R-020": {
    "PROF": G(
        data="PI claim history; engagement letter compliance; matter quality reviews; insurance claims data.",
        systems="Matter management; conflicts; engagement letter platform; PI claims system.",
        stakeholders="Risk Partner; GC; PI insurer; clients.",
        key_factors="Matter complexity / value; PI insurance pressure; engagement scope discipline; supervision quality."),
    "FINS": G(
        data="IDR/EDR volumes; AFCA referrals; class action register; remediation programme costs.",
        systems="Complaints management; remediation tracking; provisioning; matter management.",
        stakeholders="Head of Complaints; GC; CFO; AFCA; class action lawyers; regulators.",
        key_factors="Class action environment; AFCA volume; remediation programme size; regulator coordination."),
    "TECH": G(
        data="SLA breach incidents; IP infringement claims; customer disputes; provisions.",
        systems="Customer success; SLA monitoring; IP register; legal matter management.",
        stakeholders="GC; Customer Success; Head of IP; enterprise customers; patent counsel.",
        key_factors="SLA exposure; IP landscape; enterprise customer leverage; FTO maturity."),
    "HCAR": G(
        data="Clinical claims; sentinel events; documentation audit; insurance claims data.",
        systems="Incident reporting; clinical records; claims system; quality management.",
        stakeholders="Risk Manager; Director of Quality; CMO; clinical insurer; patients/families.",
        key_factors="Clinical risk profile; documentation quality; open disclosure maturity; clinician engagement."),
    "RETL": G(
        data="Consumer claims; recall events; supplier disputes; class action register.",
        systems="Quality management; recall coordination; supplier portal; legal matter management.",
        stakeholders="Quality Director; GC; Property; suppliers; consumers; ACCC.",
        key_factors="Product safety regime; class action exposure; supplier dispute volume; landlord lease portfolio."),
    "INDU": G(
        data="Project variations; product liability claims; recall capability; contractual disputes.",
        systems="Project controls; claims register; quality management; legal matter management.",
        stakeholders="Commercial Director; Quality Director; GC; customers; subcontractors; insurers.",
        key_factors="Project contract complexity; product liability exposure; claim management discipline; insurance programme."),
    "PUBL": G(
        data="Beneficiary complaints; redress scheme participation; historical conduct claims; class action register.",
        systems="Complaints management; safeguarding; redress scheme reporting; matter management.",
        stakeholders="Complaints Lead; Safeguarding Lead; GC; CEO; redress schemes; survivors.",
        key_factors="Historical conduct exposure; safeguarding maturity; redress scheme participation; ministerial visibility."),
},

"R-021": {
    "PROF": G(
        data="Horizon items tracked; tranche 2 readiness; practice updates published.",
        systems="Regulatory horizon; KM; client advisory.",
        stakeholders="Head of Regulatory Affairs; Practice Group Leaders; MLRO; clients.",
        key_factors="Tranche 2 commencement; sector regulator activity; cross-jurisdiction practice exposure."),
    "FINS": G(
        data="Regulatory PMO RAG; supervisory feedback; commitment closure; horizon items tracked.",
        systems="Regulatory PMO; obligation register; regulator interaction tracking.",
        stakeholders="Head of Regulatory Affairs; CCO; programme sponsors; regulator (APRA/PRA/FCA).",
        key_factors="Regulatory programme volume; supervisory focus areas; commitment closure pace; regulator relationship strength."),
    "TECH": G(
        data="Privacy / AI regulation tracking; product readiness; enforcement-date compliance.",
        systems="Regulatory horizon; product compliance; AI governance.",
        stakeholders="DPO; Chief AI Officer; CCO; product leadership; regulators.",
        key_factors="Cross-jurisdiction privacy scope; AI Act commencement; product release alignment; enforcement pace."),
    "HCAR": G(
        data="Standards adoption; clinician training on changes; accreditation readiness; inquiry recommendations status.",
        systems="Clinical governance; training; accreditation tracking; inquiry response tracking.",
        stakeholders="Director of Clinical Governance; CMO; CEO; sector regulator; ministerial office.",
        key_factors="Sector reform pace (NDIS, aged care); royal commission recommendations; accreditation refresh."),
    "RETL": G(
        data="Sustainability disclosure readiness; modern slavery DD; class action environment monitoring.",
        systems="Sustainability platform; supplier portal; legal horizon scanning.",
        stakeholders="CSO; GC; CMO; suppliers; ACCC.",
        key_factors="Mandatory sustainability disclosure; modern slavery expansion; class action environment."),
    "INDU": G(
        data="Climate / ESG regulation tracking; permitting status; readiness assessments.",
        systems="Sustainability platform; permit tracking; risk management.",
        stakeholders="CSO; HSE; CFO; environmental regulators; ASIC.",
        key_factors="ASRS / ISSB commencement; sector decarbonisation policy; permit renewal cycle."),
    "PUBL": G(
        data="Sector reform tracking; ministerial brief acceptance; funder requirement changes.",
        systems="Government relations; funding agreement tracking; sector intelligence.",
        stakeholders="GM Government Relations; CCO; CFO; ministerial advisors; funders.",
        key_factors="Election cycles; sector reform direction; funder requirement evolution; cross-jurisdictional pace."),
},

"R-022": {
    "PROF": G(
        data="Reputation sentiment; partner conduct events; matter sensitivity reviews; client/talent impact.",
        systems="Media monitoring; sentiment platform; acceptance system; HR.",
        stakeholders="Managing Partner; CCO; Ethics Partner; clients; media; talent market.",
        key_factors="Partner conduct profile; sensitive matter portfolio; firm visibility; talent market dynamics."),
    "FINS": G(
        data="Sentiment data; royal commission/inquiry status; remediation programme progress; document production.",
        systems="Media monitoring; remediation tracking; legal matter management.",
        stakeholders="CEO; CCO; Communications; regulators; customers; investors.",
        key_factors="Inquiry exposure; remediation programme size; customer harm scale; media intensity."),
    "TECH": G(
        data="Trust & safety incident data; AI ethics commitments tracking; user safety outcomes; sentiment data.",
        systems="Trust & safety platform; AI governance; sentiment monitoring.",
        stakeholders="Chief Trust Officer; CEO; users; regulators; press.",
        key_factors="AI deployment scale; user vulnerability; press attention to AI; ethics commitment credibility."),
    "HCAR": G(
        data="Sentinel events; open disclosure outcomes; family satisfaction; sentiment data.",
        systems="Patient safety system; open disclosure tracking; complaints; media monitoring.",
        stakeholders="Director of Patient Safety; CMO; Family Liaison; regulators; coroner; media.",
        key_factors="Clinical risk profile; open disclosure maturity; coroner inquest exposure; media interest."),
    "RETL": G(
        data="Recall events; product safety incidents; social media sentiment; consumer complaints.",
        systems="Recall coordination; sentiment platform; complaints management; social listening.",
        stakeholders="Quality Director; Communications; CMO; consumers; ACCC; media.",
        key_factors="Product safety profile; social media virality; brand strength; consumer trust capital."),
    "INDU": G(
        data="Community sentiment; safety / environmental incident data; ESG ratings; investor engagement.",
        systems="Community engagement; HSE management; ESG platform; sentiment monitoring.",
        stakeholders="GM Community Relations; CSO; CEO; community; investors; media.",
        key_factors="Operations community proximity; safety / environmental track record; ESG investor sentiment."),
    "PUBL": G(
        data="Ministerial brief quality; sentiment data; safeguarding incidents; community engagement.",
        systems="Government relations; safeguarding system; complaints; sentiment monitoring.",
        stakeholders="CEO; GM Government Relations; Director of Safeguarding; ministerial office; beneficiaries; media.",
        key_factors="Vulnerable beneficiary risk; ministerial visibility; community trust; sector inquiry environment."),
},

"R-023": {
    "PROF": G(
        data="Client NPS; relationship review outcomes; directory rankings; talent attraction data.",
        systems="CRM; relationship review platform; engagement surveys; brand tracking.",
        stakeholders="Managing Partner; Practice Group Leaders; clients; talent market; directories.",
        key_factors="Client perception; quality reputation; talent attractiveness; directory positioning."),
    "FINS": G(
        data="NPS by segment; complaint themes; analyst sentiment; share register stability.",
        systems="VOC platform; complaints; investor relations; analyst tracking.",
        stakeholders="Chief Customer Officer; CFO; Head of IR; customers; analysts; investors.",
        key_factors="Customer franchise strength; analyst confidence; investor engagement; remediation impact."),
    "TECH": G(
        data="NRR; logo retention; community engagement; product feedback integration.",
        systems="Customer success; product analytics; community platforms; feedback systems.",
        stakeholders="Chief Customer Officer; Head of Community; product leadership; customers; developers.",
        key_factors="Customer outcome focus; community vibrancy; product feedback responsiveness; product-market fit signals."),
    "HCAR": G(
        data="Patient experience scores; family feedback; referrer satisfaction; visible action evidence.",
        systems="Patient experience platform; CRM; feedback systems; clinical liaison.",
        stakeholders="Director of Patient Experience; Business Development; CMO; patients; families; referrers.",
        key_factors="Patient experience excellence; clinical reputation; referrer relationship strength; visible action on feedback."),
    "RETL": G(
        data="Loyalty programme metrics; brand health; ethical sourcing transparency; consumer trust on ethics.",
        systems="Loyalty platform; brand tracking; sustainability disclosure; CDP.",
        stakeholders="Chief Customer Officer; CMO; CSO; consumers; loyalty members.",
        key_factors="Loyalty engagement; brand health trajectory; ethical credentials; consumer trust resilience."),
    "INDU": G(
        data="Community sentiment; benefit-sharing delivery; ESG ratings; investor engagement.",
        systems="Community engagement; CSR programme; ESG platform; investor relations.",
        stakeholders="GM Community Relations; CSO; CFO; communities; investors; ratings agencies.",
        key_factors="Community partnership depth; benefit delivery; ESG ratings trajectory; investor confidence."),
    "PUBL": G(
        data="Beneficiary co-design participation; funder satisfaction; outcomes achievement.",
        systems="Service design platform; outcomes reporting; funder reporting.",
        stakeholders="Director of Service Design; CEO; CFO; beneficiaries; funders; ministerial.",
        key_factors="Beneficiary lived experience integration; outcomes evidence; funder confidence; transparent learning."),
},

"R-024": {
    "PROF": G(
        data="Footprint metrics; energy / waste / travel; client demand for ESG capability; disclosure quality.",
        systems="Sustainability platform; expense system; facilities management; KM.",
        stakeholders="Sustainability Lead; Office Manager; Practice Group Leaders; clients; talent.",
        key_factors="Office footprint scale; client demand for ESG advisory; talent expectations; disclosure landscape."),
    "FINS": G(
        data="Climate-aligned portfolio; high-risk exposure; transition plan progress; scenario analysis.",
        systems="Climate risk platform; portfolio analytics; scenario tools; ESG data.",
        stakeholders="CRO; CSO; Head of Climate Risk; APRA/PRA; investors.",
        key_factors="Portfolio carbon intensity; transition risk exposure; scenario analysis maturity; regulator expectations."),
    "TECH": G(
        data="Compute carbon intensity; PUE; AI training emissions; sustainability features in product.",
        systems="Cloud platform; AI infrastructure; sustainability dashboard.",
        stakeholders="Sustainability Lead; CTO; engineering; investors; customers (sustainability requirements).",
        key_factors="Compute scale; AI training intensity; cloud provider sustainability; product sustainability features."),
    "HCAR": G(
        data="Waste segregation compliance; pharmaceutical disposal; energy intensity; anaesthetic gas footprint.",
        systems="Waste management; energy management; sustainability platform.",
        stakeholders="Director of Facilities; Sustainability Lead; HSE; clinical leaders.",
        key_factors="Clinical waste volume; pharmaceutical disposal complexity; energy demand; anaesthetic alternatives."),
    "RETL": G(
        data="Packaging reduction; supplier sustainability; deforestation exposure; recyclability %.",
        systems="Sustainability platform; supplier portal; product data.",
        stakeholders="CSO; Buying Director; suppliers; consumers; investors.",
        key_factors="Packaging volume; supply chain visibility; high-risk commodity exposure; consumer expectations."),
    "INDU": G(
        data="Process safety events; emissions intensity; abatement delivered; permit compliance.",
        systems="HSE management; emissions monitoring; permit tracking; sustainability platform.",
        stakeholders="HSE Director; CSO; CEO; environmental regulator; communities; investors.",
        key_factors="Process safety profile; emissions trajectory; SBT alignment; permit complexity."),
    "PUBL": G(
        data="Emissions reduction; commitment progress; community concerns; environmental compliance.",
        systems="Sustainability platform; community engagement; HSE management.",
        stakeholders="Sustainability Lead; CEO; HSE; community; ministerial.",
        key_factors="Net-zero commitment credibility; community impact; compliance maturity; political support."),
},

"R-025": {
    "PROF": G(
        data="Acceptance review outcomes; pro bono engagement; talent / client signals.",
        systems="Acceptance system; pro bono tracking; HR.",
        stakeholders="Acceptance Committee; Ethics Partner; talent; clients; community.",
        key_factors="Sensitive client portfolio; ethics committee maturity; pro bono visibility; talent values."),
    "FINS": G(
        data="Vulnerable customer support delivery; ethical investment compliance; HRDD coverage.",
        systems="Vulnerable customer system; ethical investment screening; HRDD platform.",
        stakeholders="Chief Customer Officer; CRO; CSO; UNGP regulators; NGOs.",
        key_factors="Vulnerable customer scale; ethical exclusion regime; HRDD maturity; activist investor pressure."),
    "TECH": G(
        data="Safety incidents; AI ethics review outcomes; transparency report quality.",
        systems="Trust & safety platform; AI governance; content moderation.",
        stakeholders="Chief Trust Officer; AI Officer; users; regulators; civil society.",
        key_factors="Platform user vulnerability; AI deployment risk; regulator focus; civil society scrutiny."),
    "HCAR": G(
        data="Cultural safety scores; indigenous health pathways; equity metrics; vulnerable patient outcomes.",
        systems="Patient experience; clinical pathways; equity dashboards.",
        stakeholders="Chief Aboriginal Health; CMO; communities; advocacy groups.",
        key_factors="Indigenous workforce; cultural safety maturity; equity pathway investment; community trust."),
    "RETL": G(
        data="Supplier audits; high-risk supplier coverage; remediation cases; marketing reviews.",
        systems="Supplier portal; modern slavery platform; marketing approval.",
        stakeholders="CSO; Procurement; CMO; suppliers; advocacy groups; consumers.",
        key_factors="Supply chain geography; high-risk commodity exposure; vulnerable consumer protection."),
    "INDU": G(
        data="ILUA currency; benefit-sharing delivery; heritage incidents; community investment delivery.",
        systems="Indigenous engagement system; community investment; heritage management.",
        stakeholders="Indigenous Relations Lead; GM Community Relations; communities; First Nations groups.",
        key_factors="Indigenous land relationship; cultural heritage exposure; community partnership depth."),
    "PUBL": G(
        data="Co-design participation; community representation; First Nations engagement quality.",
        systems="Service design platform; engagement tracking; First Nations engagement.",
        stakeholders="Director of Service Design; GM First Nations; community representatives.",
        key_factors="Beneficiary engagement maturity; First Nations relationship; treaty/voice mechanisms; community influence on decisions."),
},

"R-026": {
    "PROF": G(
        data="Psychosocial survey; EAP utilisation; ergonomic assessments; reported incidents.",
        systems="HR; EAP system; OHS reporting.",
        stakeholders="CHRO; Safety Lead; partners; staff.",
        key_factors="Workload pressure; harassment / burnout patterns; remote work safety; partner-level conduct."),
    "FINS": G(
        data="Branch security incidents; psychosocial indicators in trading / customer service; staff support utilisation.",
        systems="Branch security; HR; psychosocial monitoring; EAP.",
        stakeholders="CHRO; Head of Branch Security; Safety; staff.",
        key_factors="Branch crime rate; high-pressure roles; staff support uptake; supervisor capability."),
    "TECH": G(
        data="Burnout indicators; on-call burden; wellbeing scores; isolation indicators.",
        systems="HR; engineering planning; wellbeing platform; on-call system.",
        stakeholders="CHRO; Engineering Leadership; Wellbeing Lead; staff.",
        key_factors="On-call rotation discipline; sustainable pace; remote-first connection; mental health support."),
    "HCAR": G(
        data="Manual handling injuries; vicarious trauma indicators; debrief participation; EAP uptake.",
        systems="OHS reporting; manual handling system; EAP; clinical wellbeing.",
        stakeholders="Director of Workforce Safety; CHRO; clinical leaders; staff.",
        key_factors="Patient handling volume; clinical exposure to trauma; wellbeing programme maturity."),
    "RETL": G(
        data="Aggression incidents; MSD injuries; security response; safety culture scores.",
        systems="OHS reporting; security; HR; safety culture survey.",
        stakeholders="Operations Director; Safety; HR; staff; security partners.",
        key_factors="Customer aggression frequency; physical work demands; security investment; safety culture maturity."),
    "INDU": G(
        data="SIF rate; critical control verification; permit compliance; near-miss correlation.",
        systems="HSE management; permit system; critical control assurance.",
        stakeholders="Chief Safety Officer; site managers; contractors; regulator (SafeWork).",
        key_factors="Hazard profile; critical control discipline; contractor management; safety culture."),
    "PUBL": G(
        data="Aggression incidents; lone worker activations; vicarious trauma indicators; supervision metrics.",
        systems="HR; lone worker system; EAP; supervision tracking.",
        stakeholders="Safety Lead; CHRO; Practice Lead; frontline staff.",
        key_factors="Beneficiary risk profile; lone worker exposure; vicarious trauma; supervision quality."),
},

"R-027": {
    "PROF": G(
        data="Visitor incidents; emergency drill outcomes; first aid response; building safety.",
        systems="Visitor management; emergency systems; building safety.",
        stakeholders="Office Manager; Security; Safety; visitors.",
        key_factors="Office visitor profile; building safety; emergency preparedness; warden coverage."),
    "FINS": G(
        data="Branch security incidents; vulnerable customer protection; elder abuse cases.",
        systems="Branch security; vulnerable customer system; complaints.",
        stakeholders="Head of Branch Security; Customer Vulnerability Lead; regulator; customers.",
        key_factors="Branch protection; vulnerable customer identification; elder financial abuse; protective intervention skills."),
    "TECH": G(
        data="Content moderation volume; user safety outcomes; harm prevention features; user reports.",
        systems="Trust & safety platform; content moderation; user reporting.",
        stakeholders="Chief Trust Officer; Product; users; regulators (online safety).",
        key_factors="User vulnerability profile; content scale; harm prevention by design; transparency reporting maturity."),
    "HCAR": G(
        data="Never-events; medication errors; critical control compliance; patient safety culture.",
        systems="Patient safety system; medication management; barcode verification.",
        stakeholders="Director of Patient Safety; CMO; pharmacy; clinicians; patients.",
        key_factors="Never-event exposure; medication safety; clinical workforce capability; safety culture maturity."),
    "RETL": G(
        data="Food safety incidents; HACCP audits; in-store safety walks; emergency drill outcomes.",
        systems="Food safety; HACCP; safety reporting; emergency systems.",
        stakeholders="Food Safety Manager; Operations; Safety; consumers; regulator (FSANZ).",
        key_factors="Food safety regime; in-store hazard profile; emergency preparedness; supplier verification."),
    "INDU": G(
        data="Public incidents; community impact; control effectiveness; contractor safety performance.",
        systems="HSE management; community engagement; contractor system.",
        stakeholders="Chief Safety Officer; community; regulator; contractors.",
        key_factors="Operations community proximity; contractor management; engineering controls; emergency preparedness."),
    "PUBL": G(
        data="Safeguarding incidents; screening compliance; training completion; critical incident response.",
        systems="Safeguarding system; HR screening; training; incident reporting.",
        stakeholders="Safeguarding Lead; CEO; regulator; vulnerable beneficiaries; families.",
        key_factors="Vulnerable beneficiary profile; safeguarding maturity; screening discipline; family trust."),
},

}
