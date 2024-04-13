from PIL import Image
import matplotlib.pyplot as plt

# Load an image
image_path = 'lemon.jpg'  # Update this to the path of your image
image = Image.open(image_path)

# Convert the image to grayscale
gray_image = image.convert('L')

# Calculate the histogram
histogram = gray_image.histogram()

# Set a style for the plot
plt.style.use('ggplot')

# Plot the histogram with enhancements
plt.figure(figsize=(10,7))
plt.title("Luminance Histogram")
plt.xlabel("Pixel value")
plt.ylabel("Frequency")

# Customizing the plot with a different line color and width
plt.plot(histogram, color='blue', linewidth=1.5)

# Adding grid lines for better readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.show()
