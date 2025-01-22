from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from calculator import calculate_project_cost 

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("calculator_form.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, 
                    monthly_income_goal: float = Form(...), 
                    daily_hours: int = Form(...), 
                    weekly_days: int = Form(...), 
                    vacation_weeks: int = Form(...), 
                    project_hours_per_day: float = Form(...), 
                    project_days: int = Form(...)):
    result = calculate_project_cost(
        monthly_income_goal, daily_hours, weekly_days, vacation_weeks,
        project_hours_per_day, project_days
    )
    return templates.TemplateResponse("result.html", {
        "request": request,
        "hourly_rate": result["hourly_rate"],
        "total_hours": result["total_hours"],
        "estimated_cost": result["project_cost"]
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
