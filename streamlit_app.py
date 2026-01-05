import streamlit as st

st.set_page_config(page_title="Sistem Laboratorium", layout="wide")

# ===============================
# DATABASE JADWAL (SIMULASI)
# ===============================
jadwal = {
    "Lab Organik": {
        "senin": {"07.00": "1A", "10.00": "1B"},
        "selasa": {"07.00": "2A"}
    },
    "Lab Analisis": {
        "senin": {"07.00": "2B"},
        "selasa": {"10.00": "2C"}
    },
    "Lab Instrument": {
        "senin": {"07.00": "2D"},
    },
    "Lab Lingkungan": {
        "selasa": {"10.00": "1C"},
    }
}

# ===============================
# DATA DOSEN / LABORAN
# ===============================
laboran = {
    "organik": [
        {"nama": "Dosen Organik 1", "telp": "08vvvvvvvvvvvvv", "foto": "https://via.placeholder.com/150"},
        {"nama": "Dosen Organik 2", "telp": "08vvvvvvvvvvvvv", "foto": "https://via.placeholder.com/150"},
    ],
    "analisis": [
        {"nama": "Dosen Analisis 1", "telp": "08vvvvvvvvvvvvv", "foto": "https://via.placeholder.com/150"},
    ],
    "instrument": [
        {"nama": "Dosen Instrument 1", "telp": "08vvvvvvvvvvvvv", "foto": "https://via.placeholder.com/150"},
    ],
    "lingkungan": [
        {"nama": "Dosen Lingkungan 1", "telp": "08vvvvvvvvvvvvv", "foto": "https://via.placeholder.com/150"},
    ],
}

# ===============================
# SESSION STATE
# ===============================
if "lab" not in st.session_state:
    st.session_state.lab = None

# ===============================
# HALAMAN JADWAL
# ===============================
def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")

    lab = st.selectbox("Pilih Lab", list(jadwal.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa"])

    data = jadwal[lab].get(hari)

    if data:
        for jam, kelas in data.items():
            st.write(f"🕒 **{jam}** → Kelas **{kelas}**")
    else:
        st.info("Tidak ada jadwal")

# ===============================
# GEDUNG B
# ===============================
def ged_b():
    st.header("Lab.Ged B")
    st.write("Daftar Laboratorium Gedung B")

    if st.button("Lab Organik"):
        st.session_state.lab = "organik"

    if st.button("Lab Analisis"):
        st.session_state.lab = "analisis"

# ===============================
# GEDUNG D
# ===============================
def ged_d():
    st.header("Lab.Ged D")
    st.write("Daftar Laboratorium Gedung D")

    if st.button("Lab Lingkungan"):
        st.session_state.lab = "lingkungan"

# ===============================
# GEDUNG E
# ===============================
def ged_e():
    st.header("Lab.Ged E")
    st.write("Daftar Laboratorium Gedung E")

    if st.button("Lab Instrument"):
        st.session_state.lab = "instrument"

# ===============================
# HALAMAN LAB (REGULASI BEDA)
# ===============================
def halaman_lab(lab):
    if lab == "organik":
        st.header("🔬 Lab Organik")
        st.write("• OOOOOOO")
        st.write("• OOOOOOO")
        st.write("• OOOOOOO")

    elif lab == "analisis":
        st.header("⚗️ Lab Analisis")
        st.write("• AAAAA")
        st.write("• AAAAA")

    elif lab == "instrument":
        st.header("🧪 Lab Instrument")
        st.write("• EEEEE")
        st.write("• EEEEE")

    elif lab == "lingkungan":
        st.header("🌱 Lab Lingkungan")
        st.write("• WWWWWW")
        st.write("• WWWWWW")

    st.subheader("👨‍🔬 Dosen / Laboran")
    for d in laboran[lab]:
        st.image(d["foto"], caption=d["nama"], width=150)
        st.write("📞", d["telp"])

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    if st.button("⬅ Kembali"):
        st.session_state.lab = None

# ===============================
# SIDEBAR MENU
# ===============================
menu = st.sidebar.radio(
    "Menu",
    [
        "Jadwal Lab",
        "Lab.Ged B",
        "Lab.Ged D",
        "Lab.Ged E",
    ]
)

# ===============================
# ROUTING UTAMA
# ===============================
if menu == "Jadwal Lab":
    lihat_jadwal()

elif st.session_state.lab is not None:
    halaman_lab(st.session_state.lab)

elif menu == "Lab.Ged B":
    ged_b()

elif menu == "Lab.Ged D":
    ged_d()

elif menu == "Lab.Ged E":
    ged_e()
