"""
Histogram visualization module for life phases.
Creates a vertical histogram showing different life phases and their progression.
"""

def generate_histogram(age: float, remaining_years: float) -> str:
    """
    Generate an ASCII histogram showing life phases vertically.
    
    Parameters:
        age: Current age of the person
        remaining_years: Calculated remaining years of life
    
    Returns:
        String representation of the histogram where:
        █ represents completed portions of life phases
        ░ represents remaining portions
        Each phase is shown vertically with proportional height
    """
    total_years = int(age + remaining_years)
    # Maximum height for visualization bars
    max_height = 10
    histogram_lines = []
    
    # Define life phases with their year ranges
    phases = [
        ("Childhood", 0, 18),
        ("Early Adult", 18, 30),
        ("Middle Adult", 30, 50),
        ("Late Adult", 50, 70),
        ("Elder", 70, total_years)
    ]
    
    # Generate histogram for each life phase
    for phase_name, start, end in phases:
        # Calculate the length of this phase
        phase_length = end - start
        
        # Calculate how much of this phase has been lived
        filled_years = max(0, min(age - start, phase_length))
        # Calculate remaining years in this phase
        remaining = max(0, min(phase_length - filled_years, phase_length))
        
        # Calculate proportional bar height for this phase
        bar_height = int((phase_length / total_years) * max_height)
        # Calculate how much of the bar should be filled
        filled_height = int((filled_years / phase_length) * bar_height)
        
        # Generate the bars from top to bottom
        for h in range(bar_height-1, -1, -1):
            if h < filled_height:
                # This portion of life has been lived
                histogram_lines.append(f"{phase_name:12} |{'█' * bar_height}")
            else:
                # This portion remains to be lived
                histogram_lines.append(f"{phase_name:12} |{'░' * bar_height}")
    
    return "\n".join(histogram_lines)

def calculate_phase_percentages(age: float, remaining_years: float) -> dict:
    """
    Calculate the percentage completion of each life phase.
    Useful for additional statistics or different visualizations.
    """
    phases = {
        "Childhood": (0, 18),
        "Early Adult": (18, 30),
        "Middle Adult": (30, 50),
        "Late Adult": (50, 70),
        "Elder": (70, float('inf'))
    }
    
    results = {}
    for phase, (start, end) in phases.items():
        if age < start:
            results[phase] = 0
        elif age >= end:
            results[phase] = 100
        else:
            completed = age - start
            total = end - start
            results[phase] = (completed / total) * 100
            
    return results