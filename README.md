# Python BMI Calculator

A simple, lightweight, and user-friendly Command Line Interface (CLI) application written in Python to calculate Body Mass Index (BMI).

---

## Repository Details
* **Suggested Repository Title:** `python-bmi-calculator`
* **Suggested Description:** A Python CLI tool to calculate Body Mass Index (BMI) with detailed health classifications and mathematical formulas.

---

## What is BMI?
Body Mass Index (BMI) is a value derived from the mass (weight) and height of a person. It is widely used as a general rule of thumb to estimate whether a person has a healthy body weight for their height. The BMI value allows categorization into underweight, normal weight, overweight, or obesity.

## The Formula
The BMI is calculated using weight in kilograms (kg) divided by the square of height in meters ($m$):

$$\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}$$

For the imperial system (pounds and inches), the formula is multiplied by a conversion factor of $703$:

$$\text{BMI} = \frac{\text{weight (lbs)}}{\text{height (in)}^2} \times 703$$

## Standard Health Categories
* **Underweight:** BMI less than $18.5$
* **Normal weight:** BMI between $18.5$ and $24.9$
* **Overweight:** BMI between $25.0$ and $29.9$
* **Obesity:** BMI $30.0$ or greater

## Features
* Quick calculations based on user input for weight and height.
* Automatic classification into standard WHO health categories.
* Clean and straightforward Python code, ideal for beginners.

## Prerequisites
Ensure you have Python installed on your system. You can verify the installation by running:
```bash
python --version
