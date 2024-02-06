from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  print("Welcome to cringineering. Be cautious, you may die of cringe")

@app.get("/register")
async def register():
  print("Your name would be: cringee123.")
  
@app.get("/cringee123")
async def show_faces():
  print("Cringee123. Faces")
  
@app.get("/cringee123/friends")
async def show_friends():
  print("Here are your cringineers")

@app.get("/cringee123/cringinews")
async def show_other_cringineers():
  print("Here are ugly guys")

@app.get("/cringee123/stickerpacks")
async def create_stickerpack():
  print("Here are your stickerpacks")