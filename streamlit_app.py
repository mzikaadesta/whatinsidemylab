import streamlit as st

# ===============================
# DATA DOSEN
# ===============================
dosen = {
    "2": {"nama": "Pak Wowo", "telp": "08vvvvvvvvvvvvv"},
    "3": {"nama": "Mas Gibran", "telp": "08vvvvvvvvvvvvv"},
    "4": {"nama": "Bu Mega", "telp": "08vvvvvvvvvvvvv"},
    "5": {"nama": "Pak Joko", "telp": "08vvvvvvvvvvvvv"},
}

import streamlit as st

# ===============================
# DATA JADWAL LAB
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
# SESSION STATE
# ===============================
if "halaman_lab" not in st.session_state:
    st.session_state.halaman_lab = "menu"

if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

# ===============================
# FITUR LIHAT JADWAL LAB
# ===============================
def lihat_jadwal():
    st.header("📅 Lihat Jadwal Laboratorium")

    lab = st.selectbox("Pilih Laboratorium", list(jadwal.keys()))
    hari = st.selectbox(
        "Pilih Hari",
        ["senin", "selasa", "rabu", "kamis", "jumat"]
    )

    data = jadwal.get(lab, {}).get(hari)

    if data:
        st.subheader(f"{lab} - {hari.capitalize()}")
        for d in data:
            st.write(d)
    else:
        st.info("Tidak ada jadwal pada hari tersebut.")

# ===============================
# MENU LAB (TOMBOL)
# ===============================
def menu_lab():
    st.header("🏫 Daftar Laboratorium")

    for lab in jadwal.keys():
        if st.button(lab):
            st.session_state.lab_terpilih = lab
            st.session_state.halaman_lab = "detail"

# ===============================
# DETAIL LAB
# ===============================
def detail_lab():
    lab = st.session_state.lab_terpilih

    st.header(f"🔬 Informasi {lab}")

    st.subheader("📋 Cara Meminjam Laboratorium")
    st.write("""
    1. Mengajukan permohonan peminjaman
    2. Mengisi formulir peminjaman
    3. Mendapat persetujuan penanggung jawab lab
    4. Menggunakan lab sesuai jadwal yang ditentukan
    """)

    st.subheader("⚠️ Aturan Penggunaan")
    st.write("""
    - Wajib menggunakan APD
    - Menjaga kebersihan laboratorium
    - Tidak membawa makanan dan minuman
    - Bertanggung jawab atas alat yang digunakan
    """)

    st.subheader("📞 Kontak Penanggung Jawab")
    st.write("Nama : Dosen Penanggung Jawab")
    st.write("No. Telp : 08vvvvvvvvvvvvv")

    if st.button("⬅ Kembali ke Daftar Lab"):
        st.session_state.halaman_lab = "menu"

# ===============================
# SIDEBAR MENU UTAMA
# ===============================
st.sidebar.title("Sistem Laboratorium")

menu = st.sidebar.radio(
    "Menu",
    ["Lihat Jadwal Lab", "Informasi Lab"]
)

# ===============================
# ROUTING
# ===============================
if menu == "Lihat Jadwal Lab":
    lihat_jadwal()

elif menu == "Informasi Lab":
    if st.session_state.halaman_lab == "menu":
        menu_lab()
    else:
        detail_lab()


# ===============================
# STATE HALAMAN DOSEN
# ===============================
if "hal_dosen" not in st.session_state:
    st.session_state.hal_dosen = "list"
if "kode_dosen" not in st.session_state:
    st.session_state.kode_dosen = None

# ===============================
# LIST DOSEN
# ===============================
def list_dosen():
    st.header("📘 Info Dosen")

    for kode, data in dosen.items():
        if st.button(data["nama"]):
            st.session_state.kode_dosen = kode
            st.session_state.hal_dosen = "detail"

# ===============================
# DETAIL DOSEN
# ===============================
def detail_dosen():
    kode = st.session_state.kode_dosen
    data = dosen[kode]

    st.header("👤 Detail Dosen")
    st.write("**Nama:**", data["nama"])
    st.write("**No. Telp:**", data["telp"])

    st.subheader("📅 Jadwal Mengajar")
    ada = False
    for lab in jadwal:
        for hari in jadwal[lab]:
            for item in jadwal[lab][hari]:
                if f"({kode})" in item:
                    st.write(f"{lab} | {hari.capitalize()} | {item}")
                    ada = True

    if not ada:
        st.info("Belum ada jadwal")

    if st.button("⬅ Kembali"):
        st.session_state.hal_dosen = "list"
        st.session_state.kode_dosen = None

# ===============================
# MENU SIDEBAR
# ===============================
menu = st.sidebar.radio(
    "Menu",
    ["Lihat Jadwal Lab", "Info Dosen"]
)

if menu == "Lihat Jadwal Lab":
    lihat_jadwal()

elif menu == "Info Dosen":
    if st.session_state.hal_dosen == "list":
        list_dosen()
    else:
        detail_dosen()
