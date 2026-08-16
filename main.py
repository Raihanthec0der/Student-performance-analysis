"""
Student Performance Analysis
----------------------------
Exploratory data analysis of student academic performance.

Expected dataset:
    data/student_data.csv

Run from the project root:
    python src/main.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "student_data.csv"
VISUALIZATION_DIR = BASE_DIR / "visualizations"

VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Data loading and validation
# ---------------------------------------------------------------------------

REQUIRED_COLUMNS = {
    "school", "sex", "age", "address", "famsize", "Pstatus",
    "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
    "traveltime", "studytime", "failures", "schoolsup", "famsup",
    "paid", "activities", "nursery", "higher", "internet",
    "romantic", "famrel", "freetime", "goout", "Dalc", "Walc",
    "health", "absences", "G1", "G2", "G3",
}


def load_data() -> pd.DataFrame:
    """Load and validate the student dataset."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Place student_data.csv inside the data/ folder."
        )

    data = pd.read_csv(DATA_FILE)

    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(
            "Dataset is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    return data


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def print_dataset_overview(df: pd.DataFrame) -> None:
    """Print basic data-quality and structure information."""
    print("\n===== DATASET OVERVIEW =====")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())


def run_analysis(df: pd.DataFrame) -> None:
    """Print the project's key exploratory analysis results."""
    average_g3 = df["G3"].mean()
    g3_counts = df["G3"].value_counts()

    print("\n===== FINAL GRADE ANALYSIS =====")
    print(f"Average G3: {average_g3:.2f}")
    print("\nG3 Distribution:")
    print(g3_counts)
    print(f"\nMost Common G3: {g3_counts.idxmax()}")
    print(f"Number of Students: {g3_counts.max()}")
    print(f"Students with G3 = 20: {(df['G3'] == 20).sum()}")

    studytime_g3 = df.groupby("studytime")["G3"].mean()
    failure_g3 = df.groupby("failures")["G3"].mean()
    gender_g3 = df.groupby("sex")["G3"].mean()
    address_g3 = df.groupby("address")["G3"].mean()
    mother_education_g3 = df.groupby("Medu")["G3"].mean()
    father_education_g3 = df.groupby("Fedu")["G3"].mean()
    grade_correlation = df[["G1", "G2", "G3"]].corr()

    print("\n===== STUDY TIME VS G3 =====")
    print(studytime_g3)

    print("\n===== ABSENCES VS G3 =====")
    print(f"Correlation: {df['absences'].corr(df['G3']):.6f}")

    print("\n===== PREVIOUS FAILURES VS G3 =====")
    print(failure_g3)

    print("\n===== GENDER VS G3 =====")
    print(gender_g3)

    print("\n===== ADDRESS VS G3 =====")
    print(address_g3)

    print("\n===== MOTHER'S EDUCATION VS G3 =====")
    print(mother_education_g3)

    print("\n===== FATHER'S EDUCATION VS G3 =====")
    print(father_education_g3)

    print("\n===== G1, G2, G3 CORRELATION =====")
    print(grade_correlation)


# ---------------------------------------------------------------------------
# Visualization helpers
# ---------------------------------------------------------------------------

def save_bar_chart(
    series: pd.Series,
    title: str,
    xlabel: str,
    filename: str,
) -> None:
    """Create and save a labeled bar chart."""
    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(series.index.astype(str), series.values)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Average G3")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.10,
            f"{height:.2f}",
            ha="center",
            va="bottom",
        )

    fig.tight_layout()
    fig.savefig(
        VISUALIZATION_DIR / filename,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)


def save_correlation_heatmap(correlation: pd.DataFrame) -> None:
    """Create and save the G1/G2/G3 correlation heatmap."""
    fig, ax = plt.subplots(figsize=(7, 5))

    image = ax.imshow(correlation, cmap="coolwarm")
    fig.colorbar(image, ax=ax, label="Correlation")

    ax.set_xticks(range(len(correlation.columns)))
    ax.set_xticklabels(correlation.columns)
    ax.set_yticks(range(len(correlation.index)))
    ax.set_yticklabels(correlation.index)

    ax.set_title("Correlation Between G1, G2 and G3")

    for i in range(len(correlation)):
        for j in range(len(correlation.columns)):
            ax.text(
                j,
                i,
                f"{correlation.iloc[i, j]:.2f}",
                ha="center",
                va="center",
            )

    fig.tight_layout()
    fig.savefig(
        VISUALIZATION_DIR / "grade_correlation.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)


def create_visualizations(df: pd.DataFrame) -> None:
    """Generate and save the project's main visualizations."""
    studytime_g3 = df.groupby("studytime")["G3"].mean()
    failure_g3 = df.groupby("failures")["G3"].mean()
    gender_g3 = df.groupby("sex")["G3"].mean()
    address_g3 = df.groupby("address")["G3"].mean()
    mother_education_g3 = df.groupby("Medu")["G3"].mean()
    father_education_g3 = df.groupby("Fedu")["G3"].mean()
    grade_correlation = df[["G1", "G2", "G3"]].corr()

    save_bar_chart(
        failure_g3,
        "Previous Failures vs Average Final Grade",
        "Previous Failures",
        "failures_vs_g3.png",
    )

    save_bar_chart(
        studytime_g3,
        "Study Time vs Average Final Grade",
        "Study Time Level",
        "studytime_vs_g3.png",
    )

    save_bar_chart(
        gender_g3,
        "Gender vs Average Final Grade",
        "Gender",
        "gender_vs_g3.png",
    )

    save_bar_chart(
        address_g3,
        "Address Type vs Average Final Grade",
        "Address Type",
        "address_vs_g3.png",
    )

    save_bar_chart(
        mother_education_g3,
        "Mother's Education vs Average Final Grade",
        "Mother's Education Level (Medu)",
        "mothers_education_vs_g3.png",
    )

    save_bar_chart(
        father_education_g3,
        "Father's Education vs Average Final Grade",
        "Father's Education Level (Fedu)",
        "fathers_education_vs_g3.png",
    )

    save_correlation_heatmap(grade_correlation)

    print(
        f"\nVisualization files saved to: {VISUALIZATION_DIR}"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Run the complete analysis pipeline."""
    df = load_data()
    print_dataset_overview(df)
    run_analysis(df)
    create_visualizations(df)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
