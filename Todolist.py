

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# l'instance de mon application
app = FastAPI(titles = "Gestionnaires de taches: Todolist")

# ma liste python qui est comme ma base de data temporaire
tasks = []

#class tache qui herite de BaseModel
class Task(BaseModel):
    Id:int
    title: str 
    description: Optional[str] = None
    status: bool = False
    date: Optional[datetime] = None

# repertoire racine
@app.get("/")
def root():
    return {"message": "Bienvenue sur notre application Todolist"}

# creer une tache
@app.post("/task", response_model =Task)
async def Create_task(task: Task):
    tasks.append(task)
    return task

#lister toutes les taches
@app.get("/tasks", response_model = List[Task])
def list_tasks():
    return tasks

#lister les taches en utilisant la pagination
@app.get("/task/pagination", response_model = List[Task] )
def list_task_pagination(debut: int = 0, limit: int = 5) -> List[Task]:
    result = tasks[debut: debut + limit]
    return result

#afficher une tache precise
@app.get("/task{task_id}", response_model = Task)
async def afficher_task_precis(task_id: int):
    for task in tasks:
        if task.Id == task_id:
            return task
    raise HTTPException(status_code = 404, detail  = "task not found")

#afficher les taches faites
@app.get("/task{status_task}", response_model = List[Task])
def afficher_tache_faites(status_task: bool):
    task_do = [t for t in tasks if t.status == True]
    if not task_do:
        raise HTTPException(status_code = 404, detail  = "task not found")
    return task_do


#afficher les taches non faites
@app.get("/task{status_task}", response_model = List[Task])
def afficher_tache_non_faites(status_task: bool):
    tasks_not_do = [t for t in tasks if t.status == False]
    if not tasks_not_do:
        raise HTTPException(status_code = 404, detail  = "task not found")
    return tasks_not_do

#afficher les taches faites en une date donnee
@app.get("/task{date_precis}", response_model = List[Task])
def afficher_tache_faites_date_precise(date_precis: datetime):
    return [t for t in tasks if t.date == date_precis]

#supprimer en utilisant l'ID
@app.delete("/task{task_id}", response_model = List[Task])
def supp_use_ID(task_id: int):
    for task in tasks:
        if task.Id == task_id:
            tasks.remove(task)
            return tasks
    raise HTTPException(status_code=404, detail="task not found")

#modifier en utilisant l'ID
@app.put("/task{task_id}", response_model = Task) 
def modifier_use_ID(task_id: int, new_task:Task):
    for j,t in enumerate(tasks):
        if t.Id == task_id:
            tasks[j] = new_task
            return tasks[j]
    raise HTTPException(status_code=404, detail="task not found")

#supprimer en utilisant le titre
@app.delete("/task{task_title}", response_model = List[Task])
def supp_use_titre(task_title: str, new_task: Task):
    for task in tasks:
        if task.title == task_title:
            tasks.remove(task)
            return tasks
    raise HTTPException(status_code=404, detail="title not found")

#modifier en utilisant le titre         
@app.put("/task{task_title}", response_model = Task)
def modifier_use_ID(task_title: str, new_task:Task):
    for i, task in enumerate(tasks):
        if task.title == task_title:
           tasks[j] = new_task
    raise HTTPException(status_code=404, detail="title not found")

            




        


