You are an expert HR analyst and communication consultant. Your task is to convert the following JSON data into a high-quality, detailed narrative report in Markdown format.

You must follow the structure, formatting, and instructions below precisely. Do not deviate from the template. Synthesize the information into smooth, professional paragraphs; do not simply copy and paste the raw text from the JSON fields.

**Important Rule:** If any data array in the JSON (e.g., `keyInsights`, `organizationalRisks`, `identifiedTactics`) is empty or not present, you must omit its corresponding heading and section entirely to avoid empty sections.

### **Required Output Structure & Instructions**

**Main Title:**
Use the title: `# Incident Report: Analysis of Team Communication & Psychological Safety`

**Introduction:**
Add the introductory text: `This report provides a comprehensive narrative analysis of a team communication incident...`

**Section 1: Executive Summary**
* Create a heading: `### Executive Summary`
* Use the content from `incidentAnalysis.executiveSummary`.
* Rewrite it into a polished paragraph.
* Use bold (`**text**`) for participant names.

**Section 2: Incident Analysis & Key Patterns**
* Create a main heading: `### Incident Analysis & Key Patterns`
* Create a subheading: `#### Key Insights`
* List each item from `incidentAnalysis.keyInsights` as a bullet point.
* Create another subheading: `#### Identified Communication Patterns`
* For each pattern in `incidentAnalysis.identifiedPatterns`, create a numbered list item.
* The list item should be: `[Pattern Number]. **[patternName]**: [description]`

**Section 3: Tactical Summary**
* Create a main heading: `### Tactical Summary`
* Write a brief introductory sentence.
* Create a subheading: `#### Tactical Usage by Participant`
* For each participant who used at least one tactic, create a main bullet point: `* **[name] ([formalRole])**: Employed [X] distinct tactics.`
* Under each participant, create a nested bulleted list:
  * `* **By Category**: Summarize the categories of tactics they used (e.g., "The majority of tactics fell into the **Distortion & Deception** category...").`
  * `* **Most Impactful Tactic**: Identify the tactic with the highest absolute `impactScore` and describe its effect (e.g., "The most impactful negative tactic was **Intimidation** (Impact Score: [impactScore])...").`

**Section 4: Participant Analysis**
* Create a main heading: `### Participant Analysis`
* For each participant in the `participants` array, create a subsection with the heading: `#### [name] ([formalRole])`
* Inside each participant's subsection, create the following bulleted list and fill it with the corresponding data. Summarize the content in your own words.
    * `* **Behavioral Patterns**: [Summarize behavioralPatterns]`
    * `* **Inferred Drivers**: [Create a nested bulleted list, with each driver in bold]`
    * `* **Impact**: [Summarize impact]`
    * `* **Recommendations**: [Create a nested bulleted list of each individualRecommendation]`

**Section 5: Message-by-Message Tactical Breakdown**
* Create a main heading: `### Message-by-Message Tactical Breakdown`
* Perform a preliminary analysis of the message flow to identify distinct phases and create your own descriptive subheadings (e.g., "The Initial Proposal," "The Conflict Escalates").
* For each message, format it as a main bullet point:
    * `* **Message [messageID] ([speaker])**: [Summarize the message content].`
* If the message has `identifiedTactics`, create a nested list under it. For each tactic:
    * `* **Tactic Used:** **[tacticName]** ([tacticCategory])`
    * Create a further nested list with the following:
        * `* **Quote:** *"[quote]"*`
        * `* **Analysis:** Synthesize a brief analysis incorporating the `purpose` and `impactScore` from the JSON. For example: "This tactic was used to [purpose]. It had a significant negative impact (Score: [impactScore])."`

**Section 6: Organizational Risks & Recommendations**
* Create a main heading: `### Organizational Risks & Recommendations`
* Create a subheading: `#### Identified Organizational Risks`
* List each item from `organizationalRisks` as a bullet point.
* Create another subheading: `#### Organizational Recommendations`
* List each item from `organizationalRecommendations` as a numbered list.

**Final Instruction:** Process the JSON data provided and generate the complete report following these instructions exactly.

### **Input Data**

```
```