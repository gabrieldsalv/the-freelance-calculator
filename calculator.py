def calculate_project_cost(
    monthly_income_goal,  # renda mensal
    daily_hours,          # horas diárias de trabalho
    weekly_days,          # quantidade de dias trabalhados por semana
    vacation_weeks,       # quantidade de semanas de férias
    project_hours_per_day, # horas diárias para o projeto
    project_days          # quantidade de dias para o projeto ser finalizado
):
    # calcular horas anuais
    annual_hours = (weekly_days * daily_hours) * (52 - vacation_weeks)
    
    # valor final da hora
    hourly_rate = (monthly_income_goal * 12) / annual_hours
    
    # calcular custo total do projeto
    project_total_hours = project_hours_per_day * project_days
    project_cost = project_total_hours * hourly_rate
    
    return {
        "hourly_rate": round(hourly_rate, 2),
        "project_cost": round(project_cost, 2),
        "total_hours": project_total_hours
    }
