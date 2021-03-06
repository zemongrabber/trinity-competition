import env_sim
import main
from tkinter import *
import time

s = env_sim.Simulation(width=100, height=100)
root = Tk()


def render():
    canvas.delete("all")
    for i in range(height):
        for j in range(width):
            if (res[i * j]) == None:
                pass
            else:
                canvas.create_rectangle(
                    j * 10,
                    i * 10,
                    j * 10 + 10,
                    i * 10 + 10,
                    fill=main.speciesColorDictionary[res[i * j]],
                )


# def beginClickDetection(animal):
#        global renderAnimal
#        renderAnimal = animal
#        canvas.bind("<Button-1>", click)
# def endClickDetection():
#        canvas.unbind("<Button-1>")

s.add_species(name="Lion", eats=["Zebra", "Vulture"])
s.add_species(name="Zebra", eats=["Grass"])
s.add_species(name="Vulture", eats=["Lion", "Zebra"])
s.add_species(name="Grass", eats=["sunlight"])
res, width, height = s.get_frame()
canvas = Canvas(root, width=width * 10, height=height * 10)
while True:
    res, width, height = s.get_frame()
    render()
    canvas.pack()
    s.advance()
    root.update()
    time.sleep(0.5)
