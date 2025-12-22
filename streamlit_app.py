import streamlit as st

# ===============================
# DATA GURU
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

# ===============================
# DATA JADWAL
# ===============================
jadwal = {
    "Lab.organik": {
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

    "Lab.lingkungan": {
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
     "Lab.instrument": {
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


    "Lab.analisis": {
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
# FITUR LIHAT JADWAL
# ===============================
def lihat_jadwal():
    st.header("Lihat Jadwal Pelajaran")

    kelas = st.selectbox("Pilih kelas", ["Lab.organik", "Lab.lingkungan","Lab.instrument", "Lab.analisis"])
    hari = st.selectbox("Pilih hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    data = jadwal.get(kelas, {}).get(hari)

    if data:
        st.subheader(f"Kelas {kelas} - {hari.capitalize()}")
        for item in data:
            st.write(item)
    else:
        st.warning("Tidak ada jadwal")

# ===============================
# FITUR CARI GURU (PAKAI TOMBOL)
# ===============================
def cari_guru():
    st.header("Cari Jadwal Guru")

    for kode, nama in kode_guru.items():
        if st.button(nama):
            st.subheader(f"Jadwal {nama}")
            ditemukan = False

            for kelas in jadwal:
                for hari in jadwal[kelas]:
                    for item in jadwal[kelas][hari]:
                        if f"({kode})" in item:
                            st.write(f"Kelas {kelas} | {hari.capitalize()} | {item}")
                            ditemukan = True

            if not ditemukan:
                st.info("Tidak ada jadwal untuk guru ini")

# ===============================
# MENU UTAMA
# ===============================
st.sidebar.title("Sistem Jadwal Sekolah")

menu = st.sidebar.radio(
    "Pilih Menu",
    ["Lihat Jadwal", "Cari Guru"]
)

if menu == "Lihat Jadwal":
    lihat_jadwal()
else:
    cari_guru()
