from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.ship = self.loader.loadModel("./Assets/Spaceships/ship.obj")
        self.ship.reparentTo(self.render)
        self.ship.setScale(5)
        tex_ship = self.loader.loadTexture("./Assets/Spaceships/ship_TEX.tga")
        self.ship.setTexture(tex_ship, 1)
        self.ship.setPos(0, 200, 0)
        self.ship.setHpr(180, 90, 0)

        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render,
            "Universe", "./Assets/Universe/Universe.jpg", (0, 0, 0), 15000)

        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet1", "./Assets/Planets/Planet1.jpg", (-1500, 5000, 350), 100)

        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet2", "./Assets/Planets/Planet2.png", (4000, 3000, 400), 100)

        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet3", "./Assets/Planets/Planet3.png", (-4000, -2000, -400), 100)

        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet4", "./Assets/Planets/Planet4.png", (-2000, 1000, 450), 100)

        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet5", "./Assets/Planets/Planet5.png", (-1500, -3000, -100), 100)

        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render,
            "Planet6", "./Assets/Planets/Planet6.png", (2000, 6000, 0), 100)

        self.Station = self.loader.loadModel("./Assets/Space_Station/SpaceStation1B/spaceStation.egg")
        self.Station.reparentTo(self.render)
        self.Station.setScale(50)
        self.Station.setPos(5000, 4000, 70)

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)

            # self.DrawCloudDefense(self.Planet1, nickName)
            # self.DrawBaseballSeams(self.Station, nickName, j, fullCycle, 2)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "", self.render, droneName, "", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "", self.render, droneName, "", position, 10)







app = MyApp()
app.run()