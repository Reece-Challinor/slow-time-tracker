"""
Calculates how time is typically allocated across different life activities,
helping visualize how much "free time" we really have.
"""

def calculate_time_allocation(remaining_years: float) -> dict:
    """
    Calculate how remaining time is typically allocated across different activities.
    Based on average time use surveys and studies.
    """
    # Convert years to hours for easier calculation
    total_hours = remaining_years * 365 * 24
    
    # Standard time allocation percentages
    SLEEP_PERCENT = 0.33  # 8 hours per day
    WORK_PERCENT = 0.23   # 40 hours per work week
    MAINTENANCE_PERCENT = 0.20  # Personal care, eating, etc.
    FREE_TIME_PERCENT = 0.24  # Truly discretionary time
    
    allocation = {
        'sleep': round(total_hours * SLEEP_PERCENT),
        'work': round(total_hours * WORK_PERCENT),
        'maintenance': round(total_hours * MAINTENANCE_PERCENT),
        'free_time': round(total_hours * FREE_TIME_PERCENT)
    }
    
    # Calculate "meaningful hours" - time you can actually use
    allocation['meaningful_hours'] = allocation['free_time']
    
    return allocation

def format_time_stats(time_dict: dict) -> dict:
    """Convert raw hours into more readable statistics."""
    stats = {}
    for key, hours in time_dict.items():
        stats[f'{key}_years'] = round(hours / (365 * 24), 1)
        stats[f'{key}_months'] = round(hours / (30 * 24), 1)
        stats[f'{key}_weeks'] = round(hours / (7 * 24), 1)
        stats[f'{key}_days'] = round(hours / 24, 1)
    return stats