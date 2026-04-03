import os

class ImageValidator:

    SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff", ".tif", ".gif"}

    MIME_TYPES = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".bmp": "image/bmp",
        ".webp": "image/webp",
        ".tiff": "image/tiff",
        ".tif": "image/tiff",
        ".gif": "image/gif",
    }

    @staticmethod
    def sanitize_path(raw_input: str) -> str:
        path = raw_input.strip()

        if (path.startswith('"') and path.endswith('"')) or \
           (path.startswith("'") and path.endswith("'")):
            path = path[1:-1].strip()
        path = os.path.expanduser(path)
        path = os.path.normpath(path)
        path = os.path.abspath(path)

        return path

    @staticmethod
    def validate(path: str) -> tuple[bool, str]:
        if not path:
            return False, "Bạn chưa nhập đường dẫn. Hãy thử lại."

        if not os.path.exists(path):
            return False, f"Không tìm thấy file '{path}'. Hãy kiểm tra lại đường dẫn."

        if os.path.isdir(path):
            return False, f"'{path}' là thư mục, không phải file ảnh."

        _, ext = os.path.splitext(path)
        ext = ext.lower()
        if ext not in ImageValidator.SUPPORTED_EXTENSIONS:
            supported = ", ".join(sorted(ImageValidator.SUPPORTED_EXTENSIONS))
            return False, f"Đuôi file '{ext}' không được hỗ trợ. Các định dạng hợp lệ: {supported}"

        if os.path.getsize(path) == 0:
            return False, f"File '{path}' bị rỗng (0 byte). Hãy chọn file ảnh khác."

        if not os.access(path, os.R_OK):
            return False, f"Không có quyền đọc file '{path}'. Hãy kiểm tra quyền truy cập."

        return True, path

    @staticmethod
    def get_mime_type(path: str) -> str:
        _, ext = os.path.splitext(path)
        return ImageValidator.MIME_TYPES.get(ext.lower(), "image/jpeg")
