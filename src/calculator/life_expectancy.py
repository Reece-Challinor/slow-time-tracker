"""
Life expectancy calculator that takes basic demographic and health factors
to estimate remaining life years. Uses simplified actuarial calculations
based on WHO data and general health factors.
"""

def calculate_base_expectancy(age: int, gender: str = 'neutral') -> float:
    # Base life expectancy of 80 years, adjusted for current age
    base_expectancy = 80 - age
    
    # Simple gender adjustment if provided
    if gender.lower() == 'female':
        base_expectancy += 5  # Women tend to live longer on average
    elif gender.lower() == 'male':
        base_expectancy -= 2
    
    return max(base_expectancy, 0)

def adjust_for_health_factors(base_years: float, bmi: float, smoker: bool) -> float:
    """Adjust life expectancy based on key health factors."""
    adjusted_years = base_years
    
    # BMI adjustments
    if bmi < 18.5:  # Underweight
        adjusted_years -= 2
    elif 25 <= bmi < 30:  # Overweight
        adjusted_years -= 1
    elif bmi >= 30:  # Obese
        adjusted_years -= 3
        
    # Smoking adjustment
    if smoker:
        adjusted_years -= 10
    
    return max(adjusted_years, 0)

def calculate_remaining_time(age: int, gender: str = 'neutral', 
                           bmi: float = 22, smoker: bool = False) -> dict:
    """
    Calculate remaining time in various units based on life expectancy.
    Returns a dictionary with years, months, weeks, and days remaining.
    """
    base_years = calculate_base_expectancy(age, gender)
    adjusted_years = adjust_for_health_factors(base_years, bmi, smoker)
    
    # Convert to various units
    months = adjusted_years * 12
    weeks = adjusted_years * 52
    days = adjusted_years * 365
    
    return {
        'years': round(adjusted_years, 1),
        'months': round(months, 1),
        'weeks': round(weeks, 1),
        'days': round(days, 1)
    }