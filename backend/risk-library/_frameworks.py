"""
Framework enrichment module
============================
Maps control names/themes to specific framework references using keyword detection.
Applied at render time over all 738 controls in the library.

Each rule:  (keywords_required, framework_string)
- keywords_required: list of keywords (lowercase) that MUST all appear in control name OR description
- The first matching rule wins (rules are ordered most-specific to most-general)
- If no rule matches and existing framework is non-empty, keep existing
- If no rule matches and existing framework is empty, leave empty
"""

# Ordered list of (keywords, framework_citation) — most specific FIRST
FRAMEWORK_RULES = [

    # ── CYBER / INFOSEC ──────────────────────────────────────────────────────
    (["mfa", "multi-factor"], "NIST 800-53 IA-2; ISO 27001 A.5.17; CIS 6.x"),
    (["identity", "access management"], "NIST 800-53 AC-2/AC-6; ISO 27001 A.5.15-A.5.18; CIS 5.x/6.x"),
    (["privileged access"], "NIST 800-53 AC-6; ISO 27001 A.8.2; CIS 5.x; SOC 2 CC6.1"),
    (["user access review", "user access certification", "uar"], "NIST 800-53 AC-2(j); SOX ITGC; SOC 2 CC6.2; ISO 27001 A.5.18"),
    (["least privilege"], "NIST 800-53 AC-6; ISO 27001 A.8.2; CIS 6.8"),
    (["vulnerability", "patch"], "NIST 800-53 RA-5/SI-2; ISO 27001 A.8.8; CIS 7.x"),
    (["soc", "security operations"], "NIST 800-53 AU-6/IR-4/SI-4; ISO 27001 A.8.16; SOC 2 CC7.2"),
    (["siem", "monitoring", "logging"], "NIST 800-53 AU-2/AU-6; ISO 27001 A.8.15-A.8.16; SOC 2 CC7.2"),
    (["incident response"], "NIST 800-53 IR-4/IR-8; ISO 27001 A.5.24-A.5.26; SOC 2 CC7.3"),
    (["isms", "information security management"], "ISO 27001:2022; NIST CSF; SOC 2 CC1.x"),
    (["pam", "privileged access management"], "NIST 800-53 AC-6; ISO 27001 A.8.2; CIS 5.x"),
    (["cspm", "cloud security posture"], "CIS Benchmarks; NIST 800-53 CM-6/CM-7; ISO 27001 A.5.23"),
    (["pci", "pci-dss"], "PCI DSS 4.0"),
    (["secure software", "ssdlc", "sdlc"], "OWASP SAMM; NIST SSDF (SP 800-218); ISO 27001 A.8.25-A.8.28"),
    (["network segmentation", "purdue"], "IEC 62443; NIST 800-53 SC-7; CIS 12.x; PCI DSS 1.x"),
    (["ot", "ics"], "IEC 62443; NIST 800-82"),
    (["medical device cyber"], "FDA Premarket Cyber; TGA Medical Device Cyber; IEC 81001-5-1"),
    (["ddos", "waf"], "NIST 800-53 SC-5/SC-7; CIS 12.x; OWASP"),
    (["phishing", "awareness"], "ISO 27001 A.6.3; NIST 800-53 AT-2; CIS 14.x"),
    (["payment data", "tokenisation"], "PCI DSS 3.x/4.0; NIST 800-53 SC-28"),
    (["authentication", "fraud prevention"], "PSD2 SCA; FFIEC; NIST 800-63"),

    # ── DATA / PRIVACY ───────────────────────────────────────────────────────
    (["data classification"], "ISO 27001 A.5.12-A.5.13; NIST 800-60; NIST 800-53 RA-2"),
    (["data loss prevention", "dlp"], "ISO 27001 A.8.12; NIST 800-53 SI-4(18); CIS 3.13"),
    (["backup", "recovery"], "ISO 27001 A.8.13; NIST 800-53 CP-9/CP-10; CIS 11.x; SOC 2 A1.2"),
    (["privacy by design", "impact assessment", "pia"], "GDPR Art. 25/35; ISO 27701; Privacy Act (AU) APP 1"),
    (["encryption", "cryptographic"], "NIST 800-53 SC-13; ISO 27001 A.8.24; PCI DSS 3.x; CIS 3.x"),
    (["secrets management"], "NIST 800-53 IA-5; CIS 4.x; OWASP Secrets"),
    (["data lineage", "data quality"], "BCBS 239; DAMA-DMBOK; ISO/IEC 25012"),
    (["bcbs 239", "risk data aggregation"], "BCBS 239"),
    (["master data", "mdm"], "DAMA-DMBOK; ISO 8000"),
    (["data governance"], "DAMA-DMBOK; DCAM; ISO/IEC 38505"),
    (["data subject", "dsar"], "GDPR Art. 12-22; CCPA §1798.100-130; Privacy Act APP 12-13"),
    (["phi", "patient health"], "HIPAA Security Rule; Privacy Act APP 6/11; HL7"),
    (["consent management"], "GDPR Art. 7; CCPA §1798.120; Privacy Act APP 3"),

    # ── FINANCIAL CRIME ──────────────────────────────────────────────────────
    (["aml", "ctf", "money laundering"], "FATF Recs 1, 10-21; AML/CTF Act; Wolfsberg"),
    (["customer due diligence", "cdd", "kyc"], "FATF Recs 10-12; AML/CTF Rules; Wolfsberg CDD"),
    (["sanctions screening"], "OFAC; UN; DFAT; OFSI; EU Restrictive Measures"),
    (["suspicious activity", "sar", "smr"], "FATF Rec 20; AUSTRAC; FinCEN; FCA SYSC 6"),
    (["transaction monitoring"], "FATF Rec 20; BCBS Sound Management of AML"),
    (["pep", "politically exposed"], "FATF Rec 12; Wolfsberg PEP; FCA FCG"),
    (["bribery", "abc", "anti-bribery"], "ISO 37001; FCPA; UK Bribery Act 2010; OECD Anti-Bribery"),
    (["fraud risk assessment"], "ACFE; COSO Fraud Risk Mgmt Guide; AICPA"),
    (["external fraud", "fraud detection"], "ACFE; COSO Fraud Risk Mgmt Guide"),

    # ── COMPLIANCE / REGULATORY ──────────────────────────────────────────────
    (["compliance management", "iso 37301"], "ISO 37301; ASIC RG 271/274"),
    (["whistleblower", "speak-up", "protected disclosure"], "ISO 37002; SOX §806; Corporations Act Pt 9.4AAA"),
    (["code of conduct", "behavioural standards"], "ISO 37301; SOX entity-level; COSO 2013 P1/P5"),
    (["regulatory horizon", "regulatory change"], "ISO 37301 §6.1.3; APRA CPS 220"),
    (["conduct framework", "conduct risk"], "FCA Consumer Duty; APRA CPS 511; ASIC RG 271"),
    (["vulnerable customer"], "FCA FG21/1; ASIC RG 271; Banking Code of Practice"),
    (["product governance"], "FCA PROD; MiFID II; ASIC RG 274; ISO 31000"),
    (["smcr", "bear", "senior manager"], "FCA SMCR; APRA BEAR/FAR"),
    (["royal commission", "inquiry"], "Hayne RC; ASIC / APRA expectations"),
    (["complaints", "idr", "edr"], "ASIC RG 271; AFCA; ISO 10002; FCA DISP"),

    # ── COSO / SOX / FINANCIAL CONTROLS ──────────────────────────────────────
    (["segregation of duties", "sod"], "COSO 2013 P10/P12; SOX ITGC; NIST 800-53 AC-5"),
    (["authority matrix", "delegation of authority", "delegated approval"], "COSO 2013 P10; SOX delegated authority"),
    (["reconciliation", "settlement verification"], "COSO 2013 P10/P14; SOX financial close"),
    (["three-way match", "po"], "COSO 2013 P10; SOX ITAC; PCAOB AS 2201"),
    (["journal entry", "manual je"], "COSO 2013 P10/P14; SOX ITAC; PCAOB AS 2201"),
    (["period-end close", "close checklist"], "COSO 2013 P10; SOX financial close"),
    (["management review", "management oversight"], "COSO 2013 P10/P16; SOX entity-level"),
    (["change management"], "COBIT BAI06; SOX ITGC; NIST 800-53 CM-3; SOC 2 CC8.1"),
    (["change advisory", "cab"], "COBIT BAI06; ITIL Change Enablement; SOC 2 CC8.1"),
    (["financial reporting", "external reporting"], "SOX §302/§404; PCAOB AS 2201; COSO 2013"),

    # ── REPORTING / TAX ──────────────────────────────────────────────────────
    (["fatca", "crs"], "FATCA; OECD CRS; ATO/HMRC tax reporting"),
    (["tax compliance"], "OECD BEPS; ATO Tax Risk Mgmt; ISA 240"),
    (["pillar two", "transfer pricing"], "OECD BEPS Pillar Two; OECD TP Guidelines"),
    (["revenue recognition", "asc 606", "ifrs 15"], "ASC 606; IFRS 15; PCAOB AS 2201"),
    (["asset valuation"], "IFRS 13; IAS 36; PCAOB AS 2201"),

    # ── OPERATIONAL / BCM ────────────────────────────────────────────────────
    (["business continuity", "bcms", "bcm"], "ISO 22301; NIST 800-53 CP-2; SOC 2 A1.2; APRA CPS 230"),
    (["business impact analysis", "bia"], "ISO 22301 §8.2.2; NIST 800-53 CP-2; APRA CPS 230"),
    (["important business service", "ibs", "impact tolerance"], "APRA CPS 230; FCA/PRA SS1/21; EU DORA"),
    (["disaster recovery", "dr"], "ISO 27031; NIST 800-53 CP-9/CP-10; SOC 2 A1.2"),
    (["crisis management"], "ISO 22361; ISO 22301"),
    (["operational resilience"], "APRA CPS 230; FCA/PRA SS1/21; EU DORA; BCBS BCP"),

    # ── HEALTH & SAFETY ──────────────────────────────────────────────────────
    (["ohsms", "occupational health and safety", "iso 45001"], "ISO 45001; AS/NZS 4801; OHSAS 18001"),
    (["hazard identification", "risk assessment", "hira"], "ISO 45001 §6.1.2; ISO 31000"),
    (["psychosocial"], "ISO 45003; Code of Practice (AU)"),
    (["critical risk", "fatality prevention", "icmm"], "ICMM Critical Control Mgmt; ISO 45001"),
    (["permit to work", "high-risk task"], "ISO 45001 §8.1.2; ICMM Critical Control"),
    (["process safety", "psm"], "ISO 45001; OSHA PSM 29 CFR 1910.119; CCPS"),
    (["safeguarding", "vulnerable beneficiary"], "Royal Commission (AU) recommendations; UK Care Act 2014"),
    (["medication safety", "barcode"], "WHO Patient Safety; ACSQHC NSQHS Std 4"),
    (["never-event", "patient safety"], "WHO Patient Safety; ACSQHC NSQHS"),

    # ── ENVIRONMENTAL ────────────────────────────────────────────────────────
    (["environmental management system", "ems", "iso 14001"], "ISO 14001; EU EMAS"),
    (["climate", "tcfd", "issb", "asrs"], "TCFD; ISSB IFRS S1/S2; ASRS S1/S2"),
    (["scenario analysis", "ngfs"], "NGFS; APRA CPG 229; TCFD"),
    (["sbt", "science-based target", "decarbonisation"], "SBTi; TCFD; GHG Protocol"),
    (["modern slavery"], "AU Modern Slavery Act 2018; UK Modern Slavery Act 2015"),
    (["sustainability disclosure", "esg disclosure"], "TCFD; ISSB; ASRS; GRI; SASB"),
    (["greenwashing"], "ASIC INFO 271; ACCC greenwashing guidance"),
    (["food safety", "haccp"], "FSANZ; HACCP; ISO 22000"),

    # ── THIRD PARTY ──────────────────────────────────────────────────────────
    (["third-party", "third party", "vendor risk", "supplier risk"], "ISO 27036; ISO 31000; APRA CPS 230; SIG"),
    (["outsourcing"], "APRA CPS 231/230; FCA SYSC 8; EU DORA; BCBS Outsourcing"),
    (["supplier due diligence"], "ISO 27036; ISO 37001 (ABC supplier); SIG"),
    (["concentration risk"], "APRA CPS 230; EU DORA; BCBS Outsourcing"),
    (["exit plan", "transition"], "APRA CPS 230; FCA Op Res; EU DORA"),

    # ── GOVERNANCE / RISK / STRATEGY ────────────────────────────────────────
    (["risk management framework", "iso 31000", "erm"], "ISO 31000; COSO ERM 2017"),
    (["strategic planning", "strategic plan"], "ISO 31000 §6.4; COSO ERM"),
    (["governance framework", "board"], "ISO 37000; COSO ERM 2017; ASX CGC Principles"),
    (["risk appetite"], "COSO ERM 2017; ISO 31000; APRA CPS 220"),
    (["scenario planning", "scenario testing"], "ISO 31000; COSO ERM; APRA CPS 220"),

    # ── PEOPLE / HR ──────────────────────────────────────────────────────────
    (["pre-employment screening", "background check"], "ISO 27001 A.6.1; FCA F&P; APRA Fit & Proper"),
    (["sexual harassment", "respect@work"], "Sex Discrimination Act (AU); Respect@Work; Equality Act (UK)"),
    (["dei", "diversity"], "ASX CGC Principle 1.5; UK CG Code"),
    (["code of conduct", "ethics"], "ISO 37301; SOX entity-level; COSO 2013 P1"),
    (["culture survey"], "FCA Culture Pubs; APRA CPS 511"),

    # ── PROJECT / CHANGE ─────────────────────────────────────────────────────
    (["project governance", "stage gate"], "PMI PMBOK; PRINCE2; APM; ISO 21500"),
    (["benefits realisation"], "PMI Benefits Realization; APM Benefits Mgmt"),

    # ── MODEL / AI ───────────────────────────────────────────────────────────
    (["model risk management", "model validation", "model inventory"], "Fed SR 11-7; OCC 2011-12; PRA SS1/23; APRA CPS 113/231"),
    (["mlops", "ml lifecycle"], "Google MLOps; ISO/IEC 23053; ISO/IEC 42001"),
    (["ai ethics", "ai governance", "responsible ai"], "EU AI Act; NIST AI RMF; ISO/IEC 42001"),
    (["ai safety", "red-teaming", "harm scenarios"], "NIST AI RMF; EU AI Act; AISI evals"),
    (["bias testing", "fairness"], "NIST AI RMF; EU AI Act; ISO/IEC 24027"),
    (["clinical ai", "clinical decision support"], "TGA Medical Device SaMD; FDA AI/ML SaMD; IEC 82304"),

    # ── LEGAL ────────────────────────────────────────────────────────────────
    (["intellectual property", "ip register"], "WIPO; AU IP Act; UK IPO; USPTO"),
    (["litigation management"], "Solicitors regulation; PCAOB AS 2501 (litigation); ISO 31000"),
    (["contract management"], "ISO 44001; CIPS; IACCM"),

    # ── CIS / INFRASTRUCTURE ─────────────────────────────────────────────────
    (["asset inventory", "cmdb"], "CIS 1.x; NIST 800-53 CM-8; ISO 27001 A.5.9"),
    (["secure configuration", "cis benchmark"], "CIS 4.x; CIS Benchmarks; NIST 800-53 CM-2/CM-6"),
    (["file integrity", "fim"], "PCI DSS 11.5; CIS 8.x; NIST 800-53 SI-7"),

    # ── SOC 2 SPECIFIC ───────────────────────────────────────────────────────
    (["slo", "error budget"], "Google SRE; SOC 2 A1.x"),
    (["service availability", "sla"], "ISO/IEC 20000; ITIL; SOC 2 A1.x"),

    # ── BROADER CATCH-ALLS (lowest priority — last resort) ────────────────────
    # Strategic / governance
    (["strategic"], "ISO 31000; COSO ERM 2017"),
    (["kpi", "dashboard"], "ISO 31000; COSO ERM monitoring"),
    (["competitor", "intelligence"], "ISO 31000 §6.4; COSO ERM"),
    (["board", "executive committee"], "ISO 37000; COSO ERM 2017; ASX CGC"),
    (["portfolio review", "portfolio analysis"], "COSO ERM 2017; ISO 31000"),
    (["scenario"], "ISO 31000; COSO ERM"),
    (["m&a", "merger", "acquisition"], "ISO 31000; COSO ERM; ASX CGC"),
    (["due diligence"], "ISO 31000; ISO 37001 (ABC); COSO ERM"),
    (["stage gate", "stage-gate"], "PMI PMBOK; PRINCE2; ISO 21500"),
    (["benefits realisation", "benefits tracking"], "PMI Benefits Realization"),

    # Financial
    (["cash flow", "liquidity"], "ISO 31000; APRA APS 210; BCBS 248"),
    (["covenant"], "ISO 31000; BCBS"),
    (["treasury policy"], "ISO 31000; ASX CGC"),
    (["hedging", "fx exposure"], "IFRS 9 / IAS 39; ISO 31000"),
    (["alco"], "BCBS Sound Liquidity; APRA APS 210"),
    (["lcr", "nsfr"], "BCBS 248 / Basel III; APRA APS 210"),
    (["var", "value at risk", "market risk"], "Basel III FRTB; APRA APS 116"),
    (["irrbb", "interest rate risk"], "BCBS 368 IRRBB"),

    # Customer / market
    (["customer concentration", "customer health"], "ISO 31000; COSO ERM"),
    (["customer success", "nrr", "net revenue retention"], "ISO 31000"),
    (["customer feedback", "voice of customer", "nps"], "ISO 10002; FCA Consumer Duty"),
    (["complaint"], "ISO 10002; ASIC RG 271; AFCA; FCA DISP"),

    # People
    (["succession", "succession plan"], "ASX CGC Principle 1; APRA Fit & Proper"),
    (["talent", "engagement", "evp"], "ISO 30414; HRBP standards"),
    (["compensation", "remuneration"], "APRA CPS 511; FCA SYSC 19"),
    (["recruitment", "time-to-hire"], "ISO 30414"),
    (["mandatory leave"], "BCBS 162; FCA SYSC"),

    # Quality / process
    (["quality management", "qms"], "ISO 9001; ISO 9004"),
    (["sop", "standard operating"], "ISO 9001 §8; ISO 22301"),
    (["root cause", "rca"], "ISO 9001 §10; ISO 31000"),
    (["audit", "internal audit"], "IIA Standards; ISO 19011; SOX"),
    (["incident management"], "ITIL; ISO 20000; ISO 22301"),
    (["non-conformance", "capa"], "ISO 9001 §10; FDA 21 CFR 820"),
    (["statistical process control", "spc"], "ISO 9001; Six Sigma"),

    # Asset / maintenance / operations
    (["asset register", "asset management"], "ISO 55000; ISO 27001 A.5.9"),
    (["maintenance"], "ISO 55000; ISO 9001"),
    (["redundancy", "failover"], "ISO 22301; NIST 800-53 CP-9; SOC 2 A1.2"),
    (["spare parts", "inventory"], "ISO 55000"),

    # Capacity / workforce
    (["demand forecasting", "capacity planning"], "ITIL Capacity Mgmt; ISO 9001"),
    (["workforce management", "rostering"], "ISO 30414; Modern Awards (AU)"),

    # Reputation
    (["reputation", "sentiment", "media monitoring"], "ISO 22361; ISO 31000"),
    (["spokesperson", "media training"], "ISO 22361"),
    (["stakeholder engagement"], "AA1000SES; UN Guiding Principles"),
    (["co-design", "lived experience"], "AA1000SES; ISO 26000"),

    # Environmental / community
    (["community", "stakeholder mapping"], "AA1000SES; ISO 26000; UN Guiding Principles"),
    (["fpic", "free, prior, and informed consent"], "UNDRIP; UN Guiding Principles"),
    (["indigenous", "first nations", "ilua"], "UNDRIP; AU Native Title Act; ISO 26000"),
    (["social impact"], "ISO 26000; AA1000"),

    # Regulator engagement
    (["regulator", "regulator engagement"], "ISO 37301; APRA CPS 220"),
    (["licence", "licensing"], "ISO 37301; sector licensing regimes"),

    # Litigation / contract
    (["contract"], "ISO 44001; CIPS"),
    (["insurance"], "ISO 31000; ASX CGC"),
    (["litigation"], "PCAOB AS 2501; ISO 31000"),

    # Generic fallbacks (lowest priority)
    (["governance"], "ISO 37000; ISO 31000"),
    (["framework", "policy"], "ISO 31000"),
    (["training"], "ISO 27001 A.6.3; ISO 9001 §7.2; ISO 45001 §7.2"),
    (["awareness"], "ISO 27001 A.6.3; ISO 9001 §7.3"),
    (["oversight"], "ISO 31000 §6.6; COSO 2013 P16-P17"),
    (["approval matrix", "approval workflow", "review and approval"], "COSO 2013 P10/P14"),

    # Final catch-all — broad business / industry-specific controls
    (["analytics", "analysis", "segmentation"], "ISO 31000; COSO ERM (industry-specific best practice)"),
    (["pipeline", "roadmap"], "ISO 31000; COSO ERM"),
    (["partner", "relationship", "engagement"], "ISO 31000; AA1000SES (industry-specific best practice)"),
    (["validation", "verification"], "ISO 9001 §8; ISO 31000"),
    (["cycle", "lifecycle"], "ISO 9001; ISO 55000; ITIL"),
    (["programme", "program"], "PMI PMBOK; ISO 21500; ISO 31000"),
    (["transformation", "change"], "PMI; PRINCE2; ISO 21500"),
    (["capability", "capability uplift"], "COSO ERM; ISO 31000"),
    (["alignment", "integration"], "ISO 31000; COSO ERM"),
    (["measurement", "tracking", "metrics"], "ISO 31000 §6.6; COSO 2013 P16"),
    (["protection", "safeguard"], "ISO 31000; ISO 27001"),
]


import re

def _kw_in(haystack, kw):
    """Word-boundary match — requires kw to appear as a whole word/phrase, not as a substring."""
    if " " in kw or "-" in kw:
        # Multi-word keywords: substring match is fine (already specific)
        return kw in haystack
    # Single word: require word boundary
    return re.search(r'\b' + re.escape(kw) + r'\b', haystack) is not None


def enrich_framework(name, description, current_framework):
    """Apply keyword rules to enrich the framework citation.
    Matching: ANY keyword in a rule matches the rule.
    First matching rule wins (rules ordered specific to general).
    Single-word keywords use word-boundary matching to prevent substring false positives.
    """
    haystack = (name + " " + description).lower()
    for keywords, framework in FRAMEWORK_RULES:
        if any(_kw_in(haystack, kw) for kw in keywords):
            # If existing framework already has specific section IDs, prefer existing
            if current_framework and len(current_framework) > len(framework) * 0.7 and any(c.isdigit() for c in current_framework):
                return current_framework
            return framework
    return current_framework
