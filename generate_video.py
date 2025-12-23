#!/usr/bin/env python3
"""
LANA - Visual Motion Video Generator
Generates cinematic video content from text descriptions using AI.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class VideoGenerator:
    """Main class for generating visual motion videos from text descriptions."""
    
    def __init__(self, config_path: str = None):
        """
        Initialize the video generator.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config = self._load_config(config_path) if config_path else {}
        self.api_key = os.getenv('OPENAI_API_KEY')
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Configuration file not found at {config_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in configuration file: {e}")
            return {}
    
    def generate_video_prompt(self, scene_description: str) -> str:
        """
        Generate an optimized video prompt from scene description.
        
        Args:
            scene_description: The text description of the scene
            
        Returns:
            Optimized prompt for video generation
        """
        # Enhance the prompt with video-specific instructions
        video_prompt = f"""Generate a cinematic visual motion video with the following specifications:

Scene Description:
{scene_description}

Technical Requirements:
- Resolution: 1920x1080 (Full HD)
- Frame Rate: 30 fps
- Duration: 30-60 seconds
- Camera Movement: Smooth cinematic pans and slow zooms
- Lighting: Natural golden hour lighting with soft shadows
- Motion: Slow motion capture (120fps source for 30fps output)
- Focus: Sharp foreground, slightly soft background for depth
- Color Grading: Warm, inviting tones with golden highlights
- Audio: Ambient sounds (crackling fire, gentle wind, distant nature)

Style:
- Cinematographic approach
- Documentary-style realism
- Attention to cultural authenticity
- Emphasis on details and textures
"""
        return video_prompt
    
    def generate_video(self, prompt: str, output_path: str = "output") -> Dict[str, Any]:
        """
        Generate video from text prompt.
        
        Args:
            prompt: The text description for video generation
            output_path: Directory to save the generated video
            
        Returns:
            Dictionary containing generation results and metadata
        """
        print("=" * 80)
        print("LANA - Visual Motion Video Generator")
        print("=" * 80)
        print("\nGenerating video from prompt...")
        print(f"\nPrompt length: {len(prompt)} characters")
        print(f"Output directory: {output_path}")
        
        # Create output directory if it doesn't exist
        Path(output_path).mkdir(parents=True, exist_ok=True)
        
        # Generate optimized prompt
        optimized_prompt = self.generate_video_prompt(prompt)
        
        # Save the prompt to a file for reference
        prompt_file = Path(output_path) / "generation_prompt.txt"
        with open(prompt_file, 'w') as f:
            f.write(optimized_prompt)
        
        print(f"\n✓ Generated prompt saved to: {prompt_file}")
        
        # Create a metadata file
        metadata = {
            "original_prompt": prompt,
            "optimized_prompt": optimized_prompt,
            "output_path": output_path,
            "status": "ready_for_generation",
            "technical_specs": {
                "resolution": "1920x1080",
                "fps": 30,
                "duration_seconds": "30-60",
                "format": "MP4",
                "codec": "H.264"
            },
            "notes": [
                "This system prepares video generation prompts for AI video generation services",
                "To generate the actual video, use services like:",
                "  - OpenAI's Sora (when available)",
                "  - Runway Gen-2",
                "  - Stability AI's Stable Video Diffusion",
                "  - Pika Labs",
                "  - Other AI video generation platforms"
            ]
        }
        
        metadata_file = Path(output_path) / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, indent=2, fp=f)
        
        print(f"✓ Metadata saved to: {metadata_file}")
        
        # Create a README with instructions
        readme_content = """# Video Generation Output

## Files Generated

- `generation_prompt.txt`: Optimized prompt for video generation services
- `metadata.json`: Technical specifications and metadata
- `README.md`: This file

## Next Steps

To generate the actual video, you can use the prompt in `generation_prompt.txt` with:

### Option 1: OpenAI Sora (when available)
```bash
# Use OpenAI's video generation API
# API coming soon
```

### Option 2: Runway Gen-2
1. Visit https://runwayml.com/
2. Sign up for an account
3. Use the "Gen-2" video generation tool
4. Paste the prompt from `generation_prompt.txt`
5. Adjust duration and settings as needed
6. Generate and download your video

### Option 3: Stable Video Diffusion
```bash
# Install Stable Video Diffusion
pip install diffusers transformers accelerate

# Use the prompt to generate video frames
# Then compile into video format
```

### Option 4: Pika Labs
1. Visit https://pika.art/
2. Create an account
3. Paste the prompt
4. Generate your cinematic video

## Technical Specifications

See `metadata.json` for complete technical specifications including:
- Resolution: 1920x1080
- Frame Rate: 30 fps
- Recommended Duration: 30-60 seconds
- Format: MP4 with H.264 codec

## Tips for Best Results

1. Use the prompt as a starting point and adjust based on the platform
2. Consider breaking long prompts into segments for some platforms
3. Adjust technical parameters based on platform capabilities
4. Review and iterate on the output
"""
        
        readme_file = Path(output_path) / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        print(f"✓ Instructions saved to: {readme_file}")
        print("\n" + "=" * 80)
        print("✓ Video generation preparation complete!")
        print("=" * 80)
        print(f"\nOutput files created in: {output_path}/")
        print("\nNext steps:")
        print("1. Review the generated prompt in generation_prompt.txt")
        print("2. Choose a video generation platform (see README.md)")
        print("3. Use the prompt to generate your cinematic video")
        print("\n" + "=" * 80)
        
        return metadata


def main():
    """Main entry point for the video generator."""
    parser = argparse.ArgumentParser(
        description='LANA - Generate visual motion videos from text descriptions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_video.py --config scenes/kazakh_scene.json
  python generate_video.py --prompt "A beautiful sunset scene" --output ./my_video
  python generate_video.py --config scenes/kazakh_scene.json --output ./kazakh_video
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        help='Path to JSON configuration file with scene description'
    )
    
    parser.add_argument(
        '--prompt',
        type=str,
        help='Direct text prompt for video generation'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='Output directory for generated files (default: output)'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.config and not args.prompt:
        parser.error("Either --config or --prompt must be provided")
    
    # Initialize generator
    generator = VideoGenerator(config_path=args.config)
    
    # Get the prompt
    if args.config:
        prompt = generator.config.get('scene_description', '')
        if not prompt:
            print("Error: No 'scene_description' found in config file")
            sys.exit(1)
    else:
        prompt = args.prompt
    
    # Generate video preparation files
    try:
        result = generator.generate_video(prompt, args.output)
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
