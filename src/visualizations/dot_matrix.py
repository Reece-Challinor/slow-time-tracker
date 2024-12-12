"""
Generates ASCII dot matrix visualization of time remaining.
"""

def generate_dot_matrix(months_lived: int, months_remaining: int, months_per_row: int = 12) -> str:
    """Generate a dot matrix visualization of life months."""
    total_months = months_lived + months_remaining
    rows = []
    
    for i in range(0, total_months, months_per_row):
        row = []
        for j in range(months_per_row):
            if i + j >= total_months:
                break
            if i + j < months_lived:
                row.append("●")
            else:
                row.append("○")
        rows.append(f"{i//12 + 1:2d}: {' '.join(row)}")
    
    return "\n".join(rows)