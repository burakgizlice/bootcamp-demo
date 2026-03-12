import pytest
from src.kol import RobotikKol


class TestTemelHareketler:
    def setup_method(self):
        self.kol = RobotikKol()

    def test_yukari_kalk_y_pozisyonunu_dogru_artirir(self):
        self.kol.yukari_kalk(5)
        assert self.kol.y == 5

    def test_asagi_in_y_pozisyonunu_dogru_azaltir(self):
        self.kol.yukari_kalk(5)
        self.kol.asagi_in(3)
        assert self.kol.y == 2

    def test_asagi_in_sifirin_altina_inemez(self):
        self.kol.asagi_in(5)
        assert self.kol.y == 0

    def test_sola_git_x_pozisyonunu_dogru_azaltir(self):
        self.kol.sola_git(4)
        assert self.kol.x == -4

    def test_sola_git_eksi_on_sinirini_gecemez(self):
        self.kol.sola_git(15)
        assert self.kol.x == -10

    def test_saga_git_x_pozisyonunu_dogru_artirir(self):
        self.kol.saga_git(4)
        assert self.kol.x == 4

    def test_saga_git_arti_on_sinirini_gecemez(self):
        self.kol.saga_git(15)
        assert self.kol.x == 10


class TestDonus:
    def setup_method(self):
        self.kol = RobotikKol()

    def test_don_aciyi_dogru_degistirir(self):
        self.kol.don(90)
        assert self.kol.aci == 90

    def test_don_360_derecede_wrap_eder(self):
        self.kol.don(400)
        assert self.kol.aci == 40

    def test_don_negatif_aci_dogru_hesaplanir(self):
        self.kol.don(-90)
        assert self.kol.aci == 270


class TestPence:
    def setup_method(self):
        self.kol = RobotikKol()

    def test_tut_tutuyor_mu_true(self):
        self.kol.tut()
        assert self.kol.tutuyor_mu is True

    def test_birak_tutuyor_mu_false(self):
        self.kol.tut()
        self.kol.birak()
        assert self.kol.tutuyor_mu is False


class TestGuvenlikKontrolleri:
    def setup_method(self):
        self.kol = RobotikKol()

    def test_yukari_kalk_masa_yuksekligini_gecince_hata_firlatir(self):
        with pytest.raises(Exception, match="Kol masaya çarptı!"):
            self.kol.yukari_kalk(15)

    def test_pikapla_guvenli_yukseklikte_calisir(self):
        self.kol.pikapla()
        assert self.kol.tutuyor_mu is True
        assert self.kol.y == 0
