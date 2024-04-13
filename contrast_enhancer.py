from PIL import Image, ImageEnhance

# Load the image
image_path = 'low_contrast.jpg'
image = Image.open(image_path)

# Enhance the contrast
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(4)  # Increase contrast

# Save the enhanced image
enhanced_image_path = 'enhanced_contrast.jpg'
enhanced_image.save(enhanced_image_path)
