class RobotikKol:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aci = 0
        self.tutuyor_mu = False
        self.masa_yuksekligi = 10

    def yukari_kalk(self, miktar):
        if self.y + miktar > self.masa_yuksekligi:
            raise Exception("Kol masaya çarptı!")
        self.y += miktar

    def asagi_in(self, miktar):
        self.y = max(0, self.y - miktar)

    def sola_git(self, miktar):
        self.x = max(-10, self.x - miktar)

    def saga_git(self, miktar):
        self.x = min(10, self.x + miktar)

    def don(self, derece):
        self.aci = ((self.aci + derece) % 360 + 360) % 360

    def tut(self):
        self.tutuyor_mu = True

    def birak(self):
        self.tutuyor_mu = False

    def pikapla(self):
        self.yukari_kalk(3)
        self.tut()
        self.asagi_in(3)
