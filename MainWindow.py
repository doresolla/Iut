from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from pyqtgraph import PlotWidget


class NumericDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QtWidgets.QLineEdit):
            reg_ex = QRegularExpression("[0-9]+.?[0-9]{,4}")
            validator = QRegularExpressionValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor


class CTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)
        self.keys = [QtCore.Qt.Key.Key_Left,QtCore.Qt.Key.Key_Right, QtCore.Qt.Key.Key_Down, QtCore.Qt.Key.Key_Up]
        self.keyPressEvent = self.keyPress
        self.context_menu = QtWidgets.QMenu(self)
        delete_menu = self.context_menu.addAction("Удалить строку")
        delete_menu.triggered.connect(self.deleteRow)

    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())

    def deleteRow(self):
        row = self.currentRow()
        if row > -1:
            self.removeRow(row)
            self.selectionModel().clearCurrentIndex()

    def keyPress(self, e):
        QtWidgets.QTableWidget.keyPressEvent(self, e)
        self._moveCursor(e.key())

    def _moveCursor(self, key):
        row = self.currentRow()
        col = self.currentColumn()
        if (key == QtCore.Qt.Key.Key_Down) and (row  == self.rowCount() - 1):
            self.AddRow()
            self.setCurrentCell(row+1, col)
    def AddRow(self):
        self.insertRow(self.rowCount())
    #    delegate = NumericDelegate(self)
   #     self.setItemDelegateForColumn(2, delegate)
        self.createCheck(self.rowCount() - 1)

    def createCheck(self, row=0):
        cell_widget = QtWidgets.QWidget()
        chk_bx = QtWidgets.QCheckBox()
        chk_bx.setCheckState(QtCore.Qt.CheckState.Checked)
        lay_out = QtWidgets.QHBoxLayout(cell_widget)
        lay_out.addWidget(chk_bx)
        lay_out.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)
        self.setCellWidget(row, 0, cell_widget)

    def FormatTable(self):
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.setRowCount(1)
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1484, 878)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.i1radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.i1radio.setObjectName("i1radio")
        self.verticalLayout_2.addWidget(self.i1radio)
        self.i2radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.i2radio.setObjectName("i2radio")
        self.verticalLayout_2.addWidget(self.i2radio)
        self.i3radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.i3radio.setObjectName("i3radio")
        self.verticalLayout_2.addWidget(self.i3radio)
        self.i4radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.i4radio.setObjectName("i4radio")
        self.verticalLayout_2.addWidget(self.i4radio)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget1 = CTableWidget(parent=self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget1.sizePolicy().hasHeightForWidth())
        self.tableWidget1.setSizePolicy(sizePolicy)
        self.tableWidget1.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget1.setBaseSize(QtCore.QSize(0, 100))
        self.tableWidget1.setLineWidth(5)
        self.tableWidget1.setMidLineWidth(1)
        self.tableWidget1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget1.setRowCount(0)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setObjectName("tableWidget1")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        self.tableWidget1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget1.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab1)
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.relHumidity1 = QtWidgets.QTextEdit(parent=self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relHumidity1.sizePolicy().hasHeightForWidth())
        self.relHumidity1.setSizePolicy(sizePolicy)
        self.relHumidity1.setMaximumSize(QtCore.QSize(150, 30))
        self.relHumidity1.setObjectName("relHumidity1")
        self.verticalLayout_3.addWidget(self.relHumidity1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(parent=self.tab1)
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.length = QtWidgets.QTextEdit(parent=self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMaximumSize(QtCore.QSize(150, 30))
        self.length.setObjectName("length")
        self.verticalLayout_3.addWidget(self.length)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButton1 = QtWidgets.QPushButton(parent=self.tab1)
        self.pushButton1.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout_3.addWidget(self.pushButton1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget2 = CTableWidget(parent=self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget2.sizePolicy().hasHeightForWidth())
        self.tableWidget2.setSizePolicy(sizePolicy)
        self.tableWidget2.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget2.setBaseSize(QtCore.QSize(0, 100))
        self.tableWidget2.setLineWidth(5)
        self.tableWidget2.setMidLineWidth(1)
        self.tableWidget2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.setObjectName("tableWidget2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        self.tableWidget2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.tableWidget2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(parent=self.tab2)
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.relHumidity2 = QtWidgets.QTextEdit(parent=self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relHumidity2.sizePolicy().hasHeightForWidth())
        self.relHumidity2.setSizePolicy(sizePolicy)
        self.relHumidity2.setMaximumSize(QtCore.QSize(150, 30))
        self.relHumidity2.setObjectName("relHumidity2")
        self.verticalLayout_12.addWidget(self.relHumidity2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.label_12 = QtWidgets.QLabel(parent=self.tab2)
        self.label_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_12.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        self.length2 = QtWidgets.QTextEdit(parent=self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length2.sizePolicy().hasHeightForWidth())
        self.length2.setSizePolicy(sizePolicy)
        self.length2.setMaximumSize(QtCore.QSize(150, 30))
        self.length2.setObjectName("length2")
        self.verticalLayout_12.addWidget(self.length2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem7)
        self.pushButton2 = QtWidgets.QPushButton(parent=self.tab2)
        self.pushButton2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout_12.addWidget(self.pushButton2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tableWidget3 = CTableWidget(parent=self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget3.sizePolicy().hasHeightForWidth())
        self.tableWidget3.setSizePolicy(sizePolicy)
        self.tableWidget3.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget3.setBaseSize(QtCore.QSize(0, 100))
        self.tableWidget3.setLineWidth(5)
        self.tableWidget3.setMidLineWidth(1)
        self.tableWidget3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget3.setRowCount(0)
        self.tableWidget3.setColumnCount(3)
        self.tableWidget3.setObjectName("tableWidget3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget3.setHorizontalHeaderItem(2, item)
        self.tableWidget3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget3.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_14.addWidget(self.tableWidget3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(parent=self.tab3)
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        spacerItem8 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem8)
        self.relHumidity3 = QtWidgets.QTextEdit(parent=self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relHumidity3.sizePolicy().hasHeightForWidth())
        self.relHumidity3.setSizePolicy(sizePolicy)
        self.relHumidity3.setMaximumSize(QtCore.QSize(150, 30))
        self.relHumidity3.setObjectName("relHumidity3")
        self.verticalLayout_13.addWidget(self.relHumidity3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.label_14 = QtWidgets.QLabel(parent=self.tab3)
        self.label_14.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_14.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        spacerItem10 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem10)
        self.length3 = QtWidgets.QTextEdit(parent=self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length3.sizePolicy().hasHeightForWidth())
        self.length3.setSizePolicy(sizePolicy)
        self.length3.setMaximumSize(QtCore.QSize(150, 30))
        self.length3.setObjectName("length3")
        self.verticalLayout_13.addWidget(self.length3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem11)
        self.pushButton3 = QtWidgets.QPushButton(parent=self.tab3)
        self.pushButton3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout_13.addWidget(self.pushButton3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tableWidget4 = CTableWidget(parent=self.tab4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget4.sizePolicy().hasHeightForWidth())
        self.tableWidget4.setSizePolicy(sizePolicy)
        self.tableWidget4.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget4.setBaseSize(QtCore.QSize(0, 100))
        self.tableWidget4.setLineWidth(5)
        self.tableWidget4.setMidLineWidth(1)
        self.tableWidget4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget4.setRowCount(0)
        self.tableWidget4.setColumnCount(3)
        self.tableWidget4.setObjectName("tableWidget4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget4.setHorizontalHeaderItem(2, item)
        self.tableWidget4.horizontalHeader().setStretchLastSection(False)
        self.tableWidget4.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_15.addWidget(self.tableWidget4)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_17 = QtWidgets.QLabel(parent=self.tab4)
        self.label_17.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_17.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_16.addWidget(self.label_17)
        spacerItem12 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_16.addItem(spacerItem12)
        self.relHumidity4 = QtWidgets.QTextEdit(parent=self.tab4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relHumidity4.sizePolicy().hasHeightForWidth())
        self.relHumidity4.setSizePolicy(sizePolicy)
        self.relHumidity4.setMaximumSize(QtCore.QSize(150, 30))
        self.relHumidity4.setObjectName("relHumidity4")
        self.verticalLayout_16.addWidget(self.relHumidity4)
        spacerItem13 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_16.addItem(spacerItem13)
        self.label_18 = QtWidgets.QLabel(parent=self.tab4)
        self.label_18.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_18.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_16.addWidget(self.label_18)
        spacerItem14 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_16.addItem(spacerItem14)
        self.length4 = QtWidgets.QTextEdit(parent=self.tab4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length4.sizePolicy().hasHeightForWidth())
        self.length4.setSizePolicy(sizePolicy)
        self.length4.setMaximumSize(QtCore.QSize(150, 30))
        self.length4.setObjectName("length4")
        self.verticalLayout_16.addWidget(self.length4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_16.addItem(spacerItem15)
        self.pushButton4 = QtWidgets.QPushButton(parent=self.tab4)
        self.pushButton4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton4.setObjectName("pushButton4")
        self.verticalLayout_16.addWidget(self.pushButton4)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tab4, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sumPlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.sumPlabel.setText("")
        self.sumPlabel.setObjectName("sumPlabel")
        self.gridLayout.addWidget(self.sumPlabel, 0, 1, 1, 1)
        self.sumP = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumP.sizePolicy().hasHeightForWidth())
        self.sumP.setSizePolicy(sizePolicy)
        self.sumP.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sumP.setFont(font)
        self.sumP.setObjectName("sumP")
        self.gridLayout.addWidget(self.sumP, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.graph1 = PlotWidget(parent=self.groupBox)
        self.graph1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graph1.setObjectName("graph1")
        self.verticalLayout_6.addWidget(self.graph1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.line_3 = QtWidgets.QFrame(parent=self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.graph2 = PlotWidget(parent=self.groupBox)
        self.graph2.setObjectName("graph2")
        self.verticalLayout_7.addWidget(self.graph2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.line_4 = QtWidgets.QFrame(parent=self.groupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.graph3 = PlotWidget(parent=self.groupBox)
        self.graph3.setObjectName("graph3")
        self.verticalLayout_8.addWidget(self.graph3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчёт токов утечки"))
        self.i1radio.setText(_translate("MainWindow", " Iут1 - в жилых помещениях дома \n"
"со скрытой электропроводкой"))
        self.i2radio.setText(_translate("MainWindow", " Iут2 - в подсобных помещениях\n"
" с наружной электропроводкой"))
        self.i3radio.setText(_translate("MainWindow", " Iут3 - на приусадебном участке \n"
"с наружной электропроводкой"))
        self.i4radio.setText(_translate("MainWindow", " Iут4 - на вводе в дом с  включенными \n"
" электроприборами по всем линиям"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование электрооборудования"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P, кВт"))
        self.label_4.setText(_translate("MainWindow", "Относительная влажность воздуха, %"))
        self.label_8.setText(_translate("MainWindow", "Протяженность электропроводки, м"))
        self.pushButton1.setText(_translate("MainWindow", "Расчёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Iут1"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование электрооборудования"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P, кВт"))
        self.label_11.setText(_translate("MainWindow", "Относительная влажность воздуха, %"))
        self.label_12.setText(_translate("MainWindow", "Протяженность электропроводки, м"))
        self.pushButton2.setText(_translate("MainWindow", "Расчёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Iут2"))
        item = self.tableWidget3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование электрооборудования"))
        item = self.tableWidget3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P, кВт"))
        self.label_13.setText(_translate("MainWindow", "Относительная влажность воздуха, %"))
        self.label_14.setText(_translate("MainWindow", "Протяженность электропроводки, м"))
        self.pushButton3.setText(_translate("MainWindow", "Расчёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Iут3"))
        item = self.tableWidget4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование электрооборудования"))
        item = self.tableWidget4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P, кВт"))
        self.label_17.setText(_translate("MainWindow", "Относительная влажность воздуха, %"))
        self.label_18.setText(_translate("MainWindow", "Протяженность электропроводки, м"))
        self.pushButton4.setText(_translate("MainWindow", "Расчёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "Iут4"))
        self.sumP.setText(_translate("MainWindow", "∑ P = "))
        self.label_5.setText(_translate("MainWindow", "I(P)"))
        self.label_6.setText(_translate("MainWindow", "I(l)"))
        self.label_7.setText(_translate("MainWindow", "I(f)"))
