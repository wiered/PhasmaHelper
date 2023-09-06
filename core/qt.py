import sys 
import textwrap

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt6.QtGui import QFont

from lists import Ghosts_dict, evidences_dict, ghosts
from timers import Smudge_Timer, Attack_timer

app = QApplication(sys.argv)

screen_size = app.primaryScreen().availableGeometry()

def show_ghost(name):
    behavior = Ghosts_dict.gd().get(name).get("behavior")
    evidences = Ghosts_dict.gd().get(name).get("evidences")
    advantages = Ghosts_dict.gd().get(name).get("advantages")
    strategy = Ghosts_dict.gd().get(name).get("strategy")

    behavior = textwrap.fill(behavior, width=130)
    advantages = textwrap.fill(advantages, width=130)
    strategy = textwrap.fill(strategy, width=130)

    fin_str = ""
    fin_str += f"=================== {name} ====================\n"
    fin_str += behavior
    fin_str += "\n===================   Улики   ====================\n"
    fin_str += "; ".join(evidences)
    fin_str += "\n=================== Слабости  ====================\n"
    fin_str += advantages
    fin_str += "\n=================== Стратегия ====================\n"
    fin_str += strategy

    return fin_str

class MainWindow(QMainWindow):
    evd_btns = {}
    evds = []
    ghost_btns = {}
    checkers = {
        "EMF": False,
        "Spirit_Box": False,
        "Fingerprints": False,
        "Ghost_Orb": False,
        "Ghost_Writing": False,
        "Freezing_Temp": False,
        "DOTS": False
    }
    def __init__(self):
        super().__init__()

        wid = QWidget(self)

        main_layout = QHBoxLayout()

        gh_btns_layout = QVBoxLayout()

        self.EMF_button_is_checked = False
        self.Spirit_Box_button_is_checked = False
        self.Fingerprints_button_is_checked = False
        self.Ghost_Orb_button_is_checked = False
        self.Ghost_Writing_button_is_checked = False
        self.Freezing_Temp_button_is_checked = False
        self.DOTS_button_is_checked = False

        Дух_btn = QPushButton('Дух')
        Дух_btn.toggle()
        Дух_btn.clicked.connect(lambda:self.get_ghost(Дух_btn))
        gh_btns_layout.addWidget(Дух_btn)

        Мираж_btn = QPushButton('Мираж')
        Мираж_btn.toggle()
        Мираж_btn.clicked.connect(lambda:self.get_ghost(Мираж_btn))
        gh_btns_layout.addWidget(Мираж_btn)

        Фантом_btn = QPushButton('Фантом')
        Фантом_btn.toggle()
        Фантом_btn.clicked.connect(lambda:self.get_ghost(Фантом_btn))
        gh_btns_layout.addWidget(Фантом_btn)

        Полтергейст_btn = QPushButton('Полтергейст')
        Полтергейст_btn.toggle()
        Полтергейст_btn.clicked.connect(lambda:self.get_ghost(Полтергейст_btn))
        gh_btns_layout.addWidget(Полтергейст_btn)

        Банши_btn = QPushButton('Банши')
        Банши_btn.toggle()
        Банши_btn.clicked.connect(lambda:self.get_ghost(Банши_btn))
        gh_btns_layout.addWidget(Банши_btn)

        Джинн_btn = QPushButton('Джинн')
        Джинн_btn.toggle()
        Джинн_btn.clicked.connect(lambda:self.get_ghost(Джинн_btn))
        gh_btns_layout.addWidget(Джинн_btn)

        Мара_btn = QPushButton('Мара')
        Мара_btn.toggle()
        Мара_btn.clicked.connect(lambda:self.get_ghost(Мара_btn))
        gh_btns_layout.addWidget(Мара_btn)

        Ревенант_btn = QPushButton('Ревенант')
        Ревенант_btn.toggle()
        Ревенант_btn.clicked.connect(lambda:self.get_ghost(Ревенант_btn))
        gh_btns_layout.addWidget(Ревенант_btn)

        Тень_btn = QPushButton('Тень')
        Тень_btn.toggle()
        Тень_btn.clicked.connect(lambda:self.get_ghost(Тень_btn))
        gh_btns_layout.addWidget(Тень_btn)

        Демон_btn = QPushButton('Демон')
        Демон_btn.toggle()
        Демон_btn.clicked.connect(lambda:self.get_ghost(Демон_btn))
        gh_btns_layout.addWidget(Демон_btn)

        Юрэй_btn = QPushButton('Юрэй')
        Юрэй_btn.toggle()
        Юрэй_btn.clicked.connect(lambda:self.get_ghost(Юрэй_btn))
        gh_btns_layout.addWidget(Юрэй_btn)

        Они_btn = QPushButton('Они')
        Они_btn.toggle()
        Они_btn.clicked.connect(lambda:self.get_ghost(Они_btn))
        gh_btns_layout.addWidget(Они_btn)

        Ёкай_btn = QPushButton('Ёкай')
        Ёкай_btn.toggle()
        Ёкай_btn.clicked.connect(lambda:self.get_ghost(Ёкай_btn))
        gh_btns_layout.addWidget(Ёкай_btn)

        Ханту_btn = QPushButton('Ханту')
        Ханту_btn.toggle()
        Ханту_btn.clicked.connect(lambda:self.get_ghost(Ханту_btn))
        gh_btns_layout.addWidget(Ханту_btn)

        Горё_btn = QPushButton('Горё')
        Горё_btn.toggle()
        Горё_btn.clicked.connect(lambda:self.get_ghost(Горё_btn))
        gh_btns_layout.addWidget(Горё_btn)

        Мюлинг_btn = QPushButton('Мюлинг')
        Мюлинг_btn.toggle()
        Мюлинг_btn.clicked.connect(lambda:self.get_ghost(Мюлинг_btn))
        gh_btns_layout.addWidget(Мюлинг_btn)

        Онрё_btn = QPushButton('Онрё')
        Онрё_btn.toggle()
        Онрё_btn.clicked.connect(lambda:self.get_ghost(Онрё_btn))
        gh_btns_layout.addWidget(Онрё_btn)

        Близнецы_btn = QPushButton('Близнецы')
        Близнецы_btn.toggle()
        Близнецы_btn.clicked.connect(lambda:self.get_ghost(Близнецы_btn))
        gh_btns_layout.addWidget(Близнецы_btn)

        Райдзю_btn = QPushButton('Райдзю')
        Райдзю_btn.toggle()
        Райдзю_btn.clicked.connect(lambda:self.get_ghost(Райдзю_btn))
        gh_btns_layout.addWidget(Райдзю_btn)

        Обакэ_btn = QPushButton('Обакэ')
        Обакэ_btn.toggle()
        Обакэ_btn.clicked.connect(lambda:self.get_ghost(Обакэ_btn))
        gh_btns_layout.addWidget(Обакэ_btn)

        Мимик_btn = QPushButton('Мимик')
        Мимик_btn.toggle()
        Мимик_btn.clicked.connect(lambda:self.get_ghost(Мимик_btn))
        gh_btns_layout.addWidget(Мимик_btn)

        Морой_btn = QPushButton('Морой')
        Морой_btn.toggle()
        Морой_btn.clicked.connect(lambda:self.get_ghost(Морой_btn))
        gh_btns_layout.addWidget(Морой_btn)

        Деоген_btn = QPushButton('Деоген')
        Деоген_btn.toggle()
        Деоген_btn.clicked.connect(lambda:self.get_ghost(Деоген_btn))
        gh_btns_layout.addWidget(Деоген_btn)

        Тайэ_btn = QPushButton('Тайэ')
        Тайэ_btn.toggle()
        Тайэ_btn.clicked.connect(lambda:self.get_ghost(Тайэ_btn))
        gh_btns_layout.addWidget(Тайэ_btn)

        MainWindow.ghost_btns = {
            "Дух": Дух_btn,
            "Мираж": Мираж_btn,
            "Фантом": Фантом_btn,
            "Полтергейст": Полтергейст_btn,
            "Банши": Банши_btn,
            "Джинн": Джинн_btn,
            "Мара": Мара_btn,
            "Ревенант": Ревенант_btn,
            "Тень": Тень_btn,
            "Демон": Демон_btn,
            "Юрэй": Юрэй_btn,
            "Они": Они_btn,
            "Ёкай": Ёкай_btn,
            "Ханту": Ханту_btn,
            "Горё": Горё_btn,
            "Мюлинг": Мюлинг_btn,
            "Онрё": Онрё_btn,
            "Близнецы": Близнецы_btn,
            "Райдзю": Райдзю_btn,
            "Обакэ": Обакэ_btn,
            "Мимик": Мимик_btn,
            "Морой": Морой_btn,
            "Деоген": Деоген_btn,
            "Тайэ": Тайэ_btn
        }

        evd_btns_layout = QVBoxLayout()

        EMF_btn = QPushButton('EMF')
        EMF_btn.toggle()
        EMF_btn.setCheckable(True)
        EMF_btn.clicked.connect(lambda:self.evd_edit(EMF_btn))
        EMF_btn.setChecked(self.EMF_button_is_checked)
        evd_btns_layout.addWidget(EMF_btn)

        Spirit_Box_btn = QPushButton('Spirit_Box')
        Spirit_Box_btn.toggle()
        Spirit_Box_btn.setCheckable(True)
        Spirit_Box_btn.clicked.connect(lambda:self.evd_edit(Spirit_Box_btn))
        Spirit_Box_btn.setChecked(self.Spirit_Box_button_is_checked)
        evd_btns_layout.addWidget(Spirit_Box_btn)

        Fingerprints_btn = QPushButton('Fingerprints')
        Fingerprints_btn.toggle()
        Fingerprints_btn.setCheckable(True)
        Fingerprints_btn.clicked.connect(lambda:self.evd_edit(Fingerprints_btn))
        Fingerprints_btn.setChecked(self.Fingerprints_button_is_checked)
        evd_btns_layout.addWidget(Fingerprints_btn)

        Ghost_Orb_btn = QPushButton('Ghost_Orb')
        Ghost_Orb_btn.toggle()
        Ghost_Orb_btn.setCheckable(True)
        Ghost_Orb_btn.clicked.connect(lambda:self.evd_edit(Ghost_Orb_btn))
        Ghost_Orb_btn.setChecked(self.Ghost_Orb_button_is_checked)
        evd_btns_layout.addWidget(Ghost_Orb_btn)

        Ghost_Writing_btn = QPushButton('Ghost_Writing')
        Ghost_Writing_btn.toggle()
        Ghost_Writing_btn.setCheckable(True)
        Ghost_Writing_btn.clicked.connect(lambda:self.evd_edit(Ghost_Writing_btn))
        Ghost_Writing_btn.setChecked(self.Ghost_Writing_button_is_checked)
        evd_btns_layout.addWidget(Ghost_Writing_btn)
        
        Freezing_Temp_btn = QPushButton('Freezing_Temp')
        Freezing_Temp_btn.toggle()
        Freezing_Temp_btn.setCheckable(True)
        Freezing_Temp_btn.clicked.connect(lambda:self.evd_edit(Freezing_Temp_btn))
        Freezing_Temp_btn.setChecked(self.Freezing_Temp_button_is_checked)
        evd_btns_layout.addWidget(Freezing_Temp_btn)

        DOTS_btn = QPushButton('DOTS')
        DOTS_btn.toggle()
        DOTS_btn.setCheckable(True)
        DOTS_btn.clicked.connect(lambda:self.evd_edit(DOTS_btn))
        DOTS_btn.setChecked(self.DOTS_button_is_checked)
        evd_btns_layout.addWidget(DOTS_btn)

        attack_timer_box = QComboBox()
        attack_timer_box.addItems(["33", "53", "63"])
        attack_timer_box.currentTextChanged.connect(self.attack_timer_changed)
        evd_btns_layout.addWidget(attack_timer_box)

        Quit_btn = QPushButton('Quit')
        Quit_btn.toggle()
        Quit_btn.clicked.connect(lambda:self.quit_btn_pressed())
        evd_btns_layout.addWidget(Quit_btn)

        MainWindow.evd_btns = {
            EMF_btn: "evd",
            Spirit_Box_btn: "evd",
            Fingerprints_btn: "evd",
            Ghost_Orb_btn: "evd",
            Ghost_Writing_btn: "evd",
            Freezing_Temp_btn: "evd",
            DOTS_btn: "evd"
        }
        
        self.smudge_timer = Smudge_Timer()
        self.smudge_timer.show()
        self.smudge_timer.location_on_the_screen()

        self.attack_timer = Attack_timer()
        self.attack_timer.show()
        self.attack_timer.location_on_the_screen()

        main_layout.addLayout(evd_btns_layout)
        main_layout.addLayout(gh_btns_layout)

        wid.setLayout(main_layout)
        self.setWindowTitle("Phasma Helper")
        self.setMinimumSize(QSize(screen_size.width()//7, screen_size.height()//4))
        self.setCentralWidget(wid)
        self.show()

    def keyPressEvent(self, event):
        print(event.text())
        match event.text():
            case '5':
                self.smudge_timer.startTimer()
            case '8':
                self.smudge_timer.endTimer()
            case '6':
                self.attack_timer.startTimer()
            case '9':
                self.attack_timer.endTimer()
    
    def attack_timer_changed(self, s):
        self.attack_timer.times = int(s)

    def quit_btn_pressed(self):
        self.smudge_timer.close()
        self.attack_timer.close()
        #self.wd.close()
        self.close()

    def get_ghost(self, b):
        Ghosts_dict.reload()
        
        self.wd = InfoWindow(b.text())
        self.wd.location_on_the_screen()
        self.wd.show()

    def evd_edit(self, b):
        if not MainWindow.checkers.get(b.text()):
            MainWindow.evds.append(b.text())
        else:
            MainWindow.evds.remove(b.text())
        MainWindow.checkers[b.text()] = not MainWindow.checkers.get(b.text())

        evd_ghosts = ghosts
        for evd in MainWindow.evds:
            ghosts1 = evidences_dict.get(evd.replace("_", " "))
            evd_ghosts = list(set(evd_ghosts) & set(ghosts1))
        for ghost in ghosts:
            if ghost not in evd_ghosts:
                btn = MainWindow.ghost_btns.get(ghost)
                btn.setEnabled(False)
            else:
                btn = MainWindow.ghost_btns.get(ghost)
                btn.setEnabled(True)
    
class InfoWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()

        label = QLabel()
        label.setFont(QFont('Arial', 7))
        label.setText(show_ghost(name))
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setWindowTitle("Phasma Helper")
        self.setMinimumSize(QSize(screen_size.width()//4, screen_size.height()//4))
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        self.setCentralWidget(label)


    def location_on_the_screen(self):
        ag = app.primaryScreen().availableGeometry()
        sg = app.primaryScreen().size()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)


def main():
    #app.setStyleSheet("QLabel{font-size: 7pt;}")

    window = MainWindow()

    app.exec()

if __name__ == '__main__':
   main()

