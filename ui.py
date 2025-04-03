import gradio as gr
from auth import login_user, register_user
from config import save_criteria, get_latest_criteria
from pdf_processor import extract_text_from_pdf
from ai_reviewer import review_text

# State untuk menyimpan user_id
user_id_state = gr.State()

def login(username: str, password: str, main_tab_visible):
    user_id = login_user(username, password)
    if user_id:
        return user_id, "Login berhasil!", gr.update(visible=True)
    return None, "Login gagal. Periksa username atau password.", main_tab_visible

def register(username: str, password: str, main_tab_visible):
    user_id = register_user(username, password)
    return user_id, f"Pengguna {username} berhasil dibuat!", gr.update(visible=True)

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
    
    main_tab_visible = gr.State(value=False)  # State untuk visibilitas tab Main
    
    with gr.Tab("Login", id="login-tab"):
        username_input = gr.Textbox(label="Username")
        password_input = gr.Textbox(label="Password", type="password")
        login_btn = gr.Button("Login")
        register_btn = gr.Button("Register")
        login_status = gr.Textbox(label="Status", interactive=False)
        login_btn.click(
            login,
            inputs=[username_input, password_input, main_tab_visible],
            outputs=[user_id_state, login_status, main_tab_visible]
        )
        register_btn.click(
            register,
            inputs=[username_input, password_input, main_tab_visible],
            outputs=[user_id_state, login_status, main_tab_visible]
        )

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

    # Update visibilitas tab Main berdasarkan state
    demo.load(
        lambda x: gr.update(visible=x),
        inputs=main_tab_visible,
        outputs=main_tab
    )

demo.launch()