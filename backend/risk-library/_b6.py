"""Batch 6 — gap-fill controls identified from ORX Reference Control Library completeness review.
These are paraphrased and adapted to align with our existing voice and structure.
Each entry adds a new universal control to a theme that lacks coverage of a specific ORX category.
"""
from risk_controls import C

# Each entry: theme_id -> list of additional universal controls to add
GAP_FILL_CONTROLS = {

# ── R-006 Internal fraud — Hiring processes, Verifications & reconciliations ──
"R-006": [
    C("Pre-employment screening and ongoing fitness checks",
      "Preventive", "Hybrid",
      "Background checks (criminal, credit, regulatory, reference, qualifications) at hiring, with periodic re-screening for sensitive roles and event-driven reviews on role changes.",
      "Per appointment + Periodic refresh",
      "CHRO / Compliance",
      "Screening completion rate; adverse findings; refresh aging on sensitive roles",
      "ISO 27001 A.6.1 / FCA F&P"),
    C("Independent reconciliations and settlement verification",
      "Detective", "Hybrid",
      "Independent reconciliation of accounts, settlements, and inter-system balances by personnel separated from origination, with break investigation and aged-break management.",
      "Daily / Weekly / Per cycle",
      "Financial Controller / Internal Audit",
      "Aged breaks; reconciliation completion; break investigation cycle time",
      "COSO Internal Control"),
],

# ── R-013 Talent — Governance frameworks (HR governance) ──
"R-013": [
    C("Workforce planning and HR governance framework",
      "Directive", "Manual",
      "Documented HR governance covering workforce planning, capability strategy, succession, and people-risk reporting to executive and board with annual capability review.",
      "Annually + Quarterly reporting",
      "CHRO / Board People Committee",
      "Workforce plan delivery; capability gap closure; board attestation",
      ""),
],

# ── R-014 Culture / conduct — Reviews & approvals (people-related) ──
"R-014": [
    C("People decision review and approval framework",
      "Preventive", "Manual",
      "Multi-eye review and approval framework for sensitive people decisions (terminations, settlements, NDAs, performance escalations) with HR partnership and consistency assurance.",
      "Per decision",
      "CHRO / GC",
      "Decisions reviewed; consistency findings; consequence equity",
      ""),
],

# ── R-015 Cyber — Resilience mechanism implementation ──
"R-015": [
    C("Cyber resilience mechanisms and recovery testing",
      "Corrective", "Hybrid",
      "Implementation and regular testing of cyber resilience mechanisms (immutable backups, isolated recovery environments, manual workarounds) ensuring recovery from destructive cyber events.",
      "Continuous + Quarterly testing",
      "CISO / Head of Infrastructure",
      "Recovery tests passed; immutable backup coverage; manual workaround readiness",
      "NIST CSF RC / ISO 27031"),
],

# ── R-016 Data — Verification & validation of data handling ──
"R-016": [
    C("Periodic data handling validation and access review",
      "Detective", "Hybrid",
      "Periodic validation of data handling controls (encryption posture, access appropriateness, retention adherence) with sample testing and remediation tracking.",
      "Quarterly",
      "Privacy Officer / Internal Audit",
      "Validation completion; control failure rate; remediation closure cycle",
      "ISO 27001 A.18 / NIST 800-53 AU"),
],

# ── R-019 Compliance — Reviews & approvals; License/cert/accreditation verification ──
"R-019": [
    C("Licence, certification, and accreditation verification",
      "Preventive", "Hybrid",
      "Centralised register of licences, certifications, and accreditations required to operate, with renewal calendars, condition tracking, and verification of staff qualifications where applicable.",
      "Continuous + Per renewal",
      "Chief Compliance Officer",
      "Licence currency; renewal lead time; conditions met; staff credential verification",
      ""),
],

# ── R-020 Legal — IP protection; Reviews & approvals; Training & awareness ──
"R-020": [
    C("Intellectual property protection and IP register",
      "Preventive", "Hybrid",
      "IP register covering trademarks, patents, copyrights, and trade secrets with renewal tracking, infringement monitoring, and protection actions including employee assignment agreements.",
      "Continuous + Annual review",
      "GC / Head of IP",
      "IP register completeness; renewal compliance; infringement actions; assignment coverage",
      ""),
    C("Legal and contract awareness training",
      "Preventive", "Hybrid",
      "Targeted legal awareness training for commercial, sales, and operational staff on contracting, liability, IP, and dispute escalation triggers, with refresher cycles.",
      "Annually + Onboarding",
      "GC / L&D",
      "Training completion; assessment scores; legal escalation accuracy",
      ""),
],

# ── R-026 Workplace injury — Reviews & approvals (safety governance) ──
"R-026": [
    C("Safety governance, leadership commitment, and review",
      "Directive", "Manual",
      "Board and executive-level safety governance with documented commitment, periodic safety performance review, and visible leadership engagement on critical risks and incidents.",
      "Continuous + Quarterly board review",
      "CEO / Board / Chief Safety Officer",
      "Board safety review participation; leadership site engagement; critical risk attestation",
      "ISO 45001 §5"),
],

# ── R-029 Third party — Risk assessments (third-party-specific); Training & awareness ──
"R-029": [
    C("Third-party risk assessment and tiering",
      "Preventive", "Hybrid",
      "Risk-based assessment of third parties at onboarding and periodically, considering criticality, data access, geography, and substitutability, with risk tier driving DD depth and oversight.",
      "Per onboarding + Annual refresh",
      "Vendor Risk / Procurement",
      "Tiering coverage; refresh aging; tier-driven oversight cadence",
      "ISO 27036 / SIG"),
    C("Third-party risk awareness training for relationship owners",
      "Preventive", "Hybrid",
      "Targeted training for business-side third-party relationship owners covering contract management, performance monitoring, and risk escalation responsibilities.",
      "Annually + Onboarding",
      "Vendor Management Office / L&D",
      "Training completion; escalation quality; relationship owner capability scores",
      ""),
],

# ── R-033 Financial Crime — Standards & policies; Reviews & approvals; Risk assessments; Verifications ──
"R-033": [
    C("Financial crime risk assessment and refresh",
      "Preventive", "Hybrid",
      "Enterprise-wide ML/TF/sanctions risk assessment covering customer, product, geography, and channel risk with annual refresh and event-driven updates feeding programme calibration.",
      "Annually + Event-driven",
      "MLRO / Chief Compliance Officer",
      "Risk assessment refresh; high-risk drivers; programme calibration",
      "FATF Rec 1 / Wolfsberg"),
    C("Senior management review and approval of high-risk decisions",
      "Preventive", "Manual",
      "Senior management review and approval of high-risk financial crime decisions including high-risk customer onboarding, alert closures above thresholds, and sanctions exception decisions.",
      "Per decision",
      "Senior Management / MLRO",
      "Decisions reviewed; rejection/approval rate; audit trail completeness",
      "FATF Rec 26"),
],

# ── R-035 External Fraud — Establishment of standards/policies; Risk assessments; Verifications ──
"R-035": [
    C("Customer and counterparty verification at high-risk events",
      "Preventive", "Hybrid",
      "Out-of-band verification (callback, biometric, document re-verification) on high-risk events including payment changes, large transactions, account changes, and credential resets.",
      "Per high-risk event",
      "Fraud Operations",
      "Verification compliance; verified-event fraud rate vs unverified; customer friction",
      ""),
],

# ── R-037 Conduct — Service delivery monitoring; Trading activity monitoring; Verifications ──
"R-037": [
    C("Service delivery and customer journey monitoring",
      "Detective", "Hybrid",
      "Monitoring of customer journeys and service delivery quality with metrics on outcomes, friction, and complaint conversion, with thematic analysis driving conduct improvements.",
      "Continuous + Monthly review",
      "Chief Customer Officer / Conduct Lead",
      "Customer journey metrics; complaint conversion; thematic improvements delivered",
      "FCA Consumer Duty"),
],

# ── R-038 Statutory Reporting — Customer tax standards; Asset valuation review; Verifications ──
"R-038": [
    C("Customer tax obligations and reporting (FATCA / CRS)",
      "Preventive", "Hybrid",
      "Customer tax framework covering self-certification, classification, withholding, and reporting under FATCA, CRS, and equivalent regimes with quality assurance on submissions.",
      "Continuous + Per cycle",
      "Head of Tax / Operations",
      "Self-cert completion; classification accuracy; FATCA/CRS submission quality",
      "FATCA / CRS / OECD"),
    C("Asset valuation review and standing data integrity",
      "Detective", "Hybrid",
      "Independent review of asset valuations and standing data feeding statutory reporting with reconciliation, source verification, and challenge of material judgments.",
      "Per cycle",
      "Financial Controller / Independent Reviewer",
      "Valuation review completion; material adjustments; source reconciliation",
      "IFRS 13 / IAS 36"),
],

}
