def hitung_ppm_si5351():
    print("=== KALKULATOR KOREKSI PPM SI5351 ===")
    try:
        # Input frekuensi dalam satuan Hz atau MHz (pastikan satuannya sama)
        target = float(input("Masukkan Frekuensi Target (misal 10000000 untuk 10 MHz): "))
        terukur = float(input("Masukkan Frekuensi Terukur/Aktual di Frequency Counter: "))

        # Rumus PPM
        ppm = ((terukur - target) / target) * 1000000

        # Menghitung penyesuaian untuk XTAL 25 MHz (contoh standar Si5351)
        xtal_standar = 25000000
        xtal_baru = xtal_standar + (xtal_standar * (ppm / 1000000))

        print("\n=== HASIL PERHITUNGAN ===")
        print(f"Selisih Frekuensi : {terukur - target:,.2f} Hz")
        print(f"Nilai Koreksi PPM : {ppm:.2f} PPM")
        print(f"Jika nilai PPM positif, frekuensi Anda terlalu tinggi (overclock).")
        print(f"Jika nilai PPM negatif, frekuensi Anda terlalu rendah (underclock).")
        print(f"\nEstimasi Frekuensi XTAL Baru untuk library: {xtal_baru:,.0f} Hz")

    except ValueError:
        print("Input harus berupa angka!")


# Menjalankan fungsi
hitung_ppm_si5351()
