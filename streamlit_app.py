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

# ===============================
# DATA JADWAL LAB (TIDAK DIUBAH)
# ===============================
jadwal = {
    "Lab.organik": {
        "senin": [
            "07.00 Kimia (2)",
            "10.00 Analisis (4)"
        ]
    },
    "Lab.instrument": {
        "selasa": [
            "08.00 Spektroskopi (3)",
            "13.00 Kromatografi (5)"
        ]
    }
}

# ===============================
# FITUR LAB (ASLI)
# ===============================
def lihat_jadwal():
    st.header("Lihat Jadwal Lab")

    kelas = st.selectbox("Pilih Lab", list(jadwal.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    data = jadwal.get(kelas, {}).get(hari)

    if data:
        for d in data:
            st.write(d)
    else:
        st.info("Tidak ada jadwal")

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
