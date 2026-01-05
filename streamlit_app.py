import streamlit as st

st.set_page_config(page_title="Sistem Informasi Laboratorium", layout="wide", page_icon="🔬")

# ===============================
# DATABASE LAB
# ===============================
DATABASE_LAB = {
    "Lab Organik": {
        "gedung": "Gedung B",
        "key": "organik",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "regulasi": [
            "1. wwww dresscode lab lengkap",
            "2. wwww dilarang makan/minum",
            "3. wwww cek alat sebelum pakai",
            "4. wwww bersihkan meja setelah praktikum",
            "5. wwww lapor jika ada kerusakan"
        ],
        "dosen": [
            {"nama": "ayung, M.Si", "telp": "08wkwkwkwkwk"},
            {"nama": "Siti Indomi, M.Si", "telp": "08wkwkwkwkwk"},
            {"nama": "Ultra Mikk. Amd, Si", "telp": "08wkwkwkwkwk"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Analisis": {
        "gedung": "Gedung B",
        "key": "analisis",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "regulasi": ["1. bbb", "2. bbb"],
        "dosen": [{"nama": "Pak Joko", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Lingkungan": {
        "gedung": "Gedung B",
        "key": "lingkungan",
        "jadwal": { "senin": {"07.00": "1A"} },
        "regulasi": ["1. ppp", "2. ppp"],
        "dosen": [{"nama": "Pak Purbay", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Instrumen": {
        "gedung": "Gedung E",
        "key": "instrumen",
        "jadwal": { "senin": {"07.00": "1A"} },
        "regulasi": ["1. 000", "2. 000"],
        "dosen": [{"nama": "Pak DD", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Mikro": {
        "gedung": "Gedung E",
        "key": "mikro",
        "jadwal": { "senin": {"07.00": "1A"} },
        "regulasi": ["Aturan Mikro..."],
        "dosen": [{"nama": "Dosen Mikro", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Fisika": {
        "gedung": "Gedung F",
        "key": "fisika",
        "jadwal": { "senin": {"07.00": "1A"} },
        "regulasi": ["1. mmmm", "2. mmmm"],
        "dosen": [{"nama": "Pak Purbay", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    },
    "Lab Teknologi": {
        "gedung": "Gedung G",
        "key": "teknologi",
        "jadwal": { "senin": {"07.00": "1A"} },
        "regulasi": ["1. msms", "2. msms"],
        "dosen": [{"nama": "agoy, M.Si", "telp": "08..."}],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    }
}

# ===============================
# FUNGSI NAVIGASI & TAMPILAN
# ===============================
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

def halaman_detail_lab(nama_lab):
    data = DATABASE_LAB[nama_lab]
    st.button("⬅ Kembali ke Daftar Gedung", on_click=reset_lab)
    st.title(f"🔬 {nama_lab}")
    st.divider()

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📜 Regulasi Peminjaman")
        for r in data["regulasi"]:
            st.write(r)
        st.divider()
        st.link_button("📑 Formulir Peminjaman", data["link_form"], type="primary", use_container_width=True)

    with col2:
        st.subheader("👨‍🔬 Dosen & Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    
    # --- LOGIKA FOTO OTOMATIS BERDASARKAN GEDUNG ---
    if nama_gedung == "Gedung B":
        st.image("https://via.placeholder.com/800x300.png?text=Foto+Gedung+B", caption="Halaman Gedung B")
    elif nama_gedung == "Gedung E":
        st.image("https://via.placeholder.com/800x300.png?text=Foto+Gedung+E", caption="Halaman Gedung E")
    elif nama_gedung == "Gedung F":
        st.image("https://via.placeholder.com/800x300.png?text=Foto+Gedung+F", caption="Halaman Gedung F")
    elif nama_gedung == "Gedung G":
        st.image("https://via.placeholder.com/800x300.png?text=Foto+Gedung+G", caption="Halaman Gedung G")
    
    st.divider()
    st.write("### Pilih Laboratorium:")
    
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    
    # Menampilkan tombol lab secara menyamping (grid)
    if lab_di_gedung:
        cols = st.columns(len(lab_di_gedung))
        for i, (nama_lab, info) in enumerate(lab_di_gedung.items()):
            with cols[i]:
                if st.button(f"ℹ️ Informasi {nama_lab}", key=info["key"]):
                    st.session_state.lab_terpilih = nama_lab
                    st.rerun()

def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")
    lab_nama = st.selectbox("Pilih Lab", list(DATABASE_LAB.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])
    
    jadwal_hari = DATABASE_LAB[lab_nama]["jadwal"].get(hari)
    if jadwal_hari:
        for jam, kls in jadwal_hari.items():
            st.info(f"🕒 **{jam}** — Kelas **{kls}**")
    else:
        st.warning("Tidak ada jadwal pada hari tersebut.")

# ===============================
# ROUTING UTAMA
# ===============================
with st.sidebar:
    st.title("🧪 Menu Lab")
    menu = st.radio("Pilih Navigasi", ["Jadwal Lab", "Gedung B", "Gedung E", "Gedung F", "Gedung G"], on_change=reset_lab)

if st.session_state.lab_terpilih:
    halaman_detail_lab(st.session_state.lab_terpilih)
else:
    if menu == "Jadwal Lab":
        lihat_jadwal()
    else:
        tampilkan_gedung(menu)
