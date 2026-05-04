"""
Batch 9 — Final polish gap-fills for the few genuinely missing themes
identified after classification rules were tightened.
"""
from risk_controls import C

POLISH_CONTROLS = {

# ── R-004 missing Limits & Authorisations ──
"R-004": [
    C("Funding and treasury authority limits",
      "Preventive", "Manual",
      "Documented authority limits for treasury, borrowing, hedging, and material payments with dual approval thresholds and escalation to the board for transactions above appetite.",
      "Per transaction + Annual review",
      "Treasurer / CFO",
      "Limit breaches; out-of-authority events; dual-approval compliance",
      "COSO 2013 P10; ASX CGC Principles"),
],

# ── R-005 missing Limits & Authorisations ──
"R-005": [
    C("Customer concentration limits and exposure cap",
      "Preventive", "Hybrid",
      "Documented concentration limits (single customer, sector, geography) with monitoring against thresholds, escalation on breach, and acceptance / mitigation governance.",
      "Continuous + Quarterly review",
      "Chief Commercial Officer / CRO",
      "Limit breaches; exposure vs cap; acceptance / mitigation actions closed",
      "ISO 31000; COSO ERM 2017"),
],

# ── R-007 missing Reconciliation & Verification ──
"R-007": [
    C("Hedge accounting and exposure reconciliation",
      "Detective", "Hybrid",
      "Periodic reconciliation between underlying exposures, hedge instruments, and hedge accounting positions with effectiveness testing and documentation.",
      "Per cycle + Quarterly effectiveness test",
      "Treasurer / Financial Controller",
      "Reconciliation breaks; effectiveness test pass rate; documentation completeness",
      "IFRS 9 / IAS 39; ASC 815"),
],

# ── R-010 missing Quality Reviews & Assurance ──
"R-010": [
    C("Capacity assurance review and audit",
      "Detective", "Manual",
      "Periodic assurance review over capacity management practices including forecast accuracy, planning discipline, and control effectiveness with findings tracked to closure.",
      "Annually",
      "Internal Audit / Operations",
      "Audit findings; finding closure; capacity management maturity",
      "IIA Standards; ITIL Capacity Mgmt"),
],

# ── R-011 missing Continuity & Recovery ──
"R-011": [
    C("Quality continuity and product alternative arrangements",
      "Corrective", "Hybrid",
      "Continuity arrangements for quality-critical processes including alternative suppliers, redundant testing capability, and rapid switchover procedures.",
      "Continuous + Annual testing",
      "Quality Manager / Supply Chain",
      "Continuity tests passed; alternative arrangements active; switchover time",
      "ISO 22301; ISO 9001 §8.4"),
],

# ── R-012 missing Policy & Framework ──
"R-012": [
    C("Key person risk policy and accountability framework",
      "Directive", "Manual",
      "Documented policy on key person risk including identification criteria, succession requirements, knowledge management obligations, and accountability for material risks.",
      "Continuous + Annual review",
      "CHRO / CEO",
      "Policy attestation; key person register currency; coverage of identified roles",
      "ASX CGC Principle 1; APRA Fit & Proper"),
],

# ── R-029 missing Due Diligence & Onboarding ──
"R-029": [
    C("Third-party due diligence and onboarding gates",
      "Preventive", "Hybrid",
      "Risk-based due diligence at onboarding covering financial health, security posture, sanctions, ESG, and regulatory compliance with onboarding gates and risk acceptance governance.",
      "Per onboarding",
      "Vendor Risk / Procurement",
      "DD completion rate; gate failures; risk acceptance volume; rejected onboardings",
      "ISO 27036; APRA CPS 230; SIG"),
],

# ── R-036 missing Quality Reviews & Assurance ──
"R-036": [
    C("BCMS audit and assurance programme",
      "Detective", "Manual",
      "Independent assurance over BCMS effectiveness covering policy compliance, plan adequacy, exercise outcomes, and continuous improvement with findings tracked to closure.",
      "Annually",
      "Internal Audit",
      "Audit findings; finding closure; BCMS maturity scores",
      "IIA Standards; ISO 22301 §9.2"),
],

}
