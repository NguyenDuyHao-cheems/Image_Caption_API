
## 📋 Thông tin sinh viên

| Thông tin | Chi tiết |
|-----------|----------|
| **Họ tên** | Nguyễn Duy Hào |
| **MSSV** | 24120306 |
| **Lớp** | 24CTT5 |
| **Môn học** | Tư Duy Tính Toán |

---

## 🧠 Mô hình AI

- **Tên mô hình:** Salesforce/blip-vqa-base
- **Hugging Face:** [https://huggingface.co/Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base)

---

## 📝 Mô tả

Hệ thống cho phép người dùng **gửi ảnh kèm câu hỏi**, mô hình AI sẽ phân tích ảnh và trả lời câu hỏi bằng ngôn ngữ tự nhiên (Visual Question Answering). Có thể để trống phần câu hỏi. Mô hình hiện tại chỉ hỗ trợ tiếng **Anh**.

**Ví dụ:** Gửi ảnh một con mèo + câu hỏi "What animal is this?" → AI trả lời "cat".

Hệ thống gồm 3 thành phần:

| Thành phần | Mô tả |
|------------|--------|
| **Server (Colab)** | Chạy model AI trên Google Colab, expose API qua Cloudflare Tunnel |
| **Client CLI** | Ứng dụng dòng lệnh Python để gọi API |
| **Web UI** | Giao diện web đơn giản gọi API từ trình duyệt |

---

## 📁 Cấu trúc dự án

```
Image_Caption_API/
├── client/                  # Module client
│   ├── __init__.py
│   ├── config.py            # Quản lý biến môi trường
│   ├── api.py               # HTTP client gọi server AI
│   ├── validators.py        # Kiểm tra đường dẫn & định dạng ảnh
│   └── cli_app.py           # Giao diện dòng lệnh (CLI)
├── notebooks/
│   └── run_model_image_vqa.ipynb  # Notebook chạy server trên Colab
├── web/
│   └── index.html           # Giao diện web
├── cli.py                   # Entry point chạy CLI
├── test_model.py            # Script test nhanh các endpoint
├── .env.example             # Template biến môi trường
├── requirements.txt         # Danh sách thư viện Python
└── README.md
```

---

## ⚙️ Hướng dẫn cài đặt

### 1. Clone dự án

```bash
git clone https://github.com/NguyenDuyHao-cheems/Image_Caption_API.git
cd Image_Caption_API
```

### 2. Tạo môi trường ảo

```bash
python -m venv .venv
```

Kích hoạt:

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Cài thư viện

```bash
pip install -r requirements.txt
```

### 4. Cấu hình biến môi trường

```bash
cp .env.example .env
```

Mở file `.env` và thay URL bằng địa chỉ server đang chạy:

```env
API_URL=https://your-server-url.trycloudflare.com
```

> **Lưu ý:** URL này lấy từ output khi chạy notebook trên Google Colab (xem bước tiếp theo).

---

## 🚀 Hướng dẫn chạy

### Bước 1: Khởi động server AI trên Google Colab

1. Mở file `notebooks/run_model_image_vqa.ipynb` trên [Google Colab](https://colab.research.google.com/)
2. Chạy tất cả các cell
3. Copy URL Cloudflare Tunnel được tạo ra (dạng `https://xxx.trycloudflare.com`)
4. Dán URL vào file `.env`

### Bước 2: Chạy Client

**Cách 1 — CLI tương tác:**

```bash
python cli.py
```

Chương trình sẽ hỏi bạn nhập đường dẫn ảnh và câu hỏi, sau đó trả kết quả từ AI.

**Cách 2 — Test nhanh:**

```bash
python test_model.py
```

Tự động test 3 endpoint: `/`, `/health`, `/predict`.

**Cách 3 — Web UI:**

Mở file `web/index.html` trên trình duyệt, thay URL API trong code JavaScript, sau đó upload ảnh và đặt câu hỏi.

---

## 📡 Hướng dẫn gọi API

Server cung cấp 3 endpoint:

### GET `/` — Kiểm tra server

```bash
curl https://your-server-url.trycloudflare.com/
```

Response:

```json
{"message": "API có khả năng đọc và trả lời các câu hỏi liên quan đến ảnh đầu vào"}
```

### GET `/health` — Kiểm tra sức khỏe

```bash
curl https://your-server-url.trycloudflare.com/health
```

Response:

```json
{"status": "Hệ thống hoạt động bình thường"}
```

### POST `/predict` — Hỏi AI về ảnh
#### Parameters

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | `File` | Yes | Hỗ trợ định dạng: JPG, PNG, WebP). |
| `query` | `String` | Yes | Câu hỏi muốn hỏi về bức ảnh. |
Gửi ảnh kèm câu hỏi:

```bash
curl -X POST https://your-server-url.trycloudflare.com/predict \
  -F "file=@/path/to/your/test_image.jpg" \
  -F "query=What color is the shirt?"
```

Response:

```json
{"answer": "blue"}
```

### Ví dụ gọi bằng Python

```python
import requests

url = "https://your-server-url.trycloudflare.com/predict"

with open("test_image.jpg", "rb") as f:
    response = requests.post(
        url,
        files={"file": ("test_image.jpg", f, "image/jpeg")},
        data={"query": "What is in this image?"}
    )

print(response.json())
# {"answer": "a cat sitting on a couch"}
```
