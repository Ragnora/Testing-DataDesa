from io import StringIO
import unittest
from unittest.mock import patch, mock_open
from DataDesa import *

class TestDataDesa(unittest.TestCase):

    # ===== Login =====

    # Valid Login
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin'])
    @patch('DataDesa.halamanUtama')
    @patch('builtins.print')
    def test_login_valid(self, mock_print, mock_halamanUtama, mock_input, mock_open_file):
        login()
        mock_halamanUtama.assert_called_once()

    # Invalid Login
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'root'])
    @patch('builtins.print')
    def test_login_invalid(self, mock_print, mock_input, mock_open_file):
        login()
        mock_print.assert_called_with('\t\t      Username atau Password Salah!')


    # ===== Tambah Data =====

    @patch('builtins.input', side_effect=['1234567891234567', 'Salsa', 'Perempuan', '17', 'Banyuwangi', '080'])
    @patch('builtins.print')
    def test_tambahData(self, mock_print, mock_input):
        tambahData()
        mock_print.assert_called_with('\n\t\t\t      Data telah ditambahkan')

    # Invalid Data Input (Input Kosong)
    @patch('builtins.input', side_effect=['', 'Salsa', 'Perempuan', '17', 'Banyuwangi', '080'])
    @patch('builtins.print')
    def test_tambahData_empty(self, mock_print, mock_input):
        tambahData()
        mock_print.assert_called_with('\n\t\t\t      Masukkan Data dengan Benar!')

    # ===== Update Data =====

    # Tambah - Update Data
    @patch('builtins.input', side_effect=['1234567891', 'Salsa', 'Perempuan', '17', 'Banyuwangi', '080', '0', '1234567890', 'Wahyu', 'Laki-Laki', '22', 'Lumajang', '081', 'Wahyu'])
    @patch('builtins.print')
    def test_integration_tambah_update(self, mock_print, mock_input):
        tambahData()
        mock_print.assert_called_with('\n\t\t\t      Data telah ditambahkan')
        mock_print.reset_mock()

        updateData()
        mock_print.assert_called_with('\n\t\t\t      Data telah diupdate')
        mock_print.reset_mock()

        # Menampilkan Data menggunakan Filter Nama
        expected_output = [
            "\nNIK : 1234567890",
            "Nama : Wahyu",
            "Jenis Kelamin : Laki-Laki",
            "Umur : 22",
            "Alamat : Lumajang",
            "No HP : 081"
        ]
        with patch('builtins.print') as mock_print:
            dataFilterNama()
            self.assertEqual(mock_print.call_count, len(expected_output))
            for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                self.assertEqual(call_args[0][0], expected_output_line)
        

    # Update Data
    @patch('builtins.input', side_effect=['0', '1234567890', 'Wahyu', 'Laki-Laki', '25', 'Lumajang', '123456789'])
    @patch('builtins.print')
    def test_updateData(self, mock_print, mock_input):
        data = [{'NIK': 111111, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '9876543210'}]
        with patch('DataDesa.data', data):
            updateData()
            mock_print.assert_called_with('\n\t\t\t      Data telah diupdate')
    
    # Invalid Index
    @patch('builtins.input', side_effect=['-1'])
    @patch('builtins.print')
    def test_updateData_invalid_index(self, mock_print, mock_input):
        data = [{'NIK': 111111, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '9876543210'}]
        with patch('DataDesa.data', data):
            updateData()
            mock_print.assert_called_with('\t\t\t    Masukkan index data dengan benar')

    # Invalid Data Input (Input Kosong)
    @patch('builtins.input', side_effect=['0', '', 'Wahyu', 'Laki-Laki', '25', 'Lumajang', '123456789'])
    @patch('builtins.print')
    def test_updateData_empty(self, mock_print, mock_input):
        data = [{'NIK': 111111, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '9876543210'}]
        with patch('DataDesa.data', data):
            updateData()
            mock_print.assert_called_with('\n\t\t\t      Masukkan Data dengan Benar!')


    # ===== Hapus data =====

    # Tambah - Hapus Data
    @patch('builtins.input', side_effect=['1234567891234567', 'Salsa', 'Perempuan', '17', 'Banyuwangi', '080', '9', 'Salsa'])
    @patch('builtins.print')
    def test_integration_tambah_hapus(self, mock_print, mock_input):
        tambahData()
        mock_print.assert_called_with('\n\t\t\t      Data telah ditambahkan')
        mock_print.reset_mock()

        hapusData()
        mock_print.assert_called_with('\n\t\t\t      Data berhasil dihapus')
        mock_print.reset_mock()

        # Menampilkan Data menggunakan Filter Nama
        dataFilterNama()
        mock_print.assert_called_with("Data tidak ditemukan")
    
    # Hapus Data
    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_hapusData(self, mock_print, mock_input):
        data = [
            {'NIK': 111111, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '9876543210'},
            {'NIK': 222222, 'Nama': 'Wahyu', 'Jenis Kelamin': 'Laki-Laki', 'Umur': 23, 'Alamat': 'Banyuwangi', 'No HP': '1234567890'}
        ]
        with patch('DataDesa.data', data):
            hapusData()
            mock_print.assert_called_with('\n\t\t\t      Data berhasil dihapus')

    # Invalid Index
    @patch('builtins.input', side_effect=['-1'])
    @patch('builtins.print')
    def test_hapusData_invalid_index(self, mock_print, mock_input):
        data = [{'NIK': 111111, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '9876543210'}]
        with patch('DataDesa.data', data):
            hapusData()
            mock_print.assert_called_with('\n\t\t\t    Masukkan index data dengan benar')
    

# ==================== FILTER ====================

    # Filter - NIK

    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin', "123"])
    @patch('DataDesa.halamanUtama')
    def test_LoginthenSearchByNIK(self, mock_halamanUtama, mock_input, mock_open_file):
        # Login
        login()
        mock_halamanUtama.assert_called_once()

        # Filter by NIK
        with patch('DataDesa.data', [{'NIK': 123, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '080'}]):
            expected_output = [
                "\nNIK : 123",
                "Nama : Salsa",
                "Jenis Kelamin : Perempuan",
                "Umur : 17",
                "Alamat : Banyuwangi",
                "No HP : 080"
            ]
            with patch('builtins.print') as mock_print:
                dataFilterNIK()
                self.assertEqual(mock_print.call_count, len(expected_output))
                for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                    self.assertEqual(call_args[0][0], expected_output_line)


    # Filter - Nama

    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin', "Salsa"])
    @patch('DataDesa.halamanUtama')
    def test_LoginthenSearchByNama(self, mock_halamanUtama, mock_input, mock_open_file):
        # Login
        login()
        mock_halamanUtama.assert_called_once()

        # Filter by Nama
        with patch('DataDesa.data', [{'NIK': 123, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '080'}]):
            expected_output = [
                "\nNIK : 123",
                "Nama : Salsa",
                "Jenis Kelamin : Perempuan",
                "Umur : 17",
                "Alamat : Banyuwangi",
                "No HP : 080"
            ]
            with patch('builtins.print') as mock_print:
                dataFilterNama()
                self.assertEqual(mock_print.call_count, len(expected_output))
                for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                    self.assertEqual(call_args[0][0], expected_output_line)
    
    
    # Filter - Umur

    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin', "17"])
    @patch('DataDesa.halamanUtama')
    def test_LoginthenSearchByUmur(self, mock_halamanUtama, mock_input, mock_open_file):
        # Login
        login()
        mock_halamanUtama.assert_called_once()

        # Filter by Umur
        with patch('DataDesa.data', [{'NIK': 123, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '080'}]):
            expected_output = [
                "\nNIK : 123",
                "Nama : Salsa",
                "Jenis Kelamin : Perempuan",
                "Umur : 17",
                "Alamat : Banyuwangi",
                "No HP : 080"
            ]
            with patch('builtins.print') as mock_print:
                dataFilterUmur()
                self.assertEqual(mock_print.call_count, len(expected_output))
                for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                    self.assertEqual(call_args[0][0], expected_output_line)
   
   
    # Filter - Alamat

    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin', "Banyuwangi"])
    @patch('DataDesa.halamanUtama')
    def test_LoginthenSearchByAlamat(self, mock_halamanUtama, mock_input, mock_open_file):
        # Login
        login()
        mock_halamanUtama.assert_called_once()

        # Filter by Alamat
        with patch('DataDesa.data', [{'NIK': 123, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '080'}]):
            expected_output = [
                "\nNIK : 123",
                "Nama : Salsa",
                "Jenis Kelamin : Perempuan",
                "Umur : 17",
                "Alamat : Banyuwangi",
                "No HP : 080"
            ]
            with patch('builtins.print') as mock_print:
                dataFilterAlamat()
                self.assertEqual(mock_print.call_count, len(expected_output))
                for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                    self.assertEqual(call_args[0][0], expected_output_line)
    
    
    # Filter - No HP

    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin', "080"])
    @patch('DataDesa.halamanUtama')
    def test_LoginthenSearchByNoHP(self, mock_halamanUtama, mock_input, mock_open_file):
        # Login
        login()
        mock_halamanUtama.assert_called_once()

        # Filter by NoHP
        with patch('DataDesa.data', [{'NIK': 123, 'Nama': 'Salsa', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Banyuwangi', 'No HP': '080'}]):
            expected_output = [
                "\nNIK : 123",
                "Nama : Salsa",
                "Jenis Kelamin : Perempuan",
                "Umur : 17",
                "Alamat : Banyuwangi",
                "No HP : 080"
            ]
            with patch('builtins.print') as mock_print:
                dataFilterNoHP()
                self.assertEqual(mock_print.call_count, len(expected_output))
                for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                    self.assertEqual(call_args[0][0], expected_output_line)


# ==================== SORTING ====================

    # Test Login - Without Short
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin'])
    @patch('DataDesa.halamanUtama')
    def testLoginThenShow(self, mock_halamanUtama, mock_input, mock_open_file):
        login()
        mock_halamanUtama.assert_called_once()

        data = [
            {'NIK': 3525015201880002, 'Nama': 'Ragnora', 'Jenis Kelamin': 'Perempuan', 'Umur': 20,'Alamat': 'Banyuwangi','No HP': '081'},
            {'NIK': 3123456789123456, 'Nama': 'Blurryface', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '082'},
            {'NIK': 3525016005650004, 'Nama': 'Nycto', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Situbondo','No HP': '083'}
        ]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dataWithOutSort(data)

            printed_output = mock_stdout.getvalue()

            self.assertIn('='*73, printed_output)
            self.assertIn('DATA PENDUDUK DESA', printed_output)
            self.assertIn('-'*73, printed_output)
            no = 0
            for person in data:
                self.assertIn(f"No : {no}", printed_output)
                self.assertIn(f"NIK : {person['NIK']}", printed_output)
                self.assertIn(f"Nama : {person['Nama']}", printed_output)
                self.assertIn(f"Jenis Kelamin : {person['Jenis Kelamin']}", printed_output)
                self.assertIn(f"Umur : {person['Umur']}", printed_output)
                self.assertIn(f"Alamat : {person['Alamat']}", printed_output)
                self.assertIn(f"No HP : {person['No HP']}", printed_output)
                no += 1
    
    
    # Test Login - Short By Name
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin'])
    @patch('DataDesa.halamanUtama')
    def testLoginThenSortByName(self, mock_halamanUtama, mock_input, mock_open_file):
        login()
        mock_halamanUtama.assert_called_once()

        data = [
            {'NIK': 3525015201880002, 'Nama': 'Ragnora', 'Jenis Kelamin': 'Perempuan', 'Umur': 20,'Alamat': 'Banyuwangi','No HP': '081'},
            {'NIK': 3123456789123456, 'Nama': 'Blurryface', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '082'},
            {'NIK': 3525016005650004, 'Nama': 'Nycto', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Situbondo','No HP': '083'}
        ]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dataSortNama(data)

            printed_output = mock_stdout.getvalue()

            self.assertIn('='*73, printed_output)
            self.assertIn('DATA PENDUDUK DESA', printed_output)
            self.assertIn('Menurut Nama', printed_output)
            self.assertIn('-'*73, printed_output)
            no = 0
            for person in data:
                self.assertIn(f"No : {no}", printed_output)
                self.assertIn(f"NIK : {person['NIK']}", printed_output)
                self.assertIn(f"Nama : {person['Nama']}", printed_output)
                self.assertIn(f"Jenis Kelamin : {person['Jenis Kelamin']}", printed_output)
                self.assertIn(f"Umur : {person['Umur']}", printed_output)
                self.assertIn(f"Alamat : {person['Alamat']}", printed_output)
                self.assertIn(f"No HP : {person['No HP']}", printed_output)
                no += 1
    
    # Test Login - Short By Umur
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin'])
    @patch('DataDesa.halamanUtama')
    def testLoginThenSortByUmur(self, mock_halamanUtama, mock_input, mock_open_file):
        login()
        mock_halamanUtama.assert_called_once()

        data = [
            {'NIK': 3525015201880002, 'Nama': 'Ragnora', 'Jenis Kelamin': 'Perempuan', 'Umur': 20,'Alamat': 'Banyuwangi','No HP': '081'},
            {'NIK': 3123456789123456, 'Nama': 'Blurryface', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '082'},
            {'NIK': 3525016005650004, 'Nama': 'Nycto', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Situbondo','No HP': '083'}
        ]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dataSortUmur(data)

            printed_output = mock_stdout.getvalue()

            self.assertIn('='*73, printed_output)
            self.assertIn('DATA PENDUDUK DESA', printed_output)
            self.assertIn('Menurut Umur', printed_output)
            self.assertIn('-'*73, printed_output)
            no = 0
            for person in data:
                self.assertIn(f"No : {no}", printed_output)
                self.assertIn(f"NIK : {person['NIK']}", printed_output)
                self.assertIn(f"Nama : {person['Nama']}", printed_output)
                self.assertIn(f"Jenis Kelamin : {person['Jenis Kelamin']}", printed_output)
                self.assertIn(f"Umur : {person['Umur']}", printed_output)
                self.assertIn(f"Alamat : {person['Alamat']}", printed_output)
                self.assertIn(f"No HP : {person['No HP']}", printed_output)
                no += 1
    
    
    # Test Login - Short By Alamat
    @patch('builtins.open', new_callable=mock_open, read_data='admin,admin\nroot,root\n')
    @patch('builtins.input', side_effect=['admin', 'admin'])
    @patch('DataDesa.halamanUtama')
    def testLoginThenSortByAlamat(self, mock_halamanUtama, mock_input, mock_open_file):
        login()
        mock_halamanUtama.assert_called_once()

        data = [
            {'NIK': 3525015201880002, 'Nama': 'Ragnora', 'Jenis Kelamin': 'Perempuan', 'Umur': 20,'Alamat': 'Banyuwangi','No HP': '081'},
            {'NIK': 3123456789123456, 'Nama': 'Blurryface', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '082'},
            {'NIK': 3525016005650004, 'Nama': 'Nycto', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Situbondo','No HP': '083'}
        ]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dataSortAlamat(data)

            printed_output = mock_stdout.getvalue()

            self.assertIn('='*73, printed_output)
            self.assertIn('DATA PENDUDUK DESA', printed_output)
            self.assertIn('Menurut Alamat', printed_output)
            self.assertIn('-'*73, printed_output)
            no = 0
            for person in data:
                self.assertIn(f"No : {no}", printed_output)
                self.assertIn(f"NIK : {person['NIK']}", printed_output)
                self.assertIn(f"Nama : {person['Nama']}", printed_output)
                self.assertIn(f"Jenis Kelamin : {person['Jenis Kelamin']}", printed_output)
                self.assertIn(f"Umur : {person['Umur']}", printed_output)
                self.assertIn(f"Alamat : {person['Alamat']}", printed_output)
                self.assertIn(f"No HP : {person['No HP']}", printed_output)
                no += 1

if __name__ == '__main__':
    unittest.main()