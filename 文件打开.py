import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单GUI应用程序")
        self.setGeometry(100, 100, 900, 300)  # 将窗口宽度增加3倍

        # 设置全局字体大小
        font = QFont()
        font.setPointSize(24)
        self.setFont(font)

        # 创建一个长条形的文本框
        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedHeight(60)  # 设置文本框的高度
        self.text_edit.setStyleSheet("""
            background-color: #f0f0f0;
            border: 1px solid #c0c0c0;
            padding: 5px;
            border-radius: 5px;
        """)

        # 创建按钮
        buttons = [
            ("PR缓存", self.display_pr_cache_path),
            ("CSP缓存", self.display_csp_cache_path),
            ("CSP工作区", self.display_csp_workspace_path),
            ("PS工作区", self.display_ps_workspace_path),
            ("SAI工作区", self.display_sai_workspace_path),
            ("ES传文件", self.display_es_transfer_path),
            ("打开", self.open_folder)
        ]

        button_widgets = []
        for text, action in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(action)
            button.setFixedSize(150, 60)  # 设置按钮固定大小
            button.setStyleSheet("""
                background-color: #e0e0e0;
                border: 1px solid #a0a0a0;
                padding: 5px;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            """)
            button_widgets.append(button)

        # 设置第一排按钮布局为水平对齐
        button_layout1 = QHBoxLayout()
        for button in button_widgets[:6]:
            button_layout1.addWidget(button)

        # 设置第二排按钮布局为水平对齐
        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(button_widgets[6])

        # 设置主布局
        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)  # 设置组件的上下间隙为2像素
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout1)
        main_layout.addLayout(button_layout2)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def display_pr_cache_path(self):
        # 获取当前用户的AppData路径
        pr_cache_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming\Adobe\Common")
        self.text_edit.setText(pr_cache_path)

    def display_csp_cache_path(self):
        # 获取当前用户的AppData路径
        csp_cache_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming\CELSYSUserData\CELSYS\CLIPStudioPaintData")
        self.text_edit.setText(csp_cache_path)

    def display_csp_workspace_path(self):
        # 获取当前用户的AppData路径
        csp_workspace_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming\CELSYSUserData")
        self.text_edit.setText(csp_workspace_path)

    def display_ps_workspace_path(self):
        # 获取当前用户的AppData路径
        ps_workspace_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Roaming\Adobe")
        self.text_edit.setText(ps_workspace_path)

    def display_sai_workspace_path(self):
        # 获取当前用户的文档路径
        sai_workspace_path = os.path.expandvars(r"C:\Users\%USERNAME%\Documents\SYSTEMAX Software Development")
        self.text_edit.setText(sai_workspace_path)

    def display_es_transfer_path(self):
        # 显示ES传文件路径
        es_transfer_path = "ftp://192.168.10.1:3721/"
        self.text_edit.setText(es_transfer_path)

    def open_folder(self):
        folder_path = self.text_edit.toPlainText().strip()
        if folder_path.startswith("ftp://"):
            self.open_ftp_url(folder_path)
        elif os.path.exists(folder_path):
            os.startfile(folder_path)  # 适用于Windows系统
        else:
            self.text_edit.setText(f"路径不存在: {folder_path}")

    def open_ftp_url(self, url):
        # 使用explorer.exe打开FTP URL
        os.system(f'explorer "{url}"')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



