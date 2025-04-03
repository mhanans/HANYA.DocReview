import gradio as gr
from auth import login_user, register_user
from config import save_criteria, get_latest_criteria
from pdf_processor import extract_text_from_pdf
from ai_reviewer import review_text

# State untuk menyimpan user_id
user_id_state = gr.State()

def login(username: str, password: str):
    user_id = login_user(username, password)
    if user_id:
        return user_id, "Login berhasil!", gr.update(visible=True), "main-tab"
    return None, "Login gagal. Periksa username atau password.", gr.update(visible=False), "login-tab"

def register(username: str, password: str):
    user_id = register_user(username, password)
    return user_id, f"Pengguna {username} berhasil dibuat!", gr.update(visible=True), "main-tab"

def save_config(user_id: str, criteria: str):
    if not user_id:
        return "Silakan login terlebih dahulu."
    save_criteria(user_id, criteria)
    return "Kriteria disimpan: " + criteria

def review_pdf(user_id: str, pdf_file):
    if not user_id:
        return "Silakan login terlebih dahulu."
    criteria = get_latest_criteria(user_id)
    if not criteria:
        return "Silakan masukkan kriteria di tab Config terlebih dahulu."
    
    text_per_page = extract_text_from_pdf(pdf_file)
    review_results = {}
    for page, text in text_per_page.items():
        if text != "Tidak ada teks yang dapat diekstrak.":
            review_results[page] = review_text(text, criteria)
        else:
            review_results[page] = text
    
    output = ""
    for page, review in review_results.items():
        output += f"**Halaman {page}:**\n{review}\n\n"
    return output

with gr.Blocks() as demo:
    gr.Markdown("## Aplikasi Review Dokumen PDF")
    
    # State untuk melacak tab yang dipilih
    tab_state = gr.State(value="login-tab")
    
    with gr.Tabs(selected=tab_state) as tabs:
        with gr.Tab("Login", id="login-tab"):
            username_input = gr.Textbox(label="Username")
            password_input = gr.Textbox(label="Password", type="password")
            login_btn = gr.Button("Login")
            register_btn = gr.Button("Register")
            login_status = gr.Textbox(label="Status", interactive=False)
        
        with gr.Tab("Main", id="main-tab", visible=False) as main_tab:
            with gr.Tab("Config"):
                criteria_input = gr.Textbox(label="Masukkan Kriteria Review")
                save_btn = gr.Button("Simpan Kriteria")
                config_status = gr.Textbox(label="Status", interactive=False)
                save_btn.click(
                    save_config,
                    inputs=[user_id_state, criteria_input],
                    outputs=config_status
                )
            with gr.Tab("Action"):
                pdf_input = gr.File(label="Unggah PDF")
                review_btn = gr.Button("Review")
                review_output = gr.Textbox(label="Hasil Review", lines=10, interactive=False)
                review_btn.click(
                    review_pdf,
                    inputs=[user_id_state, pdf_input],
                    outputs=review_output
                )

    # Event handler untuk login dan register
    login_btn.click(
        login,
        inputs=[username_input, password_input],
        outputs=[user_id_state, login_status, main_tab, tab_state]
    ).then(
        lambda tab: gr.update(selected=tab),
        inputs=tab_state,
        outputs=tabs
    )

    register_btn.click(
        register,
        inputs=[username_input, password_input],
        outputs=[user_id_state, login_status, main_tab, tab_state]
    ).then(
        lambda tab: gr.update(selected=tab),
        inputs=tab_state,
        outputs=tabs
    )

demo.launch()