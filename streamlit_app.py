import streamlit as st

# ===============================
# DATA JADWAL SEKOLAH
# ===============================

kode_guru = {
    "2": "Pak Wowo",
    "3": "Mas Gibran",
    "4": "Bu Mega",
    "5": "Pak Joko",
    "6": "Bu Puan",
    "7": "Bu Sri",
    "8": "Pak Purbay",
    "9": "Bu Retno",
    "10": "Mas Jaka"
}

jadwal = {
    "A": {
        "senin": [
            "07.00 Matematika (9)",
            "10.00 Sejarah (7)",
            "13.00 IPA (8)"
        ],
        "selasa": [
            "07.00 IPS (6)",
            "10.00 Kimia (10)",
            "13.00 Bahasa Inggris (2)"
        ],
        "rabu": [
            "07.00 Olahraga (5)",
            "10.00 Matematika (9)",
            "13.00 IPA (8)"
        ],
        "kamis": [
            "07.00 IPS (6)",
            "10.00 Kimia (10)",
            "13.00 Bahasa Indonesia (4)"
        ],
        "jumat": [
            "07.00 Bahasa Indonesia (4)",
            "13.00 PKN (3)"
        ]
    },

    "B": {
        "senin": [
            "07.00 Bahasa Indonesia (4)",
            "10.00 Kimia (10)",
            "13.00 PKN (3)"
        ],
        "selasa": [
            "07.00 Sejarah (7)",
            "10.00 Matematika (9)",
            "13.00 IPA (8)"
        ],
        "rabu": [
            "07.00 Olahraga (5)",
            "10.00 Kimia (10)",
            "13.00 IPA (8)"
        ],
        "kamis": [
            "07.00 IPS (6)",
            "10.00 Matematika (9)",
            "13.00 Bahasa Inggris (2)"
        ],
        "jumat": [
            "07.00 IPS (6)",
            "13.00 Bahasa Indonesia (4)"
        ]
    },

    "C": {
        "senin": [
            "07.00 IPS (6)",
            "10.00 Kimia (10)",
            "13.00 Bahasa Inggris (2)"
        ],
        "selasa": [
            "07.00 Matematika (9)",
            "10.00 Sejarah (7)",
            "13.00 IPA (8)"
        ],
        "rabu": [
            "07.00 IPS (6)",
            "10.00 Kimia (10)",
            "13.00 Bahasa Indonesia (4)"
        ],
        "kamis": [
            "07.00 Bahasa Indonesia (4)",
            "10.00 Matematika (9)",
            "13.00 PKN (3)"
        ]
    }
}

# ===============================
# FUNGSI: LIHAT JADWAL
# ===============================

def tampilkan_jadwal():
    st.header("📚 Lihat Jadwal Pelajaran")

    kelas = st.selectbox("Pilih kelas", ["A", "B", "C"])
    hari = st.selectbox("Pilih hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    data = jadwal.get(kelas, {}).get(hari)

    if data:
        st.subheader(f"Jadwal Kelas {kelas} - {hari.capitalize()}")
        for d in data:
            st.write("•", d)
    else:
        st.warning("Tidak ada jadwal.")


# ===============================
# FUNGSI: CARI GURU (TOMBOL)
# ===============================

def cari_guru():
    st.header("🔍 Cari Guru (Klik Nama)")

    cols = st.columns(3)

    for i, (kode, nama) in enumerate(kode_guru.items()):
        with cols[i % 3]:
            if st.button(nama):
                st.subheader(f"Jadwal {nama}")

                ditemukan = False
                for kelas in jadwal:
                    for hari in jadwal[kelas]:
                        for d in jadwal[kelas][hari]:
                            kode_d = d.split("(")[1].replace(")", "")
                            if kode_d == kode:
                                st.write(
                                    f"Kelas {kelas} | {hari.capitalize()} | {d}"
                                )
                                ditemukan = True

                if not ditemukan:
                    st.info("Tidak ada jadwal.")


# ===============================
# MENU UTAMA
# ===============================

st.sidebar.title("📝 Sistem Jadwal Sekolah")

menu = st.sidebar.radio(
    "Pilih Menu",
    ["Lihat Jadwal", "Cari Guru"]
)

if menu == "Lihat Jadwal":
    tampilkan_jadwal()

elif menu == "Cari Guru":
    cari_guru()
