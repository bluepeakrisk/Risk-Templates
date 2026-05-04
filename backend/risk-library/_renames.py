"""
Rename map — applies "[Document] governance and monitoring" pattern.
Maps OLD control name → (NEW control name, optional NEW description).
If new description is None, original description is retained.

The principle: a policy / framework / standard / code is a document.
The CONTROL is the management of, monitoring of, and adherence to those documents.
"""

# Format: old_name: (new_name, new_description_or_None)
RENAME_MAP = {

    # ── R-001 ──
    "Innovation budget and experimentation framework": (
        "Innovation portfolio governance and experimentation oversight",
        "Documented innovation budget and experimentation framework with governance over portfolio allocation, periodic review of pipeline progress, and outcomes assessment of experiments against hypotheses."
    ),

    # ── R-003 ──
    "M&A / partnership governance framework": (
        "M&A and partnership governance and oversight",
        "Defined M&A and partnership governance with investment committee approval, deal-stage gating, post-deal performance reviews, and reporting to the board on portfolio outcomes."
    ),

    # ── R-004 ──
    "Treasury policy and liquidity risk appetite": (
        "Treasury policy governance and liquidity appetite monitoring",
        "Documented treasury policy and liquidity risk appetite with periodic board approval, monitoring of position against appetite, breach escalation, and annual policy review."
    ),

    # ── R-005 ──
    "Long-term framework and offtake agreements": (
        "Long-term agreement governance and offtake monitoring",
        "Documented long-term contract and offtake agreement framework with execution governance, ongoing performance monitoring, and renewal / renegotiation tracking."
    ),

    # ── R-006 ──
    "Segregation of duties (SoD) framework": (
        "Segregation of duties enforcement and conflict review",
        "Documented SoD framework with enforcement through system controls, periodic conflict matrix review, and exception monitoring with management approval."
    ),
    "Whistleblower hotline and protected disclosure framework": (
        "Whistleblower programme governance and case management",
        "Operated whistleblower hotline with protected disclosure governance, independent investigation of reports, case management, board reporting on themes, and policy review."
    ),
    "Mandatory leave / vacation policy enforcement": (
        "Mandatory leave compliance monitoring and enforcement",
        "Monitoring of mandatory leave / vacation compliance for sensitive roles with HR oversight, exception escalation, and annual policy review."
    ),

    # ── R-007 ──
    "Treasury policy with hedging mandate": (
        "Treasury policy governance and hedging mandate compliance",
        "Documented treasury policy with hedging mandate, periodic compliance monitoring, breach escalation, and board-approved policy review."
    ),
    "Market risk identification and quantification framework": (
        "Market risk identification and exposure quantification programme",
        "Operated market risk identification programme covering FX, IR, and commodity exposures with periodic measurement, sensitivity testing, and exposure reporting."
    ),
    "Layered FX hedging policy": (
        "FX hedging policy compliance and effectiveness monitoring",
        "Layered FX hedging policy with execution oversight, hedge effectiveness testing, exposure-vs-hedge monitoring, and quarterly policy review."
    ),

    # ── R-008 ──
    "Service delivery quality framework": (
        "Service delivery quality standards monitoring and review",
        "Documented service delivery quality standards with performance monitoring, quality review cycles, customer outcome tracking, and continuous improvement."
    ),

    # ── R-010 ──
    "Service level agreements and prioritisation framework": (
        "SLA management and prioritisation governance",
        "Documented SLA framework with performance tracking against commitments, prioritisation governance for capacity allocation, and breach escalation."
    ),

    # ── R-011 ──
    "Service quality standards and outcomes measurement": (
        "Service quality standards monitoring and outcomes review",
        "Operated service quality standards with continuous outcome measurement, periodic review of trends, and corrective action on substandard performance."
    ),

    # ── R-012 ──
    "Key person risk policy and accountability framework": (
        "Key person risk policy compliance and accountability monitoring",
        "Documented key person risk policy with periodic identification of key personnel, succession plan compliance, knowledge management oversight, and accountability reporting."
    ),

    # ── R-013 ──
    "Workforce planning and HR governance framework": (
        "Workforce planning execution and HR governance oversight",
        "Documented workforce planning and HR governance with annual capability planning, quarterly talent reviews, capability gap closure tracking, and board reporting on talent risks."
    ),
    "Hybrid working and flexibility framework": (
        "Hybrid working policy compliance and effectiveness review",
        "Documented hybrid working framework with team-level compliance monitoring, periodic effectiveness review against productivity and engagement metrics, and policy refresh."
    ),

    # ── R-014 ──
    "Code of conduct and behavioural standards": (
        "Code of conduct attestation and behavioural standards monitoring",
        "Annual attestation against code of conduct and behavioural standards with breach investigation, consistent consequences, and culture monitoring."
    ),
    "Partner-level conduct framework": (
        "Partner-level conduct standards monitoring and accountability",
        "Documented partner conduct standards with peer review, conduct surveillance, partner-level performance assessment integrating conduct, and accountability for breaches."
    ),
    "Conduct risk framework and surveillance": (
        "Conduct risk surveillance and breach review",
        "Operated conduct risk framework with continuous surveillance, behavioural risk indicator monitoring, breach investigation, and quarterly executive review."
    ),
    "FIFO / remote site cultural standards": (
        "FIFO and remote-site cultural standards monitoring and review",
        "Documented FIFO / remote-site cultural standards with site-level compliance monitoring, periodic cultural climate surveys, and intervention tracking."
    ),

    # ── R-016 ──
    "Data classification and handling policy": (
        "Data classification policy compliance and handling oversight",
        "Documented data classification and handling policy with classification coverage monitoring, periodic handling-control validation, and policy review."
    ),
    "Data protection policy and privacy framework": (
        "Data protection policy governance and privacy oversight",
        "Documented data protection and privacy framework with periodic policy review, privacy incident monitoring, individual rights handling oversight, and compliance attestation."
    ),

    # ── R-019 ──
    "Conduct framework with Senior Manager accountability": (
        "Senior Manager conduct accountability and certification",
        "SMCR / FAR-style conduct accountability with documented Statements of Responsibility, fit-and-proper attestation, breach assessment against responsibilities, and consequence application."
    ),
    "Climate disclosure and ESG advisory standards": (
        "Climate and ESG disclosure compliance and advisory governance",
        "Documented climate / ESG disclosure standards with compliance assurance over published statements, ESG advisory engagement governance, and disclosure refresh."
    ),
    "Vulnerable customer framework": (
        "Vulnerable customer framework compliance and outcomes monitoring",
        "Operated vulnerable customer framework with identification compliance monitoring, outcome tracking for vulnerable customers, complaints surveillance, and periodic policy review."
    ),
    "Ethical investment and lending policies": (
        "Ethical investment / lending policy compliance and exclusion monitoring",
        "Documented ethical investment / lending policies with exclusion list monitoring, sector limit compliance, human rights due diligence oversight, and policy refresh."
    ),

    # ── R-020 ──
    "Premises and product safety standards": (
        "Premises and product safety standards compliance monitoring",
        "Documented premises and product safety standards with continuous compliance monitoring, customer-facing communication assurance, and incident-driven standards review."
    ),

    # ── R-025 ──
    "Safeguarding framework for vulnerable beneficiaries": (
        "Safeguarding programme governance and case oversight",
        "Documented safeguarding framework with screening compliance monitoring, training completion tracking, supervision assurance, safeguarding case oversight, and reporting to the board."
    ),

    # ── R-028 ──
    "Project / programme governance framework": (
        "Project / programme governance and steering oversight",
        "Documented project governance with steering committee participation, decision rights enforcement, escalation oversight, and ExCo / board reporting on material programmes."
    ),
    "Programme and policy implementation governance": (
        "Programme implementation governance and outcomes review",
        "Operated programme governance covering implementation milestones, benefits realisation tracking, risk management, and post-implementation review."
    ),

    # ── R-030 ──
    "Outsourcing policy and material outsourcing framework": (
        "Outsourcing policy compliance and material arrangement monitoring",
        "Board-approved outsourcing policy with monitoring of material arrangement register, governance compliance assurance, due-diligence completion oversight, and exit-readiness verification."
    ),

    # ── R-031 ──
    "Customer experience and retention framework": (
        "Customer experience standards and retention outcomes monitoring",
        "Documented customer experience and retention framework with journey ownership accountability, voice-of-customer integration, retention KPI monitoring, and executive review."
    ),

    # ── R-032 ──
    "Reserves policy and counter-cyclical capacity": (
        "Reserves policy compliance and counter-cyclical readiness monitoring",
        "Documented reserves policy with periodic monitoring of reserves against minimum levels, counter-cyclical capacity readiness assessment, and board approval of releases."
    ),

    # ── R-033 ──
    "AML/CTF policy and programme framework": (
        "AML/CTF programme governance and effectiveness review",
        "Board-approved AML/CTF policy and programme with periodic effectiveness review, risk-based programme calibration, regulator interaction oversight, and annual MLRO attestation."
    ),

    # ── R-034 ──
    "Anti-bribery and corruption (ABC) policy and code of conduct": (
        "ABC policy attestation and code of conduct compliance monitoring",
        "Documented ABC policy and code of conduct with annual attestation, gift / hospitality register monitoring, conflict of interest review, breach investigation, and policy refresh."
    ),
    "ICAC-compliant integrity framework": (
        "Integrity framework governance and ICAC-aligned reporting",
        "Operated integrity framework aligned to ICAC / corruption commission expectations with case oversight, investigation governance, ICAC referral compliance, and consequence application."
    ),

    # ── R-037 ──
    "Conduct risk framework with clear standards": (
        "Conduct standards monitoring and outcomes review",
        "Documented conduct standards with continuous behavioural surveillance, customer outcome testing, conduct dashboard review, and policy refresh on emerging risks."
    ),
    "Vulnerable customer / consumer framework": (
        "Vulnerable customer framework compliance and journey oversight",
        "Operated vulnerable customer framework with identification compliance, tailored journey oversight, vulnerable-customer outcome testing, and complaints surveillance."
    ),

    # ── R-038 ──
    "Tax compliance framework": (
        "Tax compliance framework governance and filing oversight",
        "Documented tax compliance framework covering income, GST/VAT, payroll, and digital taxes with filing oversight, position documentation review, and ATO/HMRC interaction governance."
    ),

    # ── R-039 ──
    "Data engineering standards and pipeline integrity": (
        "Data engineering standards compliance and pipeline integrity monitoring",
        "Documented data engineering standards covering schema enforcement and contract testing with continuous pipeline integrity monitoring, lineage capture verification, and standards review."
    ),

    # ── R-040 ──
    "AI / model engineering standards and reproducibility": (
        "AI engineering standards compliance and reproducibility verification",
        "Documented AI / ML engineering standards with reproducibility verification on releases, deployment-gate compliance monitoring, observability instrumentation review, and standards refresh."
    ),
    "Generative AI usage policy and matter safeguards": (
        "Generative AI usage policy compliance and matter safeguard monitoring",
        "Documented GenAI usage policy with matter-level compliance monitoring, output verification on AI-assisted work, client disclosure compliance, and policy refresh as tools evolve."
    ),

}


def apply_renames(controls_dict):
    """Apply rename map to all universal and industry controls in place.
    Returns count of controls renamed."""
    renamed = 0
    for tid, theme in controls_dict.items():
        # Universal
        new_universal = []
        for ctl in theme["universal"]:
            if ctl["name"] in RENAME_MAP:
                new_name, new_desc = RENAME_MAP[ctl["name"]]
                ctl = {**ctl, "name": new_name}
                if new_desc:
                    ctl["description"] = new_desc
                renamed += 1
            new_universal.append(ctl)
        theme["universal"] = new_universal
        # Industry
        for code, ctl_list in theme["industry"].items():
            new_ind = []
            for ctl in ctl_list:
                if ctl["name"] in RENAME_MAP:
                    new_name, new_desc = RENAME_MAP[ctl["name"]]
                    ctl = {**ctl, "name": new_name}
                    if new_desc:
                        ctl["description"] = new_desc
                    renamed += 1
                new_ind.append(ctl)
            theme["industry"][code] = new_ind
    return renamed
