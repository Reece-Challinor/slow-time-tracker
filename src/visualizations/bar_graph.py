"""
Bar graph visualization module for time representation.
Creates decade-by-decade visualization of life progression using ASCII characters.
"""

import math

def generate_bar_graph(age: float, remaining_years: float) -> str:
    """
    Generate an ASCII bar graph showing life progression by decades.
    
    Parameters:
        age: Current age of the person
        remaining_years: Calculated remaining years of life
    
    Returns:
        String representation of the bar graph where:
        █ represents lived years
        ░ represents remaining years
        Each line represents a decade
    """
    # Calculate total lifespan for visualization
    total_years = int(age + remaining_years)
    # Calculate how many decade rows we need
    decades = math.ceil(total_years / 10)
    
    # Store each line of the visualization
    visualization = []
    
    # Generate each decade row
    for decade in range(decades):
        # Calculate the year range for this decade
        start_year = decade * 10
        # Make sure we don't exceed total years for the last decade
        end_year = min(start_year + 10, total_years)
        
        # Build the bar for this decade
        bar = ""
        for year in range(start_year, end_year):
            # Fill with solid block for lived years, outline block for remaining
            if year < age:
                bar += "█"  # Lived year
            else:
                bar += "░"  # Remaining year
                
        # Format the decade range and add to visualization
        visualization.append(f"{start_year:2d}-{end_year-1:2d}: {bar}")
    
    # Join all decades into a single string with newlines
    return "\n".join(visualization)