import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单GUI应用程序")
        self.setGeometry(100, 100, 900, 300)  # 将窗口宽度增加3倍

        # 创建一个长条形的文本框
        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedHeight(30)  # 设置文本框的高度

        # 创建一个PR缓存按钮
        self.pr_cache_button = QPushButton("PR缓存", self)
        self.pr_cache_button.clicked.connect(self.display_pr_cache_path)

        # 创建一个CSP缓存按钮
        self.csp_cache_button = QPushButton("CSP缓存", self)
        self.csp_cache_button.clicked.connect(self.display_csp_cache_path)

        # 创建一个CSP工作区按钮
        self.csp_workspace_button = QPushButton("CSP工作区", self)
        self.csp_workspace_button.clicked.connect(self.display_csp_workspace_path)

        # 创建一个PS工作区按钮
        self.ps_workspace_button = QPushButton("PS工作区", self)
        self.ps_workspace_button.clicked.connect(self.display_ps_workspace_path)

        # 创建一个SAI工作区按钮
        self.sai_workspace_button = QPushButton("SAI工作区", self)
        self.sai_workspace_button.clicked.connect(self.display_sai_workspace_path)

        # 创建一个ES传文件按钮
        self.es_transfer_button = QPushButton("ES传文件", self)
        self.es_transfer_button.clicked.connect(self.display_es_transfer_path)

        # 创建一个打开按钮
        self.open_button = QPushButton("打开", self)
        self.open_button.clicked.connect(self.open_folder)

        # 设置第一排按钮布局为水平对齐
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.pr_cache_button)
        button_layout1.addWidget(self.csp_cache_button)
        button_layout1.addWidget(self.csp_workspace_button)
        button_layout1.addWidget(self.ps_workspace_button)
        button_layout1.addWidget(self.sai_workspace_button)
        button_layout1.addWidget(self.es_transfer_button)

        # 设置第二排按钮布局为水平对齐
        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(self.open_button)

        # 设置主布局
        main_layout = QVBoxLayout()
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



