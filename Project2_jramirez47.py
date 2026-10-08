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

        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex_UNI = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex_UNI, 1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setScale(100)
        self.Planet1.setPos(-1500, 5000, 350)
        tex1 = self.loader.loadTexture("./Assets/Planets/Planet1.jpg")
        self.Planet1.setTexture(tex1, 1)

        # Add the class here from SpaceJamClasses. Below is an example.
        # self.Planet1 = spaceJamClasses.Planet(self.loader, "./")

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setScale(100)
        self.Planet2.setPos(4000, 3000, 400)
        tex2 = self.loader.loadTexture("./Assets/Planets/Planet2.png")
        self.Planet2.setTexture(tex2, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setScale(100)
        self.Planet3.setPos(-4000, -2000, -400)
        tex3 = self.loader.loadTexture("./Assets/Planets/Planet3.png")
        self.Planet3.setTexture(tex3, 1)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setScale(100)
        self.Planet4.setPos(-2000, 1000, 450)
        tex4 = self.loader.loadTexture("./Assets/Planets/Planet4.png")
        self.Planet4.setTexture(tex4, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setScale(100)
        self.Planet5.setPos(-1500, -3000, -100)
        tex5 = self.loader.loadTexture("./Assets/Planets/Planet5.png")
        self.Planet5.setTexture(tex5, 1)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setScale(150)
        self.Planet6.setPos(2000, 6000, 0)
        tex6 = self.loader.loadTexture("./Assets/Planets/Planet6.png")
        self.Planet6.setTexture(tex6, 1)

        self.Station = self.loader.loadModel("./Assets/Space_Station/SpaceStation1B/spaceStation.egg")
        self.Station.reparentTo(self.render)
        self.Station.setScale(50)
        self.Station.setPos(5000, 4000, 70)

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.self.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.self.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Station, nickName, j, fullCycle, 1)

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