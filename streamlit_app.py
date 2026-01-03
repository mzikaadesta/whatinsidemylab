import streamlit as st

# ===============================
# DATA DOSEN
# ===============================
dosen = {
    "2": {"nama": "Pak Wowo", "telp": "08vvvvvvvvvvvvv"},
    "3": {"nama": "Mas Gibran", "telp": "08vvvvvvvvvvvvv"},
    "4": {"nama": "Bu Mega", "telp": "08vvvvvvvvvvvvv"},
    "5": {"nama": "Pak Joko", "telp": "08vvvvvvvvvvvvv"},
    "6": {"nama": "Bu Puan", "telp": "08vvvvvvvvvvvvv"},
    "7": {"nama": "Bu Sri", "telp": "08vvvvvvvvvvvvv"},
    "8": {"nama": "Pak Purbay", "telp": "08vvvvvvvvvvvvv"},
    "9": {"nama": "Bu Retno", "telp": "08vvvvvvvvvvvvv"},
    "10": {"nama": "Mas Jaka", "telp": "08vvvvvvvvvvvvv"},
}

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
if "hal_lab" not in st.session_state:
    st.session_state.hal_lab = "menu"
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

if "hal_dosen" not in st.session_state:
    st.session_state.hal_dosen = "menu"
if "kode_dosen" not in st.session_state:
    st.session_state.kode_dosen = None

# ===============================
# FITUR JADWAL LAB
# ===============================
def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")

    lab = st.selectbox("Pilih Lab", list(jadwal.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    data = jadwal.get(lab, {}).get(hari)

    if data:
        for d in data:
            st.write(d)
    else:
        st.info("Tidak ada jadwal")

# ===============================
# LAB MENU & DETAIL
# ===============================
def menu_lab():
    st.header("🏫 Daftar Laboratorium")
    for lab in jadwal.keys():
        if st.button(lab):
            st.session_state.lab_terpilih = lab
            st.session_state.hal_lab = "detail"

def detail_lab():
    lab = st.session_state.lab_terpilih
    st.header(f"🔬 {lab}")

    st.subheader("📋 Cara Meminjam Lab")
    st.write("""
    1. Mengisi formulir peminjaman 

    st.link_button("Go to gallery", "https://streamlit.io/gallery")
    2. Persetujuan dosen / PJ Lab
    3. Menggunakan lab sesuai jadwal
    """)

    st.subheader("⚠️ Aturan")
    st.write("""
    - Wajib APD
    - Jaga kebersihan
    - Bertanggung jawab atas alat
    """)

    st.subheader("📞 Kontak PJ")
    st.write("08vvvvvvvvvvvvv")

    if st.button("⬅ Kembali"):
        st.session_state.hal_lab = "menu"

# ===============================
# DOSEN MENU & DETAIL
# ===============================
def menu_dosen():
    st.header("👨‍🏫 Daftar Dosen")
    for kode, data in dosen.items():
        if st.button(data["nama"]):
            st.session_state.kode_dosen = kode
            st.session_state.hal_dosen = "detail"

def detail_dosen():
    kode = st.session_state.kode_dosen
    data = dosen[kode]

    st.header(data["nama"])
    st.write("📞", data["telp"])

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
        st.session_state.hal_dosen = "menu"

# ===============================
# SIDEBAR
# ===============================
menu = st.sidebar.radio(
    "Menu",
    ["Lihat Jadwal Lab", "Informasi Lab", "Informasi Dosen"]
)

# ===============================
# ROUTING
# ===============================
if menu == "Lihat Jadwal Lab":
    lihat_jadwal()

elif menu == "Informasi Lab":
    if st.session_state.hal_lab == "menu":
        menu_lab()
    else:
        detail_lab()

elif menu == "Informasi Dosen":
    if st.session_state.hal_dosen == "menu":
        menu_dosen()
    else:
        detail_dosen()
