import json
import html
import argparse

# --- Helper Functions ---


def format_css_class(name, prefix=""):
    """Converts a string into a CSS-friendly class name."""
    class_name = str(name).lower().replace("&", "").replace(" ", "-")
    return f"{prefix}{class_name}" if prefix else class_name


def get_unique_speakers(data):
    """Extracts a list of unique speaker names from the data."""
    speakers = set()
    for message in data.get("messageAnalysis", []):
        if message.get("speaker"):
            speakers.add(message.get("speaker"))
    return sorted(list(speakers))


def generate_speaker_styles(speakers):
    """Generates dynamic CSS for speaker colors from a predefined palette."""
    colors = ["#d32f2f", "#1976d2", "#388e3c", "#f57c00", "#512da8", "#00796b", "#c2185b", "#e64a19", "#689f38", "#0288d1", "#455a64", "#d81b60", "#00897b", "#f4511e", "#37474f"]
    styles = ""
    for i, speaker in enumerate(speakers):
        speaker_class = format_css_class(speaker, prefix="speaker-")
        color = colors[i % len(colors)]
        styles += f"        .{speaker_class} {{ color: {color}; }}\n"
    return styles


def get_unique_categories(data):
    """Extracts a list of unique tactic categories from the data."""
    categories = set()
    for message in data.get("messageAnalysis", []):
        for tactic in message.get("identifiedTactics", []):
            category = tactic.get("tacticCategory", "Unknown")
            # Normalize category names
            if category == "Constructive & De-escalating":
                category = "Constructive"
            categories.add(category)
    return sorted(list(categories))


def generate_category_styles_and_map(categories):
    """Generates dynamic CSS and a color map for tactic categories."""
    # Palettes for background (rgba) and solid colors (hex)
    bg_colors = ["rgba(239, 68, 68, 0.15)", "rgba(168, 85, 247, 0.15)", "rgba(249, 115, 22, 0.15)", "rgba(245, 158, 11, 0.15)", "rgba(34, 197, 94, 0.15)", "rgba(59, 130, 246, 0.15)", "rgba(236, 72, 153, 0.15)", "rgba(139, 92, 246, 0.15)"]
    solid_colors = ["#ef4444", "#a855f7", "#f97316", "#f59e0b", "#22c55e", "#3b82f6", "#ec4899", "#8b5cf6"]

    styles = ""
    color_map = {}
    for i, category in enumerate(categories):
        category_class = format_css_class(category, prefix="tactic-")
        bg_color = bg_colors[i % len(bg_colors)]
        solid_color = solid_colors[i % len(solid_colors)]

        styles += f"""
        .{category_class} {{ background-color: {bg_color}; text-decoration-color: {solid_color}; }}
        .{category_class} .tooltip-text strong {{ color: {solid_color}; }}"""

        color_map[category] = bg_color

    return styles, color_map


def create_tooltip_html(tactic):
    """Generates the HTML for a single tooltip pop-up."""
    tactic_name = html.escape(tactic.get("tacticName", "N/A"))
    category = html.escape(tactic.get("tacticCategory", "N/A"))
    purpose = html.escape(tactic.get("purpose", "No purpose provided."))
    driver = html.escape(tactic.get("likelyDriver", "N/A"))
    impact_score = tactic.get("impactScore", 0)
    confidence = tactic.get("confidenceScore", 0) * 100

    impact_class = "impact-positive" if impact_score > 0 else "impact-negative"
    impact_score_str = f"+{impact_score}" if impact_score > 0 else str(impact_score)

    return f"""<span class="tooltip-text">
        <strong>{tactic_name}</strong>
        <div class="tactic-category">Category: {category}</div>
        <div class="tactic-purpose">{purpose}</div>
        <div class="tactic-driver">Likely Driver: {driver}</div>
        <div><span>Impact Score: </span><span class="{impact_class}">{impact_score_str}</span></div>
        <div><span>Confidence: </span><span>{confidence:.1f}%</span></div>
    </span>"""


def wrap_message_with_tactics(message_text, tactics):
    """
    Finds tactic quotes in the message and wraps them with the appropriate HTML.
    """
    processed_message = html.escape(message_text)

    sorted_tactics = sorted(tactics, key=lambda t: len(t.get("quote", "")), reverse=True)

    for tactic in sorted_tactics:
        quote = tactic.get("quote")
        if not quote:
            continue

        escaped_quote = html.escape(quote)
        category = tactic.get("tacticCategory", "")
        if category == "Constructive & De-escalating":
            category = "Constructive"

        category_class = format_css_class(category, prefix="tactic-")
        tooltip = create_tooltip_html(tactic)

        wrapper_html = f'<span class="has-tactic {category_class}">{escaped_quote}{tooltip}</span>'

        processed_message = processed_message.replace(escaped_quote, wrapper_html, 1)

    processed_message = processed_message.replace("\n", "<br>")
    if message_text.strip().startswith(">"):
        lines = processed_message.split("<br>")
        blockquote_content = []
        regular_content = []

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith("&gt; "):
                blockquote_content.append(stripped_line.replace("&gt; ", "", 1))
            elif stripped_line == "&gt;":
                blockquote_content.append("")
            else:
                regular_content.append(line)

        final_lines = []
        if regular_content:
            final_lines.append("<br>".join(regular_content))
        if blockquote_content:
            final_lines.append(f"<blockquote>{'<br>'.join(blockquote_content)}</blockquote>")

        processed_message = "".join(final_lines)

    return processed_message


def generate_html_body(data, category_color_map):
    """Generates the main body content of the HTML file."""
    messages_html = ""
    for message_data in data.get("messageAnalysis", []):
        speaker = html.escape(message_data.get("speaker", "Unknown"))
        speaker_class = format_css_class(speaker, prefix="speaker-")

        message_content = wrap_message_with_tactics(message_data.get("message", ""), message_data.get("identifiedTactics", []))

        messages_html += f"""
            <!-- Message {message_data.get("messageID")} -->
            <div class="message">
                <div class="speaker {speaker_class}">{speaker}</div>
                <div class="message-content">{message_content}</div>
            </div>
        """

    legend_html = ""
    for category, color in category_color_map.items():
        legend_html += f'<div class="legend-item"><div class="legend-color-box" style="background-color: {color};"></div>{category}</div>'

    return f"""
    <div class="canvas-frame">
        <h1>Chat Message Analysis</h1>
        <p class="intro">Hover over the highlighted text to see the identified communication tactics.</p>
        <div class="legend">{legend_html}</div>
        <div class="chat-log">{messages_html}</div>
    </div>
    """


def get_html_template(body_content, speaker_styles, category_styles):
    """Returns the full HTML document structure with CSS and JavaScript."""
    javascript_code = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const tactics = document.querySelectorAll('.has-tactic');
            let activeTactic = null;

            // Function to hide any active tooltip
            const hideActiveTooltip = () => {
                if (activeTactic) {
                    activeTactic.classList.remove('show-tooltip');
                    activeTactic = null;
                }
            };

            tactics.forEach(tactic => {
                tactic.addEventListener('click', function(event) {
                    event.stopPropagation(); // Stop click from bubbling up to the document
                    
                    // If this tactic is already active, hide it and we're done
                    if (this.classList.contains('show-tooltip')) {
                        hideActiveTooltip();
                    } else {
                        // Otherwise, hide any other active tooltip first
                        hideActiveTooltip();
                        // Then show this one
                        this.classList.add('show-tooltip');
                        activeTactic = this;
                    }
                });
            });

            // Add a listener to the whole document to close tooltips when clicking away
            document.addEventListener('click', function() {
                hideActiveTooltip();
            });
        });
    </script>
    """

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Message Analysis</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            background-color: #f0f2f5;
            color: #333;
            padding: 20px;
            line-height: 1.5;
            margin: 0;
        }}
        .canvas-frame {{
            background-color: #ffffff;
            padding: 20px 10px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
            max-width: 860px;
            margin: 20px auto;
            border: 1px solid #e0e0e0;
        }}
        h1, .intro {{ text-align: center; color: #444; padding: 0 20px; }}
        .intro {{ margin-bottom: 20px; }}
        .legend {{
            display: flex; flex-wrap: wrap; justify-content: center;
            gap: 20px; margin-bottom: 30px; padding: 10px 20px; font-size: 14px;
        }}
        .legend-item {{ display: flex; align-items: center; gap: 8px; }}
        .legend-color-box {{
            width: 16px; height: 16px; border-radius: 3px; border: 1px solid rgba(0,0,0,0.1);
        }}
        .chat-log {{ max-width: 800px; margin: 0 auto; background-color: #ffffff; padding: 20px 30px; }}
        .message {{ margin-bottom: 24px; }}
        .speaker {{ font-weight: bold; margin-bottom: 5px; }}
{speaker_styles}
        .message-content {{ line-height: 1.6; word-wrap: break-word; }}
        .message-content blockquote {{
            border-left: 3px solid #e0e0e0; padding-left: 15px; margin: 10px 0 10px 5px;
            color: #666; font-style: italic;
        }}
        .has-tactic {{
            position: relative; text-decoration: underline; text-decoration-style: dashed;
            cursor: pointer; /* Changed from 'help' to 'pointer' for better touch affordance */
            border-radius: 3px; padding: 1px 2px;
        }}
{category_styles}
        .tooltip-text {{
            visibility: hidden; width: 320px; background-color: #263238; color: #fff;
            text-align: left; border-radius: 6px; padding: 12px; position: absolute;
            z-index: 1; bottom: 130%; left: 50%; margin-left: -160px; opacity: 0;
            transition: opacity 0.3s; font-size: 14px; line-height: 1.4;
            text-decoration: none; box-shadow: 0 4px 12px rgba(0,0,0,0.2); white-space: normal;
        }}
        .tooltip-text::after {{
            content: ""; position: absolute; top: 100%; left: 50%; margin-left: -5px;
            border-width: 5px; border-style: solid; border-color: #263238 transparent transparent transparent;
        }}
        /* Show tooltip on hover (for desktop) OR when 'show-tooltip' class is added by JS (for touch/click) */
        .has-tactic:hover .tooltip-text,
        .has-tactic.show-tooltip .tooltip-text {{
            visibility: visible;
            opacity: 1;
        }}
        .tooltip-text strong {{ display: block; margin-bottom: 2px; }}
        .tooltip-text .tactic-category, .tooltip-text .tactic-driver {{
            font-size: 0.85em; font-style: italic; color: #b0bec5; margin-bottom: 8px;
        }}
        .tooltip-text .tactic-purpose {{ margin-bottom: 8px; }}
        .impact-positive {{ color: #81c784; font-weight: bold; }}
        .impact-negative {{ color: #e57373; font-weight: bold; }}
    </style>
</head>
<body>
    {body_content}
    {javascript_code}
</body>
</html>
    """


# --- Main Execution ---


def main():
    """Main function to generate the HTML report."""
    parser = argparse.ArgumentParser(description="Generate an HTML report from a chat analysis JSON file.")
    parser.add_argument("input_json", help="Path to the input JSON file.")
    parser.add_argument("output_html", help="Path to the output HTML file.")
    args = parser.parse_args()

    try:
        with open(args.input_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found at {args.input_json}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {args.input_json}. Please check the file format.")
        return

    unique_speakers = get_unique_speakers(data)
    speaker_styles = generate_speaker_styles(unique_speakers)

    unique_categories = get_unique_categories(data)
    category_styles, category_color_map = generate_category_styles_and_map(unique_categories)

    body = generate_html_body(data, category_color_map)
    full_html = get_html_template(body, speaker_styles, category_styles)

    try:
        with open(args.output_html, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Successfully generated HTML report at {args.output_html}")
    except IOError:
        print(f"Error: Could not write to output file at {args.output_html}")


if __name__ == "__main__":
    main()
