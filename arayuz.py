import sys
from PyQt5.QtWidgets import *
import temel_odev


class Pencere(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.odev_sec = QLabel("Uygulamak istediğiniz ödevi seçiniz:")
        self.to1_buton = QPushButton("Temel Ödev 1")
        self.to2_buton = QPushButton("Temel Ödev 2")
        self.to3_buton = QPushButton("Temel Ödev 3")
        self.to4_buton = QPushButton("Temel Ödev 4")
        self.brm_sec = QLabel("Lütfen açı birimini seçiniz:")
        self.derece = QRadioButton("Derece")
        self.grad = QRadioButton("Grad")
        self.sonuc_lable = QLabel("Sonuçlar:")
        self.sonuclar = QTextEdit()
        self.yazi = QLabel("KULLANIM KLAVUZU:\n1.Açı birimi seçiniz.\n2.Sonucunu istediğiniz temel ödevin boşluğunu belirtilen şekilde doldurunuz.\n3.Boşluk veya boşlukları doldurduktan sonra ilgili Temel Ödev butonuna basınız.\n4.Sonuçlarınızı aşağıda görebilirsiniz.")
        self.to1_lable = QLabel("Temel Ödev 1 : Verileri 'Ya,Xa,AB semt açısı,UzunlukAB' formatında giriniz.")
        self.to1_line = QLineEdit()
        self.to1_line.setPlaceholderText("Ya,Xa,AB semt açısı,UzunlukAB")
        self.to2_lable = QLabel("Temel Ödev 2 : Verileri 'Ya,Xa,Yb,Xb' formatında giriniz.")
        self.to2_line = QLineEdit()
        self.to2_line.setPlaceholderText("Ya,Xa,Yb,Xb")
        self.to3_lable = QLabel("Temel Ödev 3 : Verileri 'AB semt açısı,Beta açısı' formatında giriniz.")
        self.to3_line = QLineEdit()
        self.to3_line.setPlaceholderText("AB semt açısı,Beta açısı")
        self.to4_lable = QLabel("Temel Ödev 4 : Verileri 'Ya,Xa,Yb,Xb,Yc,Xc' formatında giriniz.")
        self.to4_line = QLineEdit()
        self.to4_line.setPlaceholderText("Ya,Xa,Yb,Xb,Yc,Xc")


        v_box1 = QVBoxLayout()

        v_box1.addWidget(self.to1_lable)
        v_box1.addWidget(self.to1_line)
        v_box1.addWidget(self.to2_lable)
        v_box1.addWidget(self.to2_line)
        v_box1.addWidget(self.to3_lable)
        v_box1.addWidget(self.to3_line)
        v_box1.addWidget(self.to4_lable)
        v_box1.addWidget(self.to4_line)
        v_box1.addWidget(self.sonuc_lable)
        v_box1.addWidget(self.sonuclar)


        v_box2 = QVBoxLayout()

        v_box2.addWidget(self.brm_sec)
        v_box2.addWidget(self.derece)
        v_box2.addWidget(self.grad)
        v_box2.addStretch()
        v_box2.addWidget(self.yazi)
        v_box2.addStretch()
        v_box2.addWidget(self.odev_sec)
        v_box2.addWidget(self.to1_buton)
        v_box2.addWidget(self.to2_buton)
        v_box2.addWidget(self.to3_buton)
        v_box2.addWidget(self.to4_buton)


        h_box = QHBoxLayout()

        h_box.addLayout(v_box1)
        h_box.addLayout(v_box2)

        self.setLayout(h_box)

        self.setWindowTitle("Temel Ödevler")

        self.to1_buton.clicked.connect(
            lambda: self.to1_click(self.derece.isChecked(), self.grad.isChecked(), self.sonuclar))
        self.to2_buton.clicked.connect(
            lambda: self.to2_click(self.derece.isChecked(), self.grad.isChecked(), self.sonuclar))
        self.to3_buton.clicked.connect(
            lambda: self.to3_click(self.derece.isChecked(), self.grad.isChecked(), self.sonuclar))
        self.to4_buton.clicked.connect(
            lambda: self.to4_click(self.derece.isChecked(), self.grad.isChecked(), self.sonuclar))


        self.show()


    def to1_click(self, derece, grad, sonuclar):
        if derece:
            aci_birim = "d"
            veriler = self.to1_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            semtAB = float(veriler[2])
            uzAB = float(veriler[3])
            sonuc = temel_odev.temel_odev1(Ya,Xa,semtAB,uzAB,aci_birim)
            self.sonuclar.setText(sonuc)

        if grad:
            aci_birim = "g"
            veriler = self.to1_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            semtAB = float(veriler[2])
            uzAB = float(veriler[3])
            sonuc = temel_odev.temel_odev1(Ya, Xa, semtAB, uzAB, aci_birim)
            self.sonuclar.setText(sonuc)


    def to2_click(self, derece, grad, sonuclar):
        if derece:
            aci_birim = "d"
            veriler = self.to2_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            Yb = float(veriler[2])
            Xb = float(veriler[3])
            sonuc = temel_odev.temel_odev2(Ya,Xa,Yb,Xb,aci_birim)
            self.sonuclar.setText("Semt Açısı = {} derece\nAB Kenar Uzunluğu = {} m.".format(sonuc[0],sonuc[1]))


        if grad:
            aci_birim = "g"
            veriler = self.to2_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            Yb = float(veriler[2])
            Xb = float(veriler[3])
            sonuc = temel_odev.temel_odev2(Ya, Xa, Yb, Xb, aci_birim)
            self.sonuclar.setText("Semt Açısı = {} grad\nAB Kenar Uzunluğu = {} m.".format(sonuc[0],sonuc[1]))

    def to3_click(self, derece, grad, sonuclar):
        if derece:
            aci_birim = "d"
            veriler = self.to3_line.text().split(",")
            semtAB = float(veriler[0])
            Beta = float(veriler[1])
            sonuc = temel_odev.temel_odev3(semtAB, Beta, aci_birim)
            self.sonuclar.setText(sonuc)
        if grad:
            aci_birim = "g"
            veriler = self.to3_line.text().split(",")
            semtAB = float(veriler[0])
            Beta = float(veriler[1])
            sonuc = temel_odev.temel_odev3(semtAB, Beta, aci_birim)
            self.sonuclar.setText(sonuc)

    def to4_click(self, derece, grad, sonuclar):
        if derece:
            aci_birim = "d"
            veriler = self.to4_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            Yb = float(veriler[2])
            Xb = float(veriler[3])
            Yc = float(veriler[4])
            Xc = float(veriler[5])
            sonuc = temel_odev.temel_odev4(Ya, Xa, Yb, Xb, Yc, Xc, aci_birim)
            self.sonuclar.setText(sonuc)
        if grad:
            aci_birim = "g"
            veriler = self.to4_line.text().split(",")
            Ya = float(veriler[0])
            Xa = float(veriler[1])
            Yb = float(veriler[2])
            Xb = float(veriler[3])
            Yc = float(veriler[4])
            Xc = float(veriler[5])

            sonuc = temel_odev.temel_odev4(Ya, Xa, Yb, Xb, Yc, Xc, aci_birim)
            self.sonuclar.setText(sonuc)


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
    