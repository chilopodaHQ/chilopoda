# Kombi
[![Build Status](https://travis-ci.org/kombiHQ/kombi.svg?branch=master)](https://travis-ci.org/kombiHQ/kombi)

<p align="center">
    <img src="data/ui/icons/kombi.png" with="256" height="256"/>
</p>

Kombi is focused in processing data across different applications and libraries.

Such as image/video processing, ingestion of files, versioning data, (etc). Where these processes may look simple at first glance they may grow in complexity overtime, becoming hard to maintain specially when different applications/libraries are involved to accomplish the goal.

This is done by providing an API that simplifies the process of grabbing whether a partial or full data generated as output of a task (application/library) and use them subsequently as input of sub tasks, and so on.

In order to avoid writing boilerplate code, Kombi provides high-level declarative definitions that can be expressed through:

<details open="1"><summary>YAML</summary>
<p>


```yaml
---
vars:
  prefix: "/tmp"
tasks:
- run: gafferScene
  metadata:
    match.types:
    - png
    match.vars:
      imageType:
      - sequence
  options:
    scene: "{configDirectory}/scene.gfr"
  target: "{prefix}/gafferBlurImageSequence/(newver <parent> as <ver>)/{name}_<ver>.(pad {frame} 6).exr"
  tasks:
  - run: ffmpeg
    options:
      frameRate: 23.976
      sourceColorSpace: bt709
      targetColorSpace: smpte170m
    target: "(dirname {filePath})/{name}.mov"
```
</p>
</details>

<details><summary>TOML</summary>
<p>

```toml
[vars]
prefix = "/tmp"

[[tasks]]
run = "gafferScene"
target = "{prefix}/gafferBlurImageSequence/(newver <parent> as <ver>)/{name}_<ver>.(pad {frame} 6).exr"

  [tasks.metadata]
  "match.types" = [
    "png"
  ]

    [tasks.metadata."match.vars"]
    imageType = [
      "sequence"
    ]

  [tasks.options]
  scene = "{configDirectory}/scene.gfr"

  [[tasks.tasks]]
  run = "ffmpeg"
  target = "(dirname {filePath})/{name}.mov"

    [tasks.tasks.options]
    frameRate = 23.976
    sourceColorSpace = "bt709"
    targetColorSpace = "smpte170m"
```
</details>

<details><summary>JSON</summary>
<p>

```json
{
  "vars": {
    "prefix": "/tmp"
  },
  "tasks": [
    {
      "run": "gafferScene",
      "metadata": {
        "match.types": [
          "png"
        ],
        "match.vars": {
          "imageType": [
            "sequence"
          ]
        }
      },
      "options": {
        "scene": "{configDirectory}/scene.gfr"
      },
      "target": "{prefix}/gafferBlurImageSequence/(newver <parent> as <ver>)/{name}_<ver>.(pad {frame} 6).exr",
      "tasks": [
        {
          "run": "ffmpeg",
          "options":{
            "frameRate": 23.976,
            "sourceColorSpace": "bt709",
            "targetColorSpace": "smpte170m"
          },
          "target": "(dirname {filePath})/{name}.mov"
        }
      ]
    }
  ]
}
```
</details>

Additionally you can run Kombi from

<details><summary>Python</summary>
<p>

```python
# TODO
```
</details>

<details><summary>Gaffer (node-based)</summary>
<p>

```
coming soon
```
</details>

### Supported platforms
- Linux
- windows
> mac os: Although running it on mac os is possible, I don't have an apple machine for troubleshooting and officially support it on this system.

### Requirement
Python 3.5+/2.7+ 

### Optional Dependencies
Name | Version
--- | ---
PySide | 2.0+

### Optional Integrations
Name | Version
--- | ---
Open Image IO (python bindings) | 1.7+
Open Color IO (python bindings) | 1.0+
Gaffer | 0.53+
FFmpeg | 3.0+
nuke | 9.0+
maya | 2016+

## Installation

In case you are building the dependencies manually skip the step below:

### Install dependencies

<details><summary>Linux</summary>
<p>

#### Ubuntu and derivatives:
```bash
pip install PySide2
apt-get install make cmake
apt-get install python-openimageio openimageio-tools
apt-get install python-pyopencolorio 
apt-get install ffmpeg
```

#### CentOS/Fedora (requires EPEL):
```bash
pip install PySide2
yum install make cmake
yum install python-OpenImageIO OpenImageIO-utils
yum install ffmpeg
```
</details>

<details><summary>windows</summary>
<p>

- [Cygwin](https://www.cygwin.com)
- [Python 3.6](https://www.python.org/downloads)
- [FFmpeg](https://ffmpeg.org)
- [PySide2](https://pypi.org/project/PySide2)
- [Open Image IO](https://www.lfd.uci.edu/~gohlke/pythonlibs/#openimageio) (Unofficial)

</details>

### Download and unzip the release
```
# TODO
```

## Building Kombi for development

<details><summary>Details</summary>
<p>
    
> For windows users please make sure you have the posix tools available on your system. It can be done through [Cygwin](https://www.cygwin.com).

#### Dependencies
Name | Version 
--- | --- 
CMake | 2.8+
Make | 3.0+
Pylama | 7.0+

#### Running tests
```bash
cd <SRC_LOCATION>
./runtests
```

#### Running linters
```bash
cd <SRC_LOCATION>
./runlint
```

#### Building Kombi

```bash
cd <SRC_LOCATION>
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<TARGET_LOCATION> -G "Unix Makefiles" ..
make all install
```

</details>

## Running 
The launchers are provided inside of the "bin" directory found inside of the installation.

Kombi command-line:
```bash
kombi --help
```

Kombi file picker tool (PySide2):
```bash
kombi-gui
```
<img src="data/doc/kombi-gui-screenshot.png"/>

## Licensing
Kombi is free software; you can redistribute it and/or modify it under the terms of the MIT License
