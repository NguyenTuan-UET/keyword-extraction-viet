import gradio as gr
from transformers import AutoModel, AutoModelForTokenClassification

from pipeline import KeywordExtractorPipeline


def extract_keyword(title, text, top_n, ngram_low_range, ngram_high_range, min_freq, diversify_result):
    inp = {"text": text, "title": title}
    keyword_ls = kw_pipeline(inputs=inp, min_freq=min_freq, ngram_n=(ngram_low_range, ngram_high_range),
                             top_n=top_n, diversify_result=diversify_result)
    result = ''
    for kw, score in keyword_ls:
        result += f'{kw}: {score:.4f}\n'
    return result


if gr.NO_RELOAD:
    # Sửa: Load từ HuggingFace thay vì file .pt
    print("Loading PhoBERT model from HuggingFace...")
    phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
    phobert.eval()

    print("Loading NER model from HuggingFace...")
    ner_model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
    ner_model.eval()
    
    kw_pipeline = KeywordExtractorPipeline(phobert, ner_model)

if __name__ == "__main__":
    demo = gr.Interface(
        fn=extract_keyword,
        inputs=[
            gr.Text(
                label="Title (Tiêu đề)",
                lines=1,
                value="",
                placeholder="Nhập tiêu đề văn bản (có thể bỏ trống)"
            ),
            gr.Textbox(
                label="Text (Nội dung văn bản)",
                lines=10,
                value="",
                placeholder="Nhập văn bản tiếng Việt cần trích xuất từ khóa..."
            ),
            gr.Number(
                label="Top N keywords",
                info="Số lượng từ khóa muốn lấy",
                value=10,
                minimum=1,
                maximum=50
            ),
            gr.Number(
                label="Ngram low range",
                info="Độ dài ngram tối thiểu (1=từ đơn, 2=cụm 2 từ)",
                value=1,
                minimum=1,
                maximum=5
            ),
            gr.Number(
                label="Ngram high range",
                info="Độ dài ngram tối đa (3=cụm 3 từ)",
                value=3,
                minimum=1,
                maximum=5
            ),
            gr.Number(
                label="Ngram minimum frequency",
                info="Tần suất xuất hiện tối thiểu của ngram",
                value=1,
                minimum=1,
                maximum=10
            ),
            gr.Checkbox(
                label="Diversify result",
                info="Đa dạng hóa kết quả (dùng K-means clustering)",
                value=False
            )
        ],
        outputs=gr.Textbox(
            label="Keywords Extracted (Từ khóa trích xuất)",
            lines=15
        ),
        title="KeyBERTVi - Trích xuất từ khóa tiếng Việt",
        description="""
        ## Hướng dẫn sử dụng:
        1. Nhập **tiêu đề** (optional) và **nội dung văn bản** tiếng Việt
        2. Điều chỉnh các tham số:
           - **Top N**: Số lượng từ khóa (5-20 phù hợp)
           - **Ngram range**: (1,3) để lấy từ đơn và cụm từ
           - **Min frequency**: Tần suất tối thiểu (1 cho văn bản ngắn, 2-3 cho văn bản dài)
           - **Diversify**: Tích nếu muốn từ khóa đa dạng về chủ đề
        3. Nhấn **Submit** để xem kết quả
        """,
        examples=[
            [
                "Truyền thuyết và hiện tại Thành Cổ Loa",
                """Nhắc đến Cổ Loa, người ta nghĩ ngay đến truyền thuyết về An Dương Vương được thần Kim Quy bày cho cách xây thành, về chiếc lẫy nỏ thần làm từ móng chân rùa thần và mối tình bi thương Mỵ Châu – Trọng Thủy. Đằng sau những câu chuyện thiên về tâm linh ấy, thế hệ con cháu còn khám phá được những giá trị khảo cổ to lớn của Cổ Loa.
Khu di tích Cổ Loa cách trung tâm Hà Nội 17km thuộc huyện Đông Anh, Hà Nội, có diện tích bảo tồn gần 500ha được coi là địa chỉ văn hóa đặc biệt của thủ đô và cả nước. Cổ Loa có hàng loạt di chỉ khảo cổ học đã được phát hiện, phản ánh quá trình phát triển liên tục của dân tộc ta từ sơ khai qua các thời kỳ đồ đồng, đồ đá và đồ sắt mà đỉnh cao là văn hóa Đông Sơn, vẫn được coi là nền văn minh sông Hồng thời kỳ tiền sử của dân tộc Việt Nam.
Cổ Loa từng là kinh đô của nhà nước Âu Lạc thời kỳ An Dương Vương (thế kỷ III TCN) và của nước Đại Việt thời Ngô Quyền (thế kỷ X) mà thành Cổ Loa là một di tích minh chứng còn lại cho đến ngày nay. Thành Cổ Loa được các nhà khảo cổ học đánh giá là "tòa thành cổ nhất, quy mô lớn vào bậc nhất, cấu trúc cũng thuộc loại độc đáo nhất trong lịch sử xây dựng thành lũy của người Việt cổ".""",
                5, 1, 3, 1, False
            ],
            [
                "",
                """Trí tuệ nhân tạo (AI) đang thay đổi mọi khía cạnh của cuộc sống. Từ y tế, giáo dục đến giao thông, AI mang lại nhiều cải tiến vượt bậc. Các thuật toán học máy giúp chẩn đoán bệnh chính xác hơn, xe tự lái giảm tai nạn giao thông, và chatbot hỗ trợ khách hàng 24/7.""",
                10, 1, 3, 1, True
            ]
        ],
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            font-family: 'Arial', sans-serif;
        }
        """
    )

    demo.launch(share=True)