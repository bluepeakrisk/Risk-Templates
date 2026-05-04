"""
Control Theme classification
=============================
Maps each control to ONE of 20 functional themes based on what the control DOES,
not what risk it protects against.

Same matching approach as frameworks: ANY keyword in a rule matches; first matching rule wins.
Single-word keywords use word-boundary matching to prevent substring false positives.
"""
import re

# Order matters — most-specific first, generic last
# Format: (keywords, theme_name)
THEME_RULES = [

    # ──────────── DETECTION ────────────
    # Reconciliation & Verification — most specific first
    (["reconciliation", "three-way match", "po", "settlement verification",
      "file integrity", "fim", "reconciliations",
      "independent verification", "balance verification",
      "control reconciliation", "data reconciliation",
      "ledger reconciliation"],
     "Reconciliation & Verification"),

    # Monitoring & Surveillance
    (["soc", "siem", "surveillance", "transaction monitoring", "kpi dashboard",
      "real-time monitoring", "behavioural analytics", "anomaly detection",
      "alert", "monitoring system", "behavioural monitoring", "voc", "voice of customer",
      "lcr", "nsfr", "exposure monitoring", "ratio monitoring",
      "intelligence", "exception monitoring", "exception reporting",
      "fraud monitoring", "fraud detection", "billing pattern monitoring",
      "exposure identification", "limits monitoring", "monitoring of",
      "performance monitoring", "leading indicators",
      "performance dashboard", "concentration monitoring dashboard",
      "talent metrics", "attrition surveillance",
      "compliance monitoring dashboard", "breach surveillance",
      "key person dependency monitoring", "third-party monitoring",
      "third-party performance"],
     "Monitoring & Surveillance"),

    # Quality Reviews & Assurance
    (["peer review", "quality review", "file review", "m&m", "morbidity",
      "internal audit", "control testing", "assurance programme", "outcome testing",
      "audit programme", "quality assurance", "matter quality", "control assurance",
      "post-implementation review", "post implementation",
      "accreditation readiness", "accreditation review", "clinical governance",
      "compliance review", "business case discipline", "peer challenge",
      "credentialing review"],
     "Quality Reviews & Assurance"),

    # Reporting & Disclosure
    (["financial reporting", "regulatory reporting", "statutory reporting",
      "esg disclosure", "tcfd", "issb", "asrs", "fatca", "crs",
      "transparency report", "disclosure", "reporting calendar",
      "reporting controls", "external reporting", "outcomes reporting",
      "acquittal", "acquittal reporting", "casemix reporting",
      "modern slavery", "sustainability reporting", "esg reporting"],
     "Reporting & Disclosure"),

    # ──────────── PREVENTION ────────────
    # Access & Identity Management
    (["iam", "identity and access", "mfa", "multi-factor", "privileged access",
      "user access review", "uar", "least privilege", "pam", "joiner",
      "access controls", "access management", "authentication",
      "production access", "access governance", "data access governance",
      "model access", "ai access governance",
      "identity modernisation", "phi access", "access logging", "credentialing"],
     "Access & Identity Management"),

    # Due Diligence & Onboarding
    (["due diligence", "kyc", "kyb", "cdd", "onboarding",
      "background check", "pre-employment", "screening",
      "lateral hire dd", "fpic", "site validation"],
     "Due Diligence & Onboarding"),

    # Training & Awareness
    (["training", "awareness", "phishing simulation", "attestation",
      "code attestation", "competency assessment"],
     "Training & Awareness"),

    # Engineering & Configuration
    (["secure software", "ssdlc", "sdlc", "secure configuration",
      "network segmentation", "encryption", "tokenisation",
      "secrets management", "cspm", "ot/ics", "purdue", "cis benchmark",
      "platform architecture", "multi-region", "active-active",
      "data isolation", "segregation between", "ddos", "waf",
      "modular architecture", "decomposition", "infrastructure resilience",
      "platform decomposition", "operational technology refresh",
      "decarbonisation", "remote working infrastructure",
      "engineering standards", "reference architecture",
      "data engineering standards", "pipeline integrity",
      "ai engineering standards", "model engineering standards",
      "modernisation engineering",
      "prompt injection", "llm input defence",
      "ai supply chain", "software bill of materials", "sbom",
      "sensitive data prevention", "vector store",
      "embedding governance"],
     "Engineering & Configuration"),

    # ──────────── GOVERNANCE & OVERSIGHT ────────────
    # Limits & Authorisations
    (["segregation of duties", "sod", "authority matrix", "delegation of authority",
      "approval limits", "limits", "delegated approval", "authorisation",
      "approval workflow", "approval matrix", "approval threshold",
      "authority breach", "limits monitoring", "var ", "value at risk"],
     "Limits & Authorisations"),

    # Strategy & Planning
    (["strategic plan", "strategic planning", "horizon scanning",
      "competitor intelligence", "war-gaming", "innovation budget",
      "capability roadmap", "scenario planning", "capacity planning",
      "demand forecasting", "kpi", "leading indicator", "stage gate",
      "stage-gate", "portfolio", "strategic flexibility", "strategy review",
      "diversification strategy", "fintech partnership", "innovation programme",
      "capability assessment", "roadmap", "transition planning",
      "channel strategy", "format strategy", "customer discovery",
      "product-market fit", "market analytics", "customer data platform",
      "demand surge capability", "modernisation programme",
      "programme monitoring", "modernisation programme monitoring"],
     "Strategy & Planning"),

    # Governance & Reporting (board / executive)
    (["board oversight", "board-level", "executive committee",
      "audit committee", "alco", "governance framework",
      "governance committee", "ministerial briefing", "board governance",
      "board attestation", "board endorsement",
      "steering committee", "investment committee", "innovation steering",
      "disruption oversight", "programme governance", "project governance",
      "governance and steering"],
     "Governance & Reporting"),

    # Investigation & Remediation — placed early so investigation-themed controls match before generic "framework" keyword
    (["fraud investigation", "rca", "root cause", "customer remediation",
      "remediation programme", "capa", "investigation framework",
      "non-conformance", "post-incident review", "post-implementation review",
      "lessons learned", "claims management", "litigation management",
      "investigation and remediation", "investigation and consequence",
      "investigation and pattern", "investigation and case management",
      "investigation and knowledge", "post-disruption review",
      "post-mortem", "departure investigation", "talent loss investigation",
      "compliance breach investigation", "reporting error investigation",
      "conduct event investigation", "aml investigation",
      "bribery investigation", "project failure investigation",
      "asset failure investigation", "capacity failure investigation",
      "safety incident investigation", "data quality incident",
      "incident and harm response", "post-deal review",
      "quality recovery and customer remediation"],
     "Investigation & Remediation"),

    # Policy & Framework
    (["policy", "framework", "code of conduct", "standards",
      "behavioural standards", "ohsms", "qms", "ems", "isms",
      "policy framework", "documented framework", "obligations register",
      "treasury policy", "abc policy", "directive control",
      "service standards", "ethical wall"],
     "Policy & Framework"),

    # Risk Assessment
    (["risk assessment", "risk-based assessment", "bia", "business impact analysis",
      "scenario analysis", "stress test", "scenario testing", "risk tiering",
      "fraud risk assessment", "ml/tf risk assessment", "social impact assessment",
      "hazard identification", "hira", "vulnerability scan",
      "risk identification", "control framework", "risk register",
      "concentration risk", "concentration monitoring",
      "exposure quantification", "exposure assessment",
      "13-week", "cash flow forecast", "burn rate", "runway tracking",
      "freedom-to-operate", "fto",
      "disruption risk", "scenario assessment",
      "tech debt risk assessment", "external fraud risk assessment",
      "data risk assessment", "cyber risk assessment", "process risk assessment",
      "outsourcing risk assessment", "asset criticality",
      "failure risk assessment", "fmea", "bottleneck",
      "demand-supply risk", "environmental aspects and impacts",
      "aspects and impacts assessment",
      "critical data elements", "cde", "threat modelling",
      "market risk identification", "market risk quantification"],
     "Risk Assessment"),

    # ──────────── RESPONSE ────────────
    # Incident & Crisis Management
    (["incident management", "incident response", "crisis management",
      "crisis playbook", "sentinel event", "open disclosure",
      "social media response", "ministerial response",
      "breach response", "spokesperson", "community communication",
      "customer communication during outages", "recall coordination",
      "recall capability", "outage response",
      "fatality response", "sif response", "serious injury",
      "breach notification", "data breach response",
      "harm response", "incident and harm"],
     "Incident & Crisis Management"),

    # Continuity & Recovery
    (["business continuity", "bcms", "bcm ", "disaster recovery", "dr ",
      "failover", "backup", "redundancy", "surge capacity",
      "spare parts", "alternative sourcing", "downtime procedure",
      "operational resilience", "important business service",
      "impact tolerance", "recovery test", "manual operation",
      "alternate", "contingency funding", "remote work continuity",
      "demand surge", "service rationing", "service prioritisation",
      "peak readiness", "peak trading", "infrastructure backup",
      "vehicle and mobile asset", "branch network resilience",
      "atm availability", "weather event preparation",
      "client commitment continuity", "cash runway resilience",
      "cost flexibility",
      "service continuity", "exit planning and continuity",
      "platform continuity", "ai service continuity",
      "model service continuity", "data platform continuity",
      "legacy system continuity"],
     "Continuity & Recovery"),

    # Investigation & Remediation rule moved to top of file (above Policy & Framework)

    # ──────────── STAKEHOLDER ENGAGEMENT ────────────
    # Customer / Beneficiary Management
    (["customer success", "voc programme", "customer feedback",
      "complaint", "vulnerable customer", "vulnerable consumer",
      "vulnerable beneficiary", "vulnerable patient", "co-design",
      "patient experience", "client relationship", "client listening",
      "nps programme", "loyalty programme", "vulnerable user",
      "trust & safety", "trust and safety",
      "branch security and customer", "customer protection",
      "patient consent", "beneficiary engagement",
      "customer experience and retention",
      "customer experience framework"],
     "Customer & Beneficiary Management"),

    # Stakeholder Engagement
    (["stakeholder", "community engagement", "community investment",
      "first nations", "indigenous engagement", "ilua",
      "regulator engagement", "regulator relationship",
      "investor engagement", "investor relations", "media monitoring",
      "reputation monitoring", "stakeholder engagement",
      "ministerial engagement", "donor", "industry engagement",
      "submissions", "investor and analyst engagement",
      "analyst engagement", "funder relationship",
      "referrer engagement", "channel partner",
      "developer community", "payer and contract"],
     "Stakeholder Engagement"),

    # People Management
    (["succession plan", "talent retention", "engagement survey",
      "compensation benchmarking", "evp", "career path", "wellbeing",
      "psychosocial", "burnout", "mandatory leave", "knowledge management",
      "knowledge transfer", "graduate programme", "apprenticeship",
      "workforce planning", "hiring", "recruitment process",
      "people decision", "diversity", "dei", "remuneration",
      "trade pipeline", "stem", "fifo", "lifestyle support",
      "cultural safety", "racism prevention", "bullying intervention",
      "harassment prevention", "respect@work", "respectful workplace",
      "macho culture", "junior clinician", "clinical wellbeing",
      "vicarious trauma", "manual handling", "ergonomics",
      "equity programme", "equity refresh", "total reward",
      "international recruitment", "frontline manager",
      "engineering productivity", "compensation flexibility",
      "talent strategy", "tech talent", "engineering brand",
      "workforce flexing"],
     "People Management"),

    # ──────────── SPECIALISED ────────────
    # Modelling & Analytics
    (["model risk", "model validation", "model inventory",
      "mlops", "ml lifecycle", "ai ethics", "ai governance",
      "responsible ai", "ai safety", "red-teaming", "bias testing",
      "fairness", "clinical ai", "explainability", "model monitoring",
      "model performance", "spc", "statistical process control",
      "predictive maintenance", "ai/ml", "algorithmic decision",
      "population health analytics", "analytics capability",
      "personalisation algorithm"],
     "Modelling & Analytics"),
]


def _kw_in(haystack, kw):
    """Word-boundary match for single words; substring for multi-word phrases."""
    if " " in kw or "-" in kw or "/" in kw:
        return kw in haystack
    return re.search(r'\b' + re.escape(kw) + r'\b', haystack) is not None


def classify_theme(name, description):
    """Return primary control theme. Falls back to 'Process & Operations' if no match.
    Matches against name AND description, but with a 2x weight on the name —
    rules that match the name take priority over those that match only the description.
    """
    name_lower = name.lower()
    full_lower = (name + " " + description).lower()

    # First pass: try to match on name only
    for keywords, theme in THEME_RULES:
        if any(_kw_in(name_lower, kw) for kw in keywords):
            return theme
    # Second pass: fall through to description if name didn't match
    for keywords, theme in THEME_RULES:
        if any(_kw_in(full_lower, kw) for kw in keywords):
            return theme
    return "Process & Operations"


# ════════════════════════════════════════════════════════════════
# Theme definitions for the reference tab
# ════════════════════════════════════════════════════════════════

THEME_DEFINITIONS = [
    # (Group, Theme, Definition, Examples)
    ("Governance & Oversight", "Strategy & Planning",
     "Forward-looking controls that set direction, anticipate change, and align resources to strategy.",
     "Strategic plans, KPI dashboards, horizon scanning, scenario planning, capability roadmaps, capacity planning"),
    ("Governance & Oversight", "Governance & Reporting",
     "Board, executive committee, and audit committee oversight controls.",
     "Board endorsement, executive committees, ALCO, audit committee reporting, ministerial briefings"),
    ("Governance & Oversight", "Policy & Framework",
     "Documented policies, frameworks, codes of conduct, and management systems.",
     "Code of conduct, policy frameworks, ISMS, OHSMS, EMS, treasury policy, ABC policy"),
    ("Governance & Oversight", "Limits & Authorisations",
     "Delegation matrices, approval thresholds, segregation of duties, position limits.",
     "SoD framework, authority matrix, delegated approvals, position limits, VaR limits"),
    ("Governance & Oversight", "Risk Assessment",
     "Identification, analysis, and prioritisation of risks and controls.",
     "Risk assessments, BIA, scenario analysis, stress testing, vulnerability assessment, HIRA"),

    ("Prevention", "Access & Identity Management",
     "Controls over who can access what — across systems, data, and physical assets.",
     "IAM, MFA, privileged access, JML process, user access reviews, PAM"),
    ("Prevention", "Due Diligence & Onboarding",
     "Risk-based screening of customers, suppliers, employees, partners, and acquisitions before establishing the relationship.",
     "KYC/CDD, supplier DD, background checks, lateral hire DD, M&A DD, FPIC"),
    ("Prevention", "Training & Awareness",
     "Building knowledge, capability, and behavioural awareness in staff and partners.",
     "Mandatory training, phishing simulations, code attestation, role-based awareness"),
    ("Prevention", "Engineering & Configuration",
     "Technical controls baked into systems, infrastructure, and software.",
     "Secure SDLC, network segmentation, encryption, tokenisation, CSPM, multi-region architecture"),

    ("Detection", "Monitoring & Surveillance",
     "Continuous monitoring of systems, transactions, behaviour, and performance with alerting.",
     "SOC, SIEM, transaction monitoring, conduct surveillance, KPI dashboards, voice of customer"),
    ("Detection", "Reconciliation & Verification",
     "Independent verification of records, balances, transactions, and integrity.",
     "Reconciliations, three-way match, settlement verification, file integrity monitoring"),
    ("Detection", "Quality Reviews & Assurance",
     "Periodic review and assurance over outputs, processes, and control effectiveness.",
     "Peer reviews, file reviews, M&M reviews, internal audit, control testing"),
    ("Detection", "Reporting & Disclosure",
     "Production and submission of internal and external reports with quality assurance.",
     "Financial reporting, regulatory reporting, ESG disclosure, FATCA/CRS, complaint reporting"),

    ("Response", "Incident & Crisis Management",
     "Detection, escalation, and response to incidents and crises with stakeholder communication.",
     "Incident response, crisis playbooks, sentinel event response, open disclosure, recall"),
    ("Response", "Continuity & Recovery",
     "Maintaining critical operations through disruption and recovering when systems fail.",
     "BCM, disaster recovery, failover, backup, surge capacity, alternate sourcing"),
    ("Response", "Investigation & Remediation",
     "Investigating root cause, remediating the underlying issue, and embedding learnings.",
     "Fraud investigation, RCA, customer remediation, CAPA, post-incident review"),

    ("Stakeholder Engagement", "Customer & Beneficiary Management",
     "Understanding, supporting, and protecting customers / beneficiaries — particularly vulnerable groups.",
     "Customer success, complaint handling, vulnerable customer framework, co-design"),
    ("Stakeholder Engagement", "Stakeholder Engagement",
     "Engagement with external stakeholders — community, regulators, investors, suppliers, ministers.",
     "Community engagement, FPIC, regulator relationship, investor engagement"),
    ("Stakeholder Engagement", "People Management",
     "Workforce-side controls covering retention, succession, wellbeing, and culture.",
     "Succession planning, talent retention, engagement surveys, EVP, wellbeing programmes"),

    ("Specialised", "Modelling & Analytics",
     "Governance, validation, and monitoring of models, AI/ML systems, and analytics.",
     "Model risk management, ML lifecycle governance, AI ethics, bias testing, predictive maintenance"),

    ("Specialised", "Process & Operations",
     "Operational controls that don't fit other themes — typically standard operating procedures and process controls.",
     "SOPs, application controls, process performance metrics, incident logging"),
]
