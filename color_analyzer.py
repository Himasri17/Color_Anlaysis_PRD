import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# -------------------------------------------------
# HSV COLOR MAPPING
# -------------------------------------------------

def classify_color(h, s, v):
    """
    h: 0-179
    s: 0-255
    v: 0-255
    """

    # Black
    if v < 40:
        return "Black"

    # White
    if s < 30 and v > 220:
        return "White"

    # Gray
    if s < 40:
        return "Gray"

    hue = h * 2  # Convert OpenCV hue to 0-360

    # Red
    if hue >= 345 or hue < 15:
        return "Red"

    # Orange
    if 15 <= hue < 40:
        return "Orange"

    # Yellow
    if 40 <= hue < 65:
        return "Yellow"

    # Green
    if 65 <= hue < 170:
        return "Green"

    # Blue
    if 170 <= hue < 260:
        return "Blue"

    # Purple
    if 260 <= hue < 290:
        return "Purple"

    # Pink
    if 290 <= hue < 345:
        return "Pink"

    return "Red"


# -------------------------------------------------
# BROWN HANDLING
# -------------------------------------------------

def detect_brown(h, s, v):
    hue = h * 2

    return (
        10 <= hue <= 35
        and s > 80
        and 40 < v < 180
    )


# -------------------------------------------------
# ANALYSIS
# -------------------------------------------------

def analyze_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    pixels = hsv.reshape(-1, 3)

    colors = []

    for h, s, v in pixels:

        if detect_brown(h, s, v):
            colors.append("Brown")
        else:
            colors.append(classify_color(h, s, v))

    counts = Counter(colors)

    total_pixels = len(colors)

    percentages = {
        color: round((count / total_pixels) * 100, 2)
        for color, count in counts.items()
    }

    return percentages


# -------------------------------------------------
# PIE CHART
# -------------------------------------------------

def create_chart(percentages, image_name):

    labels = list(percentages.keys())
    sizes = list(percentages.values())

    plt.figure(figsize=(8, 8))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(f"Color Distribution - {image_name}")

    output_file = f"{image_name}_chart.png"

    plt.savefig(output_file, bbox_inches="tight")

    plt.close()

    print(f"Saved chart: {output_file}")


# -------------------------------------------------
# MAIN
# -------------------------------------------------

if __name__ == "__main__":

    image_files = [
        "images/TestImage1.jpg",
        "images/TestImage2.jpg",
        "images/TestImage3.jpg",
        "images/TestImage4.jpg"
    ]

    all_results = []

    for image_path in image_files:

        image_name = image_path.split("/")[-1].split(".")[0]

        print(f"\nAnalyzing {image_name}...")

        percentages = analyze_image(image_path)

        create_chart(percentages, image_name)

        df = pd.DataFrame(
            percentages.items(),
            columns=["Color", "Percentage"]
        )

        print(df)

        all_results.append({
            "Image": image_name,
            **percentages
        })

    summary = pd.DataFrame(all_results)

    summary.to_csv(
        "color_analysis_results.csv",
        index=False
    )

    print("\nSaved color_analysis_results.csv")