# LANA - Visual Motion Video Generator     
  
**LANA** (Language-Assisted Narrative Animation) is a powerful tool for generating cinematic visual motion videos from text descriptions. It creates optimized prompts and configuration files for use with AI video generation platforms.
  
## Features

-  Generate optimized video prompts from text descriptions
-  Support for detailed scene configurations
-  Automatic metadata generation
-  Cinematic quality specifications 
-  Cultural authenticity support
-  Flexible configuration system

## Installation

1. Clone this repository:
```bash 
git clone https://github.com/alinapradhan/LANA-.git
cd LANA-
```

2. No external dependencies required! The tool uses only Python standard library.

3. Run the generator:
```bash
python3 generate_video.py --config scenes/kazakh_scene.json
```

## Usage

### Generate from Configuration File

Use a pre-configured scene (like the included Kazakh traditional meal scene):

```bash
python generate_video.py --config scenes/kazakh_scene.json --output ./kazakh_video
```

### Generate from Direct Prompt

Provide your own scene description:

```bash
python generate_video.py --prompt "A serene mountain landscape at sunset" --output ./mountain_scene
```

### Command Line Options

- `--config PATH`: Path to JSON configuration file with scene description
- `--prompt TEXT`: Direct text prompt for video generation
- `--output PATH`: Output directory for generated files (default: `output`)

## Example Scene: Traditional Kazakh Family Meal

The repository includes a pre-configured scene showcasing:
- Traditional Kazakh yurt on the steppes
- Family gathering around beshbarmak and kymyz
- Golden hour lighting and cinematic slow motion
- Cultural authenticity and attention to detail

Run it with:
```bash
python generate_video.py --config scenes/kazakh_scene.json
```

## Output Files

After running the generator, you'll find:

- `generation_prompt.txt`: Optimized prompt for AI video platforms
- `metadata.json`: Technical specifications and scene details
- `README.md`: Instructions for next steps

## Video Generation Platforms

Use the generated prompts with these platforms:

1. **OpenAI Sora** (when available) - High-quality AI video generation
2. **Runway Gen-2** - https://runwayml.com/
3. **Pika Labs** - https://pika.art/
4. **Stable Video Diffusion** - Open-source option
5. **Other AI video generation services**

## Configuration Format

Create custom scenes using JSON:

```json
{
  "scene_name": "Your Scene Name",
  "scene_description": "Detailed description of your scene...",
  "technical_requirements": {
    "resolution": "1920x1080",
    "frame_rate": 30,
    "duration_seconds": 60
  },
  "key_visual_elements": [
    "Element 1",
    "Element 2"
  ]
}
```

## Project Structure

```
LANA-/
├── generate_video.py      # Main video generation script
├── requirements.txt       # Python dependencies
├── scenes/               # Scene configuration files
│   └── kazakh_scene.json # Example Kazakh traditional scene
├── output/               # Generated output files (created on run)
├── README.md            # This file
└── LICENSE              # MIT License
```

## Technical Specifications

Default video specifications:
- **Resolution**: 1920x1080 (Full HD)
- **Frame Rate**: 30 fps
- **Duration**: 30-60 seconds
- **Format**: MP4 with H.264 codec
- **Style**: Cinematic with slow motion
- **Lighting**: Natural, context-appropriate

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for culturally authentic visual storytelling
- Built to support AI video generation workflows
- Designed for cinematic quality output


