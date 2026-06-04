# Color Analysis Tool

A simple Python-based prototype that analyzes an image at the pixel level and generates a percentage breakdown of colors grouped into 11 predefined color categories.

## Problem Statement

The tool accepts an image as input, analyzes all pixels, maps each pixel to one of the predefined color categories, and generates a color distribution chart showing the percentage contribution of each color.

### Supported Color Categories

* White
* Black
* Gray
* Red
* Green
* Blue
* Yellow
* Orange
* Brown
* Purple
* Pink

Examples:

* Light Yellow → Yellow
* Navy Blue → Blue
* Burgundy → Red
* Dark Orange → Brown

---

## Features

* Pixel-level image analysis
* RGB to HSV color conversion
* Intelligent color grouping
* Percentage calculation for each color category
* Automatic pie chart generation
* CSV export of analysis results
* Batch processing of multiple images

---

## Project Structure

```text
color-analyzer/
│
├── images/
│   ├── TestImage1.jpg
│   ├── TestImage2.jpg
│   ├── TestImage3.jpg
│   └── TestImage4.jpg
│
├── color_analyzer.py
├── requirements.txt
├── color_analysis_results.csv
└── README.md
```

---

## Installation

### 1. Clone or Download Project

```bash
git clone <repository-url>
cd color-analyzer
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
```

Activate:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pillow numpy pandas matplotlib
```

---

## How It Works

### Step 1: Load Image

The image is loaded into memory using Pillow.

### Step 2: Convert RGB to HSV

HSV (Hue, Saturation, Value) color space is used because:

* Hue represents the actual color
* Saturation measures color intensity
* Value represents brightness

HSV makes color classification more reliable than RGB.

### Step 3: Color Classification

Each pixel is assigned to one of the predefined color categories using HSV thresholds.

Example:

| Hue Range | Color  |
| --------- | ------ |
| 0–15     | Red    |
| 15–40    | Orange |
| 40–65    | Yellow |
| 65–170   | Green  |
| 170–260  | Blue   |
| 260–290  | Purple |
| 290–345  | Pink   |

Special rules:

* Very low brightness → Black
* Low saturation + high brightness → White
* Low saturation → Gray
* Dark orange shades → Brown

### Step 4: Percentage Calculation

For each color category:

```text
Percentage =
(Color Pixels / Total Pixels) × 100
```

### Step 5: Visualization

A pie chart is generated showing the color distribution.

---

## Running the Application

Place all test images inside the `images` folder.

Run:

```bash
python3 color_analyzer.py
```

---

## Output

For each image:

### Generated Files

```text
TestImage1_chart.png
TestImage2_chart.png
TestImage3_chart.png
TestImage4_chart.png
```

### CSV Summary

```text
color_analysis_results.csv
```

Example:

| Image      | Red  | Green | Blue | Yellow |
| ---------- | ---- | ----- | ---- | ------ |
| TestImage1 | 12.4 | 23.1  | 4.8  | 18.9   |
| TestImage2 | 6.3  | 14.7  | 35.2 | 7.4    |

---

## Assumptions

* Every pixel belongs to exactly one color category.
* Similar shades are grouped into the closest primary color.
* Percentages may vary slightly due to HSV threshold definitions.
* Total percentages will approximately sum to 100%.

---

## Future Improvements

For a production-scale implementation:

1. K-Means Color Clustering
   * Extract dominant colors before classification
   * Reduce pixel noise
2. Custom Color Profiles
   * Allow users to define categories
3. Interactive Dashboard
   * Upload images through a web interface
4. Batch Upload Support
   * Process multiple images simultaneously
5. API Integration
   * Expose analysis functionality through REST APIs

---

## Tech Stack

* Python 3.x
* Pillow
* NumPy
* Pandas
* Matplotlib
