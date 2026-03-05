# 🔑 KeyBERTVi - Trích xuất Từ khóa Tiếng Việt

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Công cụ trích xuất từ khóa tự động cho văn bản tiếng Việt**

Sử dụng PhoBERT + NER + VnCoreNLP

</div>

---

## 📖 Giới thiệu

KeyBERTVi là công cụ trích xuất từ khóa (keyword extraction) cho tiếng Việt, lấy cảm hứng từ [KeyBERT](https://github.com/MaartenGr/KeyBERT). 

### Cách hoạt động:

1. **Tiền xử lý**: Chuẩn hóa văn bản, tách từ tiếng Việt bằng VnCoreNLP
2. **Named Entity Recognition**: Nhận diện tên riêng (người, địa danh, tổ chức)
3. **Tạo Embeddings**: Sử dụng PhoBERT để tạo vector cho document và các n-grams
4. **Tính Similarity**: Dùng Cosine Similarity để tìm n-grams tương đồng nhất với document
5. **Chọn Keywords**: Lấy top-N keywords với score cao nhất

### Tính năng:

- ✅ Trích xuất từ khóa đơn (unigram) và cụm từ (bigram, trigram, ...)
- ✅ Tích hợp NER để bắt tên riêng quan trọng
- ✅ Hỗ trợ đa dạng hóa kết quả (K-means clustering)
- ✅ Giao diện web thân thiện (Gradio)
- ✅ API Python đơn giản

---

## 📑 Mục lục

1. [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
2. [Cài đặt](#-cài-đặt)
3. [Cách chạy dự án](#-cách-chạy-dự-án)
4. [Sử dụng cơ bản](#-sử-dụng-cơ-bản)
5. [Các tham số](#️-các-tham-số)
6. [Ví dụ nâng cao](#-ví-dụ-nâng-cao)
7. [Khắc phục sự cố](#-khắc-phục-sự-cố)


---

## 🚀 Cài đặt

### Bước 1: Clone repository

```bash
git clone https://github.com/NguyenTuan-UET/keyword-extraction-viet.git
cd keyword-extraction-viet
```

### Bước 2: Cài đặt Java (nếu chưa có)

# 🔑 KeyBERTVi - Trích xuất Từ khóa Tiếng Việt

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Công cụ trích xuất từ khóa tự động cho văn bản tiếng Việt**

Sử dụng PhoBERT + NER + VnCoreNLP

</div>

---

## 📖 Giới thiệu

KeyBERTVi là công cụ trích xuất từ khóa (keyword extraction) cho tiếng Việt, lấy cảm hứng từ [KeyBERT](https://github.com/MaartenGr/KeyBERT). 

### Cách hoạt động:

1. **Tiền xử lý**: Chuẩn hóa văn bản, tách từ tiếng Việt bằng VnCoreNLP
2. **Named Entity Recognition**: Nhận diện tên riêng (người, địa danh, tổ chức)
3. **Tạo Embeddings**: Sử dụng PhoBERT để tạo vector cho document và các n-grams
4. **Tính Similarity**: Dùng Cosine Similarity để tìm n-grams tương đồng nhất với document
5. **Chọn Keywords**: Lấy top-N keywords với score cao nhất

### Tính năng:

- ✅ Trích xuất từ khóa đơn (unigram) và cụm từ (bigram, trigram, ...)
- ✅ Tích hợp NER để bắt tên riêng quan trọng
- ✅ Hỗ trợ đa dạng hóa kết quả (K-means clustering)
- ✅ Giao diện web thân thiện (Gradio)
- ✅ API Python đơn giản

---

## 📑 Mục lục

1. [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
2. [Cài đặt](#-cài-đặt)
3. [Cách chạy dự án](#-cách-chạy-dự-án)
4. [Sử dụng cơ bản](#-sử-dụng-cơ-bản)
5. [Các tham số](#️-các-tham-số)
6. [Ví dụ nâng cao](#-ví-dụ-nâng-cao)
7. [Khắc phục sự cố](#-khắc-phục-sự-cố)

---

## 💻 Yêu cầu hệ thống

- **Python**: 3.8 hoặc cao hơn
- **Java JDK**: 8, 11, hoặc 17 (cho VnCoreNLP)
- **RAM**: Tối thiểu 4GB (khuyến nghị 8GB)
- **Dung lượng**: ~2GB cho models và dependencies

---

## 🚀 Cài đặt

### Bước 1: Clone repository

```bash
git clone https://github.com/NguyenTuan-UET/keyword-extraction-viet.git
cd keyword-extraction-viet
```

### Bước 2: Cài đặt Java (nếu chưa có)

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

**Mac:**
```bash
brew install openjdk@11
```

**Windows:**
Download và cài đặt từ [Oracle](https://www.oracle.com/java/technologies/downloads/)

**Kiểm tra:**
```bash
java -version
```

### Bước 3: Tạo môi trường ảo Python

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# hoặc
.venv\\Scripts\\activate  # Windows
```

### Bước 4: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 5: Tải models (tự động)

Models sẽ tự động tải về khi chạy lần đầu:
- **PhoBERT**: ~540MB từ HuggingFace
- **NER Model**: ~532MB từ HuggingFace
- **VnCoreNLP**: ~150MB

**Lưu ý**: Lần chạy đầu tiên sẽ mất 5-10 phút để tải models.

---

## 🎮 Cách chạy dự án

Có **3 cách** để chạy dự án:

### 1️⃣ Giao diện Web (Gradio) - **Dễ nhất**

Chạy lệnh:

```bash
python app.py
```

Mở trình duyệt tại: `http://localhost:7860`

### 2️⃣ Python API - **Linh hoạt nhất**

Tạo file `test.py`:

```python
from pipeline import KeywordExtractorPipeline
from transformers import AutoModel, AutoModelForTokenClassification

# Load models
phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
ner_model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")

# Tạo pipeline
kw_pipeline = KeywordExtractorPipeline(phobert, ner_model)

# Trích xuất keywords
text = "Trường Đại học Công nghệ là một trong những trường hàng đầu về CNTT tại Việt Nam."
keywords = kw_pipeline(
    inputs={"text": text},
    top_n=5,
    ngram_n=(1, 2),
    min_freq=1,
    diversify_result=False
)

print(keywords)
```

Chạy:
```bash
python test.py
```

### 3️⃣ Command Line - **Nhanh nhất**

Sửa file `test_file.txt` với văn bản của bạn, sau đó:

```bash
python pipeline.py
```

---

## 📚 Sử dụng cơ bản

### Ví dụ 1: Trích xuất từ khóa đơn giản

```python
from pipeline import KeywordExtractorPipeline
from transformers import AutoModel, AutoModelForTokenClassification

# Load models
phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
ner_model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
kw_pipeline = KeywordExtractorPipeline(phobert, ner_model)

# Văn bản đầu vào
text = """
Trí tuệ nhân tạo (AI) đang thay đổi cuộc sống con người. 
Machine Learning và Deep Learning là hai nhánh quan trọng của AI.
Các ứng dụng AI xuất hiện ở mọi lĩnh vực từ y tế đến giáo dục.
"""

# Trích xuất 5 keywords
keywords = kw_pipeline(inputs={"text": text}, top_n=5)

# Kết quả: [('Trí_tuệ nhân_tạo', 0.89), ('Machine_Learning', 0.85), ...]
```

### Ví dụ 2: Trích xuất với tiêu đề

```python
title = "Trí tuệ nhân tạo trong y tế"
text = "AI đang cách mạng hóa ngành y tế..."

keywords = kw_pipeline(
    inputs={"title": title, "text": text},  # Có title
    top_n=10
)
```

**Lưu ý**: Khi có `title`, nó sẽ được ghép vào đầu text và được tăng trọng số (x2).

### Ví dụ 3: Trích xuất cụm từ (N-grams)

```python
# Chỉ từ đơn (unigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 1),  # min=1, max=1
    top_n=5
)

# Từ đơn + cụm 2 từ (unigrams + bigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 2),  # min=1, max=2
    top_n=5
)

# Cụm từ 1-3 từ (unigrams + bigrams + trigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 3),  # min=1, max=3
    top_n=10
)
```

### Ví dụ 4: Lọc theo tần suất

```python
# Chỉ lấy keywords xuất hiện ≥2 lần
keywords = kw_pipeline(
    inputs={"text": text},
    min_freq=2,  # Lọc keywords hiếm
    top_n=10
)
```

**Khuyến nghị**: 
- Văn bản ngắn (<500 từ): `min_freq=1`
- Văn bản trung bình (500-2000 từ): `min_freq=2`
- Văn bản dài (>2000 từ): `min_freq=3-5`

### Ví dụ 5: Đa dạng hóa kết quả

```python
# Không đa dạng hóa (lấy top keywords tương đồng nhất)
keywords = kw_pipeline(
    inputs={"text": text},
    diversify_result=False,  # Default
    top_n=5
)

# Đa dạng hóa (dùng K-means để nhóm keywords)
keywords = kw_pipeline(
    inputs={"text": text},
    diversify_result=True,  # Bật diversification
    top_n=5
)
```

**Khi nào dùng `diversify_result=True`?**
- ✅ Văn bản đề cập **nhiều chủ đề** (ví dụ: bài báo tổng hợp)
- ✅ Muốn keywords **đa dạng** hơn
- ❌ Văn bản **một chủ đề** rõ ràng → dùng `False` để tập trung

---

## ⚙️ Các tham số

### Bảng tham số của `kw_pipeline()`

| Tham số | Kiểu | Mặc định | Mô tả |
|---------|------|----------|-------|
| `inputs` | dict | **Bắt buộc** | `{"text": str}` hoặc `{"title": str, "text": str}` |
| `top_n` | int | `5` | Số lượng keywords trả về |
| `ngram_n` | tuple | `(1, 3)` | Min và max số từ trong cụm. VD: `(1,1)`, `(1,2)`, `(1,3)`, `(2,3)` |
| `min_freq` | int | `1` | Lọc keywords xuất hiện dưới n lần |
| `diversify_result` | bool | `False` | Đa dạng hóa kết quả bằng K-means |

### Chi tiết các tham số:

#### 1. `inputs` - Văn bản đầu vào

```python
# Chỉ có text
inputs = {"text": "Nội dung văn bản..."}

# Có cả title (title được tăng trọng số x2)
inputs = {
    "title": "Tiêu đề bài viết",
    "text": "Nội dung văn bản..."
}
```

#### 2. `top_n` - Số lượng keywords

```python
top_n=5   # Lấy 5 keywords
top_n=10  # Lấy 10 keywords
top_n=20  # Lấy 20 keywords
```

**Khuyến nghị theo độ dài văn bản:**
- Ngắn (<200 từ): `top_n=5`
- Trung bình (200-1000 từ): `top_n=10`
- Dài (>1000 từ): `top_n=15-20`

#### 3. `ngram_n` - Loại cụm từ

```python
ngram_n=(1, 1)  # Chỉ từ đơn: "AI", "y_tế", "giáo_dục"
ngram_n=(1, 2)  # Từ đơn + 2 từ: "AI", "trí_tuệ nhân_tạo"
ngram_n=(1, 3)  # 1-3 từ: "AI", "trí_tuệ nhân_tạo", "trí_tuệ nhân_tạo trong y_tế"
ngram_n=(2, 3)  # Chỉ cụm 2-3 từ (không có từ đơn)
```

**Khuyến nghị:**
- Bài báo ngắn: `(1, 2)`
- Bài báo khoa học: `(1, 3)` ⭐ **Phổ biến nhất**
- Tìm cụm từ chuyên ngành: `(2, 3)`

#### 4. `min_freq` - Tần suất tối thiểu

```python
min_freq=1  # Không lọc (giữ tất cả)
min_freq=2  # Chỉ giữ keywords xuất hiện ≥2 lần
min_freq=3  # Chỉ giữ keywords xuất hiện ≥3 lần
```

**Khuyến nghị:**
- Văn bản ngắn: `min_freq=1`
- Văn bản dài, muốn lọc noise: `min_freq=2-3`

#### 5. `diversify_result` - Đa dạng hóa

```python
diversify_result=False  # Không đa dạng (lấy keywords tương đồng nhất)
diversify_result=True   # Đa dạng hóa (dùng K-means clustering)
```

**Cách hoạt động:**
- `False`: Lấy top-N keywords có **cosine similarity cao nhất** với document
- `True`: Dùng **K-means** để nhóm keywords thành K clusters, lấy 1 đại diện mỗi cluster

---

## 🎯 Ví dụ nâng cao

### Ví dụ 1: Bài báo tin tức

```python
title = "Apple ra mắt iPhone 15 với nhiều cải tiến"
text = """
Apple vừa chính thức giới thiệu dòng iPhone 15 tại sự kiện đặc biệt. 
iPhone 15 Pro Max được trang bị chip A17 Bionic mạnh mẽ và camera 48MP.
Giá bán khởi điểm từ 999 USD tại thị trường Mỹ.
Sản phẩm sẽ có mặt tại Việt Nam vào tháng 10.
"""

keywords = kw_pipeline(
    inputs={"title": title, "text": text},
    top_n=8,
    ngram_n=(1, 2),
    min_freq=1,
    diversify_result=True  # Bài báo đề cập nhiều khía cạnh
)

# Kết quả có thể:
# [('iPhone_15', 0.92), ('Apple', 0.88), ('chip A17_Bionic', 0.85), 
#  ('camera 48MP', 0.82), ('giá_bán', 0.78), ...]
```

### Ví dụ 2: Văn bản học thuật

```python
text = """
Nghiên cứu này tập trung vào ứng dụng học sâu trong xử lý ngôn ngữ tự nhiên.
Chúng tôi đề xuất mô hình Transformer cải tiến cho bài toán dịch máy.
Kết quả thử nghiệm trên tập dữ liệu IWSLT cho thấy BLEU score tăng 3.2 điểm.
Phương pháp của chúng tôi vượt trội so với các baseline hiện tại.
"""

keywords = kw_pipeline(
    inputs={"text": text},
    top_n=10,
    ngram_n=(1, 3),  # Bắt cụm từ chuyên ngành
    min_freq=1,
    diversify_result=False  # Tập trung vào chủ đề chính
)

# Kết quả tập trung vào NLP & Deep Learning:
# [('học_sâu', 0.91), ('xử_lý ngôn_ngữ tự_nhiên', 0.89), 
#  ('mô_hình Transformer', 0.87), ('dịch_máy', 0.85), ...]
```

### Ví dụ 3: Xử lý batch (nhiều documents)

```python
documents = [
    "Văn bản 1 về AI...",
    "Văn bản 2 về blockchain...",
    "Văn bản 3 về IoT..."
]

all_keywords = []
for doc in documents:
    keywords = kw_pipeline(
        inputs={"text": doc},
        top_n=5,
        ngram_n=(1, 2)
    )
    all_keywords.append(keywords)

# Xử lý kết quả
for i, kws in enumerate(all_keywords):
    print(f"Document {i+1}: {kws}")
```

### Ví dụ 4: Kết hợp tất cả tham số

```python
# Cấu hình tối ưu cho bài báo dài, nhiều chủ đề
keywords = kw_pipeline(
    inputs={
        "title": "Tiêu đề bài báo",
        "text": "Nội dung dài..."
    },
    top_n=15,              # Lấy nhiều keywords
    ngram_n=(1, 3),        # Từ đơn đến cụm 3 từ
    min_freq=2,            # Lọc keywords hiếm
    diversify_result=True  # Đa dạng hóa
)
```

---

## 🐛 Khắc phục sự cố

### Lỗi 1: `ModuleNotFoundError`

```
ModuleNotFoundError: No module named 'transformers'
```

**Nguyên nhân**: Chưa cài dependencies

**Giải pháp**:
```bash
pip install -r requirements.txt
```

### Lỗi 2: Java không tìm thấy

```
Exception: Unable to find javac
```

**Nguyên nhân**: Chưa cài Java JDK

**Giải pháp**:
```bash
# Ubuntu/Debian
sudo apt install openjdk-11-jdk

# Mac
brew install openjdk@11

# Windows: Tải từ oracle.com
```

### Lỗi 3: Model tải lâu

**Nguyên nhân**: Models tải từ HuggingFace lần đầu (~1.2GB)

**Giải pháp**: Đợi 5-10 phút. Các lần sau sẽ dùng cache.

### Lỗi 4: Out of Memory

```
RuntimeError: CUDA out of memory
```

**Nguyên nhân**: GPU/RAM không đủ

**Giải pháp**:
- Giảm `top_n`
- Giảm `ngram_n` (ví dụ từ `(1,3)` xuống `(1,2)`)
- Chia nhỏ văn bản nếu quá dài
- Chạy trên CPU (tự động nếu không có GPU)

### Lỗi 5: Kết quả không chính xác

**Nguyên nhân**: Tham số chưa phù hợp

**Giải pháp**:
- Tăng `top_n` để xem nhiều kết quả hơn
- Thử `diversify_result=True` hoặc `False`
- Điều chỉnh `ngram_n` phù hợp với văn bản
- Tăng `min_freq` để lọc noise

### Lỗi 6: Port 7860 đã được sử dụng

```
OSError: [Errno 98] Address already in use
```

**Giải pháp**:
```bash
# Kill process đang dùng port 7860
lsof -ti:7860 | xargs kill -9

# Hoặc đổi port trong app.py:
# demo.launch(server_port=7861)
```

---

## 📊 So sánh cấu hình

| Loại văn bản | top_n | ngram_n | min_freq | diversify |
|--------------|-------|---------|----------|-----------|
| Bài báo ngắn | 5 | (1, 2) | 1 | False |
| Bài báo dài | 10-15 | (1, 3) | 2 | True |
| Văn bản học thuật | 10 | (1, 3) | 1 | False |
| Mô tả sản phẩm | 5-8 | (1, 2) | 1 | False |
| Tóm tắt nhiều chủ đề | 15-20 | (1, 3) | 2 | True |

---

## 🔧 Cấu trúc dự án

```
keyword-extraction-viet/
├── app.py                          # Gradio web interface
├── pipeline.py                     # Main KeywordExtractorPipeline
├── requirements.txt                # Dependencies
├── test_file.txt                   # File test mẫu
├── vietnamese-stopwords-dash.txt   # Danh sách stopwords
├── model/
│   ├── keyword_extraction_utils.py # Core extraction logic
│   ├── named_entities.py           # NER functions
│   └── process_text.py             # Text preprocessing
└── pretrained-models/
    └── vncorenlp/                  # VnCoreNLP models
```

---

## 🙏 Tham khảo

1. [KeyBERT](https://github.com/MaartenGr/KeyBERT) - Ý tưởng gốc
2. [PhoBERT](https://github.com/VinAIResearch/PhoBERT) - Vietnamese BERT
3. [NER ELECTRA](https://huggingface.co/NlpHUST/ner-vietnamese-electra-base) - Named Entity Recognition
4. [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) - Vietnamese NLP toolkit
5. [Underthesea](https://github.com/undertheseanlp/underthesea) - Vietnamese NLP library

---

## 📝 License

MIT License - Xem file `LICENSE` để biết chi tiết.

---

## 👥 Contributors

- **Nguyễn Tuấn** - [@NguyenTuan-UET](https://github.com/NguyenTuan-UET)

---

## 📧 Liên hệ

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo [Issue](https://github.com/NguyenTuan-UET/keyword-extraction-viet/issues) trên GitHub.

---

<div align="center">

⭐ **Nếu thấy hữu ích, hãy cho repo một star nhé!** ⭐

</div>

    min_freq=1,
    diversify_result=False
)

print(keywords)
```

Chạy:
```bash
python test.py
```

---

## 📚 Sử dụng cơ bản

### Ví dụ 1: Trích xuất từ khóa đơn giản

```python
from pipeline import KeywordExtractorPipeline
from transformers import AutoModel, AutoModelForTokenClassification

# Load models
phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
ner_model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
kw_pipeline = KeywordExtractorPipeline(phobert, ner_model)

# Văn bản đầu vào
text = """
Trí tuệ nhân tạo (AI) đang thay đổi cuộc sống con người. 
Machine Learning và Deep Learning là hai nhánh quan trọng của AI.
Các ứng dụng AI xuất hiện ở mọi lĩnh vực từ y tế đến giáo dục.
"""

# Trích xuất 5 keywords
keywords = kw_pipeline(inputs={"text": text}, top_n=5)

# Kết quả: [('Trí_tuệ nhân_tạo', 0.89), ('Machine_Learning', 0.85), ...]
```

### Ví dụ 2: Trích xuất với tiêu đề

```python
title = "Trí tuệ nhân tạo trong y tế"
text = "AI đang cách mạng hóa ngành y tế..."

keywords = kw_pipeline(
    inputs={"title": title, "text": text},  # Có title
    top_n=10
)
```

**Lưu ý**: Khi có `title`, nó sẽ được ghép vào đầu text và được tăng trọng số (x2).

### Ví dụ 3: Trích xuất cụm từ (N-grams)

```python
# Chỉ từ đơn (unigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 1),  # min=1, max=1
    top_n=5
)

# Từ đơn + cụm 2 từ (unigrams + bigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 2),  # min=1, max=2
    top_n=5
)

# Cụm từ 1-3 từ (unigrams + bigrams + trigrams)
keywords = kw_pipeline(
    inputs={"text": text},
    ngram_n=(1, 3),  # min=1, max=3
    top_n=10
)
```

### Ví dụ 4: Lọc theo tần suất

```python
# Chỉ lấy keywords xuất hiện ≥2 lần
keywords = kw_pipeline(
    inputs={"text": text},
    min_freq=2,  # Lọc keywords hiếm
    top_n=10
)
```

**Khuyến nghị**: 
- Văn bản ngắn (<500 từ): `min_freq=1`
- Văn bản trung bình (500-2000 từ): `min_freq=2`
- Văn bản dài (>2000 từ): `min_freq=3-5`

### Ví dụ 5: Đa dạng hóa kết quả

```python
# Không đa dạng hóa (lấy top keywords tương đồng nhất)
keywords = kw_pipeline(
    inputs={"text": text},
    diversify_result=False,  # Default
    top_n=5
)

# Đa dạng hóa (dùng K-means để nhóm keywords)
keywords = kw_pipeline(
    inputs={"text": text},
    diversify_result=True,  # Bật diversification
    top_n=5
)
```

**Khi nào dùng `diversify_result=True`?**
- ✅ Văn bản đề cập **nhiều chủ đề** (ví dụ: bài báo tổng hợp)
- ✅ Muốn keywords **đa dạng** hơn
- ❌ Văn bản **một chủ đề** rõ ràng → dùng `False` để tập trung

---

## ⚙️ Các tham số

### Bảng tham số của `kw_pipeline()`

| Tham số | Kiểu | Mặc định | Mô tả |
|---------|------|----------|-------|
| `inputs` | dict | **Bắt buộc** | `{"text": str}` hoặc `{"title": str, "text": str}` |
| `top_n` | int | `5` | Số lượng keywords trả về |
| `ngram_n` | tuple | `(1, 3)` | Min và max số từ trong cụm. VD: `(1,1)`, `(1,2)`, `(1,3)`, `(2,3)` |
| `min_freq` | int | `1` | Lọc keywords xuất hiện dưới n lần |
| `diversify_result` | bool | `False` | Đa dạng hóa kết quả bằng K-means |

### Chi tiết các tham số:

#### 1. `inputs` - Văn bản đầu vào

```python
# Chỉ có text
inputs = {"text": "Nội dung văn bản..."}

# Có cả title (title được tăng trọng số x2)
inputs = {
    "title": "Tiêu đề bài viết",
    "text": "Nội dung văn bản..."
}
```

#### 2. `top_n` - Số lượng keywords

```python
top_n=5   # Lấy 5 keywords
top_n=10  # Lấy 10 keywords
top_n=20  # Lấy 20 keywords
```

**Khuyến nghị theo độ dài văn bản:**
- Ngắn (<200 từ): `top_n=5`
- Trung bình (200-1000 từ): `top_n=10`
- Dài (>1000 từ): `top_n=15-20`

#### 3. `ngram_n` - Loại cụm từ

```python
ngram_n=(1, 1)  # Chỉ từ đơn: "AI", "y_tế", "giáo_dục"
ngram_n=(1, 2)  # Từ đơn + 2 từ: "AI", "trí_tuệ nhân_tạo"
ngram_n=(1, 3)  # 1-3 từ: "AI", "trí_tuệ nhân_tạo", "trí_tuệ nhân_tạo trong y_tế"
ngram_n=(2, 3)  # Chỉ cụm 2-3 từ (không có từ đơn)
```

**Khuyến nghị:**
- Bài báo ngắn: `(1, 2)`
- Bài báo khoa học: `(1, 3)` ⭐ **Phổ biến nhất**
- Tìm cụm từ chuyên ngành: `(2, 3)`

#### 4. `min_freq` - Tần suất tối thiểu

```python
min_freq=1  # Không lọc (giữ tất cả)
min_freq=2  # Chỉ giữ keywords xuất hiện ≥2 lần
min_freq=3  # Chỉ giữ keywords xuất hiện ≥3 lần
```

**Khuyến nghị:**
- Văn bản ngắn: `min_freq=1`
- Văn bản dài, muốn lọc noise: `min_freq=2-3`

#### 5. `diversify_result` - Đa dạng hóa

```python
diversify_result=False  # Không đa dạng (lấy keywords tương đồng nhất)
diversify_result=True   # Đa dạng hóa (dùng K-means clustering)
```

**Cách hoạt động:**
- `False`: Lấy top-N keywords có **cosine similarity cao nhất** với document
- `True`: Dùng **K-means** để nhóm keywords thành K clusters, lấy 1 đại diện mỗi cluster

**Khi nào dùng?**

| Trường hợp | Nên dùng |
|------------|----------|
| Văn bản **một chủ đề** rõ ràng | `False` |
| Văn bản **nhiều chủ đề/khía cạnh** | `True` |
| Muốn keywords **tập trung** vào chủ đề chính | `False` |
| Muốn keywords **đa dạng**, bao quát nhiều góc độ | `True` |

---

## 🎯 Ví dụ nâng cao

### Ví dụ 1: Bài báo tin tức

```python
title = "Apple ra mắt iPhone 15 với nhiều cải tiến"
text = """
Apple vừa chính thức giới thiệu dòng iPhone 15 tại sự kiện đặc biệt. 
iPhone 15 Pro Max được trang bị chip A17 Bionic mạnh mẽ và camera 48MP.
Giá bán khởi điểm từ 999 USD tại thị trường Mỹ.
Sản phẩm sẽ có mặt tại Việt Nam vào tháng 10.
"""

keywords = kw_pipeline(
    inputs={"title": title, "text": text},
    top_n=8,
    ngram_n=(1, 2),
    min_freq=1,
    diversify_result=True  # Bài báo đề cập nhiều khía cạnh
)

# Kết quả:
# [('iPhone_15', 0.92), ('Apple', 0.88), ('chip A17_Bionic', 0.85), 
#  ('camera 48MP', 0.82), ('giá_bán', 0.78), ...]
```

### Ví dụ 2: Văn bản học thuật

```python
text = """
Nghiên cứu này tập trung vào ứng dụng học sâu trong xử lý ngôn ngữ tự nhiên.
Chúng tôi đề xuất mô hình Transformer cải tiến cho bài toán dịch máy.
Kết quả thử nghiệm trên tập dữ liệu IWSLT cho thấy BLEU score tăng 3.2 điểm.
Phương pháp của chúng tôi vượt trội so với các baseline hiện tại.
"""

keywords = kw_pipeline(
    inputs={"text": text},
    top_n=10,
    ngram_n=(1, 3),  # Bắt cụm từ chuyên ngành
    min_freq=1,
    diversify_result=False  # Tập trung vào chủ đề chính
)

# Kết quả tập trung vào NLP & Deep Learning:
# [('học_sâu', 0.91), ('xử_lý ngôn_ngữ tự_nhiên', 0.89), 
#  ('mô_hình Transformer', 0.87), ('dịch_máy', 0.85), ...]
```

### Ví dụ 3: Xử lý batch (nhiều documents)

```python
documents = [
    "Văn bản 1 về AI...",
    "Văn bản 2 về blockchain...",
    "Văn bản 3 về IoT..."
]

all_keywords = []
for doc in documents:
    keywords = kw_pipeline(
        inputs={"text": doc},
        top_n=5,
        ngram_n=(1, 2)
    )
    all_keywords.append(keywords)

# Xử lý kết quả
for i, kws in enumerate(all_keywords):
    print(f"Document {i+1}: {kws}")
```

### Ví dụ 4: Kết hợp tất cả tham số

```python
# Cấu hình tối ưu cho bài báo dài, nhiều chủ đề
keywords = kw_pipeline(
    inputs={
        "title": "Tiêu đề bài báo",
        "text": "Nội dung dài..."
    },
    top_n=15,              # Lấy nhiều keywords
    ngram_n=(1, 3),        # Từ đơn đến cụm 3 từ
    min_freq=2,            # Lọc keywords hiếm
    diversify_result=True  # Đa dạng hóa
)
```

**Gợi ý**:
- Tăng `top_n` để xem nhiều kết quả hơn
- Thử `diversify_result=True` hoặc `False`
- Điều chỉnh `ngram_n` phù hợp với văn bản
- Tăng `min_freq` để lọc noise


## 📊 So sánh cấu hình

| Loại văn bản | top_n | ngram_n | min_freq | diversify |
|--------------|-------|---------|----------|-----------|
| Bài báo ngắn | 5 | (1, 2) | 1 | False |
| Bài báo dài | 10-15 | (1, 3) | 2 | True |
| Văn bản học thuật | 10 | (1, 3) | 1 | False |
| Mô tả sản phẩm | 5-8 | (1, 2) | 1 | False |
| Tóm tắt nhiều chủ đề | 15-20 | (1, 3) | 2 | True |

---

## Tham khảo

1. [KeyBERT](https://github.com/MaartenGr/KeyBERT) - Ý tưởng gốc
2. [PhoBERT](https://github.com/VinAIResearch/PhoBERT) - Vietnamese BERT
3. [NER ELECTRA](https://huggingface.co/NlpHUST/ner-vietnamese-electra-base) - Named Entity Recognition
4. [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) - Vietnamese NLP toolkit
5. [Underthesea](https://github.com/undertheseanlp/underthesea) - Vietnamese NLP library

---

## License

MIT License - Xem file `LICENSE` để biết chi tiết.

---

## Contributors

- **Nguyễn Tuấn** - [@NguyenTuan-UET](https://github.com/NguyenTuan-UET)

---

## Liên hệ

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo [Issue](https://github.com/NguyenTuan-UET/keyword-extraction-viet/issues) trên GitHub.

---