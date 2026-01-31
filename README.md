# KeyBert_VietNam
A version for extracting keywords from Vietnamese documents, inspired by KeyBERT.

# <a name="introduction"></a>  KeyBERTVi - Keyword Extraction for Vietnamese language

Inspired by [KeyBERT](https://github.com/MaartenGr/KeyBERT), KeyBERTVi implements a similar keyword extraction technique that leverages the embeddings of [PhoBERT](https://huggingface.co/vinai/phobert-base) and minimal linguistics properties to extract keywords and keyphrases that are most similar to the document.

<a name="toc"/></a>
## Table of Contents  
<!--ts-->  
   1. [About the Project](#about)  
   2. [Getting Started](#gettingstarted)  
        2.1. [Installation](#installation)  
        2.2. [Basic Usage](#usage)  
        2.3. [Diversify Results](#diversify)  
   3. [Limitations](#limitations)  
<!--te-->  

<a name="about"/></a>
## 1. About the Project

This implementation took inspiration from the simple yet intuitive and powerful method of [KeyBERT](https://github.com/MaartenGr/KeyBERT/), applied for the Vietnamese language. PhoBERT are used to generate both document-level embeddings and word-level embeddings for extracted N-grams. Cosine similarity is then used to compute which N-grams are most similar to the document-level embedding, thus can be perceived as most representative of the document. 
Preprocessing catered to the Vietnamese language was applied. 

<a name="gettingstarted"/></a>
## 2. Getting Started
<a name="installation"/></a>
###  2.1. Setting up

```bash
  git clone https://github.com/NguyenTuan-UET/KeyBert_VietNam.git
```

You can use existing pre-trained models in the repo or download your own and put them in `pretrained-models` folder. 

```python
  phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
  phobert.eval()
  torch.save(phobert, f'{dir_path}/pretrained-models/phobert.pt')
  
  ner_model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
  ner_model.eval()
  torch.save(ner_model, f'{dir_path}/pretrained-models/ner-vietnamese-electra-base.pt')
```

**Note:** `dir_path` is the absolute path to the repo. 

As [PhoBERT](https://huggingface.co/vinai/phobert-base) requires [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) as part of pre-processing, the folder `pretrained-models/vncorenlp` is required. To download your own: 
```bash
  pip install py_vncorenlp
```

```python
  import py_vncorenlp
  
  py_vncorenlp.download_model(save_dir=f'{dir_path}/pretrained-models/vncorenlp')
```

<a name="usage"/></a>
###  2.2. Basic Usage

```python
  phobert = torch.load(f'{dir_path}/pretrained-models/phobert.pt')
  phobert.eval()
  ner_model = torch.load(f'{dir_path}/pretrained-models/ner-vietnamese-electra-base.pt')
  ner_model.eval()
  kw_pipeline = KeywordExtractorPipeline(phobert, ner_model)
```

```python
  title = "Giới thiệu về UET"
  text = """
            Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội được thành lập 
            theo Quyết định số 92/2004/QĐ-TTg ngày 25/05/2004 của Thủ tướng Chính phủ 
            trên cơ sở Khoa Công nghệ và Trung tâm Hợp tác Đào tạo và Bồi dưỡng Cơ học trực thuộc Đại học Quốc gia Hà Nội với hai nhiệm vụ như sau:
            1. Đào tạo nguồn nhân lực trình độ đại học, sau đại học và bồi dưỡng nhân tài thuộc lĩnh vực khoa học, công nghệ;
            2. Nghiên cứu và triển khai ứng dụng khoa học, công nghệ đáp ứng nhu cầu phát triển kinh tế – xã hội.
            Sứ mạng của Nhà trường là đào tạo nguồn nhân lực chất lượng cao, trình độ cao và bồi dưỡng nhân tài; 
            nghiên cứu phát triển và ứng dụng các lĩnh vực khoa học công nghệ tiên tiến mũi nhọn trên cơ sở phát huy 
            thế mạnh về Công nghệ thông tin và Truyền thông. Nhà trường cũng đã xác định sứ mạng tiên phong tiếp cận 
            chuẩn mực giáo dục đại học khu vực và thế giới, ứng dụng công nghệ thông tin trong quản trị đại học đóng góp tích cực 
            vào sự phát triển nền kinh tế và xã hội tri thức của đất nước. Sứ mạng này hoàn toàn phù hợp và thống nhất với chủ trương, 
            giải pháp và các mục tiêu của Chương trình đổi mới toàn diện giáo dục đại học mà Đảng và Nhà nước đang triển khai thực hiện.
          """
  inp = {"title": title, "text": text}

  keywords = kw_pipeline(
          inputs=inp,
          min_freq=1,
          ngram_n=(1, 3),
          top_n=10,
          diversify_result=True
      )

  Named Entities list
  ['Khoa_Công nghệ', 'Trường Đại_học Công_nghệ', 'Đại_học Quốc_gia Hà_Nội', 'Trung_tâm Hợp_tác Đào_tạo và Bồi_dưỡng Cơ_học']
  
  Final ngram list
  ['Bồi_dưỡng Cơ_học trực_thuộc', 'Chương_trình đổi_mới', 'Công_nghệ_thông_tin', 'Cơ_học trực_thuộc Đại_học', 'Giới_thiệu', 'Nghiên_cứu', 'Nhà_nước', 'Nhà_trường', 'Quyết_định', 'Sứ_mạng', 'Thủ_tướng Chính_phủ', 'Trung_tâm Hợp_tác Đào_tạo và Bồi_dưỡng Cơ_học', 'Truyền_thông', 'Trường Đại_học Công_nghệ', 'bồi_dưỡng nhân_tài', 'chuẩn_mực giáo_dục đại_học', 'chủ_trương', 'công_nghệ đáp_ứng nhu_cầu', 'cơ_sở Khoa_Công nghệ', 'cơ_sở phát_huy', 'giáo_dục đại_học khu_vực', 'giải_pháp', 'lĩnh_vực khoa_học công_nghệ', 'mũi_nhọn', 'mục_tiêu', 'nghiên_cứu phát_triển', 'nhiệm_vụ', 'nhu_cầu phát_triển kinh_tế', 'nhân_lực chất_lượng', 'nhân_lực trình_độ đại_học', 'quản_trị đại_học đóng_góp', 'sau_đại_học', 'thành_lập', 'thế_giới', 'thống_nhất', 'tiếp_cận chuẩn_mực giáo_dục', 'triển_khai ứng_dụng khoa_học', 'trực_thuộc Đại_học Quốc_gia', 'xác_định sứ_mạng', 'xã_hội tri_thức', 'Đại_học Quốc_gia Hà_Nội', 'Đảng', 'đào_tạo', 'đáp_ứng nhu_cầu phát_triển', 'đất_nước', 'ứng_dụng công_nghệ_thông_tin']

  Keywords:
    - Trường Đại_học Công_nghệ: 0.8765
    - triển_khai ứng_dụng khoa_học: 0.8453
    - Giới_thiệu: 0.8207
    - nhu_cầu phát_triển kinh_tế: 0.8358
    - Trung_tâm Hợp_tác Đào_tạo và Bồi_dưỡng Cơ_học: 0.8000
    - Đảng: 0.8068
    - xã_hội tri_thức: 0.8392
    - chuẩn_mực giáo_dục đại_học: 0.8312
    - cơ_sở phát_huy: 0.7535
    - cơ_sở Khoa_Công nghệ: 0.8010
```

<a name="diversify"/></a>
###  2.3. Diversify Results

More information needed

<a name="limitations"/></a>
## 3. Limitations

More information needed

## References
1. https://github.com/MaartenGr/KeyBERT
2. https://github.com/VinAIResearch/PhoBERT
3. https://huggingface.co/NlpHUST/ner-vietnamese-electra-base
4. https://github.com/undertheseanlp/underthesea
5. https://github.com/vncorenlp/VnCoreNLP
