# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia=21, pendapatan=6500000, insentif_lembur=100000):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur

    def lembur(self):
        self.pendapatan_tambahan += insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class TenagaLepas sebagai child class dari class Karyawan


class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().(nama, usia, pendapatan, 0)

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01

# Definisikan class AnalisData sebagai child class dari class Karyawan


class AnalisData(Karyawan):
    def __init__(self, nama, usia=___, pendapatan=___,
                 insentif_lembur=___):
        super().(___, ___, ___, ___)

# Definisikan class IlmuwanData sebagai child class dari class Karyawan


class IlmuwanData(Karyawan):
    def __init__(self, nama, usia=___, pendapatan=___,
                 insentif_lembur=___):
        ___(___, ___, ___, ___)

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += 0.1 * ___

# Definisikan class PembersihData sebagai child class dari class TenagaLepas


class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan=___):
        ___(___, ___, ___)

# Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas


class ___(___):
    def __init__(self, nama, usia, pendapatan=___):
        ___(___, ___, ___)

        def tambahan_proyek(self, jumlah_tambahan):
            return

# Definisikan class Perusahaan


class ___:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = ___
        self.alamat = ___
        self.nomor_telepon = ___
        self.list_karyawan = []

    def aktifkan_karyawan(self, karyawan):
        ___(karyawan)

    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in ___:
            if karyawan.nama == ___:
                karyawan_nonaktif = ___
                break
        if karyawan_nonaktif is not None:
            ___(karyawan_nonaktif)

    def total_pengeluaran(self):
        pengeluaran = 0
        for karyawan in ___:
            pengeluaran += ___
        return pengeluaran

    def cari_karyawan(self, nama_karyawan):
        for karyawan in ___:
            if karyawan.nama == ___:
                return karyawan
        return None


# Create object karyawan sesuai dengan tugasnya masing-masing
# seperti yang dinyatakan dalam tabel.
ani = ___
budi = ___
cici = ___
didi = ___
efi = ___
febi = ___

# Create object perusahaan
perusahaan = ___

# Aktifkan setiap karyawan yang telah didefinisikan
___
___
___
___
___
___

# Cetak keseluruhan total pengeluaran perusahaan
print(___)
