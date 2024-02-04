import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUIdemo import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("GroupImpact_Point Group")

    def PageSet_1(self):
        self.stackedWidget.setCurrentIndex(0)

    def PageSet_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def PageSet_3(self):
        self.stackedWidget.setCurrentIndex(2)

    def run_Cn_group(self):
        n = self.Cn_spinBox_n.value()
        m = self.Cn_spinBox_m.value()
        if n < m:
            QMessageBox.critical(self, "Error", "n should be no smaller than m!!!")
            return
        os.system(f"python ../Point_group/Cn_group.py {n} {m}")

    def run_Dn_group(self):
        n = self.Dn_spinBox_n.value()
        os.system(f"python ../Point_group/Dn_group.py {n}")

    def run_T_group(self):
        os.system(f"python ../Point_group/T_group.py")

    def run_O_group(self):
        os.system(f"python ../Point_group/O_group.py")

    def run_Y_group(self):
        os.system(f"python ../Point_group/Y_group.py")

    def run_Cnh_group(self):
        n = self.Cnh_spinBox_n.value()
        m = self.Cnh_spinBox_m.value()
        if n < m:
            QMessageBox.critical(self, "Error", "n should be no smaller than m!!!")
            return
        ref_num = self.Cnh_spinBox_ref.value()
        if ref_num == 1:
            ref = True
        else:
            ref = False
        os.system(f"python ../Point_group/Cnh_group.py {n} {m} {ref}")

    def run_Cnv_group(self):
        n = self.Cnv_spinBox_n.value()
        os.system(f"python ../Point_group/Cnv_group.py {n}")

    def run_Dnh_group(self):
        n = self.Dnh_spinBox_n.value()
        os.system(f"python ../Point_group/Dnh_group.py {n}")

    def run_Dnd_group(self):
        n = self.Dnd_spinBox_n.value()
        os.system(f"python ../Point_group/Dnd_group.py {n}")

    def run_Sn_group(self):
        n = self.Sn_spinBox_n.value()
        m = self.Sn_spinBox_m.value()
        if n < m:
            QMessageBox.critical(self, "Error", "n should be no smaller than m!!!")
            return
        os.system(f"python ../Point_group/Sn_group.py {n} {m}")

    def run_Th_group(self):
        os.system(f"python ../Point_group/Th_group.py")

    def run_Td_group(self):
        os.system(f"python ../Point_group/Td_group.py")

    def run_Oh_group(self):
        os.system(f"python ../Point_group/Oh_group.py")

    def run_Yh_group(self):
        os.system(f"python ../Point_group/Yh_group.py")

    def run_C1_group(self):
        os.system(f"python ../Crystal_Point_group/Cn_group.py 1")

    def run_C2_group(self):
        os.system(f"python ../Crystal_Point_group/Cn_group.py 2")

    def run_C3_group(self):
        os.system(f"python ../Crystal_Point_group/Cn_group.py 3")

    def run_C4_group(self):
        os.system(f"python ../Crystal_Point_group/Cn_group.py 4")

    def run_C6_group(self):
        os.system(f"python ../Crystal_Point_group/Cn_group.py 6")

    def run_D2_group(self):
        os.system(f"python ../Crystal_Point_group/Dn_group.py 2")

    def run_D3_group(self):
        os.system(f"python ../Crystal_Point_group/Dn_group.py 3")

    def run_D4_group(self):
        os.system(f"python ../Crystal_Point_group/Dn_group.py 4")

    def run_D6_group(self):
        os.system(f"python ../Crystal_Point_group/Dn_group.py 6")

    def run_S2_group(self):
        os.system(f"python ../Crystal_Point_group/Sn_group.py 2")

    def run_S4_group(self):
        os.system(f"python ../Crystal_Point_group/Sn_group.py 4")

    def run_S6_group(self):
        os.system(f"python ../Crystal_Point_group/Sn_group.py 6")

    def run_C1h_group(self):
        os.system(f"python ../Crystal_Point_group/Cnh_group.py 1")

    def run_C2h_group(self):
        os.system(f"python ../Crystal_Point_group/Cnh_group.py 2")

    def run_C3h_group(self):
        os.system(f"python ../Crystal_Point_group/Cnh_group.py 3")

    def run_C4h_group(self):
        os.system(f"python ../Crystal_Point_group/Cnh_group.py 4")

    def run_C6h_group(self):
        os.system(f"python ../Crystal_Point_group/Cnh_group.py 6")

    def run_C2v_group(self):
        os.system(f"python ../Crystal_Point_group/Cnv_group.py 2")

    def run_C3v_group(self):
        os.system(f"python ../Crystal_Point_group/Cnv_group.py 3")

    def run_C4v_group(self):
        os.system(f"python ../Crystal_Point_group/Cnv_group.py 4")

    def run_C6v_group(self):
        os.system(f"python ../Crystal_Point_group/Cnv_group.py 6")

    def run_D2h_group(self):
        os.system(f"python ../Crystal_Point_group/Dnh_group.py 2")

    def run_D3h_group(self):
        os.system(f"python ../Crystal_Point_group/Dnh_group.py 3")

    def run_D4h_group(self):
        os.system(f"python ../Crystal_Point_group/Dnh_group.py 4")

    def run_D6h_group(self):
        os.system(f"python ../Crystal_Point_group/Dnh_group.py 6")

    def run_D2d_group(self):
        os.system(f"python ../Crystal_Point_group/Dnd_group.py 2")

    def run_D3d_group(self):
        os.system(f"python ../Crystal_Point_group/Dnd_group.py 3")

    def run_HM_1(self):
        os.system(f"python ../Hermann-Mauguin/HM_n.py 1")

    def run_HM_2(self):
        os.system(f"python ../Hermann-Mauguin/HM_n.py 2")

    def run_HM_3(self):
        os.system(f"python ../Hermann-Mauguin/HM_n.py 3")

    def run_HM_4(self):
        os.system(f"python ../Hermann-Mauguin/HM_n.py 4")

    def run_HM_6(self):
        os.system(f"python ../Hermann-Mauguin/HM_n.py 6")

    def run_HM_bar_1(self):
        os.system(f"python ../Hermann-Mauguin/HM_bar_n.py 1")

    def run_HM_bar_3(self):
        os.system(f"python ../Hermann-Mauguin/HM_bar_n.py 3")

    def run_HM_bar_4(self):
        os.system(f"python ../Hermann-Mauguin/HM_bar_n.py 4")

    def run_HM_bar_6(self):
        os.system(f"python ../Hermann-Mauguin/HM_bar_n.py 6")

    def run_HM_D2(self):
        os.system(f"python ../Hermann-Mauguin/HM_D.py 2")

    def run_HM_D3(self):
        os.system(f"python ../Hermann-Mauguin/HM_D.py 3")

    def run_HM_D4(self):
        os.system(f"python ../Hermann-Mauguin/HM_D.py 4")

    def run_HM_D6(self):
        os.system(f"python ../Hermann-Mauguin/HM_D.py 6")

    def run_HM_T(self):
        os.system(f"python ../Hermann-Mauguin/HM_T.py")

    def run_HM_O(self):
        os.system(f"python ../Hermann-Mauguin/HM_O.py")

    def run_HM_Y(self):
        os.system(f"python ../Hermann-Mauguin/HM_Y.py")

    def run_HM_C1h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Ch.py 1")

    def run_HM_C2h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Ch.py 2")

    def run_HM_C4h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Ch.py 4")

    def run_HM_C6h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Ch.py 6")

    def run_HM_C2v(self):
        os.system(f"python ../Hermann-Mauguin/HM_Cv.py 2")

    def run_HM_C3v(self):
        os.system(f"python ../Hermann-Mauguin/HM_Cv.py 3")

    def run_HM_C4v(self):
        os.system(f"python ../Hermann-Mauguin/HM_Cv.py 4")

    def run_HM_C6v(self):
        os.system(f"python ../Hermann-Mauguin/HM_Cv.py 6")

    def run_HM_D2h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dh.py 2")

    def run_HM_D3h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dh.py 3")

    def run_HM_D4h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dh.py 4")

    def run_HM_D6h(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dh.py 6")

    def run_HM_D2d(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dd.py 2")

    def run_HM_D3d(self):
        os.system(f"python ../Hermann-Mauguin/HM_Dd.py 3")

    def run_HM_Th(self):
        os.system(f"python ../Hermann-Mauguin/HM_Th.py")

    def run_HM_Td(self):
        os.system(f"python ../Hermann-Mauguin/HM_Td.py")

    def run_HM_Oh(self):
        os.system(f"python ../Hermann-Mauguin/HM_Oh.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
