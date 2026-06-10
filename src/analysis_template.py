"""商业分析基础模板。"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def load_data(file_name: str) -> pd.DataFrame:
    """读取原始 CSV 数据。"""
    file_path = RAW_DATA_DIR / file_name
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """执行基础清洗，具体规则应按业务口径调整。"""
    return df.drop_duplicates().copy()


def main() -> None:
    """分析流程入口。"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"项目目录：{PROJECT_ROOT}")
    print("请在 main() 中添加数据读取、清洗和分析逻辑。")


if __name__ == "__main__":
    main()
