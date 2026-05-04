"""
AI driver batch — treats AI (especially agentic AI) as a risk driver
amplifying existing themes. R-040 retains its dedicated AI governance focus;
this batch adds AI-specific controls to other risks where AI changes the
threat model, control surface, or harm pathway.

Reference frameworks:
- NIST AI RMF (Risk Management Framework)
- ISO/IEC 42001 (AI management systems)
- ISO/IEC 23894 (AI risk management)
- EU AI Act (high-risk AI obligations)
- OWASP Top 10 for LLM Applications
- OWASP Agentic AI threats
- MITRE ATLAS (adversarial threat landscape for AI)
"""
from risk_controls import C

AI_DRIVER_CONTROLS = {

# ─────────────────────────────────────────────────────────────
# R-015 Cyber attack — agentic AI introduces new attack surfaces
# ─────────────────────────────────────────────────────────────
"R-015": [
    C("Prompt injection and LLM input defence",
      "Preventive", "Hybrid",
      "Defence-in-depth controls against prompt injection in LLM-integrated systems including input sanitisation, system-prompt isolation, output filtering, and red-team testing of agent boundaries.",
      "Continuous + Per release",
      "CISO / Head of AI Security",
      "Injection test pass rate; agent boundary breaches; output filter activations",
      "OWASP LLM01; NIST AI RMF; MITRE ATLAS"),
    C("AI agent access controls and tool authorisation",
      "Preventive", "Hybrid",
      "Strict authorisation framework for AI agents covering tool permissions, action approvals on high-risk operations, scope-bounded credentials, and audit logging of all agent-initiated actions.",
      "Continuous",
      "CISO / Head of AI Engineering",
      "Agent action volume; high-risk action approval rate; scope violations",
      "NIST AI RMF MANAGE; ISO/IEC 42001; OWASP Agentic AI"),
    C("Adversarial AI testing and red-teaming",
      "Detective", "Hybrid",
      "Programme of adversarial testing against AI systems covering evasion, model extraction, data poisoning, jailbreaks, and agent manipulation with structured remediation.",
      "Quarterly + Per major release",
      "AI Security / Red Team",
      "Test scenarios covered; vulnerabilities identified; remediation closure",
      "MITRE ATLAS; NIST AI RMF MEASURE; OWASP LLM Top 10"),
],

# ─────────────────────────────────────────────────────────────
# R-016 Data loss — AI changes the data threat model
# ─────────────────────────────────────────────────────────────
"R-016": [
    C("AI input data governance and DLP",
      "Preventive", "Hybrid",
      "Engineering controls to prevent sensitive data from entering AI model inputs (training corpora, fine-tuning sets, runtime prompts) including DLP integration on AI tools, approved-data classification, and prompt logging review for sensitive content.",
      "Continuous",
      "DPO / CISO",
      "DLP blocks on AI inputs; sensitive prompt incidents; classification coverage on AI inputs",
      "GDPR Art. 5; ISO/IEC 27701; NIST AI RMF"),
    C("Vector store and embedding governance",
      "Preventive", "Hybrid",
      "Governance over vector databases and embedding stores covering classification, access controls, retention, deletion (right-to-erasure), and segregation across tenants or use cases.",
      "Continuous + Annual review",
      "DPO / Head of Data Platforms",
      "Vector store inventory; access events; deletion request compliance; tenant isolation tests",
      "GDPR Art. 17; ISO/IEC 27701; ISO/IEC 42001"),
],

# ─────────────────────────────────────────────────────────────
# R-019 Compliance — AI-specific regulatory obligations emerging
# ─────────────────────────────────────────────────────────────
"R-019": [
    C("AI regulatory horizon scanning and obligations mapping",
      "Detective", "Manual",
      "Continuous horizon scanning of AI-specific regulation (EU AI Act, ASIC / APRA AI guidance, sector-specific requirements) with use-case classification, obligations mapping, and readiness tracking.",
      "Continuous + Quarterly review",
      "CCO / Head of AI Governance",
      "AI regs tracked; high-risk use cases identified; obligation closure; readiness scores",
      "EU AI Act; ASIC INFO 269; APRA CPG 230; ISO/IEC 42001"),
],

# ─────────────────────────────────────────────────────────────
# R-022 Brand and reputation — AI failures go viral fast
# ─────────────────────────────────────────────────────────────
"R-022": [
    C("AI incident response and public communication",
      "Corrective", "Manual",
      "Defined response to AI failure events affecting brand including rapid containment, public communication, customer remediation, and post-incident transparency reporting.",
      "Per material event + Quarterly drill",
      "Chief Communications Officer / Head of AI",
      "Activation timeliness; customer remediation reach; sentiment recovery",
      "ISO 22361; NIST AI RMF GOVERN"),
],

# ─────────────────────────────────────────────────────────────
# R-029 Third party — foundation models are critical vendors
# ─────────────────────────────────────────────────────────────
"R-029": [
    C("Foundation model and AI vendor governance",
      "Preventive", "Hybrid",
      "Tiered governance over foundation model and AI vendors covering due diligence on training data, security posture, terms of service, model behaviour change notifications, and exit options.",
      "Per onboarding + Annual review",
      "Vendor Risk / Head of AI",
      "Vendor inventory; behaviour change notifications; exit options assessed",
      "APRA CPS 230; ISO 27036; NIST AI RMF; EU AI Act"),
],

# ─────────────────────────────────────────────────────────────
# R-030 Outsourcing — AI supply chain risk
# ─────────────────────────────────────────────────────────────
"R-030": [
    C("AI supply chain and software bill of materials",
      "Preventive", "Hybrid",
      "Software supply chain governance for AI-integrated systems including model provenance, AI SBOM, third-party model licensing compliance, and known-vulnerability monitoring across the AI stack.",
      "Continuous + Per release",
      "CISO / Head of AI Engineering",
      "AI SBOM coverage; vulnerable component count; provenance gaps; licence compliance",
      "NIST SSDF; CISA SBOM; EU AI Act; ISO/IEC 42001"),
],

# ─────────────────────────────────────────────────────────────
# R-035 External fraud — AI-enabled fraud techniques
# ─────────────────────────────────────────────────────────────
"R-035": [
    C("Deepfake and AI-generated content detection",
      "Detective", "Hybrid",
      "Surveillance and detection capability for deepfake voice, video, and AI-generated documentation in high-risk transaction and verification flows, with secondary checks triggered on suspect signals.",
      "Continuous",
      "Head of Fraud / Customer Identity",
      "Deepfake alerts; secondary check escalations; confirmed deepfake incidents",
      "FFIEC; FATF Rec 10; NIST AI RMF; ENISA"),
    C("Synthetic identity and AI-enabled application fraud screening",
      "Preventive", "Hybrid",
      "Enhanced screening for synthetic identities and AI-fabricated applications including device intelligence, behavioural biometrics, document authenticity verification, and velocity / pattern analysis.",
      "Per application + Continuous",
      "Head of Fraud / Onboarding",
      "Synthetic identity detection rate; suspect application volume; confirmed synthetic ID losses",
      "FATF Rec 10; FFIEC; PSD2 SCA"),
],

# ─────────────────────────────────────────────────────────────
# R-037 Conduct — AI in customer-facing decisions
# ─────────────────────────────────────────────────────────────
"R-037": [
    C("Algorithmic fairness testing for customer-impacting AI",
      "Detective", "Hybrid",
      "Pre-deployment and ongoing fairness testing of AI systems making customer-impacting decisions covering protected attributes, disparate impact, and outcome equity across cohorts.",
      "Per deployment + Quarterly",
      "Head of AI / Head of Conduct",
      "Models tested; disparate impact findings; remediation closure; outcome equity scores",
      "EU AI Act Art. 10; NIST AI RMF MEASURE; ISO/IEC 24027"),
    C("AI explainability and adverse-decision review",
      "Detective", "Hybrid",
      "Explainability capability for AI-driven adverse decisions affecting customers (declines, pricing, service restrictions) including per-decision rationale, customer-accessible explanations, and human review on contested outcomes.",
      "Continuous + Per contested decision",
      "Head of AI / Customer Resolutions",
      "Adverse decisions with rationale; customer reviews requested; review outcomes vs original",
      "EU AI Act Art. 14; ASIC RG 271; NIST AI RMF; GDPR Art. 22"),
    C("AI advice boundary and human-in-the-loop controls",
      "Preventive", "Hybrid",
      "Defined boundaries on AI advice delivery to customers (regulated advice, medical, legal) with human-in-the-loop on regulated outputs, scope guards on AI agents, and audit of outputs against policy.",
      "Continuous + Per use case",
      "CCO / Head of AI",
      "AI use cases classified; human-in-the-loop coverage; out-of-scope outputs detected",
      "EU AI Act Art. 14; FCA Consumer Duty; ASIC AI guidance"),
],

}
