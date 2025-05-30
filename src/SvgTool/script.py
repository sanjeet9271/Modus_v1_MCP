import base64
import os
import re
from PIL import Image
import io
import textwrap
import argparse

def create_side_by_side_svg(image_path, text, output_path="output.svg", 
                           svg_width=4193, svg_height=800,  # Increased default height
                           text_size=180, text_color="white",  # Increased default text size
                           text_x=500, text_width=35):  # Adjusted text position and width
    """
    Create an SVG with an image and text side by side.
    """
    # Check if file is an SVG
    is_svg = image_path.lower().endswith('.svg')
    
    if is_svg:
        try:
            # For SVG files, just read the content directly
            with open(image_path, 'r', encoding='utf-8') as svg_file:
                svg_content = svg_file.read()
                
                # Try to extract width and height from SVG
                width_match = re.search(r'width="(\d+)', svg_content)
                height_match = re.search(r'height="(\d+)', svg_content)
                
                img_width = int(width_match.group(1)) if width_match else 300
                img_height = int(height_match.group(1)) if height_match else 300
                
                # Calculate scaling to fit full height while maintaining aspect ratio
                scale_factor = svg_height / img_height
                new_img_width = int(img_width * scale_factor)
                
                # Encode SVG to base64
                svg_bytes = svg_content.encode('utf-8')
                img_base64 = base64.b64encode(svg_bytes).decode('utf-8')
                img_format = 'svg+xml'  # Correct MIME type for SVG
                
        except Exception as e:
            print(f"Error processing SVG: {e}")
            return False
    else:
        # Original code for raster images
        try:
            with Image.open(image_path) as img:
                img_width, img_height = img.size
                img_format = img.format.lower()
                
                # Calculate scaling to fit full height while maintaining aspect ratio
                scale_factor = svg_height / img_height
                new_img_width = int(img_width * scale_factor)
                
                # Resize image if needed
                if scale_factor != 1:
                    img = img.resize((new_img_width, svg_height), Image.LANCZOS)
                
                # Convert image to base64
                buffer = io.BytesIO()
                img.save(buffer, format=img.format)
                img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                
        except Exception as e:
            print(f"Error processing image: {e}")
            return False
      # Wrap text for better display
    wrapped_text = textwrap.fill(text, width=text_width)
    
    # Replace newlines with SVG line breaks
    formatted_text = wrapped_text.replace('\n', f'<tspan x="{text_x}" dy="1.2em">')      # Create SVG content
    svg_content = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- No background rectangle -->
        
        <!-- Image - full height -->
        <image x="10" y="0" width="{new_img_width}" height="{svg_height}" 
               xlink:href="data:image/{img_format};base64,{img_base64}" />
          <!-- Text - centered vertically -->        
          <text x="{new_img_width + 50}" y="{svg_height/2}" font-family="Arial, Helvetica, sans-serif" font-size="{text_size}" fill="{text_color}" font-weight="400" letter-spacing="1.5px" dominant-baseline="middle">
            {formatted_text}
        </text>
    </svg>
    """
    
    # Save SVG to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"SVG created successfully at {output_path}")
        return True
    except Exception as e:
        print(f"Error saving SVG: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an SVG with an image and text side by side.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("text", help="Text to display next to the image")    
    parser.add_argument("-o", "--output", default="output.svg", help="Output SVG file name")
    parser.add_argument("-w", "--width", type=int, default=4193, help="SVG width")
    parser.add_argument("-H", "--height", type=int, default=800, help="SVG height")    
    parser.add_argument("--text-size", type=int, default=180, help="Font size for text")
    parser.add_argument("--text-color", default="white", help="Color for text")
    parser.add_argument("--text-x", type=int, default=500, help="X position for text")
    parser.add_argument("--text-width", type=int, default=35, help="Characters per line for text wrapping")
    
    args = parser.parse_args()
    
    create_side_by_side_svg(
    args.image_path, 
    args.text, 
    args.output,
    args.width, 
    args.height,
    args.text_size, 
    args.text_color, 
    args.text_x, 
    args.text_width
)