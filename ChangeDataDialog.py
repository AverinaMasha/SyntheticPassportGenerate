import functools
import os

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog

from utils.path_utils import Paths


class ChangeDataDialog(QDialog):
    def __init__(self, passport_data, parameters_generate):
        QDialog.__init__(self)
        uic.loadUi('ChangeDataDialog.ui', self)

        # self.setWindowIcon(QtGui.QIcon('Icons/results.ico'))

        self.label_photo.mousePressEvent = functools.partial(self._load_img, obj=self.label_photo, name='label_photo')
        self.label_signature_1.mousePressEvent = functools.partial(self._load_img, obj=self.label_signature_1,
                                                                   name='label_signature_1')
        self.label_signature_2.mousePressEvent = functools.partial(self._load_img, obj=self.label_signature_2,
                                                                   name='label_signature_2')

        self.imgs_dict = {'label_photo': parameters_generate['images']['label_photo'],
                          'label_signature_1': parameters_generate['images']['label_signature_1'],
                          'label_signature_2': parameters_generate['images']['label_signature_2'],
                          'background': ['', {}]
                          }
        self._fill_fields(passport_data, parameters_generate)

    def _fill_fields(self, passport_data, parameters_generate):
        self.sexComboBox.setCurrentText(passport_data['sex'])

        for file in os.listdir(Paths.fonts()):
            if file != 'fonts.txt':
                self.fontComboBox.addItem(file)
        self.fontComboBox.setCurrentText(parameters_generate['fontComboBox'])
        self.codeSpinBox1_R.setValue(parameters_generate['color_text'][0])
        self.codeSpinBox1_G.setValue(parameters_generate['color_text'][1])
        self.codeSpinBox1_B.setValue(parameters_generate['color_text'][2])

        self.upperCheckBox.setChecked(parameters_generate['upperCheckBox'])

        self.blurCheckBox.setChecked(parameters_generate['blurCheckBox'])
        self.crumpledCheckBox.setChecked(parameters_generate['crumpledCheckBox'])
        self.noiseCheckBox.setChecked(parameters_generate['noiseCheckBox'])

        self.organizationLineEdit1.setText(passport_data['department'])

        self.surnameLineEdit1.setText(passport_data['second_name'])
        self.nameLineEdit.setText(passport_data['first_name'])
        self.patronymicLineEdit.setText(passport_data['patronymic_name'])

        self.birthplaceLineEdit1.setText(passport_data['address'])

        self.serieSpinBox.setValue(passport_data['series_passport'])
        self.numberSpinBox.setValue(passport_data['number_passport'])

        self.issueDateEdit.setDate(passport_data['date_issue'])

        self.codeSpinBox1.setValue(passport_data['department_code'][0])
        self.codeSpinBox2.setValue(passport_data['department_code'][1])

        self.sexComboBox.setCurrentText(passport_data['sex'])

        self.birthDateEdit.setDate(passport_data['date_birth'])

        self.blotsnumSpinBox.setValue(parameters_generate['blotsnumSpinBox'])
        self.flashnumSpinBox.setValue(parameters_generate['flashnumSpinBox'])
        self.blurFlashnumBlotsnum.setValue(parameters_generate['blurFlashnumBlotsnum'])

        # self.fontComboBox.setCurrentText(parameters_generate['fontComboBox'])
        self.fontsizeSpinBox.setValue(parameters_generate['fontsizeSpinBox'])
        self.fontblurSpinBox.setValue(parameters_generate['fontblurSpinBox'])

    def _load_img(self, event, obj, name: str):
        image_path = QFileDialog.getExistingDirectory(self, 'Search image', '')

        if os.path.isfile(image_path):
            self.imgs_dict.update({name: image_path})
            img = QPixmap(image_path) \
                .scaledToWidth(obj.frameGeometry().width()) \
                .scaledToWidth(obj.frameGeometry().height())
            obj.setPixmap(img)
        self.show()
