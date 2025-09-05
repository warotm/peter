# P.E.T.E.R.

> A tool for finding clarity in confusing conversations.

P.E.T.E.R. is a web-based tool that uses Google's Gemini AI to analyse conversation transcripts. It identifies specific psychological and emotive tactics used by participants to provide an objective, high-level view of communication dynamics.

**P.E.T.E.R.** stands for **Psychological Emotive Tactics Emergency Response**.

## The Story Behind P.E.T.E.R.

This project is deeply personal.

I created P.E.T.E.R. to turn a painful experience in a former toxic workplace into a tool for empowerment. The name itself is a quiet reminder of that difficult situation, repurposed to help others.

I know the feeling of leaving a conversation completely drained, confused, and filled with self-doubt. I would ruminate for days, lose sleep, and question my own perspective. It was an isolating and disorienting experience. That feeling of helplessness, and the injustice that often follows, is what drove me to create this tool. I wanted to build the neutral third party I wish I'd had—something that could look at the words on a page and offer objective clarity.

The mission of this tool is simple: to serve as a mirror, helping you see communication patterns that are hard to spot when you're emotionally involved. My hope is that it provides a moment of clarity, validates your experiences, and helps you trust your own feelings a little more.

## Key Features

* **AI-Powered Analysis:** Utilises the Gemini API to identify dozens of communication tactics.
* **Identifies Manipulative Tactics:** Highlights patterns like Gaslighting, Deflection, Circular Arguments, and more.
* **Highlights Constructive Communication:** Recognises healthy communication strategies to provide a balanced view.
* **Privacy-Focused:** The application is client-side. Your conversation data is sent directly to the Google API and is **not stored or saved** on any server I control.
* **PDF Report Generation:** Generates a downloadable PDF of the analysis for your private records.

## How It Works

The process is straightforward:

1.  The user pastes an anonymised conversation transcript into the text area.
2.  The application formats the text and sends it to the Gemini API with a specialised prompt.
3.  The Gemini API analyses the text based on the **Psychological Emotive Tactics Emergency Response** framework.
4.  The application receives the analysis from the API.
5.  The results are formatted and presented to the user, with an option to download as a PDF.

## How to Use

### Standard Use
1.  Navigate to the P.E.T.E.R. web page. (You can find the latest link on my Linktree profile: https://linktr.ee/warotm)
2.  **CRITICAL: Anonymise your transcript.** Remove all names, locations, and any other personally identifiable information.
3.  Paste the transcript into the input box. Ensure each message is clearly attributed to a speaker (e.g., `Speaker A:`, `Speaker B:`).
4.  Click the "Generate PDF Report" button. The process may take up to a minute.
5.  Your generated report will be downloaded automatically.

### Power Users
For advanced use, the prompt and output schema are available in the `protocol` folder, allowing you to run the analysis on your preferred LLM.

## Important Disclaimers

> \[!WARNING\]
> **This is an informational tool, not a substitute for professional advice.**
> I am not a therapist, psychologist, or legal professional. This tool is designed to provide perspective and should not be used for making diagnoses or as a substitute for professional help. If you are in distress, please seek assistance from a qualified professional.

> \[!NOTE\]
> **AI-generated content has limitations.**
> The analysis is provided by a large language model (LLM) and may not be perfectly accurate or complete. It can make mistakes. Please use your own judgement when interpreting the results.

> \[!IMPORTANT\]
> **Data Privacy and Security**
> This tool operates on the Gemini API's free tier. While the application itself does not save your data, the transcript is processed by Google's servers. **Do not submit sensitive, confidential, or personally identifiable information.** Always ensure your transcript is fully anonymised.

## Acknowledgements

This project was born from a difficult period, and it would not have been possible without the unwavering support of some incredible people.

To my partner: Thank you for being my rock. Your patience, love, and constant belief in me were the foundation I needed to not only get through a hard time but to create something positive from it.

To my friends: Thank you for the inspirations, the reality checks, and for reminding me of my own strength when I struggled to see it. Your support was a lifeline.

## Contributing

This is a one-person project born from personal experience, but I welcome feedback and suggestions. If you have ideas on how to improve P.E.T.E.R., please feel free to reach out.

---

*This tool was created for those who need a moment of clarity. I hope it helps.*
