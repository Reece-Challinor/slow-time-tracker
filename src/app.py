from flask import Flask, render_template_string, request
from datetime import datetime
import math

app = Flask(__name__)

def calculate_life_expectancy(age, bmi, smoker, country):
    # Basic life expectancy calculation
    # Based on simplified actuarial data
    base_expectancy = 78.0  # US/Canada base
    
    # BMI adjustment
    if 18.5 <= bmi <= 24.9:
        bmi_adj = 2.0
    elif 25 <= bmi <= 29.9:
        bmi_adj = 0
    else:
        bmi_adj = -2.0
        
    # Smoking adjustment
    smoker_adj = -10 if smoker else 0
    
    # Calculate remaining years
    total_expectancy = base_expectancy + bmi_adj + smoker_adj
    remaining_years = total_expectancy - age
    
    return max(remaining_years, 0)

def generate_dot_matrix(age, remaining_years):
    total_months = int((age + remaining_years) * 12)
    months_lived = int(age * 12)
    months_per_row = 12
    
    visualization = []
    for i in range(0, total_months, months_per_row):
        row = []
        for j in range(months_per_row):
            if i + j < months_lived:
                row.append("●")
            else:
                row.append("○")
        visualization.append(f"{i//12 + 1:2d}: {' '.join(row)}")
    
    return "\n".join(visualization)

def generate_bar_graph(age, remaining_years):
    total_years = int(age + remaining_years)
    decades = math.ceil(total_years / 10)
    
    visualization = []
    for decade in range(decades):
        start_year = decade * 10
        end_year = min(start_year + 10, total_years)
        bar = ""
        for year in range(start_year, end_year):
            if year < age:
                bar += "█"
            else:
                bar += "░"
        visualization.append(f"{start_year:2d}-{end_year-1:2d}: {bar}")
    
    return "\n".join(visualization)

def generate_histogram(age, remaining_years):
    total_years = int(age + remaining_years)
    max_height = 10
    histogram = []
    
    # Simplified life phases
    phases = [
        ("Childhood", 0, 18),
        ("Early Adult", 18, 30),
        ("Middle Adult", 30, 50),
        ("Late Adult", 50, 70),
        ("Elder", 70, total_years)
    ]
    
    for phase_name, start, end in phases:
        phase_length = end - start
        filled_years = max(0, min(age - start, phase_length))
        remaining = max(0, min(phase_length - filled_years, phase_length))
        
        bar_height = int((phase_length / total_years) * max_height)
        filled_height = int((filled_years / phase_length) * bar_height)
        
        for h in range(bar_height-1, -1, -1):
            if h < filled_height:
                histogram.append(f"{phase_name:12} |{'█' * bar_height}")
            else:
                histogram.append(f"{phase_name:12} |{'░' * bar_height}")
    
    return "\n".join(histogram)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>How Much Is Left?</title>
    <style>
        :root {
            --bg-color: #1a1a1a;
            --text-color: #e0e0e0;
            --accent-color: #404040;
            --highlight-color: #606060;
        }
        
        body {
            font-family: monospace;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 2rem;
            max-width: 900px;
            margin: 0 auto;
        }
        
        .visualization {
            white-space: pre;
            margin: 2rem 0;
            padding: 1rem;
            background-color: #222;
            border-radius: 4px;
        }
        
        .philosophy {
            border-left: 3px solid var(--accent-color);
            padding-left: 1rem;
            margin: 2rem 0;
        }
        
        .watch {
            text-align: center;
            font-size: 2rem;
            margin: 2rem 0;
        }
        
        .tabs {
            display: flex;
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .tab {
            padding: 0.5rem 1rem;
            background-color: var(--accent-color);
            border: none;
            color: var(--text-color);
            cursor: pointer;
        }
        
        .tab.active {
            background-color: var(--highlight-color);
        }
        
        form {
            margin: 2rem 0;
            display: grid;
            gap: 1rem;
        }
        
        input, select, button {
            background: #333;
            color: var(--text-color);
            border: 1px solid var(--accent-color);
            padding: 0.5rem;
            margin: 0.5rem 0;
        }
        
        .quote {
            font-style: italic;
            margin: 2rem 0;
            padding: 1rem;
            border-radius: 4px;
            background-color: #222;
        }
    </style>
</head>
<body>
    <h1>How Much Is Left?</h1>
    
    <div class="watch">
        ⌚ {{ current_time }}
    </div>
    
    <form method="POST">
        <div>
            <label for="age">Your current age:</label>
            <input type="number" name="age" id="age" required min="0" max="100" value="{{ age if age else '' }}">
        </div>
        <div>
            <label for="bmi">BMI:</label>
            <input type="number" name="bmi" id="bmi" step="0.1" required value="{{ bmi if bmi else '' }}">
        </div>
        <div>
            <label for="smoker">Do you smoke?</label>
            <select name="smoker" id="smoker">
                <option value="0" {% if not smoker %}selected{% endif %}>No</option>
                <option value="1" {% if smoker %}selected{% endif %}>Yes</option>
            </select>
        </div>
        <button type="submit">Generate Visualization</button>
    </form>

    {% if visualization %}
    <div class="tabs">
        <button class="tab active" onclick="showViz('matrix')">Dot Matrix</button>
        <button class="tab" onclick="showViz('bar')">Bar Graph</button>
        <button class="tab" onclick="showViz('histogram')">Histogram</button>
    </div>
    
    <div class="visualization" id="matrix-viz">
{{ matrix }}
    </div>
    
    <div class="visualization" id="bar-viz" style="display: none;">
{{ bar }}
    </div>
    
    <div class="visualization" id="histogram-viz" style="display: none;">
{{ histogram }}
    </div>
    {% endif %}

    <div class="philosophy">
        <h2>Understanding Your Time</h2>
        
        <div class="quote">
            "The bad news is time flies. The good news is you're the pilot." - Michael Altshuler
        </div>
        
        <p>This visualization represents your life in discrete units of time. Each marker is a month of potential - either spent or yet to be lived.</p>
        
        <h3>The Time You Have</h3>
        <ul>
            <li>Average person has about 80,000 hours of discretionary time</li>
            <li>That's roughly 1,000 months or 4,000 weeks</li>
            <li>About 25,000 days of consciousness</li>
        </ul>
        
        <h3>Weekly Reflection Points</h3>
        <ul>
            <li>How are you investing your remaining time?</li>
            <li>What would your future self thank you for doing now?</li>
            <li>Are your daily actions aligned with your life's goals?</li>
        </ul>
        
        <p class="quote">
            "Time is what we want most, but what we use worst." - William Penn
        </p>
    </div>

    <script>
        function showViz(type) {
            document.querySelectorAll('.visualization').forEach(v => v.style.display = 'none');
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(`${type}-viz`).style.display = 'block';
            event.target.classList.add('active');
        }
    </script>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    bmi = None
    smoker = None
    matrix = None
    bar = None
    histogram = None
    
    if request.method == "POST":
        age = float(request.form.get("age", 0))
        bmi = float(request.form.get("bmi", 0))
        smoker = bool(int(request.form.get("smoker", 0)))
        
        remaining_years = calculate_life_expectancy(age, bmi, smoker, "US")
        
        matrix = generate_dot_matrix(age, remaining_years)
        bar = generate_bar_graph(age, remaining_years)
        histogram = generate_histogram(age, remaining_years)
    
    return render_template_string(
        TEMPLATE,
        age=age,
        bmi=bmi,
        smoker=smoker,
        matrix=matrix,
        bar=bar,
        histogram=histogram,
        current_time=datetime.now().strftime("%H:%M"),
    )

if __name__ == "__main__":
    app.run(debug=True)